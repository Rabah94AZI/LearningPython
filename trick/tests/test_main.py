from trick.main import maxi


def test_maxi():
    assert maxi(10, 5, 3) == 10
    assert maxi(2, 8, 4) == 8
    assert maxi(1, 3, 9) == 9