# EduFlow System Architecture & Design Specification

## High-Level Architectural Pattern
EduFlow implements the Django Model-View-Template (MVT) design pattern, augmented with:
- **Service Layer Pattern**: Business logic decoupled from views into transaction-safe domain services.
- **Role-Based Access Control (RBAC)**: 11 distinct roles with granular object-level permissions.
- **Immutable Audit Trail**: All state mutations recorded with timestamps, actor stamps, and JSON diffs.
- **Tenancy Context**: Support for multi-campus institutions with contextual scoping.

## Component Interactions
1. **Request Flow**: Gateway -> Security Middleware -> InstitutionContextMiddleware -> URL Routing -> Viewset -> Domain Service -> ORM Model -> Database.
2. **Response Flow**: Database -> Serializer / Context Processor -> Django Template Engine -> HTML5 Response.
