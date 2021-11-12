from src.johny_bravo.johny import Johny
from src.johny_bravo.bravo import Bravo

class Test_Implementation:
    global j, b
    j = Johny()
    b = Bravo()
    
    def test_representation(self):
        assert j.__str__() == "Implement Johny class"
        assert b.__str__() == "Implement Bravo class"
