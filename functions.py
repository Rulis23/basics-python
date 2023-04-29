def hello_world():
    print("Hello World!")

def hello_world_name(first_name):
    print(f"Hello World! {first_name}")

def hello_world_args(*args):
    first_name=args[0]
    second_name=args[1]
    third_name=args[2]

    print(args)
    print(type(args))
    print(first_name)
    print(f"Hello, {first_name} / {second_name} / {third_name}")

def hello_world_keyword_args(first_person,second_person):
    print(f"Hello, {first_person}/{second_person}")

def hello_world_arbitrary_keyword_args(**kwargs):
    if kwargs.get('second_person') is None:
        print("no hay segundo nombre")
    else:
        print("si hay segundo nombre")
        print(kwargs)
        print(type(kwargs))
        print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']} from here!")

hello_world()
hello_world_name("Rulis")
hello_world_args("sebastian", "daniel", "vanessa")
hello_world_keyword_args(first_person="raul",second_person="daniel")
hello_world_arbitrary_keyword_args(first_person="raul",second_person="daniel")
hello_world_arbitrary_keyword_args(first_person="raul")