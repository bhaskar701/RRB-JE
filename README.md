# RRB JE Question Bank

A responsive, dark-mode-ready RRB JE practice website with year-wise filtering and progressive question loading.

## Current question bank
- 2025: 595 questions (Numerical Ability, Reasoning, General Science)
- 2024: 248 Numerical Ability + 217 Reasoning + 268 General Science questions
- 2024 General Science is limited to the three requested topics: Physics, Chemistry and Biology
- Total: 1,313 questions

## 2024 General Science
The supplied RRB JE 2024 General Science & Awareness PDF was used for the 2024 Science additions. Only Physics (87), Chemistry (99), and Biology (82) were imported. The source dates/shifts are not displayed on 2024 cards, consistent with the existing 2024 question presentation.

## Architecture
- `data/questions.json` — human-readable master database
- `data/questions.v7.min.json` — minified production database
- `js/app.v7.min.js` — production app logic
- `css/style.v4.min.css` — responsive styling and dark mode
- `assets/railway-logo.webp` — optimized logo asset

## 2024 filtering
The year switcher supports 2025, 2024 and All Years. Topic filtering in General Science now includes Physics, Chemistry and Biology for 2024.
