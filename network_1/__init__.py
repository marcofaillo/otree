from otree.api import *
import random as r
import json

doc = """NetROL networks experiment. v. 7/5/2026"""

# ruolo = player.id_in_group: 1 = A, 2 = B, 3 = C

class C(BaseConstants):
    NAME_IN_URL = 'network_1'
    EXCHANGE_RATE=0.15
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT=50

class Subsession(BaseSubsession):
     pass


class Group(BaseGroup):
    choice_1_A_B= models.IntegerField()
    choice_1_A_C= models.IntegerField()
    choice_1_B_A= models.IntegerField()
    choice_1_B_C= models.IntegerField()
    choice_1_C_A= models.IntegerField()
    choice_1_C_B= models.IntegerField()
    choice_2_A_B= models.IntegerField()
    choice_2_A_C= models.IntegerField()
    choice_2_B_A= models.IntegerField()
    choice_2_B_C= models.IntegerField()
    choice_2_C_A= models.IntegerField()
    choice_2_C_B= models.IntegerField()
    choice_3_A_B= models.IntegerField()
    choice_3_A_C= models.IntegerField()
    choice_3_B_A= models.IntegerField()
    choice_3_B_C= models.IntegerField()
    choice_3_C_A= models.IntegerField()
    choice_3_C_B= models.IntegerField()

class Player(BasePlayer):
    proceed = models.IntegerField(initial=0)
    person=models.IntegerField()
    id_player=models.IntegerField()
# ---------ripristinare q_1 per sessioni ------------
#    q_1 = models.IntegerField(choices=[[1, 'You all participated in a previous survey'], [2, 'You all participated in a previous survey and selected the same topic as the most important one'], [3, 'You all participated in a previous survey and gave the same answers to the questions about the topic you consider as the most important one']], initial=0, widget=widgets.RadioSelect)
    q_1 = models.IntegerField()
    q_2 = models.IntegerField()
    q_3 = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    q_4 = models.BooleanField(choices=[[True, 'True'], [False, 'False']])
    re_read=models.IntegerField()
    errors=models.IntegerField(initial = 0)
    # failed_too_many = models.BooleanField(initial=False)
    failed_once = models.BooleanField(initial=False)
    wrong_answers = models.LongStringField()
    first= models.BooleanField(initial=False) #answer all questions at the first attempt
    next_rounds = models.IntegerField()
    stage = models.IntegerField()
    coparticipant = models.IntegerField()
    pay = models.IntegerField()
    gbp = models.FloatField()


# inital questionnaire
    gender = models.IntegerField(choices=[[1, 'Male'], [2, 'Female'], [3, 'Non-binary']])


#final questionnaire

    student = models.IntegerField(choices=[[1, 'Yes'], [0, 'No']])
    employment = models.IntegerField(choices=[[1, 'Full-time'], [2, 'Part-time'], [3, 'Due to start a new job within the next month'], [4,'Unemployed (and job seeking)'], [5,'Not in paid work (e.g. homemaker, retired or disabled)'], [6,'Other']])
    comment=models.StringField(null=True, blank=True)
# def set_payoff(player: Player):
#
def check_proceed(player:Player):
    if player.proceed != 1:
        player.payoff=-1

def compute_payoffs(group: Group):
    stage = r.randint(2, 3)
    coparticipant = r.randint(1, 2)

    for player in group.get_players():
        player.stage = stage
        player.coparticipant = coparticipant

        if player.id_in_group == 1:
            if stage == 2:
                if coparticipant == 1:
                    player.pay = 10 - group.choice_2_A_B + 2 * group.choice_2_B_A
                else:
                    player.pay= 10 - group.choice_2_A_C + 2 * group.choice_2_C_A
            else:
                if coparticipant == 1:
                    player.pay = 10 - group.choice_3_A_B + 2 * group.choice_3_B_A
                else:
                    player.pay = 10 - group.choice_3_A_C + 2 * group.choice_3_C_A

        elif player.id_in_group == 2:
            if stage == 2:
                if coparticipant == 1:
                    player.pay = 10 - group.choice_2_B_A + 2 * group.choice_2_A_B
                else:
                    player.pay = 10 - group.choice_2_B_C + 2 * group.choice_2_C_B
            else:
                if coparticipant == 1:
                    player.pay = 10 - group.choice_3_B_A + 2 * group.choice_3_A_B
                else:
                    player.pay = 10 - group.choice_3_B_C + 2 * group.choice_3_C_B

        else:
            if stage == 2:
                if coparticipant == 1:
                    player.pay= 10 - group.choice_2_C_A + 2 * group.choice_2_A_C
                else:
                    player.pay = 10 - group.choice_2_C_B + 2 * group.choice_2_B_C
            else:
                if coparticipant == 1:
                    player.pay = 10 - group.choice_3_C_A + 2 * group.choice_3_A_C
                else:
                    player.pay = 10 - group.choice_3_C_B + 2 * group.choice_3_B_C
        player.gbp = player.pay * C.EXCHANGE_RATE

class Landing(Page):
        form_model = 'player'
        form_fields = ['proceed']
        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            check_proceed(player)


class Instructions1(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and  player.session.config['test'] == 0

class Instructions2(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0

class Instructions3(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0


class Instructions4(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0

class Instructions5(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0



class Questions(Page):
    form_model = 'player'
    form_fields = ['q_1', 'q_2', 'q_3', 'q_4']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.session.config['test'] == 0

    def error_message(player: Player, values):
        solutions = dict(q_1=11, q_2=12, q_3=False, q_4=True)

        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        if errors:
                player.errors += 1
                return errors

class InstructionsHelp(Page):
    @staticmethod
    def is_displayed(player):
        return True

class InstructionsWaitPage(WaitPage):
    wait_for_all_groups=True
    body_text = "Wait for the other participants to make their choices."

class Choice_1_A(Page):
    form_model = 'group'
    form_fields = ['choice_1_A_B','choice_1_A_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 1
    def vars_for_template(player: Player):
        return {'network': player.session.config['network']}


class Choice_1_B(Page):
    form_model = 'group'
    form_fields = ['choice_1_B_A','choice_1_B_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 2
    def vars_for_template(player: Player):
        return {'network': player.session.config['network']}

class Choice_1_C(Page):
    form_model = 'group'
    form_fields = ['choice_1_C_A','choice_1_C_B']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 3
    def vars_for_template(player: Player):
        return {'network': player.session.config['network']}




class See_declaration(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1
    def vars_for_template(player: Player):
        return {'role': player.id_in_group,'network': player.session.config['network'],'choice_1_A_B':player.group.choice_1_A_B,'choice_1_A_C': player.group.choice_1_A_C, 'choice_1_B_A': player.group.choice_1_B_A,'choice_1_B_C': player.group.choice_1_B_C, 'choice_1_C_A': player.group.choice_1_C_A, 'choice_1_C_B': player.group.choice_1_C_B}




class Choice_2_A(Page):
    form_model = 'group'
    form_fields = ['choice_2_A_B','choice_2_A_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 1
    def vars_for_template(player: Player):
        return {'network': player.session.config['network'],'choice_1_A_B':player.group.choice_1_A_B,'choice_1_A_C': player.group.choice_1_A_C}

class Choice_2_B(Page):
    form_model = 'group'
    form_fields = ['choice_2_B_A','choice_2_B_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 2
    def vars_for_template(player: Player):
        return {'network': player.session.config['network'],'choice_1_B_A': player.group.choice_1_B_A,'choice_1_B_C': player.group.choice_1_B_C}

class Choice_2_C(Page):
    form_model = 'group'
    form_fields = ['choice_2_C_A','choice_2_C_B']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 3
    def vars_for_template(player: Player):
        return {'network': player.session.config['network'],'choice_1_C_A': player.group.choice_1_C_A,'choice_1_C_B': player.group.choice_1_C_B}



class See_information(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1
    def vars_for_template(player: Player):
        return {'network': player.session.config['network'], 'role': player.id_in_group,'choice_1_A_B':player.group.choice_1_A_B,'choice_1_A_C': player.group.choice_1_A_C, 'choice_1_B_A': player.group.choice_1_B_A,'choice_1_B_C': player.group.choice_1_B_C, 'choice_1_C_A': player.group.choice_1_C_A, 'choice_1_C_B': player.group.choice_1_C_B, 'choice_2_A_B':player.group.choice_2_A_B,'choice_2_A_C': player.group.choice_2_A_C, 'choice_2_B_A': player.group.choice_2_B_A,'choice_2_B_C': player.group.choice_2_B_C, 'choice_2_C_A': player.group.choice_2_C_A, 'choice_2_C_B': player.group.choice_2_C_B}


class Choice_3_A(Page):
    form_model = 'group'
    form_fields = ['choice_3_A_B','choice_3_A_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 1
    def vars_for_template(player: Player):
        return {'network': player.session.config['network']}

class Choice_3_B(Page):
    form_model = 'group'
    form_fields = ['choice_3_B_A','choice_3_B_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 2
    def vars_for_template(player: Player):
        return {'network': player.session.config['network']}

class Choice_3_C(Page):
    form_model = 'group'
    form_fields = ['choice_3_C_A','choice_3_C_B']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.id_in_group == 3
    def vars_for_template(player: Player):
        return {'network': player.session.config['network']}


class ResultsWaitPage(WaitPage):
    body_text = "Wait for the other participants to make their choices."

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['student', 'employment','comment']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class ResultsWaitPage2(WaitPage):
    body_text = "Wait for the other participants to make their choices."
    after_all_players_arrive = compute_payoffs

class Final_feedback (Page):
    @staticmethod
    def vars_for_template(player: Player):
            return {'payoff': player.pay, 'gbp': player.gbp,'role': player.id_in_group, 'stage': player.stage, 'coparticipant' : player.coparticipant, 'choice_2_A_B':player.group.choice_2_A_B,'choice_2_A_C': player.group.choice_2_A_C, 'choice_2_B_A': player.group.choice_2_B_A,'choice_2_B_C': player.group.choice_2_B_C, 'choice_2_C_A': player.group.choice_2_C_A, 'choice_2_C_B': player.group.choice_2_C_B,   'choice_3_A_B':player.group.choice_3_A_B,'choice_3_A_C': player.group.choice_3_A_C, 'choice_3_B_A': player.group.choice_3_B_A,'choice_3_B_C': player.group.choice_3_B_C, 'choice_3_C_A': player.group.choice_3_C_A, 'choice_3_C_B': player.group.choice_3_C_B }

class Back_to_Prolific (Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'prolific': player.session.config['prolific']}

# page_sequence = [Landing, Instructions1, Instructions2,Instructions3,Instructions4,Instructions1_2, Instructions2_2,Instructions3_2, Instructions4_2, Questions, Feedback_Answers, Instructions1_2, Instructions2_2, Instructions3_2,Questions, Fail, Choice_1, Choice_1_stop, Choice_g, Choice_app, Choice_neu, Choice_pol,Choice_soc, Questionnaire_2,Back_to_Prolific]
page_sequence = [Landing,Instructions1, Instructions2,Instructions3,Instructions4,Instructions5, Questions, InstructionsWaitPage, Choice_1_A, Choice_1_B, Choice_1_C,ResultsWaitPage, See_declaration, Choice_2_A, Choice_2_B, Choice_2_C,ResultsWaitPage,See_information,ResultsWaitPage, Choice_3_A, Choice_3_B, Choice_3_C,ResultsWaitPage2,Final_feedback,Questionnaire,Back_to_Prolific]
