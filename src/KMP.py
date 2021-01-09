#Yasyfiana Fariha
#13518143
#Knuth Morris Prat
#Tucil 4

#Melakukan pencarian nilai b(x)
#atau border function
def kmpBorderFuntion (pattern):
    m = len(pattern)
    BorderF = [0 for x in range(m-1)]
    j = 0
    i = 1

    while(i<m-1):
        if(pattern[j]==pattern[i]):
            BorderF[i] = j + 1
            i += 1
            j += 1
        elif(j >0):
            j = BorderF[j-1]
        else:
            BorderF[i] = 0
            i+=1
            
    return(BorderF)
    
#Algoritma KMP
#Memanggil fungsi kmpBorderFunction
def KMP(text, pattern):
    n = len(text)
    m = len(pattern)
    i = 0
    j = 0
    BorderF = kmpBorderFuntion(pattern)
    # print(BorderF)
    while (i<n):
        #Cek dia udah sama atau belum.
        #cek karakternya di huruf teraakhir pattern atau bukan
        #Kalau iya return i dimana pattern pertama sama
        #Kalau engga next
        if(pattern[j] == text[i]): 
            if(j == (m - 1)): 
                return(i-m+1)
            i+=1
            j+=1
        #missmatch bukan di huruf pertama pattern
        #ganti j sesuai nilai hasil fungsi b(k)
        elif(j>0):
            k = j-1
            j = BorderF[k]
           #missmatch terjadi diawal huruf pattern, langsung geser 
        else:
            i+=1
    return -1
