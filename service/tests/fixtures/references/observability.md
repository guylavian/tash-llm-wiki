---
domain: keycloak
title: Observability — Metrics, Health, Tracing
product: RHBK
applies_to: ['26.6', '26.4']
routable: true
type: kb
inject: section
authority: internal-distilled
source_provenance:
  - ref: RHBK Observability Guide
    visibility: public
keywords: [observability, metrics, health, tracing, ispn000541, otlp, sli]
last_verified: '2026-06-28'
---

# Observability — Metrics, Health, Tracing

Intro paragraph about observability.

## Metrics endpoint
The metrics endpoint exposes Micrometer counters at /metrics.

## ISPN000541 cache DNS failure
Symptom: log shows ISPN000541 with a dns_query error during JGroups discovery.
Cause: DNS_PING cannot resolve the headless service.
Fix: verify the headless Service and DNS_PING query name.

## Tracing OTLP
Configure the OTLP exporter endpoint for distributed tracing.
