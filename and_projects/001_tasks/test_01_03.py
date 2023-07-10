
from x01_03_task import hacker_speak


def test_returns_correct_hacker_speak():
    assert hacker_speak("everything everyhere all at once") == "3v3ryth1ng 3v3ryh3r3 4ll 4t 0nc3"
    assert hacker_speak("abcdefghijklmnopqrstuvwxyz") == "4bcd3fgh1jklmn0pqr5tuvwxyz"

