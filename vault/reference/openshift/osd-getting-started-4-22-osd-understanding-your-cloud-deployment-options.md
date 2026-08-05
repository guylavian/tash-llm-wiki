---
title: "Understanding your cloud deployment options"
type: reference
domain: openshift
slug: osd-getting-started-4-22-osd-understanding-your-cloud-deployment-options
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_getting_started/osd-understanding-your-cloud-deployment-options
version: 4.22
family: osd_getting_started
documentKind: "Documentation"
---

# Understanding your cloud deployment options

[id="osd-understanding-your-cloud-deployment-options"]
= Understanding your cloud deployment options

[role="_abstract"]
You can install OpenShift Container Platform on {AWS} or {GCP} using a cloud account that you own or using a cloud account that is owned by Red Hat. This document provides details about the cloud deployment options for OpenShift Container Platform clusters.

// Module included in the following assemblies:
//
// * osd_getting_started/osd-understanding-your-cloud-deployment-options.adoc

[id="overview-of-osd-cloud-deployment-options_{context}"]
= Overview of the OpenShift Container Platform cloud deployment options

[role="_abstract"]
OpenShift Container Platform offers {OCP} clusters as a managed service on {AWS} or {GCP}.

Through the Customer Cloud Subscription (CCS) model, you can deploy clusters in an existing AWS or {gcp-short} cloud account that you own.

Alternatively, you can install OpenShift Container Platform in a cloud account that is owned by Red{nbsp}Hat.

[id="osd-deployment-option-ccs_{context}"]
== Deploying clusters using the Customer Cloud Subscription (CCS) model

With the Customer Cloud Subscription (CCS) model you can deploy Red{nbsp}Hat managed OpenShift Container Platform clusters in an existing {AWS} or {GCP} account that you own. Red{nbsp}Hat requires customers to meet several prerequisites to provide this service, and this service is supported by Red{nbsp}Hat Site Reliability Engineers (SRE).

In the CCS model, the customer pays the cloud infrastructure provider directly for cloud costs, and the cloud infrastructure account is part of an organization owned by the customer, with specific access granted to Red{nbsp}Hat. In this model, the customer pays Red{nbsp}Hat for the CCS subscription and pays the cloud provider for the cloud costs.

By using the CCS model, you can use the services that are provided by your cloud provider, in addition to the services provided by Red{nbsp}Hat.

[id="osd-deployment-option-red-hat-cloud-account_{context}"]
== Deploying clusters in Red{nbsp}Hat cloud accounts

As an alternative to the CCS model, you can deploy OpenShift Container Platform clusters in AWS or {gcp-short} cloud accounts that are owned by Red{nbsp}Hat. With this model, Red{nbsp}Hat is responsible for the cloud account and the cloud infrastructure costs are paid directly by Red{nbsp}Hat. The customer only pays the Red{nbsp}Hat subscription costs.

[id="additional-resources-cloud-deploy_{context}"]
[role="_additional-resources"]
== Additional resources

* Understanding Customer Cloud Subscriptions on {gcp-short}

* Understanding Customer Cloud Subscriptions on AWS
