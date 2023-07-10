from x01_02_task import check_string

# return NO   "Dog", "pet", "music", "Funny meme", "Listen to this"


def test_returns_no():
    assert check_string("pet is dead") == "NO!"
    assert check_string("dog is dead") == "NO!"
    assert check_string("music is dead") == "NO!"
    assert check_string("Funny Meme is dead") == "NO!"
    assert check_string("Listen to this") == "NO!"


def test_returns_safe_watching():
    assert check_string("oalala listen") == "Safe watching!"
    assert check_string("nothing to see here") == "Safe watching!"
    assert check_string("totally empty") == "Safe watching!"

