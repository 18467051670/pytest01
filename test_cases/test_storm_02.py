import pytest


class TestStorm02(object):
    @pytest.mark.L2
    def test_02(self):
        print("bbb")
        assert "b" == "b1"


