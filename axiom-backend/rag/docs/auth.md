---

# 📄 `auth.md`

```md
# Authentication & Authorization

## Authentication vs Authorization
- Authentication: Who are you?
- Authorization: What are you allowed to do?

Never mix these concepts.

---

## Common Authentication Methods

### API Keys
- Simple
- Best for server-to-server
- Must be rotated and scoped

---

### Token-Based Authentication
- JWTs or opaque tokens
- Stateless
- Scales horizontally

Important considerations:
- Token expiration
- Refresh strategies
- Revocation

---

### OAuth 2.0 (Conceptual)
- Delegated access
- Used for third-party integrations
- Avoid rolling your own OAuth

---

## Authorization Models

### Role-Based Access Control (RBAC)
- Roles like `admin`, `user`
- Simple but rigid

---

### Attribute-Based Access Control (ABAC)
- Decisions based on attributes
- More flexible
- Harder to reason about

---

## Security Best Practices
- Never store plaintext secrets
- Always hash passwords
- Use HTTPS everywhere
- Rotate credentials regularly

---

## Common Pitfalls
- Long-lived tokens
- Over-privileged roles
- Missing authorization checks
- Leaking auth errors
