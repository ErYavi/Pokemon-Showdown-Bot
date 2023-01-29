import AlgoritmoGenetico as al
import numpy as np
import moves


class Pokemon (object):

    def __init__(self, tipos, hp, atk, defensa, spc, spe, ataques):
        self.tipos = tipos
        self.hp = hp
        self.atk = atk
        self.defensa = defensa
        self.spc = spc
        self.spe = spe
        self.ataques = ataques

    # 4 objetos clase ataque

    def mostrar(self):
        print("STATS: ")
        print("TIPOS:"+str(self.tipos))
        print("-HP: " + str(self.hp))
        print("-ATK: " + str(self.atk))
        print("-DEF: " + str(self.defensa))
        print("-SPC: " + str(self.spc))
        print("-SPE: " + str(self.spe))
        print("-Ataques: " + str(self.ataques))
