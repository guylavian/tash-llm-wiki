---
title: "CCO-based workflow for OLM-managed Operators with {gcp-wid-short}"
type: reference
domain: openshift
slug: operators-4-22-osdk-cco-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/osdk-cco-gcp
version: 4.22
family: operators
documentKind: "Documentation"
---

# CCO-based workflow for OLM-managed Operators with {gcp-wid-short}

[id="osdk-cco-gcp"]
= CCO-based workflow for OLM-managed Operators with {gcp-wid-short}

When an OpenShift Container Platform cluster running on {gcp-first} is in *{gcp-wid-short} / Federated Identity* mode, it means the cluster is utilizing features of {gcp-first} and OpenShift Container Platform to apply permissions in {gcp-wid-short} at an application level.

The Cloud Credential Operator (CCO) is a cluster Operator installed by default in OpenShift Container Platform clusters running on cloud providers. Starting in OpenShift Container Platform 4.17, the CCO supports workflows for OLM-managed Operators with {gcp-wid-short}.

For the purposes of {gcp-wid-short}, the CCO provides the following functions:

* Detects when it is running on an {gcp-wid-short}-enabled cluster
* Checks the `CredentialsRequest` object for the presence of fields that provide the required information for granting Operators access to {gcp-short} resources

The CCO can semi-automate this process through an expanded use of `CredentialsRequest` objects, which can request the creation of `Secrets` that contain the information required for {gcp-wid-short} workflows.

[NOTE]
====
Subscriptions with automatic approvals for updates are not recommended because there might be permission changes to make before updating. Subscriptions with manual approvals for updates ensure that administrators have the opportunity to verify the permissions of the later version, take any necessary steps, and then update.
====

As an Operator author preparing an Operator for use alongside the updated CCO in OpenShift Container Platform 4.17 and later, you should instruct users and add code to handle the divergence from earlier CCO versions, in addition to handling {gcp-wid-short} token authentication (if your Operator is not already enabled). The recommended method is to provide a `CredentialsRequest` object with the correctly filled {gcp-wid-short} fields and let the CCO create the `Secret` object for you.

[IMPORTANT]
====
If you plan to support OpenShift Container Platform clusters earlier than version 4.17, consider providing users with instructions on how to manually create a secret with the {gcp-wid-short}-enabling information by using the CCO utility (`ccoctl`). Earlier CCO versions are unaware of {gcp-wid-short} mode on the cluster and cannot create secrets for you.

Your code should check for secrets that never appear and warn users to follow the fallback instructions you have provided.
====

To authenticate with {gcp-short} using short-lived tokens via {gcp-wid-first}, Operators must provide the following information:

`AUDIENCE`::
Created in {gcp-short} by the administrator when they set up {gcp-wid-short}, the `AUDIENCE` value must be a preformatted URL in the following format:
+
[source,text]
----
//iam.googleapis.com/projects/<project_number>/locations/global/workloadIdentityPools/<pool_id>/providers/<provider_id>
----

`SERVICE_ACCOUNT_EMAIL`::
The `SERVICE_ACCOUNT_EMAIL` value is a {gcp-short} service account email that is impersonated during Operator operation, for example:
+
[source,text]
----
<service_account_name>@<project_id>.iam.gserviceaccount.com
----

The *Install Operator* page in the web console allows cluster administrators to provide this information at installation time. This information is then propagated to the `Subscription` object as environment variables on the Operator pod.

[role="_additional-resources"]
.Additional resources

* OLM-managed Operator support for authentication with {gcp-wid-short}
* Installing from OperatorHub using the web console
* Installing from OperatorHub using the CLI

// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-token-auth/osdk-cco-gcp.adoc

[id="osdk-cco-gcp-enabling_{context}"]
= Enabling Operators to support CCO-based workflows with {gcp-wid-short}

As an Operator author designing your project to run on Operator Lifecycle Manager (OLM), you can enable your Operator to authenticate against {gcp-wid-first} on OpenShift Container Platform clusters by customizing your project to support the Cloud Credential Operator (CCO).

With this method, the Operator is responsible for and requires RBAC permissions for creating the `CredentialsRequest` object and reading the resulting `Secret` object.

[NOTE]
====
By default, pods related to the Operator deployment mount a `serviceAccountToken` volume so that the service account token can be referenced in the resulting `Secret` object.
====

.Prerequisites

* OpenShift Container Platform 4.17 or later
* Cluster in *{gcp-wid-short} / Federated Identity* mode
* OLM-based Operator project

.Procedure

. Update your Operator project's `ClusterServiceVersion` (CSV) object:

.. Ensure Operator deployment in the CSV has the following `volumeMounts` and `volumes` fields so that the Operator can assume the role with web identity:
+
.Example `volumeMounts` and `volumes` fields
[%collapsible]
====
[source,yaml]
----
# ...
      volumeMounts:

      - name: bound-sa-token
        mountPath: /var/run/secrets/openshift/serviceaccount
        readOnly: true
      volumes:
         # This service account token can be used to provide identity outside the cluster.
         - name: bound-sa-token
           projected:
             sources:
             - serviceAccountToken:
               path: token
               audience: openshift
----
====

.. Ensure your Operator has RBAC permission to create `CredentialsRequests` objects:
+
.Example `clusterPermissions` list
[%collapsible]
====
[source,yaml]
----
# ...
install:
  spec:
    clusterPermissions:
    - rules:
      - apiGroups:
        - "cloudcredential.openshift.io"
        resources:
        - credentialsrequests
        verbs:
        - create
        - delete
        - get
        - list
        - patch
        - update
        - watch
----
====

.. Add the following annotation to claim support for this method of CCO-based workflow with {gcp-wid-short}:
+
[source,yaml]
----
# ...
metadata:
 annotations:
   features.operators.openshift.io/token-auth-gcp: "true"
----

. Update your Operator project code:

.. Get the `audience` and the `serviceAccountEmail` values from the environment variables set on the pod by the subscription config:
+
[source,go]
----
 // Get ENV var
   audience := os.Getenv("AUDIENCE")
   serviceAccountEmail := os.Getenv("SERVICE_ACCOUNT_EMAIL")
   gcpIdentityTokenFile := "/var/run/secrets/openshift/serviceaccount/token"
----

.. Ensure you have a `CredentialsRequest` object ready to be patched and applied.
+
[NOTE]
====
Adding a `CredentialsRequest` object to the Operator bundle is not currently supported.
====

.. Add the {gcp-wid-short} variables to the credentials request and apply it during Operator initialization:
+
.Example applying `CredentialsRequest` object during Operator initialization
[%collapsible]
====
[source,go]
----
// apply CredentialsRequest on install
   credReqTemplate.Spec.GCPProviderSpec.Audience = audience
   credReqTemplate.Spec.GCPProviderSpec.ServiceAccountEmail = serviceAccountEmail
   credReqTemplate.CloudTokenPath = gcpIdentityTokenFile

   c := mgr.GetClient()
   if err := c.Create(context.TODO(), credReq); err != nil {
       if !errors.IsAlreadyExists(err) {
           setupLog.Error(err, "unable to create CredRequest")
           os.Exit(1)
       }
   }
----
====

.. Ensure your Operator can wait for a `Secret` object to show up from the CCO, as shown in the following example, which is called along with the other items you are reconciling in your Operator:
+
.Example wait for `Secret` object
[%collapsible]
====
[source,go]
----
// WaitForSecret is a function that takes a Kubernetes client, a namespace, and a v1 "k8s.io/api/core/v1" name as arguments
// It waits until the secret object with the given name exists in the given namespace
// It returns the secret object or an error if the timeout is exceeded
func WaitForSecret(client kubernetes.Interface, namespace, name string) (*v1.Secret, error) {
  // set a timeout of 10 minutes
  timeout := time.After(10 * time.Minute) <1>

  // set a polling interval of 10 seconds
  ticker := time.NewTicker(10 * time.Second)

  // loop until the timeout or the secret is found
  for {
     select {
     case <-timeout:
        // timeout is exceeded, return an error
        return nil, fmt.Errorf("timed out waiting for secret %s in namespace %s", name, namespace)
// add to this error with a pointer to instructions for following a manual path to a Secret that will work
     case <-ticker.C:
        // polling interval is reached, try to get the secret
        secret, err := client.CoreV1().Secrets(namespace).Get(context.Background(), name, metav1.GetOptions{})
        if err != nil {
           if errors.IsNotFound(err) {
              // secret does not exist yet, continue waiting
              continue
           } else {
              // some other error occurred, return it
              return nil, err
           }
        } else {
           // secret is found, return it
           return secret, nil
        }
     }
  }
}
----
<1> The `timeout` value is based on an estimate of how fast the CCO might detect an added `CredentialsRequest` object and generate a `Secret` object. You might consider lowering the time or creating custom feedback for cluster administrators that could be wondering why the Operator is not yet accessing the cloud resources.
====

.. Read the `service_account.json` field from the secret and use it to authenticate your {gcp-short} client:
+
[source,go]
----
service_account_json := secret.StringData["service_account.json"]
----
