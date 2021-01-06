import axelrod as axl

# Include a list of parametrized strategies

#### ORDER MUST BE THE SAME AS FIRSTEN_STR TYPE
firstgen_str_text = [   "Cooperator", "Alternator", "TitForTat", "TidemanAndChieruzzi", "Nydegger", "Grofman",
                        "Shubik", "SteinAndRapoport", "Grudger", "Davis", "RevisedDowning", "Feld", "Joss","Tullock", "Random" ]

firstgen_str_type = [       axl.Cooperator(),   
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
#### ORDER MUST BE THE SAME AS FISTGEN STR STR(TEXT)
secondgen_str_text = [  "Champion", "Eatherley", "Tester", "Gladstein", "Tranquilizer", "SecGrofman", "Kluepfel", "Borufsen", "Cave",
                        "WmAdams", "GraaskampKatzen", "Weiner", "Harrington", "SecTidemanAndChieruzzi", "Getzler", "Leyvraz", "White", "Black",
                        "RichardHufford", "Yamachi", "Colbert", "Mikkelson", "Rowsam", "Appold"]

secondgen_str_type = [  axl.SecondByChampion(),   
                        axl.SecondByEatherley(),
                        axl.SecondByTester(),
                        axl.SecondByGladstein(),
                        axl.SecondByTranquilizer(),
                        axl.SecondByGrofman(),
                        axl.SecondByKluepfel(),
                        axl.SecondByBorufsen(),
                        axl.SecondByCave(),
                        axl.SecondByWmAdams(),
                        axl.SecondByGraaskampKatzen(),
                        axl.SecondByWeiner(),
                        axl.SecondByHarrington(),
                        axl.SecondByTidemanAndChieruzzi(),
                        axl.SecondByGetzler(),
                        axl.SecondByLeyvraz(),
                        axl.SecondByWhite(),
                        axl.SecondByRichardHufford(),
                        axl.SecondByYamachi(),
                        axl.SecondByColbert(),
                        axl.SecondByMikkelson(),
                        axl.SecondByRowsam(),
                        axl.SecondByAppold() ]


players = secondgen_str_type

# players = [s() for s in axl.strategies] + parameterized_players
# players.sort(key=lambda p:p.__repr__())
