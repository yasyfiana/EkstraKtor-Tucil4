# PUSKUSI
Aplikasi ekstraksi informasi dengan berupa angka dan tanggal dari informasi keyword yang diberikan input. Aplikasi ini disusun menggunakan bahasa python dengan menggunakan library regex dan nltk. Aplikasi berbasis web ini menggunakan flask sebagai perkakasnya. Aplikasi ini digunakan untuk memenuhi 

## Getting Started
Sebelum menjalankan aplikasi ini ada beberapa hal yang perlu diperhatikan mengenai environment yang harus dipenuhi. Aplikasi ini melakukan import terhadap beberapa libarary yaitu regex untuk melakukan pencocokan, nltk untuk merubah menjadi beberapa kalimat, dan os untuk mendapatkan file path. Dan Aplikasi ini menggunakan Flask sebagai perkakas untuk membangun web aplikasi dengan bantuan templet html

### Prerequisites & Installing
* nltk, di windows bisa dengan mnjalankan kode berikut di terminal python 
import nltk 
nltk.download()
* regex, bisa dengan pip install regex.
* Tidak lupa pastikan telah mengintall Flask
* Pastikan folder test yang berisikan file test berada di directory yang sama dengan app.py

## Running the program
* Pastikan prerequisties telah terpenuhi.
* Jika sudah terpenuhi, buka command prompt (windows) pada directory yang sama dengan file app.py berada.
* compile file app.py, bisa lakukan 'python app.py'. Tunggu hingga cmd menampilkan Running on http:/...
* Copy alamat tersebut ke browser anda. Dan aplikasi siap dijalankan.
* Untuk menjalankan program anda perlu memasukan keywoard, memilihalgoritma pencocokkan string, dan memasukan file.
* Setelah itu tekan tombol 'cek' untuk melihat hasil ektraksi, dan tombol 'perihal' untuk melihat perihal dari aplikasi ini


### Break down into end to end tests
Dalam folder testcase terdapat beberapa text yang dapat dicari menggnaakan kata kunci tertentu. Bisa jadi antara satu file dan file yang lain tidak memiliki irisan kata. Dan tentu belum tentu semua kata yang kita masukan berada pada file tersebut.


## Author
Yasyfiana Fariha Putrisusari
NIM 13518143
Teknik INFORMATIKA
