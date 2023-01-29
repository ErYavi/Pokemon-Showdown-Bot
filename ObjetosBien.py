import AlgoritmoGenetico as al
import numpy as np
import moves


class Pokemon (object):

    def __init__(self, tipos, hp, atk, defensa, spc, spe):
        self.tipos = tipos
        self.hp = hp
        self.atk = atk
        self.defensa = defensa
        self.spc = spc
        self.spe = spe
        self.ataques = []

    # 4 objetos clase ataque

    def mostrar(self):
        print("STATS: ")
        print("TIPOS:"+str(self.tipos))
        print("-HP: " + str(self.hp))
        print("-ATK: " + str(self.atk))
        print("-DEF: " + str(self.defensa))
        print("-SPC: " + str(self.spc))
        print("-SPE: " + str(self.spe))

        # for i in ataques:
        #   print("Ataques: ")


class Ataque (object):
    def __init__(self, nombre):
        for i in moves and nombre != moves[i][0]:
            i += 1

        self.nombre = moves[i][0]
        self.tipo = moves[i][1]
        self.daño = moves[i][2]
        self.precision = moves[i][3]
        self.categoria = moves[i][4]
