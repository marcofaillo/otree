from otree.api import *
import random as r

doc = """
Weingast 1997 version: 7 Oct 2024
"""


class C(BaseConstants):
    NAME_IN_URL = 'weingast_citizens_2'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT=50

class Subsession(BaseSubsession):
     pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    proceed = models.IntegerField()
    person=models.IntegerField()
# ---------ripristinare q_1 per sessioni ------------

    # q_1 = models.IntegerField(choices=[[1, 'You all participated in a previous survey'], [2, 'You all participated in a previous survey and selected the same topic as the most important one'], [3, 'You all participated in a previous survey and gave the same answers to the questions about the topic you consider as the most important one']], initial=0, widget=widgets.RadioSelect)
    q_2 = models.IntegerField(choices=[[1, 'Person 1, and choose between A, B, C, D'], [2, 'Person 2, and choose between X and Y'], [3, 'Person 3, and choose between X and Y']], initial=0, widget=widgets.RadioSelect)
    q_3 = models.IntegerField(choices=[[1, '2'], [2, '8'], [3, '9'],[4, '1']],initial=0)
    q_4 = models.IntegerField(choices=[[1, '2'], [2, '12'], [3, '8'],[4, '1']],initial=0)
    errors=models.IntegerField(initial = 0)
    failed_too_many = models.BooleanField(initial=False)
    choice_A= models.IntegerField()
    choice_B= models.IntegerField()
    choice_C= models.IntegerField()
    choice_D= models.IntegerField()

    instructions=models.IntegerField(choices=[[1, '1. Not at all clear.'], [2, '2.'], [3,'3.'], [4,'4.'], [5, '5. Perfectly clear.']])
    student = models.IntegerField(choices=[[1, 'Yes'], [0, 'No']])
    employment = models.IntegerField(choices=[[1, 'Full-time'], [2, 'Part-time'], [3, 'Due to start a new job within the next month'], [4,'Unemployed (and job seeking)'], [5,'Not in paid work (e.g. homemaker, retired or disabled)'], [6,'Other']])
    comment = models.StringField(blank=True)

# def set_payoff(player: Player):
#
def check_proceed(player:Player):
    if player.proceed != 1:
        player.payoff=-1


class Landing(Page):
        form_model = 'player'
        form_fields = ['proceed']
        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            check_proceed(player)


class Treatment(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed ==  1
        def vars_for_template(player: Player):
            return dict(treatment=player.session.config['treatment'])   #,topic=player.session.config['topic'])

class Instructions(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed ==  1
        def vars_for_template(player: Player):
            return dict(treatment=player.session.config['treatment'])


class Instructions2(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed ==  1
        def vars_for_template(player: Player):
            return dict(treatment=player.session.config['treatment'])

class Questions(Page):
    form_model = 'player'
    form_fields = ['q_2', 'q_3', 'q_4'] # ---------ripristinare q_1 per sessioni ------------

    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

    def error_message(player: Player, values):
        solutions = dict( q_2=2, q_3=4, q_4 = 2)    #    solutions = dict(q_1=2, q_2=3, q_3=3, q_4 = 2)#

        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        if errors:
            player.errors += 1
            if player.errors>1:
                player.failed_too_many = True
                # we don't return any error here; just let the user proceed to the
                # next page, but the next page is the 'failed' page that boots them
                # from the experiment.
            else:
                return errors

class Fail (Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many


class Choice_A(Page):
    form_model = 'player'
    form_fields = ['choice_A']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class Choice_B(Page):
    form_model = 'player'
    form_fields = ['choice_B']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class Choice_C(Page):
    form_model = 'player'
    form_fields = ['choice_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class Choice_D(Page):
    form_model = 'player'
    form_fields = ['choice_D']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['student', 'instructions', 'employment', 'comment']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class Back_to_Prolific (Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'prolific': player.session.config['prolific']}

page_sequence = [Landing, Treatment, Instructions, Instructions2, Questions, Fail, Choice_A, Choice_B, Choice_C,Choice_D,Questionnaire, Back_to_Prolific]
