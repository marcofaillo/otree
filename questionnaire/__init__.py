from otree.api import *
c = Currency


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	sex = models.StringField(widget=widgets.RadioSelectHorizontal(),choices=['Maschile', 'Femminile', 'Non binario'])
	age = models.IntegerField(choices = range(18,60,1))
	num_experiments = models.IntegerField(choices = range(1,50,1))
	faculty = models.PositiveIntegerField(choices=[[1, 'Economia/Management'],[2, 'Giurisprudenza'],[3, 'Ingegneria'],[4,'Lettere'],[5,'Sociologia'],[6,'Psicologia'],[7,'Matematica/Fisica'],[8,'Informatica'],[9,'Altro'],[10,'Non sono studente/studentessa'],])




# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['sex', 'age',   'num_experiments','faculty']





page_sequence = [Demographics]
