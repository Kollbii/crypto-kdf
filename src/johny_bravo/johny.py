from typing import List
from johny_bravo.bravo import Bravo

'''
Look here for inspirations: https://courses.csail.mit.edu/6.857/2016/files/salsa20.py
'''
class Johny(object):
    ROUNDS=16
    def __init__(self, key, iv = '\x00'*8, rounds: int = ROUNDS):
        pass

    def _key_setup(self, key):
        '''Convert key to list of 4-byte unsigned intigers (32-bits)'''
        pass

    def ROTL(self, a, b):
        '''Do some bitwise shifts'''
        pass

    def QR(self, a, b, c, d):
        '''Do some xoring'''
        pass

    def blonde16_block(self, out, inp):
        x = ['\u0000' for _ in range(16)] # fill with 0s

        for i in range(0, 16):
            pass

        for i in range(0, self.ROUNDS, 2):
            pass

        for i in range(0, 16):
            pass

        return out

    def __str__(self):
        return "Implement Johny class"

    def __add__(self, bravo: Bravo):
        return "[JBH] Johny Bravo hash"