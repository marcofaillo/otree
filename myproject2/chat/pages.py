from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Instructions_1(Page):

    def vars_for_template(self):
        return dict(
            nickname = self.player.chat_nickname()
        )


page_sequence = [
 # ProlificID,
  Instructions_1,

]
