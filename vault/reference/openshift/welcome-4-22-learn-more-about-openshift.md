---
title: "Learn more about {product-title}"
type: reference
domain: openshift
slug: welcome-4-22-learn-more-about-openshift
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/welcome/learn_more_about_openshift
version: 4.22
family: welcome
documentKind: "Documentation"
---

# Learn more about {product-title}

[id="learn_more_about_openshift"]
= Learn more about OpenShift Container Platform

Use the following sections to find content to help you learn about and better understand OpenShift Container Platform functions:

[id="support"]
== Learning and support

[options="header",cols="2*",width="%autowidth.stretch"]
|===
| Learn about OpenShift Container Platform |Optional additional resources

|What's new in OpenShift Container Platform
|OpenShift blog

|OpenShift Container Platform Life Cycle Policy
|OpenShift Container Platform life cycle

|OpenShift Interactive Learning Portal
|OpenShift Knowledgebase articles

| Getting Support
| Gathering data about your cluster

|===

[id="architecture"]
== Architecture

[options="header",cols="2*",width="%autowidth.stretch"]
|===
| Learn about OpenShift Container Platform |Optional additional resources

| Enterprise Kubernetes with OpenShift
| Tested platforms

| Architecture
| Security and compliance

| Networking
| OVN-Kubernetes architecture

| Backup and restore
| Restoring to a previous cluster state

|===

[id="installation"]
== Installation
Explore the following OpenShift Container Platform installation tasks:

[options="header",cols="2*",width="%autowidth.stretch"]
|===
| Learn about installation on OpenShift Container Platform |Optional additional resources

| OpenShift Container Platform installation overview
| Selecting a cluster installation method and preparing it for users

| Installing a cluster in FIPS mode
| About FIPS compliance

|===

[id="other-cluster-installer-tasks"]
== Other cluster installer tasks

[options="header",cols="2*",width="%autowidth.stretch"]
|===
| Learn about other installer tasks on OpenShift Container Platform |Optional additional resources

| Troubleshooting installation issues
| Validating an installation

| Install {rh-storage-first}
| {image-mode-os-lower}

|===

=== Install a cluster in a restricted network

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about installing in a restricted network |Optional additional resources

a|About disconnected installation mirroring
a| If your cluster uses user-provisioned infrastructure, and the cluster does not have full access to the internet, you must mirror the OpenShift Container Platform installation images.

* {aws-first}
* {gcp-short}
* {vmw-short}
* {ibm-cloud-name}
* {ibm-z-name} and {ibm-linuxone-name}
* {ibm-power-name}
* bare metal

|===

=== Install a cluster in an existing network

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about installing in a restricted network |Optional additional resources

| If you use an existing Virtual Private Cloud (VPC) in
{aws-first} or
{gcp-short} or an existing
VNet
on Microsoft Azure, you can install a cluster
| Installing a cluster on {gcp-short} into a shared VPC

|===

[id="cluster-administrator"]
== Cluster Administrator

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about OpenShift Container Platform cluster activities |Optional additional resources

| Understand OpenShift Container Platform management
a|* Machine API
* Operators
* etcd

| Enable cluster capabilities
| Optional cluster capabilities in OpenShift Container Platform 

|===

[id="managing-changing-cluster-components"]
=== Managing and changing cluster components

==== Managing cluster components

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about managing cluster components |Optional additional resources

| Manage compute and control plane machines with machine sets
| Deploy machine health checks

| Apply autoscaling to an OpenShift Container Platform cluster
| Including pod priority in pod scheduling decisions

| Manage container registries
| {quay}

| Manage users and groups
| Impersonating the system:admin user

| Manage authentication
| Multiple identity providers

| Manage Ingress, API server, and Service certificates
| Network security

| Manage networking
a|* Cluster Network Operator
* Multiple network interfaces
* Network policy

| Manage Operators
| Creating applications from installed Operators

|===

Hiding until WMCO 10.19.0 releases, replace as the last row of the above table after WMCO GAs
| {productwinc} overview
| windows_containers/understanding-windows-container-workloads.adoc#understanding-windows-container-workloads_understanding-windows-container-workloads[Understanding Windows container workloads]

==== Changing cluster components

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn more about changing cluster components |Optional additional resources

| Introduction to OpenShift updates
a|* Updating a cluster using the web console
* Updating using the CLI
* Using the OpenShift Update Service in a disconnected environment

| Use custom resource definitions (CRDs) to modify the cluster
a|* Create a CRD
* Manage resources from CRDs

| Set resource quotas
| Resource quotas across multiple projects

| Prune and reclaim resources
| Performing advanced builds

| Scale and tune clusters
| OpenShift Container Platform scalability and performance

|===

[id="observe-cluster"]
== Observe a cluster

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about OpenShift Container Platform |Optional additional resources

| Release notes for the {DTProductName}
| {DTProductName}

| Red Hat build of OpenTelemetry
| Receiving telemetry data from multiple clusters

| About Network Observability
a|* Using metrics with dashboards and alerts
* Observing the network traffic from the Traffic flows view

| About OpenShift Container Platform monitoring
a|* Remote health monitoring
* {PM-title-c} (Technology Preview)

|===

[id="storage-activities"]
== Storage activities

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about OpenShift Container Platform |Optional additional resources

| Storage types
a| * Persistent storage
* Ephemeral storage

|===

[id="application_site_reliability_engineer"]
== Application Site Reliability Engineer (App SRE)

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about OpenShift Container Platform |Optional additional resources

| Building applications overview
| Projects

| Operators
| Cluster Operator reference

|===

[id="Developer"]
== Developer
OpenShift Container Platform is a platform for developing and deploying containerized applications. Read the following OpenShift Container Platform documentation, so that you can better understand OpenShift Container Platform functions:

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about application development in OpenShift Container Platform |Optional additional resources

| Getting started with OpenShift for developers (interactive tutorial)
a|* Understanding OpenShift Container Platform development
* Working with projects
* Create deployments

| Red Hat Developers site
| Understanding image builds

| {openshift-dev-spaces-productname} (formerly Red Hat CodeReady Workspaces)
| Operators

| Create container images
| Managing images overview

| `odo`
| Developer-focused CLI

| Viewing application composition using the Topology view
| Exporting applications

| Understanding {pipelines-shortname}
| Create CI/CD Pipelines

| Configuring an OpenShift cluster by deploying an application with cluster configurations
a|* Controlling pod placement using node taints
* Creating infrastructure machine sets
|===

[id="self-managed-hcp"]
== {hcp-capital}

[options="header",cols="2*",width="%autowidth.stretch"]
|===
|Learn about {hcp} |Optional additional resources

| Hosted control planes overview
a|
Versioning for {hcp}

| Preparing to deploy
a| * Requirements for {hcp}
* Sizing guidance for {hcp}
* Overriding resource utilization measurements
* Installing the {hcp} command-line interface
* Distributing hosted cluster workloads
* Enabling or disabling the {hcp} feature

| Deploying {hcp}
a| * Deploying {hcp} on {VirtProductName}
* Deploying {hcp} on {aws-short}
* Deploying {hcp} on bare metal
* Deploying {hcp} on non-bare-metal agent machines
* Deploying {hcp} on {ibm-z-title}
* Deploying {hcp} on {ibm-power-title}

| Deploying {hcp} in a disconnected environment
a| * Deploying {hcp} on bare metal in a disconnected environment
* Deploying {hcp} on {VirtProductName} in a disconnected environment

| Troubleshooting {hcp}
a| Gathering information to troubleshoot {hcp}

|===
