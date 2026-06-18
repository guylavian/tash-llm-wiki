---
title: "Appendix B. Generating Keycloak host names automatically - Red Hat Trusted Artifact Signer 1.1 Deployment Guide"
type: reference
domain: keycloak
slug: doc-generating-keycloak-host-names-automatically-deploy
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_trusted_artifact_signer/1.1/html/deployment_guide/generating-keycloak-host-names-automatically_deploy
guide: deployment_guide
documentKind: "Documentation"
---

# Appendix B. Generating Keycloak host names automatically - Red Hat Trusted Artifact Signer 1.1 Deployment Guide

Appendix B. Generating Keycloak host names automatically
OpenShift routes has support for automatically generating host names by using a set pattern. This feature can integrate with Red Hat’s build of Keycloak (RHBK) operator running on OpenShift.
Prerequisites
- Red Hat OpenShift Container Platform version 4.13 or later.
- Installation of the RHBK operator.
-
Access to the OpenShift web console with the
cluster-admin
role. -
A workstation with the
oc
binary installed.
Procedure
Enable the automatically generated route hostname feature.
Under the
.spec
section, remove the entirehostname
section, and replace it with theingress
section andclassName
property within theKeycloak
resource:Example
spec: ... hostname: hostname: example.com ...
Example
spec: ... ingress: className: openshift-default ...
NoteTo view all of the available Ingress classes, run the following command:
$ oc get ingressclass
- Click the Save button.
Verify the automatically generated
hostname
by clicking the Reload button to view the latest configuration:Example
spec: ... hostname: hostname: example-keycloak-ingress-keycloak-system.apps.rhtas.example.com ...
