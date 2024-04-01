import textwrap

from AccountDatabase import AccountDatabase
from CustomersDatabase import CustomersDatabase

customer = CustomersDatabase()
account = AccountDatabase()


def menu():
    menu = """\n
            *******\\  New Bank  //*******
            Digite o valor para a operação:
            [1]\tNovo Usuário
            [2]\tNova Conta
            [3]\tDepositar
            [4]\tSacar
            [5]\tExtrato
            [0]\tSair        
            ---------------> """
    return input(textwrap.dedent(menu))


while True:

    opcao = menu()

    if opcao == "1":
        print("Criando novo usuário")
        customer.create_user()

    elif opcao == "2":
        print("Criando nova conta")
        account.create_account_user(customer)

    elif opcao == "3":
        cpf = input("Informe o cpf do usuario para depósito")
        value = float(input("Informe o valor do depósito: "))
        account.depositar(cpf_sought=cpf, new_balance=value)

    elif opcao == "4":

        cpf = input("Informe o cpf do usuario para saque")
        value = float(input("Informe o valor do saque: "))
        account.sacar(cpf_sought=cpf, new_balance=value)

    elif opcao == "5":
        cpf = input("Informe o cpf do usuario para extrato")
        account.extrato(cpf_sought=cpf)

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
