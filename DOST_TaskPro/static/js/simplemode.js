(function() {
  'use strict';

  var STORAGE_KEY = 'simpleMode';
  var syncTimeout = null;
  var isProcessing = false;

  function getStoredState() {
    return localStorage.getItem(STORAGE_KEY) === 'true';
  }

  function getAlpineRoot() {
    return document.documentElement;
  }

  function isSimpleModeActive() {
    return document.documentElement.classList.contains('simple-mode');
  }

  function setAlpineSimpleMode(active) {
    var root = getAlpineRoot();
    if (root && root._x_dataStack && root._x_dataStack[0] && Object.prototype.hasOwnProperty.call(root._x_dataStack[0], 'simpleMode')) {
      root._x_dataStack[0].simpleMode = active;
    }
  }

  function applySimpleMode(active) {
    document.documentElement.classList.toggle('simple-mode', active);
    if (document.body) {
      document.body.classList.toggle('simple-mode', active);
    }
    localStorage.setItem(STORAGE_KEY, String(active));
    setAlpineSimpleMode(active);
    updateControls(active);
    syncTables();
    window.dispatchEvent(new CustomEvent('taskpro:simple-mode-changed', { detail: { active: active } }));
  }

  function toggleSimpleMode() {
    applySimpleMode(!isSimpleModeActive());
  }

  function removeLegacyFloatingToggle() {
    document.querySelectorAll('.simple-mode-floating-toggle').forEach(function(el) {
      el.remove();
    });
  }

  function updateControls(active) {
    removeLegacyFloatingToggle();
    document.querySelectorAll('[data-simple-mode-toggle]').forEach(function(control) {
      control.setAttribute('aria-pressed', active ? 'true' : 'false');
      control.setAttribute('title', active ? 'Turn off Simple Mode' : 'Turn on Simple Mode');
      var label = control.querySelector('[data-simple-mode-label]');
      if (label) label.textContent = active ? 'Simple Mode On' : 'Simple Mode';
      var icon = control.querySelector('.material-icons');
      if (icon) icon.textContent = active ? 'visibility' : 'auto_awesome';
    });

    var notice = document.getElementById('simpleModeNotice');
    if (notice) {
      notice.hidden = !active;
    }
  }

  function createSimpleNotice() {
    if (document.getElementById('simpleModeNotice')) return;
    var main = document.querySelector('main');
    if (!main) return;
    var notice = document.createElement('div');
    notice.id = 'simpleModeNotice';
    notice.className = 'simple-mode-page-notice';
    notice.hidden = true;
    notice.innerHTML = '<span class="material-icons">tips_and_updates</span><div><strong>Simple Mode is on.</strong><span> This view keeps actions clear, spacing calm, and advanced details tucked away.</span></div><button type="button" data-simple-mode-turn-off>Turn off</button>';
    var content = main.querySelector('.p-4, .p-6, .px-4, .px-6') || main.firstElementChild || main;
    content.parentNode.insertBefore(notice, content);
    var off = notice.querySelector('[data-simple-mode-turn-off]');
    if (off) off.addEventListener('click', function() { applySimpleMode(false); });
  }

  function addSimpleHints() {
    var actions = [
      ['a[href*="create"], button[onclick*="open"], button[id*="add"], a[href*="add"]', 'Start here'],
      ['button[type="submit"], input[type="submit"]', 'Save'],
      ['a[href*="edit"], button[data-edit], button[title*="Edit"]', 'Change'],
      ['a[href*="delete"], button[onclick*="delete"], button[id*="delete"]', 'Remove']
    ];

    actions.forEach(function(pair) {
      document.querySelectorAll(pair[0]).forEach(function(el) {
        if (el.dataset.simpleHintApplied === 'true') return;
        if (el.closest('#sidebar, header, .simple-mode-page-notice')) return;
        el.dataset.simpleHintApplied = 'true';
        el.setAttribute('data-simple-label', pair[1]);
      });
    });
  }

  function injectModernSimpleModeStyles() {
    if (document.getElementById('simpleModeModernStyles')) return;
    var style = document.createElement('style');
    style.id = 'simpleModeModernStyles';
    style.textContent = `
      html.simple-mode {
        --sm-bg: #f4f7fb;
        --sm-card: #ffffff;
        --sm-soft: #f8fafc;
        --sm-border: #d8e2ee;
        --sm-text: #172033;
        --sm-muted: #53647a;
        --sm-accent: #2563eb;
        --sm-accent-soft: #e8f1ff;
        --sm-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
      }
      html.dark.simple-mode {
        --sm-bg: #0f172a;
        --sm-card: #111827;
        --sm-soft: #162033;
        --sm-border: #2f4057;
        --sm-text: #f8fafc;
        --sm-muted: #b6c2d2;
        --sm-accent: #60a5fa;
        --sm-accent-soft: #142948;
        --sm-shadow: 0 16px 32px rgba(0, 0, 0, 0.28);
      }
      html.simple-mode body {
        background: var(--sm-bg) !important;
        color: var(--sm-text) !important;
        font-size: 15.5px !important;
        line-height: 1.5 !important;
      }
      html.simple-mode main { background: transparent !important; }
      html.simple-mode h1,
      html.simple-mode h2,
      html.simple-mode h3,
      html.simple-mode h4,
      html.simple-mode h5,
      html.simple-mode h6 {
        color: var(--sm-text) !important;
        letter-spacing: 0 !important;
      }
      html.simple-mode .text-xs { font-size: 0.82rem !important; }
      html.simple-mode .text-sm { font-size: 0.95rem !important; }
      html.simple-mode .text-base { font-size: 1rem !important; }
      html.simple-mode .text-lg { font-size: 1.12rem !important; }
      html.simple-mode .bg-white,
      html.simple-mode .admin-surface,
      html.simple-mode .settings-panel,
      html.simple-mode .settings-nav,
      html.simple-mode .settings-help,
      html.simple-mode .comm-panel,
      html.simple-mode .calendar-panel,
      html.simple-mode .chart-card,
      html.simple-mode .user-table-card,
      html.simple-mode .reports-card,
      html.simple-mode .metric-card,
      html.simple-mode .section-card,
      html.simple-mode .card {
        background: var(--sm-card) !important;
        border-color: var(--sm-border) !important;
        border-radius: 16px !important;
        box-shadow: var(--sm-shadow) !important;
      }
      html.simple-mode .shadow-lg,
      html.simple-mode .shadow-xl,
      html.simple-mode .shadow-2xl {
        box-shadow: var(--sm-shadow) !important;
      }
      html.simple-mode button:not(.theme-toggle):not(.sidebar-toggle-btn):not([aria-label]),
      html.simple-mode .btn:not(.theme-toggle):not(.sidebar-toggle-btn),
      html.simple-mode input[type="submit"],
      html.simple-mode a[role="button"] {
        min-height: 42px !important;
        padding: 0.72rem 1rem !important;
        border-radius: 10px !important;
        font-size: 0.95rem !important;
      }
      html.simple-mode input[type="text"],
      html.simple-mode input[type="email"],
      html.simple-mode input[type="password"],
      html.simple-mode input[type="number"],
      html.simple-mode input[type="date"],
      html.simple-mode input[type="search"],
      html.simple-mode select,
      html.simple-mode textarea {
        min-height: 44px !important;
        padding: 0.78rem 0.9rem !important;
        border: 1px solid var(--sm-border) !important;
        border-radius: 10px !important;
        background: var(--sm-card) !important;
        color: var(--sm-text) !important;
        font-size: 0.95rem !important;
      }
      html.simple-mode input:focus,
      html.simple-mode select:focus,
      html.simple-mode textarea:focus {
        border-color: var(--sm-accent) !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
      }
      html.simple-mode table td,
      html.simple-mode table th {
        padding: 0.85rem 1rem !important;
        font-size: 0.9rem !important;
      }
      html.simple-mode [data-simple-label]::before { content: none !important; }
      html.simple-mode .simple-mode-page-notice {
        border: 1px solid rgba(37, 99, 235, 0.24) !important;
        border-radius: 16px !important;
        background: var(--sm-accent-soft) !important;
        color: var(--sm-text) !important;
        box-shadow: 0 10px 24px rgba(37, 99, 235, 0.08) !important;
      }
      html.simple-mode .simple-mode-page-notice span { color: var(--sm-muted) !important; }
      html.simple-mode .hover-card:hover,
      html.simple-mode .comm-action:hover,
      html.simple-mode .calendar-action-btn:hover,
      html.simple-mode .settings-nav-link:hover {
        transform: translateY(-1px) !important;
      }
      html.simple-mode .text-gray-400,
      html.simple-mode .text-gray-500,
      html.simple-mode .text-gray-600,
      html.simple-mode .text-slate-400,
      html.simple-mode .text-slate-500,
      html.simple-mode .text-slate-600 {
        color: var(--sm-muted) !important;
      }
    `;
    document.head.appendChild(style);
  }

  function markTechnicalColumns() {
    document.querySelectorAll('table').forEach(function(table) {
      var headers = Array.prototype.slice.call(table.querySelectorAll('thead th'));
      headers.forEach(function(th, index) {
        var text = (th.textContent || '').trim().toLowerCase();
        if (/^(id|#|uuid|created at|updated at|timestamp|ip|logs?|metadata|debug|token)$/.test(text)) {
          th.classList.add('column-technical');
          table.querySelectorAll('tbody tr').forEach(function(row) {
            if (row.children[index]) row.children[index].classList.add('column-technical');
          });
        }
      });
    });
  }

  function syncTables() {
    if (isProcessing) return;
    isProcessing = true;
    try {
      var isSimple = isSimpleModeActive();
      var body = document.body;
      var isReversed = body && body.classList.contains('simple-mode-reversed');
      var isExcluded = body && body.classList.contains('no-simple-mode');
      var hasCharts = !!document.querySelector('.chart-section');

      document.querySelectorAll('.table-section').forEach(function(tableEl) {
        if (!isSimple || isExcluded) {
          tableEl.style.removeProperty('display');
          return;
        }
        if (isReversed || !hasCharts) {
          tableEl.style.setProperty('display', 'block', 'important');
        } else {
          tableEl.style.setProperty('display', 'none', 'important');
        }
      });
    } catch (e) {
      console.error('SimpleModeHelper error:', e);
    }
    isProcessing = false;
  }

  function debouncedSync() {
    clearTimeout(syncTimeout);
    syncTimeout = setTimeout(function() {
      addSimpleHints();
      markTechnicalColumns();
      syncTables();
    }, 100);
  }

  function bindExistingToggles() {
    document.querySelectorAll('[data-simple-mode-toggle]').forEach(function(control) {
      if (control.dataset.simpleModeBound === 'true') return;
      if (control.hasAttribute('@click') || control.hasAttribute('x-on:click')) {
        control.dataset.simpleModeBound = 'true';
        return;
      }
      control.dataset.simpleModeBound = 'true';
      control.addEventListener('click', function(event) {
        event.preventDefault();
        toggleSimpleMode();
      });
    });
  }

  function init() {
    removeLegacyFloatingToggle();
    injectModernSimpleModeStyles();
    applySimpleMode(getStoredState());
    createSimpleNotice();
    bindExistingToggles();
    addSimpleHints();
    markTechnicalColumns();
    updateControls(isSimpleModeActive());

    var observer = new MutationObserver(function(mutations) {
      var shouldSync = false;
      for (var i = 0; i < mutations.length; i++) {
        if (mutations[i].attributeName === 'class' || mutations[i].addedNodes.length) {
          shouldSync = true;
          break;
        }
      }
      if (shouldSync) debouncedSync();
    });

    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    if (document.body) observer.observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.SimpleModeHelper = {
    isActive: isSimpleModeActive,
    set: applySimpleMode,
    toggle: toggleSimpleMode,
    sync: syncTables
  };
})();
