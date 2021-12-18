# Такмичари су радили тестове из програмирања, математике и физике. За сваки предмет добили су одређени
# број поена (цео број од 0 до 50). Такмичари се рангирају по укупном броју поена из сва три предмета. Ако
# два такмичара имају исти број поена, победник је онај који има више поена из програмирања. Ако је и
# број поена из програмирања једнак, онда се посматра број поена из математике. На крају, ако је и број
# поена из математике једнак, посматра се број поена из физике. Потребно је написати програм који одређује
# победника такмичења.

# Улаз: Учитава се прво број такмичара, а затим и подаци за сваког такмичара. За сваког такмичара учитава
# се број поена из програмирања, а затим број поена из математике, и на крају број поена из физике, сви у
# истом реду.

# Излаз: Потребно је исписати редни број победника и број његових поена из сваког предмета. Бројање
# такмичара почиње од 1. Ако су два или више такмичара остварила потпуно идентичан успех, победник је
# онај који има мањи редни број (јер је остварио више поена на квалификационом такмичењу).
# Пример
# Улаз
# 4
# 20 30 40
# 10 20 30
# 20 40 30
# 10 50 20
# Излаз
# 3: 20 40 30

# funkcija koja proverava da li je takmicar A losiji od takmicara B
def losiji(progA, matA, fizA, progB, matB, fizB):
    # prvo se poredi ukupan broj poena
    ukupnoA = progA + matA + fizA
    ukupnoB = progB + matB + fizB
    if ukupnoA < ukupnoB:
        return True
    if ukupnoA > ukupnoB:
        return False
    # ukupan broj poena je jednak, pa se porede poeni iz programiranja
    if progA < progB:
        return True
    if progA > progB:
        return False

    # i ukupan broj poena iz programiranja je jednak,
    # pa se porede poeni iz matematike
    if matA < matB:
        return True
    if matA > matB:
        return False

    # i ukupan broj poena iz matematika je jednak,
    # pa se porede poeni iz fizike
    return fizA < fizB

# funkcija koja ucitava poene takmicara iz jedne linije
def ucitajTakmicara():
    prog_str, mat_str, fiz_str = input("Unesi broj poena iz programiranja pa matematike pa fizike: ").split()
    return int(prog_str), int(mat_str), int(fiz_str)

# funkcija koja prikazuje poene takmicara
def prikaziTakmicara(prog, mat, fiz):
    print(prog, mat, fiz)


# ucitavamo broj takmicara
brojTakmicara = int(input("Unesi broj takmicara: "))

# prog, mat, fiz - poeni tekuceg takmicar
# progPobednik, matPobednik, fizPobednik - poeni pobednika
# brojPobednika - redni broj pobednika
# ucitavamo podatke i istovremeno odredjujemo poziciju najveceg elementa,
# kada se poredjenje vrsi u odnosu na relaciju ”losiji”
# ucitavamo poene prvog takmicara
(prog, mat, fiz) = ucitajTakmicara()
# pretpostavljamo da je prvi takmicar pobednik
(progPobednik, matPobednik, fizPobednik) = (prog, mat, fiz)
brojPobednika = 1
for i in range(2, brojTakmicara+1):
    # Ucitavamo poene tekuceg takmicara
    (prog, mat, fiz) = ucitajTakmicara()

    # Ako je dosadasnji pobednik losiji od tekuceg takmicara
    if losiji(progPobednik, matPobednik, fizPobednik, prog, mat, fiz):
    # Za pobednika proglasavamo tekuceg takmicara
        (progPobednik, matPobednik, fizPobednik) = (prog, mat, fiz)
        brojPobednika = i

# Prijavljujemo rezultat
print(brojPobednika, ": ", end="")
prikaziTakmicara(progPobednik, matPobednik, fizPobednik)
