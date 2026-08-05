---
title: "{gitops-title} release notes"
type: reference
domain: openshift
slug: cicd-4-22-gitops-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/gitops-release-notes
version: 4.22
family: cicd
documentKind: "Documentation"
---

# {gitops-title} release notes

//OpenShift GitOps Release Notes
[id="gitops-release-notes"]
= {gitops-title} release notes

[role="_abstract"]
{gitops-title} is a declarative way to implement continuous deployment for cloud native applications. {gitops-title} ensures consistency in applications when you deploy them to different clusters in different environments, such as: development, staging, and production. {gitops-title} helps you automate the following tasks:

* Ensure that the clusters have similar states for configuration, monitoring, and storage
* Recover or recreate clusters from a known state
* Apply or revert configuration changes to multiple OpenShift Container Platform clusters
* Associate templated configuration with different environments
* Promote applications across clusters, from staging to production

For an overview of {gitops-title}, see Understanding OpenShift GitOps.

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="GitOps-compatibility-support-matrix_{context}"]
= Compatibility and support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

In the table, features are marked with the following statuses:

* *TP*: _Technology Preview_
* *GA*: _General Availability_
* *NA*: _Not Applicable_

[IMPORTANT]
====
In OpenShift Container Platform 4.13, the `stable` channel has been removed. Before upgrading to OpenShift Container Platform 4.13, if you are already on the `stable` channel, choose the appropriate channel and switch to it.
====

|===
|*OpenShift GitOps* 7+|*Component Versions*|*OpenShift Versions*

|*Version* |*`kam`*    |*Helm*  |*Kustomize* |*Argo CD*|*ApplicationSet* |*Dex*     |*RH SSO* |
|1.9.0    |0.0.49 TP |3.11.2 GA|5.0.1 GA   |2.7.2 GA |NA     |2.35.1 GA |7.5.1 GA |4.12-4.13
|1.8.0    |0.0.47 TP |3.10.0 GA|4.5.7 GA   |2.6.3 GA |NA     |2.35.1 GA |7.5.1 GA |4.10-4.13
|1.7.0    |0.0.46 TP |3.10.0 GA|4.5.7 GA   |2.5.4 GA |NA     |2.35.1 GA |7.5.1 GA |4.10-4.12
|1.6.0    |0.0.46 TP |3.8.1 GA|4.4.1 GA   |2.4.5 GA |GA and included in ArgoCD component    |2.30.3 GA |7.5.1 GA |4.8-4.11
|1.5.0    |0.0.42 TP|3.8.0 GA|4.4.1 GA   |2.3.3 GA |0.4.1 TP       |2.30.3 GA |7.5.1 GA |4.8-4.11
|1.4.0    |0.0.41 TP|3.7.1 GA|4.2.0 GA   |2.2.2 GA |0.2.0 TP       |2.30.0 GA |7.4.0 GA |4.7-4.10
|1.3.0    |0.0.40 TP|3.6.0 GA|4.2.0 GA   |2.1.2 GA |0.2.0 TP       |2.28.0 GA |7.4.0 GA |4.7-4.9, 4.6 with limited GA support
|1.2.0    |0.0.38 TP |3.5.0 GA |3.9.4 GA  |2.0.5 GA |0.1.0 TP      |NA |7.4.0 GA|4.8
|1.1.0    |0.0.32 TP |3.5.0 GA |3.9.4 GA  |2.0.0 GA |NA            |NA |NA |4.7
|===

* `kam` is the {gitops-title} Application Manager command-line interface (CLI).
* RH SSO is an abbreviation for Red Hat SSO.

// Writer, to update this support matrix, refer to https://spaces.redhat.com/display/GITOPS/GitOps+Component+Matrix

[id="GitOps-technology-preview_{context}"]
== Technology Preview features

The features mentioned in the following table are currently in Technology Preview (TP). These experimental features are not intended for production use.

.Technology Preview tracker
[cols="4,1,1",options="header"]
|====
|Feature |TP in {gitops-title} versions|GA in {gitops-title} versions

|The custom `must-gather` tool
|1.9.0
|NA

|Argo Rollouts
|1.9.0
|NA

|ApplicationSet Progressive Rollout Strategy
|1.8.0
|NA

|Multiple sources for an application
|1.8.0
|NA

|Argo CD applications in non-control plane namespaces
|1.7.0
|NA

|Argo CD Notifications controller
|1.6.0
|NA

|The {gitops-title} *Environments* page in the *Developer* perspective of the OpenShift Container Platform web console
|1.1.0
|NA
|====

// Modules included, most to least recent
// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
[id="gitops-release-notes-1-9-0_{context}"]
= Release notes for {gitops-title} 1.9.0

{gitops-title} 1.9.0 is now available on OpenShift Container Platform 4.12 and 4.13.

[id="errata-updates-1-9-0_{context}"]
== Errata updates

=== RHSA-2023:112944 - {gitops-title} 1.9.0 security update advisory

Issued: 2023-06-09

The list of security fixes that are included in this release is documented in the following advisory:

* RHSA-2023:112944

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

[id="new-features-1-9-0_{context}"]
== New features

The current release adds the following improvements:

* With this update, you can use a custom `must-gather` tool to collect diagnostic information for project-level resources, cluster-level resources, and {gitops-title} components. This tool provides the debugging information about the cluster associated with {gitops-title}, which you can share with the Red Hat Support team for analysis. GITOPS-2797
+
[IMPORTANT]
====
The custom `must-gather` tool is a Technology Preview feature.
====

* With this update, you can add support to progressive delivery using Argo Rollouts. Currently, the supported traffic manager is only {SMProductName}. GITOPS-959
+
[IMPORTANT]
====
Argo Rollouts is a Technology Preview feature.
====

[role="_additional-resources"]
.Additional resources
* Using Argo Rollouts

[id="deprecated-features-1-9-0_{context}"]
== Deprecated and removed features

* In {gitops-title} 1.7.0,  the `.spec.resourceCustomizations` parameter was deprecated. The deprecated `.spec.resourceCustomizations` parameter is planned to be removed in the upcoming {gitops-title} GA v1.10.0 release. You can use the new formats `spec.ResourceHealthChecks`, `spec.ResourceIgnoreDifferences`, and `spec.ResourceActions` instead. GITOPS-2890

* With this update, the support for the following deprecated `sso` and `dex` fields extends until the upcoming {gitops-title} GA v1.10.0 release:
+
** The `.spec.sso.image`, `.spec.sso.version`, `.spec.sso.resources`, and `.spec.sso.verifyTLS` fields.
** The `.spec.dex` parameter along with `DISABLE_DEX`.
+
The deprecated previous `sso` and `dex` fields were earlier scheduled for removal in the {gitops-title} v1.9.0 release but are now planned to be removed in the upcoming {gitops-title} GA v1.10.0 release.
GITOPS-2904

[id="fixed-issues-1-9-0_{context}"]
== Fixed issues
The following issues have been resolved in the current release:

* Before this update, when the `argocd-server-tls` secret was updated with a new certificate Argo CD was not always picking up this secret. As a result, the old expired certificate was presented. This update fixes the issue with a new `GetCertificate` function and ensures that the latest version of certificates is in use. When adding new certificates, now Argo CD picks them up automatically without the user having to restart the `argocd-server` pod. GITOPS-2375

* Before this update, when enforcing GPG signature verification against a `targetRevision` integer pointing to a signed Git tag, users got a `Target revision in Git is not signed` error. This update fixes the issue and lets users enforce GPG signature verification against signed Git tags. GITOPS-2418

* Before this update, users could not connect to Microsoft Team Foundation Server (TFS) type Git repositories through Argo CD deployed by the Operator. This update fixes the issue by updating the Git version to
2.39.3 in the Operator. GITOPS-2768

* Before this update, when the Operator was deployed and running with the High availability (HA) feature enabled, setting resource limits under the `.spec.ha.resources` field did not affect Redis HA pods. This update fixes the reconciliation by adding checks in the Redis reconciliation code. These checks ensure whether the `spec.ha.resources` field in the Argo CD custom resource (CR) is updated. When the Argo CD CR is updated with new CPU and memory requests or limit values for HA, now these changes are applied to the Redis HA pods. GITOPS-2404

* Before this update, if a namespace-scoped Argo CD instance was managing multiple namespaces by using the `managed-by` label and one of those managed namespaces was in a *Terminating* state, the Argo CD instance could not deploy resources to all other managed namespaces. This update fixes the issue by enabling the Operator to remove the `managed-by` label from any previously managed now terminating namespace. Now, a terminating namespace managed by a namespace-scoped Argo CD instance does not block the deployment of resources to other managed namespaces. GITOPS-2627

[id="known-issues-1-10_{context}"]
== Known issues
* Currently, the Argo CD does not read the Transport Layer Security (TLS) certificates from the path specified in the `argocd-tls-certs-cm` config map resulting in the `x509: certificate signed by unknown authority` error.
+
Workaround: Perform the following steps:

. Add the `SSL_CERT_DIR` environment variable:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
   ...
  repo:
    env:
      - name: SSL_CERT_DIR
        value: /tmp/sslcertdir
    volumeMounts:
      - name: ssl
        mountPath: /tmp/sslcertdir
    volumes:
      - name: ssl
        configMap:
          name: user-ca-bundle
   ...
----

. Create an empty config map in the namespace where the subscription for your Operator exists and include the following label:
+
.Example config map

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-ca-bundle <1>
  labels:
    config.openshift.io/inject-trusted-cabundle: "true" <2>
----
<1> Name of the config map.
<2> Requests the Cluster Network Operator to inject the merged bundle.
+
After creating this config map, the `user-ca-bundle` content from the `openshift-config` namespace automatically gets injected into this config map, even merged with the system ca-bundle. GITOPS-1482
// 1.25.0 additional resources, OCP docs
[role="_additional-resources"]
.Additional resources
* Injecting a custom CA certificate

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
[id="gitops-release-notes-1-8-4_{context}"]
= Release notes for {gitops-title} 1.8.4

{gitops-title} 1.8.4 is now available on OpenShift Container Platform 4.10, 4.11, 4.12, and 4.13.

[id="new-features-1-8-4_{context}"]
== New features

The current release adds the following improvements:

* With this update, the bundled Argo CD has been updated to version 2.6.13.

[id="fixed-issues-1-8-4_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, Argo CD was becoming unresponsive when there was an increase in namespaces and applications. The functions competing for resources caused a deadlock. This update fixes the issue by removing the deadlock. Now, you should not experience crashes or unresponsiveness when there is an increase in namespaces or applications. GITOPS-3192

* Before this update, the Argo CD application controller resource could suddenly stop working when resynchronizing applications. This update fixes the issue by adding logic to prevent a cluster cache deadlock. Now, applications should resynchronize successfully. GITOPS-3052

* Before this update, there was a mismatch in the RSA key for known hosts in the `argocd-ssh-known-hosts-cm` config map. This update fixes the issue by matching the RSA key with the upstream project. Now, you can use the default RSA keys on default deployments. GITOPS-3144

* Before this update, an old Redis image version was used when deploying the {gitops-title} Operator, which resulted in vulnerabilities. This update fixes the vulnerabilities on Redis by upgrading it to the latest version of the `registry.redhat.io/rhel-8/redis-6` image. GITOPS-3069

* Before this update, users could not connect to Microsoft Team Foundation Server (TFS) type Git repositories through Argo CD deployed by the Operator. This update fixes the issue by updating the Git version to 2.39.3 in the Operator. Now, you can set the `Force HTTP basic auth` flag during repository configurations to connect with the TFS type Git repositories. GITOPS-1315

[id="known-issues-1-8-4_{context}"]
== Known issues

* Currently, {gitops-title} 1.8.4 is not available in the `latest` channel of OpenShift Container Platform 4.10 and 4.11. The `latest` channel is taken by {gitops-shortname} 1.9.z, which is only released on OpenShift Container Platform 4.12 and later versions.
+
As a workaround, switch to the `gitops-1.8` channel to get the new update. GITOPS-3158

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
[id="gitops-release-notes-1-8-3_{context}"]
= Release notes for {gitops-title} 1.8.3

{gitops-title} 1.8.3 is now available on OpenShift Container Platform 4.10, 4.11, 4.12, and 4.13.

[id="errata-updates-1-8-3_{context}"]
== Errata updates

=== RHBA-2023:3206 and RHSA-2023:3229 - {gitops-title} 1.8.3 security update advisory

Issued: 2023-05-18

The list of security fixes that are included in this release is documented in the following advisories:

* RHBA-2023:3206
* RHSA-2023:3229

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

[id="fixed-issues-1-8-3_{context}"]
== Fixed issues

* Before this update, when `Autoscale` was enabled and the horizontal pod autoscaler (HPA) controller tried to edit the replica settings in server deployment, the Operator overwrote it. In addition, any changes specified to the autoscaler parameters were not propagated correctly to the HPA on the cluster. This update fixes the issue. Now the Operator reconciles on replica drift only if `Autoscale` is disabled and the HPA parameters are updated correctly. GITOPS-2629

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
[id="gitops-release-notes-1-8-2_{context}"]
= Release notes for {gitops-title} 1.8.2

{gitops-title} 1.8.2 is now available on OpenShift Container Platform 4.10, 4.11, 4.12, and 4.13.

[id="fixed-issues-1-8-2_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, when you configured Dex using the `.spec.dex` parameter and tried to log in to the Argo CD UI by using the *LOG IN VIA OPENSHIFT* option, you were not able to log in. This update fixes the issue.
+
[IMPORTANT]
====
The `spec.dex` parameter in the ArgoCD CR is deprecated. In a future release of {gitops-title} v1.9, configuring Dex using the `spec.dex` parameter in the ArgoCD CR is planned to be removed. Consider using the `.spec.sso` parameter instead. See "Enabling or disabling Dex using .spec.sso".  GITOPS-2761
====

* Before this update, the cluster and `kam` CLI pods failed to start with a new installation of {gitops-title} v1.8.0 on the OpenShift Container Platform 4.10 cluster. This update fixes the issue and now all pods run as expected. GITOPS-2762

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-8-1_{context}"]
= Release notes for {gitops-title} 1.8.1

{gitops-title} 1.8.1 is now available on OpenShift Container Platform 4.10, 4.11, 4.12, and 4.13.

[id="errata-updates-1-8-1_{context}"]
== Errata updates

=== RHSA-2023:1452 - {gitops-title} 1.8.1 security update advisory

Issued: 2023-03-23

The list of security fixes that are included in this release is documented in the RHSA-2023:1452 advisory.

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-8-0_{context}"]
= Release notes for {gitops-title} 1.8.0

{gitops-title} 1.8.0 is now available on OpenShift Container Platform 4.10, 4.11, 4.12, and 4.13.

[id="new-features-1-8-0_{context}"]
== New features

The current release adds the following improvements:

* With this update,  you can add support for the ApplicationSet Progressive Rollout Strategy feature. Using this feature, you can enhance the ArgoCD ApplicationSet resource to embed a rollout strategy for a progressive application resource update after you modify the ApplicationSet spec or Application templates. When you enable this feature, applications are updated in a declarative order instead of simultaneously. GITOPS-956
+
[IMPORTANT]
====
ApplicationSet Progressive Rollout Strategy is a Technology Preview feature.
====
//https://github.com/argoproj/argo-cd/pull/12103

* With this update, the *Application environments* page in the *Developer* perspective of the OpenShift Container Platform web console is decoupled from the {gitops-title} Application Manager command-line interface (CLI), `kam`. You do not have to use the `kam` CLI to generate Application Environment manifests for the environments to show up in the *Developer* perspective of the OpenShift Container Platform web console. You can use your own manifests, but the environments must still be represented by namespaces. In addition, specific labels and annotations are still needed. GITOPS-1785

* With this update, the {gitops-title} Operator and the `kam` CLI are now available to use on ARM architecture on OpenShift Container Platform. GITOPS-1688
+
[IMPORTANT]
====
`spec.sso.provider: keycloak` is not yet supported on ARM.
====

* With this update, you can enable workload monitoring for specific Argo CD instances by setting the `.spec.monitoring.enabled` flag value to `true`. As a result, the Operator creates a `PrometheusRule` object that contains alert rules for each Argo CD component. These alert rules trigger an alert when the replica count of the corresponding component has drifted from the desired state for a certain amount of time. The Operator will not overwrite the changes made to the `PrometheusRule` object by the users. GITOPS-2459

* With this update, you can pass command arguments to the repo server deployment using the Argo CD CR. GITOPS-2445
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  repo:
    extraRepoCommandArgs:
      - --max.combined.directory.manifests.size
      - 10M
----

[id="fixed-issues-1-8-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, you could set the `ARGOCD_GIT_MODULES_ENABLED` environment variable only on the `openshift-gitops-repo-server` pod and not on the `ApplicationSet Controller` pod. As a result, when using the Git generator, Git submodules were cloned during the generation of child applications because the variable was missing from the `ApplicationSet Controller` environment. In addition, if the credentials required to clone these submodules were not configured in ArgoCD, the application generation failed. This update fixes the issue; you can now add any environment variables such as `ArgoCD_GIT_MODULES_ENABLED` to the `ApplicationSet Controller` pod using the Argo CD CR. The `ApplicationSet Controller` pod then successfully generates child applications from the cloned repository and no submodule is cloned in the process. GITOPS-2399
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  applicationSet:
    env:
     - name: ARGOCD_GIT_MODULES_ENABLED
       value: "true"
----

* Before this update, while installing the {gitops-title} Operator v1.7.0, the default `argocd-cm.yml` config map file created for authenticating Dex contained the base64-encoded client secret in the format of a `key:value` pair. This update fixes this issue by not storing the client secret in the default `argocd-cm.yml` config map file. Instead, the client secret is inside an `argocd-secret` object now, and you can reference it inside the configuration map as a secret name. GITOPS-2570

[id="known-issues-1-8-0_{context}"]
== Known issues

* When you deploy applications using your manifests without using the `kam` CLI and view the applications in the *Application environments* page in the *Developer* perspective of the OpenShift Container Platform web console, the Argo CD URL to the corresponding application does not load the page as expected from the Argo CD icon in the card. GITOPS-2736

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-7-3_{context}"]
= Release notes for {gitops-title} 1.7.3

{gitops-title} 1.7.3 is now available on OpenShift Container Platform 4.10, 4.11, and 4.12.

[id="errata-updates-1-7-3_{context}"]
== Errata updates

=== RHSA-2023:1454 - {gitops-title} 1.7.3 security update advisory

Issued: 2023-03-23

The list of security fixes that are included in this release is documented in the RHSA-2023:1454 advisory.

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-7-1_{context}"]
= Release notes for {gitops-title} 1.7.1

{gitops-title} 1.7.1 is now available on OpenShift Container Platform 4.10, 4.11, and 4.12.

[id="errata-updates-1-7-1_{context}"]
== Errata updates

=== RHSA-2023:0467 - {gitops-title} 1.7.1 security update advisory

Issued: 2023-01-25

The list of security fixes that are included in this release is documented in the RHSA-2023:0467 advisory.

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-7-0_{context}"]
= Release notes for {gitops-title} 1.7.0

{gitops-title} 1.7.0 is now available on OpenShift Container Platform 4.10, 4.11, and 4.12.

[id="new-features-1-7-0_{context}"]
== New features

The current release adds the following improvements:

* With this update, you can add environment variables to the Notifications controller. GITOPS-2313

* With this update, the default nodeSelector `"kubernetes.io/os": "linux"` key-value pair is added to all workloads such that they only schedule on Linux nodes. In addition, any custom node selectors are added to the default and take precedence if they have the same key. GITOPS-2215

* With this update, you can set custom node selectors in the Operator workloads by editing their `GitopsService` custom resource. GITOPS-2164

* With this update, you can use the RBAC policy matcher mode to select from the following options: `glob` (default) and `regex`.GITOPS-1975

* With this update, you can customize resource behavior using the following additional subkeys:
+
[options=header]
|===
| Subkey | Key form | Mapped field in argocd-cm
| resourceHealthChecks | resource.customizations.health.<group_kind> | resource.customizations.health
| resourceIgnoreDifferences | resource.customizations.ignoreDifferences.<group_kind> | resource.customizations.ignoreDifferences
| resourceActions | resource.customizations.actions.<group_kind> | resource.customizations.actions
|===
+
GITOPS-1561
+
[NOTE]
====
In future releases, there is a possibility to deprecate the old method of customizing resource behavior by using only resourceCustomization and not subkeys.
====

* With this update, to use the *Environments* page in the *Developer* perspective, you must upgrade if you are using a {gitops-title} version prior to 1.7 and OpenShift Container Platform 4.15 or above. GITOPS-2415

* With this update, you can create applications, which are managed by the same control plane Argo CD instance, in any namespace in the same cluster. As an administrator, perform the following actions to enable this update:
** Add the namespace to the `.spec.sourceNamespaces` attribute for a cluster-scoped Argo CD instance that manages the application.
** Add the namespace to the `.spec.sourceNamespaces` attribute in the `AppProject` custom resource that is associated with the application.
+
GITOPS-2341

* With this update, Argo CD supports the Server-Side Apply feature, which helps users to perform the following tasks:
** Manage large resources which are too big for the allowed annotation size of 262144 bytes.
** Patch an existing resource that is not managed or deployed by Argo CD.
+
You can configure this feature at application or resource level. GITOPS-2340

[id="fixed-issues-1-7-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, {gitops-title} releases were affected by an issue of Dex pods failing with `CreateContainerConfigError` error when the `anyuid` SCC was assigned to the Dex service account. This update fixes the issue by assigning a default user id to the Dex container. GITOPS-2235

* Before this update, {gitops-title} used the RHSSO (Keycloak) through OIDC in addition to Dex. However, with a recent security fix, the certificate of RHSSO could not be validated when configured with a certificate not signed by one of the well-known certificate authorities. This update fixes the issue; you can now provide a custom certificate to verify the KeyCloak's TLS certificate while communicating with it. In addition, you can add `rootCA` to the Argo CD custom resource `.spec.keycloak.rootCA` field. The Operator reconciles such changes and updates the `oidc.config in argocd-cm` config map with the PEM encoded root certificate. GITOPS-2214

Example Argo CD with Keycloak configuration:

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  sso:
    keycloak:
      rootCA: '<PEM encoded root certificate>'
    provider: keycloak
.......
.......
----

* Before this update, the application controllers restarted multiple times due to the unresponsiveness of liveness probes. This update fixes the issue by removing the liveness probe in the `statefulset` application controller. GITOPS-2153

[id="known-issues-1-7-0_{context}"]
== Known issues

* Before this update, the Operator did not reconcile the `mountsatoken` and `ServiceAccount` settings for the repository server. While this has been fixed, deletion of the service account does not revert to the default. GITOPS-1873

* Workaround: Manually set the `spec.repo.serviceaccountfield to thedefault` service account. GITOPS-2452

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-6-4_{context}"]
= Release notes for {gitops-title} 1.6.4

{gitops-title} 1.6.4 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-6-4_{context}"]
== Fixed issues

* Before this update, all versions of Argo CD v1.8.2 and later were vulnerable to an improper authorization bug. As a result, Argo CD would accept tokens for audiences who might not be intended to access the cluster. This issue is now fixed. CVE-2023-22482

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-6-2_{context}"]
= Release notes for {gitops-title} 1.6.2

{gitops-title} 1.6.2 is now available on OpenShift Container Platform 4.8, 4.9, 4.10 and 4.11.

[id="new-features-1-6-2_{context}"]
== New features

* This release removes the `DISABLE_DEX` environment variable from the `openshift-gitops-operator` CSV file. As a result, this environment variable is no longer set when you perform a fresh installation of {gitops-title}. GITOPS-2360

[id="fixed-issues-1-6-2_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the subscription health check was marked *degraded* for missing *InstallPlan* when more than 5 Operators were installed in a project. This update fixes the issue. GITOPS-2018

* Before this update, the {gitops-title} Operator would spam the cluster with a deprecation notice warning whenever it detected that an Argo CD instance used deprecated fields. This update fixes this issue and shows only one warning event for each instance that detects a field. GITOPS-2230

* From OpenShift Container Platform 4.12, it is optional to install the console. This fix updates the {gitops-title} Operator to prevent errors with the Operator if the console is not installed. GITOPS-2352

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-6-1_{context}"]
= Release notes for {gitops-title} 1.6.1

{gitops-title} 1.6.1 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-6-1_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, in a large set of applications the application controllers were restarted multiple times due to the unresponsiveness of liveness probes. This update fixes the issue by removing the liveness probe in the application controller `StatefulSet` object. GITOPS-2153

* Before this update, the RHSSO certificate cannot be validated when it is set up with a certificate which is not signed by certificate authorities. This update fixes the issue and now you can provide a custom certificate which will be used in verifying the Keycloak's TLS certificate when communicating with it. You can add the `rootCA` to the Argo CD custom resource `.spec.keycloak.rootCA` field. The Operator reconciles this change and updates the `oidc.config` field in the `argocd-cm` `ConfigMap` with the PEM-encoded root certificate. GITOPS-2214
+
[NOTE]
====
Restart the Argo CD server pod after updating the `.spec.keycloak.rootCA` field.
====
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  sso:
    provider: keycloak
    keycloak:
     rootCA: |
       ---- BEGIN CERTIFICATE ----
       This is a dummy certificate
       Please place this section with appropriate rootCA
       ---- END CERTIFICATE ----
  server:
    route:
      enabled: true
----

* Before this update, a terminating namespace that was managed by Argo CD would block the creation of roles and other configuration of other managed namespaces. This update fixes this issue. GITOPS-2277

* Before this update, the Dex pods failed to start with `CreateContainerConfigError` when an SCC of `anyuid` was assigned to the Dex `ServiceAccount` resource. This update fixes this issue by assigning a default user id to the Dex container. GITOPS-2235

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-6-0_{context}"]
= Release notes for {gitops-title} 1.6.0

{gitops-title} 1.6.0 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="new-features-1-6-0_{context}"]
== New features

The current release adds the following improvements:

* Previously, the Argo CD `ApplicationSet` controller was a technology preview (TP) feature. With this update, it is a general availability (GA) feature. GITOPS-1958

* With this update, the latest releases of the {gitops-title} are available in `latest` and version-based channels. To get these upgrades, update the `channel` parameter in the `Subscription` object YAML file: change its value from `stable` to `latest` or a version-based channel such as `gitops-1.6`. GITOPS-1791

* With this update, the parameters of the `spec.sso` field that controlled the keycloak configurations are moved to `.spec.sso.keycloak`.
The parameters of the `.spec.dex` field have been added to `.spec.sso.dex`. Start using `.spec.sso.provider` to enable or disable Dex. The `.spec.dex` parameters are deprecated and planned to be removed in version 1.9, along with the  `DISABLE_DEX` and `.spec.sso` fields for keycloak configuration. GITOPS-1983

* With this update, the Argo CD Notifications controller is available as an optional workload that can be enabled or disabled by using the `.spec.notifications.enabled` parameter in the Argo CD custom resource. The Argo CD Notifications controller is available as a Technical Preview feature. GITOPS-1917

* With this update, resource exclusions for Tekton pipeline runs and tasks runs are added by default. Argo CD, prunes these resources by default. These resource exclusions are added to the new Argo CD instances that are created from the OpenShift Container Platform. If the instances are created from the CLI, the resources are not added. GITOPS-1876

* With this update, you can select the tracking method that by Argo CD uses by setting the `resourceTrackingMethod` parameter in the Operand's specification. GITOPS-1862

* With this update, you can add entries to the `argocd-cm` configMap using the `extraConfig` field of {gitops-title} Argo CD custom resource. The entries specified are reconciled to the live `config-cm` configMap without validations. GITOPS-1964

* With this update, on OpenShift Container Platform 4.11, the {gitops-title} *Environments* page in the *Developer* perspective shows history of the successful deployments of the application environments, along with links to the revision for each deployment. GITOPS-1269

* With this update, you can manage resources with Argo CD that are also being used as template resources or "source" by an Operator. GITOPS-982

* With this update, the Operator will now configure the Argo CD workloads with the correct permissions to satisfy the Pod Security Admission that has been enabled for Kubernetes 1.24. GITOPS-2026

* With this update, Config Management Plugins 2.0 is supported. You can use the Argo CD custom resource to specify sidebar containers for the repo server. GITOPS-776

* With this update, all communication between the Argo CD components and the Redis cache are properly secured using modern TLS encryption. GITOPS-720

* This release of {gitops-title} adds support for IBM Z and IBM Power on OpenShift Container Platform 4.10. Currently, installations in restricted environments are not supported on IBM Z and IBM Power.

[id="fixed-issues-1-6-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the `system:serviceaccount:argocd:gitops-argocd-application-controller` cannot create resource "prometheusrules" in API group `monitoring.coreos.com` in the namespace `webapps-dev`. This update fixes this issue and {gitops-title} is now able to manage all resources from the `monitoring.coreos.com` API group. GITOPS-1638

* Before this update, while reconciling cluster permissions, if a secret belonged to a cluster config instance it was deleted. This update fixes this issue. Now, the `namespaces` field from the secret is deleted instead of the secret. GITOPS-1777

* Before this update, if you installed the HA variant of Argo CD through the Operator, the Operator created the Redis `StatefulSet` object with `podAffinity` rules instead of `podAntiAffinity` rules. This update fixes this issue and now the Operator creates the Redis `StatefulSet` with `podAntiAffinity` rules. GITOPS-1645

* Before this update, Argo CD **ApplicationSet** had too many `ssh` Zombie processes. This update fixes this issue: it adds tini, a simple init daemon that spawns processes and reaps zombies, to the **ApplicationSet** controller. This ensures that a `SIGTERM` signal is properly passed to the running process, preventing it from being a zombie process. GITOPS-2108

[id="known-issues-1-6-0_{context}"]
== Known issues

*  {gitops-title} Operator can make use of RHSSO (KeyCloak) through OIDC in addition to Dex. However, with a recent security fix applied, the certificate of RHSSO cannot be validated in some scenarios. GITOPS-2214
+
As a workaround, disable TLS validation for the OIDC (Keycloak/RHSSO) endpoint in the ArgoCD specification.

[source,yaml]
----
spec:
  extraConfig:
    oidc.tls.insecure.skip.verify: "true"
...
----

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-9_{context}"]
= Release notes for {gitops-title} 1.5.9

{gitops-title} 1.5.9 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-9_{context}"]
== Fixed issues

* Before this update, all versions of Argo CD v1.8.2 and later were vulnerable to an improper authorization bug. As a result, Argo CD would accept tokens for users who might not be authorized to access the cluster. This issue is now fixed. CVE-2023-22482

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-7_{context}"]
= Release notes for {gitops-title} 1.5.7

{gitops-title} 1.5.7 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-7_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* From OpenShift Container Platform 4.12, it is optional to install the console. This fix updates the {gitops-title} Operator to prevent errors with the Operator if the console is not installed. GITOPS-2353

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-6_{context}"]
= Release notes for {gitops-title} 1.5.6

{gitops-title} 1.5.6 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-6_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, in a large set of applications the application controllers were restarted multiple times due to the unresponsiveness of liveness probes. This update fixes the issue by removing the liveness probe in the application controller `StatefulSet` object. GITOPS-2153

* Before this update, the RHSSO certificate cannot be validated when it is set up with a certificate which is not signed by certificate authorities. This update fixes the issue and now you can provide a custom certificate which will be used in verifying the Keycloak's TLS certificate when communicating with it. You can add the `rootCA` to the Argo CD custom resource `.spec.keycloak.rootCA` field. The Operator reconciles this change and updates the `oidc.config` field in the `argocd-cm` `ConfigMap` with the PEM-encoded root certificate. GITOPS-2214
+
[NOTE]
====
Restart the Argo CD server pod after updating the `.spec.keycloak.rootCA` field.
====
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  sso:
    provider: keycloak
    keycloak:
     rootCA: |
       ---- BEGIN CERTIFICATE ----
       This is a dummy certificate
       Please place this section with appropriate rootCA
       ---- END CERTIFICATE ----
  server:
    route:
      enabled: true
----

* Before this update, a terminating namespace that was managed by Argo CD would block the creation of roles and other configuration of other managed namespaces. This update fixes this issue. GITOPS-2278

* Before this update, the Dex pods failed to start with `CreateContainerConfigError` when an SCC of `anyuid` was assigned to the Dex `ServiceAccount` resource. This update fixes this issue by assigning a default user id to the Dex container. GITOPS-2235

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-5_{context}"]
= Release notes for {gitops-title} 1.5.5

{gitops-title} 1.5.5 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="new-features-1-5-5_{context}"]
== New features

The current release adds the following improvements:

* With this update, the bundled Argo CD has been updated to version 2.3.7.

[id="fixed-issues-1-5-5_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the `redis-ha-haproxy` pods of an ArgoCD instance failed when more restrictive SCCs were present in the cluster. This update fixes the issue by updating the security context in workloads. GITOPS-2034

[id="known-issues-1-5-5_{context}"]
== Known issues

*  {gitops-title} Operator can use RHSSO (KeyCloak) with OIDC and Dex. However, with a recent security fix applied, the Operator cannot validate the RHSSO certificate in some scenarios. GITOPS-2214
+
As a workaround, disable TLS validation for the OIDC (Keycloak/RHSSO) endpoint in the ArgoCD specification.
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  extraConfig:
    "admin.enabled": "true"
...
----

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-4_{context}"]
= Release notes for {gitops-title} 1.5.4

{gitops-title} 1.5.4 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-4_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the {gitops-title} was using an older version of the *REDIS 5* image tag. This update fixes the issue and upgrades the `rhel8/redis-5` image tag. GITOPS-2037

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-3_{context}"]
= Release notes for {gitops-title} 1.5.3

{gitops-title} 1.5.3 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-3_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, all unpatched versions of Argo CD v1.0.0 and later were vulnerable to a cross-site scripting bug. As a result, an unauthorized user would be able to inject a javascript link in the UI. This issue is now fixed. CVE-2022-31035

* Before this update, all versions of Argo CD v0.11.0 and later were vulnerable to multiple attacks when SSO login was initiated from the Argo CD CLI or the UI. This issue is now fixed. CVE-2022-31034

* Before this update, all unpatched versions of Argo CD v0.7 and later were vulnerable to a memory consumption bug. As a result, an unauthorized user would be able to crash the Argo CD's repo-server. This issue is now fixed. CVE-2022-31016

* Before this update, all unpatched versions of Argo CD v1.3.0 and later were vulnerable to a symlink-following bug. As a result, an unauthorized user with repository write access would be able to leak sensitive YAML files from Argo CD's repo-server. This issue is now fixed. CVE-2022-31036

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-2_{context}"]
= Release notes for {gitops-title} 1.5.2

{gitops-title} 1.5.2 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-2_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, images referenced by the `redhat-operator-index` were missing. This issue is now fixed.  GITOPS-2036

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-1_{context}"]
= Release notes for {gitops-title} 1.5.1

{gitops-title} 1.5.1 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="fixed-issues-1-5-1_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, if Argo CD's anonymous access was enabled, an unauthenticated user was able to craft a JWT token and get full access to the Argo CD instance. This issue is fixed now. CVE-2022-29165

* Before this update, an unauthenticated user was able to display error messages on the login screen while SSO was enabled. This issue is now fixed. CVE-2022-24905

* Before this update, all unpatched versions of Argo CD v0.7.0 and later were vulnerable to a symlink-following bug. As a result, an unauthorized user with repository write access would be able to leak sensitive files from Argo CD's repo-server. This issue is now fixed. CVE-2022-24904

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-5-0_{context}"]
= Release notes for {gitops-title} 1.5.0

[role="_abstract"]
{gitops-title} 1.5.0 is now available on OpenShift Container Platform 4.8, 4.9, 4.10, and 4.11.

[id="new-features-1-5-0_{context}"]
== New features

The current release adds the following improvements:

* This enhancement upgrades Argo CD to version *2.3.3*. GITOPS-1708

* This enhancement upgrades Dex to version *2.30.3*. GITOPS-1850

* This enhancement upgrades Helm to version *3.8.0*. GITOPS-1709

* This enhancement upgrades Kustomize to version *4.4.1*. GITOPS-1710

* This enhancement upgrades Application Set to version *0.4.1*.

* With this update, a new channel by the name *latest* has been added that provides the latest release of the {gitops-title}. For GitOps v1.5.0, the Operator is pushed to *gitops-1.5*, *latest* channel, and the existing *stable* channel. From GitOps v1.6 all the latest releases will be pushed only to the *latest* channel and not the *stable* channel. GITOPS-1791

* With this update, the new CSV adds the `olm.skipRange: '>=1.0.0 <1.5.0'` annotation. As a result, all the previous release versions will be skipped. The Operator upgrades to v1.5.0 directly. GITOPS-1787

* With this update, the Operator updates the Red Hat Single Sign-On (RH-SSO) to version v7.5.1 including the following enhancements:

** You can log in to Argo CD using the OpenShift credentials including the `kube:admin` credential.
** The RH-SSO supports and configures Argo CD instances for Role-based Access Control (RBAC) using OpenShift groups.
** The RH-SSO honors the `HTTP_Proxy` environment variables. You can use the RH-SSO as an SSO for Argo CD running behind a proxy.
+
GITOPS-1330

* With this update, a new `.host` URL field is added to the `.status` field of the Argo CD operand. When a route or ingress is enabled with the priority given to route, then the new URL field displays the route. If no URL is provided from the route or ingress, the `.host` field is not displayed.
+
When the route or ingress is configured, but the corresponding controller is not set up properly and is not in the `Ready` state or does not propagate its URL, the value of the `.status.host` field in the operand indicates as `Pending` instead of displaying the URL. This affects the overall status of the operand by making it `Pending` instead of `Available`. GITOPS-654

[id="fixed-issues-1-5-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, RBAC rules specific to *AppProjects* would not allow the use of commas for the subject field of the role, thus preventing bindings to the LDAP account. This update fixes the issue and you can now specify complex role bindings in *AppProject* specific RBAC rules. GITOPS-1771

* Before this update, when a `DeploymentConfig` resource is scaled to `0`, Argo CD displayed it in a *progressing* state with a health status message as *"replication controller is waiting for pods to run"*. This update fixes the edge case and the health check now reports the correct health status of the `DeploymentConfig` resource. GITOPS-1738

* Before this update, the TLS certificate in the `argocd-tls-certs-cm` configuration map was deleted by the {gitops-title} unless the certificate was configured in the `ArgoCD` CR specification `tls.initialCerts` field. This issue is fixed now. GITOPS-1725

* Before this update, while creating a namespace with the `managed-by` label it created a lot of `RoleBinding` resources on the new namespace. This update fixes the issue and now {gitops-title} removes the irrelevant `Role` and `RoleBinding` resources created by the previous versions. GITOPS-1550

* Before this update, the TLS certificate of the route in pass-through mode did not have a CA name.  As a result, Firefox 94 and later failed to connect to Argo CD UI with error code *SEC_ERROR_BAD_DER*. This update fixes the issue. You must delete the `<openshift-gitops-ca>` secrets and let it recreate. Then, you must delete the `<openshift-gitops-tls>` secrets. After the {gitops-title} recreates it, the Argo CD UI is accessible by Firefox again. GITOPS-1548

[id="known-issues-1-5-0_{context}"]
== Known issues

* Argo CD `.status.host` field is not updated when an `Ingress` resource is in use instead of a `Route` resource on OpenShift clusters. GITOPS-1920

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-13_{context}"]
= Release notes for {gitops-title} 1.4.13

{gitops-title} 1.4.13 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-13_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* From OpenShift Container Platform 4.12, it is optional to install the console. This fix updates the {gitops-title} Operator to prevent errors with the Operator if the console is not installed. GITOPS-2354

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-12_{context}"]
= Release notes for {gitops-title} 1.4.12

{gitops-title} 1.4.12 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-12_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, in a large set of applications the application controllers were restarted multiple times due to the unresponsiveness of liveness probes. This update fixes the issue by removing the liveness probe in the application controller `StatefulSet` object. GITOPS-2153

* Before this update, the RHSSO certificate cannot be validated when it is set up with a certificate which is not signed by certificate authorities. This update fixes the issue and now you can provide a custom certificate which will be used in verifying the Keycloak's TLS certificate when communicating with it. You can add the `rootCA` to the Argo CD custom resource `.spec.keycloak.rootCA` field. The Operator reconciles this change and updates the `oidc.config` field in the `argocd-cm` `ConfigMap` with the PEM-encoded root certificate. GITOPS-2214
+
[NOTE]
====
Restart the Argo CD server pod after updating the `.spec.keycloak.rootCA` field.
====
+
For example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  sso:
    provider: keycloak
    keycloak:
     rootCA: |
       ---- BEGIN CERTIFICATE ----
       This is a dummy certificate
       Please place this section with appropriate rootCA
       ---- END CERTIFICATE ----
  server:
    route:
      enabled: true
----

* Before this update, a terminating namespace that was managed by Argo CD would block the creation of roles and other configuration of other managed namespaces. This update fixes this issue. GITOPS-2276

* Before this update, the Dex pods failed to start with `CreateContainerConfigError` when an SCC of `anyuid` was assigned to the Dex `ServiceAccount` resource. This update fixes this issue by assigning a default user id to the Dex container. GITOPS-2235

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-11_{context}"]
= Release notes for {gitops-title} 1.4.11

{gitops-title} 1.4.11 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="new-features-1-4-11_{context}"]
== New features

The current release adds the following improvements:

* With this update, the bundled Argo CD has been updated to version 2.2.12.

[id="fixed-issues-1-4-11_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, the `redis-ha-haproxy` pods of an ArgoCD instance failed when more restrictive SCCs were present in the cluster. This update fixes the issue by updating the security context in workloads. GITOPS-2034

[id="known-issues-1-4-11_{context}"]
== Known issues

*  {gitops-title} Operator can use RHSSO (KeyCloak) with OIDC and Dex. However, with a recent security fix applied, the Operator cannot validate the RHSSO certificate in some scenarios. GITOPS-2214
+
As a workaround, disable TLS validation for the OIDC (Keycloak/RHSSO) endpoint in the ArgoCD specification.
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
spec:
  extraConfig:
    "admin.enabled": "true"
...
----

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-6_{context}"]
= Release notes for {gitops-title} 1.4.6

[role="_abstract"]
{gitops-title} 1.4.6 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-6_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* The base images are updated to the latest version to avoid OpenSSL flaw (CVE-2022-0778).

[NOTE]
====
To install the current release of {gitops-title} 1.4 and receive further updates during its product life cycle, switch to the **GitOps-1.4** channel.
====

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-5_{context}"]
= Release notes for {gitops-title} 1.4.5

[role="_abstract"]
{gitops-title} 1.4.5 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-5_{context}"]
== Fixed issues

[WARNING]
====
You should directly upgrade to {gitops-title} v1.4.5 from {gitops-title} v1.4.3. Do not use {gitops-title} v1.4.4 in a production environment. Major issues that affected {gitops-title} v1.4.4 are fixed in {gitops-title} 1.4.5.
====

The following issue has been resolved in the current release:

* Before this update, Argo CD pods were stuck in the `ErrImagePullBackOff` state. The following error message was shown:
[source,yaml]
----
reason: ErrImagePull
          message: >-
            rpc error: code = Unknown desc = reading manifest
            sha256:ff4ad30752cf0d321cd6c2c6fd4490b716607ea2960558347440f2f370a586a8
            in registry.redhat.io/openshift-gitops-1/argocd-rhel8: StatusCode:
            404, <HTML><HEAD><TITLE>Error</TITLE></HEAD><BODY>
----
This issue is now fixed. GITOPS-1848

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-3_{context}"]
= Release notes for {gitops-title} 1.4.3

[role="_abstract"]
{gitops-title} 1.4.3 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-3_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, the TLS certificate in the `argocd-tls-certs-cm` configuration map was deleted by the {gitops-title} unless the certificate was configured in the ArgoCD CR specification `tls.initialCerts` field. This update fixes this issue. GITOPS-1725

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-2_{context}"]
= Release notes for {gitops-title} 1.4.2

[role="_abstract"]
{gitops-title} 1.4.2 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-2_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, the *Route* resources got stuck in `Progressing` Health status if more than one `Ingress` were attached to the route.  This update fixes the health check and reports the correct health status of the *Route* resources. GITOPS-1751

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-1_{context}"]
= Release notes for {gitops-title} 1.4.1

{gitops-title} 1.4.1 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-4-1_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* {gitops-title} Operator v1.4.0 introduced a regression which removes the description fields from `spec` for the following CRDs:

** `argoproj.io_applications.yaml`
** `argoproj.io_appprojects.yaml`
** `argoproj.io_argocds.yaml`
+
Before this update, when you created an `AppProject` resource using the `oc create` command, the resource failed to synchronize due to the missing description fields. This update restores the missing description fields in the preceding CRDs.  GITOPS-1721

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-4-0_{context}"]
= Release notes for {gitops-title} 1.4.0

{gitops-title} 1.4.0 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.10.

[id="new-features-1-4-0_{context}"]
== New features

The current release adds the following improvements.

* This enhancement upgrades the {gitops-title} Application Manager CLI (`kam`) to version *0.0.41*. GITOPS-1669

* This enhancement upgrades Argo CD to version *2.2.2*. GITOPS-1532

* This enhancement upgrades Helm to version *3.7.1*. GITOPS-1530

* This enhancement adds the health status of the `DeploymentConfig`, `Route`, and `OLM Operator` items to the Argo CD Dashboard and OpenShift Container Platform web console. This information helps you monitor the overall health status of your application. GITOPS-655, GITOPS-915, GITOPS-916, GITOPS-1110

* With this update, you can to specify the number of desired replicas for the `argocd-server` and `argocd-repo-server` components by setting the `.spec.server.replicas` and `.spec.repo.replicas` attributes in the Argo CD custom resource, respectively. If you configure the horizontal pod autoscaler (HPA) for the `argocd-server` components, it takes precedence over the Argo CD custom resource attributes. GITOPS-1245

* As an administrative user, when you give Argo CD access to a namespace by using the `argocd.argoproj.io/managed-by` label, it assumes namespace-admin privileges. These privileges are an issue for administrators who provide namespaces to non-administrators, such as development teams, because the privileges enable non-administrators to modify objects such as network policies.
+
With this update, administrators can configure a common cluster role for all the managed namespaces. In role bindings for the Argo CD application controller, the Operator refers to the `CONTROLLER_CLUSTER_ROLE` environment variable. In role bindings for the Argo CD server, the Operator refers to the `SERVER_CLUSTER_ROLE` environment variable. If these environment variables contain custom roles, the Operator does not create the default admin role. Instead, it uses the existing custom role for all managed namespaces. GITOPS-1290

* With this update, the *Environments* page in the OpenShift Container Platform *Developer* perspective displays a broken heart icon to indicate degraded resources, excluding ones whose status is `Progressing`, `Missing`, and `Unknown`. The console displays a yellow yield sign icon to indicate out-of-sync resources. GITOPS-1307

[id="fixed-issues-1-4-0_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Before this update, when the Route to the {gitops-title} Application Manager CLI (`kam`) was accessed without specifying a path in the URL, a default page without any helpful information was displayed to the user. This update fixes the issue so that the default page displays download links for the `kam` CLI. GITOPS-923

* Before this update, setting a resource quota in the namespace of the Argo CD custom resource might cause the setup of the Red Hat SSO (RH SSO) instance to fail. This update fixes this issue by setting a minimum resource request for the RH SSO deployment pods. GITOPS-1297

* Before this update, if you changed the log level for the `argocd-repo-server` workload, the Operator did not reconcile this setting. The workaround was to delete the deployment resource so that the Operator recreated it with the new log level. With this update, the log level is correctly reconciled for existing `argocd-repo-server` workloads. GITOPS-1387

* Before this update, if the Operator managed an Argo CD instance that lacked the `.data` field in the `argocd-secret` Secret, the Operator on that instance crashed. This update fixes the issue so that the Operator does not crash when the `.data` field is missing. Instead, the secret regenerates and the `gitops-operator-controller-manager` resource is redeployed. GITOPS-1402

* Before this update, the `gitopsservice` service was annotated as an internal object. This update removes the annotation so you can update or delete the default Argo CD instance and run GitOps workloads on infrastructure nodes by using the UI. GITOPS-1429

[id="known-issues-1-4-0_{context}"]
== Known issues

These are the known issues in the current release:

* If you migrate from the Dex authentication provider to the Keycloak provider, you might experience login issues with Keycloak.
+
To prevent this issue, when migrating, uninstall Dex by removing the `.spec.dex` section from the Argo CD custom resource. Allow a few minutes for Dex to uninstall completely. Then, install Keycloak by adding `.spec.sso.provider: keycloak` to the Argo CD custom resource.
+
As a workaround, uninstall Keycloak by removing `.spec.sso.provider: keycloak`. Then, re-install it. GITOPS-1450, GITOPS-1331

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-7_{context}"]
= Release notes for {gitops-title} 1.3.7

{gitops-title} 1.3.7 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="fixed-issues-1-3-7_{context}"]
== Fixed issues

The following issue has been resolved in the current release:

* Before this update, a flaw was found in OpenSSL. This update fixes the issue by updating the base images to the latest version to avoid the OpenSSL flaw. (CVE-2022-0778).

[NOTE]
====
To install the current release of {gitops-title} 1.3 and receive further updates during its product life cycle, switch to the **GitOps-1.3** channel.
====

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-6_{context}"]
= Release notes for {gitops-title} 1.3.6

{gitops-title} 1.3.6 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="fixed-issues-1-3-6_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* In {gitops-title}, improper access control allows admin privilege escalation (CVE-2022-1025). This update fixes the issue.

* A path traversal flaw allows leaking of out-of-bound files (CVE-2022-24731). This update fixes the issue.

* A path traversal flaw and improper access control allows leaking of out-of-bound files (CVE-2022-24730). This update fixes the issue.

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-2_{context}"]
= Release notes for {gitops-title} 1.3.2

{gitops-title} 1.3.2 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="new-features-1-3-2_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {gitops-title} 1.3.2:

* Upgraded Argo CD to version *2.1.8*

* Upgraded Dex to version *2.30.0*

[id="fixed-issues-1-3-2_{context}"]
== Fixed issues

The following issues have been resolved in the current release:

* Previously, in the software catalog UI under the *Infrastructure Features* section, when you filtered by `Disconnected` the {gitops-title} Operator did not show in the search results, as the Operator did not have the related annotation set in its CSV file. With this update, the `Disconnected Cluster` annotation has been added to the {gitops-title} Operator as an infrastructure feature. GITOPS-1539

* When using an `Namespace-scoped` Argo CD instance, for example, an Argo CD instance that is not scoped to *All Namepsaces* in a cluster, {gitops-title} dynamically maintains a list of managed namespaces. These namespaces include the `argocd.argoproj.io/managed-by` label. This list of namespaces is stored in a cache in *Argo CD -> Settings -> Clusters -> "in-cluster" -> NAMESPACES*. Before this update, if you deleted one of these namespaces, the Operator ignored that, and the namespace remained in the list. This behavior broke the *CONNECTION STATE* in that cluster configuration, and all sync attempts resulted in errors. For example:
+
[source,text]
----
Argo service account does not have <random_verb> on <random_resource_type> in namespace <the_namespace_you_deleted>.
----
+
This bug is fixed. GITOPS-1521

* With this update, the {gitops-title} Operator has been annotated with the *Deep Insights* capability level. GITOPS-1519

* Previously, the Argo CD Operator managed the `resource.exclusion` field by itself but ignored the `resource.inclusion` field. This prevented the `resource.inclusion` field configured in the `Argo CD` CR to generate in the `argocd-cm` configuration map. This bug is fixed. GITOPS-1518

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3-1_{context}"]
= Release notes for {gitops-title} 1.3.1

{gitops-title} 1.3.1 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="fixed-issues-1-3-1_{context}"]
== Fixed issues

* If you upgrade to v1.3.0, the Operator does not return an ordered slice of environment variables. As a result, the reconciler fails causing the frequent recreation of Argo CD pods in OpenShift Container Platform clusters running behind a proxy. This update fixes the issue so that Argo CD pods are not recreated. GITOPS-1489

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-3_{context}"]
= Release notes for {gitops-title} 1.3

{gitops-title} 1.3 is now available on OpenShift Container Platform 4.7, 4.8, 4.9, and 4.6 with limited GA support.

[id="new-features-1-3_{context}"]
== New features
In addition to the fixes and stability improvements, the following sections highlight what is new in {gitops-title} 1.3.0:

* For a fresh install of v1.3.0, Dex is automatically configured. You can log into the default Argo CD instance in the `openshift-gitops` namespace using the OpenShift or `kubeadmin` credentials.  As an admin you can disable the Dex installation after the Operator is installed which will remove the Dex deployment from the `openshift-gitops` namespace.
* The default Argo CD instance installed by the  Operator as well as accompanying controllers can now run on the infrastructure nodes of the cluster by setting a simple configuration toggle.
* Internal communications in Argo CD can now be secured using the TLS and the OpenShift cluster certificates. The Argo CD routes can now leverage the OpenShift cluster certificates in addition to using external certificate managers such as the cert-manager.
* Use the improved *Environments* page in the *Developer* perspective of the console 4.9 to gain insights into the GitOps environments.
* You can now access custom health checks in Argo CD for `DeploymentConfig` resources, `Route` resources, and Operators installed using OLM.
* The GitOps Operator now conforms to the naming conventions recommended by the latest Operator-SDK:
** The prefix `gitops-operator-` is added to all resources
** Service account is renamed to `gitops-operator-controller-manager`

[id="fixed-issues-1-3_{context}"]
== Fixed issues
The following issues were resolved in the current release:

* Previously, if you set up a new namespace to be managed by a new instance of Argo CD, it would immediately be **Out Of Sync** due to the new roles and bindings that the Operator creates to manage that new namespace. This behavior is fixed.  GITOPS-1384

[id="known-issues-1-3_{context}"]
== Known issues

* While migrating from the Dex authentication provider to the Keycloak provider, you may experience login issues with Keycloak. GITOPS-1450
+
To prevent the above issue, when migrating, uninstall Dex by removing the `.spec.dex` section found in the Argo CD custom resource. Allow a few minutes for Dex to uninstall completely, and then proceed to install Keycloak by adding `.spec.sso.provider: keycloak` to the Argo CD custom resource.
+
As a workaround, uninstall Keycloak by removing `.spec.sso.provider: keycloak` and then re-install.

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-2-2_{context}"]
= Release notes for {gitops-title} 1.2.2

{gitops-title} 1.2.2 is now available on OpenShift Container Platform 4.8.

[id="fixed-issues-1-2-2_{context}"]
== Fixed issues
The following issue was resolved in the current release:

* All versions of Argo CD are vulnerable to a path traversal bug that allows to pass arbitrary values to be consumed by Helm charts. This update fixes the CVE-2022-24348 gitops error, path traversal and dereference of symlinks when passing Helm value files.
GITOPS-1756

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-2-1_{context}"]
= Release notes for {gitops-title} 1.2.1

{gitops-title} 1.2.1 is now available on OpenShift Container Platform 4.8.

[id="support-matrix-1-2-1_{context}"]
== Support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

Technology Preview Features Support Scope

In the table below, features are marked with the following statuses:

- *TP*: _Technology Preview_

- *GA*: _General Availability_

Note the following scope of support on the Red Hat Customer Portal for these features:

.Support matrix
[cols="1,1",options="header"]
|===
| Feature | {gitops-title} 1.2.1
| Argo CD
| GA
| Argo CD ApplicationSet
| TP
| {gitops-title} Application Manager CLI (`kam`)
| TP
|===

[id="fixed-issues-1-2-1_{context}"]
== Fixed issues
The following issues were resolved in the current release:

* Previously, huge memory spikes were observed on the application controller on startup. The flag `--kubectl-parallelism-limit` for the application controller is now set to 10 by default, however
this value can be overridden by specifying a number for `.spec.controller.kubeParallelismLimit` in the Argo CD CR specification.
GITOPS-1255

*  The latest Triggers APIs caused Kubernetes build failure due to duplicate entries in the kustomization.yaml when using the `kam bootstrap` command. The Pipelines and Tekton triggers components have now been updated to v0.24.2 and v0.14.2, respectively, to address this issue.
GITOPS-1273

* Persisting RBAC roles and bindings are now automatically removed from the target namespace when the Argo CD instance from the source namespace is deleted.
GITOPS-1228

* Previously, when deploying an Argo CD instance into a namespace, the Argo CD instance would change the "managed-by" label to be its own namespace. This fix would make namespaces unlabelled while also making sure the required RBAC roles and bindings are created and deleted for the namespace.
GITOPS-1247

* Previously, the default resource request limits on Argo CD workloads, specifically for the repo-server and application controller, were found to be very restrictive. The existing resource quota has now been removed and the default memory limit has been increased to 1024M in the repo server. Please note that this change will only affect new installations; existing Argo CD instance workloads will not be affected.
GITOPS-1274

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-2_{context}"]
= Release notes for {gitops-title} 1.2

{gitops-title} 1.2 is now available on OpenShift Container Platform 4.8.

[id="support-matrix-1-2_{context}"]
== Support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

Technology Preview Features Support Scope

In the table below, features are marked with the following statuses:

- *TP*: _Technology Preview_

- *GA*: _General Availability_

Note the following scope of support on the Red Hat Customer Portal for these features:

.Support matrix
[cols="1,1",options="header"]
|===
| Feature | {gitops-title} 1.2
| Argo CD
| GA
| Argo CD ApplicationSet
| TP
| {gitops-title} Application Manager CLI (`kam`)
| TP
|===

[id="new-features-1-2_{context}"]
== New features
In addition to the fixes and stability improvements, the following sections highlight what is new in {gitops-title} 1.2:

* If you do not have read or write access to the openshift-gitops namespace, you can now use the `DISABLE_DEFAULT_ARGOCD_INSTANCE` environment variable in the GitOps Operator and set the value to `TRUE` to prevent the default Argo CD instance from starting in the `openshift-gitops` namespace.
* Resource requests and limits are now configured in Argo CD workloads.  Resource quota is enabled in the `openshift-gitops` namespace. As a result, out-of-band workloads deployed manually in the openshift-gitops namespace must be configured with resource requests and limits and the resource quota may need to be increased.
* Argo CD authentication is now integrated with Red Hat SSO and it is automatically configured with OpenShift 4 Identity Provider on the cluster. This feature is disabled by default.  To enable Red Hat SSO, add SSO configuration in `ArgoCD` CR as shown below. Currently,`keycloak` is the only supported provider.

+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  sso:
    provider: keycloak
  server:
    route:
     enabled: true
----
* You can now define hostnames using route labels to support router sharding. Support for setting labels on the `server` (argocd server), `grafana`, and `prometheus` routes is now available. To set labels on a route, add `labels` under the route configuration for a server in the `ArgoCD` CR.
+
.Example `ArgoCD` CR YAML to set labels on argocd server
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  server:
    route:
     enabled: true
     labels:
       key1: value1
       key2: value2
----
* The GitOps Operator now automatically grants permissions to Argo CD instances to manage resources in target namespaces by applying labels. Users can label the target namespace with the label `argocd.argoproj.io/managed-by: <source-namespace>`, where the `source-namespace` is the namespace where the argocd instance is deployed.

[id="fixed-issues-1-2_{context}"]
== Fixed issues
The following issues were resolved in the current release:

* Previously, if a user created additional instances of Argo CD managed by the default cluster instance in the openshift-gitops namespace, the application responsible for the new Argo CD instance would get stuck in an `OutOfSync` status. This issue has now been resolved by adding an owner reference to the cluster secret. GITOPS-1025

[id="known-issues-1-2_{context}"]
== Known issues
These are the known issues in {gitops-title} 1.2:

* When an Argo CD instance is deleted from the source namespace, the `argocd.argoproj.io/managed-by` labels in the target namespaces are not removed. GITOPS-1228

* Resource quota has been enabled in the openshift-gitops namespace in {gitops-title} 1.2. This can affect out-of-band workloads deployed manually and workloads deployed by the default Argo CD instance in the `openshift-gitops` namespace. When you upgrade from {gitops-title} `v1.1.2` to `v1.2` such workloads must be configured with resource requests and limits. If there are any additional workloads, the resource quota in the openshift-gitops namespace must be increased.

+
Current Resource Quota for `openshift-gitops` namespace.
+
[cols="1,1,1",options="header"]
|===
| *Resource* | *Requests* | *Limits*

| CPU
| 6688m
| 13750m

| Memory
| 4544Mi
| 9070Mi

|===
+
You can use the below command to update the CPU limits.
+
[source,terminal]
----
$ oc patch resourcequota openshift-gitops-compute-resources -n openshift-gitops --type='json' -p='[{"op": "replace", "path": "/spec/hard/limits.cpu", "value":"9000m"}]'
----
+
You can use the below command to update the CPU requests.
+
[source,terminal]
----
$ oc patch resourcequota openshift-gitops-compute-resources -n openshift-gitops --type='json' -p='[{"op": "replace", "path": "/spec/hard/cpu", "value":"7000m"}]
----
+
You can replace the path in the above commands from `cpu` to `memory` to update the memory.

// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

[id="gitops-release-notes-1-1_{context}"]
= Release notes for {gitops-title} 1.1

{gitops-title} 1.1 is now available on OpenShift Container Platform 4.7.

[id="support-matrix-1-1_{context}"]
== Support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

Technology Preview Features Support Scope

In the table below, features are marked with the following statuses:

- *TP*: _Technology Preview_

- *GA*: _General Availability_

Note the following scope of support on the Red Hat Customer Portal for these features:

.Support matrix
[cols="1,1",options="header"]
|===
| Feature | {gitops-title} 1.1
| Argo CD
| GA
| Argo CD ApplicationSet
| TP
| {gitops-title} Application Manager CLI (`kam`)
| TP
|===

[id="new-features-1-1_{context}"]
== New features
In addition to the fixes and stability improvements, the following sections highlight what is new in {gitops-title} 1.1:

* The `ApplicationSet` feature is now added (Technology Preview). The `ApplicationSet` feature enables both automation and greater flexibility when managing Argo CD applications across a large number of clusters and within monorepos. It also makes self-service usage possible on multitenant Kubernetes clusters.
* Argo CD is now integrated with cluster logging stack and with the OpenShift Container Platform Monitoring and Alerting features.
* Argo CD auth is now integrated with OpenShift Container Platform.
* Argo CD applications controller now supports horizontal scaling.
* Argo CD Redis servers now support high availability (HA).

[id="fixed-issues-1-1_{context}"]
== Fixed issues
The following issues were resolved in the current release:

* Previously, {gitops-title} did not work as expected in a proxy server setup with active global proxy settings. This issue is fixed and now Argo CD is configured by the {gitops-title} Operator using fully qualified domain names (FQDN) for the pods to enable communication between components. GITOPS-703
* The {gitops-title} backend relies on the `?ref=` query parameter in the {gitops-title} URL to make API calls. Previously, this parameter was not read from the URL, causing the backend to always consider the default reference. This issue is fixed and the {gitops-title} backend now extracts the reference query parameter from the {gitops-title} URL and only uses the default reference when there is no input reference provided. GITOPS-817
* Previously, the {gitops-title} backend failed to find the valid GitLab repository. This was because the {gitops-title} backend checked for `main` as the branch reference, instead of `master` in the GitLab repository. This issue is fixed now. GITOPS-768
* The *Environments* page in the *Developer* perspective of the OpenShift Container Platform web console now shows the list of applications and the number of environments. This page also displays an Argo CD link that directs you to the Argo CD *Applications* page that lists all the applications. The Argo CD *Applications* page has *LABELS* (for example, `app.kubernetes.io/name=appName`) that help you filter only the applications of your choice. GITOPS-544

[id="known-issues-1-1_{context}"]
== Known issues
These are the known issues in {gitops-title} 1.1:

* {gitops-title} does not support Helm v2 and ksonnet.
* The Red Hat SSO (RH SSO) Operator is not supported in disconnected clusters. As a result, the {gitops-title} Operator and RH SSO integration is not supported in disconnected clusters.
* When you delete an Argo CD application from the OpenShift Container Platform web console, the Argo CD application gets deleted in the user interface, but the deployments are still present in the cluster. As a workaround, delete the Argo CD application from the Argo CD console. GITOPS-830

[id="breaking-change-1-1_{context}"]
== Breaking Change
=== Upgrading from {gitops-title} v1.0.1

When you upgrade from {gitops-title} `v1.0.1` to `v1.1`, the {gitops-title} Operator renames the default Argo CD instance created in the `openshift-gitops` namespace from `argocd-cluster` to `openshift-gitops`.

This is a breaking change and needs the following steps to be performed manually, before the upgrade:

. Go to the OpenShift Container Platform web console and copy the content of the `argocd-cm.yml` config map file in the `openshift-gitops` namespace to a local file. The content may look like the following example:
+
.Example argocd config map YAML
[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
selfLink: /api/v1/namespaces/openshift-gitops/configmaps/argocd-cm
resourceVersion: '112532'
name: argocd-cm
uid: f5226fbc-883d-47db-8b53-b5e363f007af
creationTimestamp: '2021-04-16T19:24:08Z'
managedFields:
...
namespace: openshift-gitops
labels:
  app.kubernetes.io/managed-by: argocd-cluster
  app.kubernetes.io/name: argocd-cm
  app.kubernetes.io/part-of: argocd
data: "" <1>
admin.enabled: 'true'
statusbadge.enabled: 'false'
resource.exclusions: |
  - apiGroups:
    - tekton.dev
    clusters:
    - '*'
    kinds:
    - TaskRun
    - PipelineRun
ga.trackingid: ''
repositories: |
  - type: git
    url: https://github.com/user-name/argocd-example-apps
ga.anonymizeusers: 'false'
help.chatUrl: ''
url: >-
  https://argocd-cluster-server-openshift-gitops.apps.dev-svc-4.7-041614.devcluster.openshift.com   "" <2>
help.chatText: ''
kustomize.buildOptions: ''
resource.inclusions: ''
repository.credentials: ''
users.anonymous.enabled: 'false'
configManagementPlugins: ''
application.instanceLabelKey: ''
----
<1> Restore only the `data` section of the content in the `argocd-cm.yml` config map file manually.
<2> Replace the URL value in the config map entry with the new instance name `openshift-gitops`.

. Delete the default `argocd-cluster` instance.
. Edit the new `argocd-cm.yml` config map file to restore the entire `data` section manually.
. Replace the URL value in the config map entry with the new instance name `openshift-gitops`. For example, in the preceding example, replace the URL value with the following URL value:
+
[source,yaml]
----
url: >-
  https://openshift-gitops-server-openshift-gitops.apps.dev-svc-4.7-041614.devcluster.openshift.com
----
. Login to the Argo CD cluster and verify that the previous configurations are present.
