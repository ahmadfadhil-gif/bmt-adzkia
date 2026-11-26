document.addEventListener('DOMContentLoaded', function () {
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Pastikan logo di bar menu (HP) dan tombol WhatsApp ada, walau HTML-nya versi lama
  var navInner = document.querySelector('.nav-inner');
  if (navInner && !navInner.querySelector('.nav-brand')) {
    var nb = document.createElement('a');
    nb.className = 'nav-brand'; nb.href = 'index.html';
    nb.innerHTML = '<img src="assets/logo-icon.png" alt=""><span>KSPPS BMT Barokatul Adzkia</span>';
    navInner.insertBefore(nb, navInner.firstChild);
  }
  if (!document.querySelector('.wa-float')) {
    var wl = document.querySelector('a[href^="https://wa.me/"]');
    var wa = document.createElement('a');
    wa.className = 'wa-float'; wa.target = '_blank'; wa.rel = 'noopener';
    wa.href = wl ? wl.href : 'https://wa.me/6285878755748';
    wa.setAttribute('aria-label', 'Chat WhatsApp');
    wa.innerHTML = '<svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.43 15.1L2 22l5.05-1.32A9.93 9.93 0 1 0 12.04 2zm0 1.8a8.13 8.13 0 1 1-4.15 15.14l-.3-.18-3 .78.8-2.92-.2-.3A8.13 8.13 0 0 1 12.04 3.8zM8.6 7.5c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.06 3.3 5.1 4.5 2.52 1 3.03.8 3.57.75.55-.05 1.76-.72 2-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35s-1.76-.87-2.03-.97c-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57z"/></svg>';
    document.body.appendChild(wa);
  }

  // Menu seluler
  var toggle = document.getElementById('navToggle');
  var navList = document.getElementById('navList');
  if (toggle && navList) {
    var navEl = toggle.closest('nav');
    var setMenu = function (isOpen) {
      navList.classList.toggle('open', isOpen);
      if (navEl) navEl.classList.toggle('menu-open', isOpen);
      toggle.setAttribute('aria-expanded', isOpen);
    };
    toggle.addEventListener('click', function () {
      setMenu(!navList.classList.contains('open'));
    });
    // Ketuk menu tujuan (bukan induk submenu) -> tutup menu.
    // Penting untuk link ke bagian di halaman yang sama (mis. produk.html#si-rela),
    // karena halaman tidak dimuat ulang dan menu akan tetap menutupi isi.
    navList.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        if (window.innerWidth <= 860 && !a.parentElement.querySelector(':scope > .submenu')) {
          setMenu(false);
        }
      });
    });
  }

  // Submenu seluler (mendukung dua tingkat)
  document.querySelectorAll('.nav-list li').forEach(function (li) {
    var link = li.querySelector(':scope > a');
    var submenu = li.querySelector(':scope > .submenu');
    if (submenu && link) {
      link.addEventListener('click', function (e) {
        if (window.innerWidth <= 860) {
          e.preventDefault();
          e.stopPropagation();
          li.classList.toggle('open');
        }
      });
    }
  });

  // Slider hero beranda
  var slides = document.querySelectorAll('.hero-slide');
  if (slides.length) {
    var current = 0;
    setInterval(function () {
      slides[current].classList.remove('active');
      current = (current + 1) % slides.length;
      slides[current].classList.add('active');
    }, 4500);
  }

  // Tab produk (simpanan / pembiayaan)
  var tabButtons = document.querySelectorAll('.tab-btn');
  if (tabButtons.length) {
    tabButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        tabButtons.forEach(function (b) { b.classList.remove('active'); });
        document.querySelectorAll('.product-panel').forEach(function (p) { p.classList.remove('active'); });
        btn.classList.add('active');
        var panel = document.getElementById(btn.dataset.target);
        if (panel) panel.classList.add('active');
      });
    });
  }

  // Buka tab yang sesuai dengan tautan (#hash) lalu gulir ke tujuannya
  function openFromHash() {
    if (!tabButtons.length || !location.hash) return;
    var id = decodeURIComponent(location.hash.slice(1));
    var alias = { simpanan: 'panel-simpanan', pembiayaan: 'panel-pembiayaan' };
    if (alias[id]) id = alias[id];
    var target = document.getElementById(id);
    if (!target) return;
    var panel = target.classList.contains('product-panel') ? target : target.closest('.product-panel');
    if (panel) {
      document.querySelectorAll('.product-panel').forEach(function (p) { p.classList.remove('active'); });
      panel.classList.add('active');
      tabButtons.forEach(function (b) {
        var on = b.dataset.target === panel.id;
        b.classList.toggle('active', on);
        b.setAttribute('aria-selected', on ? 'true' : 'false');
      });
    }
    setTimeout(function () {
      var tabs = document.querySelector('.tab-btn');
      var el = (panel && target === panel && tabs) ? tabs.parentElement : target;
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 60);
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);

  // Muncul halus saat digulir
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var targets = document.querySelectorAll(
      '.section-head, .hero-slider, .product-card, .why-card, .hub-card, .vm-card, .award-card, ' +
      '.founder, .syarat-card, .dl-item, .gal-item, .about-grid > *, .branch-table, .legal-table'
    );
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    targets.forEach(function (el) {
      var idx = Array.prototype.indexOf.call(el.parentElement.children, el);
      el.style.setProperty('--d', Math.min(idx, 4) * 70 + 'ms');
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.92) { el.classList.add('in'); }   // sudah terlihat: tampil langsung
      el.classList.add('reveal');
      io.observe(el);
    });
  }

  // Pencarian sederhana di navbar
  var searchInput = document.getElementById('siteSearchInput');
  var searchBtn = document.getElementById('siteSearchBtn');
  if (searchInput && searchBtn) {
    var siteMap = [
      { url: 'index.html',         keywords: ['beranda', 'home', 'depan'] },
      { url: 'profil.html',        keywords: ['profil koperasi', 'profil'] },
      { url: 'tentang-kami.html',  keywords: ['tentang kami', 'tentang'] },
      { url: 'legalitas.html',     keywords: ['legalitas', 'badan hukum', 'npwp', 'izin usaha', 'induk koperasi'] },
      { url: 'visi-misi.html',     keywords: ['visi misi', 'visi', 'misi', 'motto'] },
      { url: 'sejarah.html',       keywords: ['sejarah', 'linimasa', 'perkembangan'] },
      { url: 'kantor-cabang.html', keywords: ['kantor cabang', 'cabang', 'kantor kas', 'lokasi', 'maps', 'alamat kantor'] },
      { url: 'produk.html',        keywords: ['produk', 'simpanan', 'pembiayaan', 'si rela', 'si pendi', 'si suqar', 'si fitri', 'si simka', 'haji', 'umroh', 'modal kerja', 'investasi', 'konsumtif', 'keanggotaan'] },
      { url: 'gallery.html',       keywords: ['gallery', 'galeri', 'foto', 'video', 'dokumentasi'] },
      { url: 'download.html',      keywords: ['download', 'unduh', 'brosur', 'formulir', 'syarat pengajuan'] },
      { url: 'kenapa-kami.html',   keywords: ['kenapa memilih kami', 'kenapa', 'alasan', 'kelebihan'] }
    ];

    var normalize = function (text) { return text.toLowerCase().trim(); };

    var findBestMatch = function (query) {
      query = normalize(query);
      if (!query) return null;
      var best = null;
      var bestScore = 0;
      siteMap.forEach(function (page) {
        var score = 0;
        page.keywords.forEach(function (kw) {
          kw = normalize(kw);
          if (query === kw) score += 10;
          else if (kw.indexOf(query) !== -1) score += 5;
          else if (query.indexOf(kw) !== -1) score += 3;
        });
        if (score > bestScore) { bestScore = score; best = page.url; }
      });
      return best;
    };

    var doSearch = function () {
      var query = searchInput.value;
      var target = findBestMatch(query);
      if (target) {
        window.location.href = target;
      } else {
        alert('Halaman untuk "' + query + '" tidak ditemukan. Coba kata kunci lain, misalnya "produk" atau "legalitas".');
      }
    };

    searchBtn.addEventListener('click', doSearch);
    searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        doSearch();
      }
    });
  }
});

// Sembunyikan lapisan loading begitu halaman selesai dimuat sepenuhnya
(function () {
  var loader = document.getElementById('pageLoader');
  if (!loader) return;

  var hideLoader = function () {
    loader.classList.add('is-hidden');
  };

  window.addEventListener('load', hideLoader);
  // Jaga-jaga kalau ada aset yang lambat/gagal dimuat, tetap hilang setelah 6 detik
  setTimeout(hideLoader, 6000);
})();