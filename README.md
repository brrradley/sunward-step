# Sunward Step Manchester

A bright, welcoming community website for **Sunward Step Manchester** — a local walking group and social support project helping people connect through friendly walks, community events, food, music and conversation.

The site is deliberately lightweight, fast and easy to maintain: a single static HTML page styled with Tailwind CSS via CDN, with no build step or framework dependency.

## Repository description

**A bright community website for Sunward Step Manchester, sharing local walks, free social events and support for people experiencing loneliness or isolation.**

## Overview

Sunward Step Manchester brings people together through simple, welcoming community activities. The website gives visitors a clear first impression of the group, highlights the weekly walking meet-up, promotes free community events and provides straightforward contact details.

The design uses bright, friendly colours, rounded cards, strong typography and simple navigation to make the information feel approachable and easy to understand on mobile and desktop.

## Key features

- **Responsive layout** for phones, tablets and desktop screens.
- **Sticky navigation bar** with desktop links and a collapsible mobile menu.
- **Hero section** promoting the weekly walking group.
- **Poster-style event card** for quick visual scanning of time, place and purpose.
- **Community support section** explaining the benefits of fresh air, conversation and connection.
- **Free event section** for warm food, music, entertainment, conversation and raffle details.
- **Contact section** with phone, email and social media prompts.
- **Smooth scrolling** for in-page navigation.
- **No build process** — the site can be edited and deployed as plain HTML.

## Tech stack

- **HTML5** for the page structure.
- **Tailwind CSS CDN** for utility-first styling.
- **Vanilla JavaScript** for the mobile menu interaction.
- **Static assets** for branding and imagery.

## Project structure

```text
sunward-step/
├── index.html
├── assets/
│   └── sunwardsteps-logo.png
└── README.md
```

## Main sections

### Walking group

The main landing section introduces the weekly walking group, including the regular time, location details and a clear call to action for visitors who want to get involved.

### Community support

A short supporting section explains the purpose of the group: helping people find fresh air, conversation, support and community connection in a safe, welcoming space.

### Free community event

The event section promotes Sunward Step Manchester’s free community event, including food, refreshments, music, entertainment, dancing, friendly conversation, laughter and a raffle.

### Contact

The contact section keeps the next step simple, with direct phone and email links plus a reminder that the group can also be found on TikTok and Facebook.

## Local development

Because this is a static site, there is no install step.

Open `index.html` directly in a browser, or use a simple local server for a more production-like preview:

```bash
python3 -m http.server 8080
```

Then visit:

```text
http://localhost:8080
```

## Deployment

This project can be deployed to any static hosting provider, including:

- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages
- Traditional web hosting via FTP/cPanel

No server-side runtime is required.

## Accessibility and usability notes

The site includes responsive navigation, readable contrast, semantic page sections, descriptive image alt text and large tap-friendly links. Future improvements could include a dedicated privacy/accessibility page, social profile links, embedded map directions and structured event schema.

## Future improvements

Potential next steps:

- Add real TikTok and Facebook profile links.
- Add a map or directions link for meeting points and event venues.
- Add event schema markup for better search visibility.
- Add a small gallery of community/event photos.
- Move repeated event details into a simple data file if the site grows.
- Add a proper favicon and social sharing image.

## Credits

Built by [Bradley Ashton](https://github.com/brrradley) as a clean, modern and accessible web presence for Sunward Step Manchester.
