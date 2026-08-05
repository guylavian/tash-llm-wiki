---
title: "Remote health reporting"
type: reference
domain: openshift
slug: support-4-22-remote-health-reporting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/remote-health-reporting
version: 4.22
family: support
documentKind: "Documentation"
---

# Remote health reporting

[id="remote-health-reporting"]
= Remote health reporting

[role="_abstract"]
You can _opt in_, enable, or _opt out_, disable, reporting health and usage data for your cluster.

// Enabling remote health reporting
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting.adoc

[id="enabling-remote-health-reporting_{context}"]
= Enabling remote health reporting

[role="_abstract"]
If you or your organization have disabled remote health reporting, you can enable this feature again. You can see that remote health reporting is disabled from the message `Insights not available` in the *Status* tile on the OpenShift Container Platform web console *Overview* page.

To enable remote health reporting, you must change the global cluster pull secret with a new authorization token. Enabling remote health reporting enables both {insights-operator} and Telemetry.

// Changing your global cluster pull secret to enable remote health reporting
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting.adoc

[id="insights-operator-new-pull-secret-enable_{context}"]
= Changing your global cluster pull secret to enable remote health reporting

[role="_abstract"]
You can change your existing global cluster pull secret to enable remote health reporting. If you have disabled remote health monitoring, you must download a new pull secret with your `console.openshift.com` access token from {cluster-manager-first}.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.
* Access to {cluster-manager}.

.Procedure

. Go to the Downloads page on the {hybrid-console}.

. From *Tokens* -> *Pull secret*, click the *Download* button.
+
The `pull-secret` file contains your `cloud.openshift.com` access token in JSON format:
+
[source,json,subs="+quotes"]
----
{
  "auths": {
    "cloud.openshift.com": {
      "auth": "_<your_token>_",
      "email": "_<email_address>_"
    }
  }
}
----

. Download the global cluster pull secret to your local file system.
+
[source,terminal]
----
$ oc get secret/pull-secret -n openshift-config \
  --template='{{index .data ".dockerconfigjson" | base64decode}}' \
  > pull-secret
----

. Make a backup copy of your pull secret.
+
[source,terminal]
----
$ cp pull-secret pull-secret-backup
----

. Open the `pull-secret` file in a text editor.

. Append the `cloud.openshift.com` JSON entry from the `pull-secret` file that you downloaded earlier into the `auths` file.

. Save the file.

. Update the secret in your cluster by running the following command:
+
[source,terminal]
----
$ oc set data secret/pull-secret -n openshift-config \
  --from-file=.dockerconfigjson=pull-secret
----
+
You might need to wait several minutes for the secret to update and your cluster to begin reporting.

.Verification

. For a verification check from the OpenShift Container Platform web console, complete the following steps:
+
.. Go to the *Overview* page on the OpenShift Container Platform web console.
+
.. View the *{red-hat-lightspeed}* section in the *Status* tile that reports the number of issues found.

. For a verification check from the {oc-first}, enter the following command and then check that the value of the `status` parameter states `false`:
+
[source,terminal]
----
$ oc get co insights -o jsonpath='{.status.conditions[?(@.type=="Disabled")]}'
----

// Consequences of disabling remote health reporting
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting.adoc

[id="telemetry-consequences-of-disabling-telemetry_{context}"]
= Consequences of disabling remote health reporting

[role="_abstract"]
In OpenShift Container Platform, customers can disable reporting usage information.

Before you disable remote health reporting, read the following benefits of a connected cluster:

* Red{nbsp}Hat can react more quickly to problems and better support our customers.
* Red{nbsp}Hat can better understand how product upgrades impact clusters.
* Connected clusters help to simplify the subscription and entitlement process.
* Connected clusters enable the {cluster-manager} service to offer an overview of your clusters and their subscription status.

[NOTE]
====
Consider leaving health and usage reporting enabled for pre-production, test, and production clusters. This means that Red{nbsp}Hat can participate in qualifying OpenShift Container Platform in your environments and react more rapidly to product issues.
====

The following lists some consequences of disabling remote health reporting on a connected cluster:

* Red{nbsp}Hat cannot view the success of product upgrades or the health of your clusters without an open support case.
* Red{nbsp}Hat cannot use configuration data to better triage customer support cases and identify which configurations our customers find important.
* The {cluster-manager} cannot show data about your clusters, which includes health and usage information.
* You must manually enter your subscription information in the `console.redhat.com` web console without the benefit of automatic usage reporting.

In restricted networks, Telemetry and {red-hat-lightspeed} data still gets gathered through the appropriate configuration of your proxy.

// Disabling remote health reporting
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting.adoc

[id="insights-operator-new-pull-secret_{context}"]
= Disabling remote health reporting

[role="_abstract"]
You can change your existing global cluster pull secret to disable remote health reporting. This configuration disables both Telemetry and the {insights-operator}.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. Download the global cluster pull secret to your local file system:
+
[source,terminal]
----
$ oc extract secret/pull-secret -n openshift-config --to=.
----

. In a text editor, edit the `.dockerconfigjson` file that you downloaded by removing the `cloud.openshift.com` JSON entry:
+
[source,json]
----
"cloud.openshift.com":{"auth":"<hash>","email":"<email_address>"}
----

. Save the file.

. Update the secret in your cluster. For more information, see "Updating the global cluster pull secret".
+
You might need to wait several minutes for the secret to update in your cluster.

// Registering your disconnected cluster
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/remote-health-reporting.adoc

[id="insights-operator-register-disconnected-cluster_{context}"]
= Registering your disconnected cluster

[role="_abstract"]
Register your disconnected OpenShift Container Platform cluster on the {hybrid-console} so that your cluster does not get impacted by disabling remote health reporting. For more information, see "Consequences of disabling remote health reporting".

[IMPORTANT]
====
By registering your disconnected cluster, you can continue to report your subscription usage to Red{nbsp}Hat. Red{nbsp}Hat can then return accurate usage and capacity trends associated with your subscription, so that you can use the returned information to better organize subscription allocations across all of your resources.
====

.Prerequisites

* You logged in to the OpenShift Container Platform web console as the `cluster-admin` role.
* You can log in to the {hybrid-console}.

.Procedure
. Go to the *Register disconnected cluster* web page on the {hybrid-console}.

. Optional: To access the *Register disconnected cluster* web page from the home page of the {hybrid-console}, go to the *Cluster List* navigation menu item and then select the *Register cluster* button.

. Enter your cluster's details in the provided fields on the *Register disconnected cluster* page.

. From the *Subscription settings* section of the page, select the subscription settings that apply to your Red{nbsp}Hat subscription offering.

. To register your disconnected cluster, select the *Register cluster* button.

* How does the subscriptions service show my subscription data?(Getting Started with the Subscription Service)

// Updating the global cluster pull secret
// Module included in the following assemblies:
// * openshift_images/managing_images/using-image-pull-secrets.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc
// * support/remote_health_monitoring/remote-health-reporting.adoc
//
// Not included, but linked to from:
// * operators/admin/olm-managing-custom-catalogs.adoc

[id="images-update-global-pull-secret_{context}"]
= Updating the global cluster pull secret

[role="_abstract"]
To add new registries or update authentication for your OpenShift Container Platform cluster, you can update the global pull secret by appending new credentials to the _additional-pull-secret_. To do this, you can use the `oc set data secret/additional-pull-secret -n kube-system` command. Hypershift manages the new credential propagation among the HostedCluster nodes.

This feature provides a dedicated mechanism to separate your private credentials from the pull secret managed by the service, ensuring cluster functionality while restricting external visibility of your sensitive data. This separation allows you to independently rotate secrets and maintain exclusive ownership for compliance without impacting core managed service operations.

OpenShift Container Platform already has some immutable entries in the file, and you will not be able to modify those. If you are in this situation, you can follow this approach to use the same registry with different credentials.
This is a sample of authentication that is already in place:

[source,terminal]
----
"auths":
  "<quay.io: xxxxYYYzzzz>"
----
In the following case you can add a more specific entry such as:

[source,terminal]
----
"auths":
  "<quay.io/sampleNamespace": 111445656>"
----
This adds a new layer to the pull secret without affecting the original registry entry.

Use this procedure when you need a separate registry to store images than the registry used during installation.

[IMPORTANT]
====
The global pull secret is a HostedControlPlane feature only and is not an OCP standalone feature.
The global pull secret is a HostedControlPlane feature only and is not an OCP standalone feature and is also only available on OpenShift Container Platform version 4.20.6 and later.

To transfer your cluster to another owner, you must initiate the transfer in {cluster-manager-url} and then update the pull secret on the cluster. Updating a cluster's pull secret without initiating the transfer in {cluster-manager} causes the cluster to stop reporting Telemetry metrics in {cluster-manager}.

For more information, see _Transferring cluster ownership_ under _Additional resources_ in the {cluster-manager-first} documentation.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Optional: To append a new pull secret to the existing pull secret:
+
.. Download the pull secret by entering the following command:
+
[source,terminal]
----
$ oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > <pull_secret_location>
----
+
--
where:

`<pull_secret_location>`:: Specifies the path to the pull secret file.
--

.. Add the new pull secret by entering the following command:
+
[source,terminal]
----
$ oc registry login --registry="<registry>" \
--auth-basic="<username>:<password>" \
--to=<pull_secret_location>
----
+
--
where:

`<registry>`:: Specifies the new registry. You can include many repositories within the same registry, for example: `--registry="<registry/my-namespace/my-repository>`.

`<username>:<password>`:: Specifies the credentials of the new registry.

`<pull_secret_location>`:: Specifies the path to the pull secret file.
--
. Update the global pull secret for your cluster by entering the following command. Note that this update rolls out to all nodes, which can take some time depending on the size of your cluster.
+
[source,terminal]
----
$ oc set data secret/pull-secret -n openshift-config \
  --from-file=.dockerconfigjson=<pull_secret_location>
----
+
--
where:

`<pull_secret_location>`:: Specifies the path to the new pull secret file.
--
+
This merges your additional pull secret with the original HostedCluster pull secret, making it available to all nodes in the cluster.

. Optional: Modify the additional pull secret added by entering the following command:
+
[source,terminal]
----
$ oc edit secret additional-pull-secret -n kube-system
----
+
The secret must contain a valid DockerConfigJSON format.
+
.Example pull secret
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: additional-pull-secret
  namespace: kube-system
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: <base64-encoded-docker-config-json>
----
+
This results in the following states of the each pull secret:

* *Original*: immutable
* *Additional*: mutable
* *Global*: final state of both the original and additional pull secrets

. Optional: Delete the additional pull secret added by entering the following command:
+
[source,terminal]
----
$ oc delete secret additional-pull-secret -n kube-system
----
+
This triggers the automatic cleanup process across your nodes.

[role=_additional_resources]
.Additional resources

* Transferring cluster ownership
