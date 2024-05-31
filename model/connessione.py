from dataclasses import dataclass

from model.object import Object


@dataclass
class Connessione:
    o1:Object
    o2:Object
    peso:int

    def __hash__(self):
        return hash((self.o1,self.o2))

    def __str__(self):
        return (f"{self.o1.object_id} - {self.o2.object_id} - {self.peso}")