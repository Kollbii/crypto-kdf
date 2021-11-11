from src.streptococcus_oralis.oralis import Oralis
from src.streptococcus_oralis.strepto import Strepo

class Test_Implementation:
    global s, o
    s = Strepo()
    o = Oralis()
    
    def test_representation(self):
        assert s.__str__() == "Implement STREPO class"
        assert o.__str__() == "Implement ORALIS class"
