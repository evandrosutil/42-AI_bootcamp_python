class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):

    def __init__(self):
        self.account = []

    def _check_corrupted(self, account):
        """
        Checks if an account is corrupted.

        Note:
            A bank account is corrupted when:
                * has an even number of attributes.
                * has an attribute starting with b.
                * has no attribute starting with zip or addr.
                * has no attribute name, id and value.

        Args:
            account (Account): account to be checked.

        Returns:
            bool: False if the account is invalid or corrupted. True otherwise.
        """
        acc = self.get_account(account)
        if not acc:
            return True
        attrs = vars(acc)
        if len(attrs) % 2 == 0:
            print('len')
            return True
        b_attr = [attr for attr in attrs if attr.lower().startswith('b')]
        if b_attr:
            return True
        if not any(attr.startswith(('zip', 'addr')) for attr in attrs):
            return True
        if not all(attr in vars(acc) for attr in ['id', 'name', 'value']):
            return True

    def add(self, account):
        if isinstance(account, Account):
            self.account.append(account)
        else:
            print('Invalid account.')

    def fix_account(self, account):
        """
        Tries to fix a corrupted account.

        Args:
            account (int or str): id or str of the account.

        Returns:
            bool: True if sucess, False if an error occured.
        """
        acc = self.get_account(account)
        b_attrs = [b for b in vars(acc) if b.lower().startswith('b')]
        for attr in vars(acc):
            if attr in b_attrs:
                new_name = attr[1:]
                acc.__dict__[new_name] = acc.__dict__.pop(attr)
        
        if 'name' not in vars(acc):
            acc.__dict__['name'] = 'John Doe'
        
        if 'value' not in vars(acc):
            acc.__dict__['value'] = 0
         
        if not any(attr in vars(acc) for attr in ('zip', 'addr')):
            acc.__dict__['zip'] = '00000-000'
        while len(vars(acc).keys()) % 2 == 0:
            acc.__dict__['fix_attr'] = None
        
        return self._check_corrupted(acc.id)

    def get_account(self, identifier):
        if isinstance(identifier, int):
            for account in self.account:
                if account.id == identifier:
                    return account
        elif isinstance(identifier, str):
            if identifier.isdigit():
                for account in self.account:
                    if account.id == int(identifier):
                        return account
            for account in self.account:
                if account.name == identifier:
                    return account
        else:
            print(
                'Invalid data type. Account identifier must be an id or name')
            return False

    def transfer(self, origin, dest, amount):
        """
        Transfer a given amount from one account (origin) to another (dest)

        Args:
            origin (int or str): id or name of the first account.
            dest (int or str): id or name of the destination account.
            amount (float): amount to transfer.

        Returns
            bool: True if success, False if an error occured.
        """
        origin_acc = self.get_account(origin)
        dest_acc = self.get_account(dest)
        if not origin_acc:
            print(f'{origin} account is not valid')
            return False
        elif not dest_acc:
            print(f'{dest} account is not valid')
            return False
        if self._check_corrupted(dest_acc.id):
            print('Invalid Transaction: destination account is corrupted.')
            return False
        if amount < 0:
            print('Invalid transaction: cannot transfer negative values.')
        elif origin_acc.value - amount < 0:
            print('Invalid transaction: unsufficient funds.')
            return False

        origin_acc.transfer(amount * -1)
        dest_acc.transfer(amount)
        print('Transaction completed.')
        return True
