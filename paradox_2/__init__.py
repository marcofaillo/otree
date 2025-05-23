from otree.api import *
import random as r
import json
from otree.api import safe_json
import numpy as np


doc = """
Paradox v.2"""


class C(BaseConstants):
    NAME_IN_URL = 'paradox_2'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    #bret
    box_value = 1
    num_rows = 10
    num_cols = 10
    box_height = '30px'
    box_width = '30px'
    random_payoff = True
    instructions = True
    feedback = True
    results = True
    dynamic = False
    time_interval = 1.00
    random = True
    devils_game = False
    undoable = True
    #draw_funds
    values = [0.25, 1]
    probabilities = [0.20, 0.80]

class Subsession(BaseSubsession):
        def creating_session(subsession):
            for player in subsession.get_players():
                 player.participant.vars['fund_1']= []
                 player.participant.vars['fund_2']= []
                 player.participant.vars['fund_3']= []
                 player.participant.vars['fund_4']= []
                 player.participant.vars['fund_5']= []
                 player.participant.vars['fund_6']= []
                 player.participant.vars['fund_7']= []
                 player.participant.vars['fund_8']= []
                 player.participant.vars['fund_9']= []
                 player.participant.vars['payoffs_choice2']= []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    proceed = models.IntegerField()
    person=models.IntegerField()

    q_1 = models.IntegerField()
    q_2 = models.FloatField()
    q_3 = models.FloatField()
    q_4 = models.IntegerField(choices=[[1, '£0; £2.5; £3.5; £.4.5; £8'], [2, '£2; £3; £4; £5; £6'], [3, '£1.5; £2.5; £3.5; £4.5; £5.5']],initial=0)
    q_5 = models.IntegerField(choices=[[1, '£4.5; £5.5; £6.5; £7.5; £8.5'], [2, '£4; £5; £6; £7; £8'], [3, '£0; £5.5; £6.5; £7.5; £8']],initial=0)

    errors=models.IntegerField(initial = 0)
    failed_too_many = models.BooleanField(initial=False)
    choice_1= models.IntegerField()
    choice_2= models.IntegerField()
# bret
    bomb = models.IntegerField(initial=0)
    bomb_location = models.TextField(initial="0")
    boxes_collected = models.IntegerField(initial=0)
    boxes_scheme = models.TextField(initial=0)
    round_to_pay = models.IntegerField(initial=0)
    round_result = models.FloatField(initial=0)
    pay_bret = models.FloatField(initial=0)
    return1 = models.FloatField()
    return2 = models.FloatField()
    return3 = models.FloatField()
    return4 = models.FloatField()
    return5 = models.FloatField()
    return6 = models.FloatField()
    return7 = models.FloatField()
    return8 = models.FloatField()
    return9 = models.FloatField()
    payoff_1 = models.FloatField()
    payment = models.FloatField()
    total_money = models.FloatField()
# def set_payoff(player: Player):
#
def check_proceed(player:Player):
    if player.proceed != 1:
        player.payoff=-1


def returns(player:Player):
       player.participant.vars['fund_1']= np.random.choice(C.values, size=8, p=C.probabilities)
       player.return1=np.sum(player.participant.vars['fund_1'])
       player.participant.vars['fund_2']= np.random.choice(C.values, size=8, p=C.probabilities)
       player.return2=np.sum(player.participant.vars['fund_2'])
       player.participant.vars['fund_3']= np.random.choice(C.values, size=8, p=C.probabilities)
       player.return3=np.sum(player.participant.vars['fund_3'])
       if player.session.config['treatment'] == 9:
           player.participant.vars['fund_4']= np.random.choice(C.values, size=8, p=C.probabilities)
           player.return4=np.sum(player.participant.vars['fund_4'])
           player.participant.vars['fund_5']= np.random.choice(C.values, size=8, p=C.probabilities)
           player.return5=np.sum(player.participant.vars['fund_5'])
           player.participant.vars['fund_6']= np.random.choice(C.values, size=8, p=C.probabilities)
           player.return6=np.sum(player.participant.vars['fund_6'])
           player.participant.vars['fund_7']= np.random.choice(C.values, size=8, p=C.probabilities)
           player.return7=np.sum(player.participant.vars['fund_7'])
           player.participant.vars['fund_8']= np.random.choice(C.values, size=8, p=C.probabilities)
           player.return8=np.sum(player.participant.vars['fund_8'])
           player.participant.vars['fund_9']= np.random.choice(C.values, size=8, p=C.probabilities)
           player.return9=np.sum(player.participant.vars['fund_9'])

def set_payoff(player:Player):
    #bret
    if player.bomb == 0:
       player.round_result = player.boxes_collected * C.box_value
       print("bomb not found", player.boxes_collected , C.box_value)
    else:
       player.round_result = 0
       print("bomb found")
    player.pay_bret = player.round_result*0.01
    if player.choice_2 == 1:
        player.payment = player.payoff_1
    else:
        player.payment = r.choice(player.participant.vars['payoffs_choice2'])
    player.total_money = player.pay_bret + player.payment

class Landing(Page):
        form_model = 'player'
        form_fields = ['proceed']
        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            check_proceed(player)


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

class Instructions3(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed ==  1
        def vars_for_template(player: Player):
            return dict(treatment=player.session.config['treatment'])

class Instructions_task(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed ==  1
        def vars_for_template(player: Player):
            return dict(treatment=player.session.config['treatment'])
        def before_next_page(player: Player, timeout_happened):
            returns(player)

class Questions(Page):
    form_model = 'player'
    form_fields = ['q_1', 'q_2', 'q_3', 'q_4', 'q_5']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

    def error_message(player: Player, values):
        if player.session.config['treatment'] == 3:
           solutions = dict(q_1=3, q_2=2, q_3=8, q_4 = 3, q_5=1)
        else:
           solutions = dict(q_1=9, q_2=2, q_3=8, q_4 = 3, q_5=1)

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


class Choice_1_3(Page):
    form_model = 'player'
    form_fields = ['choice_1']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.session.config['treatment'] == 3
    def vars_for_template(player: Player):
            return dict(fund_1 = player.participant.vars['fund_1'],fund_2 = player.participant.vars['fund_2'],fund_3 = player.participant.vars['fund_3'], return1= player.return1,return2= player.return2,return3= player.return3)

class Choice_1_9(Page):
    form_model = 'player'
    form_fields = ['choice_1']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.session.config['treatment'] == 9
    def vars_for_template(player: Player):
            return dict(fund_1 = player.participant.vars['fund_1'],fund_2 = player.participant.vars['fund_2'],fund_3 = player.participant.vars['fund_3'],fund_4 = player.participant.vars['fund_4'], fund_5 = player.participant.vars['fund_5'],fund_6 = player.participant.vars['fund_6'],fund_7 = player.participant.vars['fund_7'],fund_8 = player.participant.vars['fund_8'],fund_9= player.participant.vars['fund_9'],return1= player.return1,return2= player.return2,return3= player.return3,return4= player.return4,return5= player.return5,return6= player.return6,return7= player.return7,return8= player.return8,return9= player.return9)

class Choice_2(Page):
    form_model = 'player'
    form_fields = ['choice_2']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1
    def vars_for_template(player: Player):
        if player.choice_1 == 1:
            player.payoff_1 = player.return1
        elif player.choice_1 == 2:
            player.payoff_1 = player.return2
        elif player.choice_1 == 3:
            player.payoff_1 = player.return3
        elif player.choice_1 == 4:
            player.payoff_1 = player.return4
        elif player.choice_1 == 5:
            player.payoff_1 = player.return5
        elif player.choice_1 == 6:
            player.payoff_1 = player.return6
        elif player.choice_1 == 7:
            player.payoff_1 = player.return7
        elif player.choice_1 == 8:
            player.payoff_1 = player.return8
        else:
            player.payoff_1 = player.return9
        player.participant.vars['payoffs_choice2']=[0,0,0,0,0]
        player.participant.vars['payoffs_choice2'][0]= player.payoff_1-2
        player.participant.vars['payoffs_choice2'][1]= player.payoff_1-1
        player.participant.vars['payoffs_choice2'][2]= player.payoff_1
        player.participant.vars['payoffs_choice2'][3]= player.payoff_1+1
        player.participant.vars['payoffs_choice2'][4]= player.payoff_1+2

        return dict(choice_1 = player.choice_1, payoff_1= player.payoff_1, payoffs_2=player.participant.vars['payoffs_choice2'])


class Stop(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1
    def before_next_page(player: Player, timeout_happened):
        set_payoff(player)

class Feedback(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1
    def vars_for_template(player: Player):
            return dict(choice_1 = player.choice_1, choice_2=player.choice_2, payoff_1=player.payoff_1, payment=player.payment, bomb=player.bomb, pay_bret=player.pay_bret, total_money=player.total_money)


class Bret(Page):
    form_model = 'player'
    form_fields = [
        'bomb',
        'boxes_collected',
        'boxes_scheme',
        'bomb_location',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.proceed == 1
    @staticmethod
    def vars_for_template(player: Player):
        # define/reset input and reset if needed
        input_value = not player.session.config.get('devils_game', False) if not C.dynamic else False
        reset = False  # placeholder unless defined elsewhere

        return {
            'reset': safe_json(reset),
            'input': safe_json(input_value),
            'random': safe_json(C.random),
            'dynamic': safe_json(C.dynamic),
            'num_rows': safe_json(C.num_rows),
            'num_cols': safe_json(C.num_cols),
            'feedback': safe_json(C.feedback),
            'undoable': safe_json(C.undoable),
            'box_width': safe_json(C.box_width),
            'box_height': safe_json(C.box_height),
            'time_interval': safe_json(C.time_interval),
        }

class Back_to_Prolific (Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'prolific': player.session.config['prolific']}

page_sequence = [Landing, Instructions, Instructions2, Instructions3,Questions, Instructions_task, Bret, Fail, Choice_1_3, Choice_1_9,Choice_2,Stop, Feedback,Back_to_Prolific]
