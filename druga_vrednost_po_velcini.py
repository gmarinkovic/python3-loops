# У студентском удружењу се организује наградна игра. Договор је да награде добијају два члана удружења
# која имају највеће бројеве индекса. Проблем је у томе што су на постојећем списку неки студенти уписани
# и више пута. Написати програм који на основу серије бројева индекса са тог списка одређује два награђена
# студента.
#
# Улаз: Прва линија стандардног улаза садржи природан број N (10 ≤ N ≤ 50000) који представља број
# студената на списку. Свака од наредних N линија садржи по један природан број из интервала [1, 50000],
# који представља број индекса студената из удружења. Може се претпоставити да ће на списку постојати бар
# два различита индекса.
#
# Излаз: На стандардном излазу приказати индексе два награђена студента. У првом реду највећу, а у другом
# реду следећу по величини вредност међу бројевима индекса.
#
# Пример
# Улаз
# 5
# 22
# 35
# 71
# 71
# 22
# Излаз
# 71
# 35

n = int(input("Unesi broj elemenata serije: "))

prvi_max = int(input("Unesi prvi element: "))

# drugi maksimum inicjalizujemo na -beskonačno
drugi_max = -1

# obrađujemo sve naredne elemente
for i in range(1, n):
    x = int(input("Unesi naredni element serije: "))

    # ako je potrebno, ažuriramo vrednosti maksimuma
    if x > prvi_max:
        drugi_max = prvi_max
        prvi_max = x
    elif x < prvi_max:
        if (x > drugi_max):
            drugi_max = x

print("Prvi maksimum je: "+ str(prvi_max))
print("Drugi maksimum je: "+str(drugi_max))
