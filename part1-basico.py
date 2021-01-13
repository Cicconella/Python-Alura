
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