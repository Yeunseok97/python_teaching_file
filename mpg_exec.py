
mpgLst = []
with open("../data/mpg.txt", "r", encoding ="utf-8") as file:
    file.readline()
    line = file.readline()
    while line != "":
        row = line.strip("\n").split(",")
        #case 01
        #mpgLst.append(row)
        #case 02
        mpgLst.append(row)
        line = file.readline()

        instance = m.Mpg(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        mpgLst.append(instance)
        line = file.readline()

print(mpgLst)