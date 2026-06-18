---
title: "Chapter 1. Red Hat build of Keycloak Operator installation - Red Hat build of Keycloak 26.2 Operator Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-installation
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/operator_guide/installation-
guide: operator_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 1. Red Hat build of Keycloak Operator installation - Red Hat build of Keycloak 26.2 Operator Guide

Chapter 1. Red Hat build of Keycloak Operator installation
How to install the Operator on OpenShift.
Use this procedure to install the Red Hat build of Keycloak Operator in an OpenShift cluster.
- Open the OpenShift Container Platform web console.
- In the left column, click Home, Operators, OperatorHub.
- Search for "Keycloak" on the search input box.
- Select the Operator from the list of results.
- Follow the instructions on the screen.
For general instructions on installing Operators by using either the CLI or web console, see Installing Operators in your namespace. In the default Catalog, the Operator is named rhbk-operator
. Make sure to use the channel corresponding with your desired Red Hat build of Keycloak version.
1.1. Configuring Manual Approval for OLM Upgrades
Important: Automatic OLM Upgrades
By default, OLM automatically updates the Red Hat build of Keycloak Operator when a new version is released. This can cause several significant issues:
- When using the default Red Hat build of Keycloak image, the Operator uses a matching image of the corresponding Red Hat build of Keycloak version, resulting in unintended Red Hat build of Keycloak upgrades when the Operator is upgraded
- Even when using custom images, major Operator upgrades can introduce significant compatibility issues with your existing Keycloak CR configuration, potentially requiring manual intervention
- New fields in Keycloak CR or behavioral changes could impact existing deployments
- No option to downgrade to the previous Red Hat build of Keycloak version due to changes related to database migration
Recommendation:
We strongly recommend using manual approval mode for the Red Hat build of Keycloak Operator. This ensures you can:
- Review release notes and follow migration changes before approving upgrades
- Schedule maintenance windows for upgrades
- Test upgrades in a non-production environment first
- Back up the database to allow downgrading to the previous Red Hat build of Keycloak in case of issues
To prevent automatic upgrades by OLM, set the approval strategy to Manual
when installing the Operator:
1.1.1. Using the OpenShift web console
When installing the Operator, select Manual
approval in the update approval strategy section:
1.1.2. Using the CLI
For command-line installation, create a Subscription with installPlanApproval: Manual
:
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
name: rhbk-operator
namespace: <target-namespace>
spec:
channel: <desired-channel>
name: rhbk-operator
source: redhat-operators
sourceNamespace: openshift-marketplace
installPlanApproval: Manual
After installation, any upgrade will require manual approval through the OLM interface or via the CLI.
1.2. Installing Multiple Operators
It is not fully supported for the operator to watch multiple or all namespaces. To watch multiple namespaces, you install multiple operators.
In this situation, consider the following:
- All Operators share the Custom Resource Definitions (CRDs) as they are installed cluster wide.
- CRD revisions from newer Operator versions will not introduce breaking changes except for the eventual removal of fields that have been deprecated for some time. Thus newer CRDs are generally backward compatible.
- The last installed CRDs become the ones that are used. This rule also applies to OLM installations; the last installed Operator version also installs and overrides the CRDs if they already exist in the cluster.
- Older CRDs may not be forward compatible with new fields used by newer operators. When using OLM it will check if your custom resources are compatible with the CRDs being installed, so the usage of new fields can prevent the simultaneous installation of older operator versions.
- Fields introduced by newer CRDs are not supported by older Operators. Older Operators fail to handle CRs that use such new fields with a deserialization error for an unrecognized field.
Therefore, in a multiple Operator installation scenario, the recommended approach is to keep versions aligned as closely as possible to minimize the potential problems with different versions.
