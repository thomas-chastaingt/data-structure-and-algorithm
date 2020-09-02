def sorting(tab):
    for j in range(1,len(tab)): 
        key = tab[j]         
        i = j - 1
        while i>=0 and tab[i] > key: 
            tab[i+1] = tab[i]    
            i=i-1
        tab[i+1] = key

tab = [98, 22, 15, 32, 2, 74, 63, 70]
sorting(tab)
print("Le tableau trié est : ")
for i in range(len(tab)):
    print("% d" % tab[i])
