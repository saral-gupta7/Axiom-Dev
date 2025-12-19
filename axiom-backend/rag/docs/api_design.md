# API Design Principles

## Purpose of API Design
API design defines how software systems communicate. A well-designed API is:
- Predictable
- Consistent
- Secure
- Easy to evolve

Poor API design increases coupling, breaks clients, and slows development.

---

## RESTful Design Fundamentals

### Resource-Oriented Design
- APIs should expose **resources**, not actions
- Use nouns, not verbs

✅ `/users`, `/orders/{id}`
❌ `/createUser`, `/getOrder`

---

### HTTP Methods Semantics

| Method | Purpose |
|------|--------|
| GET | Retrieve data |
| POST | Create resource |
| PUT | Replace resource |
| PATCH | Partial update |
| DELETE | Remove resource |

Never overload meanings.

---

### HTTP Status Codes

| Code | Meaning |
|----|-------|
| 200 | Success |
| 201 | Resource created |
| 204 | No content |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |
| 409 | Conflict |
| 500 | Server error |

Correct status codes improve debuggability and client behavior.

---

## Request & Response Design

### Consistent JSON Structure
```json
{
  "data": {...},
  "error": null,
  "meta": {...}
}
