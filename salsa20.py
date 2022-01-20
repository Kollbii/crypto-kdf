'''
Funkcja Ćwierć-Rundy
Przesunięcie cykliczne w lewo. Ważna kolejność!
Operacja add-rotate-XOR
'''
def QR(a, b, c, d):
    b = b ^ rot_left_32((a + d) & 0xffffffff, 7)
    c = c ^ rot_left_32((b + a) & 0xffffffff, 9)
    d = d ^ rot_left_32((c + b) & 0xffffffff, 13)
    a = a ^ rot_left_32((d + c) & 0xffffffff, 18)


'''
Funkcja pomocnicza - przesunięcie cykliczne w lewo
'''
def rot_left_32(a, b):
    return ((( a << b ) & 0xffffffff) | (a >> (32 - b)))


'''
Funkcja pomocnicza - transpozycja macierzy
'''
def transpose(state):
    state =[state[0],state[4],state[8],state[12],
            state[1],state[5],state[9],state[13],
            state[2],state[6],state[10],state[14],
            state[3],state[7],state[11],state[15]]
    return state


'''
Funkcja pomocnicza - XOR na macierzy 4x4
'''
def xor_block(b1, b2):
    return [b1[i]^b2[i] for i in range(16)]


'''
Zwróć macierze 4x4 dla wiadomości odpowiedniej długości. (Bez obsługi paddingu!)
'''
def message_to_blocks(message):
    message_blocks = []
    for b in range(int(len(message)/64)):
        message_blocks.append([littleendian(message[64*b + 4*i : 4*i + 4 + 64*b]) for i in range(16)])
    return message_blocks


'''
Pełna runda to:
4 Ćwierć-Rundy (QR) -> transpozycja -> 4 Ćwierć-Rundy (QR) -> transpozycja

My dla czytelności implementujemy półrundy:
4 Ćwierć-Rundy -> transpozycja
Dlatego muszą zostać wykonane "dwukrotnie" na każde wykonanie
'''
def round(state):
    QR(state[0],state[4],state[8], state[12])
    QR(state[1],state[5],state[9], state[13])
    QR(state[2],state[6],state[10], state[14])
    QR(state[3],state[7],state[11], state[15])

    new_state = transpose(state)
    return new_state


''' 
key - musi być długości 16 lub 32 bajtów
nuo - nonce (number used once) - unikalna liczba dla każdej wiadomości 2x4bytes
msg - wiadomość
con - stały ciąg znaków o wartości "expand 32 byte k"
'''
def salsa20(key, nuo, ctr):
    # Zamienione bajty na liczby:
    #     ['expa'    , 'nd 3'    , '2 by'    , 'te k']
    con = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
    key = [littleendian(key[4*i:4*i+4]) for i in range(8)]
    nuo = [littleendian(nuo[4*i:4*i+4]) for i in range(2)]
    ctr = [littleendian(ctr[4*i:4*i+4]) for i in range(2)]

    # Stan pierwotny
    init_state = [
        con[0], key[0], key[1], key[2],
        key[3], con[1], nuo[0], nuo[1],
        ctr[0], ctr[1], con[2], key[4],
        key[5], key[6], key[7], con[3]
    ]
    
    # Ilość rund może zostać zmieniona, w Salsa20/8 odbywa się 8 rund
    new_state = round(init_state) # Pierwsza runda
    for _ in range(15): # pozostałe rundy  (nasz kod dla czytelności implementuje pół-rundy, stąd 15)
        new_state = round(new_state)

    # Na koniec dodajemy całą przekształconą tablicę 16 słów do oryginalnej
    state = [(new_state[i] + init_state[i]) & 0xffffffff for i in range(16)]

    # Zwracamy dodane tablice
    return state


'''
Funkcja pomocnicza - Zmiana kolejności bajtów na Little Endian
'''
def littleendian(bytes):
     # przykład: 0x4A3B2C1D ==> [1D, 2C, 3B, 4A]
    return bytes[0] ^ (bytes[1] << 8) ^ (bytes[2] << 16) ^ (bytes[3] << 24)


if __name__ == '__main__':
    print("Testowanie poprawności implementacji:")

    # Wybierz klucz
    key="10101110100001010000001001111010"
    key=[int(i) for i in key]
    assert len(key) == 32

    # Podaj nonce
    nonce = [0,1,3,3,7,6,9,4]
    assert len(nonce) == 8

    # Inicjowanie licznika
    counter = [0,0,0,0,0,0,0,0]
    assert len(counter) == 8

    # Wiadomość (128 bitowa)
    message = "10001110111110101110101011010000101010001101001011111111100111011100111011100110111010101101211110101010110100101001111110011101"
    assert len(message) == 128
    
    # Zamień wiadomość na bloki po 16 znaków.
    # Dla wiadomości długości 128 każda komórka po 4 powinna mieć 2 bloki.
    message = [int(i) for i in message]
    message_blocks = message_to_blocks(message)
    assert len(message_blocks) == 2

    print('Test kodowania i dekodowania dla wiadomości długości 128 dla 2 bloków')
    print('Oryginalne bloki wiadomości')
    print(message_blocks[0])
    print(message_blocks[1])
    cipher_msg = []
    for i in range(2):
        counter[0] += 1
        block = salsa20(key, nonce, counter)
        cipher_msg.append(xor_block(block, message_blocks[i]))

    print('Zakodowane bloki')
    print(cipher_msg[0])        
    print(cipher_msg[1])      


    # Reset licznika przed dekodowaniem
    counter = [0]*8

    origin_msg = []
    for i in range(2):
        counter[0] += 1
        block = salsa20(key, nonce, counter)
        origin_msg.append(xor_block(block, cipher_msg[i]))

    print('Dekodowane bloki')
    print(origin_msg[0])
    print(origin_msg[1])
    print("Są równe?", origin_msg == message_blocks)