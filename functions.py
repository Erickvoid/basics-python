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

hello_world_arbitrary_keywords(first_person="Erick", second_person="Diego")
hello_world_arbitrary_keywords(first_person="Erick")