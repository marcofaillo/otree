from random import randrange
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)



author = 'Your name here'

ddoc = """
SIF versione Prolif - finanziatore"""
# #1 "F fixed" (finanziatore con pagamento fisso) 2 Quantity 3 "Quality" 4 "Average Quantity" 5 "Threshold"

class Constants(BaseConstants):
    name_in_url = 'chat'
    players_per_group = 2
    num_rounds = 1



class Subsession(BaseSubsession):

    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def chat_nickname(self):
        group = self.group

        return 'player {}'.format(self.id_in_group)
