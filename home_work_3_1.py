
data=("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")
count=1
string=''
for y in range(len(data)-1):
    if data[y]==data[y+1]:
        count+=1
    else:
        string+=str(count)+data[y]
        count=1
print(string)