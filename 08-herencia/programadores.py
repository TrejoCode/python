class Programador:

    def __init__(self, id, name, level, skill):
        self.__id = id
        self.name = name
        self.level = level
        self.skill = skill

    def programar(self):
        print(f"Hola, soy {self.name} y programo en {self.skill}")

class ProgramadorJava(Programador):

    def __init__(self, mi_id, mi_name, mi_level, mi_skill = "Java"):
        super().__init__(mi_id, mi_name, mi_level, mi_skill)
    
class ProgramadorPython(Programador):

    def __init__(self, new_id, new_name, new_level, new_skill = "Python"):
        super().__init__(new_id, new_name, new_level, new_skill)

def run():

    programador1 = ProgramadorJava(1, "Sergio", "Sr")
    programador2 = ProgramadorPython(2, "Manuel", "Middle")

    programador1.programar()
    programador2.programar()

if __name__ == '__main__':
    run()