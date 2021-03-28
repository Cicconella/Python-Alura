
# Imprimir texto

print('amazing ana')
print('amazing','ana', sep="+")

# Variáveis

nome = "ana"

idade = 30

print(nome, "tem", idade, "anos")

# Tipo da variável

print(type(nome))
print(type(idade))

# Outro exemplo

dia = 3
mes = 3
ano = 1990

print(dia, mes, ano, sep="/", end="\n")

# Formato das strings

# duas casas decimais
print("R$ {:.2f}".format(1.5))

print("R$ {:.2f}".format(1234.50))

# uma casa decimal
print("R$ {:.1f}".format(1.5))

print("R$ {:.1f}".format(1234.50))

# colocar zeros
print("R$ {:07.2f}".format(1.5))

# para inteiros tirar o f e colocar d

nome = 'Matheus'
print(f'Meu nome é {nome.lower()}')

# palavras

palavra = "elefante"

print(palavra.upper())

# list comprehension

inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

#equivale a

inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]

# Escrever arquivos
# abrir (criar), escrever e fechar arquivos

arquivo = open("palavras.txt", "w")
arquivo.write("elefante\n")
arquivo.write("cavalo\n")
arquivo.write("golfinho\n")
arquivo.write("cachorro\n")
arquivo.close()

#colocar uma nova linha no arquivo

arquivo = open("palavras.txt", "a")
arquivo.write("tartaruga\n")
arquivo.close()

# podemos usar r = para somente leitura, w = escrever sobrescrevendo, a = escrever adicionando novas linhas no arquivo existente

# lendo arquivo
arquivo = open("palavras.txt", "r")
linha = arquivo.readline()
print(linha.strip())
