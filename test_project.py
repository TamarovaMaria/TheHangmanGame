from project import get_help, is_it_letter, get_level
import pytest

def test_get_help():
    assert get_help("utopia") == "A perfect society in which people work well with each other and are happy."
    assert get_help("indigo") == "A bluish-purple colour."
    assert get_help("balsam") == "A pleasant-smelling substance used as the base for medical or beauty treatments."

def test_is_it_letter():
    assert is_it_letter("a") == True
    with pytest.raises(ValueError):
        is_it_letter("1")
    with pytest.raises(ValueError):
        is_it_letter("utopia")

def test_get_level():
    assert get_level("easy") == 0
    assert get_level("mid") == 1
    assert get_level("hard") == 2


if __name__ == "__main__":
    main()
