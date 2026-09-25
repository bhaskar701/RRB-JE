# RRB JE 2025–26 Complete Practice Bank

A fast, responsive RRB JE MCQ practice website built with plain HTML, CSS and JavaScript.

## Repository structure

```text
.
├── index.html
├── assets/
│   └── railway-logo.webp
├── css/
│   └── style.v2.min.css
├── js/
│   └── app.v2.min.js
├── data/
│   ├── questions.json
│   └── questions.v2.min.json
├── robots.txt
├── sitemap.xml
├── _headers
└── README.md
```

## Adding questions

Edit **`data/questions.json`**. Keep the same object structure:

```json
{
  "section": "science",
  "topic": "Physics",
  "question": "What is the SI unit of force?",
  "options": ["Joule", "Newton", "Watt", "Pascal"],
  "answer": 1,
  "date": "25/09/2026",
  "shift": "Shift 1"
}
```

Answer indexes are zero-based:

- `0` = Option A
- `1` = Option B
- `2` = Option C
- `3` = Option D

Use these section values:

- `numerical`
- `reasoning`
- `science`

After editing `questions.json`, run the included build script to generate the minified production JSON used by the site.

## Local build

Requirements: Python 3.

Run:

```bash
python tools/build_questions.py
```

This creates/updates:

```text
data/questions.v2.min.json
```

## GitHub + Netlify workflow

1. Create a GitHub repository, e.g. `rrb-je-qbank`.
2. Upload the contents of this folder to the repository root.
3. Connect the repository to Netlify.
4. Set the Netlify publish directory to `.` (the repository root).
5. Every push to the selected GitHub branch can trigger a new Netlify deployment.

The website remains a static site; no server is required.

## Important

The `_headers` file is useful when the site is hosted on Netlify. It is not interpreted by GitHub Pages.

The website's UI and quiz interaction are kept in the existing HTML/CSS/JavaScript application. Questions are stored separately so the question bank can be maintained without editing the UI.
