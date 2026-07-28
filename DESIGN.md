# Design System: Sistem Informasi TKIT
**Project ID:** [Pending Creation]

## 1. Visual Theme & Atmosphere
Visual theme untuk aplikasi TKIT ini mengusung nuansa **"Friendly, Clean, dan Trustworthy"**. Desainnya harus memberikan rasa aman dan profesional bagi orang tua, namun tetap terasa hangat, ceria, dan tidak kaku (cocok untuk institusi pendidikan anak usia dini). Atmosfer antarmuka dibuat **"Airy & Spacious"** (luas dan lega) untuk menghindari kesan rumit pada aplikasi guru dan orang tua, dengan density informasi yang diatur agar mudah dipindai (scannable).

## 2. Color Palette & Roles
Palet warna didesain untuk ramah anak namun tetap terlihat kredibel bagi administrasi sekolah.

*   **Deep Royal Purple (#342781)**
    *   *Fungsi:* Warna primer (Primary). Digunakan untuk *call-to-action* utama, *header*, *sidebar* aktif, dan elemen branding utama YPBWI. Memberikan kesan elegan, islami, dan terpercaya.
*   **Warm Gold (#FFB800)**
    *   *Fungsi:* Warna sekunder / aksen (Secondary). Digunakan untuk menarik perhatian pada notifikasi penting, *badges*, tombol aksi utama/sekunder, dan aksen ceria.
*   **Mint Success (#22C55E)**
    *   *Fungsi:* Warna status sukses. Digunakan untuk indikator kelulusan hafalan, status SPP Lunas, dan notifikasi check-in presensi yang berhasil.
*   **Soft Slate Background (#F8FAFC)**
    *   *Fungsi:* Warna latar belakang halaman (Background). Putih keabu-abuan yang sangat lembut untuk mengurangi kelelahan mata saat guru atau orang tua membaca jurnal.
*   **Deep Charcoal Text (#1E293B)**
    *   *Fungsi:* Warna teks utama (Text High-Emphasis). Digunakan untuk judul, teks paragraf, dan data penting. Memberikan kontras maksimal untuk keterbacaan.
*   **Muted Blue-Gray (#94A3B8)**
    *   *Fungsi:* Warna teks sekunder (Text Low-Emphasis) dan garis batas (*border*). Digunakan untuk teks *placeholder*, tanggal pada jurnal, dan pembatas konten.

## 3. Typography Rules
Tipografi menggunakan pendekatan modern dan bersih untuk memastikan keterbacaan tinggi di berbagai ukuran perangkat, khususnya mobile (untuk aplikasi orang tua).

*   **Font Family:** **Inter** atau **Nunito** (Nunito memberikan kesan membulat yang lebih ramah dan cocok untuk konteks pendidikan anak).
*   **Headers (H1 - H3):** Menggunakan *font weight* **Bold (700)** atau **ExtraBold (800)**. Spasi huruf (*letter-spacing*) dibuat sedikit lebih rapat (tighter) untuk tampilan yang solid.
*   **Body & Paragraf:** Menggunakan *font weight* **Regular (400)** dan **Medium (500)** dengan *line-height* yang cukup longgar (relaxed, 1.5 - 1.6) agar nyaman dibaca saat guru mengisi catatan tumbuh kembang.
*   **Microcopy / Caption:** Menggunakan ukuran teks lebih kecil dengan *font weight* **Medium (500)** untuk status label dan *badge*.

## 4. Component Stylings
Komponen UI didesain membulat (*rounded*) untuk meminimalisir kesan tajam dan kaku, memperkuat kesan *playful* dan *friendly*.

*   **Buttons (Tombol):**
    *   *Shape:* "Pill-shaped" atau ujung membulat penuh (`rounded-full`) untuk tombol aksi utama. Tombol ukuran kecil menggunakan `rounded-lg` (sudut membulat lembut).
    *   *Styling:* Tombol utama menggunakan latar belakang solid **Soft Ocean Teal**, tanpa *border*, dengan teks putih tebal. Tombol sekunder menggunakan *outline* (garis luar) atau latar belakang pudar/transparan dengan teks berwarna Ocean Teal.
    *   *Interaction:* Perubahan warna menjadi sedikit lebih gelap (*shade*) saat di-*hover*, disertai efek micro-animation (sedikit ditekan/scale-down).
*   **Cards/Containers (Kartu Konten):**
    *   *Shape:* Sudut membulat dengan ukuran yang generos (`rounded-xl` atau `rounded-2xl`).
    *   *Background:* Putih solid (`#FFFFFF`) di atas *Soft Slate Background*.
    *   *Shadow & Elevation:* Menggunakan "Whisper-soft diffused shadows" (bayangan jatuh yang sangat halus, besar, dan transparan, misal `shadow-sm` atau `shadow-md` dengan opasitas rendah) agar kartu terlihat melayang tipis (menggambarkan kedalaman yang *clean*).
*   **Inputs/Forms (Kolom Isian):**
    *   *Shape:* Ujung membulat lembut (`rounded-lg`).
    *   *Styling:* Latar belakang putih atau sangat terang, dengan garis luar tipis (*stroke*) berwarna Muted Blue-Gray (`#E2E8F0`). Saat aktif (fokus), garis luar berubah menjadi Soft Ocean Teal yang sedikit ditebalkan (`ring-2`) untuk menandakan aksesibilitas interaksi.

## 5. Layout Principles
Prinsip *layout* berfokus pada ruang kosong (*white space*) dan pengelompokan informasi yang jelas.

*   **Whitespace & Margins:** Menerapkan strategi "Generous Padding". Setiap grup informasi dalam *card* diberikan *padding* yang luas (misal `p-6` atau 24px) agar konten tidak terlihat sesak. Margin antar *section* dibuat lebar.
*   **Grid Alignment:** Menggunakan sistem *grid* 12 kolom untuk Dashboard Admin (desktop-first). Untuk portal Orang Tua dan Guru (mobile-first), menggunakan tata letak kolom tunggal (stack) vertikal dengan lebar maksimal (*max-width*) untuk *form* pendaftaran dan *feed* aktivitas.
*   **Visual Hierarchy:** Elemen terpenting (seperti Status SPP belum lunas atau Notifikasi Anak Sakit) diposisikan di atas (Top-Fold) dengan penggunaan ukuran teks lebih besar dan didukung *badge* warna aksen (Sunrise Tangerine).
