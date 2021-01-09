#Yasyfiana Fariha
#13518143
#Regex
#Tucil 4
import re

#Melakukan pencocokan secara exact match menggunakan regex
def REexact(reg, text):
    rex = "(" + reg +")"
    hasil = re.search(rex, text,re.IGNORECASE)
    if(hasil):
        return hasil.start()
    else:
        return -1
    
#Mencari waktu yang terdapat pada kalimat tersebut
def REWaktu(text):
    pattern = r"""((pagi|siang|malam)\s(hari))?((bulan|tahun|minggu))?
    ((sehari|sebulan|seminggu)\s*(sebelum|setelah)?)?((kemarin|besok)\s?)?(lusa)?
    (((senin|selasa|rabu|kamis|jumat|sabtu|minggu).?\s?)?
    (([(]?\d{1,2}[/-]\d{1,2}[/-]\d{4}[)]?))?(([(]?\d{4}[/-]\d{1,2}[/-]\d{1,2}[)]?))?
    ((.?([012]{0,1}[1-9]{1}|30|31)\s
    ((januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)
    |(jan|feb|mar|apr|mei|jun|jul|aug|sept|nov|des)){1}\s\d{4}\s*))?
    ((pukul )?\d{1,2}[.:]\d{1,2}([.:]\d{1,2})?(\s+(WIB))?)?)
    """
    hasil =[]
    for m in re.finditer(pattern, text,re.VERBOSE | re.IGNORECASE):
        if(m.group() != ""):
            hasil.append(m.group())
    if(len(hasil) >= 1):
        return(hasil[0])
    #     time = ""
    #     for t in hasil:
    #         time += t
    #     return(time)
    # elif(len(hasil) == 1):
    #     return(hasil[0])
    else:
        return("None")
        

#Mencari jumlah atau angka
#jika angka ditemuka 2 kali cari yang terdekat dengan indeks
def REjumlah(awal,pat,text):
    tup = []
    reg = r"\d+((\.|,)+\d+)*"
    p = re.compile(reg)
    # awal = REexact(pat,text)
    akhir = awal + len(pat) - 1
    selisih = 9999999
    jumlah = ""
    for m in re.finditer(p, text):
        if(m.group != ""):
            tup.append((m.start(), m.end(), m.group()))
            # print(tup)
            
    if(len(tup) ==1):
        return (str(tup[0][2]))
    elif (len(tup) > 1):
        for i in range (len(tup)):
            if(tup[i][0] < awal):
                # print("A")
                temp = awal - tup[i][1] -1
            else:
                temp = tup[i][0] - akhir -1
                # print("B")
            if(temp<selisih):
                selisih = temp
                jumlah = tup[i][2]
        return((jumlah))
    else:
        return("Tidak tercantum jumlah")
    