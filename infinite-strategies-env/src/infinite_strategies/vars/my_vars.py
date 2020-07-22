import axelrod as axl


# relevant for the single matches only 
base_strategies =	{
    
    "coop": axl.Cooperator(),
    "alter": axl.Alternator(),
    "tft": axl.TitForTat(),
    "tac": axl.FirstByTidemanAndChieruzzi(),
    "nydg": axl.FirstByNydegger(),
    "grof": axl.FirstByGrofman(),
    "shub": axl.FirstByShubik(),
    "sara": axl.FirstBySteinAndRapoport(),
    "grudger": axl.Grudger(),
    "davis": axl.FirstByDavis(),
    "rdown": axl.RevisedDowning(),
    "feld": axl.FirstByFeld(),
    "joss": axl.FirstByJoss(),
    "tull": axl.FirstByTullock(),
    "rand": axl.Random()
}
# used by roundrobin_logic.py for creating the tables
# insert your lists below with your strategies to run your experiments

firstgen_strategies_str = ["Cooperator", "Alternator", "TitForTat", "TidemanAndChieruzzi", "Nydegger", "Grofman",
                "Shubik", "SteinAndRapoport", "Grudger", "Davis", "RevisedDowning", "Feld", "Joss","Tullock", "Random" ]

firstgen_strategies_axl = [  axl.Cooperator(),
                    axl.Alternator(),
                    axl.TitForTat(),
                    axl.FirstByTidemanAndChieruzzi(),
                    axl.FirstByNydegger(),
                    axl.FirstByGrofman(),
                    axl.FirstByShubik(),
                    axl.FirstBySteinAndRapoport(),
                    axl.Grudger(),
                    axl.FirstByDavis(),
                    axl.RevisedDowning(),
                    axl.FirstByFeld(),
                    axl.FirstByJoss(),
                    axl.FirstByTullock(),
                    axl.Random() ]
