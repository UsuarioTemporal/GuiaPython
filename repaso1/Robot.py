# vida --> 100 --> vivo 0
# revivir ,dar comer, pegar -->-10

def nacimento():
    global vida
    vida = 100
def matar():
    global vida
    vida=0
def pegar():
    global vida
    vida-=10
def alimentar():
    global vida
    vida+=10

def revivir():
    global vida
    vida=100
def laVida():
    global vida
    return vida
nacimento()
pegar()
print(laVida())