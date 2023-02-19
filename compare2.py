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
    for j in range (0, len(data[i])):
        if data[i][j][0:12] == "https://www.":
            data[i][j] = data[i][j][12:]
            print("first")
        elif data[i][j][:11] == 'http://www.':
            data[i][j] = data[i][j][11:]
            print("second")
        elif data[i][j][:8] == 'https://':
            data[i][j] = data[i][j][8:]
            print("third")
        elif data[i][j][:7] == 'http://':
            data[i][j] = data[i][j][7:]
            print("fourth")

for i in googledata:
    for j in range (0, len(data[i])):
        if googledata[i][j][0:12] == "https://www.":
            googledata[i][j] = googledata[i][j][12:]
            print("first")
        elif googledata[i][j][:11] == 'http://www.':
            googledata[i][j] = googledata[i][j][11:]
            print("second")
        elif googledata[i][j][:8] == 'https://':
            googledata[i][j] = googledata[i][j][8:]
            print("third")
        elif googledata[i][j][:7] == 'http://':
            googledata[i][j] = googledata[i][j][7:]
            print("fourth")


# print(data)










with open('task5.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Query', 'Overlap', 'Correlation'])
        writer.writerow(["Queries", "Number of Overlapping Results", "Percent Overlap", "Spearman Coefficient"])
        
file.close()





qcount = 1
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

    with open('task5.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Query', 'Overlap', 'Correlation'])
        writer.writerow(["Query " + str(qcount), count, (count/10) * 100, rho])
        qcount += 1
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
df = pd.read_csv('task5.csv')
column_names=['Query', 'Number of Overlapping Results', 'Percent Overlap', 'Spearman Coefficient']

df.columns = column_names

# print(df)
print(df['Number of Overlapping Results'].mean())
print(df['Percent Overlap'].mean())
print(df['Spearman Coefficient'].mean())

with open('task5.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Query', 'Overlap', 'Correlation'])
        writer.writerow(["Averages",df['Number of Overlapping Results'].mean(), df['Percent Overlap'].mean(), df['Spearman Coefficient'].mean()])
        
file.close()