

# Fajniej to zrobić jako klase ale w jupiterze wsyzstko jest globalne więc tak zostanie na chwile tutaj
''' 
key - must be 16 or 32 bytes
nuo - nounce (number used once) - uniqe number for each msg 2x4bytes
msg - message
con - constant msg with values of string "expand 32 byte k"
'''
def salsa20(key, nuo, ctr):
    #     ['expa'    , 'nd 3'    , '2 by'    , 'te k']
    con = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
    key = [littleendian(key[4*i:4*i+4]) for i in range(8)]
    nuo = [littleendian(nuo[4*i:4*i+4]) for i in range(2)]
    ctr = [littleendian(ctr[4*i:4*i+4]) for i in range(2)]

    # print("Constant", con)
    # print("Key\t", key)
    # print("Nounce\t", nuo)
    # print("Counter\t", ctr)

    init_state = [
        con[0], key[0], key[1], key[2],
        key[3], con[1], nuo[0], nuo[1],
        ctr[0], ctr[1], con[2], key[4],
        key[5], key[6], key[7], con[3]]
    
    # Number of rounds can be changed
    new_state = round(init_state) # Initial round 1
    for _ in range(19):
        new_state = round(new_state)

    state = [(new_state[i] + init_state[i]) & 0xffffffff for i in range(16)]

    return state


'''4 QR for collumns -> transposition -> 4 QR for rows -> repeat'''
def round(state):
    QR(state[0],state[4],state[8], state[12])
    QR(state[1],state[5],state[9], state[13])
    QR(state[2],state[6],state[10], state[14])
    QR(state[3],state[7],state[11], state[15])

    new_state = transpose(state)
    return new_state

'''Transpose matrix - swap columns and rows'''
def transpose(state):
    state =[state[0],state[4],state[8],state[12],
            state[1],state[5],state[9],state[13],
            state[2],state[6],state[10],state[14],
            state[3],state[7],state[11],state[15]]
    return state

'''
Quarter-Round function.
Bitwise left. Sequence matters!!
Performing add-rotate-XOR operation.
'''
def QR(a, b, c, d):
    b = b ^ rot_left_32((a + d) & 0xffffffff, 7)
    c = c ^ rot_left_32((b + a) & 0xffffffff, 9)
    d = d ^ rot_left_32((c + b) & 0xffffffff, 13)
    a = a ^ rot_left_32((d + c) & 0xffffffff, 18)

def rot_left_32(a, b):
    return ((( a << b ) & 0xffffffff) | (a >> (32 - b))) # 0xffffffff 32 byte mask

def littleendian(bytes):
    return bytes[0] ^ (bytes[1] << 8) ^ (bytes[2] << 16) ^ (bytes[3] << 24) # ex. 0x4A3B2C1D ==> [1D, 2C, 3B, 4A]

'''Perform XOR operation for 4x4 matrix'''
def xor_block(b1, b2):
    return [b1[i]^b2[i] for i in range(16)]

'''Return 4x4 matrixs of messages of given length. Padding not included. Blank spaces'''
def message_to_blocks(message):
    message_blocks = []
    for b in range(int(len(message)/64)):
        message_blocks.append([littleendian(message[64*b + 4*i : 4*i + 4 + 64*b]) for i in range(16)])
    return message_blocks

if __name__ == '__main__':
    print("Testing output. Can be imported as module.")

    # Pick key
    key="10101110100001010000001001111010"
    key=[int(i) for i in key]
    assert len(key) == 32

    # Gener random number
    nounce = [0,1,3,3,7,6,9,4]
    assert len(nounce) == 8

    # Counter
    counter = [0,0,0,0,0,0,0,0]
    assert len(counter) == 8

    # Message
    message = "10001110111110101110101011010000101010001101001011111111100111011100111011100110111010101101211110101010110100101001111110011101"
    assert len(message) == 128
    
    # Convert message to blocks of 16. For msg of len 128 each cell of 4 should be 2 blocks.
    message = [int(i) for i in message]
    message_blocks = message_to_blocks(message)
    assert len(message_blocks) == 2

    print('Test encoding and decoding for message of len=128 for 2 blocks')
    print('Original msg blocks')
    print(message_blocks[0])
    print(message_blocks[1])
    cipher_msg = []
    for i in range(2):
        counter[0] += 1
        block = salsa20(key, nounce, counter)
        cipher_msg.append(xor_block(block, message_blocks[i]))

    print('Encoded blocks')
    print(cipher_msg[0])        
    print(cipher_msg[1])      


    # Reset counter before decoding
    counter = [0]*8

    origin_msg = []
    for i in range(2):
        counter[0] += 1
        block = salsa20(key, nounce, counter)
        origin_msg.append(xor_block(block, cipher_msg[i]))

    print('Decoded blocks')
    print(origin_msg[0])
    print(origin_msg[1])
    print("Are equal?", origin_msg == message_blocks)

    # TODO: Do przemyslenia czy countera nie lepiej wrzucić jakoś do środka. Ale tak wydaje mi się wszystko czytelniejsze.
    # Wiadomość wyżej, która jest "binarna" to tak nie do końca ale dla samej ideii może zostać. W końcu mamy tylko pokazać o co kaman.