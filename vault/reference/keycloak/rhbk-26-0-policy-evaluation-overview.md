---
title: "Chapter 7. Evaluating and testing policies - Red Hat build of Keycloak 26.0 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-policy-evaluation-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/authorization_services_guide/policy_evaluation_overview
guide: authorization_services_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "When designing your policies, you can simulate authorization requests to test how your policies are being evaluated. You can access the Policy Evaluation Tool by clicking the Evaluate tab when editing a resource server. There you can specify different inputs to simulate real authorization requests and test the effect of your policies. Policy evaluation tool 7.1. Providing identity information The …"
---

# Chapter 7. Evaluating and testing policies - Red Hat build of Keycloak 26.0 Authorization Services Guide

Chapter 7. Evaluating and testing policies
When designing your policies, you can simulate authorization requests to test how your policies are being evaluated.
You can access the Policy Evaluation Tool by clicking the Evaluate
tab when editing a resource server. There you can specify different inputs to simulate real authorization requests and test the effect of your policies.
Policy evaluation tool
7.1. Providing identity information
The Identity Information filters can be used to specify the user requesting permissions.
7.2. Providing contextual information
The Contextual Information filters can be used to define additional attributes to the evaluation context, so that policies can obtain these same attributes.
7.3. Providing the permissions
The Permissions filters can be used to build an authorization request. You can request permissions for a set of one or more resources and scopes. If you want to simulate authorization requests based on all protected resources and scopes, click Add without specifying any Resources
or Scopes
.
When you’ve specified your desired values, click Evaluate.
