# Марко је велики обожаватељ скокова у воду и не пропушта ниједно такмичење. Скок се оцењује тако што
# сваки од n судија донесе своју оцену, а затим се најслабија и најбоља оцена одбаце и одреди се просек преосталих оцена. Написати програм којим се одређује Марков резултат на основу судијских оцена.
#
# Улаз: У n (2 < n ≤ 10) линија стандардног улаза налази се по један цео број из интервала [0, 10], ти бројеви
# представљају оцене које је Марко добио. Након тога долази крај улаза (он се може унети помоћу ctrl + z
# у системима Windows или ctrl + d у системима Linux).
#
# Излаз: У првој линији стандардног излаза приказати, на две децимале, Марков резултат.
#
# Пример
# Улаз
# 8
# 7
# 9
# 9
# 5
# Излаз
# 8.00

import sys

ocena = int(input("Unesi ocenu skoka: ")) # ucitavamo prvu ocenu
broj = 1        # broj svih ocena
zbir = ocena    # zbir svih ocena
min = ocena     # najmanja ocena
max = ocena     # najveca ocena

# obradjujemo sve ostale ocene
for linija in sys.stdin:
    ocena = int(linija) # ucitavamo tekucu ocenu
    # azuriramo broj, zbir, minimum i maksimum
    broj = broj + 1
    zbir += ocena

    if ocena < min:
        min = ocena
    elif ocena > max:
        max = ocena

# izracunavamo i ispisujemo prosek preostalih ocena
prosek = (zbir - min - max) / (broj-2)
print(format(prosek, '.2f'))
