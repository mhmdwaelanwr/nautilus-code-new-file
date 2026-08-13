# Security Policy

## Reporting a vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do not** open a public GitHub issue.
2. Email the maintainer or use [GitHub's private vulnerability reporting](https://github.com/mhmdwaelanwr/nautilus-code-new-file/security/advisories/new).
3. Include steps to reproduce and any relevant logs.

You should receive a response within 72 hours.

## Scope

This project is a Nautilus file-manager extension. It does not run a network service, handle authentication, or process untrusted input beyond the local filesystem. The primary risk surface is local privilege interaction (file creation with user permissions).

## Supported versions

| Version | Supported |
| ------- | --------- |
| 1.x     | Yes       |
| < 1.0   | No        |
