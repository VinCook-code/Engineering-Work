# Vincent T. Cook — Engineering Portfolio

[Live portfolio](https://vincook-code.github.io/Engineering-Work/)

A dark, responsive portfolio for an Aerospace Engineering student at San José State University, with graduation expected in May 2027.

## Content

- Six technical projects and engineering-team experiences.
- Eleven confirmed projects in **Applied in the classroom**.
- Five work experiences and three organizations.
- Three supplied résumé PDFs: main, robotics, and manufacturing.

Project and experience descriptions come from Vincent's supplied **List of Projects & Experiences** document. The detailed experience dates take precedence over its duplicated extracurricular recap. Classroom descriptions use his previously confirmed project notes. The earlier Technical foundations reference library has been removed.

The supplied résumé PDFs are published unchanged. Obsolete Word, text, and earlier résumé versions are no longer linked or published.

## Files and editing

| File | Purpose |
| --- | --- |
| `content/portfolio.json` | Project descriptions, dates, classroom work, skills, and résumé metadata |
| `tools/build_portfolio.py` | Generates static HTML from that content; Python standard library only |
| `dist/index.html` | Generated accessible portfolio page |
| `dist/styles.css` | Dark theme, responsive layouts, and CSS animations |
| `dist/app.js` | Project filters, navigation, reveal effects, and motion preference |
| `dist/downloads/` | The three supplied PDF résumés |

After editing the content, run:

```sh
python tools/build_portfolio.py
python -m http.server 8000 --directory dist
```

Open `http://localhost:8000`. No Node dependencies or framework build are needed. Google Fonts has system-font fallbacks.

## Accessibility and motion

Content and résumé links remain available without JavaScript. Native disclosures expose additional descriptions and classroom projects. The design includes keyboard focus indicators, mobile navigation, project filters with an accessible result count, once-only scroll reveals, and a decorative SVG diagram. Motion respects the operating system's reduced-motion preference and can also be switched off in the footer.

## Publishing

Push to `main`. The [Pages workflow](.github/workflows/pages.yml) publishes `dist/` to the existing GitHub Pages address. The older ChatGPT-hosted review copy is a separate website and does not update through this repository.
