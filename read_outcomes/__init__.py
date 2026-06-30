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
    entered_id = models.StringField(label='Insert your Prolific ID')
    round = models.StringField()
    car_own = models.StringField()
    car_match = models.StringField()
    sent_own = models.IntegerField()
    sent_match= models.IntegerField()
    rank_own=models.IntegerField()
    rank_match=models.IntegerField()
    impl_own=models.StringField()
    impl_match=models.StringField()
    payment=models.IntegerField()


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
    form_fields = ['entered_id']

    @staticmethod
    def error_message(player, values):
        riga = look_up(values['entered_id'])
        if riga is None:
            return 'ID not found.'

    @staticmethod
    def before_next_page(player, timeout_happened):
        riga = look_up(player.entered_id)

        player.round = str(riga['round'])
        player.car_own = str(riga['car_own'])
        player.car_match = str(riga['car_match'])
        player.sent_own = int(riga['sent_own'])
        player.sent_match = int(riga['sent_match'])
        player.rank_own= int(riga['rank_own'])
        rank_match=player.rank_match = int(riga['rank_match'])
        player.impl_own = str(riga['impl_own'])
        player.impl_match = str(riga['impl_match'])
        payment=player.payment = int(riga['payment'])


class Show_results(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            id=player.entered_id,
            round=player.round,
            car_own=player.car_own,
            car_match=player.car_match,
            sent_own=player.sent_own,
            sent_match=player.sent_match,
            rank_own=player.rank_own,
            rank_match=player.rank_match,
            impl_own=player.impl_own,
            impl_match=player.impl_match,
            payment=player.payment,

        )



page_sequence = [Prolific_ID,Show_results]
