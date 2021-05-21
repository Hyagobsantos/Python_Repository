# Até agora a gente aprendeu a desviar das coisas, agora vmaos aprender a repetir elas!

# Imagina que nós queremos escrever na telá olá 5 vezes, nós teriamos que colcoar:

print('Olá')
print('Olá')
print('Olá')
print('Olá')
print('Olá')

# Mas e se eu quiser escrever isso 500 vezes? Seria inviável, por isso temos o laço for, podemos substituir o código de cima por:

for c in range(1, 6): # De 1 a 6 porque o range ignora o ultimo número.
   print('Olá')
print('Fim')

# O laço for é chamado de laço com variável de controle, caso acima, o c é a variável de controle.

# Outro exemplo, pra entendermos variáveis de controle:

for c in range(0, 5):
   print(c) # Vai mostrar uma contagem crescente

# Para contagens descrescentes utilize:

for c in range(5, 0, -1): # começa no 5, tira 1 (-1), até o 1 (pois o útimo é ignorado)
   print(c)

# Para pular de dois em dois:

for c in range(0, 7, 2): # começa no 0, pula de 2 em 2, até o 6 (pois o útimo é ignorado)
   print(c)

# Vamos a mais um exemplo:

n = int(input('Digite um número: '))

for c in range(0, n+1): # Li o n e utilizei dentro do range para contagem.
   print(c)
print('Fim')

# Agora vamos receber o incio do range, o fim e o passo:

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))


for c in range(i, f+1, p): 
   print(c)
print('Fim')

# Vamos pedir varios valores no for, através do input e somar todos eles:

s = 0
for c in range(0, 4):
   n = int(input('Digite um número: '))
   s += n
print(f'A soma de todos os numeros é {s}')

# O in pode ser usado para Strings

for letra in 'Thiago Veiga Lima':
   if letra == 'e':
      print(f'Achei a letra {letra}')
print('Fim')

#Tuplas
#É uma variável que guarda de 1 a N valores, ou seja, ela vai criar vários espaços na memória para você e irá guarda em apenas 1 variável.

#Para acessar os elementos dentro da tupla a gente utiliza os indices, assim como na String, o indice sempre inicia no zero.

alunos = ('José', 'Maria', 'Augusto', 'Mayara') #Tupla são representadas por parenteses, nas ultimas atualizações, nem precisa de parenteses

print(alunos)

print(alunos[2])

print(alunos[0:2])

print(alunos[1:])

print(len(alunos))

print(sorted(alunos)) #não altera a tupla, apenas ordena.

#AS TUPLAS SÃO IMUTÁVEIS

alunos[0] = 'Thiago' #Isso não funciona, porque eu não consigo atribuir itens a tuplas a não ser na atribuição dela.

#Nós conseguimos concatenar tuplas também:

a = (1, 2 ,3)
b = (4, 5, 6, 7, 8)
c = a + b
print(c)

print(len(c))

print(c.count(3)) #conta quantas vezes o 3 aparece.

print(c.index(7)) #mostra a posição do 7 na tupla. Aqui ele pega a primeira ocorrencia do numero na tupla.

#As tuplas podem receber valores de tipos diferentes:

pessoa = ('Thiago', 27, 'Casado', 1.70, True)
print(pessoa)

del(pessoa) #Apaga toda a tupla, porem você não pode deletar apenas um item da tupla




