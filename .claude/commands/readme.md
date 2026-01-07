## Readme file creation

README Standards & Guidelines

This document outlines the required structure and formatting for project documentation. To ensure all projects are consistent, easy to deploy, and transparent regarding security.

## 1. Core Structure
Every README must follow this specific order to prioritize user experience and deployment speed:

1.  **Title & Hook:** Name and 1-sentence value proposition.
2.  **Features:** Bullet points of what it *does* (not just what it *is*).
3.  **Live Demo:** A link or GIF immediately available.
4.  **Setup (The Core):** Step-by-step installation instructions.
5.  **Architecture:** ASCII diagram of data flow.
6.  **Privacy/Security:** Explicit statement on token handling.
7.  **Tech Stack:** List of technologies used.
8.  **License:** Default MIT if not mentiond in project.

## 2. Writing Guidelines for specific Sections

### A. The Setup Section
This is the most critical part. Do not assume the user knows how to use the tools.
* **Tokens:** Explicitly list where to get them and which scopes are needed (e.g., `repo`, `read:user`).
* **CLI Commands:** Provide full copy-pasteable blocks for terminal commands.
* **Secrets:** If using Cloudflare/AWS, show exactly how to set environment variables.

### B. Architecture Diagrams
Use ASCII art to visualize how the frontend talks to the backend. This adds immediate professional value.
* *Tool Recommendation:* Use [textik.com](https://textik.com) or [asciiflow.com](https://asciiflow.com).

### C. Privacy & Security
If the app handles OAuth tokens or personal data, you **must** disclose:
1.  Where tokens are stored (LocalStorage, Cookies, or Server-side KV).
2.  If analytics are present.
3.  If data is encrypted.
