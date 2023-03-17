#importando biblioteca para lidar com datas
import datetime

#armazenar o próximo id para todas as novas anotações

last_id = 0

# criamos a classe Note
class Note:
    """
    Representa uma anotação no notebook. Verifica o conteúdo de uma 
    String na busca e armazena tags para cada anotação.
    """

    def __init__(self, memo, tags=""):
        """
        Inicializa uma anotação com texto e uma tag opcional. Automaticamente 
        define uma data de criação dessa nota. E também define um id único
        para a nota.
        """

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id

        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Define se essa anotação bate com o filtro. Retorna True se sim,
        False se não.
        """

        return filter in self.memo or filter in self.tags
    
# criamos a classe Notebook
class Notebook:
    """
    Representa a uma coleção de anotações que pode ser tagueadas, 
    modificadas e buscadas.
    """

    def __init__(self):
        """
        Inicia a classe Notebook com uma lista vazia de anotações.
        """

        self.notes = []

    def new_note(self, memo, tags=""):
        """
        Cria uma nova anotação e adiciona à lista.
        """

        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Localizar a anotação dado um id.
        """
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        Procura uma anotação dado um id e muda o seu texto para um valor
        dado.
        """

        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        """
        Procura a tag com a identificação da anotação dada e altera a sua
        tag para um valor dado.
        """

        self._find_note(note_id).tags = tags

    def search(self, filter):
        """
        Busca todas as anotações que batem com o filtro determinado.
        """

        return [note for note in self.notes if note.match(filter)]