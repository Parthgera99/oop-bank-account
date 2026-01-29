import pytest
from bank_account import BankAccount


def test_initial_balance():
    account = BankAccount("Alice")
    assert account.get_balance() == 0.0


def test_deposit():
    account = BankAccount("Bob")
    account.deposit(100)
    assert account.get_balance() == 100


def test_withdraw():
    account = BankAccount("Charlie", 200)
    account.withdraw(50)
    assert account.get_balance() == 150


def test_withdraw_insufficient_balance():
    account = BankAccount("Dave", 50)
    with pytest.raises(ValueError):
        account.withdraw(100)
