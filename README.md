# Vincent Cook — Engineering Portfolio

Aerospace Engineering senior at San José State University, with an expected graduation date of May 2027.

This repository contains my engineering portfolio website and two tailored resumes:

- [Robotics & Mechatronics resume](dist/downloads/Vincent-Cook-Robotics-Mechatronics.pdf)
- [Manufacturing & Production resume](dist/downloads/Vincent-Cook-Manufacturing-Production.pdf)

Each resume also has editable Word and plain-text versions in [`dist/downloads/`](dist/downloads/).

The [GitHub Pages portfolio address](https://vincook-code.github.io/Engineering-Work/) is published by the repository's deployment workflow. The [original review portfolio](https://vincent-cook-engineering.san-jose-sta-2217.chatgpt.site/) is hosted separately.

## Portfolio contents

The website features seventeen project and coursework entries, work experience, and a searchable library of 41 SJSU course and requirement references.

Engineering projects include FIRST Robotics Team 3925 circuitry design, battery testing, and circuit repairs, SJSU Robotics, an SAE Spartan Racing electric motor test bench, BROADSWORD Inventor landing-leg CAD and rocket-stage liftoff/landing trajectory programming (August-December 2023), an ongoing hybrid electric/hydrogen aircraft senior project, and the NASA L’SPACE Mission Concept Academy.

Work experience includes a guest representative role at PayPal Stadium during the 2026 soccer season, working San José Earthquakes and Bay FC women’s matches.

Confirmed coursework includes ENGR 10 wind-tunnel design and a programmed class robot; AE 20 V6 piston-engine CAD and paper schematics in Inventor; AE 30 missile trajectory coding; AE 112 structural laboratory calculations; AE 114 structural and material behavior; AE 138 MotionGenesis multibody orbital mechanics and disc trajectories; AE 140 MATLAB Frisbee dynamics with external variables and moments of inertia; AE 157 Simulink controls; and AE 160/162 open wind-tunnel aerodynamic data and Navier-Stokes coursework.

Athletics include SJSU Division I club Ultimate Frisbee since 2022, team gym and conditioning coordination, and SJSU club swimming with a Cal-hosted meet in spring 2026. Swimming is listed as club participation.

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

The course references remain readable without JavaScript. Replace resume files under the same names when updating them.

## Publish updates

Push changes to `main`. The [Pages deployment workflow](.github/workflows/pages.yml) uploads `dist/` and publishes it automatically after a successful run. Deployment progress is available under the repository's **Actions** tab. The workflow can also be run manually from that tab.

GitHub Pages is configured with **Settings → Pages → Source: GitHub Actions**. The original review portfolio is hosted separately and does not update from this workflow.
