from sys import argv

filename = argv[1] # Because index 0 is the name of the script

txt = open(filename, "r")
print(txt.read())
txt.close()

txt = open(filename, "a")
txt.write("\nID: xxx")
txt.close()
