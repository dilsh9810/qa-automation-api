from Main import getgrades

def test_getgrades():
    assert getgrades(75) == "Excellent"
    assert getgrades(40) == "Pass"
    