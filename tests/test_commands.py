import unittest
from kb.commands import add
from kb.config import DEFAULT_CONFIG
from kb.main import main
from pathlib import Path


def test_add_check_file_created_on_destination():
    add.add(args={
        "title":"test_title", # required
        "file":"", # required
        "category":"Journey,Notes",
        "tags":"",
        "author":"jhon doe",
        "status":"",
        "body":"",
        "template": "blog"}, config=DEFAULT_CONFIG)
    want = "~/.kb/default/test_title"
    got = str(Path(want))

    assert got == want