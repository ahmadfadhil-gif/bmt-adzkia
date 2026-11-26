#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merakit seluruh halaman situs dari header/nav/footer bersama.
Jalankan: python3 build.py
"""
import glob
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

HEAD_LINKS = """<link rel="icon" type="image/png" href="assets/logo-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">"""

WA_LINK = "https://wa.me/6285878755748"
WA_LINK_KANTOR = "https://wa.me/6285199603106"   # Tanya cara mendaftar & Syarat pengajuan
PHONE_TEL = "+62287661386"
PHONE_DISPLAY = "(0287) 661386"
EMAIL = "ksppsdamba@gmail.com"

def header(active=""):
    def cls(key):
        return " class=\"current\"" if key == active else ""
    return f"""<a class="skip-link" href="#main">Langsung ke konten utama</a>

<div class="topbar">
  <div class="wrap">
    <div class="topbar-left">
      <div class="social-icons">
        <a href="https://www.facebook.com/profile.php?id=61551480452807" title="Facebook" aria-label="Facebook" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor" aria-hidden="true"><path d="M22 12.06C22 6.53 17.52 2 12 2S2 6.53 2 12.06c0 5 3.66 9.13 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.51 1.49-3.9 3.77-3.9 1.09 0 2.23.2 2.23.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.87h2.78l-.44 2.91h-2.34V22c4.78-.81 8.44-4.94 8.44-9.94z"/></svg></a>
        <a href="https://www.instagram.com/barokatul_adzkia" title="Instagram" aria-label="Instagram" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg></a>
        <a href="https://www.tiktok.com/@baitul.maal.barok" title="TikTok" aria-label="TikTok" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor" aria-hidden="true"><path d="M16.5 2h-3v13.6a3 3 0 1 1-2.6-2.97V9.5a6.1 6.1 0 1 0 5.6 6.08V9.2a7.9 7.9 0 0 0 4.5 1.4V7.6a4.6 4.6 0 0 1-4.5-4.6z"/></svg></a>
      </div>
    </div>
    <div class="topbar-right">
      <div class="topbar-item">☎ <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
      <div class="topbar-item">✉ <a href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
  </div>
</div>

<header class="masthead">
  <div class="wrap">
    <div class="masthead-info">
      <div>Kantor Pusat, Ambal Kebumen</div>
      <div class="phone-big">{PHONE_DISPLAY}</div>
    </div>
    <div class="brand">
      <div class="brand-mark"><img src="assets/logo-icon.png" alt="Logo BMT Barokatul Adzkia"></div>
      <div class="brand-text">
        <h1>KSPPS BMT Barokatul Adzkia</h1>
        <p>Menuai Berkah Dengan Syariah</p>
      </div>
    </div>
    <div class="masthead-meta">
      <div><strong>Jam Operasional:</strong></div>
      <div>Senin–Jumat 08.00–15.00 &middot; Sabtu 08.00–12.00</div>
    </div>
  </div>
</header>

<nav class="mainnav">
  <div class="wrap">
  <div class="nav-inner">
    <a class="nav-brand" href="index.html"><img src="assets/logo-icon.png" alt=""><span>KSPPS BMT Barokatul Adzkia</span></a>
    <button class="navbar-toggle" id="navToggle" aria-expanded="false" aria-controls="navList">☰</button>
    <ul class="nav-list" id="navList">
      <li><a href="index.html"{cls('beranda')}>Beranda</a></li>
      <li><a href="profil.html"{cls('profil')}>Profil Koperasi <span class="chevron">▾</span></a>
        <ul class="submenu">
          <li><a href="tentang-kami.html">Tentang Kami</a></li>
          <li><a href="legalitas.html">Legalitas</a></li>
          <li><a href="visi-misi.html">Visi &amp; Misi</a></li>
          <li><a href="sejarah.html">Sejarah</a></li>
          <li><a href="kantor-cabang.html">Kantor Cabang <span class="subarrow">›</span></a>
            <ul class="submenu">
              <li><a href="kantor-cabang.html#tabel">Tabel Kantor Cabang</a></li>
              <li><a href="kantor-cabang.html#maps">Lokasi Kantor (Maps)</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="produk.html"{cls('produk')}>Produk Kami <span class="chevron">▾</span></a>
        <ul class="submenu">
          <li><a href="produk.html#simpanan">Simpanan Anggota <span class="subarrow">›</span></a>
            <ul class="submenu">
              <li><a href="produk.html#si-rela">Si Rela (Simpanan Sukarela)</a></li>
              <li><a href="produk.html#si-pendi">Si Pendi (Simpanan Pendidikan)</a></li>
              <li><a href="produk.html#si-suqur">Si Suqur (Simpanan Qurban/Aqiqah)</a></li>
              <li><a href="produk.html#si-fitri">Si Fitri (Simpanan Idul Fitri)</a></li>
              <li><a href="produk.html#si-simka">Si Simka (Simpanan Mudharabah Berjangka)</a></li>
              <li><a href="produk.html#simpanan-haji">Simpanan Haji/Umroh</a></li>
            </ul>
          </li>
          <li><a href="produk.html#pembiayaan">Pembiayaan Anggota <span class="subarrow">›</span></a>
            <ul class="submenu">
              <li><a href="produk.html#modal-kerja">Pembiayaan Modal Kerja</a></li>
              <li><a href="produk.html#investasi">Pembiayaan Investasi</a></li>
              <li><a href="produk.html#konsumtif">Pembiayaan Konsumtif</a></li>
            </ul>
          </li>
          <li><a href="produk.html#keanggotaan">Keanggotaan</a></li>
        </ul>
      </li>
      <li><a href="gallery.html"{cls('gallery')}>Gallery <span class="chevron">▾</span></a>
        <ul class="submenu">
          <li><a href="gallery.html#foto">Foto Kegiatan</a></li>
          <li><a href="gallery.html#video">Video Dokumentasi</a></li>
        </ul>
      </li>
      <li><a href="download.html"{cls('download')}>Download <span class="chevron">▾</span></a>
        <ul class="submenu">
          <li><a href="download.html#brosur">Brosur &amp; Formulir</a></li>
          <li><a href="download.html#syarat">Syarat Pengajuan</a></li>
        </ul>
      </li>
      <li><a href="kenapa-kami.html"{cls('kenapa')}>Kenapa Memilih Kami</a></li>
    </ul>
    <div class="nav-search">
      <input type="text" id="siteSearchInput" placeholder="Cari sesuatu">
      <button type="button" id="siteSearchBtn" aria-label="Cari">🔍</button>
    </div>
  </div>
  </div>
</nav>
"""

def page_head_block(title, desc):
    return f"""<div class="page-head">
  <div class="wrap">
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</div>"""

def crumb(items):
    # items: list of (label, href_or_None)
    parts = []
    for label, href in items:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(label)
    inner = " / ".join(parts)
    return f'<div class="crumb"><div class="wrap">{inner}</div></div>'

FOOTER = f"""<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>KSPPS BMT Barokatul Adzkia</h4>
        <p>Jl. Raya Kambalan, RT 02 RW 04, Kembangsawit, Kec. Ambal, Kab. Kebumen, Prov. Jawa Tengah</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h4>Jam Layanan</h4>
        <p>Senin – Jumat: 08.00 – 15.00</p>
        <p>Sabtu: 08.00 – 12.00</p>
        <p>Minggu &amp; hari libur nasional: tutup</p>
      </div>
      <div>
        <h4>Navigasi</h4>
        <a href="profil.html">Profil Koperasi</a>
        <a href="produk.html">Produk Kami</a>
        <a href="gallery.html">Gallery</a>
        <a href="download.html">Download</a>
        <a href="kenapa-kami.html">Kenapa Memilih Kami</a>
      </div>
    </div>
    <div class="footer-bottom">
      © <span id="year"></span> KSPPS BMT Barokatul Adzkia Kebumen. Seluruh hak cipta dilindungi.
    </div>
  </div>
</footer>

<a class="wa-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Chat WhatsApp"><svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.43 15.1L2 22l5.05-1.32A9.93 9.93 0 1 0 12.04 2zm0 1.8a8.13 8.13 0 1 1-4.15 15.14l-.3-.18-3 .78.8-2.92-.2-.3A8.13 8.13 0 0 1 12.04 3.8zM8.6 7.5c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.06 3.3 5.1 4.5 2.52 1 3.03.8 3.57.75.55-.05 1.76-.72 2-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35s-1.76-.87-2.03-.97c-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57z"/></svg></a>
<script src="js/site.js"></script>
</body>
</html>"""

def page(title, description, active, body):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - KSPPS BMT Barokatul Adzkia</title>
<meta name="description" content="{description}">
{HEAD_LINKS}
</head>
<body>
<div class="page-loader" id="pageLoader"><div class="page-loader-spinner"></div></div>
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
"""

# ---------------------------------------------------------------------------
# BERANDA
# ---------------------------------------------------------------------------
index_body = f"""
  <section class="hero" id="beranda">
    <div class="wrap">
      <div>
        <div class="hero-eyebrow">Koperasi Simpan Pinjam Pembiayaan Syariah</div>
        <h2>Melayani anggota di Ambal, Kebumen dengan prinsip keuangan syariah sejak berdiri.</h2>
        <p class="lead">Amanah, profesional, dan mandiri — dari anggota, oleh anggota, untuk anggota. Simpanan dan pembiayaan dijalankan sesuai akad syariah.</p>
        <div class="cc-buttons">
          <a class="cc-btn solid" href="{WA_LINK}" target="_blank">Hubungi via WhatsApp</a>
          <a class="cc-btn" href="produk.html">Lihat produk kami</a>
        </div>
        <p class="warn">Hati-hati terhadap penipuan yang mengatasnamakan KSPPS BMT Barokatul Adzkia.</p>
        <div class="hero-slider" id="heroSlider">
          <div class="hero-slide active">
            <h3>Amanah &middot; Profesional &middot; Mandiri</h3>
            <p>Menjadi lembaga keuangan syariah yang bermanfaat bagi umat di Ambal dan sekitarnya.</p>
          </div>
          <div class="hero-slide">
            <h3>Simpanan &amp; Pembiayaan Syariah</h3>
            <p>Melayani kebutuhan simpan pinjam anggota berdasarkan akad-akad syariah.</p>
          </div>
          <div class="hero-slide">
            <h3>Dari Anggota, Oleh Anggota, Untuk Anggota</h3>
            <p>Dikelola secara profesional, efektif, efisien, dan transparan.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="trust">
    <div class="wrap">
      <div class="trust-item"><b>AHU-0000307.AH.01.38 / 2023</b><span>Nomor Badan Hukum</span></div>
      <div class="trust-item"><b>3305070150008</b><span>Nomor Induk Koperasi</span></div>
      <div class="trust-item"><b>Ambal, Kebumen</b><span>Kantor pusat &amp; 4 unit layanan</span></div>
      <div class="trust-item"><b>Prinsip Syariah</b><span>Seluruh akad sesuai jati diri koperasi</span></div>
    </div>
  </section>

  <section id="profil-teaser">
    <div class="wrap">
      <div class="section-head">
        <div class="kicker">Profil Koperasi</div>
        <h2>Mengenal KSPPS BMT Barokatul Adzkia</h2>
        <p>Lembaga keuangan mikro syariah yang melayani anggota di Ambal, Kebumen — amanah, profesional, dan mandiri.</p>
      </div>
      <a class="cc-btn" style="border-color:var(--blue);color:var(--blue)" href="profil.html">Lihat profil lengkap</a>
    </div>
  </section>

  <section class="alt-bg">
    <div class="wrap">
      <div class="section-head">
        <div class="kicker">Nilai Kami</div>
        <h2>Kenapa memilih kami</h2>
      </div>
      <div class="why-grid">
        <div class="why-card"><h3>Sesuai prinsip syariah</h3><p>Seluruh produk simpanan dan pembiayaan dijalankan berdasarkan akad syariah.</p></div>
        <div class="why-card"><h3>Dekat dengan anggota</h3><p>Melayani langsung masyarakat di wilayah Ambal, Kebumen dan sekitarnya.</p></div>
        <div class="why-card"><h3>Pelayanan profesional</h3><p>Dikelola secara efektif, efisien, dan transparan sesuai jati diri koperasi.</p></div>
      </div>
    </div>
  </section>

  <section class="cta-band" id="kontak">
    <div class="wrap">
      <div>
        <h3>Ingin tahu produk simpanan atau pembiayaan kami?</h3>
        <p>Hubungi kantor kami di jam operasional Senin – Jumat 08.00 – 15.00, Sabtu 08.00 – 12.00.</p>
      </div>
      <a class="cc-btn solid" href="tel:+6285199603106">☎ +62 851-9960-3106</a>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# PROFIL (hub)
# ---------------------------------------------------------------------------
profil_body = f"""
{crumb([("Beranda","index.html"),("Profil Koperasi",None)])}
{page_head_block("Profil Koperasi", "Mengenal lebih dekat KSPPS BMT Barokatul Adzkia — legalitas, arah lembaga, dan perjalanannya.")}
  <section>
    <div class="wrap">
      <div class="hub-grid">
        <div class="hub-card">
          <div class="kicker">Profil Lembaga</div>
          <h3>Tentang Kami</h3>
          <p>Nama lembaga, alamat kantor, dan kontak resmi KSPPS BMT Barokatul Adzkia.</p>
          <a class="more" href="tentang-kami.html">Selengkapnya</a>
        </div>
        <div class="hub-card">
          <div class="kicker">Profil / Badan Hukum</div>
          <h3>Legalitas</h3>
          <p>Data badan hukum dan penghargaan KSPPS BMT Barokatul Adzkia.</p>
          <a class="more" href="legalitas.html">Selengkapnya</a>
        </div>
        <div class="hub-card">
          <div class="kicker">Arah Lembaga</div>
          <h3>Visi &amp; Misi</h3>
          <p>Motto, visi, dan misi yang menjadi pedoman arah KSPPS BMT Barokatul Adzkia dalam melayani anggota.</p>
          <a class="more" href="visi-misi.html">Selengkapnya</a>
        </div>
        <div class="hub-card">
          <div class="kicker">Perjalanan Kami</div>
          <h3>Sejarah Perkembangan</h3>
          <p>Linimasa perjalanan KSPPS BMT Barokatul Adzkia sejak awal berdiri hingga saat ini.</p>
          <a class="more" href="sejarah.html">Selengkapnya</a>
        </div>
        <div class="hub-card">
          <div class="kicker">Jaringan Kantor</div>
          <h3>Kantor Cabang</h3>
          <p>Daftar dan lokasi kantor pusat, kantor cabang, dan kantor kas kami.</p>
          <a class="more" href="kantor-cabang.html">Selengkapnya</a>
        </div>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# TENTANG KAMI
# ---------------------------------------------------------------------------
tentang_body = f"""
{crumb([("Beranda","index.html"),("Profil Koperasi","profil.html"),("Tentang Kami",None)])}
{page_head_block("Tentang Kami", "Profil singkat, alamat, dan kontak resmi KSPPS BMT Barokatul Adzkia.")}
  <section>
    <div class="wrap">
      <div class="about-grid">
        <div class="about-figure">
          <h4>Nama Lembaga</h4>
          <p>KSPPS BMT Barokatul Adzkia Kebumen</p>
          <h4>Alamat Kantor</h4>
          <p>Jl. Raya Kambalan, RT 02 RW 04, Kembangsawit, Kec. Ambal, Kab. Kebumen, Prov. Jawa Tengah</p>
          <h4>Kontak</h4>
          <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div>
          <p>KSPPS BMT Barokatul Adzkia Kebumen berawal dari 40 anggota Ikatan Cendekiawan Muslim Indonesia (ICMI) yang mendirikan BMT di Kambalan, Ambal, pada 1997. Tokoh pendirinya adalah K.H. Mudhofir, B.A. Tujuan awalnya adalah memudahkan anggota dan menjauhkan mereka dari rentenir.</p>
          <p>Modal awal dikumpulkan dari simpanan wajib Rp2.500 pada tahun pertama, sebelum lembaga berbadan hukum. BMT bertumbuh dari Rp500 ribu hingga kini memiliki aset sekitar Rp23 miliar.</p>
          <p>Seiring berjalannya regulasi, lembaga ini berubah dari Kopontren menjadi BMT Barokatul Adzkia, KSPPS DAMBA, dan kini KSPPS BMT Barokatul Adzkia Kebumen yang beroperasi di tingkat kabupaten. Perjalanan lengkapnya ada di halaman <a href="sejarah.html" style="color:var(--blue);font-weight:600">Sejarah</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="alt-bg">
    <div class="wrap">
      <div class="section-head">
        <div class="kicker">Makna Nama</div>
        <h2>Arti nama kami</h2>
      </div>
      <div class="why-grid">
        <div class="why-card"><h3>Barokatul Adzkia</h3><p>Keberkahan orang-orang pandai, merujuk pada latar belakang pendirinya dari ICMI.</p></div>
        <div class="why-card"><h3>DAMBA</h3><p>Singkatan dari Darul Amwal.</p></div>
        <div class="why-card"><h3>BMT</h3><p>Singkatan dari Baitul Maal wat Tamwil. Baitul berarti rumah.</p></div>
      </div>
      <p style="margin:34px 0 18px;color:var(--ink-soft)">Secara umum, sebuah BMT memiliki dua fungsi:</p>
      <div class="vm-grid">
        <div class="vm-card">
          <h3>Maal (fungsi sosial)</h3>
          <ul>
            <li>Berfokus pada pengumpulan dan penyaluran dana sosial.</li>
            <li>Mengelola ZIS (zakat, infak, sedekah), dana wakaf, serta pinjaman kebajikan (qardh) untuk masyarakat kelas menengah ke bawah atau fakir miskin.</li>
          </ul>
        </div>
        <div class="vm-card">
          <h3>Tamwil (fungsi bisnis)</h3>
          <ul>
            <li>Berfokus pada pengembangan usaha-usaha produktif.</li>
            <li>Menggalang dana dari masyarakat dalam bentuk simpanan atau tabungan.</li>
            <li>Menyalurkan pembiayaan kepada pelaku UMKM dengan akad syariah seperti bagi hasil (mudharabah/musyarakah), jual beli (murabahah), atau sewa (ijarah).</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="pengurus-band">
    <div class="wrap">
      <div class="section-head">
        <div class="kicker">Struktur Kami</div>
        <h2>Pengurus dan Pengawas</h2>
        <p>Jajaran pengurus dan pengawas KSPPS BMT Barokatul Adzkia yang mengelola dan mengawasi jalannya koperasi.</p>
      </div>
      <img src="assets/pengurus-bmt.png" alt="Pengurus dan pengawas KSPPS BMT Barokatul Adzkia">
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# LEGALITAS
# ---------------------------------------------------------------------------
legalitas_body = f"""
{crumb([("Beranda","index.html"),("Profil Koperasi","profil.html"),("Legalitas",None)])}
{page_head_block("Legalitas", "Data badan hukum dan penghargaan KSPPS BMT Barokatul Adzkia.")}
  <section>
    <div class="wrap">
      <div class="info-note"><span>🔎</span><span>KSPPS BMT Barokatul Adzkia dapat diverifikasi lewat portal resmi Kementerian Koperasi: <strong>nik.depkop.go.id</strong>. Kalau sudah punya tautan verifikasi langsung ke data koperasi ini, kirimkan agar dipasang sebagai tautan langsung di halaman ini.</span></div>

      <div class="section-head" style="margin-bottom:18px">
        <div class="kicker">Profil / Badan Hukum</div>
        <h2>Data Badan Hukum</h2>
        <p>Baris bertanda <em>italic</em> berarti data belum diisi — mohon dilengkapi oleh manajer.</p>
      </div>
      <table class="legal-table">
        <tr><th>Nama Badan Usaha</th><td>BMT Barokatul Adzkia Kebumen</td></tr>
        <tr><th>Jenis Usaha</th><td>Koperasi Simpan Pinjam Syariah</td></tr>
        <tr><th>Tanggal Berdiri</th><td>16 Januari 1997 (1417 H)</td></tr>
        <tr><th>No. Badan Hukum</th><td>AHU-0000307.AH.01.38 Tahun 2023</td></tr>
        <tr><th>Akta Badan Hukum (1998)</th><td>No. 13619/BH/KWK.11/III/1998</td></tr>
        <tr><th>No. PAD</th><td>518.08/13619/PAD/BH/XIV.12/III/2016</td></tr>
        <tr><th>No. Izin Usaha Simpan Pinjam (USP)</th><td>0220008761374</td></tr>
        <tr><th>No. Induk Koperasi</th><td>3305070150008</td></tr>
        <tr><th>No. NPWP</th><td>1.627.714.7.523</td></tr>
        <tr><th>Akte Notaris</th><td class="field-empty">Belum diisi</td></tr>
      </table>
    </div>
  </section>

  <section class="alt-bg" id="penghargaan">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:22px">
        <div class="kicker">Penghargaan</div>
        <h2>Piagam penghargaan</h2>
        <p>Penghargaan yang pernah diterima dari Pemerintah Kabupaten Kebumen dalam rangka peringatan Hari Koperasi. Klik gambar untuk melihat ukuran penuh.</p>
      </div>
      <div class="award-grid">
        <a class="award-card" href="assets/penghargaan/penghargaan-2017.jpg" target="_blank" rel="noopener">
          <img src="assets/penghargaan/penghargaan-2017.jpg" alt="Piagam penghargaan Koperasi Berprestasi Peringkat III, Hari Koperasi ke-70 Tahun 2017" loading="lazy">
          <div class="award-body">
            <span class="award-year">2017</span>
            <h3>Koperasi Berprestasi Peringkat III</h3>
            <p>Diberikan dalam rangka Hari Koperasi ke-70 oleh Panitia Hari Koperasi Kabupaten Kebumen.</p>
          </div>
        </a>
        <a class="award-card" href="assets/penghargaan/penghargaan-2016.jpg" target="_blank" rel="noopener">
          <img src="assets/penghargaan/penghargaan-2016.jpg" alt="Piagam penghargaan Koperasi Berprestasi Harapan II, Hari Koperasi ke-69 Tahun 2016" loading="lazy">
          <div class="award-body">
            <span class="award-year">2016</span>
            <h3>Koperasi Berprestasi Harapan II</h3>
            <p>Diberikan dalam rangka Hari Koperasi ke-69 oleh Panitia Hari Koperasi Kabupaten Kebumen.</p>
          </div>
        </a>
        <a class="award-card" href="assets/penghargaan/penghargaan-2014.jpg" target="_blank" rel="noopener">
          <img src="assets/penghargaan/penghargaan-2014.jpg" alt="Piagam penghargaan Koperasi Berprestasi Jenis Koperasi Syariah Peringkat III, Hari Koperasi ke-67 Tahun 2014" loading="lazy">
          <div class="award-body">
            <span class="award-year">2014</span>
            <h3>Koperasi Berprestasi Jenis Koperasi Syariah, Peringkat III</h3>
            <p>Diberikan dalam rangka Hari Koperasi ke-67 oleh Panitia Hari Koperasi Kabupaten Kebumen.</p>
          </div>
        </a>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# VISI MISI
# ---------------------------------------------------------------------------
visimisi_body = f"""
{crumb([("Beranda","index.html"),("Profil Koperasi","profil.html"),("Visi & Misi",None)])}
{page_head_block("Visi & Misi", "Motto, visi, dan misi yang menjadi pedoman arah KSPPS BMT Barokatul Adzkia.")}
  <section>
    <div class="wrap">
      <div class="motto-block">
        <span>Motto Kami</span>
        <h2>&ldquo;Menuai Berkah dengan Syariah&rdquo;</h2>
      </div>
      <div class="section-head" style="margin-bottom:18px">
        <div class="kicker">Arah Lembaga</div>
        <h2>Visi &amp; Misi</h2>
      </div>
      <div class="vm-grid">
        <div class="vm-card">
          <h3>Visi</h3>
          <p>Menjadikan KSPPS BMT Barokatul Adzkia Kebumen sebagai lembaga keuangan syariah yang amanah, profesional, mandiri, serta bermanfaat bagi umat.</p>
        </div>
        <div class="vm-card">
          <h3>Misi</h3>
          <ul>
            <li>Menyelenggarakan pelayanan kepada anggota sesuai jati diri koperasi.</li>
            <li>Menjalankan kegiatan usaha dengan efektif, efisien, dan transparan.</li>
            <li>Menjalin kerjasama usaha dengan berbagai pihak.</li>
            <li>Mengelola koperasi dan unit usaha secara profesional.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# SEJARAH
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# TOKOH PENDIRI
# Muncul otomatis kalau fotonya ada di assets/pendiri/ dengan nama mudhofir.*
# (boleh .jpg, .jpeg, .png, atau .webp). Kalau belum ada, bagian ini dilewati.
# ---------------------------------------------------------------------------
FOUNDER_NAME = "K.H. Mudhofir, B.A."   # ganti di sini kalau nama perlu dikoreksi
FOUNDER_DESC = ("Sosok visioner yang menjadi pelopor berdirinya KSPPS BMT Barokatul Adzkia Kebumen, "
                "dengan semangat kebersamaan dan kepedulian terhadap umat, beliau telah meletakkan "
                "dasar yang kuat bagi kemajuan koperasi ini hingga hari ini.")
FOUNDER_META = "Berdiri 16 Januari 1997 &middot; Kambalan, Ambal, Kebumen"
FOUNDER_QUOTE = "Bersama membangun ekonomi umat menuju kesejahteraan bersama."

_founder_files = []
for _name in ("tokoh-pendiri", "mudhofir"):   # nama file foto yang dikenali, berurutan
    _founder_files = sorted(glob.glob(os.path.join(OUT_DIR, "assets", "pendiri", _name + ".*")))
    if _founder_files:
        break
if _founder_files:
    _founder_src = "assets/pendiri/" + os.path.basename(_founder_files[0])
    FOUNDER_BLOCK = f"""  <section class="founder-section" id="pendiri">
    <div class="wrap">
      <div class="founder">
        <img class="founder-photo" src="{_founder_src}" alt="Foto {FOUNDER_NAME}, tokoh pendiri KSPPS BMT Barokatul Adzkia" width="720" height="864" loading="lazy">
        <div class="founder-text">
          <span class="founder-badge">Tokoh Pendiri</span>
          <h2 class="founder-name">{FOUNDER_NAME}</h2>
          <div class="founder-rule" aria-hidden="true"><i></i></div>
          <p class="founder-desc">{FOUNDER_DESC}</p>
          <p class="founder-meta">{FOUNDER_META}</p>
          <blockquote class="founder-quote">
            <span class="qm" aria-hidden="true">&ldquo;</span>
            <p>{FOUNDER_QUOTE}</p>
          </blockquote>
        </div>
      </div>
    </div>
  </section>
"""
else:
    FOUNDER_BLOCK = ""
    print("CATATAN: foto pendiri belum ada di assets/pendiri/ (nama file: tokoh-pendiri.jpg). Bagian 'Tokoh pendiri' dilewati.")

sejarah_body = f"""
{crumb([("Beranda","index.html"),("Profil Koperasi","profil.html"),("Sejarah",None)])}
{page_head_block("Sejarah Perkembangan", "Linimasa perjalanan KSPPS BMT Barokatul Adzkia sejak awal berdiri hingga saat ini.")}
{FOUNDER_BLOCK}  <section>
    <div class="wrap">
      <div class="timeline">
        <div class="tl-item">
          <b>16 Januari 1997 (1417 H)</b>
          <h3>BMT berdiri di Kambalan</h3>
          <p>Didirikan oleh 40 anggota ICMI. Modal awal dari simpanan wajib Rp2.500 pada tahun pertama. Usaha pertamanya simpan pinjam syariah dan warung serba ada.</p>
        </div>
        <div class="tl-item">
          <b>1998</b>
          <h3>Berbadan hukum</h3>
          <p>Akta Badan Hukum No. 13619/BH/KWK.11/III/1998.</p>
        </div>
        <div class="tl-item">
          <b>2000</b>
          <h3>Berdiri kantor dan Gedung Rapat Anggota</h3>
          <p>BMT mendirikan kantor beserta Gedung Rapat Anggota (RA) yang dikelola oleh BMT.</p>
        </div>
        <div class="tl-item">
          <b>2003</b>
          <h3>Gedung baru</h3>
          <p>BMT menempati gedung baru bernilai sekitar Rp1 miliar.</p>
        </div>
        <div class="tl-item">
          <b>Seiring waktu</b>
          <h3>Perubahan bentuk dan nama</h3>
          <p>Berawal dari Kopontren (koperasi pondok pesantren) yang mengikuti pusat Cilacap, lalu dibina Kopsyah Cilacap dan Dinas Koperasi. Seiring regulasi, lembaga ini menjadi BMT Barokatul Adzkia, KSPPS DAMBA, dan kini KSPPS BMT Barokatul Adzkia Kebumen yang beroperasi di tingkat kabupaten. Karena regulasi KSPPS, usaha warung serba ada tidak dilanjutkan.</p>
        </div>
        <div class="tl-item">
          <b>2016</b>
          <h3>Perubahan Anggaran Dasar</h3>
          <p>Perubahan Anggaran Dasar (PAD) tahun 2016.</p>
        </div>
        <div class="tl-item">
          <b>Saat ini</b>
          <h3>Aset sekitar Rp23 miliar</h3>
          <p>BMT memiliki kantor pusat, satu kantor cabang, dan tiga kantor kas, dengan aset sekitar Rp23 miliar.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="alt-bg">
    <div class="wrap">
      <div class="section-head">
        <div class="kicker">Dari Masa ke Masa</div>
        <h2>Pengurus dan manajer</h2>
      </div>
      <div class="vm-grid">
        <div class="vm-card">
          <h3>Pengurus</h3>
          <ul>
            <li>Muhammad Danuri (ketua pertama)</li>
            <li>Drs. Ashar Muhamadi, M.Ag.</li>
            <li>Azizil Karim</li>
            <li>Bambang Sudiyono, B.Sc</li>
            <li>Wiyono, M.M.Pd</li>
          </ul>
        </div>
        <div class="vm-card">
          <h3>Manajer</h3>
          <ul>
            <li>Nurul Hadi (manajer pertama)</li>
            <li>Drs. Samidi</li>
            <li>Teguh Hari Yulianto</li>
            <li>Masfud Alfatoni, S.H.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# KANTOR CABANG
# ---------------------------------------------------------------------------
kantor_body = f"""
{crumb([("Beranda","index.html"),("Profil Koperasi","profil.html"),("Kantor Cabang",None)])}
{page_head_block("Jaringan Kantor", "Daftar dan lokasi kantor pusat, kantor cabang, dan kantor kas kami.")}
  <section id="tabel">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px">
        <div class="kicker">Tabel Kantor Cabang</div>
        <h2>Kantor kami</h2>
      </div>
      <table class="branch-table">
        <thead><tr><th>Kantor</th><th>Alamat</th><th>Telepon / Jam</th></tr></thead>
        <tbody>
          <tr>
            <td>Kantor Pusat</td>
            <td>Jl. Raya Kambalan, RT 02 RW 04, Kembangsawit, Kec. Ambal, Kab. Kebumen, Prov. Jawa Tengah</td>
            <td>+62 851-9960-3106<br>Senin–Jumat 08.00–15.00, Sabtu 08.00–12.00</td>
          </tr>
          <tr>
            <td>Kantor Cabang</td>
            <td>Jl. Pasar Kejawang No. 7, RT 01 RW 05, Tanggeran, Kec. Sruweng, Kab. Kebumen, Prov. Jawa Tengah</td>
            <td>+62 852-2840-0732<br>Senin–Jumat 08.00–15.00, Sabtu 08.00–12.00</td>
          </tr>
          <tr>
            <td>Kantor Kas 1</td>
            <td>Pasar Kutowinangun, Jl. Dwikora, Kutowinangun, Kec. Kutowinangun, Kab. Kebumen, Prov. Jawa Tengah</td>
            <td>Senin–Jumat 08.00–15.00, Sabtu 08.00–12.00</td>
          </tr>
          <tr>
            <td>Kantor Kas 2</td>
            <td>Jl. Raya Prembun, Desa Kabekelan, Kec. Prembun, Kab. Kebumen, Prov. Jawa Tengah</td>
            <td>Senin–Jumat 08.00–15.00, Sabtu 08.00–12.00</td>
          </tr>
          <tr>
            <td>Kantor Kas 3</td>
            <td>Jl. Raya Kambalan, RT 01 RW 04, Kembangsawit, Kec. Ambal, Kab. Kebumen, Prov. Jawa Tengah</td>
            <td>Senin–Jumat 08.00–15.00, Sabtu 08.00–12.00</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="alt-bg" id="maps">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px">
        <div class="kicker">Lokasi</div>
        <h2>Lokasi Kantor (Maps)</h2>
      </div>
      <div class="map-embed">
        <iframe title="Lokasi Kantor Pusat KSPPS BMT Barokatul Adzkia" loading="lazy"
          src="https://www.google.com/maps?q=Kembangsawit,+Ambal,+Kebumen&output=embed"></iframe>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# PRODUK
# ---------------------------------------------------------------------------
produk_body = f"""
{crumb([("Beranda","index.html"),("Produk Kami",None)])}
{page_head_block("Produk Kami", "Simpanan dan pembiayaan syariah untuk kebutuhan anggota KSPPS BMT Barokatul Adzkia.")}
  <section>
    <div class="wrap">
      <div class="product-tabs" role="tablist">
        <button class="tab-btn active" data-target="panel-simpanan" role="tab" aria-selected="true">Simpanan Anggota</button>
        <button class="tab-btn" data-target="panel-pembiayaan" role="tab" aria-selected="false">Pembiayaan Anggota</button>
      </div>

      <div class="product-panel active" id="panel-simpanan">
        <div class="product-card" id="si-rela">
          <h3>Si Rela <span style="font-weight:400;color:var(--ink-soft)">(Simpanan Sukarela)</span></h3>
          <p>Simpanan lancar yang dapat disetorkan dan diambil sewaktu-waktu.</p>
          <ul>
            <li>Setoran awal Rp10.000, selanjutnya minimal Rp5.000</li>
            <li>Mendapatkan bagi hasil setiap bulan</li>
            <li>Tanpa potongan administrasi</li>
          </ul>
        </div>
        <div class="product-card" id="si-pendi">
          <h3>Si Pendi <span style="font-weight:400;color:var(--ink-soft)">(Simpanan Pendidikan)</span></h3>
          <p>Diperuntukkan untuk kebutuhan biaya pendidikan pelajar dan mahasiswa.</p>
          <ul><li>Setoran awal Rp10.000, selanjutnya minimal Rp5.000</li></ul>
        </div>
        <div class="product-card" id="si-suqur">
          <h3>Si Suqur <span style="font-weight:400;color:var(--ink-soft)">(Simpanan Ahli Qurban/Aqiqah)</span></h3>
          <p>Diperuntukkan untuk kebutuhan Qurban atau Aqiqah.</p>
          <ul><li>Setoran awal Rp10.000, selanjutnya minimal Rp5.000</li></ul>
        </div>
        <div class="product-card" id="si-fitri">
          <h3>Si Fitri <span style="font-weight:400;color:var(--ink-soft)">(Simpanan Idul Fitri)</span></h3>
          <p>Dipersiapkan untuk kebutuhan menyambut Hari Raya Idul Fitri.</p>
          <ul><li>Setoran awal Rp10.000, selanjutnya minimal Rp5.000</li></ul>
        </div>
        <div class="product-card" id="si-simka">
          <h3>Si Simka <span style="font-weight:400;color:var(--ink-soft)">(Simpanan Mudharabah Berjangka)</span></h3>
          <p>Simpanan berjangka (3, 6, atau 12 bulan) yang hanya dapat diambil saat jatuh tempo.</p>
          <ul>
            <li>Setoran minimal Rp1.000.000</li>
            <li>Bagi hasil menarik sesuai nisbah, akad Mudharabah</li>
            <li>Dapat dijadikan jaminan pembiayaan</li>
          </ul>
        </div>
        <div class="product-card" id="simpanan-haji">
          <h3>Simpanan Haji / Umroh</h3>
          <p>Untuk kebutuhan menjelang keberangkatan haji atau umroh.</p>
          <ul><li>Setoran awal Rp10.000, selanjutnya minimal Rp5.000</li></ul>
        </div>
      </div>

      <div class="product-panel" id="panel-pembiayaan">
        <div class="product-card" id="modal-kerja">
          <h3>Pembiayaan Modal Kerja</h3>
          <p>Bagi Anda yang sudah memiliki usaha berjalan minimal 2 tahun — untuk kebutuhan modal saat mendapat proyek dengan SPK/PO, menjelang Lebaran, atau kebutuhan permodalan lain.</p>
        </div>
        <div class="product-card" id="investasi">
          <h3>Pembiayaan Investasi</h3>
          <p>Untuk keperluan investasi seperti pembelian kendaraan penunjang usaha, mesin produksi, tanah/bangunan, atau investasi lain yang menunjang usaha Anda.</p>
        </div>
        <div class="product-card" id="konsumtif">
          <h3>Pembiayaan Konsumtif</h3>
          <p>Untuk berbagai kebutuhan, mulai dari barang elektronik sampai renovasi tempat tinggal, insya Allah kami siap membantu.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="alt-bg" id="keanggotaan">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px">
        <div class="kicker">Keanggotaan</div>
        <h2>Menjadi anggota</h2>
      </div>
      <div class="syarat-card">
        <h3>Berkas yang dibawa</h3>
        <ol class="syarat-list">
          <li>Fotokopi KTP pemohon</li>
          <li>Fotokopi Kartu Keluarga (KK)</li>
          <li>Untuk pendaftar yang di bawah umur wajib mendaftarkan atas nama orang tua. Sertakan fotokopi KK yang memuat nama anak, serta fotokopi KIA atau akta kelahiran anak</li>
        </ol>
        <h3 style="margin-top:22px">Simpanan keanggotaan</h3>
        <ol class="syarat-list">
          <li>Simpanan Pokok Rp20.000</li>
          <li>Simpanan Wajib minimal Rp150.000, atau Rp2.000 per bulan</li>
          <li>Setoran awal produk simpanan sesuai pilihan Anda (lihat daftar produk di atas)</li>
        </ol>
        <h3 style="margin-top:22px">Cara mendaftar</h3>
        <ol class="syarat-list">
          <li>Unduh dan isi Formulir Permohonan Menjadi Anggota, atau isi langsung di kantor</li>
          <li>Cantumkan ahli waris pada formulir</li>
          <li>Serahkan formulir dan berkas ke kantor kami, lalu bayar simpanan pokok dan simpanan wajib</li>
        </ol>
        <p class="syarat-note">Formulir tersedia di halaman <a href="download.html#form-simpanan">Download</a>.</p>
        <a class="cc-btn solid" href="{WA_LINK_KANTOR}" target="_blank" rel="noopener">Tanyakan cara mendaftar</a>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# KENAPA KAMI
# ---------------------------------------------------------------------------
kenapa_body = f"""
{crumb([("Beranda","index.html"),("Kenapa Memilih Kami",None)])}
{page_head_block("Kenapa Memilih Kami", "Nilai-nilai yang kami pegang dalam melayani anggota.")}
  <section>
    <div class="wrap">
      <div class="why-grid">
        <div class="why-card"><h3>Sesuai prinsip syariah</h3><p>Seluruh produk simpanan dan pembiayaan dijalankan berdasarkan akad syariah.</p></div>
        <div class="why-card"><h3>Dekat dengan anggota</h3><p>Melayani langsung masyarakat di wilayah Ambal, Kebumen dan sekitarnya.</p></div>
        <div class="why-card"><h3>Pelayanan profesional</h3><p>Dikelola secara efektif, efisien, dan transparan sesuai jati diri koperasi.</p></div>
        <div class="why-card"><h3>Kerjasama terpercaya</h3><p>Menjalin kerjasama usaha dengan berbagai pihak demi manfaat bersama.</p></div>
        <div class="why-card"><h3>Berbasis kekeluargaan</h3><p>Mengedepankan nilai gotong royong dan kepercayaan antaranggota.</p></div>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# GALLERY
# ---------------------------------------------------------------------------
gallery_body = f"""
{crumb([("Beranda","index.html"),("Gallery",None)])}
{page_head_block("Gallery", "Dokumentasi foto kegiatan dan video KSPPS BMT Barokatul Adzkia.")}
  <section id="foto">
    <div class="wrap">
      <div class="info-note"><span>ℹ️</span><span>Bagian ini masih placeholder — nanti diisi foto kegiatan asli dari kantor.</span></div>
      <div class="section-head" style="margin-bottom:18px"><div class="kicker">Dokumentasi</div><h2>Foto Kegiatan</h2></div>
      <div class="gal-grid">
        <div class="gal-item">Foto kegiatan 1<br>belum diunggah</div>
        <div class="gal-item">Foto kegiatan 2<br>belum diunggah</div>
        <div class="gal-item">Foto kegiatan 3<br>belum diunggah</div>
        <div class="gal-item">Foto kegiatan 4<br>belum diunggah</div>
        <div class="gal-item">Foto kegiatan 5<br>belum diunggah</div>
        <div class="gal-item">Foto kegiatan 6<br>belum diunggah</div>
      </div>
    </div>
  </section>
  <section class="alt-bg" id="video">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px"><div class="kicker">Dokumentasi</div><h2>Video Dokumentasi</h2></div>
      <div class="gal-grid">
        <div class="gal-item">Video dokumentasi<br>belum diunggah</div>
      </div>
    </div>
  </section>
"""

# ---------------------------------------------------------------------------
# DOWNLOAD
# ---------------------------------------------------------------------------
def _dl_item(name, filename, kind):
    """Satu baris unduhan. Kalau file ada di assets/download/, tombol jadi tautan unduh;
    kalau belum ada, tampil 'Belum tersedia'. Tambah file baru cukup dengan menaruhnya di folder itu."""
    path = os.path.join(OUT_DIR, "assets", "download", filename)
    if os.path.exists(path):
        kb = os.path.getsize(path) / 1024
        size = f"{kb/1024:.1f} MB" if kb >= 1024 else f"{kb:.0f} KB"
        return (f'<div class="dl-item"><div><div class="dl-name">{name}</div>'
                f'<div class="dl-desc">{kind} &middot; {size}</div></div>'
                f'<a class="dl-btn" href="assets/download/{filename}" download>Unduh</a></div>')
    return (f'<div class="dl-item"><div><div class="dl-name">{name}</div>'
            f'<div class="dl-desc field-empty">Belum diunggah</div></div>'
            f'<span class="dl-btn dl-off">Segera hadir</span></div>')

SYARAT_PEMBIAYAAN = [
    "Fotokopi KTP pemohon",
    "Fotokopi KTP pihak ke-2",
    "Fotokopi Kartu Keluarga (KK)",
    "Fotokopi jaminan: BPKB + STNK, atau Sertifikat + SPPT",
    "Fotokopi surat nikah",
    "Daftar sumber penghasilan (slip gaji / data usaha)",
]
_syarat_li = "\n".join(f"          <li>{s}</li>" for s in SYARAT_PEMBIAYAAN)

download_body = f"""
{crumb([("Beranda","index.html"),("Download",None)])}
{page_head_block("Download", "Brosur produk, formulir simpanan dan pembiayaan, serta syarat pengajuan.")}
  <section id="brosur">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px"><div class="kicker">Unduhan</div><h2>Brosur Produk</h2></div>
      <div class="dl-list">
        {_dl_item("Brosur Produk Simpanan", "brosur-simpanan.jpg", "Gambar JPG")}
        {_dl_item("Brosur Produk Pembiayaan", "brosur-pembiayaan.jpg", "Gambar JPG")}
      </div>
    </div>
  </section>
  <section class="alt-bg" id="form-simpanan">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px"><div class="kicker">Formulir</div><h2>Formulir Simpanan &amp; Keanggotaan</h2></div>
      <div class="dl-list">
        {_dl_item("Formulir Permohonan Menjadi Anggota", "formulir-permohonan-simpanan.docx", "Dokumen Word")}
        {_dl_item("Pembukaan Rekening Simpanan (Lembar 2)", "pembukaan-simpanan-lembar-2.docx", "Dokumen Word")}
        {_dl_item("Data Pribadi Nasabah (Lembar 3)", "pembukaan-simpanan-lembar-3.docx", "Dokumen Word")}
        {_dl_item("Akad Simpanan Wadiah", "akad-simpanan-wadiah.docx", "Dokumen Word")}
      </div>
    </div>
  </section>
  <section id="form-pembiayaan">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px"><div class="kicker">Formulir</div><h2>Formulir Pembiayaan</h2></div>
      <div class="dl-list">
        {_dl_item("Formulir Permohonan Pembiayaan", "formulir-pembiayaan.doc", "Dokumen Word")}
        {_dl_item("Surat Pernyataan Keluarga", "surat-pernyataan-keluarga.doc", "Dokumen Word")}
        {_dl_item("Surat Pernyataan Jaminan", "pernyataan-jaminan.docx", "Dokumen Word")}
      </div>
    </div>
  </section>
  <section class="alt-bg" id="syarat">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:18px"><div class="kicker">Ketentuan</div><h2>Syarat Pengajuan</h2></div>
      <div class="syarat-card">
        <h3>Pembiayaan</h3>
        <ol class="syarat-list">
{_syarat_li}
        </ol>
        <p class="syarat-note">Siapkan berkas di atas lalu serahkan ke kantor kami. Untuk pertanyaan, hubungi kami lewat WhatsApp atau telepon.</p>
        <a class="cc-btn solid" href="{WA_LINK_KANTOR}" target="_blank" rel="noopener">Tanya via WhatsApp</a>
      </div>
    </div>
  </section>
"""

PAGES = [
    ("index.html", "KSPPS BMT Barokatul Adzkia Kebumen", "KSPPS BMT Barokatul Adzkia - Koperasi Simpan Pinjam Pembiayaan Syariah di Ambal, Kebumen. Amanah, Profesional, Mandiri.", "beranda", index_body),
    ("profil.html", "Profil Koperasi", "Profil, Visi Misi, Legalitas, dan Sejarah KSPPS BMT Barokatul Adzkia.", "profil", profil_body),
    ("tentang-kami.html", "Tentang Kami", "Tentang KSPPS BMT Barokatul Adzkia Kebumen.", "profil", tentang_body),
    ("legalitas.html", "Legalitas", "Legalitas, badan hukum, dan izin usaha KSPPS BMT Barokatul Adzkia.", "profil", legalitas_body),
    ("visi-misi.html", "Visi & Misi", "Visi, Misi, dan Motto KSPPS BMT Barokatul Adzkia.", "profil", visimisi_body),
    ("sejarah.html", "Sejarah", "Sejarah dan perjalanan KSPPS BMT Barokatul Adzkia.", "profil", sejarah_body),
    ("kantor-cabang.html", "Kantor Cabang", "Daftar dan lokasi kantor cabang KSPPS BMT Barokatul Adzkia.", "profil", kantor_body),
    ("produk.html", "Produk Kami", "Produk Simpanan dan Pembiayaan Syariah KSPPS BMT Barokatul Adzkia.", "produk", produk_body),
    ("kenapa-kami.html", "Kenapa Memilih Kami", "Alasan memilih KSPPS BMT Barokatul Adzkia.", "kenapa", kenapa_body),
    ("gallery.html", "Gallery", "Dokumentasi foto dan video KSPPS BMT Barokatul Adzkia.", "gallery", gallery_body),
    ("download.html", "Download", "Unduh brosur, formulir, dan syarat pengajuan KSPPS BMT Barokatul Adzkia.", "download", download_body),
]

for filename, title, desc, active, body in PAGES:
    html = page(title, desc, active, body)
    with open(os.path.join(OUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)