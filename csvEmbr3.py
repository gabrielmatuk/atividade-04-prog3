import csv
import pandas as pd
filename = "cotacao.csv.csv"

fields = []
rows = []

df = pd.read_csv(filename)
with open(filename, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                fields = next(csvreader)
                for row in csvreader:
                    rows.append(row)

                print("Número de cotações nesse arquivo :%d"%(csvreader.line_num))
csvfile.close()
maior = df.values.max()
menor = df.values.min()
media = (maior + menor)/2
data = [maior,menor,media, csvreader.line_num]
print('Valor máximo:', df.values.max())
print('Valor mínimo:', df.values.min())
print(f'Média valor máximo e valor mínimo: {media}')

with open('novocsv.csv', 'w') as f:
    out = csv.writer(f)
    out.writerows(map(lambda x: [x], data))
    f.close()
