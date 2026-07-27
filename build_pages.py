import os

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the boundaries
hero_idx = content.find('    <!-- Hero Section -->')
footer_idx = content.find('    <!-- Footer -->')

head_nav = content[:hero_idx]
footer_part = content[footer_idx:]

# Update the navbar links to point back to index.html
head_nav_sub = head_nav.replace('href="#beranda"', 'href="index.html#beranda"')
head_nav_sub = head_nav_sub.replace('href="#profil"', 'href="index.html#profil"')
head_nav_sub = head_nav_sub.replace('href="#peta-persebaran"', 'href="index.html#peta-persebaran"')
head_nav_sub = head_nav_sub.replace('href="#berita"', 'href="index.html#berita"')
head_nav_sub = head_nav_sub.replace('href="#ppdb"', 'href="index.html#ppdb"')
head_nav_sub = head_nav_sub.replace('href="#galeri"', 'href="index.html#galeri"')

# SEJARAH HTML
sejarah_css = """
    <style>
        .timeline-section { padding: 100px 0; background-color: var(--bg-gray); overflow: hidden; }
        .timeline { position: relative; max-width: 1000px; margin: 0 auto; }
        .timeline::after { content: ''; position: absolute; width: 4px; background-color: var(--primary); top: 0; bottom: 0; left: 50%; margin-left: -2px; border-radius: 2px;}
        .timeline-container { padding: 10px 40px; position: relative; width: 50%; }
        .timeline-container.left { left: 0; }
        .timeline-container.right { left: 50%; }
        .timeline-container::after { content: ''; position: absolute; width: 24px; height: 24px; right: -12px; background-color: var(--white); border: 4px solid var(--primary); top: 20px; border-radius: 50%; z-index: 1; }
        .timeline-container.right::after { left: -12px; }
        .timeline-content { padding: 30px; background-color: var(--white); position: relative; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .timeline-content h3 { color: var(--primary); font-size: 1.5rem; margin-bottom: 10px; }
        .timeline-content h4 { color: var(--text-dark); font-size: 1.2rem; margin-bottom: 15px; }
        .timeline-date { display: inline-block; padding: 5px 15px; background: var(--secondary-light); color: var(--primary-dark); font-weight: bold; border-radius: 50px; margin-bottom: 15px; font-size: 0.9rem;}
        
        .page-hero { background-color: var(--primary); color: white; padding: 100px 0 60px; text-align: center; position: relative;}
        .page-hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 20px; }
        .page-hero p { font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto; }

        @media screen and (max-width: 768px) {
            .timeline::after { left: 31px; }
            .timeline-container { width: 100%; padding-left: 70px; padding-right: 25px; }
            .timeline-container.right { left: 0; }
            .timeline-container.left::after, .timeline-container.right::after { left: 19px; }
        }
    </style>
"""

sejarah_body = """
    <!-- Page Hero -->
    <section class="page-hero">
        <div class="container">
            <h1>Sejarah YPBWI</h1>
            <p>Membangun generasi cerdas berakhlak mulia sejak langkah pertama.</p>
        </div>
    </section>

    <!-- Timeline Section -->
    <section class="timeline-section">
        <div class="container">
            <div class="timeline">
                <div class="timeline-container left" data-aos="fade-up">
                    <div class="timeline-content">
                        <div class="timeline-date">Tahun 1990</div>
                        <h3>Pendirian Yayasan</h3>
                        <p>YPBWI (Yayasan Pendidikan Bakti Wanita Islam) resmi didirikan dengan cita-cita mulia untuk memberikan akses pendidikan yang berkualitas dan berlandaskan ajaran agama Islam.</p>
                    </div>
                </div>
                <div class="timeline-container right" data-aos="fade-up">
                    <div class="timeline-content">
                        <div class="timeline-date">Tahun 1995</div>
                        <h3>TK Islam Bakti Pertama</h3>
                        <p>Pembukaan cabang pertama TK Islam Bakti. Di sinilah langkah awal sistem pendidikan anak usia dini kami diterapkan dengan metode belajar sambil bermain yang islami.</p>
                    </div>
                </div>
                <div class="timeline-container left" data-aos="fade-up">
                    <div class="timeline-content">
                        <div class="timeline-date">Tahun 2005</div>
                        <h3>Penerapan Kurikulum Terpadu</h3>
                        <p>Memadukan kurikulum nasional dengan pendidikan karakter dan hafalan Al-Quran juz 30, menjadikan TK Islam Bakti sebagai salah satu pelopor pendidikan karakter anak.</p>
                    </div>
                </div>
                <div class="timeline-container right" data-aos="fade-up">
                    <div class="timeline-content">
                        <div class="timeline-date">Tahun 2015</div>
                        <h3>Ekspansi Cabang</h3>
                        <p>Seiring dengan tingginya kepercayaan masyarakat, yayasan berhasil mendirikan belasan cabang baru di berbagai penjuru kota untuk menjangkau lebih banyak anak-anak.</p>
                    </div>
                </div>
                <div class="timeline-container left" data-aos="fade-up">
                    <div class="timeline-content">
                        <div class="timeline-date">Tahun 2026 - Sekarang</div>
                        <h3>16 Cabang Unggulan</h3>
                        <p>Kini YPBWI mengelola 16 cabang TK Islam Bakti yang tersebar luas, dilengkapi fasilitas modern, serta didukung oleh ratusan tenaga pengajar profesional.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open('sejarah.html', 'w', encoding='utf-8') as f:
    f.write(head_nav_sub.replace('</style>', sejarah_css + '</style>') + sejarah_body + footer_part)


# PROFIL HTML
profil_css = """
    <style>
        .page-hero { background-color: var(--primary); color: white; padding: 100px 0 60px; text-align: center; position: relative;}
        .page-hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 20px; }
        .page-hero p { font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto; }
        
        .profile-section { padding: 80px 0; background-color: var(--white); }
        .vm-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px; }
        .vm-card { padding: 40px; background: var(--bg-gray); border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .vm-card i { font-size: 3rem; color: var(--secondary); margin-bottom: 20px; }
        .vm-card h3 { font-size: 1.8rem; color: var(--primary-dark); margin-bottom: 20px; }
        .vm-card p { font-size: 1.1rem; color: var(--text-gray); }
        
        .structure-section { padding: 80px 0; background-color: var(--bg-gray); text-align: center; }
        .org-chart { max-width: 800px; margin: 0 auto; padding: 40px; background: var(--white); border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .org-node { padding: 15px 30px; background: var(--primary); color: white; border-radius: 10px; display: inline-block; font-weight: bold; margin-bottom: 20px; }
        
        @media screen and (max-width: 768px) {
            .vm-grid { grid-template-columns: 1fr; }
        }
    </style>
"""

profil_body = """
    <!-- Page Hero -->
    <section class="page-hero">
        <div class="container">
            <h1>Profil Yayasan</h1>
            <p>Mengenal lebih dekat Visi, Misi, dan dedikasi YPBWI di bidang pendidikan.</p>
        </div>
    </section>

    <!-- Visi Misi -->
    <section class="profile-section">
        <div class="container">
            <div class="section-header" style="text-align: center;" data-aos="fade-up">
                <span class="section-tag">TUJUAN KAMI</span>
                <h2>Visi & Misi Yayasan</h2>
            </div>
            <div class="vm-grid">
                <div class="vm-card" data-aos="fade-up" data-aos-delay="100">
                    <i class="fa-solid fa-eye"></i>
                    <h3>Visi</h3>
                    <p>"Menjadi lembaga pendidikan usia dini terdepan yang mengintegrasikan nilai-nilai keislaman, kecerdasan emosional, dan pengetahuan modern untuk melahirkan generasi penerus bangsa yang unggul, berakhlak mulia, dan siap menghadapi tantangan masa depan."</p>
                </div>
                <div class="vm-card" data-aos="fade-up" data-aos-delay="200">
                    <i class="fa-solid fa-bullseye"></i>
                    <h3>Misi</h3>
                    <p>
                        1. Menyelenggarakan pendidikan berkualitas dengan pendekatan belajar sambil bermain.<br><br>
                        2. Menanamkan adab, nilai moral, dan cinta Al-Quran sejak dini.<br><br>
                        3. Meningkatkan kompetensi dan profesionalisme tenaga pendidik secara berkesinambungan.<br><br>
                        4. Menjalin sinergi yang kuat antara pihak sekolah, orang tua, dan lingkungan masyarakat.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Struktur Organisasi -->
    <section class="structure-section">
        <div class="container">
            <div class="section-header" data-aos="fade-up">
                <span class="section-tag">PENGURUS</span>
                <h2>Struktur Organisasi (Contoh)</h2>
            </div>
            <div class="org-chart" data-aos="zoom-in">
                <div class="org-node" style="background: var(--primary-dark);">Ketua Yayasan</div>
                <br><i class="fa-solid fa-arrow-down" style="color: var(--text-gray); margin-bottom: 20px;"></i><br>
                <div class="org-node">Sekretaris</div> &nbsp;&nbsp;&nbsp;&nbsp; <div class="org-node">Bendahara</div>
                <br><i class="fa-solid fa-arrow-down" style="color: var(--text-gray); margin-bottom: 20px;"></i><br>
                <div class="org-node" style="background: var(--secondary); color: var(--primary-dark);">Kepala Divisi Pendidikan</div>
                <br><i class="fa-solid fa-arrow-down" style="color: var(--text-gray); margin-bottom: 20px;"></i><br>
                <div class="org-node" style="background: var(--white); color: var(--text-dark); border: 2px solid var(--primary);">Kepala Sekolah TK Islam Bakti 1 - 16</div>
            </div>
        </div>
    </section>
"""

with open('profil.html', 'w', encoding='utf-8') as f:
    f.write(head_nav_sub.replace('</style>', profil_css + '</style>') + profil_body + footer_part)


# CABANG HTML
cabang_css = """
    <style>
        .page-hero { background-color: var(--primary); color: white; padding: 100px 0 60px; text-align: center; position: relative;}
        .page-hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 20px; }
        .page-hero p { font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto; }
        
        .cabang-section { padding: 80px 0; background-color: var(--bg-gray); }
        .cabang-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px; }
        .cabang-card { background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.05); transition: transform 0.3s; border: 1px solid #eaeaea; }
        .cabang-card:hover { transform: translateY(-5px); border-color: var(--primary); }
        
        .cabang-header { background: var(--primary-light); padding: 20px; color: white; text-align: center; }
        .cabang-header h3 { font-size: 1.4rem; color: var(--primary-dark); font-weight: 800; }
        .cabang-body { padding: 25px; }
        .cabang-body p { margin-bottom: 10px; color: var(--text-gray); display: flex; gap: 10px; align-items: flex-start; }
        .cabang-body i { color: var(--secondary); margin-top: 4px; }
        
        .search-container { max-width: 600px; margin: -30px auto 40px; position: relative; z-index: 10; display: flex; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-radius: 50px; overflow: hidden;}
        .search-input { flex: 1; padding: 20px 30px; border: none; font-size: 1.1rem; outline: none; font-family: inherit;}
        .search-btn { background: var(--secondary); border: none; padding: 0 30px; color: var(--primary-dark); font-weight: bold; cursor: pointer; transition: background 0.3s;}
        .search-btn:hover { background: var(--secondary-light); }
    </style>
"""

# Generate 16 branches dummy data
cabang_cards = ""
for i in range(1, 17):
    delay = (i % 3) * 100
    cabang_cards += f'''
                <div class="cabang-card" data-aos="fade-up" data-aos-delay="{delay}">
                    <div class="cabang-header">
                        <h3>TK Islam Bakti {i}</h3>
                    </div>
                    <div class="cabang-body">
                        <p><i class="fa-solid fa-location-dot"></i> Jl. Contoh Pendidikan No. {i}, Surakarta</p>
                        <p><i class="fa-solid fa-phone"></i> (0271) 12345{i:02d}</p>
                        <p><i class="fa-solid fa-clock"></i> Senin - Jumat: 07.30 - 14.00</p>
                    </div>
                </div>'''

cabang_body = f"""
    <!-- Page Hero -->
    <section class="page-hero">
        <div class="container">
            <h1>Jelajahi TK Kami</h1>
            <p>Temukan 16 cabang TK Islam Bakti yang terdekat dengan lokasi Anda.</p>
        </div>
    </section>

    <div class="container">
        <div class="search-container">
            <input type="text" class="search-input" placeholder="Cari lokasi TK terdekat (Contoh: Banjarsari)...">
            <button class="search-btn"><i class="fa-solid fa-search"></i> Cari</button>
        </div>
    </div>

    <!-- Cabang Grid -->
    <section class="cabang-section">
        <div class="container">
            <div class="section-header" style="text-align: center;" data-aos="fade-up">
                <h2>Daftar 16 Cabang TK Islam Bakti</h2>
            </div>
            <div class="cabang-grid">
                {cabang_cards}
            </div>
        </div>
    </section>
"""

with open('cabang.html', 'w', encoding='utf-8') as f:
    f.write(head_nav_sub.replace('</style>', cabang_css + '</style>') + cabang_body + footer_part)
