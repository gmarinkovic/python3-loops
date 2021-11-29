# За дате целе бројеве a и b, написати програм који исписује редом све парне троцифрене бројеве који припадају датом интервалу [a, b]
#
# Улаз: Са стандардног улаза учитавају се бројеви a и b (0 ≤ a ≤ 1500 и a ≤ b ≤ 1500).
#
# Излаз: На стандардном излазу исписују се редом (од најмањег до највећег) сви парни троцифрени бројеви,
# у свакој линији по један број.
#
# Пример
# Улаз
# 85
# 109
# Излаз
# 100
# 102
# 104
# 106
# 108

# ucitavamo interval [a, b]
a = int(input("Unesi prvi broj intervala: "))
b = int(input("Unesi drugi broj intervala: "))

# odredjujemo presek sa intervalom [100, 999]
od = max(a, 100)     # ako je prvi broj intervala manji od 100 onda uzima prvi trocifreni broj
do = min(b, 999)     # ako je drugi broj intervala veci od 999 onda uzima poslednji trocifreni broj

# osiguravamo da levi i desni kraj budu parni brojevi
if (od % 2 != 0):       # ako je npr 127 onda se on postavlja na prvi veci tj na 128
    od = od + 1
if (do % 2 != 0):       # ako je npr 773 onda se on postavlja na prvi manji tj na 772
    do = do - 1

# vrsimo iteraciju i ispisujemo sve trazene brojeve
for i in range(od, do+1, 2):
    print(i)
