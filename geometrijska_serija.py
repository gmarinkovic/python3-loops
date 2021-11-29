# Написати програм који за дате природне бројеве a, b исписује бројеве из интервала [a, b], од којих је први
# број који се исписује једнак a, а сваки следећи је три пута већи од претходног. На пример, за [a, b] = [5, 50]
# треба исписати 5, 15, 45.
#
# Улаз: Са стандардног улаза се учитавају природни бројеви a (1 ≤ a ≤ 50) и b (a ≤ b ≤ 10000 ) сваки у
# посебном реду.
#
# Излаз: На стандардном излазу исписују се сви тражени бројеви, редом (од најмањег до највећег). Сваки
# број исписати у посебној линији.
#
# Пример
# Улаз
# 5
# 50
# Излаз
# 5
# 15
# 45


# ucitavamo interval [a, b]
a = int(input("Uneti prvi broj intervala: "))
b = int(input("Uneti drugi broj intervala: "))

# generisemo i ispisujemo sve trazene brojeve iz intervala [a, b]
i = a
while i <= b:
    print(i)
    i *= 3