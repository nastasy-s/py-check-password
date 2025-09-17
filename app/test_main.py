# write your code here
import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "pwd",
    [
        "Pass@word1",
        "A1$bcdef",              # рівно 8
        "A1$bcdefghijklmn",      # рівно 16
        "Good_Pass1-",
    ],
)
def test_check_password_valid(pwd: str) -> None:
    assert check_password(pwd) is True


@pytest.mark.parametrize(
    "pwd",
    [
        "qwerty",                # приклад з умови
        "Str@ng",                # приклад з умови (надто короткий)
        "A1$bcde",               # 7 символів
        "A1$bcdefghijklmnop",    # >16
        "Password$",             # немає цифри
        "Password1",             # немає спецсимволу
        "password1$",            # немає великої літери
        "Pass^word1$",           # заборонений символ ^
        "Pass word1$",           # пробіл заборонений
        "Passwörd1$",            # нелітерний латинський символ
    ],
)
def test_check_password_invalid(pwd: str) -> None:
    assert check_password(pwd) is False
