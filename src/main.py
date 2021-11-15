from johny_bravo.johny import Johny
from johny_bravo.bravo import Bravo


'''
Streptococcus Oralis / Johny Bravo

KDF Johny-Bravo inspirowany scryptem. Program ćwiczący dokładniejsze zrozumienie
jak działają funkcje wyprowadzania klucza.
'''

if __name__ == "__main__":
    j = Johny(16)
    b = Bravo("crypto", "NaCl", 8, 4, 32)
    b()

    # print(j, b)
    # print(j._blonde16('', 'CryptoIsFun'))
    # print(j + b)
    # j._initial_state()