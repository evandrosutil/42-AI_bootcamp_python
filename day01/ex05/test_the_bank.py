import unittest

from the_bank import Account, Bank


class BankAccountTest(unittest.TestCase):

    def test_transfer(self):
        bank = Bank()
        bank.add(Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31',
            )
        )
        bank.add(Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation',
            )
        )

        self.assertFalse(bank.transfer('William John', 'Smith Jane', 545.0))

    def test_insufficient_funds_transfer(self):
        bank = Bank()
        bank.add(Account(
            'Andrezinho',
            zip='12345-000',
            value = 20.0,
            ref='21313213ac231de2131310128abd1231',
            )
        )
        bank.add(Account(
            'Vadinho',
            zip='0000-000',
            vaue=450.0,
            ref='12313312cacb12122c1b12ac212b21',
            )
        )
        self.assertFalse(bank.transfer(1, 2, 1000.0))

    def test_fix_account(self):
        bank = Bank()
        bank.add(Account(
            'Claumirzinho',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
            )
        )
        bank.add(Account(
            'Marquinhos Pato',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info= None
            )
        )

        self.assertFalse(bank.transfer('Marquinhos Pato', 'Claumirzinho', 1000.0))

        bank.fix_account('Claumirzinho')
        bank.fix_account('Marquinhos Pato')

        self.assertTrue(bank.transfer('Marquinhos Pato', 'Claumirzinho', 1000.0))
