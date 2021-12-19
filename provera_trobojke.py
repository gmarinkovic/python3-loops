# Напиши програм који проверава да ли су бројеви који се уносе уређени тако да прво иду негативни, затим
# нуле и на крају позитивни бројеви (могуће је и да било којих од наведених бројева нема).
#
# Улаз: Са стандардног улаза се уноси број бројева n (1 ≤ n ≤ 20), а након тога и сами бројеви, сваки у
# посебном реду.
#
# Излаз: На стандардни излаз исписати da ако су бројеви уређени како је наведено тј. ne у супротном.
#
# Пример
# Улаз
# 5
# -3
# -1
# 0
# 4
# 2
# Излаз
# da

def unos():
    x = int(input("Unesi broj: "))
    return x

def status(x):
    if x < 0:
        status = 1
    elif x == 0:
        status = 2
    else:
        status = 3
    return status

n = int(input("Unesi broj unosa: "))

x = unos()
status_x = status(x)
provera = True

for i in range (1,n):
    y = unos()
    status_y = status(y)

    if status_x > status_y:
        provera = False
        break

    status_x = status_y

if provera:
    print("da")
else:
    print("ne")
