from project import add_bullet_points, add_date, save_to_clipboard
from datetime import date
import pyperclip


def test_add_bullet_points():
    assert add_bullet_points("I am Omar") == "- I am Omar"


def test_add_date():
    today_date = str(date.today())
    assert add_date("Lecture Notes") == f"{today_date}\nLecture Notes"


def test_save_to_clipboard():
    save_to_clipboard("Thank you Harvard for this outstanding course!")
    assert pyperclip.paste() == "Thank you Harvard for this outstanding course!"
