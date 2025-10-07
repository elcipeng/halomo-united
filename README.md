# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
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

# Tugas 3: Implementasi Form dan Data Delivery pada Django
Nama : Justin Dwitama Seniang
NPM : 2406406742
Kelas : PBP D

PWS : https://justin-dwitama-halomounited.pbp.cs.ui.ac.id
POSTMAN : https://drive.google.com/file/d/1folqPAhhkmLQwJ5o-8yQAeTGT9Vvo0D-/view?usp=drive_link

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

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
Nama : Justin Dwitama Seniang
NPM : 2406406742
Kelas : PBP D

PWS : https://justin-dwitama-halomounited.pbp.cs.ui.ac.id

## 1. Apa itu Django AuthenticationForm

AuthenticationForm adalah form bawaan atau built in django yang digunakan untuk proses login pengguna. Form ini sudah otomatis menyediakan field username dan password, serta melakukan validasi terhadap kredensial yang dimasukkan.

Kelebihan:
1. Sudah terintegrasi dengan sistem autentikasi Django
2. Validasi username & password dilakukan otomatis.
3. Aman karena memanfaatkan mekanisme hashing password Django.
4. Praktis, tidak perlu membuat form login dari nol

Kekurangan:
1. Hanya mendukung login dengan username secara default (jika ingin login dengan email, perlu kustomisasi).
2.  Tampilannya sederhana, biasanya butuh modifikasi jika ingin menyesuaikan UI.

## 2. Perbedaan Autentikasi dan Otorisasi

Autentikasi = proses verifikasi identitas pengguna (contoh: login dengan username & password).

Otorisasi = proses menentukan hak akses setelah pengguna berhasil diautentikasi (contoh: hanya admin bisa menghapus data).

Implementasi di Django:\\
1. Autentikasi disediakan oleh sistem django.contrib.auth dengan AuthenticationForm, authenticate(), dan login().
2. Otorisasi dilakukan dengan Permissions, Groups, serta decorator seperti @login_required dan @permission_required.

## 3. Kelebihan dan Kekurangan Session & Cookies

Session:\\
-Kelebihan: Data disimpan di server, lebih aman; pengguna hanya menyimpan session ID di cookie.•	Kekurangan: Membebani server karena data session harus disimpan di database/memori.

Cookies:\\
-Kelebihan: Ringan, data langsung tersimpan di browser pengguna. Cocok untuk data kecil.
-Kekurangan: Rentan diubah pengguna, bisa dimanipulasi; risiko keamanan jika menyimpan data sensitif.

## 4. Apakah Cookies Aman Secara Default?

Tidak sepenuhnya aman. Risiko yang perlu diwaspadai:\\
	-Cookie theft (pencurian cookies) lewat serangan XSS.
	-Session hijacking jika cookie berisi session ID bocor.
	-Cookie manipulation karena pengguna bisa mengubah nilainya.

Cara Django menangani:\\
	-Password tidak pernah disimpan di cookie, hanya session ID yang disimpan.
	-Mendukung HttpOnly cookies (mencegah akses via JavaScript).
	-Mendukung Secure cookies (hanya dikirim melalui HTTPS).
	-Menyediakan proteksi CSRF secara default (csrftoken).

## 5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Untuk mengimplementasikan fungsi autentikasi, saya terlebih dahulu memahami bagaimana Django mengelola state login dengan session dan cookie. Django menyimpan informasi login pengguna melalui session, sehingga `request.user` bisa diakses di setiap request. Hal ini penting agar aplikasi dapat menyesuaikan tampilan sesuai status login maupun logout. Pada tahap registrasi, saya memanfaatkan `UserCreationForm` untuk mempermudah pembuatan akun baru, serta `messages` untuk memberi notifikasi. Fungsi registrasi saya buat di `views.py`, dengan kondisi jika request berupa POST maka data akan disimpan, lalu diarahkan ke halaman login. Setelah itu saya membuat halaman `register.html` dan menambahkan path ke `urls.py`.  
Selanjutnya saya membuat fitur login menggunakan `AuthenticationForm` dan fungsi `login()` dari Django. Jika data valid, pengguna akan diarahkan ke halaman utama, sekaligus saya set cookie `last_login` agar informasi login terakhir bisa ditampilkan kembali. Untuk logout, saya cukup menggunakan fungsi `logout()` dari Django, menambahkan logika di `views.py`, lalu menaruh tombol logout di `main.html` agar pengguna bisa keluar dengan mudah.  
Setelah fitur autentikasi berjalan, saya membuat dua akun pengguna berbeda dan masing-masing diberi tiga produk dummy. Model `Product` saya hubungkan dengan model `User` melalui field `owner = models.ForeignKey(User, on_delete=models.CASCADE)`. Dengan relasi ini, setiap produk akan tercatat sebagai milik pengguna tertentu.  
Terakhir, pada halaman utama saya menampilkan detail pengguna yang sedang login seperti username dan `last_login`. Informasi tersebut diambil dari `request.user` serta cookie yang sudah saya set sebelumnya. Dengan demikian, seluruh checklist seperti autentikasi, pembuatan akun dengan data dummy, relasi produk dengan user, serta tampilan detail informasi pengguna sudah terpenuhi.

# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
Nama : Justin Dwitama Seniang
NPM : 2406406742
Kelas : PBP D

PWS : https://justin-dwitama-halomounited.pbp.cs.ui.ac.id

## 1. Urutan Prioritas CSS Selector
Prioritas selector CSS ditentukan oleh spesifisitas (specificity). Aturan dengan spesifisitas lebih tinggi akan diterapkan. Urutan dari prioritas tertinggi hingga terendah adalah:
1. Inline Styles (atribut style="...")
2. ID Selectors (#id)
3. Class, Attribute, dan Pseudo-class Selectors (.class, [type="text"], :hover)
4. Type Selectors dan Pseudo-elements (h1, p, ::before)
Aturan !important akan mengesampingkan semua prioritas di atas.
Contoh:
CSS
p#intro { color: blue; } /* Lebih spesifik (ID) */
p.text { color: red; }   /* Kurang spesifik (Class) */
HTML
<p id="intro" class="text">Teks ini akan berwarna biru karena ID lebih prioritas.</p>

## 2. Pentingnya Responsive Design
Responsive design penting karena memastikan aplikasi web memberikan pengalaman pengguna (UX) yang optimal di semua perangkat (desktop, tablet, mobile). Hal ini krusial karena:
Mayoritas trafik web berasal dari perangkat mobile. Mengabaikan pengguna mobile berarti kehilangan sebagian besar audiens.
Meningkatkan peringkat SEO. Google memprioritaskan situs yang mobile-friendly.

Contoh:
Sudah Responsif: Tokopedia. Tampilannya berubah total dari versi desktop ke mobile. Navigasi di mobile pindah ke bawah agar mudah dijangkau jempol, dan produk ditampilkan dalam satu kolom vertikal yang mudah di-scroll.
Belum Responsif: Situs-situs akademik atau pemerintahan lama. Pengguna mobile harus melakukan pinch-and-zoom untuk membaca teks dan kesulitan menekan link yang terlalu kecil.

## 3. Pentingnya Responsive Design
Ketiganya adalah komponen dari CSS Box Model yang mengatur ruang di sekitar konten.
Padding: Ruang transparan di dalam border, yang memisahkan konten dari border.
Border: Garis yang mengelilingi padding dan konten.
Margin: Ruang transparan di luar border, yang memberi jarak antara elemen tersebut dengan elemen lain.
Implementasi:

CSS
.box {
  padding: 15px;           /* Ruang di dalam */
  border: 1px solid black; /* Garis bingkai */
  margin: 20px;            /* Jarak di luar */
}
## 4. Konsep Flexbox dan Grid Layout
Flexbox
Konsep: Layout satu dimensi untuk mengatur item dalam satu baris (row) atau satu kolom (column).
Kegunaan: Ideal untuk komponen UI seperti navbar, alignment item di dalam kartu, atau memusatkan konten.

Grid
Konsep: Layout dua dimensi untuk mengatur item dalam baris dan kolom secara bersamaan.
Kegunaan: Sempurna untuk layout halaman keseluruhan, seperti galeri produk, dashboard, atau tata letak kompleks lainnya.

## 5. Step-by-Step Implementasi Checklist

Proses pengerjaan tugas ini dilakukan dengan alur sebagai berikut:

1. Implementasi Fungsi dan Setup Awal: Langkah pertama adalah fokus pada backend. Saya mengimplementasikan fungsi edit_product dan delete_product di views.py beserta URL routing-nya di urls.py. Pada tahap ini, framework CSS Tailwind CSS juga diintegrasikan ke dalam proyek sebagai fondasi untuk semua kustomisasi desain yang akan dilakukan.

2. Desain Halaman Autentikasi: Setelah fungsionalitas inti siap, pekerjaan dilanjutkan ke antarmuka pengguna, dimulai dari halaman login dan register. Halaman-halaman ini didesain ulang dengan layout yang lebih modern, seperti menggunakan dua kolom dan menambahkan logo "Halomo United" untuk memberikan kesan profesional saat pengguna pertama kali berinteraksi dengan aplikasi.

3. Desain Halaman Utama dan Kartu Produk: Selanjutnya, saya merombak halaman utama (main page). Header teks yang sederhana diganti dengan Hero Section yang memiliki gambar latar dinamis untuk memberikan visual yang kuat. Kemudian, card_product.html didesain ulang agar lebih menarik dengan efek hover "pop-up". Pada kartu inilah tombol ikon untuk Edit dan Delete ditambahkan, menghubungkan desain frontend dengan fungsionalitas backend yang dibuat pada langkah pertama.

4. Kustomisasi Halaman Detail Produk: Halaman detail produk, yang diakses dari link "Read more" pada kartu, juga didesain ulang. Saya menerapkan layout dua kolom menggunakan Flexbox untuk memisahkan gambar produk di sisi kiri dan detail informasinya (harga, deskripsi, penjual) di sisi kanan, sehingga lebih mudah dibaca.

5. Finalisasi Desain Forms (Create & Edit): Sebagai langkah terakhir, saya melakukan kustomisasi pada halaman create_product.html dan edit_product.html. Untuk memastikan semua form memiliki tampilan yang konsisten, saya meninggalkan looping form Django yang generik. Sebagai gantinya, semua styling (seperti border, padding, dan focus ring) didefinisikan secara terpusat di forms.py menggunakan atribut widgets. Dengan cara ini, satu ProductForm yang sudah didesain dengan baik dapat digunakan untuk kedua halaman tersebut, memastikan tampilan yang seragam dan profesional.

# Tugas 6: Javascript dan AJAX
Nama : Justin Dwitama Seniang
NPM : 2406406742
Kelas : PBP D

PWS : https://justin-dwitama-halomounited.pbp.cs.ui.ac.id

## 1. Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request berjalan dengan cara menunggu satu proses selesai terlebih dahulu sebelum melanjutkan ke proses berikutnya, sehingga pengguna harus menunggu sampai halaman dimuat ulang sepenuhnya. Sedangkan asynchronous request memungkinkan pengiriman dan penerimaan data ke server tanpa harus me-reload seluruh halaman, sehingga proses lain tetap bisa berjalan paralel.

## 2. Bagaimana AJAX bekerja di Django (alur request–response)?
AJAX di Django bekerja dengan mengirimkan request ke server melalui JavaScript tanpa reload halaman. Request ini diproses oleh view di Django, lalu server mengembalikan response dalam format JSON atau data lain. Data tersebut kemudian diproses kembali oleh JavaScript di frontend untuk ditampilkan ke pengguna secara dinamis.

## 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
AJAX memberikan pengalaman yang lebih interaktif karena tidak memerlukan reload halaman penuh. Hal ini mengurangi waktu tunggu, membuat aplikasi lebih responsif, serta meningkatkan efisiensi karena hanya data yang dibutuhkan saja yang ditransfer, bukan seluruh halaman.

## 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

Keamanan AJAX dapat dijaga dengan memastikan penggunaan CSRF token pada setiap request, mengenkripsi data sensitif seperti password, serta melakukan validasi input baik di sisi frontend maupun backend. Selain itu, komunikasi sebaiknya menggunakan protokol HTTPS agar data tidak mudah disadap.

## 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

AJAX meningkatkan pengalaman pengguna karena membuat website terasa lebih cepat, dinamis, dan interaktif. Dengan meminimalkan reload halaman, pengguna bisa berinteraksi secara lebih mulus, misalnya saat login, register, atau mengirim data, sehingga alur penggunaan terasa lebih modern dan nyaman.
