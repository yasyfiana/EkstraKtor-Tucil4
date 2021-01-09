#Yasyfiana Fariha
#13518143
#Program
#Tucil 4
import os
import re
from BM import *
from KMP import *
from RE import *
from nltk.tokenize import sent_tokenize

#Convert file menjadi list of sentence
def ConvertText(filename):
    script_dir = os.path.dirname(__file__)
    loc = "text\\"
    rel_path = loc + filename
    pathfile = os.path.join(script_dir, rel_path)
    with open(pathfile, 'r') as file:
        text = file.read().lower()
        text = sent_tokenize(text)
    return(text)

"""
Pekerjaan Utama dalam program ekstraksi ini
Program akan memanggil Convertlist
Setiap sentence di list tersebut di cek apapah ada kata keywoard yang dimasukan
pencocokan sesuai algoritma yang di pilih
jika cocok, program akan melakukan pengecekan ada keterangan waktu atau tidak
jika jika tidak ada gunakan waktu teks
setelah itu melakukan pencarian angka
PEMAHAMAN pembuat program. Jika string ditemukan, namun angka tidak
diasumsikan menampilkan pesan angka tidak ditemukan
"""
def match(word,algo,filename):
    sentL = ConvertText(filename)
    word = word.lower()
    awalan = re.split('\n', sentL[0])
    judul = awalan[0]
    waktufile = awalan[2]
    del sentL[0]
    sentL.insert(0,awalan[4])
    sentL.insert(0,judul)
    # print(awalan[4])
    hasil = []
    if(algo == "Regex"):
        for s in sentL:
            # print(s)
            t = s
            awal = REexact(word, s)
            res =[]
            if(awal != -1):
                waktu = REWaktu(s)
                if(waktu == "None"):
                    waktu = waktufile
                else:
                    s = re.sub(waktu,"",s)
                jumlah = REjumlah(awal,word,s)
                
                res.append("Jumlah    :" + jumlah)
                res.append("Waktu     :" + waktu)
                res.append(t + "(" + filename + ")")
                hasil.append(res)
        return(hasil)      
    elif (algo == "KMP"):
        for s in sentL:
            # print(s)
            t = s
            awal = KMP(s, word)
            res =[]
            if(awal != -1):
                waktu = REWaktu(s)
                if(waktu == "None"):
                    waktu = waktufile
                else:
                    s = re.sub(waktu,"",s)
                jumlah = REjumlah(awal,word,s)
                
                res.append("Jumlah    :" + jumlah)
                res.append("Waktu     :" + waktu)
                res.append(t + "(" + filename + ")")
                hasil.append(res)
        return(hasil)
    elif (algo == "BM"):
        for s in sentL:
            # print(s)
            t = s
            awal = (BM(s, word))
            res =[]
            if(awal != -1):
                waktu = REWaktu(s)
                if(waktu == "None"):
                    waktu = waktufile
                else:
                    s = re.sub(waktu,"",s)
                jumlah = REjumlah(awal,word,s)
                
                res.append("Jumlah    :" + jumlah)
                res.append("Waktu     :" + waktu)
                res.append(t + "(" + filename + ")")
                hasil.append(res)
        return(hasil)
# match("corona","BM",'doc5.txt')
    
