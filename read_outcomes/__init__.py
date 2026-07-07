from otree.api import *
import csv
from pathlib import Path


doc = """NetROL Discrimination experiment: read outcomes"""

# ricorda di creare il file con google sheet !!!!""

class C(BaseConstants):
    NAME_IN_URL = 'read_outcomes'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
     pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    PID = models.StringField(label='Insert your Prolific ID')
    name = models.IntegerField()
    round = models.StringField()
    stopped_round1 = models.IntegerField()
    own_choice_1 = models.IntegerField()
    partner_choice_1 = models.IntegerField()
    char_own = models.StringField()
    char_match = models.StringField()
    sent_own = models.IntegerField()
    sent_match= models.IntegerField()
    rank_own=models.IntegerField()
    rank_match=models.IntegerField()
    impl_own=models.StringField()
    impl_match=models.StringField()
    payoff_points =models.IntegerField()
    payment=models.FloatField()


def look_up(input_id):
    # percorso del file CSV dentro la cartella dell'app
    file_path = Path(__file__).parent / 'outcomes.csv'

    with open(file_path, encoding='utf-8-sig') as f:
        righe = csv.DictReader(f)
        for riga in righe:
            if riga['PID'].strip() == input_id.strip():
                return riga
    return None

class Prolific_ID(Page):
    form_model = 'player'
    form_fields = ['PID']

    @staticmethod
    def error_message(player, values):
        riga = look_up(values['PID'])
        if riga is None:
            return 'ID not found.'

    @staticmethod
    def before_next_page(player, timeout_happened):
        riga = look_up(player.PID)
        player.round = str(riga['round'])
        player.stopped_round1 = int(riga['stopped_round1'])
        player.char_own = str(riga['char_own'])
        player.char_match = str(riga['char_match'])
        player.sent_own = int(riga['sent_own'])
        player.sent_match = int(riga['sent_match'])
        player.rank_own= int(riga['rank_own'])
        rank_match=player.rank_match = int(riga['rank_match'])
        player.impl_own = str(riga['impl_own'])
        player.impl_match = str(riga['impl_match'])
        player.payoff_points=int(riga['payoff_points'])
        player.payment = float(riga['payment'])


class Show_results(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            id=player.PID,
            round=player.round,
            stopped_round1 = player.stopped_round1,
            car_own=player.char_own,
            car_match=player.char_match,
            sent_own=player.sent_own,
            sent_match=player.sent_match,
            rank_own=player.rank_own,
            rank_match=player.rank_match,
            impl_own=player.impl_own,
            impl_match=player.impl_match,
            payment=player.payment,
            payoff_points =player.payoff_points,

        )



page_sequence = [Prolific_ID,Show_results]
