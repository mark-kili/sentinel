# Architecture Decision Records (ADR)

---

## ADR-001

### Title

Use Docker as the deployment platform.

### Status

Accepted

### Date

2026-07-02

### Context

Sentinel is designed to run on an Ubuntu home server and should be portable across machines.

### Decision

All Sentinel services will be containerized using Docker Compose.

### Consequences

- Easy deployment
- Consistent environments
- Simplified updates
- Better isolation