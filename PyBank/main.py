from dataclasses import dataclass 
import csv

@dataclass
class EvaluationWindow:
    month: str
    profit: int

data = open("./Resources/budget_data.csv")
data = list(csv.reader(data))
# print(data)



months = []

for x in data[1:]: 
    months.append(EvaluationWindow(x[0],int(x[1])))
    # print(x)

totalmonths = len(months)
print(totalmonths)

total = 0
for month in months :
    total = total + month.profit
print (total)

averagechange = total/totalmonths
print (averagechange)

Max = max(months, key = lambda x : x.profit)
print(Max)

Min = min(months, key = lambda x : x.profit)
print(Min)
