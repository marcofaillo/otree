from otree.api import *
import random as r
import json

doc = """NetROL Discrimination experiment"""

# Sequence 1: gender, appearence, neutral, ideo, socio

class C(BaseConstants):
    NAME_IN_URL = 'discrimination_1'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT=50

class Subsession(BaseSubsession):
     pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    proceed = models.IntegerField(initial=0)
    person=models.IntegerField()

# ---------ripristinare q_1 per sessioni ------------
#    q_1 = models.IntegerField(choices=[[1, 'You all participated in a previous survey'], [2, 'You all participated in a previous survey and selected the same topic as the most important one'], [3, 'You all participated in a previous survey and gave the same answers to the questions about the topic you consider as the most important one']], initial=0, widget=widgets.RadioSelect)
    q_1 = models.IntegerField()
    q_2 = models.IntegerField()
    q_3 = models.IntegerField()
    q_4 = models.IntegerField()
    re_read=models.IntegerField()
    errors=models.IntegerField(initial = 0)
    failed_too_many = models.BooleanField(initial=False)
    failed_once = models.BooleanField(initial=False)
    wrong_answers = models.LongStringField()
    first= models.BooleanField(initial=False) #answer all questions at the first attempt
    next_rounds = models.IntegerField()
    choice_1= models.IntegerField()
    ord =  models.IntegerField()
    choice_g_2_confirm= models.IntegerField(initial=0)
    choice_g_3_confirm= models.IntegerField(initial=0)
    choice_app_1_confirm= models.IntegerField(initial=0)
    choice_app_2_confirm= models.IntegerField(initial=0)
    choice_app_3_confirm= models.IntegerField(initial=0)
    choice_neu_1_confirm= models.IntegerField(initial=0)
    choice_neu_2_confirm= models.IntegerField(initial=0)
    choice_neu_3_confirm= models.IntegerField(initial=0)
    choice_pol_1_confirm= models.IntegerField(initial=0)
    choice_pol_2_confirm= models.IntegerField(initial=0)
    choice_pol_3_confirm= models.IntegerField(initial=0)
    choice_pol_4_confirm= models.IntegerField(initial=0)
    choice_soc_1_confirm= models.IntegerField(initial=0)
    choice_soc_2_confirm= models.IntegerField(initial=0)
    choice_soc_3_confirm= models.IntegerField(initial=0)

    choice_g_1= models.IntegerField(initial=None)
    choice_g_2= models.IntegerField(initial=None)
    choice_g_3= models.IntegerField(initial=None)
    choice_app_1= models.IntegerField(initial=None)
    choice_app_2= models.IntegerField(initial=None)
    choice_app_3= models.IntegerField(initial=None)
    choice_neu_1= models.IntegerField(initial=None)
    choice_neu_2= models.IntegerField(initial=None)
    choice_neu_3= models.IntegerField(initial=None)
    choice_pol_1= models.IntegerField(initial=None)
    choice_pol_2= models.IntegerField(initial=None)
    choice_pol_3= models.IntegerField(initial=None)
    choice_pol_4= models.IntegerField(initial=None)
    choice_soc_1= models.IntegerField(initial=None)
    choice_soc_2= models.IntegerField(initial=None)
    choice_soc_3= models.IntegerField(initial=None)
    choice_soc_4= models.IntegerField(initial=None)

# inital questionnaire
    gender = models.IntegerField(choices=[[1, 'Male'], [2, 'Female'], [3, 'Non-binary']])
    activity = models.IntegerField(choices=[[1, 'More than 6 hours per week'], [2, 'From 3 to 6 hours per week'], [3, 'Less than 3 hours per week']])
    height = models.IntegerField(initial = None)
    weight = models.IntegerField(initial = None)
    politics = models.IntegerField(choices=[[1, 'Left'], [2, 'Centre-Left'], [3, 'Centre-Right'], [3, 'Right']])
    holidays = models.IntegerField(choices=[[1, 'Mountains'], [2, 'Beach'], [3, 'Visiting cities']])
    ladder= models.IntegerField(choices=[[1, '1(worst off in terms of economic power)'], [2, '2'], [3,'3'], [4,'4'], [5, '5'],[6, '6'], [7, '7'], [8, '8'], [9, '9'],[10, '10(best off in terms of economic power)']])
    risk_1= models.IntegerField(choices=[[1, '1(Strongly disagree)'], [2, '2'], [3,'3'], [4,'4'], [5, '5'],[6, '6'], [7, '7'], [8, '8'], [9, '9'],[10, '10(Strongly agree)']])


#final questionnaire

    instructions=models.IntegerField(choices=[[1, '1. Not at all clear.'], [2, '2.'], [3,'3.'], [4,'4.'], [5, '5. Perfectly clear.']])
    student = models.IntegerField(choices=[[1, 'Yes'], [0, 'No']])
    employment = models.IntegerField(choices=[[1, 'Full-time'], [2, 'Part-time'], [3, 'Due to start a new job within the next month'], [4,'Unemployed (and job seeking)'], [5,'Not in paid work (e.g. homemaker, retired or disabled)'], [6,'Other']])
    religiosity = models.IntegerField(choices=[[1, 'Low'], [2, 'Medium'], [3, 'High'], [4,'I am not a religious person']])
    siblings = models.IntegerField(choices=[[1, 'Only child'], [2, 'One'], [3, 'More than one']])
    risk_2= models.IntegerField(choices=[[1, '1(Strongly disagree)'], [2, '2'], [3,'3'], [4,'4'], [5, '5'],[6, '6'], [7, '7'], [8, '8'], [9, '9'],[10, '10(Strongly agree)']])
    comment=models.StringField(null=True, blank=True)
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

class Questionnaire_1(Page):
    form_model = 'player'
    form_fields = ['gender', 'activity', 'height', 'weight','politics', 'ladder', 'risk_1']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1


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
        form_model = 'player'
        form_fields = ['re_read']
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0


class Instructions1_2(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0 and (player.failed_once == True or player.re_read == 1)

class Instructions2_2(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0 and (player.failed_once == True or player.re_read == 1)


class Instructions3_2(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0 and (player.failed_once == True or player.re_read == 1)

class Instructions4_2(Page):
        @staticmethod
        def is_displayed(player: Player):
            return player.proceed == 1 and player.session.config['test'] == 0 and (player.failed_once == True or player.re_read == 1)

class Questions(Page):
    form_model = 'player'
    form_fields = ['q_1', 'q_2', 'q_3', 'q_4']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.session.config['test'] == 0 and not player.first

    def error_message(player: Player, values):
        solutions = dict(q_1=13, q_2=13, q_3=6, q_4=12)

        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        if errors:
                player.errors += 1
                player.wrong_answers = json.dumps(errors)  # store as string
                if player.errors == 1:
                    player.failed_once = True
                    return None # show wrongs, then go to feedback
                else:
                    player.failed_too_many = True
                    return None
        else:
            player.first = True


class Feedback_Answers(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_once and player.session.config['test'] == 0 and player.errors == 1
    @staticmethod
    def vars_for_template(player: Player):
            import json

            question_texts = {
                'q_1': "1) In round 1, if you send 3 points and your co-participant sends 3 points, your earning will be",
                'q_2': "2) In round 1, if you send 4 points and your co-participant sends 5  points,  your co-participant's  earning will be",
                'q_3': "3) Considering the example of the instructions, suppose that in round 1 you decided to send 3 point to your co-participant. You decided to go on to round 2. In round 2, you decided to revise your choice only in case you are matched with a tall person, sending 6 points. How many points your co-participant will receive if, at the end, round 2 is selected and your co-participant is a  medium-sized person?",
                'q_4': "4) Considering the previous scenario, How many points your co-participant will receive if, at the end, round 2 is selected and your co-participant is a tall person?",
            }

            wrong_fields = json.loads(player.wrong_answers)

            wrong_named = {
                question_texts[key]: wrong_fields[key]
                for key in wrong_fields
            }

            answers_named = {}
            answers_named = {}
            for key in ['q_1', 'q_2', 'q_3', 'q_4']:

                label = str(getattr(player, key))
                    # Add "→ Wrong" only if this question was wrong
                if key in wrong_fields:
                    label += " → Wrong"
                answers_named[question_texts[key]] = label  # ✅ include all questions

            return {
                'wrong': wrong_named,
                'answers': answers_named
            }




    # def is_processing_error_message(player):
    #         return False  # disable revalidation

class Fail (Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many


class Choice_1(Page):
    form_model = 'player'
    form_fields = ['choice_1']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class Choice_1_stop(Page):
    form_model = 'player'
    form_fields = ['next_rounds']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

class Choice_g(Page):
    form_model = 'player'
    form_fields = ['choice_g_1','choice_g_2','choice_g_3']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.next_rounds == 1
        player.ord=player.session.config['sequence']
    def vars_for_template(player: Player):
        return {'choice_1': player.choice_1}
    def error_message(player, values):
        for field in ['choice_g_1', 'choice_g_2', 'choice_g_3']:
            value = values[field]
            if not (0 <= value <= 10 or value == 99):
                return "Numbers must be between 0 and 10"

class Choice_app(Page):
    form_model = 'player'
    form_fields = ['choice_app_1','choice_app_2','choice_app_3']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.next_rounds == 1
    def vars_for_template(player: Player):
        return {'choice_1': player.choice_1}
    def error_message(player, values):
        for field in ['choice_app_1', 'choice_app_2', 'choice_app_3']:
            value = values[field]
            if not (0 <= value <= 10 or value == 99):
                return "Numbers must be between 0 and 10"

class Choice_neu(Page):
    form_model = 'player'
    form_fields = ['choice_neu_1','choice_neu_2','choice_neu_3']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.next_rounds == 1
    def vars_for_template(player: Player):
        return {'choice_1': player.choice_1}
    def error_message(player, values):
        for field in ['choice_neu_1', 'choice_neu_2', 'choice_neu_3']:
            value = values[field]
            if not (0 <= value <= 10 or value == 99):
                return "Numbers must be between 0 and 10"



class Choice_pol(Page):
    form_model = 'player'
    form_fields = ['choice_pol_1','choice_pol_2','choice_pol_3','choice_pol_4']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.next_rounds == 1
    def vars_for_template(player: Player):
        return {'choice_1': player.choice_1}
    def error_message(player, values):
        for field in ['choice_pol_1', 'choice_pol_2', 'choice_pol_3']:
            value = values[field]
            if not (0 <= value <= 10 or value == 99):
                return "Numbers must be between 0 and 10"



class Choice_soc(Page):
    form_model = 'player'
    form_fields = ['choice_soc_1','choice_soc_2','choice_soc_3']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.next_rounds == 1
    def vars_for_template(player: Player):
        return {'choice_1': player.choice_1}
    def error_message(player, values):
        for field in ['choice_soc_1', 'choice_soc_2', 'choice_soc_3']:
            value = values[field]
            if not (0 <= value <= 10 or value == 99):
                return "Numbers must be between 0 and 10"



class Questionnaire_2(Page):
    form_model = 'player'
    form_fields = ['student', 'employment', 'religiosity', 'siblings', 'risk_2', 'comment']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1


class Back_to_Prolific (Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {'prolific': player.session.config['prolific']}

page_sequence = [Landing, Questionnaire_1, Instructions1, Instructions2,Instructions3,Instructions4,Instructions1_2, Instructions2_2,Instructions3_2, Instructions4_2, Questions, Feedback_Answers, Instructions1_2, Instructions2_2, Instructions3_2,Questions, Fail, Choice_1, Choice_1_stop, Choice_g, Choice_app, Choice_neu, Choice_pol,Choice_soc, Questionnaire_2,Back_to_Prolific]
