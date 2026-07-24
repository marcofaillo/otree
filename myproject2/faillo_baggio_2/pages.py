from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random




class Choice_1(Page):
	form_model = 'player'
	def get_form_fields(self):
		rt = ['slider_' + str(i) for i in range(1, 6)]
		rt.append('play_game_1')
		return rt

	def vars_for_template(self):
		targets = []
		for i in range(1,6):
			targets.append(random.randint(1,100))
		return {
				'ruolo' : self.player.role(),
				'targets' : targets,
				}

class Choice_2(Page):
	form_model = 'player'
	def get_form_fields(self):
		rt = ['slider_' + str(i) for i in range(6, 11)]
		rt.append('play_game_2')
		return rt

	def vars_for_template(self):
		targets = []
		for i in range(6,11):
			targets.append(random.randint(1,100))
		return {
				'ruolo' : self.player.role(),
				'targets' : targets
				}


class Istruzioni(Page):
	form_model = 'player'
	form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']


	def error_message(self, values):
		if values['q1'] != 1:
			self.player.Errors += 1
			return 'La risposta alla domanda 1 è sbagliata'

		if values['q2'] != 2:
			self.player.Errors += 1
			return 'La risposta alla domanda 2 è sbagliata'

		if values['q3'] != 2:
			self.player.Errors += 1
			return 'La risposta alla domanda 3 è sbagliata'

		if values['q4'] != 1:
			self.player.Errors += 1
			return 'La risposta alla domanda 4 è sbagliata'

		if values['q5'] != 7:
			self.player.Errors += 1
			return 'La risposta alla domanda 5 (PARTECIPANTE A) è sbagliata'

		if values['q6'] != 1:
			self.player.Errors += 1
			return 'La risposta alla domanda 5  (PARTECIPANTE B) è sbagliata'
		if self.session.config['treatment'] == 1:
			if values['q7'] != 12:
				self.player.Errors += 1
				return 'La risposta alla domanda 6  (PARTECIPANTE A) è sbagliata'
		else:
			if values['q7'] != 7:
				self.player.Errors += 1
				return 'La risposta alla domanda 6  (PARTECIPANTE A) è sbagliata'

		if values['q8'] != 0:
			self.player.Errors += 1
			return 'La risposta alla domanda 6  (PARTECIPANTE B) è sbagliata'

		if values['q9'] != 6:
			self.player.Errors += 1
			return 'La risposta alla domanda 7 è sbagliata'

		if values['q10'] != 0:
			self.player.Errors += 1
			return 'La risposta alla domanda 7 è sbagliata'

	def is_displayed(self):
		return self.round_number == 1

	def vars_for_template(self):
		return{
			'trattamento': self.session.config['treatment'],
		}


# Pagina di risoluzione slider player A
class Stage_1(Page):
	form_model = 'player'

	def get_form_fields(self):
		rt = ['slider_' + str(i) for i in range(1,4)]
		rt.append('task_type')
		rt.append('task_quality')
		rt.append('tempo_impiegato')
		return rt

	def get_timeout_seconds(self):
		return Constants.seconds_A

	def vars_for_template(self):
		targets = [self.player.participant.vars['target'][self.round_number-1][i] for i in range(0,3)]

		if self.subsession.round_number > 2:
			self.player.mio_round = self.subsession.round_number -2


		else:
			self.player.mio_round = self.subsession.round_number

# pagamento culumalo
		if self.subsession.round_number > 2:

		 	self.player.UMS_cumulati = sum(self.player.participant.vars['UMS'])

		else:

			self.player.UMS_cumulati = 0
			print(self.player.UMS_cumulati)

		return{
			'ruolo' : self.player.role(),
			'tasktype' : self.player.participant.vars['easy_complicated'][self.round_number-1],
			'targets' : targets,
			'round': self.player.mio_round,
			'round_vero': self.subsession.round_number,
			'trattamento': self.session.config['treatment'],
			'UMS': self.player.UMS_cumulati
		}

	def before_next_page(self):
		# sl = [self.player.slider_1,self.player.slider_2,self.player.slider_3]
		# self.player.task_solved = sum(i > 0 for i in sl)
		self.player.set_quality()

	def is_displayed(self):
		return self.player.role() == 'A'


# Calcolo evento stocastico
class StochasticEventWaitPage(WaitPage):

	def after_all_players_arrive(self):
		se = random.randint(1,101) < 20
		for player in self.group.get_players():
			player.stochastic_event = se

# Pagina di risoluzione slider player B
class Stage_2(Page):
	form_model = 'player'

	def get_form_fields(self):
		rt = ['slider_1','tempo_impiegato']
		return rt

	def get_timeout_seconds(self):
		return Constants.seconds_B

	def vars_for_template(self):
		if self.subsession.round_number > 2:
			self.player.mio_round = self.subsession.round_number - 2
		else:
			self.player.mio_round = self.subsession.round_number

	# pagamento culumalo
		if self.subsession.round_number > 2:

			self.player.UMS_cumulati = sum(self.player.participant.vars['UMS'])
			print(self.player.UMS_cumulati)

		else:

			self.player.UMS_cumulati = 0

		return{
			'ruolo' : self.player.role(),
			'stochastic': self.player.stochastic_event,
			'tasktype' : self.group.get_players()[0].participant.vars['easy_complicated'][self.round_number-1],
			'tasksolved' : self.group.get_players()[0].task_solved,
			'target': self.player.participant.vars['target'][self.round_number-1][0],
			'taskquality' : self.group.get_players()[0].task_quality,
			'round': self.player.mio_round,
			'round_vero': self.subsession.round_number,
			'trattamento': self.session.config['treatment'],
			'UMS': self.player.UMS_cumulati
		}

	def before_next_page(self):
		t = self.player.participant.vars['target'][self.round_number-1][0]
		s = self.player.slider_1
		self.player.task_solved = int(s == t)
		# self.player.task_solved = int(s >= t - 5 and s <= t + 5)

	def is_displayed(self):
		return self.player.role() == 'B'

# Calcolo evento stocastico
class EndRoundWaitPage(WaitPage):

	wait_for_all_groups = True
	def after_all_players_arrive(self):
		self.subsession.set_payoff()

class EndRound(Page):
	def vars_for_template(self):
		if self.subsession.round_number > 2:
			self.player.mio_round = self.subsession.round_number -2
		else:
			self.player.mio_round = self.subsession.round_number

		# if self.player.role() == 'A' and self.player.payoff_round == 0 and self.player.task_solved > 0:
		# 	payoff_dovuto = 1
		# else:
		# 	payoff_dovuto = 0
		return{
			'payoffround' : self.player.payoff_round,
			'ruolo': self.player.role(),
			'slidersvolti': self.player.task_solved,
			#'payoff_dovuto': payoff_dovuto,
			'tempo_residuo': self.player.tempo_residuo,
			'trattamento': self.session.config['treatment'],
			'taskquality': self.group.get_players()[0].task_quality,
			'task_quality_A' : self.player.task_quality,
			'altro_risolve': self.player.altro_risolve,
			'stochastic_event': self.player.stochastic_event,
			'payoff_secondi' : self.player.payoff_secondi,
			'round': self.player.mio_round,
			'round_vero': self.subsession.round_number,
			'UMS': self.player.UMS_cumulati,
		}

#fine del round di prova
class EndTest(Page):
	def is_displayed(self):
		return self.round_number==2

#inizio round di prova
class Test(Page):
	def vars_for_template(self):
		return {'ruolo' : self.player.role()}

	def is_displayed(self):
		return self.round_number == 1

#pagamento finale
class Pagamento(Page):
	def vars_for_template(self):

		# pagamento culumalo
		if self.subsession.round_number > 2:

			self.player.UMS_cumulati = sum(self.player.participant.vars['UMS'])

		else:

			self.player.UMS_cumulati = 0

		return {
		'ruolo' : self.player.role(),
		'finalpay': self.participant.payoff,
		'finalmoney': self.participant.payoff_plus_participation_fee(),
		'UMS': self.player.UMS_cumulati
		}

	def is_displayed(self):
		return self.round_number == Constants.num_rounds

#questionario
class Questionario(Page):
	form_model = 'player'

	def get_form_fields(self):
		rt = ['age','sex','num_experiments','faculty']
		return rt

	def is_displayed(self):
		return self.round_number == Constants.num_rounds

page_sequence = [
	Istruzioni,
	Test,
	Stage_1,
	StochasticEventWaitPage,
	Stage_2,
	EndRoundWaitPage,
	EndRound,
	EndTest,
	Pagamento,
	Questionario,

]
