f=open('file.txt','w')
f.write('hello saketh the music teacher')
f.write('\nsai raju is a motivation speaker')
f=open('file.txt','r')
print(f.read())
print(f.read(9))
print(f.readlines())
'''

'''
line=[
      "the first line of code\n"
      "the second line of code\n"
       " the third line of code\n"
      ]
f=open('example.txt','w')
f.writelines(line)
f=open('example.txt','r')
print(f.read())
f.close  
#binary
file=open('binary.bin','wb')
file.write(b'\x00\x01\x02\x03')
file=open('binary.bin','rb')
print(file.read())
'''
#csv
import csv
'''
data=[
      ['s.no','roll no','name'],
      [1,501,'sairaju'],
      [2,502,'saketh'] ,  
      [3,503,'saikiran']
      ]
      
with open('table.csv','w',newline='') as f:
    rf=csv.read(f)
    rf.writerows(data)
  
with open('table.csv','r',newline='') as f:
    rf=csv.reader(f)
    for row in rf:
    
        print(row) 

