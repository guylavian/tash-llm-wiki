---
title: "Using Operators with {microshift-short}"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-operators
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-operators
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Using Operators with {microshift-short}

[id="microshift-operators"]
= Using Operators with {microshift-short}

[role="_abstract"]
You can use Operators with {microshift-short} to create applications that monitor the running services in your node. As customized software running inside your node, you can use Operators to implement and automate common operations.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators.adoc

[id="microshift-about-using-operators_{context}"]
= About using Operators with a {microshift-short} node

[role="_abstract"]
You can use Operators to manage applications and their resources, such as deploying a database or message bus.

Operators offer a more localized configuration experience and integrate with Kubernetes APIs and CLI tools such as `kubectl` and `oc`. You can design or use Operators that are specifically for your applications. By using Operators, you can configure components instead of modifying a global configuration file.

{microshift-short} applications are generally expected to be deployed in static environments. However, Operators are available if helpful in your use case. To discover whether an Operator is compatible with {microshift-short}, check the Operator documentation.

//Module included in the following assemblies:
//
//* microshift_running_apps/microshift_operators/microshift-operators.adoc

[id="microshift-operators-how-to-install-and-manage_{context}"]
= How to use Operators with a {microshift-short} node

[role="_abstract"]
There are two ways to install and manage Operators for your {microshift-short} node. You can use manifests or Operator Lifecycle Manager (OLM).

[id="microshift-operators-paths-manifests_{context}"]
== Manifests for Operators

You can install and manage Operators directly by using manifests. You can use the `kustomize` configuration management tool with {microshift-short} to deploy an application. Use the same steps to install Operators with manifests. For more information, see the following links:

* Using Kustomize manifests to deploy applications
* Using manifests example

[id="microshift-operators-paths-olm_{context}"]
== Operator Lifecycle Manager for Operators

You can also install add-on Operators to a {microshift-short} node by using Operator Lifecycle Manager (OLM). OLM can be used to manage both custom Operators and Operators that are widely available. Building catalogs is required to use OLM with {microshift-short}. For more information, see the following Using Operator Lifecycle Manager with {microshift-short}
