/* ── Book data ──────────────────────────────────────── */
const BOOKS = [
    {
        title: "Pride and Prejudice",
        author: "Jane Austen",
        genre: "Classic Romance",
        year: 1813,
        price: "£8.99",
        badge: "Bestseller",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/PrideAndPrejudice.jpg/390px-PrideAndPrejudice.jpg",
        coverBg: "#4A2C1A",
        desc: "Witty and irresistible, Austen's beloved novel follows the spirited Elizabeth Bennet as she navigates society, love, and misunderstanding. A masterwork of social observation, romantic tension, and biting humour that remains utterly modern.",
    },
    {
        title: "Jane Eyre",
        author: "Charlotte Brontë",
        genre: "Gothic Fiction",
        year: 1847,
        price: "£7.99",
        badge: "Classic",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jane_Eyre_title_page.jpg/390px-Jane_Eyre_title_page.jpg",
        coverBg: "#2E1A0E",
        desc: "A fierce orphan girl grows into a woman of rare moral courage. Brontë's Gothic romance crackles with passion, secrets hidden behind locked doors, and one of literature's most enduring declarations of selfhood and independent love.",
    },
    {
        title: "Great Expectations",
        author: "Charles Dickens",
        genre: "Victorian Novel",
        year: 1861,
        price: "£8.49",
        badge: "Staff Pick",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Great_Expectations_Penguin_cover.jpg/390px-Great_Expectations_Penguin_cover.jpg",
        coverBg: "#3B2010",
        desc: "Young Pip dreams of escaping poverty for a life of gentility, guided by the eccentric Miss Havisham and his own foolish ambitions. Dickens weaves a rich tapestry of class, identity, guilt, and what it truly means to be a gentleman.",
    },
    {
        title: "Wuthering Heights",
        author: "Emily Brontë",
        genre: "Gothic Romance",
        year: 1847,
        price: "£7.99",
        badge: "Classic",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Wuthering_Heights_1847.jpg/390px-Wuthering_Heights_1847.jpg",
        coverBg: "#251510",
        desc: "Across storm-lashed Yorkshire moors, Heathcliff and Catherine are bound by a love as violent as the landscape itself. Raw, tempestuous and darkly romantic, Brontë's only novel is one of literature's most haunting explorations of obsession.",
    },
    {
        title: "Anna Karenina",
        author: "Leo Tolstoy",
        genre: "Literary Fiction",
        year: 1878,
        price: "£10.99",
        badge: "Masterwork",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Anna_Karenina_1878_title_page.jpg/390px-Anna_Karenina_1878_title_page.jpg",
        coverBg: "#3A1C0C",
        desc: "Tolstoy's monumental novel traces the tragic affair of the beautiful, married Anna Karenina against the vivid canvas of Russian aristocratic society. A profound meditation on love, hypocrisy, freedom, and the devastating consequences of transgression.",
    },
    {
        title: "Crime and Punishment",
        author: "Fyodor Dostoevsky",
        genre: "Psychological Fiction",
        year: 1866,
        price: "£9.49",
        badge: "Landmark",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Prestuplenie_i_nakazanie_-_Crime_and_Punishment_-_1st_edition%2C_1867.jpg/390px-Prestuplenie_i_nakazanie_-_Crime_and_Punishment_-_1st_edition%2C_1867.jpg",
        coverBg: "#1E1008",
        desc: "A destitute student murders a pawnbroker, convinced the deed is morally justified. Dostoevsky's gripping novel descends into the psychology of guilt and redemption, crafting one of the most intense and searching portraits of the human conscience ever written.",
    },
    {
        title: "Madame Bovary",
        author: "Gustave Flaubert",
        genre: "Realist Fiction",
        year: 1856,
        price: "£8.99",
        badge: "Classic",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Madame_bovary_1857.jpg/390px-Madame_bovary_1857.jpg",
        coverBg: "#2A1A12",
        desc: "Emma Bovary, a doctor's wife in provincial Normandy, fills her days with romantic fantasies and ruinous desires. Flaubert's precise, devastating prose dissects bourgeois provincial life and the corrosive power of illusions that cannot be fulfilled.",
    },
    {
        title: "Don Quixote",
        author: "Miguel de Cervantes",
        genre: "Adventure & Satire",
        year: 1605,
        price: "£11.99",
        badge: "The First Novel",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/DQ_Cervantes_en_Bruselas.jpg/390px-DQ_Cervantes_en_Bruselas.jpg",
        coverBg: "#3D2108",
        desc: "A Spanish gentleman driven mad by chivalric romances sets off as a knight-errant with his loyal squire Sancho Panza. By turns comic, tragic, and profoundly humane, Cervantes created the world's first modern novel — and perhaps its greatest.",
    },
    {
        title: "The Brothers Karamazov",
        author: "Fyodor Dostoevsky",
        genre: "Philosophical Novel",
        year: 1880,
        price: "£10.49",
        badge: "Masterwork",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Dostoevsky_Brothers_Karamazov_first_edition.jpg/390px-Dostoevsky_Brothers_Karamazov_first_edition.jpg",
        coverBg: "#1C100A",
        desc: "Three brothers and their dissolute father collide over love, money, faith, and murder in Tsarist Russia. Dostoevsky's final novel is his greatest — a vast, tumultuous inquiry into God, free will, and the spiritual struggle within every human soul.",
    },
    {
        title: "Middlemarch",
        author: "George Eliot",
        genre: "Victorian Novel",
        year: 1871,
        price: "£9.99",
        badge: "Staff Pick",
        cover: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Middlemarch_-_Eliot.png/390px-Middlemarch_-_Eliot.png",
        coverBg: "#352010",
        desc: "Set in a fictional English Midlands town, Eliot's masterpiece weaves together the lives of idealistic Dorothea Brooke, the ambitious Dr Lydgate, and an entire community. Virginia Woolf called it one of the few English novels written for grown-up people.",
    },
];

/* ── Render cards ────────────────────────────────────── */
function renderBooks() {
    const grid = document.getElementById('book-grid');

    BOOKS.forEach(book => {
        const card = document.createElement('article');
        card.className = 'book-card';
        card.innerHTML = `
          <div class="book-card-cover" style="background:${book.coverBg}">
            <img
              src="${book.cover}"
              alt="Cover of ${book.title}"
              loading="lazy"
              onerror="this.style.display='none';this.parentElement.querySelector('.cover-fallback').style.display='flex'"
            />
            <div class="cover-fallback" style="display:none">
              <div class="cf-ornament">❧</div>
              <div class="cf-title">${book.title}</div>
              <div class="cf-author">${book.author}</div>
            </div>
            <span class="book-badge">${book.badge}</span>
          </div>
          <div class="book-card-body">
            <p class="book-genre">${book.genre} · ${book.year}</p>
            <h3 class="book-title">${book.title}</h3>
            <p class="book-author">${book.author}</p>
            <p class="book-desc">${book.desc}</p>
          </div>
          <div class="book-card-footer">
            <div>
              <span class="book-price">${book.price}</span>
            </div>
            <a href="/cart/add?book=${encodeURIComponent(book.title)}" class="btn-add-to-bag">
              <svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" fill="none" stroke-width="2.5" aria-hidden="true">
                <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/>
              </svg>
              Add to Bag
            </a>
          </div>
        `;
        grid.appendChild(card);
    });
}

/* ── Account dropdown ──────────────────────────────── */
(function () {
    const toggle = document.querySelector('.account-menu-toggle');
    const dropdown = document.getElementById('account-dropdown');
    if (!toggle || !dropdown) return;
    const open = () => {
        dropdown.classList.add('is-open');
        dropdown.setAttribute('aria-hidden', 'false');
        toggle.setAttribute('aria-expanded', 'true');
    };
    const close = () => {
        dropdown.classList.remove('is-open');
        dropdown.setAttribute('aria-hidden', 'true');
        toggle.setAttribute('aria-expanded', 'false');
    };
    toggle.addEventListener('click', e => {
        e.stopPropagation();
        dropdown.classList.contains('is-open') ? close() : open();
    });
    document.addEventListener('click', e => {
        if (!toggle.contains(e.target) && !dropdown.contains(e.target)) close();
    });
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape') close();
    });
})();

document.addEventListener('DOMContentLoaded', function () {
    renderBooks();
});