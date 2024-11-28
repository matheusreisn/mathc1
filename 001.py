cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", 
"onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    n = int(input('Digite um numero de 0 a 20: '))
    if n > 20:
        print ("Tente novamente!")
    elif n < 0:
        print ("Tente novamente!")
    else:
        break
print (f'Voce digitou o numero {cont[n]}.')