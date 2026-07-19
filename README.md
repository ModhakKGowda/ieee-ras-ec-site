# 🤖 Robot Runner Game & Management Portal

A modern, responsive web application combining an interactive canvas-based mini-game with a community events directory and portal management features. Built with a clean Python backend structure and a fully custom-optimized CSS grid frontend.

---

## 🛠️ Project Structure Overview

Based on our verified deployment tree:

```text
├── api/
│   └── app.py            # Main application server runtime (Flask / WSGI handler)
├── static/
│   ├── css/
│   │   └── style.css     # Global baseline theme with mobile alignment fixes
│   ├── js/
│   │   └── game.js      # Game canvas configuration, physics, and touch inputs
│   └── images/
│       ├── ras_logo.png  # IEEE RAS Organization Brand asset
│       └── pes_logo.png  # IEEE PES Organization Brand asset
├── templates/
│   ├── about.html        # About Platform layout 
│   ├── events.html       # Events matrix tracking layout
│   ├── index.html        # Main landing area and Game container shell
│   └── admin.html        # Portal administration views
├── requirements.txt      # Engine dependencies (Flask, etc.)
└── README.md             # Repository documentation (This file)



🚀 Key Implemented Features

🎮 Universal Game Inputs: Interactive canvas loops that register both standard desktop Spacebar presses and omnidirectional touchstart events on physical smartphone frames.

📱 True Liquid Responsiveness: Custom structural updates to the layout blocks completely fix mobile horizontal scrolling bugs (overflow-x: hidden) and stack items cleanly on smaller viewports.

⚡ Non-Collapsing Event Cards: Box containers on the events and about views are set to expand natively using height: auto !important to ensure text wrapping behaves predictably on narrow phone screens.

🛡️ Polished Dual-Brand Header: Features an elegant navbar container that positions both organization logos crisp and centered without cluttering mobile screens.
