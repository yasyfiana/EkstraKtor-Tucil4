#Yasyfiana Fariha
#13518143
#Boyer Moore
#Tucil 4

#Malakukan pencarian lasoccurence
#dari text pada pattern
def LastOccur(text, pattern):
    # last = [-1 for x in range(len(text))]
    last = {}
    for x in range(len(text)):
        if((text[x] in last) == False):
            char = text[x]
            hasil = -1
            for y in range(len(pattern)):
                if(char == pattern[y]):
                    hasil = y
            last[char] = hasil
    return(last)
             
#Pencarian string melalui Booyer-Moore
#pencarian dilakukan dengan memanggil LastOccur
#pemanggilan tersebut dilakukan hanya diawal fungsi dijalankan
def BM(text, pattern):
    last = LastOccur(text, pattern)
    n = len(text)
    m = len(pattern)
    i = m-1
    j = m - 1
    hasil = -1
    # print(last)
    if (m > n):
        return(hasil)
    else:
        while(True):
            
            if(pattern[j] != text[i]):
                valueLastO = last.get(text[i])
                if(valueLastO == -1 ): #kasus 3
                    j = m-1
                    i = i + m
                elif(valueLastO < j):
                    j = m-1
                    i = i + m -1 - valueLastO #kasus 1
                elif(valueLastO > j):
                        i = i + m - j
                        j = m-1
            else:
                if(j == 0):
                    hasil = i
                    break
                else:
                    i-=1
                    j-=1
            if(i > n-1):
                break
        return(hasil)
