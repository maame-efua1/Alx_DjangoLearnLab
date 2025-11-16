# Security checklist

- DEBUG = False in production
- ALLOWED_HOSTS set
- Secure cookies enabled: SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE
- SecurityMiddleware active
- Use CSRF tokens in all POST forms: {% csrf_token %}
- Use Django ORM and forms to prevent SQL injection
- CSP configured via django-csp or middleware
- Permissions used to protect sensitive views
- Testing: verify headers and forms produce expected 403/redirects
