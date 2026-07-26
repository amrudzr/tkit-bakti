# Pattern Library: Sistem Informasi TKIT

Dokumen ini berisi koleksi pola antarmuka (UI patterns) yang dapat digunakan kembali untuk mempercepat pengembangan Sistem Informasi TKIT. Setiap pola memiliki panduan penggunaan spesifik berdasarkan audiens (Orang Tua, Guru, Admin).

## 1. Navigation Structures

### 1.1. Mobile Bottom Navigation (Aplikasi Orang Tua & Guru)
*   **Pola:** Bilah navigasi di bagian bawah layar dengan 4-5 ikon utama.
*   **Penggunaan:** Digunakan pada Parent Portal dan Teacher App karena keduanya adalah aplikasi *mobile-first*.
*   **Item Orang Tua:** Beranda (Home), Aktivitas (Feed), Tagihan (Billing), Profil/Buku Penghubung.
*   **Item Guru:** Kelas, Input Jurnal, Presensi, Pesan.

### 1.2. Sidebar & Topbar (Web Admin Dashboard)
*   **Pola:** Navigasi vertikal di sebelah kiri (Sidebar) yang dapat diciutkan (*collapsible*), dipadukan dengan Topbar untuk pencarian dan profil.
*   **Penggunaan:** Khusus untuk Kepala Sekolah dan Admin PPDB/Keuangan yang mengakses via desktop.
*   **Keunggulan:** Mendukung hierarki menu yang dalam (misal: Data Master > Guru, Siswa, Kelas).

## 2. Form Layouts

### 2.1. Multi-step Wizard (Form PPDB)
*   **Pola:** Formulir panjang yang dipecah menjadi beberapa langkah dengan *progress bar* di bagian atas (Contoh: 1. Data Anak -> 2. Data Orang Tua -> 3. Upload Dokumen).
*   **Penggunaan:** Pendaftaran siswa baru oleh orang tua.
*   **Panduan:** Jangan meminta terlalu banyak input dalam satu layar. Validasi dilakukan per langkah (*step*).

### 2.2. Batch Input List (Input KBM & Presensi Guru)
*   **Pola:** Daftar siswa berbaris vertikal, di mana tiap baris memiliki opsi *toggle/checkbox* cepat (Hadir/Tidak, Hafalan Lancar/Mengulang).
*   **Penggunaan:** Mempercepat kerja guru saat mengabsen atau menilai hafalan satu kelas.
*   **Panduan:** Tombol "Simpan Semua" (Save All) diletakkan di bagian bawah secara *sticky* agar tidak perlu *scroll* jauh.

## 3. Card Patterns

### 3.1. Activity Feed Card (Jurnal Harian)
*   **Pola:** Kartu yang berisi header (Nama kelas/guru, Waktu), media (Foto kegiatan), dan deskripsi teks di bawahnya. Mirip dengan tampilan pos media sosial.
*   **Penggunaan:** Ditampilkan di beranda portal Orang Tua agar mereka bisa melihat kegiatan anak hari ini.
*   **Visual:** Menggunakan sudut membulat (`rounded-xl`), bayangan halus (`shadow-sm`), dan batas visual yang jelas antar kartu.

### 3.2. Billing Status Card (Kartu Tagihan)
*   **Pola:** Kartu yang menyoroti Nominal besar, Tanggal Jatuh Tempo, dan *Badge* Status (Menunggu Pembayaran / Lunas).
*   **Penggunaan:** Halaman Keuangan orang tua.
*   **Interaksi:** Kartu dengan status "Menunggu Pembayaran" memiliki tombol *call-to-action* sekunder (misal: "Bayar Sekarang") yang mengarah ke Payment Gateway.

### 3.3. Student Profile Card
*   **Pola:** Foto profil melingkar, Nama anak, Kelas, dan Ikon ringkas untuk info darurat (alergi).
*   **Penggunaan:** Digunakan di aplikasi Guru saat melihat daftar murid di kelasnya.

## 4. Intelligent AI Patterns (Integrasi AI)

### 4.1. Smart Summary (Ringkasan AI)
*   **Pola:** Kotak *callout* dengan ikon AI (Sparkles) yang berisi teks ringkasan.
*   **Penggunaan:** Digunakan di Dashboard Kepsek untuk merangkum narasi otomatis dari data presensi dan keuangan bulan ini, atau ringkasan tumbuh kembang anak dari jurnal harian yang ditulis guru.
*   **Panduan:** Selalu berikan indikasi visual bahwa teks tersebut di-*generate* oleh AI agar admin/guru dapat memverifikasi ulang.
