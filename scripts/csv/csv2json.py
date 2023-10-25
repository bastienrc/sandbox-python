import os, csv, json, time

def csv2json(csvFile, jsonFile):
    rows = []

    with open(csvFile) as file_csv:
        data = csv.DictReader(file_csv, delimiter=';')
        for row in data:
            rows.append(row)

    # print(json.dumps(rows, indent=4))

    with open(jsonFile, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(rows, indent=4)
        jsonf.write(jsonString)


csvFile = f'{os.path.dirname(__file__)}/auteurs.csv'
jsonFile = f'{os.path.dirname(__file__)}/auteurs.json'

start = time.perf_counter()
csv2json(csvFile, jsonFile)
finish = time.perf_counter()

print(f"Conversion terminer en {(finish - start)*1000:0.4f} millisecondes")
