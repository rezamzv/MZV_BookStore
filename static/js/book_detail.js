/* book_detail.js */
document.addEventListener('DOMContentLoaded', () => {

    /* Cover image fallback (in case onerror fires before JS loads) */
    const img = document.querySelector('.detail-cover img');
    if (img && !img.complete) {
        img.addEventListener('error', () => {
            img.style.display = 'none';
            const fb = img.parentElement.querySelector('.cover-fallback');
            if (fb) fb.style.display = 'flex';
        });
    }

});
