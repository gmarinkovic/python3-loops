# Са рачунара у школи на сајт школе се логују разни ђаци. Сваки пут када се неко улогује то се памти у бази.
# Напиши програм који за дати број рачунара одређује који је први, а који је последњи ђак који се логовао.
#
# Улаз: Са стандардног улаза се у првој линији уноси редни број рачунара који нас занима (цео број од 1 до
# 100), у другој линији се налази укупан број n (1 ≤ n ≤ 50000) логовања, а затим се у наредних n линија
# налазе подаци о појединачним логовањима: број рачунара са којег се неки ђак логовао (цео број од 1 до 100)
# и корисничко име тог ђака (ниска од највише 20 малих слова енглеске абецеде).
#
# Излаз: На стандардни излаз исписати име првог и име последњег ђака који се логовао на тај рачунар (свако
# у посебном реду) или текст nema ако се са тог рачунара нико није логовао.
#
# Пример
# Улаз
# 3
# 5
# 1 zika
# 3 jovana
# 2 ana
# 3 pera
# 3 milica
# Излаз
# jovana
# milica

def unos():
    s ,d = input("Unesi racunar na kom se logovao djak i ime djaka: ").split()
    return int(s), d

a = int(input("Unesi broj racunara za koji nas interesuje prvo i poslednje logovanje: "))
n = int(input("Unesi broj djaka koji su koristili skolske racunare: "))
c = 1

for i in range (0,n):
    a1 , ime = unos()
    if a==a1 :
        if c==1:
            ime1=ime
            ime2=ime
        else:
            ime2=ime
        c=c+1

print("Prvi djak koji se ulogovao na racunaru "+str(a)+" je "+str(ime1))
print("Poslednji djak koji se ulogovao na racunaru "+str(a)+" je "+str(ime2))
