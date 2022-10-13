# Tugas 6
## Perbedaan *Asynchronous Programming* dan *Synchronous Programming*

**Asynchronous programming:** 

Pada asynchronous programming, lebih dari satu operasi dapat berjalan bersamaan tanpa harus menunggu task lain selesai terlebih dahulu. Asynchronous programming tidak memblokir suatu eksekusi ketika lebih dari satu operasi sedang berjalan. Asynchronous merupakan multi-thread model. Asynchronous programming merupakan non-blocking architecture sehingga multiple request dapat dikirim ke server. Pada web, perubahan dapat terjadi atau request dapat dieksekusi tanpa harus melakukan load ulang pada seluruh web

**Synchronous programming:** 

Pada synchronous programming, hanya satu operasi yang dapat berjalan pada satu waktu. Eksekusi akan dilakukan secara berurutan berdasarkan urutan perintah eksekusi. Jika suatu operasi sedang berjalan, maka operasi lain akan diblokir. Jika satu task sudah selesai, maka task selanjutnya akan dieksekusi. Synchronous programming merupakan blocking architecture sehingga hanya satu request saja yang dapat dikirim ke server. Pada web, perubahan dapat terlihat atau request dapat dieksekusi dengan harus melakukan load ulang web terlebih dahulu.

## Paradigma *Event-Driven Programming* dan Contoh Penerapannya

Event-Driven Programming merupakan paradigma yang menerapkan suatu operasi akan dieksekusi setelah dilakukan trigger dari suatu event. Contohnya adalah saat mengklik tombol add new task. Saat tombol add new task diklik maka modal yang berisi form akan muncul. Munculnya modal di-trigger oleh event mouse click. Selain itu, saat mengklik tombol add maka task baru akan ditambahkan pada tabel. Penambahan task ini juga di-trigger oleh event mouse click.

## Penerapan *Asynchronous Programming* pada AJAX

AJAX merupakan singkatan dari Asynchronous Javascript and XML. AJAX dapat meng-update halaman web tanpa harus melakukan load ulang keseluruhan halaman web dengan melakukan pertukaran data dengan web server di belakang layar. Data akan di-fetch oleh XMLHttpRequest object di belakang layar. Jika suatu event terjadi pada suatu web page, maka XMLHttpRequest object akan dibuat oleh JavaScript. Kemudian, XMLHttpRequest object akan mengirimkan request ke server web dan request tersebut akan diproses oleh server. Kemudian, server akan memberikan respons terhadap request tersebut dan respons tersebut akan dibaca oleh JavaScript. Lalu, JavaScript akan meng-update halaman web.

## Cara Implementasi

1. Pertama, saya membuat fungsi baru pada views.py bernama todolist_json yang menerima parameter request untuk mengembalikan data dalam bentuk JSON.
2. Kemudian, saya membuat path baru pada urls.py, yaitu /json yang mengarah kepada fungsi todolist_json yang telah dibuat di views.py.
3. Lalu, saya membuat fungsi show_todolist_ajax dan membuat file html baru bernama untuk todolist_ajax.html untuk pengimplementasian AJAX pada todolist.
4. Selanjutnya, saya membuat fungsi add_task_ajax pada views.py untuk pengimplementasian form dengan ajax untuk menambahkan task baru. Saya juga membuat path baru di urls.py, yaitu /add yang mengarah kepada fungsi add_task_ajax pada views.py.
5. Pada todolist_ajax.html, saya menyalin potongan kode dari todolist.html dan memodifikasinya sesuai dengan to do Tugas 6.
6. Pada todolist_ajax.html, saya mengimplementasikan modal yang berisi form untuk menambahkan task baru.
7. Saya juga menambahkan script untuk pengimplementasian AJAX.
8. Saya membuat fungsi asynchronous untuk membuat tabel yang berisi task dan akan diload secara asynchronous setiap task baru dibuat. Pada fungsi ini saya juga mengimplementasikan AJAX GET untuk mengambil data JSON task yang sudah dibuat.
9. Saya juga membuat fungsi untuk pengimplementasian AJAX POST untuk form pembuatan task baru. Setelah task ditambahkan, field pada form akan di-reset dan modal akan tertutup.
10. Saya juga menambahkan eventlistener untuk pembuatan task. Ketika tombol add diklik maka fungsi untuk pengimplementasian AJAX POST akan berjalan dan tabel akan ter-load secara asynchronous untuk menambahkan task yang baru ditambahkan.