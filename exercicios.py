#%% 
nome_aluno ='Caio$lasdla    '

print(type("gustavo "))

print(nome_aluno)

print(type(nome_aluno))

print(nome_aluno.lower())



# %%alunoaluno


print(nome_aluno.split("$"))


# %%
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#%%
#%%
v1 = input('escreva um número inteiro')
v2 = input('escreva um segundo número inteiro')
print(int(v1) + int(v2))
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#%%
n = int(input("escreva um número que vc quer dividir por 5 "))
print(n%5 )
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#%%
n1 =input('numero ')
n2 =input('mais um')

print(int(n1)* int(n2) )

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#%%
d1 = int(input('numero'))
d2 = int(input('dividir'))

print(d1//d2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#%%

f1= float(input('digite um número ccom vírgula '))
f2= float(input('mais 1 '))
print(f1+f2)
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#%%
f1= float(input('digite um decimal'))
f2 = float(input('escreva'))
media = (f1+f2)/2
print(media)


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#%%
base=float(input('digite um numero'))
expoente= int(input('digite um número para elevar '))
resultado =base**expoente
print(resultado)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#%%
import math

raio = float(input('digite a o raio da circunferencia'))
area =  math.pi*raio**2

print(area)





# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
 #%%
nome=input('qual seu nomwe?')
maiusculo = nome.upper()
print(maiusculo)
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#%%
nome= input('digitw sue nome completo')
minusc = nome.lower()

print(minusc)
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#%% 

frase = input('digite uma frase e coloque espaços no final e no começo')

print(frase.strip())


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#%%
data = input('digite uma data no formato "dd/mm/aaaa"')
split = data.split('/')
dia = split[0]
mes=split[1]
ano = split[2]

print(data.split('/'))
print ('dia =', dia )
print ('mes =', mes )
print ('ano =', ano )
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#%%

palavra = input('digite um substantivo')
adj = input('digite um adjetivo')

print(palavra + adj)
print(palavra+' '+ adj)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#%%

v1 = True 
v2 =True

print(v1 and v2 )
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR
#%%

v1 = False 
v2 =False

print(v1 or v2 )

# 18. Desenvolva um programa que peça ao usu ário para inserir um valor booleano e, em seguida, inverta esse valor.
#%%

v1 = input('digite true or false')


print('vc digitou', v1)
print('o oposoo é', not v1)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#%%

v1 = float(input('digite um númeor'))
v2 = float(input('digite outro '))

if v1 == v2:
    print('iguais')
else:
    print('diferente')
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#%%

v1 = float(input('digite um númeor'))
v2 = float(input('digite outro '))

if v1 != v2:
    print('diferente')
else:
    print('iguais')

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação






# %%
