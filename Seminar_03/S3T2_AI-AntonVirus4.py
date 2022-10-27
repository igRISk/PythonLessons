data = "C:\\Users\\МSI\\Desktop\\Python for n00bz\\seminars\\sem3\\fridges.txt"
busted_serialNumbers=[]
k=0

with open(data,'r') as f:
    for i in f:
        if 'a' in i:
            if 'n' in i:
                if 't' in i:
                    if 'o' in i:
                        if 'n' in i:
                            busted_serialNumbers.append(k)
                            k+=1

print(busted_serialNumbers)