import autode as ade
ade.Config.n_cores = 8

### predefinitions for running ORCA calculations -> level of theory: GFN2-XTB
kwds = ade.Config.ORCA.keywords
kwds.sp = ['SP', 'PBE0', 'def2-SVP']
kwds.opt = ['Opt', 'XTB2']
kwds.low_opt = ['Opt', 'XTB2']
kwds.hess = ['NumFreq', 'XTB2']
kwds.grad = ['EnGrad', 'XTB2']
kwds.opt_ts = ['OptTS', 'NumFreq', 'XTB2']
kwds.optts_block = ('%geom\n'
                    'NumHess true\n'
                    'Calc_Hess true\n'
                    'Recalc_Hess 30\n'
                    'Trust -0.1\n'
                    'MaxIter 150\n'
                    'end')

### the method that gets the reaction notation (in SMILES form) and returns a reaction profile (Delta G vs. reaction pathway)
rxn = ade.Reaction('C=CC=C.C=C>>C1=CCCCC1', name='DA')
rxn.calculate_reaction_profile()
