#!/usr/bin/env python3
"""
Generate Royal Obsidian Gold SVG Assets for Satyam Kumar Kapri's GitHub Profile.
Palette:
  Primary Background:    #090B0E (Deep Royal Obsidian Black)
  Secondary Background:  #101318 (Midnight Charcoal)
  Card Background:       #15191F (Elevated Charcoal Surface)
  Antique Gold:          #C5A059 (Buttons, badges, accents)
  Champagne Gold:        #E8D5A5 (Headings, identity highlights)
  Hover Gold:            #F0C978 (Interactive & glowing accents)
  Warm Ivory:            #F5F0E6 (Readable body text)
  Secondary Text:        #A6A29A (Muted silver metadata)
  Border:                #493A23 (Subtle bronze/gold borders)
"""

import os
import json
import base64
import io
from PIL import Image

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_hero_banner():
    path = os.path.join(OUTPUT_DIR, "hero-banner.svg")
    
    # Load and optimize hero.png
    b64_photo = ""
    hero_path = os.path.join(os.path.dirname(__file__), "..", "hero.png")
    if not os.path.exists(hero_path):
        hero_path = os.path.join(OUTPUT_DIR, "hero.png")
    
    if os.path.exists(hero_path):
        im = Image.open(hero_path)
        w, h = im.size
        target_w = 460
        target_h = int(h * target_w / w)
        resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format='PNG', optimize=True)
        b64_photo = base64.b64encode(buf.getvalue()).decode('utf-8')

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 420" width="100%" height="auto" style="background: transparent;">
  <defs>
    <!-- Royal Obsidian Background Gradient -->
    <radialGradient id="bg-glow" cx="35%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#181510" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#101318" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#090B0E" stop-opacity="1"/>
    </radialGradient>

    <!-- Royal Gold Gradients -->
    <linearGradient id="gold-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C5A059"/>
      <stop offset="35%" stop-color="#F0C978"/>
      <stop offset="70%" stop-color="#E8D5A5"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>

    <linearGradient id="gold-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C5A059" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#493A23" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#E8D5A5" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="frame-gold-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0C978" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#493A23" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#C5A059" stop-opacity="0.9"/>
    </linearGradient>

    <linearGradient id="badge-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#15191F"/>
      <stop offset="50%" stop-color="#1b212a"/>
      <stop offset="100%" stop-color="#15191F"/>
    </linearGradient>

    <!-- Technical Grid Pattern -->
    <pattern id="tech-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#C5A059" stroke-width="0.5" stroke-opacity="0.06"/>
      <circle cx="0" cy="0" r="1" fill="#C5A059" fill-opacity="0.16"/>
    </pattern>

    <!-- Subtle Glow Filter -->
    <filter id="subtle-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Name Specialized Champagne & Antique Gold Gradient -->
    <linearGradient id="name-gold-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E8D5A5"/>
      <stop offset="30%" stop-color="#F5F0E6"/>
      <stop offset="70%" stop-color="#E8D5A5"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>

    <!-- Subtle Antique Gold Text Glow (Delicate, Non-intrusive) -->
    <filter id="subtle-name-glow" x="-20%" y="-30%" width="140%" height="160%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.77  0 0 0 0 0.63  0 0 0 0 0.35  0 0 0 0 0.4 0"/>
    </filter>

    <!-- Portrait Clip Path -->
    <clipPath id="portrait-clip">
      <rect x="882" y="38" width="246" height="280" rx="16"/>
    </clipPath>
  </defs>

  <style>
    @keyframes pulse-slow {{
      0%, 100% {{ opacity: 0.25; }}
      50% {{ opacity: 0.65; }}
    }}
    @keyframes dash {{
      to {{ stroke-dashoffset: -100; }}
    }}
    .grid-bg {{ opacity: 0.85; }}
    .synapse {{
      stroke: #C5A059;
      stroke-width: 1;
      stroke-dasharray: 4, 8;
      animation: dash 25s linear infinite;
    }}
    .pulse-node {{
      animation: pulse-slow 4s ease-in-out infinite;
    }}
    .text-mono {{
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
    }}
    .name-title {{
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, 'Helvetica Neue', 'Arial', sans-serif;
      text-rendering: geometricPrecision;
      shape-rendering: geometricPrecision;
    }}
    .subtitle-font {{
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
      text-rendering: geometricPrecision;
    }}
    .code-font {{
      font-family: 'JetBrains Mono', 'Fira Code', 'SFMono-Regular', Consolas, Menlo, monospace;
    }}
  </style>

  <!-- Base Canvas -->
  <rect width="1200" height="420" rx="16" fill="url(#bg-glow)" stroke="url(#gold-stroke)" stroke-width="1.5"/>

  <!-- Background Technical Grid -->
  <rect x="2" y="2" width="1196" height="416" rx="14" fill="url(#tech-grid)" class="grid-bg"/>

  <!-- Left Margin Circuit Accent (Outside text zone, zero interference) -->
  <g opacity="0.4">
    <path d="M 32 80 V 160 L 42 175 V 250" fill="none" stroke="#C5A059" stroke-opacity="0.3" stroke-width="1.2"/>
    <circle cx="32" cy="80" r="2" fill="#C5A059"/>
    <circle cx="42" cy="175" r="2.5" fill="#F0C978"/>
    <circle cx="42" cy="250" r="2" fill="#E8D5A5"/>
  </g>

  <!-- Center Decorative Glow -->
  <ellipse cx="450" cy="180" rx="260" ry="80" fill="#C5A059" fill-opacity="0.04" filter="url(#subtle-glow)"/>

  <!-- Precision Corner Geometric Brackets -->
  <path d="M 24 44 V 24 H 44" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>
  <path d="M 1176 44 V 24 H 1156" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>
  <path d="M 24 376 V 396 H 44" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>
  <path d="M 1176 376 V 396 H 1156" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>

  <!-- ==================== LEFT / CENTER IDENTITY ==================== -->
  <!-- Top Royal Obsidian Gold Badge -->
  <g transform="translate(60, 48)">
    <rect x="0" y="-13" width="418" height="26" rx="13" fill="url(#badge-grad)" stroke="#493A23" stroke-width="1"/>
    <circle cx="18" cy="0" r="3" fill="#F0C978"/>
    <circle cx="18" cy="0" r="6" fill="#F0C978" fill-opacity="0.25" class="pulse-node"/>
    <text x="32" y="3.5" class="code-font" font-size="10.5" font-weight="600" fill="#E8D5A5" letter-spacing="2">
      &#10022; ROYAL OBSIDIAN GOLD // VERIFIED DEVELOPER &#10022;
    </text>
  </g>

  <!-- Main Name Heading in Crisp Champagne Gold with Subtle Antique Gold Glow -->
  <g transform="translate(60, 134)">
    <!-- Subtle Antique Gold Glow Behind (Soft, Non-blurry, Reduced) -->
    <text class="name-title" font-size="48" font-weight="900" fill="#C5A059" letter-spacing="4" filter="url(#subtle-name-glow)">
      SATYAM KUMAR KAPRI
    </text>
    <!-- Extremely Sharp Foreground Text (Direct Vector, Champagne Gold) -->
    <text class="name-title" font-size="48" font-weight="900" fill="url(#name-gold-grad)" letter-spacing="4">
      SATYAM KUMAR KAPRI
    </text>
  </g>

  <!-- Roles & Architecture Subtitle -->
  <g transform="translate(60, 178)">
    <text class="subtitle-font" font-size="14" font-weight="700" fill="#E8D5A5" letter-spacing="3.2">
      AI / ML ENGINEER  &#8226;  FULL-STACK DEVELOPER  &#8226;  COMPETITIVE PROGRAMMER
    </text>
  </g>

  <!-- Tagline -->
  <g transform="translate(60, 218)">
    <text class="text-mono" font-size="16" font-style="italic" font-weight="400" fill="#C5A059" letter-spacing="1">
      &#8220;Engineering Intelligence. Building What&apos;s Next.&#8221;
    </text>
  </g>

  <!-- Architectural Focus Line -->
  <g transform="translate(60, 256)">
    <line x1="0" y1="0" x2="720" y2="0" stroke="#493A23" stroke-width="1"/>
    <line x1="0" y1="0" x2="160" y2="0" stroke="#C5A059" stroke-width="1.5"/>
    <circle cx="160" cy="0" r="2.5" fill="#F0C978"/>
    <text x="180" y="3.5" class="code-font" font-size="10.5" font-weight="600" fill="#A6A29A" letter-spacing="2">
      SYSTEM DESIGN  &#8226;  APPLIED ML  &#8226;  ENTERPRISE SCALE
    </text>
  </g>

  <!-- ==================== RIGHT PORTRAIT SECTION ==================== -->
  <!-- Ambient Gold Glow Behind Portrait -->
  <ellipse cx="1005" cy="178" rx="150" ry="160" fill="#C5A059" fill-opacity="0.10" filter="url(#subtle-glow)"/>

  <!-- Portrait Frame Exterior Outer Ring -->
  <rect x="878" y="34" width="254" height="288" rx="18" fill="#15191F" stroke="url(#frame-gold-stroke)" stroke-width="1.8"/>

  <!-- Portrait Frame Inner Inset -->
  <rect x="882" y="38" width="246" height="280" rx="15" fill="#101318" stroke="#493A23" stroke-width="1"/>

  <!-- Fine Decorative Corner Accents on Portrait Frame -->
  <path d="M 870 52 V 26 H 896" fill="none" stroke="#F0C978" stroke-width="1.8" stroke-opacity="0.9"/>
  <path d="M 1140 52 V 26 H 1114" fill="none" stroke="#F0C978" stroke-width="1.8" stroke-opacity="0.9"/>
  <path d="M 870 304 V 330 H 896" fill="none" stroke="#F0C978" stroke-width="1.8" stroke-opacity="0.9"/>
  <path d="M 1140 304 V 330 H 1114" fill="none" stroke="#F0C978" stroke-width="1.8" stroke-opacity="0.9"/>

  <!-- Circuit Trace Anchors into Portrait -->
  <line x1="820" y1="178" x2="878" y2="178" stroke="#C5A059" stroke-opacity="0.5" stroke-width="1.2" stroke-dasharray="3, 3"/>
  <circle cx="820" cy="178" r="3" fill="#F0C978"/>
  <circle cx="878" cy="178" r="2.5" fill="#C5A059"/>

  <!-- The Photograph (Preserving Aspect Ratio & Transparency) -->
  <g clip-path="url(#portrait-clip)">
    <!-- Dark Gradient Fill Behind Cutout for Contrast -->
    <rect x="882" y="38" width="246" height="280" fill="#101318"/>
    <ellipse cx="1005" cy="140" rx="90" ry="100" fill="#C5A059" fill-opacity="0.08"/>
    <image x="885" y="40" width="240" height="278" preserveAspectRatio="xMidYMid meet" href="data:image/png;base64,{b64_photo}" xlink:href="data:image/png;base64,{b64_photo}"/>
  </g>

  <!-- Frame Inner Bevel Highlight -->
  <rect x="882" y="38" width="246" height="280" rx="16" fill="none" stroke="#E8D5A5" stroke-opacity="0.25" stroke-width="1"/>

  <!-- Small Name Plate on Frame -->
  <g transform="translate(1005, 318)">
    <rect x="-85" y="-10" width="170" height="20" rx="10" fill="#15191F" stroke="#C5A059" stroke-width="1"/>
    <text text-anchor="middle" y="3.5" class="code-font" font-size="9" font-weight="700" fill="#F0C978" letter-spacing="1.2">
      SATYAM KUMAR KAPRI
    </text>
  </g>

  <!-- ==================== BOTTOM HIGHLIGHTS STRIP ==================== -->
  <g transform="translate(600, 375)">
    <rect x="-550" y="-23" width="1100" height="46" rx="8" fill="#15191F" stroke="#493A23" stroke-width="1"/>

    <!-- Item 1: Education (2nd Year B.Tech CSE) -->
    <text x="-525" y="5" class="code-font" font-size="11" letter-spacing="0.3">
      <tspan font-weight="700" fill="#E8D5A5">KL UNIVERSITY</tspan>
      <tspan fill="#493A23"> | </tspan>
      <tspan font-weight="600" fill="#F5F0E6">2ND YEAR B.TECH CSE</tspan>
      <tspan fill="#493A23"> | </tspan>
      <tspan font-weight="700" fill="#F0C978">9.12 CGPA</tspan>
    </text>

    <line x1="-185" y1="-11" x2="-185" y2="11" stroke="#493A23" stroke-width="1"/>

    <!-- Item 2: CodeChef -->
    <text x="-162" y="5" class="code-font" font-size="11" font-weight="700" fill="#F0C978" letter-spacing="0.5">
      CODECHEF 4&#9733;
    </text>
    <text x="-57" y="5" class="code-font" font-size="11" fill="#A6A29A">
      2128 Peak (Div 2)
    </text>

    <line x1="65" y1="-11" x2="65" y2="11" stroke="#493A23" stroke-width="1"/>

    <!-- Item 3: LeetCode -->
    <text x="88" y="5" class="code-font" font-size="11" font-weight="700" fill="#E8D5A5" letter-spacing="0.5">
      LEETCODE
    </text>
    <text x="160" y="5" class="code-font" font-size="11" fill="#A6A29A">
      Top 9.35% (1780)
    </text>

    <line x1="300" y1="-11" x2="300" y2="11" stroke="#493A23" stroke-width="1"/>

    <!-- Item 4: Solved -->
    <text x="325" y="5" class="code-font" font-size="11" font-weight="700" fill="#F0C978" letter-spacing="0.5">
      640+
    </text>
    <text x="368" y="5" class="code-font" font-size="11" fill="#A6A29A">
      Problems Solved
    </text>
  </g>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_terminal_profile():
    path = os.path.join(OUTPUT_DIR, "terminal-profile.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 380" width="100%" height="auto" style="background: transparent;">
  <defs>
    <linearGradient id="term-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C5A059" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#493A23" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#E8D5A5" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="term-header" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#15191F"/>
      <stop offset="100%" stop-color="#101318"/>
    </linearGradient>
  </defs>

  <style>
    .term-font {
      font-family: 'JetBrains Mono', 'Fira Code', 'SFMono-Regular', Consolas, Menlo, Monaco, monospace;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    .cursor {
      animation: blink 1s infinite;
      fill: #F0C978;
    }
  </style>

  <!-- Terminal Window Body -->
  <rect x="2" y="2" width="936" height="376" rx="10" fill="#090B0E" stroke="url(#term-border)" stroke-width="1.2"/>

  <!-- Terminal Header Bar -->
  <path d="M 2 12 Q 2 2 12 2 L 928 2 Q 938 2 938 12 L 938 38 L 2 38 Z" fill="url(#term-header)" stroke="#493A23" stroke-width="0.8"/>
  <line x1="2" y1="38" x2="938" y2="38" stroke="#493A23" stroke-width="1"/>

  <!-- Window Action Buttons (Royal Obsidian Gold Theme) -->
  <circle cx="24" cy="20" r="5.5" fill="#493A23" stroke="#66512e" stroke-width="0.8"/>
  <circle cx="44" cy="20" r="5.5" fill="#C5A059" stroke="#dbb46b" stroke-width="0.8"/>
  <circle cx="64" cy="20" r="5.5" fill="#F0C978" stroke="#fce09d" stroke-width="0.8"/>

  <!-- Terminal Window Title -->
  <text x="470" y="24" text-anchor="middle" class="term-font" font-size="11.5" font-weight="600" fill="#A6A29A" letter-spacing="1.2">
    satyam@system-x: ~/engineering-identity (zsh)
  </text>

  <!-- Status Indicator (Right Header) -->
  <g transform="translate(870, 20)">
    <circle cx="-35" cy="0" r="3.5" fill="#C5A059"/>
    <text x="-25" y="3.5" class="term-font" font-size="10" font-weight="600" fill="#C5A059" letter-spacing="1">
      READY
    </text>
  </g>

  <!-- Terminal Body Content -->
  <g transform="translate(30, 48)" class="term-font">
    <!-- Command 1: whoami -->
    <text x="0" y="24" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E8D5A5">~</tspan><tspan fill="#F0C978" font-weight="700">$</tspan> <tspan fill="#F5F0E6" font-weight="600">whoami</tspan>
    </text>
    <text x="20" y="46" font-size="13" fill="#E8D5A5" font-weight="600">
      Satyam Kumar Kapri <tspan fill="#A6A29A" font-weight="400">· Computer Science Engineer &amp; AI Systems Developer</tspan>
    </text>

    <!-- Command 2: education -->
    <text x="0" y="80" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E8D5A5">~</tspan><tspan fill="#F0C978" font-weight="700">$</tspan> <tspan fill="#F5F0E6" font-weight="600">education</tspan>
    </text>
    <text x="20" y="102" font-size="13" fill="#F5F0E6">
      B.Tech Computer Science and Engineering (2nd Year) <tspan fill="#C5A059">|</tspan> <tspan fill="#E8D5A5">KL University</tspan> <tspan fill="#A6A29A">(CGPA: 9.12 / 10.0)</tspan>
    </text>

    <!-- Command 3: interests -->
    <text x="0" y="136" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E8D5A5">~</tspan><tspan fill="#F0C978" font-weight="700">$</tspan> <tspan fill="#F5F0E6" font-weight="600">interests</tspan>
    </text>
    <text x="20" y="158" font-size="13" fill="#E8D5A5">
      Artificial Intelligence <tspan fill="#493A23">•</tspan> Machine Learning <tspan fill="#493A23">•</tspan> Full-Stack Development <tspan fill="#493A23">•</tspan> DSA <tspan fill="#493A23">•</tspan> System Design <tspan fill="#493A23">•</tspan> Entrepreneurship
    </text>

    <!-- Command 4: philosophy -->
    <text x="0" y="192" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E8D5A5">~</tspan><tspan fill="#F0C978" font-weight="700">$</tspan> <tspan fill="#F5F0E6" font-weight="600">philosophy</tspan>
    </text>
    <text x="20" y="214" font-size="13" fill="#F0C978" font-weight="600">
      &#8220;Think Algorithmically. Engineer Intelligently. Build Relentlessly.&#8221;
    </text>

    <!-- Command 5: current_status -->
    <text x="0" y="248" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E8D5A5">~</tspan><tspan fill="#F0C978" font-weight="700">$</tspan> <tspan fill="#F5F0E6" font-weight="600">sys_status --active-work</tspan>
    </text>
    <text x="20" y="270" font-size="12.5" fill="#A6A29A">
      [OK] Architecting intelligent software platforms, solving hard graph/DP algorithms, shipping production systems.
    </text>

    <!-- Command 6: prompt cursor -->
    <text x="0" y="304" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E8D5A5">~</tspan><tspan fill="#F0C978" font-weight="700">$</tspan> <rect x="175" y="291" width="8" height="15" class="cursor"/>
    </text>
  </g>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_metrics_card():
    path = os.path.join(OUTPUT_DIR, "metrics-card.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 135" width="100%" height="auto" style="background: transparent;">
  <defs>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#15191F"/>
      <stop offset="100%" stop-color="#101318"/>
    </linearGradient>
    <linearGradient id="gold-text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F0C978"/>
      <stop offset="50%" stop-color="#E8D5A5"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#493A23"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="#493A23"/>
    </linearGradient>
  </defs>

  <style>
    .stat-font {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif;
    }
    .code-font {
      font-family: 'JetBrains Mono', 'Fira Code', 'SFMono-Regular', Consolas, monospace;
    }
  </style>

  <!-- Metric 1: Peak CodeChef Rating -->
  <g transform="translate(0, 0)">
    <rect x="0" y="0" width="220" height="135" rx="10" fill="url(#card-grad)" stroke="url(#card-border)" stroke-width="1.2"/>
    <path d="M 0 0 L 25 0 L 0 25 Z" fill="#C5A059" fill-opacity="0.3"/>
    <text x="110" y="52" text-anchor="middle" class="stat-font" font-size="34" font-weight="900" fill="url(#gold-text-grad)" letter-spacing="1">
      2128
    </text>
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E8D5A5" letter-spacing="1.5">
      PEAK CODECHEF
    </text>
    <text x="110" y="100" text-anchor="middle" class="code-font" font-size="9.5" fill="#A6A29A" letter-spacing="0.5">
      Division 2 · Global #3,556
    </text>
    <line x1="70" y1="116" x2="150" y2="116" stroke="#C5A059" stroke-opacity="0.3" stroke-width="1"/>
  </g>

  <!-- Metric 2: 4-Star Status -->
  <g transform="translate(240, 0)">
    <rect x="0" y="0" width="220" height="135" rx="10" fill="url(#card-grad)" stroke="url(#card-border)" stroke-width="1.2"/>
    <path d="M 0 0 L 25 0 L 0 25 Z" fill="#C5A059" fill-opacity="0.3"/>
    <text x="110" y="52" text-anchor="middle" class="stat-font" font-size="34" font-weight="900" fill="url(#gold-text-grad)" letter-spacing="1">
      4&#9733;
    </text>
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E8D5A5" letter-spacing="1.5">
      CODECHEF STATUS
    </text>
    <text x="110" y="100" text-anchor="middle" class="code-font" font-size="9.5" fill="#A6A29A" letter-spacing="0.5">
      Top Algorithmic Tier
    </text>
    <line x1="70" y1="116" x2="150" y2="116" stroke="#C5A059" stroke-opacity="0.3" stroke-width="1"/>
  </g>

  <!-- Metric 3: DSA Rating -->
  <g transform="translate(480, 0)">
    <rect x="0" y="0" width="220" height="135" rx="10" fill="url(#card-grad)" stroke="url(#card-border)" stroke-width="1.2"/>
    <path d="M 0 0 L 25 0 L 0 25 Z" fill="#C5A059" fill-opacity="0.3"/>
    <text x="110" y="52" text-anchor="middle" class="stat-font" font-size="34" font-weight="900" fill="url(#gold-text-grad)" letter-spacing="1">
      1904
    </text>
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E8D5A5" letter-spacing="1.5">
      DSA PEAK RATING
    </text>
    <text x="110" y="100" text-anchor="middle" class="code-font" font-size="9.5" fill="#A6A29A" letter-spacing="0.5">
      Ranked #445 Global · #422 India
    </text>
    <line x1="70" y1="116" x2="150" y2="116" stroke="#C5A059" stroke-opacity="0.3" stroke-width="1"/>
  </g>

  <!-- Metric 4: Problems Solved -->
  <g transform="translate(720, 0)">
    <rect x="0" y="0" width="220" height="135" rx="10" fill="url(#card-grad)" stroke="url(#card-border)" stroke-width="1.2"/>
    <path d="M 0 0 L 25 0 L 0 25 Z" fill="#C5A059" fill-opacity="0.3"/>
    <text x="110" y="52" text-anchor="middle" class="stat-font" font-size="34" font-weight="900" fill="url(#gold-text-grad)" letter-spacing="1">
      640+
    </text>
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E8D5A5" letter-spacing="1.5">
      PROBLEMS SOLVED
    </text>
    <text x="110" y="100" text-anchor="middle" class="code-font" font-size="9.5" fill="#A6A29A" letter-spacing="0.5">
      Gold Badge Problem Solver
    </text>
    <line x1="70" y1="116" x2="150" y2="116" stroke="#C5A059" stroke-opacity="0.3" stroke-width="1"/>
  </g>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_gold_divider():
    path = os.path.join(OUTPUT_DIR, "gold-divider.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 24" width="100%" height="24" style="background: transparent;">
  <defs>
    <linearGradient id="divider-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#090B0E" stop-opacity="0"/>
      <stop offset="25%" stop-color="#493A23" stop-opacity="0.8"/>
      <stop offset="45%" stop-color="#C5A059" stop-opacity="1"/>
      <stop offset="50%" stop-color="#F0C978" stop-opacity="1"/>
      <stop offset="55%" stop-color="#C5A059" stop-opacity="1"/>
      <stop offset="75%" stop-color="#493A23" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#090B0E" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="40" y1="12" x2="960" y2="12" stroke="url(#divider-grad)" stroke-width="1.2"/>
  <circle cx="500" cy="12" r="4" fill="#090B0E" stroke="#F0C978" stroke-width="1.5"/>
  <circle cx="500" cy="12" r="1.5" fill="#E8D5A5"/>
  <polygon points="460,12 466,9 472,12 466,15" fill="#C5A059" fill-opacity="0.5"/>
  <polygon points="540,12 534,9 528,12 534,15" fill="#C5A059" fill-opacity="0.5"/>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_engineering_roadmap():
    path = os.path.join(OUTPUT_DIR, "engineering-roadmap.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 240" width="100%" height="auto" style="background: transparent;">
  <defs>
    <linearGradient id="card-surface" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#15191F"/>
      <stop offset="100%" stop-color="#101318"/>
    </linearGradient>
    <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#493A23"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="#493A23"/>
    </linearGradient>
  </defs>

  <style>
    .road-head {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif;
      font-weight: 800;
    }
    .road-body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .road-num {
      font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
      font-weight: 700;
    }
  </style>

  <!-- Background Base Container -->
  <rect x="2" y="2" width="936" height="236" rx="12" fill="#090B0E" stroke="#493A23" stroke-width="1"/>

  <!-- Connecting Backbone Rail -->
  <line x1="80" y1="46" x2="860" y2="46" stroke="url(#line-grad)" stroke-width="1.8"/>

  <!-- Node 01: Artificial Intelligence -->
  <g transform="translate(18, 20)">
    <circle cx="75" cy="26" r="14" fill="#15191F" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F0C978">01</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#493A23" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E8D5A5" letter-spacing="0.5">ARTIFICIAL INTEL.</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Building intelligent systems,</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">applied ML pipelines, and</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">modern AI architectures.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#101318"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">ML · DEEP LEARNING</text>
  </g>

  <!-- Node 02: Software Engineering -->
  <g transform="translate(202, 20)">
    <circle cx="75" cy="26" r="14" fill="#15191F" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F0C978">02</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#493A23" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E8D5A5" letter-spacing="0.5">SOFTWARE ENG.</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Designing robust, modular,</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">and scalable enterprise</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">full-stack web apps.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#101318"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">JAVA · REACT · APIS</text>
  </g>

  <!-- Node 03: Competitive Programming -->
  <g transform="translate(386, 20)">
    <circle cx="75" cy="26" r="14" fill="#15191F" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F0C978">03</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#493A23" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E8D5A5" letter-spacing="0.5">COMPETITIVE CODING</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Strengthening algorithmic</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">intuition: DP, graph theory,</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">trees &amp; time efficiency.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#101318"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">4★ CODECHEF · DSA</text>
  </g>

  <!-- Node 04: System Design -->
  <g transform="translate(570, 20)">
    <circle cx="75" cy="26" r="14" fill="#15191F" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F0C978">04</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#493A23" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E8D5A5" letter-spacing="0.5">SYSTEM DESIGN</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Scalable architectures,</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">distributed caching, fault</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">tolerance &amp; concurrency.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#101318"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">DISTRIBUTED SYS</text>
  </g>

  <!-- Node 05: Entrepreneurship -->
  <g transform="translate(754, 20)">
    <circle cx="75" cy="26" r="14" fill="#15191F" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F0C978">05</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#493A23" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E8D5A5" letter-spacing="0.5">ENTREPRENEURSHIP</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Bridging technical rigor</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">with business strategy to</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">build viable products.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#101318"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">VENTURES &amp; SCALE</text>
  </g>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_profile_footer():
    path = os.path.join(OUTPUT_DIR, "profile-footer.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 130" width="100%" height="auto" style="background: transparent;">
  <defs>
    <linearGradient id="footer-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#15191F"/>
      <stop offset="100%" stop-color="#090B0E"/>
    </linearGradient>
    <linearGradient id="gold-stroke-f" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#493A23" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#C5A059" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#493A23" stop-opacity="0.3"/>
    </linearGradient>
  </defs>

  <style>
    .footer-title {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Montserrat, sans-serif;
      font-weight: 800;
      letter-spacing: 4px;
    }
    .footer-quote {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-style: italic;
    }
    .footer-mono {
      font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
    }
  </style>

  <rect x="2" y="2" width="996" height="126" rx="10" fill="url(#footer-bg)" stroke="url(#gold-stroke-f)" stroke-width="1"/>

  <!-- Symmetrical Gold Corner Accents -->
  <path d="M 16 32 V 16 H 32" fill="none" stroke="#C5A059" stroke-width="1.5" stroke-opacity="0.6"/>
  <path d="M 984 32 V 16 H 968" fill="none" stroke="#C5A059" stroke-width="1.5" stroke-opacity="0.6"/>
  <path d="M 16 98 V 114 H 32" fill="none" stroke="#C5A059" stroke-width="1.5" stroke-opacity="0.6"/>
  <path d="M 984 98 V 114 H 968" fill="none" stroke="#C5A059" stroke-width="1.5" stroke-opacity="0.6"/>

  <!-- Center Signature Text -->
  <g transform="translate(500, 38)">
    <text text-anchor="middle" class="footer-title" font-size="18" fill="#E8D5A5">
      SATYAM KUMAR KAPRI
    </text>
  </g>

  <!-- Quote -->
  <g transform="translate(500, 68)">
    <text text-anchor="middle" class="footer-quote" font-size="13" fill="#C5A059">
      &#8220;Think Algorithmically. Engineer Intelligently. Build Relentlessly.&#8221;
    </text>
  </g>

  <!-- Subtitle Metadata -->
  <g transform="translate(500, 98)">
    <text text-anchor="middle" class="footer-mono" font-size="10.5" fill="#A6A29A" letter-spacing="1.5">
      ROYAL OBSIDIAN GOLD EDITION · ENGINEERED FOR EXCELLENCE · KL UNIVERSITY CSE
    </text>
  </g>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_datewise_contribution_graph():
    """Generates an authentic date-wise contribution matrix with months, weekdays, legend and snake."""
    path_dark = os.path.join(OUTPUT_DIR, "github-contribution-grid-snake-dark.svg")
    path_light = os.path.join(OUTPUT_DIR, "github-contribution-grid-snake.svg")
    
    grid_json_path = os.path.join(os.path.dirname(__file__), "grid_data.json")
    if os.path.exists(grid_json_path):
        with open(grid_json_path, "r", encoding="utf-8") as f:
            grid = json.load(f)
    else:
        grid = []

    LEVEL_COLORS = {
        0: ("#15191F", "#212731"),
        1: ("#3a2d18", "#493A23"),
        2: ("#6e5425", "#8c6e33"),
        3: ("#C5A059", "#d4ad63"),
        4: ("#F0C978", "#ffe9a3")
    }

    MONTHS = [
        (0, "Nov"), (4, "Dec"), (8, "Jan"), (12, "Feb"), (17, "Mar"), (21, "Apr"),
        (26, "May"), (30, "Jun"), (35, "Jul"), (39, "Aug"), (44, "Sep"), (48, "Oct"), (52, "Nov")
    ]

    month_labels = []
    for col, name in MONTHS:
        x = 58 + col * 14
        month_labels.append(f'<text x="{x}" y="52" class="axis-font" font-size="10" fill="#A6A29A" font-weight="600">{name}</text>')

    WEEKDAYS = [(1, "Mon"), (3, "Wed"), (5, "Fri")]
    day_labels = []
    for row, name in WEEKDAYS:
        y = 62 + row * 14 + 9
        day_labels.append(f'<text x="24" y="{y}" class="axis-font" font-size="9.5" fill="#A6A29A">{name}</text>')

    cells_svg = []
    for c in grid:
        row = c['row']
        col = c['col']
        date_str = c['date']
        level = c['level']
        fill, stroke = LEVEL_COLORS.get(level, LEVEL_COLORS[0])
        x = 58 + col * 14
        y = 62 + row * 14
        cells_svg.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="2.2" fill="{fill}" stroke="{stroke}" stroke-width="0.6"><title>{date_str}: level {level}</title></rect>')

    snake_head_x = 58 + 48 * 14
    snake_head_y = 62 + 4 * 14

    snake_svg = f"""
  <!-- Snake Animation Group -->
  <g class="snake-group">
    <rect x="{snake_head_x - 28}" y="{snake_head_y}" width="11" height="11" rx="2" fill="#E8D5A5" opacity="0.8"/>
    <rect x="{snake_head_x - 14}" y="{snake_head_y}" width="11" height="11" rx="2" fill="#F0C978" />
    <rect x="{snake_head_x}" y="{snake_head_y}" width="11" height="11" rx="2.5" fill="#F0C978" stroke="#FFE9A3" stroke-width="1.2"/>
    <circle cx="{snake_head_x + 8}" cy="{snake_head_y + 3.5}" r="1.2" fill="#090B0E" />
    <circle cx="{snake_head_x + 8}" cy="{snake_head_y + 7.5}" r="1.2" fill="#090B0E" />
  </g>
"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 205" width="100%" height="auto" style="background: transparent;">
  <defs>
    <linearGradient id="grid-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#493A23" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#C5A059" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#493A23" stop-opacity="0.8"/>
    </linearGradient>
  </defs>

  <style>
    .title-font {{
      font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
    }}
    .axis-font {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    @keyframes snake-pulse {{
      0%, 100% {{ filter: drop-shadow(0 0 2px #F0C978); }}
      50% {{ filter: drop-shadow(0 0 6px #F0C978); }}
    }}
    .snake-group {{
      animation: snake-pulse 3s infinite ease-in-out;
    }}
  </style>

  <!-- Container Box in Royal Obsidian Black -->
  <rect x="2" y="2" width="836" height="201" rx="10" fill="#090B0E" stroke="url(#grid-border)" stroke-width="1.2"/>

  <!-- Top Title Bar -->
  <text x="24" y="26" class="title-font" font-size="11" font-weight="700" fill="#E8D5A5" letter-spacing="1">
    &#10022; 292 CONTRIBUTIONS IN THE LAST YEAR // 2025 &#8211; 2026 &#10022;
  </text>
  <text x="816" y="26" text-anchor="end" class="title-font" font-size="10.5" font-weight="600" fill="#C5A059" letter-spacing="0.8">
    ROYAL OBSIDIAN GOLD ACTIVITY MATRIX
  </text>
  <line x1="24" y1="36" x2="816" y2="36" stroke="#493A23" stroke-width="0.8"/>

  <!-- Month Labels (X-Axis) -->
  {''.join(month_labels)}

  <!-- Day-of-Week Labels (Y-Axis) -->
  {''.join(day_labels)}

  <!-- Grid Cells -->
  {''.join(cells_svg)}

  <!-- Snake Game Character -->
  {snake_svg}

  <!-- Footer & Legend -->
  <text x="58" y="185" class="title-font" font-size="9.5" fill="#A6A29A" letter-spacing="0.5">
    Nov 9, 2025 &#8212; Nov 12, 2026 &#8226; 52-Week Daily Timeline
  </text>

  <g transform="translate(680, 175)">
    <text x="0" y="9" class="title-font" font-size="9" fill="#A6A29A">Less</text>
    <rect x="28" y="0" width="10" height="10" rx="2" fill="#15191F" stroke="#212731" stroke-width="0.5"/>
    <rect x="42" y="0" width="10" height="10" rx="2" fill="#3a2d18" stroke="#493A23" stroke-width="0.5"/>
    <rect x="56" y="0" width="10" height="10" rx="2" fill="#6e5425" stroke="#8c6e33" stroke-width="0.5"/>
    <rect x="70" y="0" width="10" height="10" rx="2" fill="#C5A059" stroke="#d4ad63" stroke-width="0.5"/>
    <rect x="84" y="0" width="10" height="10" rx="2" fill="#F0C978" stroke="#ffe9a3" stroke-width="0.5"/>
    <text x="100" y="9" class="title-font" font-size="9" fill="#A6A29A">More</text>
  </g>
</svg>"""

    with open(path_dark, "w", encoding="utf-8") as f:
        f.write(svg)
    with open(path_light, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path_dark)
    print("Generated:", path_light)

if __name__ == "__main__":
    generate_hero_banner()
    generate_terminal_profile()
    generate_metrics_card()
    generate_gold_divider()
    generate_engineering_roadmap()
    generate_profile_footer()
    generate_datewise_contribution_graph()
    print("All assets successfully generated!")
