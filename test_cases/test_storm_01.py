import pytest


class TestStorm01(object):
    @pytest.mark.L1
    def test_01(self):
        print("aaa")
        assert "a" == "a"


# if __name__ == '__main__':
#     pytest.main(["-s", "test_storm_01.py"])
