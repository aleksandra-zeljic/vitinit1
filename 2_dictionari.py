import json
import os


eng_na_srp_fajl = "eng_na_srp.json"
srp_na_eng_fajl = "srp_na_eng.json"


def ucitaj_recnike():
    if os.path.exists(eng_na_srp_fajl):
        with open(eng_na_srp_fajl, 'r', encoding='utf-8') as f:
            eng_na_srp = json.load(f)
    else:
        eng_na_srp = {}

    if os.path.exists(srp_na_eng_fajl):
        with open(srp_na_eng_fajl, 'r', encoding='utf-8') as f:
            srp_na_eng = json.load(f)
    else:
        srp_na_eng = {}

    return eng_na_srp, srp_na_eng


def sacuvaj_recnike(eng_na_srp, srp_na_eng):
    with open(eng_na_srp_fajl, 'w', encoding='utf-8') as f:
        json.dump(eng_na_srp, f, ensure_ascii=False, indent=4)
    with open(srp_na_eng_fajl, 'w', encoding='utf-8') as f:
        json.dump(srp_na_eng, f, ensure_ascii=False, indent=4)


def dodaj_rec(eng_na_srp, srp_na_eng, eng_rec, srp_rec):
    eng_na_srp[eng_rec] = srp_rec
    srp_na_eng[srp_rec] = eng_rec
    sacuvaj_recnike(eng_na_srp, srp_na_eng)
    print(f"Dodato: {eng_rec} -> {srp_rec}")


def pretrazi_rec(recnik, rec):
    return recnik.get(rec, "Reč nije pronađena.")


def azuriraj_rec(eng_na_srp, srp_na_eng, eng_rec, nova_srp_rec):
    if eng_rec in eng_na_srp:
        stara_srp_rec = eng_na_srp[eng_rec]
        eng_na_srp[eng_rec] = nova_srp_rec
        srp_na_eng.pop(stara_srp_rec, None)  # Ukloni staru srpsku reč iz srpsko-engleskog rečnika
        srp_na_eng[nova_srp_rec] = eng_rec
        sacuvaj_recnike(eng_na_srp, srp_na_eng)
        print(f"Ažurirano: {eng_rec} -> {nova_srp_rec}")
    else:
        print(f"Reč '{eng_rec}' nije pronađena u rečniku.")


def obrisi_rec(eng_na_srp, srp_na_eng, eng_rec):
    if eng_rec in eng_na_srp:
        srp_rec = eng_na_srp.pop(eng_rec)
        srp_na_eng.pop(srp_rec, None)
        sacuvaj_recnike(eng_na_srp, srp_na_eng)
        print(f"Obrisano: {eng_rec} -> {srp_rec}")
    else:
        print(f"Reč '{eng_rec}' nije pronađena u rečniku.")


def glavni_meni():
    eng_na_srp, srp_na_eng = ucitaj_recnike()

    while True:
        print("\n-------------------")
        print("1. Dodaj reč")
        print("2. Pretraži reč")
        print("3. Ažuriraj prevod")
        print("4. Izbriši reč")
        print("5. Izlaz")

        izbor = input("Unesite opciju (1-5): ")

        if izbor == "1":
            eng_rec = input("Unesite englesku reč: ")
            srp_rec = input("Unesite prevod na srpski: ")
            dodaj_rec(eng_na_srp, srp_na_eng, eng_rec, srp_rec)

        elif izbor == "2":
            pretraga_izbor = input("Pretraži po (1) engleskom ili (2) srpskom: ")
            rec = input("Unesite reč: ")
            if pretraga_izbor == "1":
                print(f"{rec} -> {pretrazi_rec(eng_na_srp, rec)}")
            else:
                print(f"{rec} -> {pretrazi_rec(srp_na_eng, rec)}")

        elif izbor == "3":
            eng_rec = input("Unesite englesku reč za ažuriranje: ")
            nova_srp_rec = input("Unesite novi prevod na srpski: ")
            azuriraj_rec(eng_na_srp, srp_na_eng, eng_rec, nova_srp_rec)

        elif izbor == "4":
            eng_rec = input("Unesite englesku reč za brisanje: ")
            obrisi_rec(eng_na_srp, srp_na_eng, eng_rec)

        elif izbor == "5":
            print("Izlaz iz programa.")
            break

        else:
            print("Pogrešan unos, pokušajte ponovo.")

        print("-----------------------------------------------\n")

if __name__ == "__main__":
    glavni_meni()
