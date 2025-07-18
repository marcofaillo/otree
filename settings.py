from os import environ


SESSION_CONFIGS = [
    # dict(
    #     name='public_goods',
    #     display_name="Public Goods",
    #     num_demo_participants=3,
    #     app_sequence=['public_goods', 'payment_info'],
    # ),
    # dict(
    #     name='guess_two_thirds',
    #     display_name="Guess 2/3 of the Average",
    #     num_demo_participants=3,
    #     app_sequence=['guess_two_thirds', 'payment_info'],
    # ),
    # dict(
    #     name='survey',
    #     display_name='survey',
    #     num_demo_participants=1,
    #     app_sequence=['survey', 'payment_info'],
    # ),




        # dict(
        #     name='bartling',
        #     display_name='bartling',
        #     num_demo_participants=16,
        #     app_sequence=['bartling'],
        # ),


        # dict(
        #     name='energy',
        #     display_name='energy',
        #     num_demo_participants=4,
        #     treatment =1,
        #     test=1,
        #     app_sequence=['energy', 'faillobret'],
        #
        #     ),
        #
        # dict(
        #     name='labeling',
        #     display_name='labeling',
        #     num_demo_participants=1,
        #     app_sequence=['labeling'],
        #     ),
        # #
        #
        # #
        # dict(
        #     name='FG_baseline_exp_high',
        #     display_name='FG_baseline_exp_high',
        #     num_demo_participants=4,
        #     app_sequence=['FG_baseline_exp_high'],
        #     ),
        # dict(
        #     name='Risk_Second_Order',
        #     display_name='Risk_Second_Order',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Second_Order', 'MPL_F'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','insure_1', 'insure_2','paid_decision','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        # dict(
        #     name='Risk_Second_Order_inv',
        #     display_name='Risk_Second_Order_inv',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Second_Order_inv', 'MPL_F_inv'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','insure_1', 'insure_2','paid_decision','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        # dict(
        #     name='Risk_Third_Order',
        #     display_name='Risk_Third_Order',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Third_Order', 'MPL_F'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','paid_decision','insure_1', 'insure_2','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        # dict(
        #     name='Risk_Third_Order_inv',
        #     display_name='Risk_Third_Order_inv',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Third_Order_inv', 'MPL_F_inv'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','paid_decision','insure_1', 'insure_2','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        #
        #
        #
        # dict(
        #     name='Risk_Mitigation_2nd',
        #     display_name='Risk_Mitigation_2nd',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Mitigation_2nd', 'MPL_F'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','insure_1', 'insure_2','paid_decision','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        # dict(
        #     name='Risk_Mitigation_2nd_inv',
        #     display_name='Risk_Mitigation_2nd_inv',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Mitigation_2nd_inv', 'MPL_F_inv'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','insure_1', 'insure_2','paid_decision','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        #
        # dict(
        #     name='Risk_Mitigation_3rd_inv',
        #     display_name='Risk_Mitigation_3rd_inv',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Mitigation_3rd_inv', 'MPL_F_inv'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','insure_1', 'insure_2','paid_decision','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        #     ),
        #
        # dict(
        #     name='Risk_Mitigation_3rd',
        #     display_name='Risk_Mitigation_3rd',
        #     num_demo_participants=1,
        #     app_sequence=['Risk_Mitigation_3rd', 'MPL_F'],
        #     PARTICIPANT_FIELDS = ['decision_1', 'decision_2','insure_1', 'insure_2','paid_decision','lottery_1','lottery_2', 'second_order'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E'
        #
        # #     ),
        #
        #
        dict(
            name='weingast_citizens_3',
            display_name='weingast_citizens_3',
            num_demo_participants=1,
            app_sequence=['weingast_citizens_3'],
            prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E',
            treatment =3, # 1 = no info,  2 = citizens coalition 3 = citizen-soveireign coalition
            topic = 5 # 1 = immigration, 2 = Gender, 3 =  LGBTQ,  4 = climate change , 5 = income
            ),
        dict(
            name='weingast_sovereign',
            display_name='weingast_sovereign',
            num_demo_participants=1,
            app_sequence=['weingast_sovereign'],
            prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E',
            treatment =3, # 1 = no info,  2 = citizens coalition 3 = P2-soveireign coalition 4 = P3-soveireign coalition
            topic = 1, # 1 = immigration, 2 = Gender, 3 =  LGBTQ,  4 = climate change , 5 = income
            person = 3, # person to which he is associated
            ),


        # dict(
        #     name='paradox_2',
        #     display_name='paradox_2',
        #     num_demo_participants=1,
        #     app_sequence=['paradox_2'],
        #     prolific='https://app.prolific.co/submissions/complete?cc=C1LHTJ3E',
        #     treatment =9, # 3  or 9 ;
        #
        #     ),


        # dict(
        #     name='are_you_sure',
        #     display_name='are_you_sure',
        #     num_demo_participants=1,
        #     app_sequence=['are_you_sure'],
        #     ),



        # dict(
        #     name='choice_list',
        #     display_name='choice_list',
        #     num_demo_participants=1,
        #     app_sequence=['choice_list'],
        #     ),

        #
        # dict(
        #     name='MPL_F',
        #     display_name='MPL_F',
        #     num_demo_participants=1,
        #     app_sequence=['MPL_F'],
        #     ),
        # dict(
        #     name='FG_baseline_exp_low',
        #     display_name='FG_baseline_exp_low',
        #     num_demo_participants=4,
        #     app_sequence=['FG_baseline_exp_low'],
        #     ),

        # dict(
        #     name='FG_mix_no_norm',
        #     display_name='FG_mix_no_norm',
        #     num_demo_participants=8,
        #     app_sequence=['FG_mix_no_norm'],
        #     ),
        #
        #
        # dict(
        #     name='FG_mix_no_norm_24',
        #     display_name='FG_mix_no_norm_24',
        #     num_demo_participants=8,
        #     app_sequence=['FG_mix_no_norm_24'],
        #     ),
        # dict(
        #     name='faillo_content_spanish_pract_gamma5',
        #     display_name='faillo_content_spanish_pract_gamma5',
        #     num_demo_participants=4,
        #     app_sequence=['faillo_content_spanish_pract_gamma5','faillo_content_spanish_exp_gamma5'],
        #     test=0,
        #     ),
        # #
        #
        #
        # dict(
        #     name='pluralistic',
        #     display_name='pluralistic',
        #     num_demo_participants=6,
        #     app_sequence=['pluralistic'],
        #     PARTICIPANT_FIELDS = ['bads', 'goods']
        #
        #     ),

        # dict(
        #     name='pluralistic_v3',
        #     display_name='pluralistic_v3',
        #     num_demo_participants=6,
        #     app_sequence=['pluralistic_v3'],
        #     PARTICIPANT_FIELDS = ['bads', 'goods']
        #
        #     ),
        # dict(
        #     name='simulation_energy',
        #     display_name='simulation_energy',
        #     num_demo_participants=1,
        #     app_sequence=['simulation_energy'],
        #
        # # #     ),
        # dict(
        #     name='energy_boost',
        #     display_name='energy_boost',
        #     num_demo_participants=4,
        #     treatment =1,
        #     app_sequence=['simulation_energy', 'energy_boost', 'faillobret'],
        #
        #     ),
        # #

    #
    # dict(
    #         name='paradox',
    #         display_name='paradox',
    #         num_demo_participants=1,
    #         app_sequence=['paradox'],
    #         treatment =1,
    #     ),

    #
    # dict(
    #         name='paradox_bret',
    #         display_name='paradox_bret',
    #         num_demo_participants=1,
    #         app_sequence=['paradox_bret'],
    #         treatment =1,
    #         prolific='https://app.prolific.co/submissions/complete?cc=17E466F8'
    #     ),



    # dict(
    #         name='lottery',
    #         display_name='lottery',
    #         num_demo_participants=1,
    #         app_sequence=['lottery'],
    #     ),
    #
    # dict(
    #         name='lottery_10',
    #         display_name='lottery_10',
    #         num_demo_participants=1,
    #         app_sequence=['lottery_10'],
    #     ),

    # dict(
    #         name='faillobret',
    #         display_name='faillobret',
    #         num_demo_participants=1,
    #         app_sequence=['faillobret'],
    #     ),
    #
    # dict(
    #     name='zero_rating_3_tarifs',
    #     display_name='zero_rating_3_tarifs',
    #     num_demo_participants=4,
    #     app_sequence=['zero_rating_3_tarifs_practice','zero_rating_3_tarifs_paid' ],
    # ),
    #

        # dict(
        #     name='sif_singolo_L3',
        #     display_name='sif_singolo_L3',
        #     num_demo_participants=1,
        #     app_sequence=['sif_singolo_L3'],
        #     treatment= 1
        #  ),
        #
        # dict(
        #     name='bartling',
        #     display_name='bartling',
        #     num_demo_participants=16,
        #     app_sequence=['bartling'],
        #     treatment= 1
        # ),


        # dict(
        #     name='sif_singolo_no_finanziatore',
        #     display_name='sif_singolo_no_finanziatore',
        #     num_demo_participants=1,
        #     app_sequence=['sif_singolo_no_finanziatore'],
        #     treatment= 1
        #     ),


        # #
        # dict(
        #     name='sif_F',
        #     display_name='sif_F',
        #     num_demo_participants=1,
        #     app_sequence=['sif_F'],
        #     treatment= 1,
        #     L_list="1 2 3 4 5",
        #     L_code="1 2 3 4 5 4"
        # ),
        #
        #         dict(
        #             name='chat',
        #             display_name='chat',
        #             num_demo_participants=1,
        #             app_sequence=['chat'],
        #         ),


        # dict(
        #     name='questionnaire',
        #
        #     display_name="questionnaire",
        #
        #     app_sequence=['questionnaire'],
        #
        #     num_demo_participants=3,
        #
        #     ),
        #
        # dict(
        #     name='Imitation_kappa_0',
        #
        #     display_name="Imitation_kappa_0",
        #
        #     app_sequence=['Imitation_kappa_0','Imitation_kappa_3', 'Imitation_kappa_9', 'questionnaire'],
        #
        #     PARTICIPANT_FIELDS = ['guadagno_cumulato_landscape'],
        #
        #     num_demo_participants=3,
        #
        #     kappa=0, # k values 0,3,9
        #
        #     instructions=1,
        #     order=1, # 1 se ordine 0 3 9  ; 2 se ordine 3 9 0 ; 3 se ordine è 9,0,3. Serve per decidere se visualizzare le istruzioni
        #
        #     error=0,
        #
        #     ),
        #
        # dict(
        #     name='Imitation_kappa_3',
        #
        #     display_name="Imitation_kappa_3",
        #
        #     app_sequence=['Imitation_kappa_3', 'Imitation_kappa_9', 'Imitation_kappa_0',  'questionnaire'],
        #
        #     num_demo_participants=3,
        #
        #     kappa=0, # k values 0,3,9
        #
        #     instructions=1,
        #
        #     error=0,
        #
        #     order=2, # 1 se ordine 0 3 9  ; 2 se ordine 3 9 0 ; 3 se ordine è 9,0,3. Serve per decidere se visualizzare le istruzioni
        #
        #
        #     ),
        #
        # dict(
        #     name='Imitation_kappa_9',
        #
        #     display_name="Imitation_kappa_9",
        #
        #     app_sequence=['Imitation_kappa_9', 'Imitation_kappa_0', 'Imitation_kappa_3',  'questionnaire' ],
        #
        #     num_demo_participants=3,
        #
        #     kappa=0, # k values 0,3,9
        #
        #     instructions=1,
        #
        #     error=0,
        #
        #     order=3, # 1 se ordine 0 3 9  ; 2 se ordine 3 0 0 ; 3 se ordine è 9,0,3. Serve per decidere se visualizzare le istruzioni
        #
        #     ),
        #
        # dict(
        #     name='faillo_np',
        #
        #     display_name="NK with imitation",
        #
        #     app_sequence=['faillo_np'],
        #
        #     num_demo_participants=3,
        #
        #     kappa=9, # k values 0,3,9
        #
        #     instructions=0,
        #
        #     error=0,
        #
        #
        #     last =1,
        #
        #     # fineexp=25,
        #     #
        #     # superadmin=0,
        #     #
        #     # waitstart=0,
        #     #
        #     # type_instructions=2,
        #     ),
        # dict(
        #     name='sif_B_F',
        #     display_name='sif_B_F',
        #     num_demo_participants=1,
        #     app_sequence=['sif_B_F'],
        #     treatment= 1,
        #     L_choice="1 2 3 4 5",
        #     F_choice="1 2 3 4 5 4"
        # ),


]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    # dict(
    #     name='econ101',
    #     display_name='Econ 101 class',
    #     participant_label_file='_rooms/econ101.txt',
    # ),
    # dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
dict(name='energy', display_name='Room for energy(no participant labels)'),

]


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = 'f2$bk1#-4j=*str#tb)w6&!s50olar*#wor5j1xmbr9n+c!u*y'

INSTALLED_APPS = ['otree']
