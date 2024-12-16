#calculadora
def calculadora ():
    while True:

        print("\n1: soma \n2: subtração\n3: multiplicação\n4: Divisão \n0: Sair")
        opcao = input("digite o numero da operação: ")

        if opcao == "0":
            print("Saindo.... Até logo!")
            break

        if opcao not in ["1" , "2" , "3" ,"4"]:
            print("essa opção nao existe , tentar novamente.")
            continue
        try:
            num1 = float(input("digite o primeiro numero: "))
            num2 = float(input("digite o segundo numero : "))
        except ValueError:
            print("erro : insira apenas números.")
            continue
        if opcao == "1":
            print(f"resultado :{num1 + num2}")
        elif opcao == "2":
            print(f"resultado:{num1 - num2}")
        elif opcao == "3":
            print(f"resultado: {num1 * num2}")
        elif opcao == "4":
            print(f"resultado :{num1 / num2}" if num2 != 0 else "erro : divisão por zero.")
calculadora()