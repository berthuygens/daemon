# Project Overview

This is a personal developer dashboard built as a static website. It integrates with GitHub to display assigned issues and pull requests, and with Google Calendar to show upcoming meetings. The dashboard is designed to be hosted on GitHub Pages.

The frontend is built with vanilla HTML, CSS, and JavaScript. It features a dark/light mode, draggable quick links, and a configurable profile picture.

A Cloudflare Worker is used to handle the OAuth 2.0 authentication flow for the Google Calendar API. This worker securely stores the refresh token in Cloudflare KV, allowing for automatic token refreshes without user intervention.

# Building and Running

## Local Development

To run the frontend locally, you can use a simple Python HTTP server:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080` in your browser.

## Cloudflare Worker

To deploy the Cloudflare Worker, you will need the `wrangler` CLI.

1.  **Install wrangler:**
    ```bash
    npm install -g wrangler
    ```

2.  **Login to Cloudflare:**
    ```bash
    wrangler login
    ```

3.  **Navigate to the worker directory:**
    ```bash
    cd cloudflare-worker
    ```

4.  **Create a KV namespace:**
    ```bash
    wrangler kv:namespace create "OAUTH_TOKENS"
    ```
    Copy the output `id` and paste it into `wrangler.toml`.

5.  **Set secrets:**
    You need to create Google OAuth 2.0 Client ID credentials in the Google Cloud Console and get a Client ID and Client Secret.

    ```bash
    wrangler secret put GOOGLE_CLIENT_ID
    # Paste your Google Client ID

    wrangler secret put GOOGLE_CLIENT_SECRET
    # Paste your Google Client Secret
    ```

6.  **Deploy the worker:**
    ```bash
    wrangler deploy
    ```

# Development Conventions

*   The frontend is a single `index.html` file containing all HTML, CSS, and JavaScript.
*   Configuration for the dashboard is stored in the browser's `localStorage`.
*   The Cloudflare Worker handles all interactions with the Google Calendar API.
*   The project uses vanilla JavaScript, with no external libraries or frameworks for the main application logic.
*   CSS is written using custom properties for theming (dark/light modes).
