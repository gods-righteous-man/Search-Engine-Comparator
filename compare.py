import json
import csv
import pandas as pd
  
# Opening JSON file
f = open('sample.json')
fgoogle = open('googlequeries.json')
# returns JSON object as 
# a dictionary
data = json.load(f)
googledata = json.load(fgoogle)
# Iterating through the json
# list
countarr = []
# with open('task2.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Query', 'Overlap', 'Correlation'])


# file.close()
for i in data:
    count = 0
    di = 0
    for j in data[i]:
        if j in googledata[i]:
            rankg = googledata[i].index(j)
            rankd = data[i].index(j)
            di += pow(rankg - rankd, 2) 
            count += 1
    if count == 1:
        if rankg == rankd:
            rho = 1
        else:
            rho = 0
    elif count == 0:
        rho = 0
    else:
        print(di)
        rho = 1 - (6*di/(pow(count, 3) - count) )
    # print(rankg - rankd)
    countarr.append(count)

    with open('task2.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Query', 'Overlap', 'Correlation'])
        writer.writerow([i, count, (count/10) * 100, rho])

    file.close()

        

print(len(countarr))
        

# for i in data:
#     print(i)
#     for j in googledata[i]:
#         # if j in googledata[i]:
#         #     print (j)
#         print(j)
  
# Closing file
f.close()


# print(df["Overlap"].mean())
df = pd.read_csv('task2.csv')
column_names=['Query', 'Number of Overlapping Results', 'Percent Overlap', 'Spearman Coefficient']

df.columns = column_names

# print(df)
print(df['Number of Overlapping Results'].mean())
print(df['Percent Overlap'].mean())
print(df['Spearman Coefficient'].mean())