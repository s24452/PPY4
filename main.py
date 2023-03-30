#funkcje
def my_function():
    print("hello world")

my_function()

def my_fumction_with_parameter(name):
    print(f"hello {name}")

my_fumction_with_parameter("Weronika")

def my_fun(name,surname):
    print(f"hello\nname:{name}\nsurname:{surname}")

my_fun("Weronika","Siwiec")

my_fun(surname="Siwiec",name="Weronika")


#domslne argumenty
def my_fun_with_default(name,surname="Doe"):
    print(f"hello\nname:{name}\nsurname:{surname}")

my_fun_with_default("Kim")


#wartosc opcjonalna
def my_fun_with_def2(name, surname, middle=''):
    person_data = name
    if middle:             #jesli znak pusty to automatycznie if false
       person_data += " " + middle
    person_data +=" "+ surname
    return person_data
   # print(f"hello\nname:{name}\nsurname:{surname}")

print(my_fun_with_def2("Wer", "Siw"))
print(my_fun_with_def2("Wer", "Siw", "Mar"))


people = {"Alice", "Bob", "Luke"}

#def hello_list(names):
   # for i in range(0, len(names)):
    #    names[i] = "hello " + names[i]



#hello_list(people)
#print(people)


def hello_multiply(*args, lang):
    greet = ""
    if lang == "PL":
        greet = "Witaj "
    elif lang == "FR":
        greet = "Bonjour "
    for p in args:
        print(greet + p)

hello_multiply("Alice", "Bob", "Luke", lang="PL")
