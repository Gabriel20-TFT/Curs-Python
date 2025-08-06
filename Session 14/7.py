# 7. * Se dă un fișier studenti.csv. Creează un nou fișier studenti_actualizat.csv
# unde fiecare elev are câmpul status adăugat: Promovat dacă media > 5, altfel Corigent.
import csv


def citire_note_studenti(nume_fisier):
    dict_note = {}
    with open(nume_fisier, newline="") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)

        for student in csv_dict_reader:
            if (student["nume"], student["prenume"]) not in dict_note:
                dict_note[(student["nume"], student["prenume"])] = []

            dict_note[(student["nume"], student["prenume"])].append(float(student["nota"]))

    return dict_note


def scrie_status_studenti(dict_note, nume_fisier):
    fieldnames = ["nume", "prenume", "medie", "status"]
    with open(nume_fisier, mode="w", newline="") as csvfile:
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for student, note in dict_note.items():
            media = sum(note) / len(note)
            csv_dict_writer.writerow(
                {"nume": student[0], "prenume": student[1], "medie": media,
                 "status": "Promovat" if media > 5 else "Corigent"})


if __name__ == '__main__':
    dict_note = citire_note_studenti("studenti.csv")
    scrie_status_studenti(dict_note, "studenti_actualizat.csv")
