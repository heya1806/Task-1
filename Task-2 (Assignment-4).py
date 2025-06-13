user_text = input('Enter text to write to the file: ' )
file1 = open('output.txt', 'w')
file1.write (user_text + "\n")
file1.close()
print('Data successfully written to output.txt.' + "\n")
file1.close()



append_text = input('Enter additional text to append: ')
file2 = open('output.txt', 'a')
file2.write ( append_text + "\n")
file2.close()
print('Data successfully appended.' + "\n")
file2.close()

file = open('output.txt', 'r')
print("Final content of output.txt: ")
print(file.read())
file.close()

