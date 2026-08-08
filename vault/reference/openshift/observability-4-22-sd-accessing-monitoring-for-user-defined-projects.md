---
title: "Accessing monitoring for user-defined projects"
type: reference
domain: openshift
slug: observability-4-22-sd-accessing-monitoring-for-user-defined-projects
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/sd-accessing-monitoring-for-user-defined-projects
version: 4.22
family: observability
documentKind: "Documentation"
---

# Accessing monitoring for user-defined projects

[id="sd-accessing-monitoring-for-user-defined-projects"]
= Accessing monitoring for user-defined projects

[role="_abstract"]
When you install a OpenShift Container Platform cluster, monitoring for user-defined projects is enabled by default. With monitoring for user-defined projects enabled, you can monitor your own OpenShift Container Platform projects without the need for an additional monitoring solution.

The `dedicated-admin` user has default permissions to configure and access monitoring for user-defined projects.

[NOTE]
====
Custom Prometheus instances and the Prometheus Operator installed through Operator Lifecycle Manager (OLM) can cause issues with user-defined project monitoring if it is enabled. Custom Prometheus instances are not supported.
====

Optionally, you can disable monitoring for user-defined projects during or after a cluster installation.
