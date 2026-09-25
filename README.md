# RRB JE Question Bank

Responsive RRB JE practice bank with clickable MCQ answers, progressive rendering, search, topic filtering, year filtering, and dark mode.

## Current database
- 2025: 595 questions (Numerical Ability, Reasoning, General Science)
- 2024: 248 Numerical Ability + 217 Reasoning + 186 General Science questions
- 2024 General Science added from the supplied RRB JE 2024 GA & GS PDF:
  - Physics: 87
  - Chemistry: 99
- Total: 1,246 questions

### 2024 General Science
For the 2024 questions, the cards intentionally show **only the topic pill**; shift/date metadata is not displayed.

The supplied GA & GS PDF contains sections for Physics, Chemistry, Biology, History, Geography, Polity, Economics, Art and Culture, Books & Author, Static GK and Current Affairs. It does **not** contain a Mathematics section. Therefore this update adds only the Physics and Chemistry questions supported by that PDF; no Mathematics questions were invented or taken from outside the supplied source.

## Files
- `index.html` — page shell
- `css/style.v4.min.css` — styles and dark mode
- `js/app.v7.min.js` — filtering, progressive rendering, answer interaction, theme and year filter
- `data/questions.json` — human-readable master database
- `data/questions.v7.min.json` — production JSON
- `assets/railway-logo.webp` — logo
- `_headers` — Netlify caching rules
- `robots.txt`, `sitemap.xml` — SEO files

## 2024 Reasoning
Added 217 topic-wise RRB JE 2024 Reasoning questions from the supplied PDF. 2024 cards show only the Topic pill; shift/date metadata is not displayed.

## 2024 Science
Added 87 Physics and 99 Chemistry questions from the supplied RRB JE 2024 General Science & Awareness PDF. The source's original question numbering and answer keys are retained in the database records.
