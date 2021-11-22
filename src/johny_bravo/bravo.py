from hmac import HMAC, digest
from hashlib import sha256

class Bravo(object):
    '''Hash for Johny class'''
    def __init__(self, password, salt, N, r, dkLen, p=False,):
        #TODO: Better validation
        self._password = password
        self._salt = salt
        if N < 2 or (N & (N- 1)): raise ValueError("N must be a power of 2 and > 1")
        self._N = N
        self.rounds = r
        self.para = p
        self.dkLen = dkLen

    def __call__(self):
        print("Called with {} {}".format(self._password, self._N))
        PRF = lambda k, m: HMAC(key=k, msg=m, digestmod=sha256()).digest()

        # Converting to intigers


    def __str__(self):
        return "Implement Bravo class"