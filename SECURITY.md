# Security Policy

## 🔐 Privacy First

Text_Swap is designed to be completely local and offline.

❌ No internet access
❌ No telemetry
❌ No tracking
❌ No external API calls
✅ All file operations happen locally on your machine
✅ Nothing is ever read, stored, or transmitted outside your system

## 🛡️ What the Tool Accesses

Text_Swap only touches what you explicitly point it at:

- **Files** — only files matching the suffix inside the directory you provide
- **Clipboard** — not accessed at any point
- **System** — no registry edits, no background services, no startup entries

## 🐍 Open Source

The full source code is available in this repository.
You can read, audit, and verify exactly what the tool does before running it.

## 🚨 Reporting a Vulnerability

If you discover a security issue, please do not open a public GitHub Issue.

Instead, report it privately via GitHub's [Security Advisories](../../security/advisories/new) feature.

Include:
- A description of the vulnerability
- Steps to reproduce it
- Any relevant files or screenshots

We'll respond as quickly as possible and coordinate a fix before any public disclosure.
