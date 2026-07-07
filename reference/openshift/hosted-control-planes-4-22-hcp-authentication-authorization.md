---
title: "Authentication and authorization for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-authentication-authorization
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-authentication-authorization
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Authentication and authorization for {hcp}

[id="hcp-authentication-authorization"]
= Authentication and authorization for {hcp}

The OpenShift Container Platform control plane includes a built-in OAuth server. You can obtain OAuth access tokens to authenticate to the OpenShift Container Platform API. After you create your hosted cluster, you can configure OAuth by specifying an identity provider.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-authentication-authorization.adoc

[id="hcp-configuring-oauth_{context}"]
= Configuring the OAuth server for a hosted cluster by using the CLI

You can configure the internal OAuth server for your hosted cluster by using the CLI.

You can configure OAuth for the following supported identity providers:

* `oidc`
* `htpasswd`
* `keystone`
* `ldap`
* `basic-authentication`
* `request-header`
* `github`
* `gitlab`
* `google`

Adding any identity provider in the OAuth configuration removes the default `kubeadmin` user provider.

[NOTE]
====
When you configure identity providers, you must configure at least one `NodePool` replica in your hosted cluster in advance. Traffic for DNS resolution is sent through the worker nodes. You do not need to configure the `NodePool` replicas in advance for the `htpasswd` and `request-header` identity providers.
====

.Prerequisites

* You created your hosted cluster.

.Procedure

. Edit the `HostedCluster` custom resource (CR) on the hosting cluster by running the following command:
+
[source,terminal]
----
$ oc edit hostedcluster <hosted_cluster_name> -n <hosted_cluster_namespace>
----

. Add the OAuth configuration in the `HostedCluster` CR by using the following example:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1alpha1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name> <1>
  namespace: <hosted_cluster_namespace> <2>
spec:
  configuration:
    oauth:
      identityProviders:
      - openID: <3>
          claims:
            email: <4>
              - <email_address>
            name: <5>
              - <display_name>
            preferredUsername: <6>
              - <preferred_username>
          clientID: <client_id> <7>
          clientSecret:
            name: <client_id_secret_name> <8>
          issuer: https://example.com/identity <9>
        mappingMethod: lookup <10>
        name: IAM
        type: OpenID
----
<1> Specifies your hosted cluster name.
<2> Specifies your hosted cluster namespace.
<3> This provider name is prefixed to the value of the identity claim to form an identity name. The provider name is also used to build the redirect URL.
<4> Defines a list of attributes to use as the email address.
<5> Defines a list of attributes to use as a display name.
<6> Defines a list of attributes to use as a preferred user name.
<7> Defines the ID of a client registered with the OpenID provider. You must allow the client to redirect to the `\https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>` URL.
<8> Defines a secret of a client registered with the OpenID provider.
<9> The Issuer Identifier described in the OpenID spec. You must use `https` without query or fragment component.
<10> Defines a mapping method that controls how mappings are established between identities of this provider and `User` objects.

. Save the file to apply the changes.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-authentication-authorization.adoc

[id="hcp-configuring-oauth-console_{context}"]
= Configuring the OAuth server for a hosted cluster by using the web console

You can configure the internal OAuth server for your hosted cluster by using the OpenShift Container Platform web console.

You can configure OAuth for the following supported identity providers:

* `oidc`
* `htpasswd`
* `keystone`
* `ldap`
* `basic-authentication`
* `request-header`
* `github`
* `gitlab`
* `google`

Adding any identity provider in the OAuth configuration removes the default `kubeadmin` user provider.

[NOTE]
====
When you configure identity providers, you must configure at least one `NodePool` replica in your hosted cluster in advance. Traffic for DNS resolution is sent through the worker nodes. You do not need to configure the `NodePool` replicas in advance for the `htpasswd` and `request-header` identity providers.
====

.Prerequisites

* You logged in as a user with `cluster-admin` privileges.
* You created your hosted cluster.

.Procedure

. Navigate to *Home* -> *API Explorer*.

. Use the *Filter by kind* box to search for your `HostedCluster` resource.

. Click the `HostedCluster` resource that you want to edit.

. Click the *Instances* tab.

. Click the Options menu {kebab} next to your hosted cluster name entry and click *Edit HostedCluster*.

. Add the OAuth configuration in the YAML file:
+
[source,yaml]
----
spec:
  configuration:
    oauth:
      identityProviders:
      - openID: <1>
          claims:
            email: <2>
              - <email_address>
            name: <3>
              - <display_name>
            preferredUsername: <4>
              - <preferred_username>
          clientID: <client_id> <5>
          clientSecret:
            name: <client_id_secret_name> <6>
          issuer: https://example.com/identity <7>
        mappingMethod: lookup <8>
        name: IAM
        type: OpenID
----
<1> This provider name is prefixed to the value of the identity claim to form an identity name. The provider name is also used to build the redirect URL.
<2> Defines a list of attributes to use as the email address.
<3> Defines a list of attributes to use as a display name.
<4> Defines a list of attributes to use as a preferred user name.
<5> Defines the ID of a client registered with the OpenID provider. You must allow the client to redirect to the `\https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>` URL.
<6> Defines a secret of a client registered with the OpenID provider.
<7> The Issuer Identifier described in the OpenID spec. You must use `https` without query or fragment component.
<8> Defines a mapping method that controls how mappings are established between identities of this provider and `User` objects.

. Click *Save*.

[role="_additional-resources"]
.Additional resources

* To know more about supported identity providers, see "Understanding identity provider configuration" in _Authentication and authorization_.

[id="hcp-cco-aws-sts_{context}"]
== Assigning components IAM roles by using the CCO in a hosted cluster on {aws-short}

You can assign components IAM roles that provide short-term, limited-privilege security credentials by using the Cloud Credential Operator (CCO) in hosted clusters on {aws-first}. By default, the CCO runs in a hosted control plane.

[NOTE]
====
The CCO supports a manual mode only for hosted clusters on {aws-short}. By default, hosted clusters are configured in a manual mode. The management cluster might use modes other than manual.
====

// Module included in the following assemblies:
//
// Hosted control plane assemblies
// * hosted_control_planes/hcp-authentication-authorization.adoc

[id="hcp-cco-verify-aws-sts_{context}"]
= Verifying the CCO installation in a hosted cluster on {aws-short}

You can verify that the Cloud Credential Operator (CCO) is running correctly in your hosted control plane.

.Prerequisites

* You configured the hosted cluster on {aws-first}.

.Procedure

. Verify that the CCO is configured in a manual mode in your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get cloudcredentials <hosted_cluster_name> \
  -n <hosted_cluster_namespace> \
  -o=jsonpath={.spec.credentialsMode}
----
+
.Expected output
[source,terminal]
----
Manual
----

. Verify that the value for the `serviceAccountIssuer` resource is not empty by running the following command:
+
[source,terminal]
----
$ oc get authentication cluster --kubeconfig <hosted_cluster_name>.kubeconfig \
  -o jsonpath --template '{.spec.serviceAccountIssuer }'
----
+
.Example output
[source,terminal]
----
https://aos-hypershift-ci-oidc-29999.s3.us-east-2.amazonaws.com/hypershift-ci-29999
----

// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-token-auth.adoc
// * hosted_control_planes/hcp-authentication-authorization.adoc

[id="osdk-cco-aws-sts-enabling_{context}"]
= Enabling Operators to support CCO-based workflows with AWS STS

As an Operator author designing your project to run on Operator Lifecycle Manager (OLM), you can enable your Operator to authenticate against AWS on STS-enabled OpenShift Container Platform clusters by customizing your project to support the Cloud Credential Operator (CCO).

With this method, the Operator is responsible for and requires RBAC permissions for creating the `CredentialsRequest` object and reading the resulting `Secret` object.

[NOTE]
====
By default, pods related to the Operator deployment mount a `serviceAccountToken` volume so that the service account token can be referenced in the resulting `Secret` object.
====

.Prerequisites

* OpenShift Container Platform 4.14 or later
* Cluster in STS mode
* OLM-based Operator project

.Procedure

. Update your Operator project's `ClusterServiceVersion` (CSV) object:

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

.. Add the following annotation to claim support for this method of CCO-based workflow with AWS STS:
+
[source,yaml]
----
# ...
metadata:
 annotations:
   features.operators.openshift.io/token-auth-aws: "true"
----

. Update your Operator project code:

.. Get the role ARN from the environment variable set on the pod by the `Subscription` object. For example:
+
[source,go]
----
// Get ENV var
roleARN := os.Getenv("ROLEARN")
setupLog.Info("getting role ARN", "role ARN = ", roleARN)
webIdentityTokenPath := "/var/run/secrets/openshift/serviceaccount/token"
----

.. Ensure you have a `CredentialsRequest` object ready to be patched and applied. For example:
+
.Example `CredentialsRequest` object creation
[%collapsible]
====
[source,go]
----
import (
   minterv1 "github.com/openshift/cloud-credential-operator/pkg/apis/cloudcredential/v1"
   corev1 "k8s.io/api/core/v1"
   metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

var in = minterv1.AWSProviderSpec{
   StatementEntries: []minterv1.StatementEntry{
      {
         Action: []string{
            "s3:*",
         },
         Effect:   "Allow",
         Resource: "arn:aws:s3:*:*:*",
      },
   },
	STSIAMRoleARN: "<role_arn>",
}

var codec = minterv1.Codec
var ProviderSpec, _ = codec.EncodeProviderSpec(in.DeepCopyObject())

const (
   name      = "<credential_request_name>"
   namespace = "<namespace_name>"
)

var CredentialsRequestTemplate = &minterv1.CredentialsRequest{
   ObjectMeta: metav1.ObjectMeta{
       Name:      name,
       Namespace: "openshift-cloud-credential-operator",
   },
   Spec: minterv1.CredentialsRequestSpec{
      ProviderSpec: ProviderSpec,
      SecretRef: corev1.ObjectReference{
         Name:      "<secret_name>",
         Namespace: namespace,
      },
      ServiceAccountNames: []string{
         "<service_account_name>",
      },
      CloudTokenPath:   "",
   },
}
----
====
+
Alternatively, if you are starting from a `CredentialsRequest` object in YAML form (for example, as part of your Operator project code), you can handle it differently:
+
.Example `CredentialsRequest` object creation in YAML form
[%collapsible]
====
[source,go]
----
// CredentialsRequest is a struct that represents a request for credentials
type CredentialsRequest struct {
  APIVersion string `yaml:"apiVersion"`
  Kind       string `yaml:"kind"`
  Metadata   struct {
     Name      string `yaml:"name"`
     Namespace string `yaml:"namespace"`
  } `yaml:"metadata"`
  Spec struct {
     SecretRef struct {
        Name      string `yaml:"name"`
        Namespace string `yaml:"namespace"`
     } `yaml:"secretRef"`
     ProviderSpec struct {
        APIVersion     string `yaml:"apiVersion"`
        Kind           string `yaml:"kind"`
        StatementEntries []struct {
           Effect   string   `yaml:"effect"`
           Action   []string `yaml:"action"`
           Resource string   `yaml:"resource"`
        } `yaml:"statementEntries"`
        STSIAMRoleARN   string `yaml:"stsIAMRoleARN"`
     } `yaml:"providerSpec"`

     // added new field
      CloudTokenPath   string `yaml:"cloudTokenPath"`
  } `yaml:"spec"`
}

// ConsumeCredsRequestAddingTokenInfo is a function that takes a YAML filename and two strings as arguments
// It unmarshals the YAML file to a CredentialsRequest object and adds the token information.
func ConsumeCredsRequestAddingTokenInfo(fileName, tokenString, tokenPath string) (*CredentialsRequest, error) {
  // open a file containing YAML form of a CredentialsRequest
  file, err := os.Open(fileName)
  if err != nil {
     return nil, err
  }
  defer file.Close()

  // create a new CredentialsRequest object
  cr := &CredentialsRequest{}

  // decode the yaml file to the object
  decoder := yaml.NewDecoder(file)
  err = decoder.Decode(cr)
  if err != nil {
     return nil, err
  }

  // assign the string to the existing field in the object
  cr.Spec.CloudTokenPath = tokenPath

  // return the modified object
  return cr, nil
}
----
====
+
[NOTE]
====
Adding a `CredentialsRequest` object to the Operator bundle is not currently supported.
====

.. Add the role ARN and web identity token path to the credentials request and apply it during Operator initialization:
+
.Example applying `CredentialsRequest` object during Operator initialization
[%collapsible]
====
[source,go]
----
// apply CredentialsRequest on install
credReq := credreq.CredentialsRequestTemplate
credReq.Spec.CloudTokenPath = webIdentityTokenPath

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
           // add to this error with a pointer to instructions for following a manual path to a Secret that will work on STS
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

.. Set up the AWS configuration by reading the secret created by the CCO from the credentials request and creating the AWS config file containing the data from that secret:
+
.Example AWS configuration creation
[%collapsible]
====
[source,go]
----
func SharedCredentialsFileFromSecret(secret *corev1.Secret) (string, error) {
   var data []byte
   switch {
   case len(secret.Data["credentials"]) > 0:
       data = secret.Data["credentials"]
   default:
       return "", errors.New("invalid secret for aws credentials")
   }

   f, err := ioutil.TempFile("", "aws-shared-credentials")
   if err != nil {
       return "", errors.Wrap(err, "failed to create file for shared credentials")
   }
   defer f.Close()
   if _, err := f.Write(data); err != nil {
       return "", errors.Wrapf(err, "failed to write credentials to %s", f.Name())
   }
   return f.Name(), nil
}
----
====
+
[IMPORTANT]
====
The secret is assumed to exist, but your Operator code should wait and retry when using this secret to give time to the CCO to create the secret.

Additionally, the wait period should eventually time out and warn users that the OpenShift Container Platform cluster version, and therefore the CCO, might be an earlier version that does not support the `CredentialsRequest` object workflow with STS detection. In such cases, instruct users that they must add a secret by using another method.
====

.. Configure the AWS SDK session, for example:
+
.Example AWS SDK session configuration
[%collapsible]
====
[source,go]
----
sharedCredentialsFile, err := SharedCredentialsFileFromSecret(secret)
if err != nil {
   // handle error
}
options := session.Options{
   SharedConfigState: session.SharedConfigEnable,
   SharedConfigFiles: []string{sharedCredentialsFile},
}
----
====

[role="_additional-resources"]
.Additional resources

* Cluster Operators reference page for the Cloud Credential Operator
