def sc(apple):
    for i in range(len(apple)):
        for j in range(len(apple[i])):
            if apple[i][j]=="B":
                return [i,j]
            
def sc(apple):
    for i in apple :
        for j in i:
            if j == "B" :
                return [apple.index(i),i.index(j)]