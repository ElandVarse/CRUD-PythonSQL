from actions.add_user import add_user
from actions.list_users import list_users
from actions.update_user import update_email
from actions.delete_user import delete_user
from db.db_setup import setup_database

def main():
    setup_database()  # Cria o banco se não existir

    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar email")
        print("4 - Deletar usuário")
        print("5 - Sair")

        option = input("\nEscolha uma opção: ")

        if option == '1':
            name = input("\nDigite o nome: ")
            email = input("Digite o email: ")
            password = input("Digite a senha: ")
            add_user(name, email, password)

        elif option == '2':
            list_users()

        elif option == '3':
            try:
                user_id = int(input("\nDigite o ID do usuário a atualizar: "))
                new_email = input("Digite o novo email: ")
                update_email(user_id, new_email)
            except ValueError:
                print("\nID inválido. Digite um número inteiro.")

        elif option == '4':
            try:
                user_id = int(input("\nDigite o ID do usuário a deletar: "))
                delete_user(user_id)
            except ValueError:
                print("\nID inválido. Digite um número inteiro.")

        elif option == '5':
            print("\nSaindo... 👋")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
