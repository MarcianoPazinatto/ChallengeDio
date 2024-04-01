import re


class Customer:
    def __init__(self, name, date_of_birth, cpf, address):
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf
        self.address = address
        self.customer_info = dict()

    def cpf_adjust(self):
        return re.sub(r'[^0-9]', '', self.cpf)

    def create_obj_customer(self):
        self.customer_info.clear()
        self.cpf_adjust()
        self.customer_info = {
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "cpf": self.cpf,
            "address": self.address,
        }


