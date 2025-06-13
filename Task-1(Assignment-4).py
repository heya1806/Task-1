
try:
    file = open('sample.txt', 'r')
    print('Reading file content: ')
    reading_file1 = file.readline()
    print('Line 1:', reading_file1, end ='')
    reading_file2 = file.readline()
    print('Line 2:',reading_file2)
    file.close()

except FileNotFoundError:
    print('Error: The file', "sample.txt", 'was not found.')
