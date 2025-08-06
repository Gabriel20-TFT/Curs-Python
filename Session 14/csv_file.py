import csv


def csv_reading(nume_csv, are_coloane=False):
    with open(nume_csv) as csvfile:
        csvreader = csv.reader(csvfile)

        if are_coloane:
            coloane = next(csvreader)
        else:
            coloane = []
        linii = list(csvreader)

        return coloane, linii


def csv_an_castigator(nume_csv):
    year = input("Enter year: ")

    with open(nume_csv) as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            if year == row[1]:
                print(f"Echipa castigatoare din anul {year} este {row[3]}.")


def csv_write(nume_csv, linie):
    with open(nume_csv, "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(linie)


def csv_dict(nume_csv):
    field_names = ["nume", "prenume"]

    with open(nume_csv, "w", newline="") as csvfile:
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)

        csv_dict_writer.writeheader()
        csv_dict_writer.writerow({"nume": "Breaz", "prenume": "Catalin"})
        csv_dict_writer.writerow({"nume": "Muresanu", "prenume": "Mihai"})
        csv_dict_writer.writerow({"nume": "George", "prenume": "Butoi"})


if __name__ == '__main__':
    pass
