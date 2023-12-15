import pytest
from snd_chapter_11 import validate_password
 
class TestPasswordValidator:
    def test_valid_password(self):
        assert validate_password("A1b2C3d4!")
        assert validate_password("R2$d5@Fg!")
 
#ADD additional test cases as part of this question!
 
if __name__ == '__main__':
    pytest.main()