from otree.api import Bot, Submission
import random as r
from . import *


class PlayerBot(Bot):

    def play_round(self):

        # Variabili player che non vengono compilate da pagine
        self.player.person = self.player.id_in_group
        self.player.id_player = self.player.participant.id_in_session
        self.player.gender = r.choice([1, 2, 3])
        self.player.wrong_answers = ''
        self.player.first = True
        self.player.next_rounds = 0

        # Landing
        yield Submission(Landing, dict(proceed=1), check_html=False)

        # Instructions + comprehension questions
        if self.session.config['test'] == 0:
            yield Instructions1
            yield Instructions2
            yield Instructions3
            yield Instructions4
            yield Submission(Instructions5, dict(re_read=0),check_html=False)

            yield Submission(
                Questions,
                dict(
                    q_1=11,
                    q_2=12,
                    q_3=False,
                    q_4=True
                ),check_html=False
            )

        # Stage 1
        if self.player.id_in_group == 1:
            yield Submission(
                Choice_1_A,
                dict(
                    choice_1_A_B=r.randint(0, 10),
                    choice_1_A_C=r.randint(0, 10)
                ),check_html=False
            )

        elif self.player.id_in_group == 2:
            yield Submission(
                Choice_1_B,
                dict(
                    choice_1_B_A=r.randint(0, 10),
                    choice_1_B_C=r.randint(0, 10)
                ),check_html=False
            )

        else:
            yield Submission(
                Choice_1_C,
                dict(
                    choice_1_C_A=r.randint(0, 10),
                    choice_1_C_B=r.randint(0, 10)
                ),check_html=False
            )

        yield See_declaration

        # Stage 2
        if self.player.id_in_group == 1:
            yield Submission(
                Choice_2_A,
                dict(
                    choice_2_A_B=r.randint(0, 10),
                    choice_2_A_C=r.randint(0, 10)
                ),check_html=False
            )

        elif self.player.id_in_group == 2:
            yield Submission(
                Choice_2_B,
                dict(
                    choice_2_B_A=r.randint(0, 10),
                    choice_2_B_C=r.randint(0, 10)
                ),check_html=False
            )

        else:
            yield Submission(
                Choice_2_C,
                dict(
                    choice_2_C_A=r.randint(0, 10),
                    choice_2_C_B=r.randint(0, 10)
                ),check_html=False
            )

        yield See_information

        # Stage 3
        if self.player.id_in_group == 1:
            yield Submission(
                Choice_3_A,
                dict(
                    choice_3_A_B=r.randint(0, 10),
                    choice_3_A_C=r.randint(0, 10)
                ),check_html=False
            )

        elif self.player.id_in_group == 2:
            yield Submission(
                Choice_3_B,
                dict(
                    choice_3_B_A=r.randint(0, 10),
                    choice_3_B_C=r.randint(0, 10)
                ),check_html=False
            )

        else:
            yield Submission(
                Choice_3_C,
                dict(
                    choice_3_C_A=r.randint(0, 10),
                    choice_3_C_B=r.randint(0, 10)
                ),check_html=False
            )

        yield Final_feedback

        yield Submission(
            Questionnaire,
            dict(
                student=r.choice([0, 1]),
                employment=r.choice([1, 2, 3, 4, 5, 6]),
                comment='Bot-generated observation'
            ),check_html=False
        )

        yield Submission(Back_to_Prolific, check_html=False)
