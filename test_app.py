# test_app.py

import pytest
from app import get_message

class TestGetMessage:

    def test_default(self):
        assert get_message() == "🚀 Hello, world!"

    def test_custom_name(self):
        assert get_message("Abhi") == "🚀 Hello, Abhi!"

    def test_empty_name_raises(self):
        with pytest.raises(ValueError):
            get_message("")

    def test_none_raises(self):
        with pytest.raises(ValueError):
            get_message(None)
