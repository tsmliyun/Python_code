file1 = open('name.txt','w')
file1.write('诸葛亮')
file1.close()

file2 = open('name.txt')
print(file2.read())
file2.close()

file3 = open('name.txt','a')
file3.write('刘备')
file3.close()

file4 = open('name.txt')
print(file4.read())
file2.close()