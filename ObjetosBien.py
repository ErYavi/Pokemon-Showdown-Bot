import AlgoritmoGenetico as al
import numpy as np
import moves

class Pokemon (object):

   def __init__(self, hp, atk, defensa, spc, spe):
      self.tipos = None
      self.hp = hp
      self.atk = atk
      self.defensa = defensa
      self.spc = spc
      self.spe = spe
      self.estado = None
      self.confuso = None
      self.ataques = []

      
   #4 objetos clase ataque
   def mostrar():
      print("Atriburtos: ")
      print("-HP: ")
      print("-ATK: ")
      print("-DEF:")
      print("-SPC: ")
      print("-SPE: ")
      print("-Estado:")
      print("-Confuso: ")
      #for i in ataques:
      #   print("Ataques: ")


class Ataque (object):
     def __init__(self, nombre):
         for i in moves and nombre != moves[i][0]:
             i += 1
         
         self.nombre = moves[i][0]
         self.tipo  = moves[i][1]
         self.daño = moves[i][2]
         self.precision = moves[i][3]
         self.categoria = moves[i][4]