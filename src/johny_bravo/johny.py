from johny_bravo.bravo import Bravo

'''
Look here for inspirations: 
https://courses.csail.mit.edu/6.857/2016/files/salsa20.py
https://github.com/Daeinar/salsa20/blob/master/salsa.py
https://github.com/csarron/mdict-analysis/blob/master/pureSalsa20.py
'''
class Johny(object):
    def __init__(self, key = [0]*32, rounds: int = 16):
        #TODO: Unpacking, validations etc.
        self._key = key
        self._rounds = rounds
        self._mask = 0xffffffff # 32-bit mask

    def _initial_state(self):
        '''
        Make initial state similarly to Salsa20
        c - fixed constant words 
        k - key
        n - nounce
        p - stream position
        '''
        c = [int("brav", 32), int("otoo", 32), int("much", 32), int("cool", 32)]
        k = []
        n = []
        p = []

        # self._state =  [c[0], k[0], k[1], k[2], 
        #                 k[3], c[1], n[0], n[1],
        #                 p[0], p[1], c[2], k[4], 
        #                 k[5], k[6], k[7], c[3]]

        # return self._state

    def _littleendian(self, b):
        assert len(b) == 4
        return b[0] ^ (b[1] << 8) ^ (b[2] << 16) ^ (b[3] << 24)

    def _key_setup(self, key):
        '''Convert key to list of 4-byte unsigned intigers (32-bits)'''
        pass

    def _rotl(self, a, b):
        '''Do some bitwise shifts'''
        return (( (a << b) & self._mask | (a >> (32 - b)) ))

    def _qr(self, a, b, c, d):
        '''Do some xoring'''
        pass

    def _blonde16(self, out, inp):
        return out

    def __str__(self):
        return "Implement Johny class"

    def __add__(self, bravo: Bravo):
        return "[JBH] Johny Bravo hash"