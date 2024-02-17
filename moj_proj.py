import os

def display_prompt():
    aktualny_katalog = os.getcwd()
    print(f"{aktualny_katalog}> ", end="")

def help_command():
    print("help                                             | Wyświetla sposób użycia programu oraz informacje o komendach")
    print("quit                                             | Kończy program")
    print("ls                                               | Wyświetla pliki")
    print("cr <nazwa>                                       | Tworzy plik o podanej nazwie")
    print("cd <katalog>                                     | Przejście do katalogu")
    print("mkdir <katalog>                                  | Tworzy katalog o podanej nazwie")
    print("o <filename>                                     | Wyświetla zawartość pliku tekstowego.")
    print("stat <filename>                                  | Podsumowuje zawartość pliku: ilość znaków")
    print("rename <n1> <n2>                                 | Zmienia nazwę pliku <n1> na <n2>")

def list_files():
    lista_plików = os.listdir()
    for i, plik in enumerate(lista_plików, start=1):
        print(f"[{i}] {plik}")

def create_file(nazwa):
    if os.path.exists(nazwa):
        print("Plik o tej nazwie już istnieje.")
    else:
        with open(nazwa, 'w') as f:
            pass
        print(f"Utworzono plik o nazwie '{nazwa}'")

def change_directory(katalog):
    if os.path.exists(katalog):
        os.chdir(katalog)
        print(f"Zmieniono katalog na '{os.getcwd()}'")
    else:
        print("Podany katalog nie istnieje.")

def make_directory(katalog):
    if os.path.exists(katalog):
        print("Katalog o tej nazwie już istnieje.")
    else:
        os.mkdir(katalog)
        print(f"Utworzono katalog o nazwie '{katalog}'")

def display_file_content(nazwa):
    if os.path.exists(nazwa):
        with open(nazwa, 'r') as f:
            zawartosc = f.read()
            print(f"Zawartość pliku '{nazwa}':\n{zawartosc}")
    else:
        print("Podany plik nie istnieje.")

def file_stat(nazwa):
    if os.path.exists(nazwa):
        with open(nazwa, 'r') as f:
            zawartosc = f.read()
            print(f"Podsumowanie pliku '{nazwa}':")
            print(f"Ilość znaków: {len(zawartosc)}")
    else:
        print("Podany plik nie istnieje.")

def rename_file(stara, nowa):
    if os.path.exists(stara):
        os.rename(stara, nowa)
        print(f"Zmieniono nazwę pliku z '{stara}' na '{nowa}'")
    else:
        print("Podany plik nie istnieje.")

commands = {
    "help": help_command,
    "quit": exit,
    "ls": list_files,
    "cr": create_file,
    "cd": change_directory,
    "mkdir": make_directory,
    "o": display_file_content,
    "stat": file_stat,
    "rename": rename_file,
}

while True:
    display_prompt()
    user_input = input().split()
    
    if user_input: 
        command = user_input[0]
        args = user_input[1:]

        if command in commands:
            commands[command](*args)
        else:
            print("Nieznana komenda. Wpisz 'help', aby uzyskać listę dostępnych komend.")
    else:
        print("Nie podano żadnej komendy.")
