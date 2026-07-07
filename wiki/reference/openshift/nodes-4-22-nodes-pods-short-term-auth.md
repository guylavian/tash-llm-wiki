---
title: "Authenticating pods with short-term credentials"
type: reference
domain: openshift
slug: nodes-4-22-nodes-pods-short-term-auth
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-pods-short-term-auth
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Authenticating pods with short-term credentials

[id="nodes-pods-short-term-auth"]
= Authenticating pods with short-term credentials

Some OpenShift Container Platform clusters use short-term security credentials for individual components that are created and managed outside the cluster.
Applications in customer workloads on these clusters can authenticate by using the short-term authentication method that the cluster uses.

[id="nodes-pods-short-term-auth-configuring_{context}"]
== Configuring short-term authentication for workloads

To use this authentication method in your applications, you must complete the following steps:

. Create a federated identity service account in the Identity and Access Management (IAM) settings for your cloud provider.

. Create an OpenShift Container Platform service account that can impersonate a service account for your cloud provider.

. Configure any workloads related to your application to use the OpenShift Container Platform service account.

[id="nodes-pods-short-term-auth-prereqs_{context}"]
=== Environment and user access requirements

To configure this authentication method, you must meet the following requirements:

* Your cluster must use short-term security credentials.

* You must have access to the {oc-first} as a user with the `cluster-admin` role.

* In your cloud provider console, you must have access as a user with privileges to manage Identity and Access Management (IAM) and federated identity configurations.

// Section to add with AWS and Azure content. Only documenting GCP at this time.
[id="nodes-pods-short-term-auth-compatibility_{context}"]
=== Compatibility limitations

This authentication method is only supported for {aws-first}, {gcp-first}, and {azure-full} clusters.
You can only authenticate workloads with short-term credentials by using the same authentication method as the cluster.

.Supported configurations for workload authentication with short-term credentials
[cols="<.^h,^.^,^.^,^.^"]
|====
|Cluster configuration |Workload authentication with {aws-short} {sts-short} |Workload authentication with {gcp-wid-short} |Workload authentication with {entra-first}

|{aws-short} with {aws-short} {sts-short}
|*Supported*
|Unsupported
|Unsupported

|{aws-short} without {aws-short} {sts-short}
|Unsupported
|Unsupported
|Unsupported

|{gcp-short} with {gcp-wid-short}
|Unsupported
|*Supported*
|Unsupported

|{gcp-short} without {gcp-wid-short}
|Unsupported
|Unsupported
|Unsupported

|{azure-short} with {entra-short}
|Unsupported
|Unsupported
|*Supported*

|{azure-short} without {entra-short}
|Unsupported
|Unsupported
|Unsupported
|====

// Content stub for later addition:

[id="nodes-pods-short-term-auth-configuring-aws_{context}"]
== Configuring {aws-short} {sts-short} authentication for applications on {aws-short}

#Placeholder for {aws-short} {sts-short} version#

To use short-term authentication for applications on an {aws-short} cluster that uses {sts-short} authentication, you must complete the following steps:

. Configure access in {aws-short}.
. Create an OpenShift Container Platform service account that can use this access.
. Deploy customer workloads that authenticate with {aws-short} {sts-short}.

#Placeholder for {aws-short} {sts-short} version#

[id="nodes-pods-short-term-auth-configuring-gcp_{context}"]
== Configuring {gcp-wid-short} authentication for applications on {gcp-short}

To use short-term authentication for applications on a {gcp-short} clusters that use {gcp-wid-short} authentication, you must complete the following steps:

. Configure access in {gcp-short}.
. Create an OpenShift Container Platform service account that can use this access.
. Deploy customer workloads that authenticate with {gcp-wid-short}.

// Creating a federated GCP service account
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-short-term-auth.adoc

[id="pod-short-term-auth-gcp-cloud-sa_{context}"]
= Creating a federated {gcp-short} service account

You can use the {gcp-full} console to create a workload identity pool and provider and allow an OpenShift Container Platform service account to impersonate a {gcp-short} service account.

.Prerequisites

* Your {gcp-short} cluster uses {gcp-wid-short}.

* You have access to the {gcp-full} console as a user with privileges to manage Identity and Access Management (IAM) and workload identity configurations.

* You have created a {gcp-full} project to use with your application.

.Procedure

. In the IAM configuration for your {gcp-full} project, identify the identity pool and provider that the cluster uses for {gcp-wid-short} authentication.

. Grant permission for external identities to impersonate a {gcp-short} service account.
With these permissions, an OpenShift Container Platform service account can work as a federated workload identity.
+
For more information, see {gcp-short} documentation about allowing your external workload to access {gcp-full} resources.

// Creating an OpenShift Container Platform service account for GCP
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-short-term-auth.adoc

[id="pod-short-term-auth-gcp-cluster-sa_{context}"]
= Creating an OpenShift Container Platform service account for {gcp-short}

You create an OpenShift Container Platform service account and annotate it to impersonate a {gcp-short} service account.

.Prerequisites

* Your {gcp-short} cluster uses {gcp-wid-short}.

* You have created a federated {gcp-short} service account.

* You have access to the {oc-first} as a user with the `cluster-admin` role.

* You have access to the {gcp-full} CLI (`gcloud`) as a user with privileges to manage Identity and Access Management (IAM) and workload identity configurations.

.Procedure

. Create an OpenShift Container Platform service account to use for {gcp-wid-short} pod authentication by running the following command:
+
[source,terminal]
----
$ oc create serviceaccount <service_account_name>
----

. Annotate the service account with the identity provider and {gcp-short} service account to impersonate by running the following command:
+
[source,terminal]
----
$ oc patch serviceaccount <service_account_name> -p '{"metadata": {"annotations": {"cloud.google.com/workload-identity-provider": "projects/<project_number>/locations/global/workloadIdentityPools/<identity_pool>/providers/<identity_provider>"}}}'
----
+
Replace `<project_number>`, `<identity_pool>`, and `<identity_provider>` with the values for your configuration.
+
[NOTE]
====
For `<project_number>`, specify the {gcp-full} project number, not the project ID.
====

. Annotate the service account with the email address for the {gcp-short} service account by running the following command:
+
[source,terminal]
----
$ oc patch serviceaccount <service_account_name> -p '{"metadata": {"annotations": {"cloud.google.com/service-account-email": "<service_account_email>"}}}'
----
+
Replace `<service_account_email>` with the email address for the {gcp-short} service account.
+
[TIP]
====
{gcp-short} service account email addresses typically use the format `<service_account_name>@<project_id>.iam.gserviceaccount.com`
====

. Annotate the service account to use the `direct` external credentials configuration injection mode by running the following command:
+
[source,terminal]
----
$ oc patch serviceaccount <service_account_name> -p '{"metadata": {"annotations": {"cloud.google.com/injection-mode": "direct"}}}'
----
+
In this mode, the Workload Identity Federation webhook controller directly generates the {gcp-short} external credentials configuration and injects them into the pod.

. Use the {gcp-full} CLI (`gcloud`) to specify the permissions for the workload by running the following command:
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding <project_id> --member "<service_account_email>" --role "projects/<project_id>/roles/<role_for_workload_permissions>"
----
+
Replace `<role_for_workload_permissions>` with the role for the workload.
Specify a role that grants the permissions that your workload requires.

.Verification

* To verify the service account configuration, inspect the `ServiceAccount` manifest by running the following command:
+
[source,terminal]
----
$ oc get serviceaccount <service_account_name>
----
+
In the following example, the `service-a/app-x` OpenShift Container Platform service account can impersonate a {gcp-short} service account called `app-x`:
+
.Example output
--
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-x
  namespace: service-a
  annotations:
    cloud.google.com/workload-identity-provider: "projects/<project_number>/locations/global/workloadIdentityPools/<identity_pool>/providers/<identity_provider>" <1>
    cloud.google.com/service-account-email: "app-x@project.iam.googleapis.com"
    cloud.google.com/audience: "sts.googleapis.com" <2>
    cloud.google.com/token-expiration: "86400" <3>
    cloud.google.com/gcloud-run-as-user: "1000"
    cloud.google.com/injection-mode: "direct" <4>
----
<1> The workload identity provider for the service account of the cluster.
<2> The allowed audience for the workload identity provider.
<3> The token expiration time period in seconds.
<4> The `direct` external credentials configuration injection mode.
--

// Deploying a pod that authenticates with {gcp-wid-short}
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-short-term-auth.adoc

[id="pod-short-term-auth-gcp-deploy-pod_{context}"]
= Deploying customer workloads that authenticate with {gcp-wid-short}

To use short-term authentication in your application, you must configure its related pods to use the OpenShift Container Platform service account.
Use of the OpenShift Container Platform service account triggers the webhook to mutate the pods so they can impersonate the {gcp-short} service account.

The following example demonstrates how to deploy a pod that uses the OpenShift Container Platform service account and verify the configuration.

.Prerequisites

* Your {gcp-short} cluster uses {gcp-wid-short}.

* You have created a federated {gcp-short} service account.

* You have created an OpenShift Container Platform service account for {gcp-short}.

.Procedure

. To create a pod that authenticates with {gcp-wid-short}, create a deployment YAML file similar to the following example:
+
.Sample deployment
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ubi9
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ubi9
  template:
    metadata:
      labels:
        app: ubi9
    spec:
      serviceAccountName: "<service_account_name>" <1>
      containers:
        - name: ubi
          image: 'registry.access.redhat.com/ubi9/ubi-micro:latest'
          command:
            - /bin/sh
            - '-c'
            - |
              sleep infinity
----
<1> Specify the name of the OpenShift Container Platform service account.

. Apply the deployment file by running the following command:
+
[source,terminal]
----
$ oc apply -f deployment.yaml
----

.Verification

* To verify that a pod is using short-term authentication, run the following command:
+
[source,terminal]
----
$ oc get pods -o json | jq -r '.items[0].spec.containers[0].env[] | select(.name=="GOOGLE_APPLICATION_CREDENTIALS")'
----
+
.Example output
[source,terminal]
----
{   "name": "GOOGLE_APPLICATION_CREDENTIALS",   "value": "/var/run/secrets/workload-identity/federation.json" }
----
+
The presence of the `GOOGLE_APPLICATION_CREDENTIALS` environment variable indicates a pod that authenticates with {gcp-wid-short}.

* To verify additional configuration details, examine the pod specification.
The following example pod specifications show the environment variables and volume fields that the webhook mutates.
+
--
.Example pod specification with the `direct` injection mode:
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: app-x-pod
  namespace: service-a
annotations:
  cloud.google.com/skip-containers: "init-first,sidecar"
  cloud.google.com/external-credentials-json: |- <1>
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/projects/<project_number>/locations/global/workloadIdentityPools/on-prem-kubernetes/providers/<identity_provider>",
      "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
      "token_url": "https://sts.googleapis.com/v1/token",
      "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/app-x@project.iam.gserviceaccount.com:generateAccessToken",
      "credential_source": {
        "file": "/var/run/secrets/sts.googleapis.com/serviceaccount/token",
        "format": {
          "type": "text"
        }
      }
    }
spec:
  serviceAccountName: app-x
  initContainers:
  - name: init-first
    image: container-image:version
  containers:
  - name: sidecar
    image: container-image:version
  - name: container-name
    image: container-image:version
    env: <2>
    - name: GOOGLE_APPLICATION_CREDENTIALS
      value: /var/run/secrets/gcloud/config/federation.json
    - name: CLOUDSDK_COMPUTE_REGION
      value: asia-northeast1
    volumeMounts:
    - name: gcp-iam-token
      readOnly: true
      mountPath: /var/run/secrets/sts.googleapis.com/serviceaccount
    - mountPath: /var/run/secrets/gcloud/config
      name: external-credential-config
      readOnly: true
  volumes:
  - name: gcp-iam-token
    projected:
      sources:
      - serviceAccountToken:
          audience: sts.googleapis.com
          expirationSeconds: 86400
          path: token
  - downwardAPI:
      defaultMode: 288
      items:
      - fieldRef:
          apiVersion: v1
          fieldPath: metadata.annotations['cloud.google.com/external-credentials-json']
        path: federation.json
    name: external-credential-config
----
<1> The external credentials configuration generated by the webhook controller.
The Kubernetes `downwardAPI` volume mounts the configuration into the container filesystem.
<2> The webhook-injected environment variables for token-based authentication.
--

// Content stub for later addition:
[id="nodes-pods-short-term-auth-configuring-azure_{context}"]
== Configuring {entra-first} authentication for applications on {azure-short}

#Placeholder for {entra-short} version#

To use short-term authentication for applications on an {azure-short} cluster that uses {entra-short} authentication, you must complete the following steps:

. Configure access in {azure-short}.
. Create an OpenShift Container Platform service account that can use this access.
. Deploy customer workloads that authenticate with {entra-short}.

#Placeholder for {entra-short} version#
