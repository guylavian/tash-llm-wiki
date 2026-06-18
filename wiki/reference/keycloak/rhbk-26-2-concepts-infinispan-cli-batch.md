---
title: "Chapter 7. Concepts to automate Data Grid CLI commands - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-concepts-infinispan-cli-batch
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-infinispan-cli-batch-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 7. Concepts to automate Data Grid CLI commands - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 7. Concepts to automate Data Grid CLI commands
Data Grid CLI commands can be automated by creating a `Batch` CR instance.
When interacting with an external Data Grid in Kubernetes, the Batch
CR allows you to automate this using standard oc
commands.
7.1. When to use it
Use this when automating interactions on Kubernetes. This avoids providing usernames and passwords and checking shell script outputs and their status.
For human interactions, the CLI shell might still be a better fit.
7.2. Example
The following Batch
CR takes a site offline as described in the operational procedure Taking a site offline.
apiVersion: infinispan.org/v2alpha1
kind: Batch
metadata:
name: take-offline
namespace: keycloak
spec:
cluster: infinispan
config: |
site take-offline --all-caches --site=site-a
site status --all-caches --site=site-a
Once the CR has been created, wait for the status to show the completion.
oc -n keycloak wait --for=jsonpath='{.status.phase}'=Succeeded Batch/take-offline
Modifying a Batch
CR instance has no effect. Batch operations are “one-time” events that modify Infinispan resources. To update .spec
fields for the CR, or when a batch operation fails, you must create a new instance of the Batch
CR.
7.3. Further reading
For more information, see the Data Grid Operator Batch
CR documentation.
