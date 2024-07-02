# Aplicación de Notas CASO 5
#Una aplicación para tomar, editar y borrar notas.

#Crear una clase 
class Notebook:
    def __init__(self):
        self.notes = {}

    def add_note(self, title, content):
        self.notes[title] = content

    def delete_note(self, title):
        try:
            del self.notes[title]
            print(f"Note '{title}' eliminada correctamente.")
        except KeyError:
            print(f"La nota '{title}' no se encontró.")


    def list_notes(self):
        for title, content in self.notes.items():
            print(f"{title}\n{content}")

# Ejemplo de uso
notebook = Notebook()
notebook.add_note("Meeting Notes", "Discuss project milestones and deadlines.")
notebook.add_note("Shopping List", "Eggs, Milk, Bread")
notebook.add_note("Enviar el deber", "Enviar lo de Python.")

notebook.delete_note("Enviar el deber")
notebook.list_notes()
