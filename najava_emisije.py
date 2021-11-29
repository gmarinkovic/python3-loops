# Познат је почетак и крај једног филма (времена у сатима и минутима). У правилним временским интервалима,
# прво на почетку филма и затим након сваких m минута у углу екрана се приказује најава следеће емисије.
# Напиши програм који исписује времена у којима се приказује та најава.
#
# Улаз: На стандардном улазу налази се време почетка филма дато у облику два цела броја, сваког у засебној
# линији који представљају број сати и број минута, затим, у следеђој линији време завршетка филма дато у
# истом облику и на крају један цео број који представља интервал у минутима у којем се приказује најава.
#
# Излаз: На стандардном излазу приказати, времена емитовања најаве у облику h:m, свако у засебном реду.
#
# Пример
# Улаз
# 12
# 0
# 13
# 23
# 15
#
# Излаз
# 12:0
# 12:15
# 12:30
# 12:45
# 13:0
# 13:15

def u_minute(h, m):
    return h * 60 + m

def od_minuta(M):
    m = M % 60
    h = M // 60
    return (h, m)

# vreme pocetka filma
hPocetak = int(input("Unesi sate pocetka filma: "))
mPocetak = int(input("Unesi minute pocetka filma: "))
pocetak = u_minute(hPocetak, mPocetak)

# vreme zavrsetka filma
hKraj = int(input("Unesi sate kraja filma: "))
mKraj = int(input("Unesi minute kraja filma: "))
kraj = u_minute(hKraj, mKraj)

# interval u kojem se emituju najave
interval = int(input("Unesi interval prikazivanje najave emisije: "))

# izracunavamo vremena u kojima se emituje najava i ispisujemo ih
for najava in range(pocetak, kraj+1, interval):
    # prebacivanja iz ukupnih minuta u odgovarajuce sate i minute
    (hNajava, mNajava) = od_minuta(najava)
    print(hNajava, ":", mNajava, sep="")
