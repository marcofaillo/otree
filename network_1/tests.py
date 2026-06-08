from otree.api import Bot, Submission
from . import *


class PlayerBot(Bot):

    def play_round(self):

        # Landing
        yield Submission(Landing, dict(proceed=1), check_html=False)

        # Se test=0, queste pagine appaiono
        if self.session.config['test'] == 0:
            yield Submission(Instructions1, check_html=False)
            yield Submission(Instructions2, check_html=False)
            yield Submission(Instructions3, check_html=False)
            yield Submission(Instructions4, check_html=False)
            yield Submission(Instructions5, dict(re_read=0), check_html=False)

            yield Submission(
                Questions,
                dict(q_1=11, q_2=12, q_3=False, q_4=True),
                check_html=False
            )

        # Stage 1
        if self.player.id_in_group == 1:
            yield Submission(
                Choice_1_A,
                dict(choice_1_A_B=3, choice_1_A_C=4),
                check_html=False
            )
        elif self.player.id_in_group == 2:
            yield Submission(
                Choice_1_B,
                dict(choice_1_B_A=2, choice_1_B_C=5),
                check_html=False
            )
        else:
            yield Submission(
                Choice_1_C,
                dict(choice_1_C_A=1, choice_1_C_B=6),
                check_html=False
            )

        yield Submission(See_declaration, check_html=False)

        # Stage 2
        if self.player.id_in_group == 1:
            yield Submission(
                Choice_2_A,
                dict(choice_2_A_B=3, choice_2_A_C=4),
                check_html=False
            )
        elif self.player.id_in_group == 2:
            yield Submission(
                Choice_2_B,
                dict(choice_2_B_A=2, choice_2_B_C=5),
                check_html=False
            )
        else:
            yield Submission(
                Choice_2_C,
                dict(choice_2_C_A=1, choice_2_C_B=6),
                check_html=False
            )

        yield Submission(See_information, check_html=False)

        # Stage 3
        if self.player.id_in_group == 1:
            yield Submission(
                Choice_3_A,
                dict(choice_3_A_B=4, choice_3_A_C=2),
                check_html=False
            )
        elif self.player.id_in_group == 2:
            yield Submission(
                Choice_3_B,
                dict(choice_3_B_A=5, choice_3_B_C=3),
                check_html=False
            )
        else:
            yield Submission(
                Choice_3_C,
                dict(choice_3_C_A=6, choice_3_C_B=1),
                check_html=False
            )

        yield Submission(Final_feedback, check_html=False)

        yield Submission(
            Questionnaire,
            dict(student=1, employment=1, comment='Bot test'),
            check_html=False
        )

        yield Submission(Back_to_Prolific, check_html=False)
