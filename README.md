# Vincent Cook — Engineering Portfolio

Aerospace Engineering senior at San José State University, with an expected graduation date of May 2027.

This repository contains my engineering portfolio website and two tailored resumes:

- [Robotics & Mechatronics resume](dist/downloads/Vincent-Cook-Robotics-Mechatronics.pdf)
- [Manufacturing & Production resume](dist/downloads/Vincent-Cook-Manufacturing-Production.pdf)

Each resume also has editable Word and plain-text versions in [`dist/downloads/`](dist/downloads/).

The [hosted portfolio](https://vincent-cook-engineering.san-jose-sta-2217.chatgpt.site/) is currently private for review.

## Portfolio contents

The website features eleven project entries, work experience, and a searchable library of 41 SJSU course and requirement references.

Engineering projects include SJSU Robotics, an SAE Spartan Racing electric motor test bench, BROADSWORD rocket landing-leg CAD and trajectory simulation, an ongoing hybrid electric/hydrogen aircraft senior project, and the NASA L’SPACE Mission Concept Academy.

Confirmed class projects include motor CAD, missile launch trajectory code, Frisbee rigid-body flight modeling in MATLAB and MotionGenesis, MATLAB/Simulink controls, open wind-tunnel airfoil studies, and structural/material behavior.

Current aircraft work is wing-model design and project planning. Further analysis, construction, electronics integration, testing, and commercial-scale modeling are planned work; spring 2027 is the first-flight target. L’SPACE is an educational project, with current contributions to scientific planning and mechanical component choices.

The course reference library follows the supplied [2023–2024 SJSU Aerospace Engineering roadmap](https://catalog.sjsu.edu/preview_program.php?catoid=10&poid=8789&returnto=5272). It distinguishes personal coursework from publicly documented course expectations.

## View locally

The site uses plain HTML, CSS, and JavaScript, with no build step. With Python installed, run this command from the repository root:

```sh
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000` in a browser. Google Fonts loads online; system font fallbacks are included.

## Edit the portfolio

| File | Purpose |
| --- | --- |
| [`dist/index.html`](dist/index.html) | Project descriptions, experience, course references, and resume links |
| [`dist/styles.css`](dist/styles.css) | Typography, colors, responsive layout, and print styles |
| [`dist/app.js`](dist/app.js) | Course search and roadmap-year filtering |
| [`dist/downloads/`](dist/downloads/) | PDF, Word, and plain-text resumes |

The course references remain readable without JavaScript. Replace resume files under the same names when updating them. Editing this repository does not automatically update the hosted portfolio.
