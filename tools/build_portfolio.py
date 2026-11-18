"""Build the static portfolio from Vincent's source descriptions. Standard library only."""
from pathlib import Path
from html import escape as e
import json
import re

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'content/portfolio.json').read_text(encoding='utf-8'))
ARROW = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 19 19 5M5 5h14v14"/></svg>'
DOWN = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3v12m-5-5 5 5 5-5M5 16v5h14v-5"/></svg>'
PLUS = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10h12M10 4v12"/></svg>'

def dates(value):
    return e(re.sub(r'\s*-\s*', ' – ', value))

def bullets(values, visible=2):
    first = '<ul class="source-bullets">'+''.join('<li>'+e(text)+'</li>' for text in values[:visible])+'</ul>'
    if len(values)>visible:
        first += '<details class="more-description"><summary>Full description '+PLUS+'</summary><ul class="source-bullets">'+''.join('<li>'+e(text)+'</li>' for text in values[visible:])+'</ul></details>'
    return first

def tags(values):
    return '<div class="tags">'+''.join('<span>'+e(text)+'</span>' for text in values)+'</div>'

projects=[]
for index,p in enumerate(data['projects'],1):
    projects.append(f'''<article class="project-row reveal" data-project-card data-category="{e(p['category'])}">
      <div class="project-meta"><span class="index">{index:02}</span><p>{dates(p['dates'])}</p><p>{e(p['location'])}</p></div>
      <div class="project-copy"><div class="project-heading"><h3>{e(p['name'])}</h3>{'<span class="current-label"><i></i>Current project</span>' if index==1 else ''}</div><p class="role">{e(p['role'])}</p>{bullets(p['bullets'])}{tags(p['tags'])}</div>
    </article>''')

classroom=[]
for p in data['classroom']:
    classroom.append(f'''<details class="classroom-card reveal"><summary><span class="course-code">{e(p['code'])}</span><h3>{e(p['title'])}</h3>{PLUS}</summary><div class="classroom-body"><p>{e(p['description'])}</p>{tags(p['tools'])}</div></details>''')

work=[]
for p in data['work']:
    name='PayPal Park' if p['name']=='Paypal Park' else p['name']
    work.append(f'''<article class="experience-row reveal"><div class="experience-meta"><p>{dates(p['dates'])}</p><p>{e(p['location'])}</p></div><div class="experience-copy"><h3>{e(name)}</h3><p class="role">{e(p['role'])}</p>{bullets(p['bullets'])}</div></article>''')

organizations=[]
for p in data['organizations']:
    name='SJSU Club Swim Team' if p['name']=='SJSU Swim Team' else p['name']
    organizations.append(f'''<article class="organization reveal"><p class="mono">{dates(p['dates'])}</p><h3>{e(name)}</h3><p class="role">{e(p['role'])}</p>{bullets(p['bullets'],2)}</article>''')

resumes=[]
for index,p in enumerate(data['resumes'],1):
    link='downloads/'+p['filename']+'?v=20261117'
    resumes.append(f'''<article class="resume-card reveal"><div class="resume-card-top"><span class="index">0{index}</span><span class="file-type">PDF / 1 PAGE</span></div><p class="resume-label">{e(p['label'])}</p><h3>{e(p['name'])}</h3><div class="resume-actions"><a class="button {'button-light' if index==1 else 'button-outline'}" href="{link}" download aria-label="Download {e(p['name'])} PDF">Download PDF {DOWN}</a><a class="preview-link" href="{link}" target="_blank" rel="noopener noreferrer" aria-label="View {e(p['name'])} PDF">View {ARROW}</a></div></article>''')

main_resume='downloads/'+data['resumes'][0]['filename']+'?v=20261117'
page=f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0b0d10"><meta name="color-scheme" content="dark">
  <title>Vincent T. Cook — Aerospace Engineering</title>
  <meta name="description" content="Vincent T. Cook, Aerospace Engineering at San José State University. Technical projects, classroom work, professional experience, and résumé downloads.">
  <link rel="icon" href="assets/monogram.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css?v=20261117">
  <script src="app.js?v=20261117" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner">
  <a class="wordmark" href="#main" aria-label="Vincent Cook home"><span class="monogram">VC<span class="wordmark-dot">.</span></span><span class="wordmark-name">VINCENT COOK</span></a>
  <button class="menu-toggle" data-menu-toggle aria-controls="site-nav" aria-expanded="false" aria-label="Open navigation"><span></span><span></span></button>
  <nav id="site-nav" aria-label="Main navigation"><a href="#projects" data-nav-link>Projects</a><a href="#classroom" data-nav-link>Classroom</a><a href="#experience" data-nav-link>Experience</a><a href="#resumes" data-nav-link>Résumés</a><a class="nav-contact" href="mailto:Vincent.Tait.Cook@gmail.com">Get in touch {ARROW}</a></nav>
</div></header>
<main id="main">
<section class="hero wrap" aria-labelledby="hero-title">
  <div class="hero-copy"><p class="eyebrow hero-intro">ENGINEERING PORTFOLIO <span>/</span> SAN JOSÉ, CA</p><h1 id="hero-title">Vincent<br><span>T. Cook</span><span class="name-dot">.</span></h1><p class="hero-degree">Aerospace Engineering</p><p class="hero-school">San José State University <span>·</span> Class of 2027</p><div class="hero-actions"><a class="button button-light" href="#projects">Explore projects <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 4v16m-6-6 6 6 6-6"/></svg></a><a class="text-link" href="{main_resume}" target="_blank" rel="noopener noreferrer">Main résumé {ARROW}</a></div><div class="hero-focus"><span>Mechanical design</span><span>Robotics</span><span>Manufacturing</span></div></div>
  <div class="hero-visual" aria-hidden="true"><div class="diagram-corner corner-top"></div><div class="diagram-corner corner-bottom"></div><svg class="engineering-diagram" viewBox="0 0 520 520" fill="none">
    <defs><linearGradient id="wing-fill" x1="80" y1="150" x2="430" y2="370" gradientUnits="userSpaceOnUse"><stop stop-color="#acd4ff" stop-opacity=".13"/><stop offset="1" stop-color="#acd4ff" stop-opacity=".01"/></linearGradient></defs>
    <g class="diagram-grid" stroke="currentColor" stroke-opacity=".12"><path d="M60 100h400M60 180h400M60 260h400M60 340h400M60 420h400M100 60v400M180 60v400M260 60v400M340 60v400M420 60v400"/></g>
    <g class="diagram-orbit" stroke="currentColor"><circle cx="260" cy="260" r="193" stroke-opacity=".13"/><circle cx="260" cy="260" r="176" stroke-opacity=".08" stroke-dasharray="2 11"/><path d="M260 60v14M460 260h-14M260 460v-14M60 260h14" stroke-opacity=".5"/><circle cx="260" cy="67" r="4" fill="currentColor" stroke="none"/></g>
    <g class="diagram-wing"><path d="M99 280C154 221 245 206 424 266L316 327C208 308 147 301 99 280Z" fill="url(#wing-fill)" stroke="currentColor" stroke-opacity=".72" stroke-width="1.4"/><path d="M99 280 206 219C261 160 352 145 424 266M206 219C254 240 315 247 424 266M99 280C166 267 247 268 424 266M153 249C201 270 262 277 370 296M206 219 99 280M260 215 153 276M316 226 209 287M370 245 263 306" stroke="currentColor" stroke-opacity=".45" stroke-width="1"/><path d="M102 353h324M102 345v16M426 345v16M115 353l8-3m-8 3 8 3m289-3-8-3m8 3-8 3" stroke="currentColor" stroke-opacity=".35"/><path class="flow-line" d="M62 205C175 122 351 125 458 209M66 321C181 387 353 380 456 318" stroke="currentColor" stroke-opacity=".3" stroke-dasharray="5 9"/></g>
    <g stroke="currentColor" stroke-opacity=".55"><path d="M115 420h40m-40 0v-40m0 40 22 18"/><path d="m155 420-5-3m5 3-5 3m-35-43-3 5m3-5 3 5"/></g><g fill="currentColor" fill-opacity=".55" font-family="monospace" font-size="10"><text x="161" y="424">X</text><text x="111" y="373">Y</text><text x="140" y="449">Z</text></g>
  </svg><div class="diagram-caption"><span>CAD / SIMULATION / CONTROLS</span><span class="diagram-signal"><i></i> AEROSPACE</span></div></div>
  <a class="scroll-cue" href="#projects"><span>SCROLL TO EXPLORE</span><span>↓</span></a>
</section>
<div class="skills-strip" aria-label="Engineering tools"><div class="wrap"><span class="skills-label">TOOLS &amp; SKILLS</span><div>{''.join('<span>'+e(skill)+'</span>' for skill in data['skills'])}</div></div></div>
<section class="section wrap" id="projects" aria-labelledby="projects-title"><div class="section-heading reveal"><div><p class="eyebrow">01 / TECHNICAL EXPERIENCE</p><h2 id="projects-title">Engineering projects<span>.</span></h2></div><p>Design, build, and engineering team experience.</p></div>
  <div class="project-toolbar reveal"><div class="project-filters" role="group" aria-label="Filter engineering projects"><button data-project-filter="all" aria-pressed="true">All projects</button><button data-project-filter="aerospace" aria-pressed="false">Aerospace</button><button data-project-filter="robotics" aria-pressed="false">Robotics</button><button data-project-filter="manufacturing" aria-pressed="false">Manufacturing</button></div><p class="project-count" data-project-count role="status" aria-live="polite">6 projects</p></div>
  <div class="project-list">{''.join(projects)}</div>
</section>
<section class="classroom-section" id="classroom" aria-labelledby="classroom-title"><div class="wrap section"><div class="section-heading reveal"><div><p class="eyebrow">02 / COURSE PROJECTS</p><h2 id="classroom-title">Applied in the classroom<span>.</span></h2></div><p>CAD, dynamics, controls, and aerodynamic testing.</p></div><div class="classroom-grid">{''.join(classroom)}</div></div></section>
<section class="section wrap" id="experience" aria-labelledby="experience-title"><div class="section-heading reveal"><div><p class="eyebrow">03 / WORK &amp; LEADERSHIP</p><h2 id="experience-title">Experience<span>.</span></h2></div><p>Work, instruction, and team responsibilities.</p></div><div class="experience-list">{''.join(work)}</div>
  <div class="organizations-heading reveal"><p class="eyebrow">OUTSIDE THE LAB</p><h2>Organizations &amp; leadership<span>.</span></h2></div><div class="organizations-grid">{''.join(organizations)}</div>
</section>
<section class="resume-section" id="resumes" aria-labelledby="resumes-title"><div class="wrap section"><div class="section-heading reveal"><div><p class="eyebrow">04 / DOWNLOADS</p><h2 id="resumes-title">Résumés<span>.</span></h2></div><p>Main résumé and two focused versions.</p></div><div class="resume-grid">{''.join(resumes)}</div></div></section>
<section class="contact-section wrap reveal" aria-labelledby="contact-title"><p class="eyebrow">CONTACT</p><div class="contact-line"><h2 id="contact-title">Get in touch<span>.</span></h2><a href="mailto:Vincent.Tait.Cook@gmail.com">Vincent.Tait.Cook@gmail.com {ARROW}</a></div><div class="contact-links"><a href="https://www.linkedin.com/in/vincent-cook-080790227/" target="_blank" rel="noopener noreferrer">LinkedIn {ARROW}</a><a href="https://github.com/VinCook-code" target="_blank" rel="noopener noreferrer">GitHub {ARROW}</a></div></section>
</main>
<footer class="site-footer wrap"><p>Vincent T. Cook <span>·</span> Aerospace Engineering <span>·</span> SJSU</p><button data-motion-toggle type="button" aria-pressed="false"><span class="motion-icon" aria-hidden="true">◌</span><span data-motion-label>Motion on</span></button><a href="#main">Back to top ↑</a></footer>
</body></html>'''
(ROOT/'dist/index.html').write_text(page,encoding='utf-8',newline='\n')
print('Built portfolio: 6 technical projects, 11 classroom projects, 5 work entries, 3 organizations, 3 resumes.')
