# Incident Response Playbook

## Purpose

This document describes the steps to follow when a production incident occurs.

## Severity Levels

### SEV-1

A SEV-1 incident represents a complete outage affecting all users.

Examples:

- Entire platform unavailable
- Login service down

Response Time:

- Engineering must respond within 15 minutes.

### SEV-2

A SEV-2 incident affects a subset of users or a major feature.

Examples:

- File uploads failing
- Dashboard not loading

Response Time:

- Engineering must respond within 1 hour.

## Communication

During an incident:

- Updates must be posted every 30 minutes.
- Status page must be updated.

## Resolution

After the incident is resolved:

- A postmortem document must be created.
- Root cause analysis must be completed within 48 hours.
