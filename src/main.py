from streptococcus_oralis.strepto import Strepo
from streptococcus_oralis.oralis import Oralis

'''
Streptococcus Oralis
Short name: strepos(?) storalis(?) strepolis(?) <-- bardzo grecko
'''

if __name__ == "__main__":
    s = Strepo()
    o = Oralis()

    print(s, o)

    from hashlib import sha256
    print(sha256(b"password").digest().hex())