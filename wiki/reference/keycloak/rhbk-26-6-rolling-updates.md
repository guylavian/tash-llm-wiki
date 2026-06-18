---
title: "Chapter 5. Avoiding downtime with rolling updates - Red Hat build of Keycloak 26.6 Operator Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-rolling-updates
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/operator_guide/rolling-updates-
guide: operator_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Avoid downtime when changing themes, providers, or configurations in optimized images. By default, the Red Hat build of Keycloak Operator will perform rolling updates on configuration changes without downtime, and recreate updates with downtime when the image name or tag changes. This chapter describes how to minimize downtimes by configuring the Red Hat build of Keycloak Operator to perform rolli…"
---

# Chapter 5. Avoiding downtime with rolling updates - Red Hat build of Keycloak 26.6 Operator Guide

Chapter 5. Avoiding downtime with rolling updates
Avoid downtime when changing themes, providers, or configurations in optimized images.
By default, the Red Hat build of Keycloak Operator will perform rolling updates on configuration changes without downtime, and recreate updates with downtime when the image name or tag changes.
This chapter describes how to minimize downtimes by configuring the Red Hat build of Keycloak Operator to perform rolling updates of Red Hat build of Keycloak automatically where possible, and how to override automatic detection for rolling updates.
Use it, for example, avoid downtimes when rolling out
- an update to a theme,
- provider or build time configuration in a custom or optimized image, or
- patch releases of Red Hat build of Keycloak.
5.1. Supported Update Strategies
The Operator supports the following update strategies:
- Rolling Updates
- Update the StatefulSet in a rolling fashion, avoiding a downtime when at least two replicas are running.
- Recreate Updates
- Scale down the StatefulSet before applying updates, causing temporary downtime.
5.2. Configuring the Update Strategy
Specify the update strategy within the spec
section of the Keycloak CR YAML definition:
apiVersion: k8s.keycloak.org/v2beta1
kind: Keycloak
metadata:
name: example-kc
spec:
update:
strategy: RecreateOnImageChange|Auto|Explicit
revision: "abc"
| Value | Downtime? | Description |
|---|---|---|
|
| On image name or tag change | Mimics Red Hat build of Keycloak 26.1 or older behavior. When the image field changes, the Operator scales down the StatefulSet before applying the new image. |
|
| On incompatible changes | The Red Hat build of Keycloak Operator detects if a rolling or recreate update is possible.
Red Hat build of Keycloak supports rolling updates for patch releases. It performs a rolling update if the Red Hat build of Keycloak version is the same or when upgrading to a newer patch version in the same |
|
|
Only the |
The Red Hat build of Keycloak Operator checks the |
5.2.1. Understanding Auto and Explicit Update Strategies
When using the Auto
update strategy, the Red Hat build of Keycloak Operator automatically starts a Job to assess the feasibility of a rolling update. Read more about the process in the Checking if rolling updates are possible chapter. This process consumes cluster resources for the time of the check and introduces a slight delay before the StatefulSet update begins.
If the Keycloak CR configured a podTemplate
as part of the unsupported
configuration parameters, the Keycloak Operator will do its best to use those settings for the started Job. Still it might miss some settings due to the flexibility of the podTemplate
feature and its unsupported nature.
As a consequence, the Operator might draw the wrong conclusions if a rolling update is possible from changes to the podTemplate
or information pulled in from Secrets, ConfigMaps or Volumes in the podTemplate
.
Therefore, if you are using the unsupported podTemplate
, you may need to use one of the other update strategies.
The Explicit
update strategy delegates the update decision to the user. The revision
field acts as a user-controlled trigger. While the Red Hat build of Keycloak Operator does not interpret the revision
value itself, any change to the Custom Resource (CR) while the revision
remains unchanged will prompt a rolling update.
Exercise caution when using this with automatic Operator upgrades. The Operator Lifecycle Manager (OLM) may upgrade the Red Hat build of Keycloak Operator, and if the Explicit
update strategy is in use, this could lead to unexpected behavior or deployment failures as the Operator would attempt a rolling update when this is actually not supported. If you are using the Explicit
update strategy, thorough testing in a non-production environment is highly recommended before upgrading.
5.2.2. CR Statuses
The Keycloak CR status of RecreateUpdateUsed
indicates the update strategy employed during the last update operation. The lastTransitionTime
field indicates when the last update occurred. Use this information to observe actions and decisions taken by the Operator.
| Status | Description |
|---|---|
|
| The initial state. It means no update has taken place. |
|
| The Operator applied the rolling update strategy in the last update. |
|
|
The Operator applied the recreate update strategy in the last update. The |
