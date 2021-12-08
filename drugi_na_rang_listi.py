# На основу резултата такмичењу на којем је учествовало N ученика формирана је ранг листа. Ранг листа
# се формира у нерастућем поретку по резултатима, од најбољег до најлошијег резултата. Написати програм
# којим се одређује број поена такмичара који је други на ранг листи.
#
# Улаз: Прва линија стандардног улаза садржи природан број N (1 ≤ N ≤ 50000) који представља број
# такмичара. У свакој од наредних N линија налази се цео број из интервала [0, 50000], ти бројеви представљају
# резултате такмичара, који нису сортирани по поенима, већ по бројевима рачунара за којима су такмичари
# седели.
#
# Излаз: У једној линији стандардног излаза приказати број поена другог такмичара на ранг листи.
#
# Пример
# Улаз
# 5
# 80
# 95
# 75
# 50
# 95
# Излаз
# 95

# broj elemenata serije
n = int(input("Unesi broj takmicara: "))

# prvi i drugi maksimum inicijalizujemo na -beskonačno
prvi_max = -1
drugi_max = -1

for i in range(0, n):

    # učitavamo poene takmicara sukcesivno
    x = int(input("Unesi broj poena takmicara: "))

    # ažuriranje vrednosti maksimuma
    if x > prvi_max:
        drugi_max = prvi_max
        prvi_max = x
    elif x > drugi_max:
        drugi_max = x

print("Drugi maksimalni broj je "+str(drugi_max))
