from contextlib import nullcontext


first_name = "Erick"

def hello_world():
    print("Hello World!")

def hello_world_name(first_name):
    print(f"Hello, {first_name}")


def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]
    #print(type(args))
    #print("Hello world args")
    print(f"Hello {first_name} / {second_name} / {third_name}")


def hello_world_keywords_args(first_person, second_person):
    print(f"Hello {first_person} / {second_person}")


def hello_world_arbitrary_keywords(**kwargs):
    #print(kwargs)
    #print(kwargs.get('second_person'))
    #print(kwargs.get('first_person'))
    
    if kwargs.get('second_person') is None:
        print("No hay segunda persona")
    else:
    #print(kwargs)
    #print(type(kwargs))
    #print("Hello from here! ")
        print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']} ")
#hello_world()
#hello_world_name(first_name)
#hello_world_args("pedro", "jose", "Yassmin", "Ruben")
#hello_world_keywords_args(first_person="Erick", second_person="Eduardo")

#hello_world_arbitrary_keywords(first_person="Erick", second_person="Diego")
#hello_world_arbitrary_keywords(first_person="Erick")


#homework1 
def ifelseExample(name):
    if (name == "Erick D"):
        print(f"hola {name}")
    else:
        print(f"No eres Erick D, de igual forma hola {name}")

#ifelseExample("Erick D")

def ticketPrice():
    age = input('Ingresa tu edad:')

    if int(age) >= 18:
        ticket_price = 20
    else:
        ticket_price = 15
    print(f"El precio del boleto es {ticket_price}")
#ticketPrice()

def forRange():
    exampleList = [0, 1, 2, 3, 4, 5]
    for i in exampleList:
        print(i)

#forRange()

def doWhile():
    flag = False
    i = 0;
    while flag != True:
        print(i);
        i +=1
        condition = input("¿Desea continuar? \n Y/n")
        condition.lower()
        if condition == "y" or condition == "yes":
            flag = False
        else: 
            flag = True
    print("Ciclo Finalizado")
#doWhile() 

def breakExample():
    for x in range(10):
        for y in range(5):
            if y > 3:
                break
            print(f"({x},{y})")

#breakExample()

def continueExample():
    for index in range(10):
        if index % 2:    
            continue
        print(index)

#continueExample()

def passExample():
    counter = 1
    max = 100
    if counter <= max:
        counter += 1
        print(counter)
    else:
        #Aqui va otra validación pendiente
        pass
passExample()


def globalExample():
    print("Ejemplo con todas las funciones de la sección")
    while True:
        print("¿Que deseas ejecutar? \n 1-Secuencia de Fibonacci \n 2-Conjetura de Collatz \n 3-resolver Gauss-Jordan \n 4-Salir del programa")
        option = input()
        if(option.isnumeric()):
            option = int(option)
            if option == 1:
                flag = False
                while flag != True:
                    valores = int(input("Cual es la cantidad de datos que le interesan de la sucesión?"))
                    n1, n2 = 0, 1
                    count = 0
                    if valores <= 0:
                        print("Por favor, ingrese un valor Positivo")
                        flag = False
                    elif valores == 1:
                        print(f"Seleccione una sucesión mayor a: {valores}")
                        flag = False
                    else:
                        print("Secuencia Fibonacci:")
                        flag = True
                    while count < valores:
                        print(n1)
                        nth = n1 + n2
                        n1 = n2
                        n2 = nth
                        count += 1
                continue
            elif option == 2:
                flag = False
                while flag !=True:
                    numero = int(input("Teclee un número entero positivo : "))
                    if numero > 0:
                        while numero != 1:
                            if numero % 2:  
                                numero = numero * 3 + 1
                            else:
                                numero //= 2
                            print(numero)
                        flag = True
                    else:
                        print("El número que tecleo no es válido")
                        flag = False
                    continue
            elif option == 3:
                print("Esta función aun no se encuentra disponible, por favor intenta con otra opción")
                continue
            elif option == 4:
                print("Has salido del Programa")
                break
            else:
                print("No estas ingresando una opción valida")
                continue
        else: 
            print("No estas ingresando una opción valida")

globalExample()