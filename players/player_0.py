from defs import Action, Turn
import random

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Topone"

    def __init__(self):
        pass

    def play(self, turn_index: int, history: list[Turn], opponent) -> Action:
        punch = ["On parle de son sourire a la faire rougir",
        "De ses yeux qui rendent amoureux",
        "Trop petit trop de bide",
        "Une meuf là bas m’fais les yeux doux",
        "Grande, belles formes et regard revolver ",
        "En tout cas garde la peche",
        "J’suis un poisson, j cherche une poissonne",
        "Que des belles croupe qui se balance",
        "La j’ai vraiment trop chaud",
        "Bois encore un verre, viens danser contre moi",
        "En tout cas j'espère bien qu’on finira tous les deux !"]
        
        if (opponent.name =="Rats" and turn_index==0) :
            print("Joyeux anniversaire Nico, tu es mon Top 1 à moi <3")
        elif (opponent.name =="YELLOW APPLE" and turn_index==0) :
            print("Meme si vous vous etes acharnees contre nous on vous aime <3")
        elif (opponent.name =="Bojji" and turn_index==0) :
            print("On vous aime moins que les YEllOW APPLE mais un peu quand meme, pas beaucoup.")
        elif (opponent.name =="Colsplif" and turn_index==0) :
            print("Nos preferes <3")
        elif (opponent.name =="Tonic" and turn_index==0) :
            print("Envie2boir1verreAvecVous <3 (de ginto)")
        elif (opponent.name =="Lucalixte" and turn_index==0) :
            print("Keur")
        elif (opponent.name =="Maxwelle" and turn_index==0) :
            print("On vous tape pas desssus kom des taupes")
        else :
            print(random.choice(punch))
        return Action.COOPERATE