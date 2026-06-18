---
title: "Chapter 1. High availability overview - Red Hat build of Keycloak 26.6 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-introduction
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/high_availability_guide/introduction-
guide: high_availability_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 1. High availability overview - Red Hat build of Keycloak 26.6 High Availability Guide

Chapter 1. High availability overview
Explore the different Red Hat build of Keycloak high-availability architectures.
Red Hat build of Keycloak can be deployed in a number of high-availability architectures, allowing system administrators to pick the deployment type most suitable for their needs. Ease of deployment, cost and fault-tolerance guarantees are important considerations when determining the correct architecture for your deployments.
Any Red Hat build of Keycloak deployment must be installed on a properly configured OpenShift cluster that has been configured per the OpenShift installation instructions. For any Red Hat build of Keycloak installations on OpenShift clusters that span multiple sites (i.e. single cluster or multi-clusters across multiple availability zones) the OpenShift cluster must adhere to the Guidance for Red Hat OpenShift Container Platform Clusters.
Ultimately high availability architectures involve many components in addition to the software running and the responsibility for availability of the service is with the customer. This guide has recommended practices for using the Red Hat build of Keycloak in such high availability architectures.
1.1. Architectures
This document describes two high availability architectures in which to deploy Red Hat build of Keycloak: Single-cluster deployments and multi-cluster deployments.
1.1.1. Single-cluster deployments
Deploy Red Hat build of Keycloak in a single cluster, optionally across multiple availability-zones or data centers with the required network latency and database configuration, using Single-cluster deployments.
- Advantages
- No external dependencies
- Deployment in a single OpenShift cluster
- Tolerate availability-zone failure or data center failure, if deployed to multiple availability zones or data centers
- Disadvantages
OpenShift cluster is a single point of failure:
- Control-plane failures could impact all Red Hat build of Keycloak pods
1.1.2. Multi-cluster deployments
Connect two Red Hat build of Keycloak clusters deployed for example in different OpenShift clusters in two availability zones or data centers with the required network latency and database configuration using Multi-cluster deployments.
- Advantages
- Tolerate availability-zone failure
- Tolerate OpenShift cluster failure
- Bridge two networks that do not offer transparent networking
- Regulatory compliance when distinct deployments are required
- Disadvantages
Complexity:
- External load-balancer required
- Separate Data Grid cluster required on each site
Cost:
- Additional load-balancer required
- Additional compute is required for external Data Grid clusters
- Two OpenShift control-planes must be provisioned
- Not supported with three or more availability zones
1.1.3. Next Steps
To learn more about the different high-availability architectures and their supported configurations, please consult the individual chapters.
