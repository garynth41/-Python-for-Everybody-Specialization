8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

  
 
1
file = input('Please enter file name:')
2
handle = open(file)
3
count = 0
4
for line in handle:
5
    line = line.rstrip()
6
    if not line.startswith('From '):
7
        continue
8
    line = line.split()
9
    print(line[1])
10
    count = count+1
11
print('There were', count, 'lines in the file with From as the fir
