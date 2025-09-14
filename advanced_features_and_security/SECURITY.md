# HTTPS and Security Configuration

## Django Settings
- `SECURE_SSL_REDIRECT = True`: Forces all traffic to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS-only access for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows site to be preloaded into browsers’ HSTS lists.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are only transmitted over HTTPS.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are only transmitted over HTTPS.
- `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS protection.

## Deployment
Configured web server (Nginx/Apache) with SSL/TLS using Let’s Encrypt.
All HTTP requests redirected to HTTPS.
