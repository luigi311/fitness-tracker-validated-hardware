/**
 * Device search & filter.
 * Reads data-* attributes off each .device-card and toggles visibility.
 * No build step, no framework — just DOM.
 */
(function () {
  'use strict';

  const grid = document.getElementById('devices-grid');
  if (!grid) return;

  const searchInput = document.getElementById('device-search');
  const noResults = document.getElementById('no-results');
  const resultsCount = document.getElementById('results-count');
  const cards = Array.from(grid.querySelectorAll('.device-card'));
  const totalCount = cards.length;

  // Active filters: { category: 'all', status: 'all', connectivity: 'all' }
  const filters = { category: 'all', status: 'all', connectivity: 'all' };
  let searchQuery = '';

  // ---------- Wire up filter chips ----------
  document.querySelectorAll('.filter-chip').forEach((chip) => {
    chip.addEventListener('click', () => {
      const type = chip.dataset.filterType;
      const value = chip.dataset.filterValue;
      filters[type] = value;

      // Update active state within the same group
      document
        .querySelectorAll(`.filter-chip[data-filter-type="${type}"]`)
        .forEach((c) => c.classList.toggle('is-active', c === chip));

      applyFilters();
    });
  });

  // ---------- Wire up search ----------
  let searchTimer;
  searchInput.addEventListener('input', (e) => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      searchQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    }, 100);
  });

  // ---------- Filter logic ----------
  function cardMatches(card) {
    // Category
    if (filters.category !== 'all' && card.dataset.category !== filters.category) {
      return false;
    }
    // Status
    if (filters.status !== 'all' && card.dataset.status !== filters.status) {
      return false;
    }
    // Connectivity (multi-value field — substring match on space-separated list)
    if (filters.connectivity !== 'all') {
      const connList = (card.dataset.connectivity || '').split(' ');
      if (!connList.includes(filters.connectivity)) return false;
    }
    // Search — match across name, manufacturer, features
    if (searchQuery) {
      const haystack = [
        card.dataset.name || '',
        card.dataset.manufacturer || '',
        card.dataset.features || '',
      ].join(' ');
      if (!haystack.includes(searchQuery)) return false;
    }
    return true;
  }

  function applyFilters() {
    let visible = 0;
    cards.forEach((card) => {
      const match = cardMatches(card);
      card.hidden = !match;
      if (match) visible++;
    });

    noResults.hidden = visible !== 0;
    updateCount(visible);
  }

  function updateCount(visible) {
    if (visible === totalCount) {
      resultsCount.textContent = `Showing all ${totalCount} devices`;
    } else {
      resultsCount.textContent = `Showing ${visible} of ${totalCount} devices`;
    }
  }

  // Initial count
  updateCount(totalCount);
})();
