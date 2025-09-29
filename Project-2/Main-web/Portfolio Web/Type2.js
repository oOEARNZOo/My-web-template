// ===== Dark Mode: โหลดค่าจากระบบ/ที่บันทึกไว้ + toggle =====
(function initTheme() {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const saved = localStorage.getItem('theme');
  const dark = saved ? saved === 'dark' : prefersDark;

  const apply = (isDark) => {
    document.body.classList.toggle('dark-mode', isDark);
    document.querySelector('header')?.classList.toggle('dark-mode', isDark);
  };

  const run = () => {
    const toggle = document.getElementById('toggle-dark');
    
    apply(dark);
    if (toggle) {
      toggle.addEventListener('click', function () {
        const newTheme = !document.body.classList.contains('dark-mode');
        apply(newTheme);
        localStorage.setItem('theme', newTheme ? 'dark' : 'light');
      });
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();

// ===== Active nav on scroll =====
(function initActiveNav() {
  const run = () => {
    const navLinks = Array.from(document.querySelectorAll('.navmenu a'))
      .filter(a => a.getAttribute('href')?.startsWith('#'));

    const sections = navLinks
      .map(a => document.querySelector(a.getAttribute('href')))
      .filter(Boolean);

    const setActive = (id) => {
      navLinks.forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
      });
    };

    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    }, { root: null, rootMargin: '-35% 0px -35% 0px', threshold: 0.01 });

    sections.forEach(sec => io.observe(sec));

    // กดลิงก์แล้วให้ active ทันที
    navLinks.forEach(a => {
      a.addEventListener('click', () => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) setActive(target.id);
      });
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
