# 8. * Ai două fișiere: clienti.csv (id_client, nume_client) și comenzi.csv (id_comanda, id_client, suma, data).
# Scrie un program care produce un nou fișier raport.csv cu toate comenzile și numele clientului corespunzător (bazat pe id_client).
import csv


def citire_clienti(nume_fisier):
    dict_clienti = {}
    with open(nume_fisier, newline="") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)

        for client in csv_dict_reader:
            dict_clienti[client["id_client"]] = client["nume_client"]

    return dict_clienti


def citire_comenzi(nume_fisier):
    dict_comenzi = {}
    with open(nume_fisier, newline="") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)

        for comanda in csv_dict_reader:
            dict_comenzi[comanda["id_comanda"]] = {'id_client': comanda["id_client"], 'suma': comanda["suma"],
                                                   'data': comanda["data"]}

    return dict_comenzi


def scrie_rapoarte(dict_clienti, dict_comenzi, nume_fisier):
    fieldnames = ["id_comanda", "id_client", "nume_client", "suma", "data"]
    with open(nume_fisier, mode="w", newline="") as csvfile:
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for id_comanda, comanda in dict_comenzi.items():
            nume_client = dict_clienti[comanda["id_client"]]
            csv_dict_writer.writerow(
                {"id_comanda": id_comanda, "id_client": comanda["id_client"], "nume_client": nume_client,
                 "suma": comanda["suma"], "data": comanda["data"]})


if __name__ == '__main__':
    dict_clienti = citire_clienti("clienti.csv")
    dict_comenzi = citire_comenzi("comenzi.csv")
    scrie_rapoarte(dict_clienti, dict_comenzi, "raport.csv")

    print("Salutare din Bucuresti!")
