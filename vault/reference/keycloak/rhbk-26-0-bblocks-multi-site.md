---
title: "Chapter 3. Building blocks multi-site deployments - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-bblocks-multi-site
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/bblocks-multi-site-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "The following building blocks are needed to set up a multi-site deployment with synchronous replication. The building blocks link to a blueprint with an example configuration. They are listed in the order in which they need to be installed. Note We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still ne…"
---

# Chapter 3. Building blocks multi-site deployments - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 3. Building blocks multi-site deployments
The following building blocks are needed to set up a multi-site deployment with synchronous replication.
The building blocks link to a blueprint with an example configuration. They are listed in the order in which they need to be installed.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
3.1. Prerequisites
- Understanding the concepts laid out in the Concepts for multi-site deployments chapter.
3.2. Two sites with low-latency connection
Ensures that synchronous replication is available for both the database and the external Data Grid.
Suggested setup: Two AWS Availability Zones within the same AWS Region.
Not considered: Two regions on the same or different continents, as it would increase the latency and the likelihood of network failures. Synchronous replication of databases as services with Aurora Regional Deployments on AWS is only available within the same region.
3.3. Environment for Red Hat build of Keycloak and Data Grid
Ensures that the instances are deployed and restarted as needed.
Suggested setup: Red Hat OpenShift Service on AWS (ROSA) deployed in each availability zone.
Not considered: A stretched ROSA cluster which spans multiple availability zones, as this could be a single point of failure if misconfigured.
3.4. Database
A synchronously replicated database across two sites.
Blueprint: Deploy AWS Aurora in multiple availability zones.
3.5. Data Grid
A deployment of Data Grid that leverages the Data Grid’s Cross-DC functionality.
Blueprint: Deploy Data Grid for HA with the Data Grid Operator using the Data Grid Operator, and connect the two sites using Data Grid’s Gossip Router.
Not considered: Direct interconnections between the Kubernetes clusters on the network layer. It might be considered in the future.
3.6. Red Hat build of Keycloak
A clustered deployment of Red Hat build of Keycloak in each site, connected to an external Data Grid.
Blueprint: Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator that includes connecting to the Aurora database and the Data Grid server.
3.7. Load balancer
A load balancer which checks the /lb-check
URL of the Red Hat build of Keycloak deployment in each site, plus an automation to detect Data Grid connectivity problems between the two sites.
Blueprint: Deploy an AWS Global Accelerator load balancer together with Deploy an AWS Lambda to disable a non-responding site.
