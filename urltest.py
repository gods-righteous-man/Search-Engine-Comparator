import json
  
# Opening JSON file
f = open('sample.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
for i in data:
    for j in range(0, len(data[i]) - 1):
        for k in range(j+1, len(data[i])):
            if data[i][j] == data[i][k]:
                print(i)



  
# Iterating through the json
# list

  
# Closing file
f.close()