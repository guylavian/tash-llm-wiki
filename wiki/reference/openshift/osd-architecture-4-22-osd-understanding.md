---
title: "Understanding {product-title}"
type: reference
domain: openshift
slug: osd-architecture-4-22-osd-understanding
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_architecture/osd-understanding
version: 4.22
family: osd_architecture
documentKind: "Documentation"
---

# Understanding {product-title}

[id="osd-understanding"]
= Understanding OpenShift Container Platform

[role="_abstract"]
With its foundation in Kubernetes, OpenShift Container Platform is a complete {OCP} cluster provided as a cloud service, configured for high availability, and dedicated to a single customer.

// Module included in the following assemblies:
//
// * osd_architecture/osd-understanding.adoc

[id="osd-intro_{context}"]
= An overview of OpenShift Container Platform

[role="_abstract"]
OpenShift Container Platform is professionally managed by Red Hat and hosted on {AWS} or {GCP}. Each OpenShift Container Platform cluster comes with a fully managed control plane (Control and Infrastructure nodes), application nodes, installation and management by Red Hat Site Reliability Engineers (SRE), premium Red Hat Support, and cluster services such as logging, metrics, monitoring, notifications portal, and a cluster portal.

OpenShift Container Platform provides enterprise-ready enhancements to Kubernetes, including the following enhancements:

* OpenShift Container Platform clusters are deployed on AWS or {gcp-short} environments and can be used as part of a hybrid approach for application management.

* Integrated Red Hat technology. Major components in OpenShift Container Platform come from Red Hat Enterprise Linux and related Red Hat technologies. OpenShift Container Platform benefits from the intense testing and certification initiatives for Red Hat’s enterprise quality software.

* Open source development model. Development is completed in the open, and the source code is available from public software repositories. This open collaboration fosters rapid innovation and development.

To learn about options for assets you can create when you build and deploy containerized Kubernetes applications in {OCP}, see Understanding {OCP} development.

[id="rhcos_{context}"]
== Custom operating system
OpenShift Container Platform uses Red Hat Enterprise Linux CoreOS (RHCOS), a container-oriented operating system that combines some of the best features and functions of the CoreOS and Red Hat Atomic Host operating systems. RHCOS is specifically designed for running containerized applications from OpenShift Container Platform and works with new tools to provide fast installation, Operator-based management, and simplified upgrades.

RHCOS includes:

- Ignition, which OpenShift Container Platform uses as a firstboot system configuration for initially bringing up and configuring machines.
- CRI-O, a Kubernetes native container runtime implementation that integrates closely with the operating system to deliver an efficient and optimized Kubernetes experience. CRI-O provides facilities for running, stopping, and restarting containers.
- Kubelet, the primary node agent for Kubernetes that is responsible for launching and monitoring containers.

[id="osd-key-features_{context}"]
== Other key features
Operators are both the fundamental unit of the OpenShift Container Platform code base and a convenient way to deploy applications and software components for your applications to use. In OpenShift Container Platform, Operators serve as the platform foundation and remove the need for manual upgrades of operating systems and control plane applications. OpenShift Container Platform Operators such as the Cluster Version Operator and Machine Config Operator allow simplified, cluster-wide management of those critical components.

Operator Lifecycle Manager (OLM) and the software catalog provide facilities for storing and distributing Operators to people developing and deploying applications.

The {quay} Container Registry is a Quay.io container registry that serves most of the container images and Operators to OpenShift Container Platform clusters. Quay.io is a public registry version of {quay} that stores millions of images and tags.

Other enhancements to Kubernetes in OpenShift Container Platform include improvements in software defined networking (SDN), authentication, log aggregation, monitoring, and routing. OpenShift Container Platform also offers a comprehensive web console and the custom OpenShift CLI (`oc`) interface.

[id="telemetry_{context}"]
== Internet and Telemetry access for OpenShift Container Platform

In OpenShift Container Platform, you require access to the internet to install and upgrade your cluster.

Through the Telemetry service, information is sent to Red Hat from OpenShift Container Platform clusters to enable subscription management automation, monitor the health of clusters, assist with support, and improve customer experience.

The Telemetry service runs automatically and your cluster is registered to {cluster-manager-first}. In OpenShift Container Platform, remote health reporting is always enabled and you cannot opt out. The Red Hat Site Reliability Engineering (SRE) team requires the information to provide effective support for your OpenShift Container Platform cluster.

[role="_additional-resources"]
== Additional resources

* About remote health monitoring
