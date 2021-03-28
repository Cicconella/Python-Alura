from teste import cria_conta, saca, deposita, extrato


### Aqui fazermos do modo procedural
conta = cria_conta(123, "Nico", 55.0, 1000.0)

print(conta)
deposita(conta, 15.0)
saca(conta, 5.0)
extrato(conta)

### Fazendo usando o paradigma OO