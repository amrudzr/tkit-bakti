# Design System: Sistem Informasi TKIT

Dokumen ini merupakan kerangka lengkap (full stack) dari Sistem Desain TKIT. Sistem desain ini menggabungkan prinsip dasar, komponen teknis, panduan aksesibilitas, dan tata kelola untuk memastikan konsistensi pengembangan di platform Antigravity/Stitch.

## 1. Principles (Prinsip Desain)
*   **Mobile-First untuk Pengguna Eksternal:** Aplikasi Orang Tua dan Guru harus didesain untuk perangkat *mobile* terlebih dahulu. Navigasi harus terjangkau oleh ibu jari (thumb-friendly).
*   **Desktop-First untuk Operasional:** Dashboard Admin dan Kepala Sekolah didesain untuk layar lebar guna menampilkan *data table*, metrik agregasi, dan manajemen operasional (PPDB, SPP).
*   **Airy & Spacious:** Gunakan ruang kosong (*whitespace*) yang lapang untuk mencegah beban kognitif (cognitive overload), terutama bagi guru yang harus menginput banyak data setiap hari.
*   **Fail Loudly, Recover Gracefully (Prinsip AI/Sistem):** Jika sistem (atau agen AI) gagal memproses data (misal gagal integrasi Payment Gateway), error harus ditampilkan dengan jelas kepada user, lengkap dengan langkah solusinya.

## 2. Design Tokens
Token desain adalah abstraksi dari nilai-nilai visual (merujuk pada `style_guide.md`). Diimplementasikan dalam bentuk variabel CSS atau konfigurasi Tailwind (`tailwind.config.js`).

*   **Colors:** 
    *   `color-primary`: `#342781` (Deep Royal Purple)
    *   `color-secondary`: `#FFB800` (Warm Gold)
    *   `color-surface`: `#FFFFFF`
    *   `color-background`: `#F6F5FC`
*   **Spacing:** Skala 4px (misal: `spacing-xs`: 4px, `spacing-md`: 16px, `spacing-xl`: 32px).
*   **Radii (Border Radius):** 
    *   `radius-base`: 8px (`rounded-lg`) untuk input.
    *   `radius-large`: 16px (`rounded-2xl`) untuk *cards*.
    *   `radius-pill`: 9999px (`rounded-full`) untuk *buttons*.

## 3. Components & Code
Komponen antarmuka yang dibangun dari token dan pola (merujuk pada `pattern_library.md`). Semua komponen harus berupa komponen React/UI yang dapat digunakan kembali (*reusable*).

*   **Buttons:** Latar belakang solid `color-primary`, tanpa border, dengan `radius-pill`. Teks putih `font-weight: 700`.
*   **Inputs/Forms:** Latar belakang putih, border tipis abu-abu. Saat aktif (fokus), muncul *ring* berwarna `color-primary`.
*   **Cards:** Menggunakan `radius-large`, latar `color-surface`, dan *box-shadow* lembut (`shadow-sm`).
*   *(Untuk daftar pola yang lebih kompleks, lihat `pattern_library.md`).*

## 4. Accessibility Rules (Aturan Aksesibilitas)
Sistem ini digunakan oleh orang tua dan guru dari berbagai rentang usia dan kemampuan penglihatan.
*   **Kontras Warna:** Semua teks harus memenuhi standar kontras WCAG 2.1 AA (rasio minimal 4.5:1 terhadap latar belakang). Teks putih di atas Ocean Teal sudah memenuhi standar ini.
*   **Ukuran Sentuh (Touch Targets):** Semua tombol dan elemen interaktif di aplikasi mobile (Orang Tua & Guru) harus memiliki ukuran sentuh minimal **44x44 pixel** untuk mencegah salah tekan.
*   **Label Form:** Semua input form (terutama pendaftaran PPDB) harus memiliki label yang jelas, tidak hanya mengandalkan *placeholder* yang akan menghilang saat diketik.

## 5. Governance & Contribution Model
Bagaimana tim mengelola dan memperbarui sistem desain ini:
*   **Single Source of Truth:** Dokumen ini dan implementasinya di konfigurasi proyek Stitch adalah sumber kebenaran tunggal.
*   **Proses Kontribusi:** 
    1. Jika developer atau *AI Agent* menemukan kebutuhan UI baru yang belum ada di `pattern_library.md`, buat sebagai komponen lokal (komponen satu kali pakai).
    2. Jika komponen tersebut digunakan di lebih dari 3 tempat berbeda, ajukan modifikasi (*Pull Request* / Evaluasi) untuk memasukkannya ke dalam inti Design System.
*   **Agentic Governance (Untuk AI Agents):** Sub-agent pengembang (seperti `/ai-agents-architect` dan agen Frontend) yang bekerja pada *codebase* diinstruksikan untuk selalu merujuk pada token di `tailwind.config.js` dan tidak menggunakan nilai *hard-coded* (seperti `bg-[#123456]`), melainkan `bg-primary`.

## 6. AI Architecture & Documentation Standards
*Berdasarkan instruksi `documentation-generation-doc-generate` dan `ai-agents-architect`:*
*   **Dokumentasi Otomatis:** API endpoint (misal untuk Payment Gateway dan PPDB) dan alur agen AI harus didokumentasikan secara otomatis menggunakan spesifikasi OpenAPI.
*   **Orkestrasi AI:** Jika sistem mengimplementasikan agen otonom (misal: Agen Pengingat Tagihan SPP atau Agen Perangkum Tumbuh Kembang), agen harus mengikuti arsitektur **Plan-and-Execute** dengan batasan limit iterasi (Circuit Breakers) yang ketat untuk mencegah *looping* tanpa batas. Semua aktivitas agen harus dilog dengan jelas untuk keperluan audit admin.
