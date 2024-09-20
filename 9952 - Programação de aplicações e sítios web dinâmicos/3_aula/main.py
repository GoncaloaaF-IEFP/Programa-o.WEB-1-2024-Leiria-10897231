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

alunos = ["João", "Rita", "Luis", "Pedro", "Ana"]

print(alunos[0])

alunos[0] = "Maria"

print(alunos[0])
alunos.append("Maria")
print(alunos)

alunos.insert(1, "Maria Joana")
print(alunos)

print(len(alunos))
print(alunos.__len__())

print("-- Count -- ")
print(alunos.count("Maria"))
print(alunos.count("Ana"))


print(alunos.index("Maria"))

alunos.pop() # remove o ultimo elm

print(alunos)


alunos.pop(3) # remove o elm no index 3


alunos.append("Rita")
print(alunos)
alunos.remove("Rita")
print(alunos)

alunos.sort()
print(alunos)

alunos.reverse()
print(alunos)

alunos.extend(["nome 1", "nome 2"])

print(alunos)

alunos.extend("Gonçalo")
print(alunos)

alunos.append(12)

print(alunos)

print("-------")

nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia",
    "Paulo", "Quintino", "Raquel", "Samuel", "Tatiana",
    "Ursula", "Vitor", "Wesley", "Xavier", "Yasmin"
]


print(nomes)
print(nomes[0])

"""

[:n] # elm das pos 0 a pos n-1
[n:m] elm da pos n ate a pos-1

[n:m:s] elm da pos n ate a pos-1  de s em s pos  


[:] mostra todos os elm da lista
"""

print(nomes[:])
print(nomes[:5])
print(nomes[5:10])
print(nomes[1:20:3])

print(nomes[-1])
print(nomes[-10])
print(nomes[::-1])

print("-"*10)

print(nomes[:])
print(nomes[::-1])

print("-"*10)

for elm in nomes:
    print(elm)

# set
# dict




dict = {"key1": "value1",
        "key2": "value2",
        "key3": "value3"
        }


print(dict)

print(dict["key1"])


dict["key1"] = "Novo Valor"

print(dict["key1"])

print(dict)

dict["new Key"] = "New Value"

print(dict["new Key"])

print(dict)


dict.pop("new Key")
print(dict)

dict["new Key"] = "New Value"
print(dict)

del dict["new Key"]
print(dict)


print(dict.keys())
print(dict.values())

print("---- for dict --- ")
for elm in dict:
    print(elm)

print("---- for dict.values() --- ")
for elm in dict.values():
    print(elm)

print("---- for dict.keys() --- ")
for elm in dict.keys():
    print(elm)

print("---- for dict.items() --- ")
for elm in dict.items():
    print("--" *3 )
    print(elm)
    print(f"key: {elm[0]}, value: {elm[1]}")
    print("--" *3 )


# tuplos
print("---- tuplos --- ")

tp = ('key1', 'Novo Valor')

print(tp)
print(tp[0])
print(tp[1])

# tp[0] = "nova Key" Erro -> TypeError: 'tuple' object does not support item assignment

print(tp)


