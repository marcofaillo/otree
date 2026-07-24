from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Faillo Baggio'

doc = """
Faillo Baggio
"""


class Constants(BaseConstants):
    name_in_url = 'faillo_baggio'
    players_per_group = 2
    num_rounds = 17
    endowment = 20
    seconds_A = 15
    seconds_B = 10
    pagamento_secondi = 0.5



class Subsession(BaseSubsession):
    def creating_session(self):

        self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['easy_complicated'] = ['E']*(int(Constants.num_rounds/2)) + ['C']*(int(Constants.num_rounds/2))
                player.participant.vars['UMS'] = []
                random.shuffle(player.participant.vars['easy_complicated'])
                player.participant.vars['target'] = []
                for n in range(Constants.num_rounds):
                    player.participant.vars['target'].append([random.randint(6,100),random.randint(6,100),random.randint(6,100)])
                print(player.participant.vars['target'])

    def set_payoff(self):

        for player in self.get_players():
            if player.role() == "A":
                other = player.get_others_in_group()[0]


                if player.task_type == "C" and player.task_solved == 3:
                    player.payoff_round = 5
                elif player.task_type == "E" and player.task_solved == 1:
                    player.payoff_round = 5
                else:
                    player.payoff_round = 0

                if other.task_solved ==1:
                    player.altro_risolve = 1


            #giocatore B
            else:
                other = player.get_others_in_group()[0]
                if other.task_quality == "H" and other.task_type == "C" and other.task_solved == 3 :
                    player.payoff_round = 3
                elif other.task_quality == "L" and other.task_type == "C" and other.task_solved == 3 :
                    player.payoff_round = 1
                elif other.task_quality == "H" and other.task_type == "E" and other.task_solved == 1 :
                    player.payoff_round = 3
                elif other.task_quality == "L" and other.task_type == "E" and other.task_solved == 1 :
                    player.payoff_round = 1
                else:
                    player.payoff_round = 0
                if player.stochastic_event or player.task_solved == 0:
                    player.payoff_round = 0



            if player.payoff_round > 0:
                if  player.role() == "A":
                    player.tempo_residuo = Constants.seconds_A - player.tempo_impiegato
                    player.payoff_secondi = player.tempo_residuo * Constants.pagamento_secondi
                else:
                    player.tempo_residuo = Constants.seconds_B - player.tempo_impiegato
                    player.payoff_secondi = player.tempo_residuo * Constants.pagamento_secondi

            if self.session.config['treatment'] == 2 and player.altro_risolve == 0:

                    player.payoff_round = player.payoff_secondi
            else:
                    player.payoff_round = player.payoff_round + player.tempo_residuo*Constants.pagamento_secondi

            if self.round_number > 2:
                    player.payoff = player.payoff_round
                    # ## calcolo payoff cumulato
                    player.participant.vars['UMS'].append(player.payoff_round)

                    player.UMS_cumulati = sum(player.participant.vars['UMS'])

            else:

                    player.UMS_cumulati = 0




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    for i in range(1,11):
        locals()['slider_' + str(i)] = models.IntegerField(min=0, max= 100,initial=0)
    del i


    play_game_1 = models.IntegerField(doc="not used")
    play_game_2 = models.IntegerField(doc="not used")

    task_type = models.CharField(initial="",doc="E for easy, C for complicated")
    task_quality = models.CharField(initial="",doc="H for high, L for low")
    task_solved = models.IntegerField(initial=0,doc="number of slide solved")


    stochastic_event = models.BooleanField(initial=False,doc="stochastic event")
    altro_risolve = models.BooleanField(initial=False, doc="altro giocatore risolve il task") ##usato solo per giocatore A

    payoff_round = models.FloatField(initial=0,doc="round payoff")

    sex = models.CharField(widget=widgets.RadioSelectHorizontal(), choices=['Maschile', 'Femminile'])
    age = models.IntegerField(choices = range(18, 60, 1))
    num_experiments = models.IntegerField(choices = range(1, 50, 1))
    faculty = models.PositiveIntegerField(choices=[[1, 'Economia'], [2, 'Giurisprudenza'], [3, 'Ingegneria'], [4, 'Lettere'],
         [5, 'Sociologia'], [6, 'Psicologia'], [7, 'Matematica/Fisica'], [8, 'Informatica'], [9, 'Altro'], [10, 'Non sono studente/studentessa'], ])

    tempo_impiegato = models.IntegerField(initial=0)
    tempo_residuo = models.IntegerField(initial=0)
    payoff_secondi = models.FloatField(initial=0)
    mio_round = models.IntegerField(initial=0)
    UMS_cumulati = models.FloatField(initial=0)

    Errors = models.IntegerField(initial=0)  # errori nelle domande di controllo.
    q1 = models.IntegerField(
        choices=[[1, 'rimarrà invariato per tutto l’esperimento'], [2, 'cambierà ad ogni round']],
        widget=widgets.RadioSelect
    )
    q2 = models.IntegerField(
        choices=[[1, 'rimarrà invariata per tutto l’esperimento'], [2, 'cambierà ad ogni round']],
        widget=widgets.RadioSelect
    )

    q3 = models.IntegerField(
        choices=[[1, '3 UMS se è da 3 cursori, 1 UMS se è da 1 cursore'], [2, '5 UMS ']],
        widget=widgets.RadioSelect
    )
    q4 = models.IntegerField(
        choices=[[1, '3 UMS se l’ho completata in modo preciso, 1 UMS se l’ho completata in modo approssimato '], [2, '5 UMS']],
        widget=widgets.RadioSelect
    )
    q5 = models.IntegerField()

    q6 = models.IntegerField()

    q7 = models.IntegerField()

    q8 = models.IntegerField()

    q9 = models.IntegerField()

    q10 = models.IntegerField()


    def set_quality(self):

        # print(self.task_type,self.slider_1,self.slider_2,self.slider_3,self.participant.vars['target'][self.round_number-1][0],self.participant.vars['target'][self.round_number-1][1],self.participant.vars['target'][self.round_number-1][2])
        if self.task_type == "E":
            if self.slider_1 == self.participant.vars['target'][self.round_number-1][0]:
                self.task_quality = "H"
            else:
                self.task_quality = "L"
            if self.get_compare(self.slider_1,self.participant.vars['target'][self.round_number-1][0]):
                self.task_solved = 1
            if self.task_solved == 0:
                self.task_quality = "N"
        else:
            if self.slider_1 == self.participant.vars['target'][self.round_number-1][0] and self.slider_2 == self.participant.vars['target'][self.round_number-1][1] and self.slider_3 == self.participant.vars['target'][self.round_number-1][2]:
                self.task_quality = "H"
            else:
                self.task_quality = "L"
            if self.get_compare(self.slider_1,self.participant.vars['target'][self.round_number-1][0]):
                self.task_solved = self.task_solved + 1
            if self.get_compare(self.slider_2,self.participant.vars['target'][self.round_number-1][1]):
                self.task_solved = self.task_solved + 1
            if self.get_compare(self.slider_3,self.participant.vars['target'][self.round_number-1][2]):
                self.task_solved = self.task_solved + 1
            if self.task_solved < 3:
                self.task_quality = "N"

    def get_compare(self,s,t):
        if self.task_quality == "H":
            return s == t
        else:
            print(s,t,(s >= t - 5 and s <= t + 5))
            return (s >= t - 5 and s <= t + 5)

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        else:
            return 'B'
