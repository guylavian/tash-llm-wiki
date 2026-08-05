---
title: "{product-title} {product-version} release notes"
type: reference
domain: openshift
slug: microshift-release-notes-4-22-microshift-4-22-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_release_notes/microshift-4-22-release-notes
version: 4.22
family: microshift_release_notes
documentKind: "Documentation"
---

# {product-title} {product-version} release notes

[id="microshift-4-22-release-notes"]
= OpenShift Container Platform  release notes

[role="_abstract"]
{product-title-first} provides developers and IT organizations with small-form-factor and edge computing delivered as an application that customers can deploy on top of their managed {op-system-base-full} devices at the edge. Built on {OCP} and Kubernetes, {microshift-short} provides an efficient way to operate a single node in low-resource edge environments.

// Module included in the following assemblies:
//
//microshift_release_notes/microshift-4-22-release-notes.adoc

[id="microshift-4-22-about-this-release_{context}"]
= About this release

[role="_abstract"]
Built on {OCP} and Kubernetes, {microshift-short} provides an efficient way to operate a single node in low-resource edge environments.

{microshift-short} is designed to make control plane restarts economical and be lifecycle-managed as a single unit by the operating system. Updates, roll-backs, and configuration changes consist of simply staging another version in parallel and then - without relying on a network - flipping to and from that version and restarting.

Version  of {microshift-short} includes new features and enhancements. Update to the latest version of {microshift-short} to receive all of the latest features, bug fixes, and security updates. {microshift-short} is derived from {OCP} {ocp-version} and uses the CRI-O container runtime. New features, changes, and known issues that pertain to {microshift-short} are included in this topic.

You can deploy a {microshift-short} node to on-premise, cloud, disconnected, and offline environments.

{microshift-short}  is supported on {op-system-base-full} {op-system-version}.

For lifecycle information, see the OpenShift Container Platform Life Cycle Policy.

// Module included in the following assemblies:
//
//microshift_release_notes/microshift-4-22-release-notes.adoc

[id="microshift-4-22-new-features-enhancements_{context}"]
= New features and enhancements

[role="_abstract"]
This release adds improvements related to the following components and concepts.

[id="microshift-4-22-RHEL-9-8-support-feature1_{context}"]
== {microshift-short} is supported on {op-system-base-full} {op-system-version}

With this release, {microshift-short} is supported on {op-system-base-full} {op-system-version}.

//TODO add new features and enhancements as needed

[id="microshift-4-22-ingress-tls-doc_{context}"]
== Ingress TLS configuration documentation

With this release, {microshift-short} documentation adds procedures and prerequisites for the default ingress router certificate (`ingress.certificateSecret`) and for TLS on Kubernetes `Ingress` objects.

* Using ingress control for a {microshift-short} node

//TODO add new features and enhancements as needed
//[id="microshift-4-22-placeholder-feature2_{context}"]
//== placeholder feature 2

//TODO add new features and enhancements as needed
//[id="microshift-4-22-placeholder-feature3_{context}"]
//== placeholder feature 3

//etc

//[id="microshift-4-2S-doc-enhancements_{context}"]
//== Documentation enhancements Red{nbsp}Hat Customer Portal for these features:

// Module included in the following assemblies:
//
//microshift_release_notes/microshift-4-22-release-notes.adoc

[id="microshift-4-22-tech-preview_{context}"]
= Technology Preview features

[role="_abstract"]
Some features in this release are currently in Technology Preview. These experimental features are not intended for production use. Note the following scope of support on the Red{nbsp}Hat Customer Portal for these features:

Technology Preview Features Support Scope

[id="microshift-4-22-RHEL10-2-support_{context}"]
== Support for {op-system-base-full} {op-system-version-10}

{op-system-base-full} {op-system-version-10} is available as a Technology Preview feature with {microshift-short} {ocp-version}.

//include::modules/microshift-4-22-bug-fixes.adoc[leveloffset=+1]

//include::modules/microshift-4-22-known-issues.adoc[leveloffset=+1]

// Module included in the following assemblies:
//
//microshift_release_notes/microshift-4-22-release-notes.adoc

[id="microshift-4-22-additional-release-notes_{context}"]
= Additional release notes

[role="_abstract"]
Release notes for related components and products are available in the following documentation:

[id="microshift-4-22-additional-release-notes-gitops_{context}"]
== GitOps release notes
See Red{nbsp}Hat OpenShift GitOps: Highlights of what is new and what has changed with this OpenShift GitOps release for more information. You can also go to the following Red{nbsp}Hat package download page and search for "gitops" if you just need the latest package: Red{nbsp}Hat packages.

[id="microshift-4-22-additional-release-notes-ocp_{context}"]
== {OCP} release notes
See the {OCP} Release Notes for information about the Operator Lifecycle Manager and other components. Not all of the changes to {OCP} apply to {microshift-short}. See the specific {microshift-short} implementation of an Operator or function for more information.

[id="microshift-4-22-additional-release-notes-rhel_{context}"]
== {op-system-base-full} release notes
See the Release Notes for Red{nbsp}Hat Enterprise Linux 10 for more information about {op-system-base}.
//Use the latest compatible RHEL, expected to be 10

[id="microshift-4-22-additional-release-notes-rhoai_{context}"]
== {rhoai} release notes
See the Release notes for more information about {rhoai}.

// Module included in the following assemblies:
//
//microshift_release_notes/microshift-4-22-release-notes.adoc

[id="microshift-4-22-asynch-updates_{context}"]
= Asynchronous updates

[role="_abstract"]
Security, bug fix, and enhancement updates for {microshift-short}  are released asynchronously through the Red{nbsp}Hat Network. All {microshift-short}  updates are https://access.redhat.com/downloads/content/290/[available on the Red{nbsp}Hat Customer Portal]. For more information about asynchronous updates, read the https://access.redhat.com/product-life-cycles?product=Red%20Hat%20build%20of%20Microshift,Red%20Hat%20Device%20Edge[{microshift-short} Life Cycle].

Red{nbsp}Hat Customer Portal users can enable update notifications in the account settings for Red{nbsp}Hat Subscription Management (RHSM). When notifications are enabled, you are notified through email whenever new updates relevant to your registered systems are released.

[NOTE]
====
Red{nbsp}Hat Customer Portal user accounts must have systems registered and consuming {microshift-short} entitlements for {microshift-short} update notification emails to generate.
====

This section is updated over time to provide notes on enhancements and bug fixes for future asynchronous releases of {microshift-short} . Versioned asynchronous releases, for example with the form {microshift-short} .z, are detailed in the following subsections.

// Module included in the following assemblies:
//
//microshift_release_notes/microshift-4-22-release-notes.adoc

[id="microshift-4-22-0-async_{context}"]
= RHEA-2026:2640 - {microshift-short} 4.22.0 bug fix and enhancement update

[role="_abstract"]
Issued: 09 June 2026

OpenShift Container Platform release 4.22.0 is now available. Bug fixes and enhancements are listed in the RHEA-2026:2640 advisory. Release notes for bug fixes and enhancements are provided in this documentation. The images that are included in the update are provided by the {OCP} RHBA-2026:449 advisory.

See the latest images included with {microshift-short} by using the following instructions:

* Listing the contents of the {microshift-short} RPM release package
* Getting the published bootc image for {microshift-short}

[id="microshift-4-22-0-enhancement_{context}"]
== Enhancement

* With this release, the {microshift-short} certificate manager container images now reference platform-specific digests instead of multi-platform manifest lists. (OCPBUGS-66414)

//add module for each z-stream
