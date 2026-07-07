---
title: "Chapter 1. Multi-site deployments - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-introduction
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/introduction-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "Connect multiple Red Hat build of Keycloak deployments in different sites to increase the overall availability. Red Hat build of Keycloak supports deployments that consist of multiple Red Hat build of Keycloak instances that connect to each other using its Infinispan caches; load balancers can distribute the load evenly across those instances. Those setups are intended for a transparent network on…"
---

# Chapter 1. Multi-site deployments - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 1. Multi-site deployments
Connect multiple Red Hat build of Keycloak deployments in different sites to increase the overall availability.
Red Hat build of Keycloak supports deployments that consist of multiple Red Hat build of Keycloak instances that connect to each other using its Infinispan caches; load balancers can distribute the load evenly across those instances. Those setups are intended for a transparent network on a single site.
The Red Hat build of Keycloak high-availability guide goes one step further to describe setups across multiple sites. While this setup adds additional complexity, that extra amount of high availability may be needed for some environments.
1.1. When to use a multi-site setup
The multi-site deployment capabilities of Red Hat build of Keycloak are targeted at use cases that:
- Are constrained to a single AWS Region.
- Permit planned outages for maintenance.
- Fit within a defined user and request count.
- Can accept the impact of periodic outages.
1.2. Supported Configuration
Two Openshift single-AZ clusters, in the same AWS Region
- Provisioned with Red Hat OpenShift Service on AWS (ROSA), either ROSA HCP or ROSA classic.
- Each Openshift cluster has all its workers in a single Availability Zone.
- OpenShift version 4.17 (or later).
Amazon Aurora PostgreSQL database
- High availability with a primary DB instance in one Availability Zone, and a synchronously replicated reader in the second Availability Zone
- Version 16.8
- AWS Global Accelerator, sending traffic to both ROSA clusters
- AWS Lambda to automate failover
Any deviation from the configuration above is not supported and any issue must be replicated in that environment for support.
Read more on each item in the Building blocks multi-site deployments chapter.
1.3. Maximum load
- 100,000 users
- 300 requests per second
See the Concepts for sizing CPU and memory resources chapter for more information.
1.4. Limitations
- During upgrades of Red Hat build of Keycloak or Data Grid both sites needs to be taken offline for the duration of the upgrade.
- During certain failure scenarios, there may be downtime of up to 5 minutes.
- After certain failure scenarios, manual intervention may be required to restore redundancy by bringing the failed site back online.
- During certain switchover scenarios, there may be downtime of up to 5 minutes.
For more details on limitations see the Concepts for multi-site deployments chapter.
1.5. Next steps
The different chapters introduce the necessary concepts and building blocks. For each building block, a blueprint shows how to set a fully functional example. Additional performance tuning and security hardening are still recommended when preparing a production setup.
