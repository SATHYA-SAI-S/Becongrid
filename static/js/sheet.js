// Bottom sheet and layout collapse controller

let currentSheetState = 'peek'; // 'peek', 'half', 'full'

export function initBottomSheet({ sheetEl, handleEl, backdropEl }) {
  if (!sheetEl || !handleEl) return;

  let startY = 0;
  let currentTranslateY = 0;
  let isDragging = false;
  let sheetHeight = sheetEl.getBoundingClientRect().height;

  function getPixelForState(state) {
    sheetHeight = sheetEl.getBoundingClientRect().height;
    if (state === 'full') return sheetHeight * 0.06;
    if (state === 'half') return sheetHeight * 0.48;
    return sheetHeight - 76; // Peek
  }

  function setSheetState(newState) {
    currentSheetState = newState;
    sheetEl.classList.remove('state-peek', 'state-half', 'state-full');
    sheetEl.classList.add(`state-${newState}`);
    sheetEl.style.transform = '';

    if (backdropEl) {
      backdropEl.classList.toggle('active', newState === 'full');
    }
  }

  // Pointer/Touch events on the drag handle area
  handleEl.addEventListener('pointerdown', (e) => {
    isDragging = true;
    startY = e.clientY;
    sheetHeight = sheetEl.getBoundingClientRect().height;
    currentTranslateY = getPixelForState(currentSheetState);
    sheetEl.classList.add('dragging');
    handleEl.setPointerCapture(e.pointerId);
  });

  handleEl.addEventListener('pointermove', (e) => {
    if (!isDragging) return;
    const deltaY = e.clientY - startY;
    let newY = currentTranslateY + deltaY;

    // Constrain within min/max bounds
    const minY = sheetHeight * 0.04;
    const maxY = sheetHeight - 60;
    if (newY < minY) newY = minY;
    if (newY > maxY) newY = maxY;

    sheetEl.style.transform = `translateY(${newY}px)`;
  });

  function endDrag(e) {
    if (!isDragging) return;
    isDragging = false;
    sheetEl.classList.remove('dragging');

    try {
      handleEl.releasePointerCapture(e.pointerId);
    } catch (_) {}

    const deltaY = e.clientY - startY;
    const currentY = currentTranslateY + deltaY;

    // Snap to nearest state
    const peekY = sheetHeight - 76;
    const halfY = sheetHeight * 0.48;
    const fullY = sheetHeight * 0.06;

    const distToPeek = Math.abs(currentY - peekY);
    const distToHalf = Math.abs(currentY - halfY);
    const distToFull = Math.abs(currentY - fullY);

    if (distToFull <= distToHalf && distToFull <= distToPeek) {
      setSheetState('full');
    } else if (distToHalf <= distToPeek) {
      setSheetState('half');
    } else {
      setSheetState('peek');
    }
  }

  handleEl.addEventListener('pointerup', endDrag);
  handleEl.addEventListener('pointercancel', endDrag);

  // Clicking the handle toggles between peek and half/full
  handleEl.addEventListener('click', (e) => {
    if (Math.abs(e.clientY - startY) > 8) return; // Ignore if user dragged
    if (currentSheetState === 'peek') {
      setSheetState('half');
    } else if (currentSheetState === 'half') {
      setSheetState('full');
    } else {
      setSheetState('peek');
    }
  });

  if (backdropEl) {
    backdropEl.addEventListener('click', () => {
      setSheetState('peek');
    });
  }

  return {
    setSheetState,
    getState: () => currentSheetState
  };
}

export function initDesktopSidebar({ sidebarEl, toggleBtnEl, closeBtnEl, appContainerEl }) {
  if (!sidebarEl) return;

  function toggleSidebar() {
    const isCollapsed = sidebarEl.classList.toggle('collapsed');
    if (appContainerEl) {
      appContainerEl.classList.toggle('sidebar-closed', isCollapsed);
    }
  }

  if (toggleBtnEl) {
    toggleBtnEl.addEventListener('click', toggleSidebar);
  }

  if (closeBtnEl) {
    closeBtnEl.addEventListener('click', toggleSidebar);
  }

  return {
    toggle: toggleSidebar,
    expand: () => {
      sidebarEl.classList.remove('collapsed');
      if (appContainerEl) appContainerEl.classList.remove('sidebar-closed');
    },
    collapse: () => {
      sidebarEl.classList.add('collapsed');
      if (appContainerEl) appContainerEl.classList.add('sidebar-closed');
    }
  };
}
