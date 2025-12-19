# Database Design & Data Modeling

## Choosing the Right Database

### Relational Databases
- Structured data
- ACID guarantees
- Strong consistency

Use when data integrity matters.

---

### NoSQL Databases
- Schema flexibility
- Horizontal scaling
- Eventual consistency

Use when scale and flexibility matter.

---

## Schema Design Principles

### Normalization
- Reduce duplication
- Improve integrity

### Denormalization
- Improve read performance
- Accept controlled redundancy

Balance is key.

---

## Indexing
- Improves query speed
- Slows writes
- Index only what you query

Poor indexing causes performance bottlenecks.

---

## Transactions
- Use when consistency matters
- Keep transactions short
- Avoid long locks

---

## Migrations
- Schema evolution must be controlled
- Version schemas explicitly
- Rollback strategies are essential

---

## Data Integrity
- Foreign keys
- Constraints
- Validation at both DB and app layer

Never trust a single layer.
