#matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#for linha in matriz:
    #for elemento in linha:
        #print(elemento)


#############################

#word = 'ola mundo'
#for n in word:
    #print(n)



#lista = ('a', 'b', 'c')
#for t in lista:

#########################

#**Exercício 1:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

list = range(2,21)
for n in list:
    print(n%2==0)



#######################################################

#**Exercício 2:** Escreva um programa que imprima os números pares de 2 a 20.

n5 = range(2,21)
for g in n5:
    print(g)



################################################

#Exercício 3: Escreva um programa que calcule a soma dos números de 1 a 100.



num = range(1,11)
for p in num:
    print(p*10)

###############################################

#**Exercício 4:** Escreva um programa que imprima os múltiplos de 5 de 5 a 50.

#Desenvolvido por Prô Terra - MakerZine

list1 = [5,51]
for x in range (1,list1+1):
  if (x % 5 == 0):
    print(x,"é múltiplo de 5")
