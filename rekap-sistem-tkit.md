# Rekap Diskusi: Sistem Informasi TKIT (TK Islam Terpadu)

> Dokumen ini merangkum hasil diskusi mengenai referensi, business flow, dan mockup untuk platform sistem informasi TKIT. Digunakan sebagai bahan lanjutan untuk implementasi di Antigravity / Stitch.

---

## 1. Konteks & Referensi

Sistem informasi sekolah (SIM Sekolah) di Indonesia umumnya berupa platform terpadu yang bisa diakses oleh guru, wali kelas, staf TU, siswa, dan orang tua untuk mempermudah operasional sekolah dan kegiatan belajar mengajar.

Untuk sekolah Islam Terpadu, implementasi SIM Akademik berbasis teknologi jadi kebutuhan agar layanan pendidikan tetap akurat, tepat, dan cepat.

**Poin regulasi yang perlu diperhatikan (khusus data anak):**
- UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)
- UU ITE terbaru (UU No. 1 Tahun 2024)
- Sistem idealnya kompatibel dengan infrastruktur IT sekolah dan bisa integrasi dengan LMS, keuangan, PPDB

**Contoh vendor lokal sebagai pembanding:** SIM-Sekolah, Pijar Sekolah, Skoolacloud — fitur umum mereka: penjadwalan, jurnal, buku tamu digital, perpustakaan digital, pengelolaan sarpras, pencatatan pelanggaran siswa, pembayaran iuran fleksibel.

---

## 2. Business Flow — Modul Inti TKIT

Berbeda dari SD/SMP, sistem TKIT lebih menekankan **monitoring + komunikasi orang tua** dibanding akademik formal (tidak ada nilai ujian/rapor angka).

| # | Modul | Fungsi Utama |
|---|-------|---------------|
| 1 | **PPDB Online** | Pendaftaran, upload dokumen, verifikasi admin |
| 2 | **Verifikasi & Penempatan Kelas** | Kelompok A/B, wali kelas, jadwal harian |
| 3 | **Presensi Digital** | Check-in/out anak (QR/RFID), notifikasi real-time ke orang tua |
| 4 | **KBM & Aktivitas** | Jurnal kegiatan, hafalan surat/doa harian, galeri foto |
| 5 | **SPP & Tagihan** | Pembayaran bulanan, uang kegiatan, uang seragam |
| 6 | **Laporan Tumbuh Kembang** | Perkembangan motorik, kognitif, keagamaan (bukan nilai angka) |
| 7 | **Portal/App Orang Tua** | Akses eksternal — pantau presensi, laporan, buku penghubung |
| 8 | **Payment Gateway** | Virtual Account, e-wallet, QRIS |
| 9 | **Dashboard Admin/Kepsek** | Laporan keuangan, statistik siswa, overview sistem |

### Alur Utama (Flow Diagram)

```
PPDB Online
    ↓
Verifikasi & Kelas
    ↓
Presensi Harian ──────→ Portal Orang Tua (akses real-time)
    ↓
KBM & Aktivitas
    ↓
SPP & Tagihan ─────────→ Payment Gateway (VA, e-wallet, QRIS)
    ↓
Tumbuh Kembang (laporan berkala ke ortu)
    ↓
Dashboard Admin (laporan & statistik)
```

**Legenda kategori:**
- Alur pendaftaran (awal proses)
- Operasional harian (presensi, KBM)
- Keuangan & laporan (SPP, tumbuh kembang, dashboard)
- Akses orang tua / eksternal (portal, payment gateway)

---

## 3. Referensi Template Mockup

### Figma Community (gratis)
- **PreSkool** — UI kit gratis untuk ERP sekolah & dashboard pendidikan, layout modern
- **School Management Admin Dashboard UI** — design system open-use, komponen & screen siap pakai
- **Smansys** — Admin Dashboard UI Kit untuk institusi pendidikan
- **Stellar School Mobile App UI Kit** — modul mobile: Super Admin, Guru, Siswa, Staf Keuangan, Staf Bus
- **School App UI Kit (ERP)** — paket premium, 21 screen siap pakai

### Envato Elements (berbayar/subscription)
- Katalog UI/UX kit khusus school management, ada varian tag "Preschool" dan "Admission School" — lebih niche buat kebutuhan TK

### Figma UI Mockup Templates Hub
- 1000+ template device frame (web/mobile/desktop) untuk membungkus hasil desain jadi presentasi profesional ke klien

### Rekomendasi Jalur Cepat
1. Fork **PreSkool** atau **School Management Admin Dashboard UI** sebagai base
2. Custom branding + tambahkan modul spesifik TKIT yang belum ada di template umum: tumbuh kembang, hafalan, buku penghubung
3. Bungkus hasil akhir pakai device frame dari hub mockup untuk presentasi klien

---

## 4. Rencana Lanjutan

- [ ] Pindah workflow ke **Antigravity**, diterapkan ke konfigurasi **Stitch** yang sudah disiapkan
- [ ] Breakdown tiap modul jadi user story / requirement teknis untuk tim dev
- [ ] Susun wireframe checklist per screen berdasarkan template Figma yang dipilih
- [ ] (Opsional) Buat dokumen formal (proposal/BRD) untuk dikirim ke klien

---

## 5. Business Requirements Document (BRD)
*(Hasil analisis lanjutan)*

### 5.1. Modul Operasional Harian
- **Presensi Digital**: 
  - **User Story**: Guru dapat scan QR/RFID, orang tua menerima notifikasi real-time saat anak sampai/pulang.
  - **Tech**: Integrasi hardware (API/WebSocket) dan notifikasi push (Firebase/WhatsApp).
- **KBM & Aktivitas**:
  - **User Story**: Guru menginput foto kegiatan dan progres hafalan, orang tua memantau dari portal.
  - **Tech**: UI interaktif untuk batch input, optimasi penyimpanan media (kompresi gambar).
- **Laporan Tumbuh Kembang**:
  - **User Story**: Guru mengisi nilai kualitatif deskriptif, orang tua menerima rekap bulanan/semester.
  - **Tech**: Rubrik penilaian di frontend, PDF rendering engine di backend.

### 5.2. Modul Administrasi & Keuangan
- **PPDB Online**:
  - **User Story**: Orang tua mendaftar dan unggah dokumen (KK/Akta), admin memverifikasi.
  - **Tech**: Form wizard pendaftaran, cloud storage terintegrasi.
- **SPP & Payment Gateway**:
  - **User Story**: Admin men-generate tagihan otomatis, orang tua bayar via QRIS/VA dan terkonfirmasi lunas.
  - **Tech**: Cron jobs/scheduler untuk tagihan, webhook listener untuk callback payment gateway.
- **Dashboard Admin/Kepsek**:
  - **User Story**: Kepala sekolah memantau statistik siswa, kehadiran, dan keuangan secara visual.
  - **Tech**: Chart library, Redis caching untuk metrik agregasi, dan RBAC terstruktur.

---

## 6. Checklist Wireframe UI/UX (Target: Antigravity/Stitch)

**📱 1. Aplikasi Orang Tua (Parent Portal)**
- [ ] **Home / Dashboard**: Timeline presensi hari ini, status tagihan terdekat.
- [ ] **KBM & Jurnal**: Feed harian ala media sosial, visualisasi hafalan dengan *progress bar*/*bintang*.
- [ ] **Pembayaran**: Daftar tagihan, checkout via payment gateway, bukti digital.
- [ ] **Buku Penghubung**: Chat ringan/pesan langsung dengan wali kelas anak.

**👩‍🏫 2. Aplikasi Guru (Teacher App)**
- [ ] **Dashboard Kelas**: List anak dengan foto profil dan status absensi.
- [ ] **Input KBM (Batch)**: Form upload jurnal foto dan check-list hafalan harian secara massal.
- [ ] **Evaluasi Tumbuh Kembang**: Slider/rating kualitatif (mis. "Mulai Berkembang") per anak.

**💻 3. Dashboard Admin (Web Panel)**
- [ ] **Overview**: Widget total siswa, kas bulanan, tingkat kehadiran.
- [ ] **Verifikasi PPDB**: Tabel pendaftar lengkap dengan dokumen dan fungsi assign ke kelas (Kelompok A/B).
- [ ] **Tagihan (Billing)**: Bulk generate tagihan dan status lunas/tunggakan per siswa.

---

*Dokumen ini dibuat sebagai rekap kerja — silakan disesuaikan lagi sesuai kebutuhan implementasi di Stitch/Antigravity.*
