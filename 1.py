lista = []

# Funkcija koja prikazuje opcije za korisnika
def opcije_za_korisnika():
    print("\n---- CRUD ----")
    print("1. Create") 
    print("2. Read (Čitanje svih zapisa)") 
    print("3. Update (Ažuriranje postojećeg zapisa)") 
    print("4. Delete (Brisanje zapisa)") 
    print("5. Exit (Izlaz iz aplikacije)")

# Kreiranje novog zapisa (dodavanje podataka u listu)
def create_a():
    ime = input("ime: ")
    prezime = input("prezime: ")
    godine = input("godine: ")
    zapis = {'ime': ime, 'prezime': prezime, 'godine': godine}
    lista.append(zapis)
    print("Uspešno dodat podatak")

# Čitanje svih zapisa
def read_a():
    if not lista:
        print("Nema podataka")
    else:
        print("\n--------------- SVI PODACI ---------------")
        # Prikazivanje podataka sa ID-jem zbog apdejta
        for idx, element in enumerate(lista, start=1):
            print(f"{idx}. Ime: {element['ime']}, Prezime: {element['prezime']}, Godine: {element['godine']}")
        print("------------------------------------------")

# Ažuriranje zapisa
def update_a():
    read_a()
    if not lista:
        return

    try:
        tmp = int(input("\nIzaberi redni broj elementa koji želiš da ažuriraš: ")) - 1
        if 0 <= tmp < len(lista):
            ime = input("Unesi novo ime: ")
            prezime = input("Unesi novo prezime: ")
            godine = input("Unesi nove godine: ")
            lista[tmp]['ime'] = ime
            lista[tmp]['prezime'] = prezime
            lista[tmp]['godine'] = godine
            print("Uspešno ažuriranje")
        else:
            print("Nekorektan redni broj")
    except ValueError:
        print("Molimo unesite validan broj.")

# Brisanje zapisa
def delete_a():
    read_a()
    if not lista:
        return

    try:
        tmp = int(input("\nIzaberi redni broj elementa koji želiš da obrišeš: ")) - 1
        if 0 <= tmp < len(lista):
            del lista[tmp]
            print("Uspešno brisanje")
        else:
            print("Nekorektan redni broj")
    except ValueError:
        print("Molimo unesite validan broj.")

# Glavni program
if __name__ == "__main__":
    while True:
        opcije_za_korisnika()
        choice = input("\nUnesite redni broj: ")

        if choice == '1':
            create_a()  # Kreiranje novog zapisa
        elif choice == '2':
            read_a()  # Čitanje svih zapisa
        elif choice == '3':
            update_a()  # Ažuriranje zapisa
        elif choice == '4':
            delete_a()  # Brisanje zapisa
        elif choice == '5':
            print("Izlazak iz aplikacije.")  # Izlaz iz aplikacije
            break
        else:
            print("Nevažeći izbor. Pokušajte ponovo.")  # Poruka o nevalidnom unosu
