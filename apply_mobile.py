import os

target_string = """  .founder-section{grid-template-columns:1fr;}
}"""

replacement_string = """  .founder-section{grid-template-columns:1fr;}
}

/* SMARTPHONE OPTIMIZATIONS (Max 480px) */
@media(max-width:480px) {
  .section-pad { padding: 3.5rem 0; }
  .hero h1 { font-size: clamp(2.2rem, 11vw, 2.8rem) !important; line-height: 1.15; }
  .hero-desc { font-size: 0.95rem; }
  .hero-stats { flex-direction: column !important; align-items: center; gap: 1.25rem; }
  .stat { width: 100%; justify-content: center; text-align: center; }
  .hero-btns, .cta-btns { flex-direction: column !important; width: 100%; gap: 1rem; }
  .btn-primary, .btn-ghost, .btn-cta, .btn-cta-ghost { width: 100%; justify-content: center; text-align: center; }
  .aaa-grid, .testi-grid, .formats-grid, .photo-strip { gap: 1.5rem !important; }
  .port-choices { grid-template-columns: 1fr !important; }
}"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_string in content and "SMARTPHONE OPTIMIZATIONS (Max 480px)" not in content:
        content = content.replace(target_string, replacement_string)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file}")
    else:
        print(f"Skipped {file}")
