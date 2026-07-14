cont0=1

while True:
    numeros=[]
    cont0=1
    parar0=False
    try:
        num0=int(input("Colocar números quantas vezes?"))
        while cont0<=num0:
            try:
                num1=int(input("Selecione o {}° número".format(cont0)))
                cont0=cont0+1
                numeros.append(num1)
            except (ValueError):
                print("Digite um número válido")
                continue
        while True:
            print("1 - Somar")
            print("2 - Multiplicar")
            try:
                num2=int(input("O que fazer com os números?"))
                if num2>2 or num2<1:
                    print("Digite 1 ou 2")
                    continue
                else:
                    if num2==1:
                        cont2=0
                        for cont1 in numeros:
                            cont2=cont2+cont1
                        print("A soma é {}".format(cont2))
                    elif num2==2:
                        cont2=1
                        for cont1 in numeros:
                            cont2=cont2*cont1
                        print("A multiplicação é {}".format(cont2))
                break
            except (ValueError):
                print("Digite 1 ou 2")
                continue
    except (ValueError):
        print("Digite um número válido")
        continue
    while True:
        parar1=str(input("Quer parar?[S/N]")).strip().upper()
        if parar1=="S":
            parar0=True
            break
        elif parar1=="N":
            print("Reiniando programa...")
            break
        else:
            print("Digite S ou N")
            continue
    if parar0:
        print("Obrigado por participar")
        break