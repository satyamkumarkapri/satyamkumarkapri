#!/usr/bin/env python3
"""
Generate Obsidian Gold SVG Assets for Satyam Kumar Kapri's GitHub Profile.
Colors:
  Primary Background:    #090909
  Secondary Background:  #111111
  Card Background:       #171717
  Elevated Surface:      #202020
  Primary Gold:          #C5A059
  Champagne Gold:        #E7D5A5
  Bright Gold:           #F2C879
  Deep Gold:             #9B773B
  Primary Text:          #F5F1E8
  Secondary Text:        #A6A29A
  Borders:               #3A3020
  Gold Gradient:         #9B773B -> #C5A059 -> #E7D5A5
"""

import os
import math

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_hero_banner():
    path = os.path.join(OUTPUT_DIR, "hero-banner.svg")
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="auto" style="background: transparent;">
  <defs>
    <!-- Background Gradient -->
    <radialGradient id="bg-glow" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#1c160c" stop-opacity="0.8"/>
      <stop offset="45%" stop-color="#111111" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#090909" stop-opacity="1"/>
    </radialGradient>

    <!-- Gold Gradients -->
    <linearGradient id="gold-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9B773B"/>
      <stop offset="35%" stop-color="#F2C879"/>
      <stop offset="70%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="#E7D5A5"/>
    </linearGradient>

    <linearGradient id="gold-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C5A059" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#3A3020" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#E7D5A5" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="badge-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1f1a12"/>
      <stop offset="50%" stop-color="#2a2215"/>
      <stop offset="100%" stop-color="#1f1a12"/>
    </linearGradient>

    <!-- Technical Grid Pattern -->
    <pattern id="tech-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#C5A059" stroke-width="0.5" stroke-opacity="0.08"/>
      <circle cx="0" cy="0" r="1" fill="#C5A059" fill-opacity="0.2"/>
    </pattern>

    <!-- Glow Filter -->
    <filter id="subtle-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @keyframes pulse-slow {
      0%, 100% { opacity: 0.2; }
      50% { opacity: 0.55; }
    }
    @keyframes dash {
      to { stroke-dashoffset: -100; }
    }
    .grid-bg { opacity: 0.85; }
    .synapse {
      stroke: #C5A059;
      stroke-width: 1;
      stroke-dasharray: 4, 8;
      animation: dash 25s linear infinite;
    }
    .pulse-node {
      animation: pulse-slow 4s ease-in-out infinite;
    }
    .text-mono {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
    }
    .code-font {
      font-family: 'JetBrains Mono', 'Fira Code', 'SFMono-Regular', Consolas, Menlo, monospace;
    }
  </style>

  <!-- Base Canvas -->
  <rect width="1200" height="400" rx="16" fill="url(#bg-glow)" stroke="url(#gold-stroke)" stroke-width="1.5"/>

  <!-- Background Technical Grid -->
  <rect x="2" y="2" width="1196" height="396" rx="14" fill="url(#tech-grid)" class="grid-bg"/>

  <!-- Abstract Neural & Circuit Structures (Left) -->
  <g opacity="0.65">
    <path d="M 60 120 L 150 70 L 240 110 L 200 220 L 110 240 Z" fill="none" stroke="#C5A059" stroke-opacity="0.15" stroke-width="1"/>
    <line x1="60" y1="120" x2="150" y2="70" class="synapse" stroke-opacity="0.3"/>
    <line x1="150" y1="70" x2="240" y2="110" class="synapse" stroke-opacity="0.3"/>
    <line x1="240" y1="110" x2="200" y2="220" class="synapse" stroke-opacity="0.3"/>
    <line x1="200" y1="220" x2="110" y2="240" class="synapse" stroke-opacity="0.3"/>
    <line x1="110" y1="240" x2="60" y2="120" class="synapse" stroke-opacity="0.3"/>
    
    <!-- Left Circuit Lines -->
    <path d="M 30 200 H 90 L 120 230 H 180" fill="none" stroke="#C5A059" stroke-opacity="0.25" stroke-width="1.2"/>
    <path d="M 80 50 V 90 L 120 130 V 170" fill="none" stroke="#C5A059" stroke-opacity="0.2" stroke-width="1"/>

    <!-- Nodes with glowing halos -->
    <circle cx="150" cy="70" r="4" fill="#F2C879"/>
    <circle cx="150" cy="70" r="10" fill="#F2C879" fill-opacity="0.15" class="pulse-node"/>
    <circle cx="240" cy="110" r="3.5" fill="#C5A059"/>
    <circle cx="200" cy="220" r="4" fill="#F2C879"/>
    <circle cx="110" cy="240" r="3" fill="#9B773B"/>
    <circle cx="60" cy="120" r="3.5" fill="#C5A059"/>
    <circle cx="180" cy="230" r="2.5" fill="#E7D5A5"/>
  </g>

  <!-- Abstract Neural & Circuit Structures (Right) -->
  <g opacity="0.65">
    <path d="M 1140 120 L 1050 70 L 960 110 L 1000 220 L 1090 240 Z" fill="none" stroke="#C5A059" stroke-opacity="0.15" stroke-width="1"/>
    <line x1="1140" y1="120" x2="1050" y2="70" class="synapse" stroke-opacity="0.3"/>
    <line x1="1050" y1="70" x2="960" y2="110" class="synapse" stroke-opacity="0.3"/>
    <line x1="960" y1="110" x2="1000" y2="220" class="synapse" stroke-opacity="0.3"/>
    <line x1="1000" y1="220" x2="1090" y2="240" class="synapse" stroke-opacity="0.3"/>
    <line x1="1090" y1="240" x2="1140" y2="120" class="synapse" stroke-opacity="0.3"/>
    
    <!-- Right Circuit Lines -->
    <path d="M 1170 200 H 1110 L 1080 230 H 1020" fill="none" stroke="#C5A059" stroke-opacity="0.25" stroke-width="1.2"/>
    <path d="M 1120 50 V 90 L 1080 130 V 170" fill="none" stroke="#C5A059" stroke-opacity="0.2" stroke-width="1"/>

    <!-- Nodes -->
    <circle cx="1050" cy="70" r="4" fill="#F2C879"/>
    <circle cx="1050" cy="70" r="10" fill="#F2C879" fill-opacity="0.15" class="pulse-node"/>
    <circle cx="960" cy="110" r="3.5" fill="#C5A059"/>
    <circle cx="1000" cy="220" r="4" fill="#F2C879"/>
    <circle cx="1090" cy="240" r="3" fill="#9B773B"/>
    <circle cx="1140" cy="120" r="3.5" fill="#C5A059"/>
    <circle cx="1020" cy="230" r="2.5" fill="#E7D5A5"/>
  </g>

  <!-- Precision Corner Geometric Brackets -->
  <path d="M 24 44 V 24 H 44" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>
  <path d="M 1176 44 V 24 H 1156" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>
  <path d="M 24 356 V 376 H 44" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>
  <path d="M 1176 356 V 376 H 1156" fill="none" stroke="#C5A059" stroke-width="2" stroke-opacity="0.8"/>

  <!-- Center Decorative Light Flare -->
  <ellipse cx="600" cy="170" rx="280" ry="70" fill="#C5A059" fill-opacity="0.06" filter="url(#subtle-glow)"/>

  <!-- Top Obsidian Gold Badge -->
  <g transform="translate(600, 52)">
    <rect x="-225" y="-14" width="450" height="28" rx="14" fill="url(#badge-grad)" stroke="#3A3020" stroke-width="1"/>
    <circle cx="-198" cy="0" r="3.5" fill="#F2C879"/>
    <circle cx="-198" cy="0" r="7" fill="#F2C879" fill-opacity="0.2" class="pulse-node"/>
    <text x="-182" y="4" class="code-font" font-size="10.5" font-weight="600" fill="#E7D5A5" letter-spacing="2.5">
      ✦ OBSIDIAN GOLD // VERIFIED SYSTEM ARCHITECT ✦
    </text>
    <circle cx="198" cy="0" r="3.5" fill="#F2C879"/>
  </g>

  <!-- Main Identity Heading -->
  <g transform="translate(600, 145)">
    <text text-anchor="middle" class="text-mono" font-size="52" font-weight="900" fill="url(#gold-grad)" letter-spacing="7" filter="url(#subtle-glow)">
      SATYAM KUMAR KAPRI
    </text>
  </g>

  <!-- Subtitle / Role Architecture -->
  <g transform="translate(600, 192)">
    <text text-anchor="middle" class="text-mono" font-size="14.5" font-weight="700" fill="#E7D5A5" letter-spacing="4.5">
      AI / ML ENGINEER  •  FULL-STACK ARCHITECT  •  COMPETITIVE PROGRAMMER
    </text>
  </g>

  <!-- Dynamic Engineering Philosophy Tagline -->
  <g transform="translate(600, 230)">
    <text text-anchor="middle" class="text-mono" font-size="16" font-style="italic" font-weight="400" fill="#C5A059" letter-spacing="1">
      &#8220;Engineering Intelligence. Building What&apos;s Next.&#8221;
    </text>
  </g>

  <!-- Center Thin Gold Rule -->
  <line x1="420" y1="260" x2="780" y2="260" stroke="#3A3020" stroke-width="1"/>
  <circle cx="600" cy="260" r="3" fill="#C5A059"/>
  <line x1="560" y1="260" x2="640" y2="260" stroke="#C5A059" stroke-width="1.5"/>

  <!-- Bottom Real-World Engineering Highlights Strip -->
  <g transform="translate(600, 318)">
    <rect x="-440" y="-22" width="880" height="44" rx="8" fill="#141414" stroke="#3A3020" stroke-width="1"/>
    
    <!-- Item 1: Education -->
    <text x="-415" y="5" class="code-font" font-size="11.5" font-weight="600" fill="#E7D5A5" letter-spacing="0.5">
      KL UNIVERSITY
    </text>
    <text x="-312" y="5" class="code-font" font-size="11" fill="#A6A29A">
      B.Tech CSE (9.12 CGPA)
    </text>
    
    <line x1="-155" y1="-10" x2="-155" y2="10" stroke="#3A3020" stroke-width="1"/>

    <!-- Item 2: CodeChef -->
    <text x="-135" y="5" class="code-font" font-size="11.5" font-weight="600" fill="#F2C879" letter-spacing="0.5">
      CODECHEF 4★
    </text>
    <text x="-32" y="5" class="code-font" font-size="11" fill="#A6A29A">
      2128 Peak (Div 2)
    </text>

    <line x1="100" y1="-10" x2="100" y2="10" stroke="#3A3020" stroke-width="1"/>

    <!-- Item 3: LeetCode -->
    <text x="120" y="5" class="code-font" font-size="11.5" font-weight="600" fill="#E7D5A5" letter-spacing="0.5">
      LEETCODE
    </text>
    <text x="198" y="5" class="code-font" font-size="11" fill="#A6A29A">
      Top 9.35% (1780)
    </text>

    <line x1="315" y1="-10" x2="315" y2="10" stroke="#3A3020" stroke-width="1"/>

    <!-- Item 4: Solved -->
    <text x="335" y="5" class="code-font" font-size="11.5" font-weight="700" fill="#F2C879" letter-spacing="0.5">
      640+
    </text>
    <text x="375" y="5" class="code-font" font-size="11" fill="#A6A29A">
      Solved
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
      <stop offset="0%" stop-color="#C5A059" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#3A3020" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#9B773B" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="term-header" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#141414"/>
      <stop offset="100%" stop-color="#1c1c1c"/>
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
      fill: #F2C879;
    }
  </style>

  <!-- Terminal Window Body -->
  <rect x="2" y="2" width="936" height="376" rx="10" fill="#0C0C0C" stroke="url(#term-border)" stroke-width="1.2"/>

  <!-- Terminal Header Bar -->
  <path d="M 2 12 Q 2 2 12 2 L 928 2 Q 938 2 938 12 L 938 38 L 2 38 Z" fill="url(#term-header)" stroke="#3A3020" stroke-width="0.8"/>
  <line x1="2" y1="38" x2="938" y2="38" stroke="#3A3020" stroke-width="1"/>

  <!-- Window Action Buttons (Luxury Obsidian Gold Theme) -->
  <circle cx="24" cy="20" r="5.5" fill="#3A3020" stroke="#52432c" stroke-width="0.8"/>
  <circle cx="44" cy="20" r="5.5" fill="#9B773B" stroke="#b88d46" stroke-width="0.8"/>
  <circle cx="64" cy="20" r="5.5" fill="#C5A059" stroke="#e8c278" stroke-width="0.8"/>

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
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E7D5A5">~</tspan><tspan fill="#F2C879" font-weight="700">$</tspan> <tspan fill="#F5F1E8" font-weight="600">whoami</tspan>
    </text>
    <text x="20" y="46" font-size="13" fill="#E7D5A5" font-weight="600">
      Satyam Kumar Kapri <tspan fill="#A6A29A" font-weight="400">· Computer Science Engineer &amp; AI Systems Developer</tspan>
    </text>

    <!-- Command 2: education -->
    <text x="0" y="80" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E7D5A5">~</tspan><tspan fill="#F2C879" font-weight="700">$</tspan> <tspan fill="#F5F1E8" font-weight="600">education</tspan>
    </text>
    <text x="20" y="102" font-size="13" fill="#F5F1E8">
      B.Tech Computer Science and Engineering <tspan fill="#C5A059">|</tspan> <tspan fill="#E7D5A5">KL University</tspan> <tspan fill="#A6A29A">(CGPA: 9.12 / 10.0)</tspan>
    </text>

    <!-- Command 3: interests -->
    <text x="0" y="136" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E7D5A5">~</tspan><tspan fill="#F2C879" font-weight="700">$</tspan> <tspan fill="#F5F1E8" font-weight="600">interests</tspan>
    </text>
    <text x="20" y="158" font-size="13" fill="#E7D5A5">
      Artificial Intelligence <tspan fill="#3A3020">•</tspan> Machine Learning <tspan fill="#3A3020">•</tspan> Full-Stack Architecture <tspan fill="#3A3020">•</tspan> DSA <tspan fill="#3A3020">•</tspan> System Design <tspan fill="#3A3020">•</tspan> Entrepreneurship
    </text>

    <!-- Command 4: philosophy -->
    <text x="0" y="192" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E7D5A5">~</tspan><tspan fill="#F2C879" font-weight="700">$</tspan> <tspan fill="#F5F1E8" font-weight="600">philosophy</tspan>
    </text>
    <text x="20" y="214" font-size="13" fill="#F2C879" font-weight="600">
      &#8220;Think Algorithmically. Engineer Intelligently. Build Relentlessly.&#8221;
    </text>

    <!-- Command 5: current_status -->
    <text x="0" y="248" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E7D5A5">~</tspan><tspan fill="#F2C879" font-weight="700">$</tspan> <tspan fill="#F5F1E8" font-weight="600">sys_status --active-work</tspan>
    </text>
    <text x="20" y="270" font-size="12.5" fill="#A6A29A">
      [OK] Architecting intelligent software platforms, solving hard graph/DP algorithms, shipping production systems.
    </text>

    <!-- Command 6: prompt cursor -->
    <text x="0" y="304" font-size="13">
      <tspan fill="#C5A059" font-weight="700">satyam@engineer</tspan><tspan fill="#A6A29A">:</tspan><tspan fill="#E7D5A5">~</tspan><tspan fill="#F2C879" font-weight="700">$</tspan> <rect x="175" y="291" width="8" height="15" class="cursor"/>
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
      <stop offset="0%" stop-color="#181818"/>
      <stop offset="100%" stop-color="#101010"/>
    </linearGradient>
    <linearGradient id="gold-text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F2C879"/>
      <stop offset="50%" stop-color="#E7D5A5"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3A3020"/>
      <stop offset="50%" stop-color="#785e2e"/>
      <stop offset="100%" stop-color="#3A3020"/>
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
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E7D5A5" letter-spacing="1.5">
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
    <text x="110" y="52" text-anchor="middle" class="stat-font" font-size="32" font-weight="900" fill="url(#gold-text-grad)" letter-spacing="1">
      FOUR STAR
    </text>
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E7D5A5" letter-spacing="1.5">
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
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E7D5A5" letter-spacing="1.5">
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
    <text x="110" y="78" text-anchor="middle" class="code-font" font-size="10.5" font-weight="700" fill="#E7D5A5" letter-spacing="1.5">
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
      <stop offset="0%" stop-color="#090909" stop-opacity="0"/>
      <stop offset="25%" stop-color="#3A3020" stop-opacity="0.8"/>
      <stop offset="45%" stop-color="#C5A059" stop-opacity="1"/>
      <stop offset="50%" stop-color="#F2C879" stop-opacity="1"/>
      <stop offset="55%" stop-color="#C5A059" stop-opacity="1"/>
      <stop offset="75%" stop-color="#3A3020" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#090909" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="40" y1="12" x2="960" y2="12" stroke="url(#divider-grad)" stroke-width="1.2"/>
  <circle cx="500" cy="12" r="4" fill="#090909" stroke="#F2C879" stroke-width="1.5"/>
  <circle cx="500" cy="12" r="1.5" fill="#E7D5A5"/>
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
      <stop offset="0%" stop-color="#161616"/>
      <stop offset="100%" stop-color="#0E0E0E"/>
    </linearGradient>
    <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3A3020"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="100%" stop-color="#3A3020"/>
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
  <rect x="2" y="2" width="936" height="236" rx="12" fill="#0A0A0A" stroke="#3A3020" stroke-width="1"/>

  <!-- Connecting Backbone Rail -->
  <line x1="80" y1="46" x2="860" y2="46" stroke="url(#line-grad)" stroke-width="1.8"/>

  <!-- Node 01: Artificial Intelligence -->
  <g transform="translate(18, 20)">
    <circle cx="75" cy="26" r="14" fill="#1A150D" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F2C879">01</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#3A3020" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E7D5A5" letter-spacing="0.5">ARTIFICIAL INTEL.</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Building intelligent systems,</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">applied ML pipelines, and</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">modern AI architectures.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#201C14"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">ML · DEEP LEARNING</text>
  </g>

  <!-- Node 02: Software Engineering -->
  <g transform="translate(202, 20)">
    <circle cx="75" cy="26" r="14" fill="#1A150D" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F2C879">02</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#3A3020" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E7D5A5" letter-spacing="0.5">SOFTWARE ENG.</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Designing robust, modular,</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">and scalable enterprise</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">full-stack web apps.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#201C14"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">JAVA · REACT · APIS</text>
  </g>

  <!-- Node 03: Competitive Programming -->
  <g transform="translate(386, 20)">
    <circle cx="75" cy="26" r="14" fill="#1A150D" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F2C879">03</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#3A3020" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E7D5A5" letter-spacing="0.5">COMPETITIVE CODING</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Strengthening algorithmic</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">intuition: DP, graph theory,</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">trees &amp; time efficiency.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#201C14"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">4★ CODECHEF · DSA</text>
  </g>

  <!-- Node 04: System Design -->
  <g transform="translate(570, 20)">
    <circle cx="75" cy="26" r="14" fill="#1A150D" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F2C879">04</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#3A3020" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E7D5A5" letter-spacing="0.5">SYSTEM DESIGN</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Scalable architectures,</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">distributed caching, fault</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">tolerance &amp; concurrency.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#201C14"/>
    <text x="84" y="174" text-anchor="middle" class="road-num" font-size="9" fill="#C5A059">DISTRIBUTED SYS</text>
  </g>

  <!-- Node 05: Entrepreneurship -->
  <g transform="translate(754, 20)">
    <circle cx="75" cy="26" r="14" fill="#1A150D" stroke="#C5A059" stroke-width="1.5"/>
    <text x="75" y="30.5" text-anchor="middle" class="road-num" font-size="11" fill="#F2C879">05</text>
    <rect x="0" y="58" width="168" height="142" rx="8" fill="url(#card-surface)" stroke="#3A3020" stroke-width="1"/>
    <text x="12" y="82" class="road-head" font-size="11" fill="#E7D5A5" letter-spacing="0.5">ENTREPRENEURSHIP</text>
    <text x="12" y="104" class="road-body" font-size="10" fill="#A6A29A">Bridging technical rigor</text>
    <text x="12" y="120" class="road-body" font-size="10" fill="#A6A29A">with business strategy to</text>
    <text x="12" y="136" class="road-body" font-size="10" fill="#A6A29A">build viable products.</text>
    <rect x="12" y="160" width="144" height="20" rx="4" fill="#201C14"/>
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
      <stop offset="0%" stop-color="#121212"/>
      <stop offset="100%" stop-color="#0A0A0A"/>
    </linearGradient>
    <linearGradient id="gold-stroke-f" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3A3020" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#C5A059" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#3A3020" stop-opacity="0.3"/>
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
    <text text-anchor="middle" class="footer-title" font-size="18" fill="#E7D5A5">
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
      OBSIDIAN GOLD EDITION · ENGINEERED FOR EXCELLENCE · KL UNIVERSITY CSE
    </text>
  </g>
</svg>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated:", path)

def generate_datewise_contribution_graph():
    """Generates an authentic date-wise contribution matrix with months, weekdays, legend and snake."""
    import json
    path_dark = os.path.join(OUTPUT_DIR, "github-contribution-grid-snake-dark.svg")
    path_light = os.path.join(OUTPUT_DIR, "github-contribution-grid-snake.svg")
    
    grid_json_path = os.path.join(os.path.dirname(__file__), "grid_data.json")
    if os.path.exists(grid_json_path):
        with open(grid_json_path, "r", encoding="utf-8") as f:
            grid = json.load(f)
    else:
        grid = []

    LEVEL_COLORS = {
        0: ("#151515", "#221d14"),
        1: ("#3d2f17", "#4d3b1e"),
        2: ("#785e2b", "#8c6e33"),
        3: ("#C5A059", "#d4ad63"),
        4: ("#F2C879", "#ffe9a3")
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
    <rect x="{snake_head_x - 28}" y="{snake_head_y}" width="11" height="11" rx="2" fill="#E7D5A5" opacity="0.8"/>
    <rect x="{snake_head_x - 14}" y="{snake_head_y}" width="11" height="11" rx="2" fill="#F2C879" />
    <rect x="{snake_head_x}" y="{snake_head_y}" width="11" height="11" rx="2.5" fill="#F2C879" stroke="#FFE9A3" stroke-width="1.2"/>
    <circle cx="{snake_head_x + 8}" cy="{snake_head_y + 3.5}" r="1.2" fill="#090909" />
    <circle cx="{snake_head_x + 8}" cy="{snake_head_y + 7.5}" r="1.2" fill="#090909" />
  </g>
"""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 205" width="100%" height="auto" style="background: transparent;">
  <defs>
    <linearGradient id="grid-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3A3020" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#C5A059" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#3A3020" stop-opacity="0.8"/>
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
      0%, 100% {{ filter: drop-shadow(0 0 2px #F2C879); }}
      50% {{ filter: drop-shadow(0 0 6px #F2C879); }}
    }}
    .snake-group {{
      animation: snake-pulse 3s infinite ease-in-out;
    }}
  </style>

  <!-- Container Box -->
  <rect x="2" y="2" width="836" height="201" rx="10" fill="#090909" stroke="url(#grid-border)" stroke-width="1.2"/>

  <!-- Top Title Bar -->
  <text x="24" y="26" class="title-font" font-size="11" font-weight="700" fill="#E7D5A5" letter-spacing="1">
    &#10022; 292 CONTRIBUTIONS IN THE LAST YEAR // 2025 &#8211; 2026 &#10022;
  </text>
  <text x="816" y="26" text-anchor="end" class="title-font" font-size="10.5" font-weight="600" fill="#C5A059" letter-spacing="0.8">
    DATE-WISE CONTRIBUTION MATRIX
  </text>
  <line x1="24" y1="36" x2="816" y2="36" stroke="#3A3020" stroke-width="0.8"/>

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
    <rect x="28" y="0" width="10" height="10" rx="2" fill="#151515" stroke="#221d14" stroke-width="0.5"/>
    <rect x="42" y="0" width="10" height="10" rx="2" fill="#3d2f17" stroke="#4d3b1e" stroke-width="0.5"/>
    <rect x="56" y="0" width="10" height="10" rx="2" fill="#785e2b" stroke="#8c6e33" stroke-width="0.5"/>
    <rect x="70" y="0" width="10" height="10" rx="2" fill="#C5A059" stroke="#d4ad63" stroke-width="0.5"/>
    <rect x="84" y="0" width="10" height="10" rx="2" fill="#F2C879" stroke="#ffe9a3" stroke-width="0.5"/>
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
