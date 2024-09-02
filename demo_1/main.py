
# comnet 1 linha

"""
comnet
varias
linha

"""
from pyasn1_modules.rfc2985 import smime

# var


nome = "valor"
print(nome)

idade = 10
print(idade)

idade2 = 10.5
print(idade2)

aprovado = True
print(aprovado)

'''
nome = 182
print(nome)
'''

# op var

#soma=idade+idade2

soma = idade + idade2
print(soma)

# concat var

nome = "Carlos"
print("nome: {nome}, idade: {idade} mais txt")
print(f"nome:\t\"{nome}\", \ \nidade: {idade} mais txt")

"""

\n
\t
\\
\"

"""


# cond
    # if
print("--------if------")
idade = 30

if idade >= 18:
    print("Adulto")
else:
    print("nao Adulto")

print("-------- if v2 ------")
idade = 16
if idade > 18:
    print("Adulto")
elif idade > 15:
    print("teen")
else:
    print("kid")

print("-------- if v3 ------")


"""
&& - and
|| - or
! - not

"""
v1 = 10
v2 = 9

if v1 == 10 and not v2 == 20:
    print("ok")
else:
    print("nao ok")



    # match case


# loops
    # for

print("-------- for ------")
nome = "O meu nome"
for l in nome:
   if l == "e":
       print("it Works")
   else:
        print(l)


 # range(n) <- 0 ate  n-1
 # range(m, n) <- m ate  n-1
 # range(m, n, s) <- m ate  n-1 com step de s

print("------for v2 -------")
for n in range(5, 100, 5):
    print(n)


print("------for v3-------")
for n in range(5, 100, 5):


    if n % 10 == 0:
        print("n % 10 == 0")
        continue

    if n == 25:
        break

    print(n)


print("-------- while ------")

# while

"""
    --  =  -= 1
    ++  =  += 1
    
"""

sum = 100
while sum > 0:

    if sum % 2 == 0:
         print(sum)
    if sum % 5 == 0:
         break

    sum -= 1



# arr (listas)

# dict


# funcs


# classes ??
