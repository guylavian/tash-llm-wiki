---
title: "Add-on services available for {product-title}"
type: reference
domain: openshift
slug: adding-service-cluster-4-22-rosa-available-services
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/adding_service_cluster/rosa-available-services
version: 4.22
family: adding_service_cluster
documentKind: "Documentation"
---

# Add-on services available for {product-title}

[id="rosa-available-services"]
= Add-on services available for OpenShift Container Platform

You can add services to your existing OpenShift Container Platform (ROSA) cluster using the {cluster-manager-first} console.

These services can also be installed using the `rosa install addon` command.

// Module included in the following assemblies:
//
// * adding_service_cluster/rosa-available-services.adoc
[id="aws-cloudwatch_{context}"]

= Amazon CloudWatch

Amazon CloudWatch forwards logs from OpenShift Container Platform (ROSA) to the AWS console for viewing. You must first install the ROSA `cluster-logging-operator` using the ROSA CLI (`rosa`) before installing the Amazon CloudWatch service through {cluster-manager-first} console.

[role="_additional-resources"]
.Additional resources

* Amazon CloudWatch product information

// Module included in the following assemblies:
//
// * adding_service_cluster/available-services.adoc
// * adding_service_cluster/rosa-available-services.adoc
[id="osd-rhoam_{context}"]
= Red{nbsp}Hat OpenShift API Management

The Red{nbsp}Hat OpenShift API Management (OpenShift API Management) service is available as an add-on to your OpenShift Container Platform on AWS cluster. OpenShift API Management is a managed API traffic control and API program management solution. It is based on the 3scale API Management platform and implements single sign-on for Red{nbsp}Hat solutions to secure and protect your APIs.

This OpenShift API Management entitlement provides:

* Availability to any cluster that meets the resource requirements listed in the Red{nbsp}Hat OpenShift API Management service definition.
* Availability to any cluster that meets the resource requirements listed in the OpenShift Container Platform service definition.
* Full production-level support.
* No time limits on usage.
* 100K quota, or calls per day. Customers have the option to pay for an OpenShift API Management subscription with higher quotas.

[role="_additional-resources"]
.Additional resources
* Red{nbsp}Hat OpenShift API Management

// Module included in the following assemblies:
//
// * adding_service_cluster/rosa-available-services.adoc
// This module is no longer included in the document due to OSDOCS-5817.
[id="rosa-rhoda_{context}"]
= Red Hat OpenShift Database Access

{rhoda} enables easy consumption of database-as-a-service (DBaaS) offerings from partners including MongoDB Atlas, Crunchy Bridge, CockroachDB, and Amazon Relational Database Service (RDS) directly from managed OpenShift Container Platform clusters. You can manage, monitor, and create cloud-hosted database instances for connecting to your applications.

{rhoda} is a Service Preview release. A Service Preview release contains features that are early in development. Service Preview releases are not production ready and are not fully tested. Do not use {rhoda-short} for production or business-critical workloads.

[role="_additional-resources"]
.Additional resources

* Red{nbsp}Hat OpenShift Database Access product page
// This module and additional resource are no longer included in the document due to OSDOCS-5817.

// Module included in the following assemblies:
//
// * adding_service_cluster/rosa-available-services.adoc
[id="rosa-AI_{context}"]
= Red{nbsp}Hat OpenShift AI

Red Hat OpenShift AI enables users to integrate data and AI and machine learning software to run end-to-end machine learning workflows. It provides a collection of notebook images with the tools and libraries required to develop and deploy data models. This allows data scientists to easily develop data models, integrate models into applications, and deploy applications using Red{nbsp}Hat OpenShift. OpenShift AI is available as an add-on to Red{nbsp}Hat managed environments such as {osd} and OpenShift Container Platform (ROSA).

[role="_additional-resources"]
.Additional resources
* Red{nbsp}Hat OpenShift AI documentation
* Red{nbsp}Hat OpenShift AI product page
