from otree.api import Bot, Submission
from . import *
import random


def c():
    return random.randint(0, 10)


def submit(page, data=None):
    return Submission(page, data or {}, check_html=False)


class PlayerBot(Bot):

    def play_round(self):

        yield submit(Landing, dict(proceed=1))

        yield submit(Questionnaire_1, dict(
            gender=random.choice([1, 2, 3]),
            activity=random.choice([1, 2, 3]),
            height=random.randint(150, 195),
            weight=random.randint(45, 110),
            politics=random.choice([1, 2, 3]),
            ladder=random.randint(1, 10),
            risk_1=random.randint(1, 10),
        ))

        if self.session.config["test"] == 0:
            yield submit(Instructions1)
            yield submit(Instructions2)
            yield submit(Instructions3)
            yield submit(Instructions4, dict(re_read=0))

            yield submit(Questions, dict(
                q_1=13,
                q_2=13,
                q_3=6,
                q_4=12,
            ))

        yield submit(Choice_1, dict(choice_1=c()))
        yield submit(Choice_1_stop, dict(next_rounds=1))

        yield submit(Choice_g, dict(
            choice_g_1=c(),
            choice_g_2=c(),
            choice_g_3=c(),
        ))

        yield submit(Choice_app, dict(
            choice_app_1=c(),
            choice_app_2=c(),
            choice_app_3=c(),
        ))

        yield submit(Choice_neu, dict(
            choice_neu_1=c(),
            choice_neu_2=c(),
            choice_neu_3=c(),
        ))

        yield submit(Choice_pol, dict(
            choice_pol_1=c(),
            choice_pol_2=c(),
            choice_pol_3=c(),
            choice_pol_4=c(),
        ))

        yield submit(Choice_soc, dict(
            choice_soc_1=c(),
            choice_soc_2=c(),
            choice_soc_3=c(),
        ))

        ranks = random.sample([1, 2, 3, 4, 5], 5)

        yield submit(Ranking, dict(
            rank_app=ranks[0],
            rank_g=ranks[1],
            rank_neu=ranks[2],
            rank_pol=ranks[3],
            rank_soc=ranks[4],
        ))

        yield submit(Questionnaire_2, dict(
            student=random.choice([0, 1]),
            employment=random.randint(1, 6),
            religiosity=random.randint(1, 4),
            siblings=random.randint(1, 3),
            risk_2=random.randint(1, 10),
            holidays=random.randint(1, 3),
            comment="Bot simulation",
        ))

        yield submit(Back_to_Prolific)
        yield submit(Stop)
