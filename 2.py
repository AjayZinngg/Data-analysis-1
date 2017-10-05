import csv
import matplotlib.pyplot as plt

with open('test_dataset.csv') as csv_file:
     csv_reader = csv.reader(csv_file, delimiter = ',')   
     next(csv_reader)
     my_set  = []
     tran = []
     gr = []
     trans = []
     grs = []
     for row in csv_reader:
         tran.append(row[3])
         gr.append(row[5])
         my_set.append(row[2]) 
     my_len  = len(my_set)
     for i in range (my_len):
         if my_set[i] =='FNB':
             trans.append(tran[i])
             grs.append(gr[i]) 
     print(trans,grs)
     plt.plot(trans,grs)
      