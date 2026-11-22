document.addEventListener('DOMContentLoaded', function () {
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

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