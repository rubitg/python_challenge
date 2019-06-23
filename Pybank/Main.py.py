

import os
import csv
# creating path 
csvpath= os.path.join('budget_data.csv')

#create file..
with open(csvpath,newline='') as csvfile:
    header=next(csvfile)
    csvreader=csv.reader(csvfile,delimiter=',')
    i=0
    total=0
    sum_i=0
    promedio=0
    min_prof=0
    max_prof=0
    for row in csvreader: #itinerates through all the rows
        total+= int(row[1]) #Prints the rows 
        sum_i+= i+1  #cuenta cuantos hay
      #  min_prof=min(total)
      #  max_prof=max(row[1])
        
       # return
    print (total)
    print(sum_i)
    promedio=total/sum_i
    print(int(promedio))