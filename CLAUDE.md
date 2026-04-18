# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Spendly** — a student-guided Flask expense tracker. Routes include placeholder comments referencing steps (Step 1, etc.), indicating this is an educational/step-by-step project where students incrementally build features.

## Tech Stack

- **Backend:** Flask (Python) — runs on `localhost:5001`
- **Frontend:** Jinja2 templates, vanilla HTML/CSS/JS
- **Database:** SQLite (via `database/db.py`) — not yet implemented (students write it)

## Key Commands

```bash
# Activate virtual environment
source venv/Scripts/activate   # Windows (Git Bash)
venv\Scripts\activate          # Windows (CMD)
source venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the dev server
python app.py

# Run tests
pytest
```

## Architecture

```
app.py                     # Flask app — routes defined here
database/
  __init__.py              # Stub — students implement in Step 1
  db.py                    # Stub — students implement in Step 1
    # Expected: get_db(), init_db(), seed_db()
templates/
  base.html                # Base layout (navbar, footer, font imports)
  landing.html             # Landing page with hero, features, YouTube modal
  login.html               # Login form
  register.html            # Registration form
  terms.html               # Terms & conditions
  privacy.html             # Privacy policy
static/
  css/style.css            # All styles — design tokens in :root
  js/main.js               # Empty — students add JS here
```

## Implementation Steps (from placeholder routes/comments)

The app is built incrementally. Steps referenced in code:

1. **Step 1** — Database setup (`database/db.py`): `get_db()`, `init_db()`, `seed_db()`
2. **Step 3** — Logout
3. **Step 4** — Profile page
4. **Step 7** — Add expense
5. **Step 8** — Edit expense
6. **Step 9** — Delete expense

When implementing features, follow the step-by-step progression and fill in the placeholder stubs rather than creating parallel implementations.

## Design System

CSS variables in `style.css` define the visual identity:
- Fonts: DM Serif Display (headings), DM Sans (body)
- Colors: green accent (`#1a472a`), gold accent (`#c17f24`), warm paper background (`#f7f6f3`)
- Max widths: 1200px (full), 440px (auth pages)

## Database (Planned)

SQLite database file `expense_tracker.db` (gitignored). Students must implement `database/db.py` with:
- `get_db()` — returns SQLite connection with `row_factory` and foreign keys enabled
- `init_db()` — creates tables using `CREATE TABLE IF NOT EXISTS`
- `seed_db()` — inserts sample data for development
