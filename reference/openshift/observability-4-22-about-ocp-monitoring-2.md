---
title: "About {product-title} monitoring"
type: reference
domain: openshift
slug: observability-4-22-about-ocp-monitoring-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/about-ocp-monitoring
version: 4.22
family: observability
documentKind: "Documentation"
---

# About {product-title} monitoring

[id="about-ocp-monitoring"]
= About OpenShift Container Platform monitoring

OpenShift Container Platform includes a preconfigured, preinstalled, and self-updating monitoring stack that provides monitoring for core platform components. You also have the option to enable monitoring for user-defined projects.

A cluster administrator can configure the monitoring stack with the supported configurations. OpenShift Container Platform delivers monitoring best practices out of the box.

A set of alerts are included by default that immediately notify administrators about issues with a cluster. Default dashboards in the OpenShift Container Platform web console include visual representations of cluster metrics to help you to quickly understand the state of your cluster. With the OpenShift Container Platform web console, you can access metrics and manage alerts.

After installing OpenShift Container Platform, cluster administrators can optionally enable monitoring for user-defined projects. By using this feature, cluster administrators, developers, and other users can specify how services and pods are monitored in their own projects.
As a cluster administrator, you can find answers to common problems such as user metrics unavailability and high consumption of disk space by Prometheus in Troubleshooting monitoring issues.

In OpenShift Container Platform, you can monitor your own projects in isolation from Red{nbsp}Hat Site Reliability Engineering (SRE) platform metrics. You can monitor your own projects without the need for an additional monitoring solution.

The OpenShift Container Platform monitoring stack is based on the Prometheus open source project and its wider ecosystem.
