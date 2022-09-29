## Link Heroku App

Link aplikasi Django yang sudah di-deploy ke Heroku: [https://django-assignment-elsa.herokuapp.com/todolist/](https://django-assignment-elsa.herokuapp.com/todolist/)

## Kegunaan `{% csrf_token %}`

CSRF token berguna untuk membuat unique value untuk disertakan pada HTTP request client. CSRF token berguna untuk keamanan. CSRF token berperan untuk menghindari peretasan data oleh hacker. Jika tidak ada, maka request client akan ditolak oleh webserver dan hacker akan dengan mudah untuk melakukan pencurian data client.

## Pembuatan `<form>` Secara Manual

Bisa. Cara membuat `<form>` secara manual adalah dengan memanggil masing-masing atribut yang diperlukan dengan menggunakan `{{form.name_of_field}}`. Misalnya kita akan membuat Login form secara manual dan yang kita butuhkan adalah username dan password untuk login, maka pada file HTML nya dapat kita tulis
    
    <div class="fieldWrapper">
    {{ form.username.errors }}
    {{ form.username.label_tag }}
    {{ form.username }}
    </div>
    <div class="fieldWrapper">
    {{ form.password.errors }}
    {{ form.password.label_tag }}
    {{ form.password }}
    </div>
Form username dan password untuk login sudah terbuat.
 
## Proses Alur Data

Pertama, pengguna mengisi form dan mengklik tombol Submit. Data yang diisikan oleh pengguna tersebut akan tersimpan dalam bentuk object pada database Django sesuai dengan atribut model yang telah dibuat sebelumnya. Misalnya pada aplikasi todolist untuk membuat task baru. Pengguna akan mengeklik tombol `Tambah Task Baru`. Lalu, pengguna akan di-direct ke url yang sesuai, yaitu `/create-task` dan template tampilan HTML yang akan muncul adalah `create_task.html`. Pengguna akan mengisi field form dan saat pengguna mengklik tombol `Tambah`, pengguna akan di-direct ke tampilan todolist. Data yang tadi pengguna masukkan akan tampil. Hal ini karena data tersebut sudah masuk ke dalam database Django dengan atributnya adalah yang telah didefinisikan pada `models.py`. Pada `views.py`, data tersebut akan diambil dan ditampilkan pada template HTML yang sesuai.

## Cara Implementasi

Pertama, saya membuat app baru bernama todolist dengan menjalankan perintah `python manage.py startapp todolist`. Lalu, saya mendaftarkan app tersebut pada variabel INTALLED_APPS yang ada pada settings.py di folder project_django. Kemudian, pada variabel `urlpatterns` di file urls.py di folder project_django ditambahkan `path('todolist/', include('todolist.urls'))`. 

Kemudian, pada models.py saya membuat model Task dengan atribut user, date, title, description. Lalu, saya menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate`untuk memigrasi skema model yang telah dibuat pada file models.py di folder todolist ke dalam *database* Django lokal. Saya menambahkan atribut is_finished dan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` kembali.

Lalu, pada views.py saya membuat fungsi show_todolist yang menerima parameter request. Fungsi ini untuk menampilkan data todolist. Saya juga membuat fungsi register yang menerima parameter request untuk registrasi akun. Selain itu, saya juga membuat fungsi login yang menerima parameter request untuk login akun. Saya juga membuat fungsi logout yang menerima parameter request untuk skema logout akun. Kemudian, saya membuat forms.py untuk membuat class TaskForm yang nantinya akan digunakan untuk membuat form task baru. Form ini akan menerima input title dan description task dari pengguna. Kemudian, pada views.py saya membuat fungsi baru bernama create_task yang menerima parameter request yang digunakan untuk menambah task baru. Untuk mengautentikasi, di atas fungsi show_todolist dan create_task saya menambahkan `@login_required(login_url='/todolist/login/')`. Untuk mengimplementasikan fungsi-fungsi tersebut saya meng-import berikut ini.

    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import authenticate, login, logout
    from django.contrib.auth.decorators import login_required
    from django.contrib import messages
    from django.contrib.auth.models import User
    from todolist.models import Task
    from todolist.forms import TaskForm

Selanjutnya, saya membuat folder templates di todolist. Kemudian, saya membuat todolist.html, register.html, login.html, dan create_task.html. File-file HTML tersebut merupakan format tampilan HTML jika link aplikasi dipanggil. Lalu, saya membuat file urls.py di folder todolist dan menulis kode berikut.

    from django.urls import path
	from todolist.views import show_todolist

	app_name = 'todolist'

	urlpatterns = [
    	path('', show_todolist, name='show_todolist'),
	]
Kemudian, pada urls.py saya menambahkan import dari todolist.views berupa create_task, register, login_user, logout_user. Saya juga mendaftarkan path pada urlpatterns sebagai berikut.
    
    urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    ]

Lalu, saya menambahkan fitur tombol delete. Pada views.py, saya membuat fungsi delete yang menerima parameter request dan id. Saya juga menambahkan import delete pada urls.py dan mendaftarkan path delete. Saya juga membuat file HTML baru yaitu delete.HTML sebagai format tampilan jika fungsi delete dipanggil.

Selanjutnya, saya melakukan push ke GitHub dan secara otomatis aplikasi Heroku ter-deploy dan aplikasi dapat diakses melalui *link* yang ada pada *section* [Link Heroku App](https://github.com/elsagiana/django-assignment/tree/main/todolist#link-heroku-app).
