---
title: "Configuring JSON Web Token authentication for Knative services"
type: reference
domain: openshift
slug: serverless-4-22-serverless-ossm-with-kourier-jwt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-ossm-with-kourier-jwt
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Configuring JSON Web Token authentication for Knative services

[id="serverless-ossm-with-kourier-jwt"]
= Configuring JSON Web Token authentication for Knative services

{ServerlessProductName} does not currently have user-defined authorization features. To add user-defined authorization to your deployment, you must integrate {ServerlessProductName} with {SMProductName}, and then configure JSON Web Token (JWT) authentication and sidecar injection for Knative services.
