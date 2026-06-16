from otree.api import *
c = Currency


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'zoom_meeting'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):

    proceed = models.IntegerField(initial=0)


# FUNCTIONS
# PAGES
class Zoom(Page):
    pass

class Agree(Page):
    form_model = 'player'
    form_fields = ['proceed']
    pass


class Stop(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed == 2

page_sequence = [Zoom, Agree, Stop]
