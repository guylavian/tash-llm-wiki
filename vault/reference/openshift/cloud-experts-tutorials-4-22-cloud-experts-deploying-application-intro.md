---
title: "Tutorial: Deploying an application"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-intro
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-intro
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Deploying an application

[id="cloud-experts-deploying-application-intro"]
= Tutorial: Deploying an application

[role="_abstract"]
After successfully provisioning your cluster, you can deploy an application on it. This application allows you to become more familiar with some of the features of OpenShift Container Platform and Kubernetes.

== Lab overview
In this lab, you will complete the following set of tasks designed to help you understand the concepts of deploying and operating container-based applications:

* Deploy a Node.js based app by using S2I and Kubernetes Deployment objects.
* Set up a continuous delivery (CD) pipeline to automatically push source code changes.
* Explore logging.
* Experience self healing of applications.
* Explore configuration management through configmaps, secrets, and environment variables.
* Use persistent storage to share data across pod restarts.
* Explore networking within Kubernetes and applications.
* Familiarize yourself with ROSA and Kubernetes functionality.
* Automatically scale pods based on loads from the Horizontal Pod Autoscaler.
* Use AWS Controllers for Kubernetes (ACK) to deploy and use an S3 bucket.

This lab uses either the {rosa-cli} or OpenShift Container Platform web user interface (UI).
