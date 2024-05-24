from sistema_database import SistemaDatabase

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class TeacherCLI(SimpleCLI):
    def __init__(self, sistema_database: SistemaDatabase):
        super().__init__()
        self.sistema_database = sistema_database
        self.add_command("create", self.create_Teacher)
        self.add_command("read", self.read_Teacher)
        self.add_command("update", self.update_Teacher)
        self.add_command("delete", self.delete_Teacher)

    def create_Teacher(self):
        name = input('Nome: ')
        ano_nasc = input('Ano de nascimento: ')
        cpf = input('Cpf: ')

        self.sistema_database.create_Teacher(name, ano_nasc, cpf)

        print('Professor criado!')

    def read_Teacher(self):
        name = input('Nome: ')

        teacher = self.sistema_database.get_Teacher(name)

        if teacher:
            print('Professor encontrado:')
            for key, value in teacher.items():
                print(f'{key}: {value}\n')
        else:
            print('Professor não encontrado!')

    def update_Teacher(self):
        name = input('Nome: ')
        newCpf = input('Novo CPF: ')

        teacher = self.sistema_database.update_Teacher(name, newCpf)

        if teacher:
            print('Professor atualizado:')
            for key, value in teacher.items():
                print(f'{key}: {value}\n')
        else:
            print('Professor não encontrado!')

    def delete_Teacher(self):
        nome = input("Nome: ")
        self.sistema_database.delete_Teacher(nome)

        print('Professor deletado')

    def run(self):
        print("Bem-vindo ao teacher CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()