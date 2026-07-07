---
title: "Optional capabilities and products in the web console"
type: reference
domain: openshift
slug: web-console-4-22-capabilities-products-web-console
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/capabilities_products-web-console
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Optional capabilities and products in the web console

[id="capabilities-products-web-console"]
= Optional capabilities and products in the web console

[role="_abstract"]
You can further customize the OpenShift Container Platform web console by adding additional capabilities to your existing workflows and integrations through products.

// Module included in the following assemblies:
//
// * capabilities-web-console.adc

[id="optional-capabilities-operators_{context}"]
=  Enhancing the OpenShift Container Platform web console with Operators

[role="_abstract"]
Cluster administrators can install Operators on clusters in the OpenShift Container Platform web console by using the software catalog to provide customization outside of layered products for developers. For example, the Web Terminal Operator allows you to start a web terminal in your browser with common CLI tools for interacting with the cluster.
//OpenShift LightSpeed
// Module included in the following assemblies:
//
// * capabilities-web-console.adc

[id="openshift-lightspeed-web-console_{context}"]
= {ols-official} in the web console

[role="_abstract"]
{ols-official} is a generative artificial intelligence-powered virtual assistant for OpenShift Container Platform. {ols} functionality uses a natural-language interface in the OpenShift Container Platform web console.

This early access program exists so that customers can provide feedback on the user experience, features and capabilities, issues encountered, and any other aspects of the product so that {ols} can become more aligned with your needs when it is released and made generally available.
//pipelines
// Module included in the following assemblies:
//
// * products-web-console.adoc

[id="pipelines-web-console_{context}"]
= {pipelines-title} in the web console

[role="_abstract"]
{pipelines-title} is a cloud-native, continuous integration and continuous delivery (CI/CD) solution based on Kubernetes resources. Install the {pipelines-title} Operator using the software catalog in the OpenShift Container Platform web console. Once the Operator is installed, you can create and modify pipeline objects on *Pipelines* page.
//serverless
// Module included in the following assemblies:
//
// * products-web-console.adoc

[id="using-serverless-with-openshift_{context}"]
= Red Hat {serverlessproductname} in the web console

[role="_abstract"]
Red Hat {serverlessproductname} enables developers to create and deploy serverless, event-driven applications on OpenShift Container Platform. You can use the OpenShift Container Platform web console software catalog to install the {serverlessproductname} Operator.
//RHDH
// Module included in the following assemblies:
//
// * capabilities_products-web-console.adoc

[id="rhdh-web-console_{context}"]
= {rh-dev-hub} in the OpenShift Container Platform web console

[role="_abstract"]
The {rh-dev-hub} is a platform you can use to experience a streamlined development environment. {rh-dev-hub} is driven by a centralized software catalog, providing efficiency to your microservices and infrastructure. It enables your product team to deliver quality code without any compromises. A quick start is available for you to learn more about how to install the developer hub.
// Module included in the following assemblies:
//
// * capabilities_products-web-console.adoc

[id="rhdh-install-web-console_{context}"]
=  Installing the {rh-dev-hub} using the OpenShift Container Platform web console

[role="_abstract"]
The web console provides a quick start with instructions on how to install the {rh-dev-hub} Operator.

.Prerequisites
* You must be logged in to the OpenShift Container Platform web console with `cluster-admin` privileges.

.Procedure
. On the *Overview* page, click *Install {rh-dev-hub} (RHDH) with an Operator* in the *Getting started resources* tile.
. A quick start pane is displayed with instructions for you to install the {rh-dev-hub} with an Operator. Follow the quick start for instructions on how to install the Operator, create a {rh-dev-hub} instance, and add your instance to the *OpenShift Console Application* menu.

.Verification
. You can click the *Application launcher* link that is displayed to verify your *Application* tab is available.
. Verify your Janus IDP instance can be opened.

[role="_additional-resources"]
.Additional resources
* Understanding the software catalog
* Installing the web terminal
* {ols} overview
* Installing {ols}
* Working with {pipelines-title} in the web console
* Pipeline execution statistics in the web console
* Installing the {ServerlessProductName} Operator from the web console
* Product Documentation for {rh-dev-hub}

//RHTaP
//Concept module explaining dance and why its useful.
//[role="_additional-resources"]
//.Additional resources
//Link out to dance docs when it comes to it.
