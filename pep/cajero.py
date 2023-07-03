# cajero automatico
from random import randrange

saldo = randrange(0, 100)
print("Elija el idioma para continuar/choose a language to continue :")
print()
print("1 - español")
print("2 -   English")
idioma = input("Elija un idioma/ Choose the language : ")
if idioma == "1":
    print("Bienvenido al Cajero Automatico")
    print()
    print("1.  Consulta de Saldo Disponible")
    print("2.  Extraer Dinero")
    print("3.  Depositar dinero")
    print("4.  Transferencias")
    print("0.  Salir")
    print()
    opcion = int(input("Selecione la Accion a Realizar :"))
    if opcion in range(5):
        if opcion == 0:
            print("Hasta luego")
        elif opcion == 1:
            print("Su Saldo Disponible es : ", "$", saldo)
        elif opcion == 2:
            monto = int(input("Indique el monto a retirar : $ "))
            if monto > saldo:
                print("Saldo no disponible")
            else:
                saldo = saldo - monto
                print("Retire su dinero")
                print("Su saldo actual es : $ ", saldo)
        elif opcion == 3:
            monto = int(input("Introduzca el monto a depositar : $"))
            saldo = monto + saldo
            print("Su saldo actual es $", saldo)
        else:
            cuenta = int(input("Indique el numero de cuenta : "))
            monto = int(input("Introduzca la cantidad que desea transferir : $"))
            if monto > saldo:
                print("Operación fallida por saldo insuficiente")
            else:
                saldo = saldo - monto
                print("Operacion exitosa")
                print()
                print("Su saldo actual es $: ", saldo)
elif idioma == "2":
    print("Welcome to the ATM")
    print()
    print("1. Available Balance Query")
    print("2. Extract Money")
    print("3. Deposit money")
    print("4. Transfers")
    print("0. Exit")
    print()
    opcion = int(input("Select the Action to Perform :"))
    if opcion in range(0, 5):
        if opcion == 0:
            print("See you later")
        elif opcion == 1:
            print("Your Available Balance is: ", "$", saldo)
        elif opcion == 2:
            monto = int(input("Indicate the amount to withdraw: $ "))
            if monto > saldo:
                print("Balance not available")
            else:
                saldo = saldo - monto
                print("Withdraw your money")
                print("Your current balance is : $ ", saldo)
        elif opcion == 3:
            monto = int(input("Enter the amount to deposit: $"))
            saldo = monto + saldo
            print("Your current balance is $", saldo)
        else:
            cuenta = int(input("Enter the account number: "))
            monto = int(input("Enter the amount you want to transfer : $ "))
            if monto > saldo:
                print("Operation failed due to insufficient balance")
            else:
                saldo = saldo - monto
                print("Operation successful")
                print()
                print("Your current balance is $: ", saldo)
