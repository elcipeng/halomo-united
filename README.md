#Tugas Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Nama : Justin Dwitama Seniang
NPM : 2406406742
Kelas : PBP D

PWS : https://justin-dwitama-halomounited.pbp.cs.ui.ac.id

## Implementasi Checklist
Berikut adalah penjelasan step-by-step bagaimana saya mengimplementasikan checklist:

1. **Membuat proyek Django baru**  
   - Menjalankan perintah `django-admin startproject project_name`.
   - Masuk ke folder proyek lalu jalankan `python manage.py runserver` untuk memastikan proyek berhasil dibuat.

2. **Membuat aplikasi baru (`main`)**  
   - Menjalankan perintah `python manage.py startapp main`.
   - Menambahkan aplikasi `main` ke dalam `INSTALLED_APPS` pada `settings.py`.

3. **Routing awal**  
   - Membuat file `urls.py` di dalam aplikasi `main`.
   - Menambahkan routing pada `project/urls.py` untuk menghubungkan aplikasi `main`.

4. **Membuat model Product**  
   - Menambahkan class `Product` di `models.py` dengan field:
     - `name = models.CharField(max_length=255)`
     - `price = models.IntegerField()`
     - `description = models.TextField()`
     - `thumbnail = models.URLField()`
     - `category = models.CharField(max_length=100)`
     - `is_featured = models.BooleanField(default=False)`
   - Melakukan `python manage.py makemigrations` lalu `python manage.py migrate`.

5. **Membuat views dan template**  
   - Menambahkan fungsi di `views.py` untuk mengirim data ke template HTML.
   - Template menampilkan nama aplikasi, nama, dan kelas.

6. **Membuat routing di urls.py (main)**  
   - Memetakan fungsi view yang sudah dibuat agar bisa diakses lewat browser.

7. **Deployment ke PWS**  
   - Menyiapkan konfigurasi deployment.
   - Upload proyek agar dapat diakses secara online.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

link gdrive: https://drive.google.com/drive/folders/1ldSR1utcvo-JcDrEzcY5GCV_WwXmFuoK?usp=sharing

1. Client kirim HTTP Request
    Masuk pertama kali ke urls.py.

2. urls.py
    Menentukan request ini harus diarahkan ke view mana.

3. views.py
    Mengolah request. Kalau perlu data dari database → komunikasi dengan models.py (read/write data).Mengirim data ke template untuk ditampilkan.

4. Template (HTML)
    Menampilkan data sesuai konteks dari view.

5. HTTP Response
    Dikirim balik ke client.

Jadi alurnya udah sesuai konsep MVT (Model-View-Template) milik Django.

## Peran settings.py dalam Proyek Django
settings.py berfungsi sebagai pusat konfigurasi proyek Django. Beberapa hal yang diatur di dalamnya antara lain:
INSTALLED_APPS: daftar aplikasi yang digunakan dalam proyek.
DATABASES: konfigurasi database yang dipakai.
TEMPLATES: pengaturan untuk template engine Django.
STATICFILES: pengaturan untuk file statis (CSS, JS, gambar).
DEBUG dan ALLOWED_HOSTS: pengaturan untuk mode development atau production.

## Cara Kerja Migrasi Database di Django

Ketika model diubah/ditambah, jalankan python manage.py makemigrations untuk membuat file migrasi.
Jalankan python manage.py migrate untuk menerapkan perubahan tersebut ke database.
Django menggunakan sistem ORM (Object Relational Mapping) sehingga kita tidak perlu menulis SQL secara langsung.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dipilih sebagai framework pertama untuk dipelajari karena:

Full-featured: sudah menyediakan banyak fitur bawaan (autentikasi, admin panel, ORM, routing, dll) sehingga tidak perlu menulis semuanya dari nol.
Konvensi yang jelas: Django punya struktur proyek yang terorganisir dengan baik, memudahkan pemula memahami alur aplikasi web.
Komunitas besar dan dokumentasi lengkap: sangat membantu ketika belajar atau menemukan kendala.
Mendorong best practice: Django menekankan konsep separation of concerns (memisahkan logic, tampilan, dan data), yang penting dalam pengembangan software jangka panjang.
Cocok untuk pembelajaran dasar web development: dengan Django, kita bisa belajar konsep fundamental seperti request–response, model–view–template, dan migrasi database.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tutorial sudah sangat membantu dan simpel sekali untuk diikuti

#Tugas Tugas 3: Implementasi Form dan Data Delivery pada Django
Nama : Justin Dwitama Seniang
NPM : 2406406742
Kelas : PBP D

PWS : https://justin-dwitama-halomounited.pbp.cs.ui.ac.id

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan agar informasi dari server dapat sampai ke client dengan format yang bisa diproses. Tanpa mekanisme pengiriman data, aplikasi tidak bisa berinteraksi secara dinamis. Misalnya, pengguna hanya akan melihat tampilan statis tanpa ada perubahan data terbaru. Dengan data delivery, platform bisa menampilkan data real-time, melakukan update otomatis, dan mendukung integrasi dengan sistem lain.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

-JSON lebih baik untuk kebanyakan kasus modern karena:
-Lebih ringkas dan lebih mudah dibaca.
-Mendukung struktur data langsung (array, objek) tanpa markup berlebihan.
-Parsing JSON lebih efisien dibandingkan XML.
-Banyak framework modern langsung mendukung JSON.
XML masih dipakai untuk sistem lama atau kebutuhan khusus (misalnya data dengan schema kompleks), tapi JSON lebih populer karena kesederhanaan dan kecepatan.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() digunakan untuk memvalidasi data yang dikirim lewat form. Method ini akan memeriksa apakah semua field sudah diisi sesuai aturan (misalnya tipe data benar, tidak ada field wajib yang kosong). Kita membutuhkan method ini supaya data yang masuk ke database valid dan terhindar dari error maupun data kotor.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token adalah token keamanan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa request form benar-benar berasal dari website kita, bukan dari website berbahaya lain.
- Jika tidak ada csrf_token, penyerang bisa membuat form palsu yang secara diam-diam mengirimkan request ke server kita (misalnya transfer uang, ubah data, hapus akun).
- Dengan token ini, server hanya menerima request yang memiliki kode unik sesuai sesi pengguna, sehingga aman dari penyalahgunaan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat 4 views untuk menampilkan data (XML, JSON, XML by ID, JSON by ID).
2. Menambahkan URL routing pada urls.py untuk setiap views.
3. Membuat halaman index yang menampilkan daftar objek model dan menambahkan tombol Add serta Detail.
4. Membuat halaman form untuk menambahkan data baru ke model.
5. Membuat halaman detail untuk melihat informasi lengkap objek tertentu.
6. Menguji semua fitur agar berjalan sesuai checklist.
7. Menulis jawaban pertanyaan ini di README.md.

## 6. Apakah ada feedback untuk untuk asdos di tutorial 2 yang sudah kalian kerjakan?

-Penjelasan sudah jelas tapi bisa lebih banyak contoh praktis.
-Waktu praktikum terlalu cepat, sebaiknya ada waktu tambahan untuk tanya jawab.
-Materi sudah sesuai dengan kebutuhan tugas.