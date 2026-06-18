---
title: "Chapter 2. Before You Begin - Red Hat Single Sign-On 7.3 Red Hat Single Sign-On for OpenShift"
type: reference
domain: keycloak
slug: rhsso-7-3-before-you-begin
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.3/html/red_hat_single_sign-on_for_openshift/before_you_begin
version: 7.3
family: rhsso
documentKind: "Documentation"
abstract: "2.1. Comparison: Red Hat Single Sign-On for OpenShift Image and Red Hat Single Sign-On The Red Hat Single Sign-On for OpenShift image version number 7.3.8.GA is based on Red Hat Single Sign-On 7.3.8.GA. There are some differences in functionality between the Red Hat Single Sign-On for OpenShift image and Red Hat Single Sign-On: The Red Hat Single Sign-On for OpenShift image includes all of the fun…"
---

# Chapter 2. Before You Begin - Red Hat Single Sign-On 7.3 Red Hat Single Sign-On for OpenShift

Chapter 2. Before You Begin
2.1. Comparison: Red Hat Single Sign-On for OpenShift Image and Red Hat Single Sign-On
The Red Hat Single Sign-On for OpenShift image version number 7.3.8.GA is based on Red Hat Single Sign-On 7.3.8.GA. There are some differences in functionality between the Red Hat Single Sign-On for OpenShift image and Red Hat Single Sign-On:
- The Red Hat Single Sign-On for OpenShift image includes all of the functionality of Red Hat Single Sign-On. In addition, the Red Hat Single Sign-On-enabled JBoss EAP image automatically handles OpenID Connect or SAML client registration and configuration for .war deployments that contain <auth-method>KEYCLOAK</auth-method> or <auth-method>KEYCLOAK-SAML</auth-method> in their respective web.xml files.
2.2. Version Compatibility and Support
See the xPaaS part of the OpenShift and Atomic Platform Tested Integrations page for details about OpenShift image version compatibility.
2.3. Deprecated Image Streams and Application Templates for Red Hat Single Sign-On for OpenShift
The Red Hat Single Sign-On for OpenShift image version number 7.0 and 7.1 are deprecated and they will no longer receive updates of image and application templates.
To deploy new applications, it is recommended to use the version 7.2 or 7.3.8.GA of the Red Hat Single Sign-On for OpenShift image along with the application templates specific to these image versions.
2.4. Initial Setup
The Tutorials in this guide follow on from and assume an OpenShift instance similar to that created by performing the installation of the OpenShift Container Platform cluster.
For information related to updating the existing database when migrating Red Hat Single Sign-On for OpenShift image from previous versions to version 7.3.8.GA, see the Updating Existing Database when Migrating Red Hat Single Sign-On for OpenShift Image to a new version section.
