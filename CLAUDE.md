# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DAEMON Dashboard is a personal developer dashboard - a static single-page application hosted on GitHub Pages with a Cloudflare Worker backend for OAuth token management. It displays GitHub issues/PRs, Google Calendar events, OTOBO helpdesk tickets, quick links, Reddit posts, and CCB security advisories.

## Development Commands

```bash
# Start local development server
python3 -m http.server 8080
# Then open http://localhost:8080

# Deploy Cloudflare Worker (from cloudflare-worker directory)
cd cloudflare-worker
wrangler deploy

# Set Worker secrets
wrangler secret put GOOGLE_CLIENT_ID
wrangler secret put GOOGLE_CLIENT_SECRET
wrangler secret put OTRS_USERNAME    # OTOBO API user
wrangler secret put OTRS_PASSWORD    # OTOBO API password

# Create KV namespace (if needed)
wrangler kv:namespace create "OAUTH_TOKENS"
```

## Architecture

```
Frontend (Static)                    Backend (Cloudflare Worker)
├── index.html (entire app)          ├── worker.js (OAuth + API handler)
│   ├── CSS styles                   │   ├── /auth → Google OAuth redirect
│   ├── HTML structure               │   ├── /callback → Token exchange
│   └── JavaScript logic             │   ├── /token → Fresh access token
│       ├── GitHub API calls         │   ├── /status → Auth check
│       ├── Calendar API calls       │   ├── /logout → Remove tokens
│       ├── OTOBO ticket calls       │   ├── /rss → RSS proxy
│       ├── Reddit API calls         │   └── /otrs/tickets → OTOBO tickets
│       ├── CCB news ticker          └── wrangler.toml (config)
│       └── LocalStorage (settings)
```

**Key architectural decisions:**
- Single HTML file contains all CSS, HTML, and JavaScript (no build system)
- GitHub token stored in browser localStorage
- Google refresh token stored in Cloudflare KV (server-side)
- Worker handles OAuth token refresh automatically - users authenticate once
- OAuth flow includes CSRF protection via state parameter validation

## External APIs

- **GitHub REST API**: Issues and PRs (requires `repo`, `read:user` scopes)
- **Google Calendar API v3**: Calendar events (requires `calendar.readonly` scope)
- **OTOBO REST API**: Helpdesk tickets (session-based auth via Worker)
- **Reddit JSON API**: Posts from SFW subreddits (no auth needed)
- **CCB RSS Feed**: Security advisories from Centre for Cybersecurity Belgium (proxied through Worker)

## Calendar Event Filtering

Events with these titles are automatically filtered (work locations):
- home, thuis, office, kantoor, bureau, HT BXL, VAC GENT

## Worker Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth` | GET | Redirect to Google OAuth |
| `/callback` | GET | OAuth callback handler |
| `/token` | GET | Get fresh access token |
| `/status` | GET | Check authentication status |
| `/logout` | POST | Remove stored tokens |
| `/rss` | GET | RSS proxy for CCB advisories |
| `/otrs/tickets` | GET | Fetch OTOBO tickets for user |

## Live URLs

- https://b3.wtf (custom domain)
- https://berthuygens.github.io/daemon/

## OTOBO Integration

The dashboard fetches helpdesk tickets from OTOBO (https://ticketing.inbo.be/otobo/).

**OTOBO Webservice Configuration:**
- Webservice name: `DaemonAPI`
- Base URL: `https://ticketing.inbo.be/otobo/nph-genericinterface.pl/Webservice/DaemonAPI`
- Operations: `/Login` (POST), `/Search` (POST/GET), `/Get/:TicketID` (GET)
- API user: `webapi` (with DB auth enabled for fallback)
- Filters: OwnerID=3 (bert.huygens), StateType=new/open

**Required OTOBO Settings:**
- `SessionCheckRemoteIP` must be **disabled** (Cloudflare Workers use different IPs)
- `webapi` user needs read access to ticket queues/groups
