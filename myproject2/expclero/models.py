from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Marco Faillo'

doc = """
Software esperimento CLERO
"""


class Constants(BaseConstants):
    name_in_url = 'expclero'
    players_per_group = None
    num_rounds = 1
    endowment_dict=10
    max_take=10
    endowment_trust=4
    mult_trust=3
    sessione='1'



class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.participant.vars['codici']= ['84PME', 'LFW3U', 'XC7HF', 'Y1T46', 'JOGRI', 'MNF9Y', 'GRVKZ', 'OULZ2', 'W33UA', 'X10XK', '3T4LF', 'CD560', '4FPV0', 'HE2E1', '2TZMG', 'HFBU3', '8780F', '8LRKP', 'Q0RSK', 'C4QZU', 'B7TKO', '4RWHU', 'UF9G7', '73E8B', 'RU8NR', 'UL6U7', 'PTMHF', 'PDTEO', 'PF4JB', 'C63RU', 'T1JTR', 'BSLUU', 'TRURT', 'JTMCS', 'IRXU3', 'OK5OS', '7JCLG', '9Q36R', 'HQMA5', 'ZS80V', 'B8376', 'DIE3Q', '0ER6A', '9U91C', 'Y5PJG', '1O8J7W', '1JT8X', '3PR7Y', '9A1A6', '17T8V', 'XTTTP', 'GKA3I', 'EC6D8', 'HETX9', 'V5H29', 'GFYNM', 'FZQ1I', '5WWTV', '1015H', 'RL4X5', 'N5Z56', 'TCAEQ', 'BWGKI', 'NE2KY', 'YHBRF', 'NL2KU', 'V6KVP', 'GW96F', '0F8FV', 'MD0F5', '8XRSK', '5XSQV', 'WMHG2', '41DC0', 'PVV3M', 'LAIHC', '50EMZ', 'Z9LAP', 'DROR9', '5MP52', 'V785J', 'BROTH', 'WQT1W', 'MUQ3D', 'ZTGF0', '8ZERN', 'WCR7W', 'US81Q', '2XPX8', 'L1NS6', 'N3WDK', '0CTMN', 'HQSUD', 'QCAPB', 'Z95L3', 'YFGZA', 'Z3SIG', 'WA7M7', '3P7CJ', 'YOQBK', '4WN1L', 'XLPFB', 'XCD7R', 'N12RD', 'T4BRH', 'YQ38V', '3BD5W', '5NSOH', '7C2QS', '5UP4B', 'PIRN2', 'YZ3SK', 'XOWZ2', '7935P', 'JT2SG', '4D3EX', '7MUF1', 'OKI8Z', 'TXB9K', 'GIJ53', 'GEAFP', 'IFF8C', 'WYM5M', '5YJKS', 'GHHSV', 'M561T', 'DRJGN', '6DHMF', 'XY7XY', 'AY9QU', '81GPK', 'CQMJ3', 'IKH17', 'Z7DYQ', 'EOERJ', 'ZOJJP', 'J2N78', 'KY69D', '2VBBX', 'YC7UL', '7TB3A', '48MQZ', 'G798O', 'TOMJN', 'NFN6G', 'O9CAU', 'JPD17', 'ZWVRM', '6VGOH', 'NEFAF']

class Group(BaseGroup):
    pass


class Player(BasePlayer):
        dict=models.IntegerField(min=0, max=Constants.endowment_dict, initial=0) #scelta dictator
        dict_db = models.IntegerField(min=0, max=Constants.endowment_dict, initial=0) #aspettative descrittive
        dict_nb_1 = models.IntegerField(min=0, max=Constants.endowment_dict, initial=0) #aspettative normative I grado
        dict_nb_2 = models.IntegerField(min=0, max=Constants.endowment_dict, initial=0) #aspettative normative II grado
        take = models.IntegerField(min=0, max=Constants.max_take, initial=0) #scelta taking
        take_db = models.IntegerField(min=0, max=Constants.max_take, initial=0) #aspettative descrittive
        take_nb_1 = models.IntegerField(min=0, max=Constants.max_take, initial=0) #aspettative normative I grado
        take_nb_2 = models.IntegerField(min=0, max=Constants.max_take, initial=0) #aspettative normative II grado
        pd=models.IntegerField(min=0, max=1) #scelta PD
        pd_db = models.IntegerField(min=0, max=1) #aspettative descrittive
        pd_nb_1 = models.IntegerField(min=0, max=1) #aspettative normative I grado
        pd_nb_2 = models.IntegerField(min=0, max=1) #aspettative normative II grado
        trust =models.IntegerField(min=0, max=4) #scelta PD
        trust_db = models.IntegerField(min=0, max=1) #aspettative descrittive
        trsut_trustee_bel=models.IntegerField(min=0, max=1) #aspettative su trustee
        trust_nb_1 = models.IntegerField(min=0, max=1) #aspettative normative I grado
        trust_nb_2 = models.IntegerField(min=0, max=1) #aspettative normative II grado
        codice = models.StringField()
        errors_dict=models.IntegerField(min=0, max=1, initial=0)
        errors_take=models.IntegerField(min=0, max=1, initial=0)
        errors_pd=models.IntegerField(min=0, max=1, initial=0)
        errors_trust=models.IntegerField(min=0, max=1, initial=0)
        q1_dict = models.IntegerField()
        q2_dict = models.IntegerField()
        q3_dict = models.IntegerField()
        q4_dict = models.IntegerField()
        q5_dict =models.IntegerField()
        q6_dict = models.IntegerField()
        q7_dict = models.IntegerField()
        q8_dict = models.IntegerField()





        def genera_codice(self):
            self.codice=random.sample(self.participant.vars['codici'],1)[0] #estrae un codice e aggiunge il numero della sessione davanti
            self.codice = Constants.sessione + self.codice

            print(self.codice)
