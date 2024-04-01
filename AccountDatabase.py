import re

from Account import Account


class AccountDatabase:
    def __init__(self):
        self.all_accounts = list()

    def add_account(self, customer: dict):
        self.all_accounts.append(customer)

    def create_account(self, cpf_customer, customer_db):
        customer = customer_db
        if customer.validate_cpf_customer_exist(cpf_customer):
            account_number = self.get_last_account()
            account = Account(account_number, cpf_customer)
            account.create_obj_account()
            self.add_account(account.account_info)
            return print("Conta cadastrada com sucesso")
        return print(f"Cliente com o cpf: {cpf_customer} não encontrado, não foi possível criar a conta")

    def get_last_account(self):
        numbers_account = [account.get('account_number', 0) for account in self.all_accounts]
        biggest_account = max(numbers_account) if numbers_account else 0
        return biggest_account + 1

    def locate_account_with_cpf(self, cpf):
        cpf = re.sub(r'[^0-9]', '', cpf)
        for customer in self.all_accounts:
            if customer.get("cpf_customer") == cpf:
                return customer
        return print("usuario não encontrado")

    def sacar(self, cpf_sought, new_balance):
        for dict_account in self.all_accounts:
            if dict_account.get('cpf_customer') == cpf_sought:
                if dict_account['balance'] - new_balance >= 0:
                    dict_account['extract'].append(f"Saldo {dict_account['balance']}")
                    dict_account['balance'] -= new_balance
                    dict_account['extract'].append(f"Saque de {new_balance}")
                    dict_account['extract'].append(f"Saldo {dict_account['balance']}")
                    return print("Saque realizado com sucesso")
                return print("Saldo insuficiente para a operação")
            else:
                print("Conta não encontrada")

    def depositar(self, cpf_sought, new_balance):
        for dict_account in self.all_accounts:
            if dict_account.get('cpf_customer') == cpf_sought:
                dict_account['extract'].append(f"Saldo {dict_account['balance']}")
                dict_account['balance'] += new_balance
                dict_account['extract'].append(f"Deposito de {new_balance}")
                dict_account['extract'].append(f"Saldo {dict_account['balance']}")
                return print("Deposito realizado com sucesso")
            return print("Conta não encontrada")

    # def extrato(self, cpf_sought):
    #     for dict_account in self.all_accounts:
    #         if dict_account.get('cpf_customer') == cpf_sought:
    #             for operation in dict_account["extract"]:
    #                 print(operation + "\n")
    #             return print(f"Saldo da conta {dict_account['account_number']}, R${dict_account['balance']}")
    #         else:
    #             return print("Conta não encontrada")

    def extrato(self, cpf_sought):
        for dict_account in self.all_accounts:
            if dict_account.get('cpf_customer') == cpf_sought:
                if 'extract' in dict_account and len(dict_account['extract']) > 0:
                    print("\n================ EXTRATO ================")
                    for operation in dict_account["extract"]:
                        print(operation + "\n")
                    print("==========================================")
                    return print(f"Saldo da conta {dict_account['account_number']}, R${dict_account['balance']}")
                else:
                    print("\n================ EXTRATO ================")
                    print("A conta possui um histórico de operações vazio.")
                    print(f"Saldo da conta {dict_account['account_number']}, R${dict_account['balance']}")
                    return print("==========================================")
        return print("Conta não encontrada")

    def create_account_user(self, customer_db):
        cpf = input("Digite o CPF do cliente(apenas numeros):")
        self.create_account(cpf_customer=cpf, customer_db=customer_db)
