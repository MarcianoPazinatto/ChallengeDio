import re

from Customer import Customer


class CustomersDatabase:
    def __init__(self):
        self.all_customers = list()

    def add_customers(self, customer: dict):
        self.all_customers.append(customer)

    def create_customer(self, name, date_of_birth, cpf, address):
        if not self.validate_cpf_customer_exist(cpf):
            customer = Customer(name, date_of_birth, cpf, address)
            customer.create_obj_customer()
            self.add_customers(customer.customer_info)
            return print("Usuario cadastrado com sucesso")
        return print("Este Cpf já conta na base de usuarios")

    def locate_customer(self, cpf):
        cpf = re.sub(r'[^0-9]', '', cpf)
        for customer in self.all_customers:
            if customer.get("cpf") == cpf:
                return customer
        return print("usuario não encontrado")

    def validate_cpf_customer_exist(self, cpf):
        for customer in self.all_customers:
            if customer.get("cpf") == cpf:
                return True
        return False

    def create_user(self):
        name = input("Digite o nome completo:")
        date_of_birth = input("Digite a data de nascimento(dia/mês/ano):")
        cpf = input("Digite o CPF(apenas numeros):")
        address = input("Digite o endereço completo (Rua, nº, bairro, cidade, estado, e país):")
        self.create_customer(name=name, date_of_birth=date_of_birth, cpf=cpf, address=address)
