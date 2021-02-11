file1 = open('SampleFile1.txt')
file2 = open('SampleFile2.txt')

data_1 = file1.read()
data_2 = file2.read()

print('This is the data before swapping.')
print('File 1: ' + data_1)
print('File 2: ' + data_2)

file1.close()
file2.close()

file3 = open('SampleFile1.txt', 'w')
file4 = open('SampleFile2.txt', 'w')


def swapData():
    file3.write(data_2)
    file4.write(data_1)
    print('Data after swapping.')
    print('File 1: ' + data_2)
    print('File 2: ' + data_1)


swapData()
