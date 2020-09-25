try:
    file = open("/Users/mikezelixon/Downloads/2020.02.12.16.14.55-users.log", "r")
    print(file)

except FileNotFoundError:
    print("file not found")

for line in file:
    parsed = line.split(" ")
    print("[" + parsed[0] + "]" + ", " + parsed[4] + " = " + parsed[5] + ", " + parsed[10], file=open("newlog.txt", "a"))
file.close()