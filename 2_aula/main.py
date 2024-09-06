# condições - match
from xxhash import xxh32

ano = 2321423

match ano:
    case 2021:
        print("ano 2021")
    case 2024:
        print("ano 2024")
    case 2030:
        print("ano 2030")
    case _:
        print("outro valor")

# funções

def ola_mundo():
    print("Ola mundo")

ola_mundo()

"""
void ola_mundo2(){
}

"""
def ola_mundo2():
    pass

print("dasdasd")




# param
"""
void ola_mundo3(char nome[100]){
}

"""
def ola_mundo3(nome):
    print(f"Ola mundo, {nome}")


ola_mundo3("Gonçalo")

nome = "Gonçalo"

def ola_mundo4(nome: str):
    print(f"Ola mundo, {nome}")

ola_mundo4("Gonçalo")

ola_mundo4(2034)


def ola_mundo5(nome: str, ano: int):
    print(f"Ola mundo, {nome} em {ano}")


def ola_mundo6(nome: str, ano: int):
    return f"Ola mundo, {nome} em {ano}"

print(ola_mundo6("Gonçalo", 2023))
resp = ola_mundo6("Gonçalo", 2023)


def ola_mundo7(nome: str, ano: int) -> str:
    return f"Ola mundo, {nome} em {ano}"


# None -> nada, vazio | Null

'''
 def ola_mundo():
    print("Ola mundo")
'''

print(ola_mundo())

print("----------")
def demo_None():
    soma = 1 + 3

print(demo_None())


def demo_retv2():
    soma = 1 + 3
    return soma


def demo_retv3(nota1, nota2):
    return nota1 + nota2


'''
= - atribuição
== - eq
'''





# listas



# set



# dict