import re


class Account:
    def __init__(self, account_number, cpf_customer):
        self.agency = "0001"
        self.account_number = account_number
        self.cpf_customer = cpf_customer
        self.account_info = dict()

    def create_obj_account(self):
        self.account_info.clear()
        self.account_info = {
            "agency": self.agency,
            "account_number": self.account_number,
            "cpf_customer": self.cpf_customer,
            "balance": 0.00,
            "extract": []
        }
