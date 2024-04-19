# Condicionais

# if, elif e else

idade = int(input("Qual a sua idade?"))
if idade >= 18:
    print("Você é maior de idade")
elif idade == 17:
    print("Você tem 17 anos")
elif idade == 12:
    print("Você é adolescente")
else:
    print("Você é menor de idade")


mensagem = "Pode tirtar CNH" if idade >= 18 else "Não pode tirar CNH"
print(mensagem)
