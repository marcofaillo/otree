from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions_intro (Page):

    def vars_for_template(self):
        self.player.genera_codice()
        return{
         'codice': self.player.codice,
         }



class Instructions_dict (Page):
        form_model = 'player'
        form_fields = ['q1_dict', 'q2_dict', 'q3_dict', 'q4_dict', 'q5_dict', 'q6_dict', 'q7_dict','q8_dict']

        def vars_for_template(self):
            return{
             'endowment_dict': Constants.endowment_dict,
             }


        def error_message(self, values):
            if values['q1_dict'] != 0:
                self.player.errors_dict += 1
                return 'La risposta alla domanda n. 1 è sbagliata'

            if values['q2_dict'] != 10:
                self.player.errors_dict += 1
                return 'La risposta alla domanda n. 2 è sbagliata'

            if values['q3_dict'] != 3:
                self.player.errors_dict += 1
                return 'La risposta alla domanda n. 3 è sbagliata'

            if values['q4_dict'] != 7:
                self.player.errors_dict += 1
                return 'La risposta alla domanda n. 4 è sbagliata'

            if values['q5_dict'] != 5:
                self.player.errors_dict += 1
                return 'La risposta alla domanda n. 5 è sbagliata'

            if values['q6_dict'] != 5:
                self.player.errors_dict += 1
                return 'La risposta alla domanda n. 6 è sbagliata'

            if values['q7_dict'] != 10:
                self.player.errors_dict+= 1
                return 'La risposta alla domanda n. 7 è sbagliata'

            if values['q8_dict'] != 0:
                self.player.errors_dict+= 1
                return 'La risposta alla domanda n. 8 è sbagliata'


class dict (Page):
        form_model = 'player'
        form_fields = ['dict']

        def vars_for_template(self):
            return
            {'endowment_dict':self.Constants.endowment_dict}


#
# class ResultsWaitPage(WaitPage):
#     def after_all_players_arrive(self):
#         pass


class Results(Page):
    pass


page_sequence = [
Instructions_intro,
Instructions_dict,
# dict,
# dict_db,
# dict_nb,
# Instructions_take,
# take,
# take_db,
# take_nb,
# Instructions_pd,
# pd,
# pd_db,
# pd_nb,
# Instructions_trustor,
# trust_trustor,
# trust_trustor_db,
# trust_trustor_b_trustee,
# trust_trustor_nb,
# # Instructions_trustee,
# # trust_trustee,
# # trust_trustee_db,
# # trust_trustee_nb,
# Results,


]
