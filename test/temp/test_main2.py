from temp import main2


def test_split():
    napis = "54545454545; dsadadsadad; hahahaha; 5.32"
    assert main2.split(napis, ";") == napis.split(";")
