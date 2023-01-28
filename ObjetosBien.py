import AlgoritmoGenetico as al
import numpy as np

class Pokemon (object):

   def __init__(self,name, hp, atk, defensa, spc, spe):
      self.name = name
      self.tipos = None
      self.hp = hp
      self.atk = atk
      self.defensa = defensa
      self.spc = spc
      self.spe = spe
      self.estado = None
      self.confuso = None
      self.ataques = np.array(Ataque[4])

      
   #4 objetos clase ataque
   def mostrar():
      print("Atriburtos: ")
      print("HP: ")
      print("ATK: ")
      print("DEF:")
      print("SPC: ")
      print("SPE: ")
      print("Estado:")
      print("Confuso: ")
      #for i in ataques:
      #   print("Ataques: ")


class Ataque (object):
     def __init__(self, nombre):
         for i in al.moves and nombre != al.moves[i].name:
             i += 1
         
         self.nombre = al.moves[i].name
         self.tipo  = al.moves[i].type
         self.daño = al.moves[i].damage
         self.precision = al.moves[i].accuracy
         self.categoria = al.moves[i].category