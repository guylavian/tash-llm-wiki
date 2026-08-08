---
title: "Chapter 6. Using custom Red Hat build of Keycloak images - Red Hat build of Keycloak 26.2 Operator Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-customizing-keycloak
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/operator_guide/customizing-keycloak-
guide: operator_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "Customize and optimize the Red Hat build of Keycloak container. 6.1. Red Hat build of Keycloak custom image with the Operator With the Keycloak Custom Resource (CR), you can specify a custom container image for the Red Hat build of Keycloak server. Note To ensure full compatibility of Operator and Operand, make sure that the version of Red Hat build of Keycloak release used in the custom image is …"
---

# Chapter 6. Using custom Red Hat build of Keycloak images - Red Hat build of Keycloak 26.2 Operator Guide

Chapter 6. Using custom Red Hat build of Keycloak images
Customize and optimize the Red Hat build of Keycloak container.
6.1. Red Hat build of Keycloak custom image with the Operator
With the Keycloak Custom Resource (CR), you can specify a custom container image for the Red Hat build of Keycloak server.
To ensure full compatibility of Operator and Operand, make sure that the version of Red Hat build of Keycloak release used in the custom image is aligned with the version of the operator.
6.1.1. Best practice
When using the default Red Hat build of Keycloak image, the server will perform a costly re-augmentation every time a Pod starts. To avoid this delay, you can provide a custom image with the augmentation built-in from the build time of the image.
With a custom image, you can also specify the Keycloak build-time configurations and extensions during the build of the container.
When using the optimized custom image, health-enabled
and metrics-enabled
options need to be explicitly set in the Containerfile.
For instructions on how to build such an image, see Running Red Hat build of Keycloak in a container.
6.1.2. Providing a custom Red Hat build of Keycloak image
To provide a custom image, you define the image
field in the Keycloak CR as shown in this example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
instances: 1
image: quay.io/my-company/my-keycloak:latest
http:
tlsSecret: example-tls-secret
hostname:
hostname: test.keycloak.org
With custom images, every build time option passed either through a dedicated field or the additionalOptions
is ignored.
The Operator is unaware of any configuration options that are specified in a custom image. Use the Keycloak CR for any configuration that requires Operator awareness, namely the TLS and HTTP(S) settings reflected when configuring services and probes.
6.1.3. Non-optimized custom image
While it is considered a best practice to use a pre-augmented image, if you want to use a non-optimized custom image or build time properties with an augmented image that is still possible. You just need set the startOptimized
field to false
as shown in this example:
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
name: example-kc
spec:
instances: 1
image: quay.io/my-company/my-keycloak:latest
startOptimized: false
http:
tlsSecret: example-tls-secret
hostname:
hostname: test.keycloak.org
Keep in mind this will incur the re-augmentation cost on every start.
