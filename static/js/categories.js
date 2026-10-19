// Multi-select Category Filters Module

import { CONFIG, getCategoryById } from './config.js';

let activeCategories = new Set(); // Empty means "All" active
let filterChangeCallback = null;

export function initCategoryFilters(containerElement, onFilterChange) {
  filterChangeCallback = onFilterChange;
  renderCategoryChips(containerElement);
}

export function getActiveCategoryList() {
  return Array.from(activeCategories);
}

function renderCategoryChips(container) {
  if (!container) return;
  container.innerHTML = '';

  // 1. "All" Chip
  const allChip = document.createElement('button');
  allChip.className = `category-chip ${activeCategories.size === 0 ? 'active' : ''}`;
  allChip.dataset.category = 'all';
  allChip.setAttribute('type', 'button');
  allChip.setAttribute('aria-pressed', activeCategories.size === 0 ? 'true' : 'false');
  allChip.innerHTML = `
    <span class="chip-dot" style="background-color: var(--color-primary);"></span>
    <span>All Resources</span>
  `;
  allChip.addEventListener('click', () => {
    activeCategories.clear();
    updateChipClasses(container);
    if (filterChangeCallback) filterChangeCallback(getActiveCategoryList());
  });
  container.appendChild(allChip);

  // 2. Individual Category Chips
  CONFIG.CATEGORIES.forEach(cat => {
    const chip = document.createElement('button');
    const isSelected = activeCategories.has(cat.id);
    chip.className = `category-chip ${isSelected ? 'active' : ''}`;
    chip.dataset.category = cat.id;
    chip.setAttribute('type', 'button');
    chip.setAttribute('aria-pressed', isSelected ? 'true' : 'false');
    chip.title = cat.description;
    chip.innerHTML = `
      <span class="chip-dot" style="background-color: ${cat.color};"></span>
      <span>${cat.label}</span>
    `;

    chip.addEventListener('click', () => {
      toggleCategory(cat.id, container);
    });

    container.appendChild(chip);
  });
}

function toggleCategory(categoryId, container) {
  if (activeCategories.has(categoryId)) {
    activeCategories.delete(categoryId);
  } else {
    activeCategories.add(categoryId);
  }

  // If user unselects everything, it automatically reverts to "All"
  updateChipClasses(container);
  if (filterChangeCallback) {
    filterChangeCallback(getActiveCategoryList());
  }
}

function updateChipClasses(container) {
  const chips = container.querySelectorAll('.category-chip');
  chips.forEach(chip => {
    const catId = chip.dataset.category;
    if (catId === 'all') {
      const isAll = activeCategories.size === 0;
      chip.classList.toggle('active', isAll);
      chip.setAttribute('aria-pressed', isAll ? 'true' : 'false');
    } else {
      const isSelected = activeCategories.has(catId);
      chip.classList.toggle('active', isSelected);
      chip.setAttribute('aria-pressed', isSelected ? 'true' : 'false');
    }
  });
}
