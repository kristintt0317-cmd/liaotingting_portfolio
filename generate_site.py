from pathlib import Path
import zipfile, textwrap, os

root = Path('/mnt/data/multipage_portfolio')
css_dir = root / 'css'
js_dir = root / 'js'
assets = root / 'assets' / 'pages'
css_dir.mkdir(exist_ok=True)
js_dir.mkdir(exist_ok=True)

style = r'''
:root{
  --bg:#f4f0ea;
  --paper:#fbf8f3;
  --ink:#161616;
  --muted:#5d5d5d;
  --line:rgba(0,0,0,.08);
  --shadow:0 24px 70px rgba(0,0,0,.08);
  --radius:28px;
  --max:1280px;
  --accent:#f78a35;
  --accent-soft:rgba(247,138,53,.12);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:
    radial-gradient(circle at top left, var(--accent-soft), transparent 28%),
    linear-gradient(180deg, #f7f2ec 0%, #f2eee8 100%);
  color:var(--ink);
  line-height:1.6;
}
body.project-page{background:
    radial-gradient(circle at top left, var(--accent-soft), transparent 26%),
    radial-gradient(circle at top right, rgba(255,255,255,.5), transparent 32%),
    linear-gradient(180deg, #f7f2ec 0%, #f2eee8 100%);
}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.wrap{width:min(calc(100% - 40px), var(--max)); margin:0 auto}
.topbar{position:sticky;top:0;z-index:50;backdrop-filter: blur(14px);background:rgba(247,242,236,.76);border-bottom:1px solid rgba(0,0,0,.05)}
.nav{display:flex;align-items:center;justify-content:space-between;min-height:76px;gap:18px}
.brand{display:flex;align-items:center;gap:14px;font-weight:700;letter-spacing:.02em}
.brand-mark{width:42px;height:42px;border-radius:14px;background:linear-gradient(135deg,var(--accent),#8bbd72);box-shadow:0 10px 24px rgba(0,0,0,.12)}
.nav-links{display:flex;gap:20px;flex-wrap:wrap;color:var(--muted);font-size:.95rem}
.nav-links a:hover{color:var(--ink)}
.hero{padding:74px 0 58px}
.hero-grid{display:grid;grid-template-columns:1.08fr .92fr;gap:34px;align-items:end}
.eyebrow,.chip{display:inline-flex;align-items:center;gap:10px;padding:10px 14px;border-radius:999px;border:1px solid var(--line);background:rgba(255,255,255,.58);color:#3d3d3d;font-size:.88rem}
.dot{width:9px;height:9px;border-radius:999px;background:var(--accent)}
h1{margin:18px 0 16px;font-size:clamp(3rem,7vw,6.6rem);line-height:.92;letter-spacing:-.06em;max-width:8ch}
.hero p{font-size:1.05rem;color:var(--muted);max-width:60ch;margin:0}
.hero-actions,.inline-actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:26px}
.button{display:inline-flex;align-items:center;gap:10px;padding:14px 18px;border-radius:999px;font-weight:600;border:1px solid transparent;transition:.25s ease}
.button.primary{background:var(--ink);color:white;box-shadow:var(--shadow)}
.button.secondary{border-color:var(--line);background:rgba(255,255,255,.58)}
.button:hover{transform:translateY(-1px)}
.hero-visual,.card-surface{position:relative;border-radius:36px;overflow:hidden;box-shadow:var(--shadow);background:#e8e2d8}
.hero-visual{min-height:620px}
.hero-visual img,.project-cover img,.gallery-grid img,.overview-card img,.other-work img,.mini-grid img,.side-image img{width:100%;height:100%;object-fit:cover}
.floating-card{position:absolute;left:22px;right:22px;bottom:22px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;background:rgba(251,248,243,.9);backdrop-filter: blur(16px);border:1px solid rgba(255,255,255,.5);border-radius:24px;padding:14px;box-shadow:0 14px 40px rgba(0,0,0,.12)}
.floating-card strong{display:block;font-size:1rem}.floating-card span{font-size:.8rem;color:var(--muted)}
.section{padding:26px 0 92px}
.section-head{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:26px}
.section-title{font-size:clamp(1.9rem,3vw,3rem);line-height:1;letter-spacing:-.04em;margin:0}
.section-note{color:var(--muted);max-width:50ch}
.intro-panels,.overview-grid,.stats-grid,.project-grid,.case-grid,.dual-grid,.mini-grid{display:grid;gap:18px}
.intro-panels,.dual-grid{grid-template-columns:1fr 1fr}
.panel,.overview-card,.other-work,.content-card,.stat-card{padding:28px;border-radius:28px;background:rgba(255,255,255,.66);border:1px solid var(--line);box-shadow:var(--shadow)}
.panel h3,.content-card h3{margin:0 0 10px;font-size:1rem;text-transform:uppercase;letter-spacing:.12em;color:#5d5d5d}
.panel p,.content-card p,.content-card li,.stat-card p{margin:0;color:#343434}
.projects{display:grid;gap:26px}
.project-card{display:grid;grid-template-columns:1.08fr .92fr;gap:0;overflow:hidden;border-radius:34px;background:var(--paper);box-shadow:var(--shadow);border:1px solid rgba(0,0,0,.06)}
.project-card.reverse{grid-template-columns:.92fr 1.08fr}
.project-card.reverse .project-image{order:2}.project-card.reverse .project-info{order:1}
.project-image{min-height:560px;position:relative;background:#e8e0d5}
.project-info{padding:34px 32px 30px;display:flex;flex-direction:column;justify-content:space-between}
.project-number{font-size:.9rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#666;margin-bottom:12px}
.project-title{font-size:clamp(2.2rem,4vw,4rem);line-height:.95;letter-spacing:-.05em;margin:0 0 14px}
.project-summary{color:var(--muted);font-size:1rem;margin-bottom:20px}
.meta-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px 18px;margin:24px 0;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.meta-item small{display:block;text-transform:uppercase;letter-spacing:.12em;color:#777;font-size:.74rem;margin-bottom:6px}
.meta-item strong{font-size:.98rem;font-weight:600}
.tags{display:flex;flex-wrap:wrap;gap:10px}.tag{padding:9px 12px;border-radius:999px;border:1px solid var(--line);background:rgba(255,255,255,.7);font-size:.86rem;color:#454545}
.icon-link{display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:999px;background:var(--accent);color:white;font-size:1.1rem;box-shadow:0 10px 24px rgba(0,0,0,.12)}
.icon-link.small{width:44px;height:44px}
.gallery-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.gallery-grid figure,.overview-card.figure{margin:0;border-radius:24px;overflow:hidden;background:white;border:1px solid var(--line);box-shadow:0 14px 30px rgba(0,0,0,.06)}
.gallery-grid img{aspect-ratio:3/4;cursor:pointer;transition:transform .35s ease}
.gallery-grid figure:hover img,.clickable:hover img{transform:scale(1.02)}
.gallery-grid figcaption,.overview-card .caption{padding:12px 14px 15px;color:#4f4f4f;font-size:.9rem;background:rgba(255,255,255,.78)}
.other-works{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.other-work{padding:0;overflow:hidden}.other-work .copy{padding:18px}.other-work h4{margin:0 0 8px;font-size:1.4rem;line-height:1}.other-work p{margin:0;color:var(--muted)}
.footer-card{padding:28px;border-radius:30px;background:rgba(255,255,255,.66);border:1px solid var(--line);display:flex;justify-content:space-between;gap:24px;align-items:flex-end;box-shadow:var(--shadow)}
.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s ease, transform .7s ease}.reveal.visible{opacity:1;transform:translateY(0)}
.lightbox{position:fixed;inset:0;background:rgba(15,15,15,.86);display:none;align-items:center;justify-content:center;padding:24px;z-index:100}.lightbox.open{display:flex}.lightbox img{max-width:min(1400px,96vw);max-height:92vh;border-radius:18px;box-shadow:0 20px 80px rgba(0,0,0,.35)}.lightbox button{position:absolute;top:18px;right:18px;width:48px;height:48px;border-radius:999px;border:none;background:rgba(255,255,255,.12);color:white;font-size:1.3rem;cursor:pointer}
.project-hero{padding:64px 0 46px}.project-layout{display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:end}
.project-cover{border-radius:34px;overflow:hidden;min-height:560px;box-shadow:var(--shadow);border:1px solid var(--line)}
.kicker{font-size:.92rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#666;margin-bottom:10px}
.lead{font-size:1.06rem;color:var(--muted);max-width:62ch}
.overview-grid{grid-template-columns:1.2fr .8fr}.overview-card.figure img{aspect-ratio:4/3}
.case-grid{grid-template-columns:1fr 1fr 1fr}.content-card ul{padding-left:20px;margin:0}.content-card li+li{margin-top:8px}
.side-image{border-radius:24px;overflow:hidden;min-height:260px;border:1px solid var(--line);box-shadow:var(--shadow)}
.stat-card strong{display:block;font-size:2rem;line-height:1;margin-bottom:8px}
.back-row{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:24px}
.next-project{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:999px;background:rgba(255,255,255,.64);border:1px solid var(--line)}
.small-note{font-size:.92rem;color:var(--muted)}
@media (max-width:1080px){
  .hero-grid,.project-card,.project-card.reverse,.project-layout,.overview-grid,.case-grid{grid-template-columns:1fr}
  .project-card.reverse .project-image,.project-card.reverse .project-info{order:initial}
  .intro-panels,.other-works,.gallery-grid,.dual-grid,.mini-grid{grid-template-columns:1fr 1fr}
  .hero-visual,.project-cover{min-height:460px}
}
@media (max-width:720px){
  .wrap{width:min(calc(100% - 24px), var(--max))}
  .nav{padding:8px 0}.nav-links{display:none}
  h1{max-width:none}.hero{padding:40px 0 32px}.hero-visual,.project-cover{min-height:340px}
  .floating-card{grid-template-columns:1fr}.panel,.project-info,.content-card,.overview-card,.stat-card{padding:22px}
  .intro-panels,.gallery-grid,.other-works,.dual-grid,.mini-grid,.stats-grid{grid-template-columns:1fr}
  .footer-card,.section-head,.back-row{flex-direction:column;align-items:flex-start}
}
'''

script = r'''
const observer = new IntersectionObserver((entries)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {threshold: .12});

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightboxImage');
const closeLightbox = document.getElementById('closeLightbox');
if(lightbox && lightboxImage && closeLightbox){
  document.querySelectorAll('[data-full]').forEach(img=>{
    img.addEventListener('click', ()=>{
      lightboxImage.src = img.dataset.full;
      lightbox.classList.add('open');
      lightbox.setAttribute('aria-hidden', 'false');
    });
  });
  function closeBox(){
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
    lightboxImage.src = '';
  }
  closeLightbox.addEventListener('click', closeBox);
  lightbox.addEventListener('click', (e)=>{ if(e.target === lightbox) closeBox(); });
  document.addEventListener('keydown', (e)=>{ if(e.key === 'Escape') closeBox(); });
}
'''

(css_dir / 'style.css').write_text(style, encoding='utf-8')
(js_dir / 'main.js').write_text(script, encoding='utf-8')

projects = [
    {
        'slug':'furever','title':'Furever','num':'Project 01','accent':'#f78a35','soft':'rgba(247,138,53,.14)',
        'eyebrow':'Service Design · Participatory Design · Interaction Design',
        'summary':'Reframing stray-dog adoption as an empathic, supported journey through offline engagement and a digital service ecosystem.',
        'duration':'10 weeks · Apr 2024','type':'Individual Project','deliverables':'Interactive wall · Adoption platform · Matching flow','cover':'page-03.jpg',
        'meta2':'China stray-dog adoption',
        'chips':['Empathy system','Adoption journey','Interactive wall','Community platform'],
        'problem':'The project focuses on abandonment caused by lack of understanding, mismatch between adopters and dogs, and a fragmented adoption experience with limited post-adoption support.',
        'approach':'Inspired by theatre and script table reads, the service uses story-based public engagement to let potential adopters emotionally rehearse the first 30 days of adoption before they commit.',
        'sections':[
            ('Background', 'Research in the portfolio identifies the scale of stray-dog issues, abandonment as a major source, and the need to shift from simple promotion to deeper adopter understanding. The project positions adoption not as a one-time transaction but as a supported relationship.'),
            ('Research & Insight', 'Field research, interviews with rescue staff, volunteers, and adopters, plus observations on adoption day, surfaced three recurring needs: a transparent platform, better guidance for first-time adopters, and smarter matching between dog personalities and adopter circumstances.'),
            ('Concept', 'The core concept compares adoption to theatre. Staff, dogs, adopters, and public audiences become analogous to cast, characters, and viewers. This allows the service to build empathy through narrative, role transition, and staged exposure to responsibilities.'),
            ('Outcome', 'The final proposal combines an offline interactive wall for story-led education with an online platform featuring matching, simulated adoption, community exchange, and parenting records. Together they reduce uncertainty and build continuity after adoption.')
        ],
        'stats':[('30-day','adaptation period framed as a key emotional window'),('2-part','service combining offline event and online platform'),('multi-role','adopters, volunteers, managers, and halfway houses linked in one system')],
        'gallery':['page-04.jpg','page-05.jpg','page-06.jpg','page-07.jpg','page-08.jpg'],
        'captions':['Empathy framing and user research','Theatre-inspired system concept','Interactive wall prototyping and threshold testing','Platform structure, wireframes, and service map','Validation, interface language, and final summary'],
        'next':'endo.html'
    },
    {
        'slug':'endo','title':'40 × 40 EnDo','num':'Project 02','accent':'#6cc55f','soft':'rgba(108,197,95,.14)',
        'eyebrow':'Participatory Design · Service Design · Application Design',
        'summary':'A modular study-space system that turns urban leftovers into flexible learning environments while collecting user insight for future planning.',
        'duration':'8 weeks · Nov 2024','type':'Individual Project','deliverables':'Mini program · Box simulation · Workshop · Service blueprint','cover':'page-09.jpg',
        'meta2':'Urban study-space participation',
        'chips':['Study space','Modular box','Mini program','Workshop research'],
        'problem':'Study needs increasingly spill beyond classrooms and libraries, yet existing spaces are often expensive, inflexible, or mismatched to different learning styles, sound tolerance, and storage or charging needs.',
        'approach':'The project uses 40 cm modular cardboard boxes as the smallest spatial unit. Users can simulate, reserve, and build their own space configurations, while the system accumulates preference data for future urban resource planning.',
        'sections':[
            ('Background', 'The project starts from the shortage and mismatch of study spaces in cities. Research traces both the rise of paid study rooms and the limitations of free ones, especially in relation to distance, light, privacy, power access, and flexibility.'),
            ('Research & Participation', 'Questionnaires, interviews, personas, case studies, and a co-design workshop were used to understand learning modes such as independent, collaborative, and diverse patterns. The workshop helped participants build and draw their own study spaces using box modules.'),
            ('Concept', '“EnDo” means “box” in local dialect. The concept turns the box into both a spatial building block and a participatory interface. Through booking, simulation, and feedback, the mini program becomes a bridge between individual habits and urban planning data.'),
            ('Outcome', 'The design includes a mini-program flow for location search, box booking, simulation construction, and personal settings. A service blueprint shows how user behaviour, merchant cooperation, backend support, and data feedback work together as a system.')
        ],
        'stats':[('40×40 cm','module size chosen after prototyping'),('8 boxes','average per participant in workshop outputs'),('online + offline','digital reservation linked with physical assembly')],
        'gallery':['page-10.jpg','page-11.jpg','page-12.jpg','page-13.jpg','page-14.jpg'],
        'captions':['Study-space history, market growth, and need framing','Questionnaires, personas, and learning-mode insights','Co-design workshop tools and outcomes','Mini program interface and box-reservation flow','Service blueprint and space-engagement scenario'],
        'next':'touch-emoji.html'
    },
    {
        'slug':'touch-emoji','title':'“Touch” Emoji','num':'Project 03','accent':'#f3c94b','soft':'rgba(243,201,75,.18)',
        'eyebrow':'Interaction Design · Product Design · Disability Design',
        'summary':'A tactile and magnetic emoji system that helps visually impaired users understand, receive, and send emojis through touch and sound.',
        'duration':'28 weeks · Dec 2023','type':'Individual Project','deliverables':'Magnetic device · 3D emoji set · Game concept','cover':'page-15.jpg',
        'meta2':'Accessible social expression',
        'chips':['Accessibility','Emoji understanding','Tactile interface','Inclusive design'],
        'problem':'Visually impaired users often encounter ambiguity, slow search processes, and partial screen-reader limitations when emojis appear in chats. Social expression becomes difficult precisely where nuance and context matter most.',
        'approach':'The project translates emoji meaning into textured, tactile forms and combines them with a magnetic device, spoken prompts, and game-based learning to reduce ambiguity and increase speed of use.',
        'sections':[
            ('Background', 'The project begins with broader information-accessibility challenges in China and then narrows to online social interaction. Interviews show that visually impaired users do chat socially online, but emojis remain difficult to interpret quickly and consistently.'),
            ('Research & Insight', 'Offline and online interviews, app comparison, and workshops revealed a key gap: ordinary users rely on visual memory and context, while visually impaired users often receive literal voice output without reliable social meaning. The same emoji can carry multiple meanings.'),
            ('Concept', 'TOUCH introduces a magnetic device with tactile 3D emojis. Positive and negative emotional tendencies are reflected in material texture, while receiving, identifying, and selecting emojis becomes a more embodied interaction. A supporting game deepens familiarity and confidence.'),
            ('Outcome', 'The final design includes the device, emoji pieces, packaging, a manual, and a social board-game format. It positions accessibility not only as assistive function but as richer participation in emotional communication.')
        ],
        'stats':[('16','emojis tested in workshop sorting'),('3 modes','identify, receive, and send emoji'),('1 device','combining tactile, magnetic, and audio interaction')],
        'gallery':['page-16.jpg','page-17.jpg','page-18.jpg','page-19.jpg','page-20.jpg'],
        'captions':['Accessibility research, interviews, and current products','Workshop insights, ambiguity, and tactile direction','Sketching, magnetic device, and game design','Product details, textures, and packaging','Storyboard and value proposition canvas'],
        'next':'living-soil.html'
    },
    {
        'slug':'living-soil','title':'Living Soil','num':'Project 04','accent':'#8f9a74','soft':'rgba(143,154,116,.18)',
        'eyebrow':'Service Design · Biomaterial Design · System Design',
        'summary':'A compost-based system connecting wet-waste reuse, soil quality, butterfly habitats, and environmental education through biodegradable touchpoints.',
        'duration':'24 weeks · Oct 2024','type':'Individual Project','deliverables':'Compost bin · Material recipe · Posters · QR instruction flow','cover':'page-21.jpg',
        'meta2':'Soil biodiversity and education',
        'chips':['Biomaterial','Compost system','Butterfly habitat','School engagement'],
        'problem':'Butterfly decline is linked to habitat loss, soil degradation, vegetation reduction, and human activities. The project asks how a small, understandable intervention can reconnect communities with soil biodiversity.',
        'approach':'Using a biodegradable compost bin as a public touchpoint, the system invites communities and schoolchildren to collect wet waste, produce fertiliser, and indirectly support healthier vegetation and butterfly habitats.',
        'sections':[
            ('Background', 'The project traces butterfly decline in Europe, North America, and Shanghai, then maps how food webs, soil organisms, vegetation, and arthropods are interconnected. Rather than treating butterflies in isolation, the project looks at the soil network beneath them.'),
            ('Research & System Insight', 'By examining urban planting choices and the effects of pesticides, monoculture, vegetation loss, and soil cracking, the project identifies soil quality as a leverage point. Intervention therefore shifts from awareness only to a practical composting system.'),
            ('Concept', 'The design uses a straw-based compost container that biodegrades along with the food waste it holds. The making process, instructions, and QR-linked guidance turn the object into both a functional container and an educational medium.'),
            ('Outcome', 'The final system includes material proportions, fabrication steps, physical posters, QR instructions, and school testing. The proposal suggests rollout through communities and primary-school practical activities to foster ecological attention through action.')
        ],
        'stats':[('15–23 days','natural fermentation window in the concept'),('9 steps','documented material-making process'),('community + school','two key participation settings')],
        'gallery':['page-22.jpg','page-23.jpg','page-24.jpg','page-25.jpg','page-26.jpg'],
        'captions':['Ecological threats and urban vegetation mismatch','System logic connecting soil, plants, and butterflies','Material recipe and fabrication process','User testing and educational opportunity','Final design, posters, and instruction rollout'],
        'next':'index.html'
    }
]

home = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tingting Liao – Design Portfolio</title>
  <meta name="description" content="A multi-page design portfolio featuring service design, interaction design, product design, and system thinking." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="topbar">
    <div class="wrap nav">
      <a class="brand" href="index.html"><span class="brand-mark"></span><span>Tingting Liao</span></a>
      <nav class="nav-links">
        <a href="#selected">Selected Work</a>
        <a href="#gallery">Visual Archive</a>
        <a href="#others">Other Work</a>
        <a href="#about">About</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="wrap hero-grid">
        <div class="reveal">
          <span class="eyebrow"><span class="dot"></span> Multi-page portfolio · Editorial layout · Project case studies</span>
          <h1>Designing systems, stories, and tactile experiences.</h1>
          <p>
            This version restructures the portfolio into a multi-page website. The home page offers a visual overview of the work, and each project opens into its own case-study page with richer detail, process, and project imagery.
          </p>
          <div class="hero-actions">
            <a class="button primary" href="#selected">View projects</a>
            <a class="button secondary" href="#gallery">Browse archive</a>
          </div>
        </div>
        <div class="hero-visual reveal">
          <img src="assets/pages/page-01.jpg" alt="Portfolio cover" />
          <div class="floating-card">
            <div><strong>04</strong><span>Main case studies</span></div>
            <div><strong>Multi-page</strong><span>Home + individual project pages</span></div>
            <div><strong>Visual-first</strong><span>Style derived from the original portfolio</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="about">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Approach</p>
            <h2 class="section-title">A portfolio site with individual case-study pages.</h2>
          </div>
          <p class="section-note">
            The visual style extends the existing HTML direction while making the structure more practical: the home page functions like a curated index, and each project icon opens a dedicated project page.
          </p>
        </div>
        <div class="intro-panels">
          <article class="panel reveal">
            <h3>Focus</h3>
            <p>Service design, participatory design, interaction design, product thinking, inclusive design, and biomaterial systems are woven throughout the portfolio.</p>
          </article>
          <article class="panel reveal">
            <h3>How to use</h3>
            <p>Click the arrow icon or the “Open project” button on any project card to view its full project page. Each project page includes overview, process, selected imagery, and a path to the next project.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="selected">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Selected work</p>
            <h2 class="section-title">Project overview.</h2>
          </div>
          <p class="section-note">The cards below stay concise on purpose. They work as entry points into longer multi-page project stories.</p>
        </div>
        <div class="projects">
'''

for idx,p in enumerate(projects):
    reverse = ' reverse' if idx % 2 else ''
    home += f'''
          <article class="project-card{reverse} reveal" style="--accent:{p['accent']};--accent-soft:{p['soft']}">
            <div class="project-image">
              <img src="assets/pages/{p['gallery'][-1]}" alt="{p['title']} preview" />
            </div>
            <div class="project-info">
              <div>
                <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:14px">
                  <div>
                    <p class="project-number">{p['num']}</p>
                    <h3 class="project-title">{p['title']}</h3>
                  </div>
                  <a class="icon-link" href="{p['slug']}.html" aria-label="Open {p['title']}">↗</a>
                </div>
                <p class="project-summary">{p['summary']}</p>
                <div class="meta-grid">
                  <div class="meta-item"><small>Type</small><strong>{p['type']}</strong></div>
                  <div class="meta-item"><small>Duration</small><strong>{p['duration']}</strong></div>
                  <div class="meta-item"><small>Focus</small><strong>{p['eyebrow']}</strong></div>
                  <div class="meta-item"><small>Deliverables</small><strong>{p['deliverables']}</strong></div>
                </div>
                <div class="tags">{''.join(f'<span class="tag">{chip}</span>' for chip in p['chips'])}</div>
              </div>
              <div class="inline-actions">
                <a class="button primary" href="{p['slug']}.html">Open project</a>
                <a class="button secondary" href="{p['slug']}.html#gallery-block">View visuals</a>
              </div>
            </div>
          </article>
'''

home += '''
        </div>
      </div>
    </section>

    <section class="section" id="gallery">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Visual archive</p>
            <h2 class="section-title">Selected pages from the original portfolio.</h2>
          </div>
          <p class="section-note">These preserve some of the original page compositions while the main navigation shifts into a web-first structure.</p>
        </div>
        <div class="gallery-grid">
          <figure class="reveal"><img src="assets/pages/page-04.jpg" alt="Furever research" data-full="assets/pages/page-04.jpg" /><figcaption>Furever · research and empathy framework</figcaption></figure>
          <figure class="reveal"><img src="assets/pages/page-12.jpg" alt="EnDo workshop" data-full="assets/pages/page-12.jpg" /><figcaption>40 × 40 EnDo · workshop tools and findings</figcaption></figure>
          <figure class="reveal"><img src="assets/pages/page-18.jpg" alt="Touch emoji device" data-full="assets/pages/page-18.jpg" /><figcaption>“Touch” Emoji · tactile and magnetic device concept</figcaption></figure>
          <figure class="reveal"><img src="assets/pages/page-24.jpg" alt="Living Soil process" data-full="assets/pages/page-24.jpg" /><figcaption>Living Soil · biomaterial making process</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="section" id="others">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Other work</p>
            <h2 class="section-title">Additional product and visual design.</h2>
          </div>
          <p class="section-note">These supporting projects remain on the main page as a compact visual archive.</p>
        </div>
        <div class="other-works">
          <article class="other-work reveal"><img src="assets/pages/page-27.jpg" alt="ПоРТ" /><div class="copy"><h4>ПоРТ</h4><p>Crane-cab redesign for aerial operations, including interior layout, seat ergonomics, and joystick placement.</p></div></article>
          <article class="other-work reveal"><img src="assets/pages/page-28.jpg" alt="Omegabot and Tail Wagging Party" /><div class="copy"><h4>Omegabot / Tail Wagging Party</h4><p>Robotics platform design and pet-event visual identity spanning modular hardware and graphic systems.</p></div></article>
          <article class="other-work reveal"><img src="assets/pages/page-29.jpg" alt="Wall climbing robot and bicycle stand" /><div class="copy"><h4>Robot / Urban Object</h4><p>Magnetic wall-climbing robot chassis plus bicycle-stand environmental design with modular functional thinking.</p></div></article>
        </div>
      </div>
    </section>
  </main>

  <footer class="section" style="padding-top:0">
    <div class="wrap">
      <div class="footer-card reveal">
        <div>
          <p class="project-number">Portfolio website</p>
          <h2 class="section-title" style="margin:0 0 8px">Home page + four detailed project pages.</h2>
          <p style="margin:0;max-width:52ch">Built as a static HTML site. You can edit text directly in each HTML file, or change the global visual language in <code>css/style.css</code>.</p>
        </div>
        <div style="font-weight:600">Tingting Liao</div>
      </div>
    </div>
  </footer>

  <div class="lightbox" id="lightbox" aria-hidden="true">
    <button type="button" id="closeLightbox" aria-label="Close">×</button>
    <img src="" alt="Expanded portfolio page" id="lightboxImage" />
  </div>

  <script src="js/main.js"></script>
</body>
</html>'''

(root / 'index.html').write_text(home, encoding='utf-8')

for p in projects:
    cards = ''.join(f'<article class="stat-card reveal"><strong>{stat}</strong><p>{desc}</p></article>' for stat,desc in p['stats'])
    sections = ''.join(f'<article class="content-card reveal"><h3>{title}</h3><p>{text}</p></article>' for title,text in p['sections'])
    figs = ''.join(
        f'<figure class="reveal"><img src="assets/pages/{img}" alt="{p["title"]} visual" data-full="assets/pages/{img}" /><figcaption>{cap}</figcaption></figure>'
        for img,cap in zip(p['gallery'], p['captions'])
    )
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['title']} – Tingting Liao</title>
  <meta name="description" content="{p['summary']}" />
  <link rel="stylesheet" href="css/style.css" />
  <style>:root{{--accent:{p['accent']};--accent-soft:{p['soft']};}}</style>
</head>
<body class="project-page">
  <header class="topbar">
    <div class="wrap nav">
      <a class="brand" href="index.html"><span class="brand-mark"></span><span>Tingting Liao</span></a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="#overview">Overview</a>
        <a href="#process">Project Story</a>
        <a href="#gallery-block">Gallery</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="project-hero">
      <div class="wrap">
        <div class="back-row reveal">
          <a class="button secondary" href="index.html">← Back to home</a>
          <a class="next-project" href="{p['next']}"><span class="small-note">Next</span><strong>{'Home' if p['next']=='index.html' else p['next'].replace('.html','').replace('-',' ').title()}</strong></a>
        </div>
        <div class="project-layout">
          <div class="reveal">
            <p class="kicker">{p['num']}</p>
            <span class="eyebrow"><span class="dot"></span> {p['eyebrow']}</span>
            <h1>{p['title']}</h1>
            <p class="lead">{p['summary']}</p>
            <div class="meta-grid">
              <div class="meta-item"><small>Type</small><strong>{p['type']}</strong></div>
              <div class="meta-item"><small>Duration</small><strong>{p['duration']}</strong></div>
              <div class="meta-item"><small>Context</small><strong>{p['meta2']}</strong></div>
              <div class="meta-item"><small>Deliverables</small><strong>{p['deliverables']}</strong></div>
            </div>
            <div class="tags">{''.join(f'<span class="tag">{chip}</span>' for chip in p['chips'])}</div>
            <div class="hero-actions">
              <a class="button primary" href="#process">Read the case study</a>
              <a class="button secondary" href="#gallery-block">Open visual gallery</a>
            </div>
          </div>
          <div class="project-cover reveal"><img src="assets/pages/{p['cover']}" alt="{p['title']} cover" /></div>
        </div>
      </div>
    </section>

    <section class="section" id="overview">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Overview</p>
            <h2 class="section-title">Problem and design response.</h2>
          </div>
          <p class="section-note">This page keeps the same visual language as the home page, but expands the project into a readable case-study structure.</p>
        </div>
        <div class="overview-grid">
          <article class="overview-card reveal">
            <h3>Project problem</h3>
            <p>{p['problem']}</p>
          </article>
          <article class="overview-card reveal">
            <h3>Design response</h3>
            <p>{p['approach']}</p>
          </article>
        </div>
        <div class="stats-grid" style="grid-template-columns:repeat(3,1fr);margin-top:18px">{cards}</div>
      </div>
    </section>

    <section class="section" id="process">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Project story</p>
            <h2 class="section-title">From research to outcome.</h2>
          </div>
          <p class="section-note">The structure below is web-first rather than PDF-first, so each stage of the project can be scanned more easily.</p>
        </div>
        <div class="case-grid">{sections}</div>
      </div>
    </section>

    <section class="section" id="gallery-block">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="project-number">Selected visuals</p>
            <h2 class="section-title">Pages, process, and final outputs.</h2>
          </div>
          <p class="section-note">Click any image to enlarge it.</p>
        </div>
        <div class="gallery-grid">{figs}</div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="footer-card reveal">
          <div>
            <p class="project-number">Navigation</p>
            <h2 class="section-title" style="margin:0 0 8px">Continue browsing the portfolio.</h2>
            <p style="margin:0;max-width:52ch">Use the next-project link above to move through the case studies, or go back to the home page to select a different project.</p>
          </div>
          <div class="inline-actions">
            <a class="button secondary" href="index.html">Back to home</a>
            <a class="button primary" href="{p['next']}">{'Back to home' if p['next']=='index.html' else 'Next project'}</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <div class="lightbox" id="lightbox" aria-hidden="true">
    <button type="button" id="closeLightbox" aria-label="Close">×</button>
    <img src="" alt="Expanded portfolio page" id="lightboxImage" />
  </div>

  <script src="js/main.js"></script>
</body>
</html>'''
    (root / f"{p['slug']}.html").write_text(html, encoding='utf-8')

readme = '''# Multi-page Design Portfolio

Files:
- `index.html` — home page with project overview cards
- `furever.html` / `endo.html` / `touch-emoji.html` / `living-soil.html` — individual project pages
- `css/style.css` — shared styles for all pages
- `js/main.js` — reveal animation and image lightbox
- `assets/pages/` — images rendered from the original portfolio PDF

How to edit:
1. Open the folder in VS Code.
2. Edit text directly in any `.html` file.
3. Change shared visual styles in `css/style.css`.
4. Replace images in `assets/pages/` if needed, keeping the same filenames or updating the HTML paths.
5. Double-click `index.html` to open locally in a browser.
'''
(root / 'README.md').write_text(readme, encoding='utf-8')

zip_path = Path('/mnt/data/tingting-multipage-portfolio-html.zip')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for path in root.rglob('*'):
        if path.name == 'generate_site.py':
            continue
        zf.write(path, path.relative_to(root.parent))
print('generated', zip_path)
