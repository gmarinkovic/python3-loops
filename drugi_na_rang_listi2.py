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

# f-ja ucitava n elemenata i odredjuje i vraca najveca dva
def dva_najveca(n):
    if n == 0:
        return (-1, -1)

    (prvi, drugi) = dva_najveca(n-1)
    x = int(input("Unesi bro poena takmicara: "))
    if x > prvi:
        return (x, prvi)
    elif x > drugi:
        return (prvi, x)
    else:
        return (prvi, drugi)

# broj elemenata serije
n = int(input("Unesi broj takmicara: "))

# pozivamo funkciju
(prvi, drugi) = dva_najveca(n)

print("Drugi takmicar sa najvise poena je "+str(drugi))
