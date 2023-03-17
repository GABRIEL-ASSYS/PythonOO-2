import sys
from notebook import Notebook

class Menu:
    """
    Mostra para o usuário as opções para serem rodadas
    """

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes, # mostrar anotações
            "2": self.search_notes, # pesquisar anotações
            "3": self.add_notes, #adicionar notas
            "4": self.modify_notes, # modifica notas
            "5": self.quit # sair do menu
        }

    def display_menu(self):
        print("""
            1. Mostrar todas as anotações
            2. Pesquisar anotações
            3. Adicionar anotações
            4. Modificar anotações
            5. Sair
        """
        )

    def run(self):
        """
        Mostra o menu e responde a uma escolha.
        """

        while True:
            self.display_menu()
            choice = input("Digite a sua escolha: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} não é uma opção válida.".format(choice))

    def show_notes(self, notes=None):   
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}/n {2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Buscar por: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_notes(self):
        memo = input("Digite seu texto: ")
        self.notebook.new_note(memo)
        print("Sua anotação foi adicionada.")

    def modify_notes(self):
        id = input("Digite o id da anotação: ")
        memo = input("Digite o texto: ")
        tags = input("Digite as tags: ")

        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Até mais!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()