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
      self.ataques = None
      
   #4 objetos clase ataque


class Ataque (object):
     def __init__(tipo,daño,precision,categoria):
        tipo
        daño
        precision
        categoria
