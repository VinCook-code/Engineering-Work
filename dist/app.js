(() => {
  'use strict';

  function init() {
    const page = document.documentElement;
    const body = document.body;
    if (!body) return;

    let motionQuery = null;
    try {
      motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    } catch (_) {
      // All content still works when a browser cannot expose this preference.
    }

    const motionKey = 'vincent-portfolio-motion';
    let manualReduction = false;
    try {
      manualReduction = window.localStorage.getItem(motionKey) === 'reduce';
    } catch (_) {
      // Storage can be unavailable in private or restricted browsing sessions.
    }

    const motionButton = document.querySelector('[data-motion-toggle]');
    const revealItems = Array.from(document.querySelectorAll('.reveal'));
    let revealObserver = null;
    let reducedMotion = false;

    function showReveal(item) {
      item.classList.add('is-visible');
      if (revealObserver) revealObserver.unobserve(item);
    }

    function configureReveals() {
      if (reducedMotion || !('IntersectionObserver' in window)) {
        if (revealObserver) revealObserver.disconnect();
        revealItems.forEach(showReveal);
        return;
      }
      if (!revealObserver) {
        try {
          revealObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
              if (entry.isIntersecting) showReveal(entry.target);
            });
          }, { rootMargin: '0px 0px -24px 0px', threshold: 0.06 });
        } catch (_) {
          revealItems.forEach(showReveal);
          return;
        }
      }
      revealItems.forEach((item) => {
        if (!item.classList.contains('is-visible')) revealObserver.observe(item);
      });
    }

    function updateMotion() {
      const systemReduction = Boolean(motionQuery && motionQuery.matches);
      reducedMotion = systemReduction || manualReduction;
      body.classList.toggle('reduce-motion', reducedMotion);
      if (motionButton) {
        motionButton.setAttribute('aria-pressed', String(reducedMotion));
        motionButton.disabled = systemReduction;
        motionButton.setAttribute('aria-label', systemReduction
          ? 'Animations are off because your system prefers reduced motion'
          : reducedMotion ? 'Turn animations on' : 'Turn animations off');
        const label = motionButton.querySelector('[data-motion-label]');
        if (label) label.textContent = reducedMotion ? 'Motion off' : 'Motion on';
      }
      configureReveals();
    }

    if (motionButton) {
      motionButton.addEventListener('click', () => {
        manualReduction = !manualReduction;
        try {
          window.localStorage.setItem(motionKey, manualReduction ? 'reduce' : 'default');
        } catch (_) {
          // The choice still applies to this page when it cannot be saved.
        }
        updateMotion();
      });
    }
    if (motionQuery) {
      if (typeof motionQuery.addEventListener === 'function') {
        motionQuery.addEventListener('change', updateMotion);
      } else if (typeof motionQuery.addListener === 'function') {
        motionQuery.addListener(updateMotion);
      }
    }
    updateMotion();

    const menuButton = document.querySelector('[data-menu-toggle]');
    const nav = document.getElementById('site-nav');

    function setMenu(open, returnFocus = false) {
      if (!menuButton || !nav) return;
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('is-open', open);
      if (returnFocus) menuButton.focus({ preventScroll: true });
    }

    if (menuButton && nav) {
      menuButton.setAttribute('aria-controls', nav.id);
      setMenu(false);
      menuButton.addEventListener('click', () => {
        setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
      });
      nav.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => setMenu(false));
      });
      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
          event.preventDefault();
          setMenu(false, true);
        }
      });
      window.addEventListener('resize', () => {
        if (window.getComputedStyle(menuButton).display === 'none') setMenu(false);
      }, { passive: true });
    }

    const filters = Array.from(document.querySelectorAll('[data-project-filter]'));
    const cards = Array.from(document.querySelectorAll('[data-project-card]'));
    const count = document.querySelector('[data-project-count]');
    const empty = document.querySelector('[data-project-empty]');
    const allowedFilters = new Set(['all', 'aerospace', 'robotics', 'manufacturing']);

    if (count) {
      count.setAttribute('role', 'status');
      count.setAttribute('aria-live', 'polite');
      count.setAttribute('aria-atomic', 'true');
    }

    function applyFilter(category, userAction = false) {
      const scrollX = window.scrollX;
      const scrollY = window.scrollY;
      let visible = 0;
      cards.forEach((card) => {
        const categories = (card.dataset.category || '').trim().split(/\s+/);
        const matches = category === 'all' || categories.includes(category);
        card.hidden = !matches;
        if (matches) {
          visible += 1;
          if (userAction) {
            if (card.classList.contains('reveal')) showReveal(card);
            card.querySelectorAll('.reveal').forEach(showReveal);
          }
        }
      });
      filters.forEach((button) => {
        const active = button.dataset.projectFilter === category;
        button.setAttribute('aria-pressed', String(active));
        button.classList.toggle('is-active', active);
      });
      if (count) count.textContent = `${visible} of ${cards.length} projects`;
      if (empty) empty.hidden = visible !== 0;
      if (userAction) {
        // Filtering changes only the grid; the visitor stays at its controls.
        window.requestAnimationFrame(() => {
          window.scrollTo({ left: scrollX, top: scrollY, behavior: 'instant' });
        });
      }
    }

    if (filters.length && cards.length) {
      filters.forEach((button) => {
        button.addEventListener('click', (event) => {
          const category = button.dataset.projectFilter;
          if (!allowedFilters.has(category)) return;
          event.preventDefault();
          applyFilter(category, true);
        });
      });
      applyFilter('all');
    }

    const navLinks = Array.from(document.querySelectorAll('[data-nav-link]'));
    const sectionLinks = new Map();
    navLinks.forEach((link) => {
      const href = link.getAttribute('href') || '';
      if (!href.startsWith('#')) return;
      const section = document.getElementById(href.slice(1));
      if (section) sectionLinks.set(section, link);
    });

    function setActiveSection(section) {
      navLinks.forEach((link) => {
        const active = sectionLinks.get(section) === link;
        link.classList.toggle('is-active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }

    if ('IntersectionObserver' in window && sectionLinks.size) {
      const intersections = new Map();
      try {
        const sectionObserver = new IntersectionObserver((entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) intersections.set(entry.target, entry.boundingClientRect.top);
            else intersections.delete(entry.target);
          });
          const current = Array.from(intersections.entries()).sort((a, b) => Math.abs(a[1]) - Math.abs(b[1]))[0];
          if (current) setActiveSection(current[0]);
        }, { rootMargin: '-18% 0px -52% 0px', threshold: 0 });
        sectionLinks.forEach((_, section) => sectionObserver.observe(section));
      } catch (_) {
        // Navigation remains ordinary anchor links without section observation.
      }
    }
    sectionLinks.forEach((link, section) => {
      link.addEventListener('click', () => setActiveSection(section));
    });

    // Content and links are visible before enhancement and with JavaScript off.
    page.classList.add('js');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
