---
title: "Providing sensitive data to pods by using secrets"
type: reference
domain: openshift
slug: nodes-4-22-nodes-pods-secrets
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-pods-secrets
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Providing sensitive data to pods by using secrets

[id="nodes-pods-secrets"]
= Providing sensitive data to pods by using secrets

[role="_abstract"]
As an administrator, you can use `Secret` objects to provide sensitive information, such as passwords and user names, to applications without exposing that information in plain text that developers could see.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-about_{context}"]
= Understanding secrets

[role="_abstract"]
You can mount secrets into containers by using a volume plugin or the system can use secrets to perform actions on behalf of a pod.

The `Secret` object type provides a mechanism to hold sensitive information such
as passwords, OpenShift Container Platform client configuration files,
private source repository credentials, and so on. Secrets decouple sensitive
content from the pods.

Key properties include:

- Secret data can be referenced independently from its definition.
- Secret data volumes are backed by temporary file-storage facilities (tmpfs) and never come to rest on a node.
- Secret data can be shared within a namespace.

.YAML `Secret` object definition

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
  namespace: my-namespace
type: Opaque
data:
  username: <username>
  password: <password>
stringData:
  hostname: myapp.mydomain.com
----
where:

`type`:: Specifies the structure of the secret's key names and values.
`data`:: Specifies the allowable format for the keys in the `data` field must meet the guidelines in the *DNS_SUBDOMAIN* value as described in "Identifiers and Names in Kubernetes" in the  Kubernetes documentation.
`data.username`:: Specifies the value associated with keys in the `data` map. This value must be base64 encoded.
`data.password`:: Specifies the value associated with keys in the `data` map. This value must be base64 encoded.
`stringData.hostname`:: Specifies the value associated with keys in the `data` map. The value associated with keys in the `stringData` map is made up of
plain text strings.
Entries in the `stringData` map are converted to base64
and the entry will then be moved to the `data` map automatically. This field
is write-only; the value will only be returned via the `data` field.

You must create a secret before creating the pods that depend on that secret.

When creating secrets:

- Create a secret object with secret data.
- Update the pod's service account to allow the reference to the secret.
- Create a pod, which consumes the secret as an environment variable or as a file
(using a `secret` volume).

[id="nodes-pods-secrets-about-types_{context}"]
== Types of secrets

The value in the `type` field indicates the structure of the secret's key names and values. The type can be used to
enforce the presence of user names and keys in the secret object. If you do not want validation, use the `opaque` type,
which is the default.

Specify one of the following types to trigger minimal server-side validation to ensure the presence of specific key names in the secret data:

* `kubernetes.io/basic-auth`: Use with Basic authentication
* `kubernetes.io/dockercfg`: Use as an image pull secret
* `kubernetes.io/dockerconfigjson`: Use as an image pull secret
* `kubernetes.io/service-account-token`: Use to obtain a legacy service account API token
* `kubernetes.io/ssh-auth`: Use with SSH key authentication
* `kubernetes.io/tls`: Use with TLS certificate authorities

Specify `type: Opaque` if you do not want validation, which means the secret does not claim to conform to any convention for key names or values.
An _opaque_ secret, allows for unstructured `key:value` pairs that can contain arbitrary values.

[NOTE]
====
You can specify other arbitrary types, such as `example.com/my-secret-type`. These types are not enforced server-side,
but indicate that the creator of the secret intended to conform to the key/value requirements of that type.
====

For examples of creating different types of secrets, see _Understanding how to create secrets_.

[id="nodes-pods-secrets-about-keys_{context}"]
== Secret data keys

Secret keys must be in a DNS subdomain.

// Module included in the following assemblies:
//
// * authentication/using-service-accounts-in-applications.adoc
// * pods/nodes-pods-secrets.adoc

[id="auto-generated-sa-token-secrets_{context}"]
= Automatically generated image pull secrets

[role="_abstract"]
OpenShift Container Platform automatically creates image pull secrets for each service account to integrate the internal image registry with user authentication.

[NOTE]
====
Prior to OpenShift Container Platform 4.16, a long-lived service account API token secret was also generated for each service account that was created. Starting with OpenShift Container Platform 4.16, this service account API token secret is no longer created.

After upgrading to , any existing long-lived service account API token secrets are not deleted and will continue to function. For information about detecting long-lived API tokens that are in use in your cluster or deleting them if they are not needed, see "Long-lived service account API tokens in OpenShift Container Platform (Red Hat Knowledgebase)".
====

This image pull secret is necessary to integrate the {product-registry} into the cluster's user authentication and authorization system.

However, if you do not enable the `ImageRegistry` capability or if you disable the integrated {product-registry} in the Cluster Image Registry Operator's configuration, an image pull secret is not generated for each service account.

When the integrated {product-registry} is disabled on a cluster that previously had it enabled, the previously generated image pull secrets are deleted automatically.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating_{context}"]
= Understanding how to create secrets

[role="_abstract"]
As an administrator you must create a secret before developers can create the pods that depend on that secret.

To use a secret, a pod needs to reference the secret. A secret can be used with
a pod in three ways:

- To populate environment variables for containers.
- As files in a volume mounted on one or more of its containers.
- By kubelet when pulling images for the pod.

Volume type secrets write data into the container as a file using the volume
mechanism. Image pull secrets use service accounts for the automatic injection of
the secret into all pods in a namespace.

When a template contains a secret definition, the only way for the template to
use the provided secret is to ensure that the secret volume sources are
validated and that the specified object reference actually points to a `Secret` object. Therefore, a secret needs to be created before any pods that
depend on it. The most effective way to ensure this is to have it get injected
automatically through the use of a service account.

Secret API objects reside in a namespace. They can only be referenced by pods in
that same namespace.

Individual secrets are limited to 1MB in size. This is to discourage the
creation of large secrets that could exhaust apiserver and kubelet memory.
However, creation of several smaller secrets could also exhaust memory.

.Procedure

. Create a secret object that contains the data you want to keep secret. The specific data required for each secret type is descibed in the following sections.
+
.Example YAML object that creates an opaque secret
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
type: Opaque
data:
  username: <username>
  password: <password>
stringData:
  hostname: myapp.mydomain.com
  secret.properties: |
    property1=valueA
    property2=valueB
----
where:
+
--
`type`:: Specifies the type of secret.
`data`:: Specifies encoded string and data.
`stringData`:: Specifies decoded string and data.
--
+
Use either the `data` or `stringdata` fields, not both.

. Update the pod's service account to reference the secret:
+
.YAML of a service account that uses a secret
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
 ...
secrets:
- name: test-secret
----

. Create a pod, which consumes the secret as an environment variable or as a file
(using a `secret` volume):
+
.YAML of a pod populating files in a volume with secret data
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: secret-example-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: secret-test-container
      image: busybox
      command: [ "/bin/sh", "-c", "cat /etc/secret-volume/*" ]
      volumeMounts:
          - name: secret-volume
            mountPath: /etc/secret-volume
            readOnly: true
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  volumes:
    - name: secret-volume
      secret:
        secretName: test-secret
  restartPolicy: Never
----
where:
+
--
`spec.container.volumeMounts`:: Specifies configurations for the secret. Add a `volumeMounts` field to each container that needs the secret.
`spec.container.volumeMounts.mountPath`:: Specifies an unused directory name where you want the secret to appear. Each key in the secret data map becomes the filename under `mountPath`.
`spec.container.volumeMounts.readOnly`::  If set to `true`, specifies that the driver should provide a read-only volume.
`spec.volumes.secret.secretName`:: Specifies the name of the secret.
--
+
.YAML of a pod populating environment variables with secret data
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: secret-example-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: secret-test-container
      image: busybox
      command: [ "/bin/sh", "-c", "export" ]
      env:
        - name: TEST_SECRET_USERNAME_ENV_VAR
          valueFrom:
            secretKeyRef:
              name: test-secret
              key: username
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  restartPolicy: Never
----
where:
+
--
`spec.containers.env.valueFrom.secretKeyRef`:: Specifies the environment variable that consumes the secret key.
--
+
.YAML of a build config populating environment variables with secret data
[source,yaml]
----
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: secret-example-bc
spec:
  strategy:
    sourceStrategy:
      env:
      - name: TEST_SECRET_USERNAME_ENV_VAR
        valueFrom:
          secretKeyRef:
            name: test-secret
            key: username
      from:
        kind: ImageStreamTag
        namespace: openshift
        name: 'cli:latest'
----
where:
+
--
`spec.strategy.sourceStrategy.env.valueFrom.secretKeyRef`:: Specifies the environment variable that consumes the secret key.
--

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating-opaque_{context}"]
= Creating an opaque secret

[role="_abstract"]
As an administrator, you can create an opaque secret, which allows you to store unstructured `key:value` pairs that can contain arbitrary values.

.Procedure

. Create a `Secret` object in a YAML file.
+
For example:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: <username>
  password: <password>
----
where:

`type`:: Specifies an opaque secret.

. Use the following command to create a `Secret` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. To use the secret in a pod:

.. Update the pod's service account to reference the secret, as shown in the "Understanding how to create secrets" section.

.. Create the pod, which consumes the secret as an environment variable or as a file (using a `secret` volume), as shown in the "Understanding how to create secrets" section.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating-sa_{context}"]
= Creating a legacy service account token secret

[role="_abstract"]
As an administrator, you can create a legacy service account token secret, which allows you to distribute a service account token to applications that must authenticate to the API.

[WARNING]
====
It is recommended to obtain bound service account tokens using the TokenRequest API instead of using legacy service account token secrets. You should create a service account token secret only if you cannot use the TokenRequest API and if the security exposure of a nonexpiring token in a readable API object is acceptable to you.

Bound service account tokens are more secure than service account token secrets for the following reasons:

* Bound service account tokens have a bounded lifetime.
* Bound service account tokens contain audiences.
* Bound service account tokens can be bound to pods or secrets and the bound tokens are invalidated when the bound object is removed.

Workloads are automatically injected with a projected volume to obtain a bound service account token. If your workload needs an additional service account token, add an additional projected volume in your workload manifest.

For more information, see "Configuring bound service account tokens using volume projection".
====

.Procedure

. Create a `Secret` object in a YAML file:
+
.Example `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: secret-sa-sample
  annotations:
    kubernetes.io/service-account.name: "sa-name"
type: kubernetes.io/service-account-token
----
where:

`metadata.annotations`:: Specifies an existing service account name. If you are creating both the `ServiceAccount` and the `Secret` objects, create the `ServiceAccount` object first.
`type`:: Specifies a service account token secret.

. Use the following command to create the `Secret` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. To use the secret in a pod:

.. Update the pod's service account to reference the secret, as shown in the "Understanding how to create secrets" section.

.. Create the pod, which consumes the secret as an environment variable or as a file (using a `secret` volume), as shown in the "Understanding how to create secrets" section.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating-basic_{context}"]
= Creating a basic authentication secret

[role="_abstract"]
As an administrator, you can create a basic authentication secret, which you can use to store the credentials needed for basic authentication.

When using this secret type, the `data` parameter of the `Secret` object must contain the following keys encoded in the base64 format:

* `username`: the user name for authentication
* `password`: the password or token for authentication

[NOTE]
====
You can use the `stringData` parameter to use clear text content.
====

.Procedure

. Create a `Secret` object in a YAML file:
+
.Example `secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: secret-basic-auth
type: kubernetes.io/basic-auth
data:
stringData:
  username: admin
  password: <password>
----
where:

`type`:: Specifies a basic authentication secret.
`stringData`:: Specifies the basic authentication values to use.

. Use the following command to create the `Secret` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. To use the secret in a pod:

.. Update the pod's service account to reference the secret, as shown in the "Understanding how to create secrets" section.

.. Create the pod, which consumes the secret as an environment variable or as a file (using a `secret` volume), as shown in the "Understanding how to create secrets" section.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating-ssh_{context}"]
= Creating an SSH authentication secret

[role="_abstract"]
As an administrator, you can create an SSH authentication secret, which you can use to store data used for SSH authentication.

When using this secret type, the `data` parameter of the `Secret` object must contain the SSH credential to use.

.Procedure

. Create a `Secret` object in a YAML file on a control plane node:
+
.Example `secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: secret-ssh-auth
type: kubernetes.io/ssh-auth <1>
data:
  ssh-privatekey: | <2>
          MIIEpQIBAAKCAQEAulqb/Y ...
----
where:

`type`:: Specifies an SSH authentication secret.
`data.ssh-privatekey`:: Specifies the SSH key/value pair as the SSH credentials to use.

. Use the following command to create the `Secret` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. To use the secret in a pod:

.. Update the pod's service account to reference the secret, as shown in the "Understanding how to create secrets" section.

.. Create the pod, which consumes the secret as an environment variable or as a file (using a `secret` volume), as shown in the "Understanding how to create secrets" section.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating-docker_{context}"]
= Creating a Docker configuration secret

[role="_abstract"]
As an administrator, you can create a Docker configuration secret, which allows you to store the credentials for accessing a container image registry.

* `kubernetes.io/dockercfg`. Use this secret type to store your local Docker configuration file. The `data` parameter of the `secret` object must contain the contents of a `.dockercfg` file encoded in the base64 format.

* `kubernetes.io/dockerconfigjson`. Use this secret type to store your local Docker configuration JSON file. The `data` parameter of the `secret` object must contain the contents of a `.docker/config.json` file encoded in the base64 format.

.Procedure

. Create a `Secret` object in a YAML file.
+
.Example Docker configuration `secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: secret-docker-cfg
  namespace: my-project
type: kubernetes.io/dockerconfig
data:
  .dockerconfig:bm5ubm5ubm5ubm5ubm5ubm5ubm5ubmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cgYXV0aCBrZXlzCg==
----
where:
+
--
`type`:: Specifies that the secret is using a Docker configuration file.
`data`:: Specifies the output of a base64-encoded Docker configuration file.
--
+
.Example Docker configuration JSON `secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: secret-docker-json
  namespace: my-project
type: kubernetes.io/dockerconfig
data:
  .dockerconfigjson:bm5ubm5ubm5ubm5ubm5ubm5ubm5ubmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cgYXV0aCBrZXlzCg==
----
where:
+
--
`type`:: Specifies that the secret is using a Docker configuration file.
`data`:: Specifies the output of a base64-encoded Docker configuration file.
--

. Use the following command to create the `Secret` object
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. To use the secret in a pod:

.. Update the pod's service account to reference the secret, as shown in the "Understanding how to create secrets" section.

.. Create the pod, which consumes the secret as an environment variable or as a file (using a `secret` volume), as shown in the "Understanding how to create secrets" section.

// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-creating-web-console-secrets_{context}"]
= Creating a secret using the web console

[role="_abstract"]
You can secure sensitive information, such as passwords or tokens, in a secret and add the information to a workload by using the web console. By using secrets, you can manage application credentials and configuration files without including them in your container images.

.Procedure

. Navigate to *Workloads* -> *Secrets*.
. Click *Create* -> *From YAML*.
.. Edit the YAML manually to your specifications, or drag and drop a file into the YAML editor.
For example:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: example
  namespace: <namespace>
type: Opaque
data:
  username: <base64 encoded username>
  password: <base64 encoded password>
stringData:
  hostname: myapp.mydomain.com
----
where:

`type`:: Specifies an opaque secret. However, you may see other secret types such as service account token secret, basic authentication secret, SSH authentication secret, or a secret that uses Docker configuration.
`stringData`:: Specifies the value associated with keys in the `data` map. The value associated with keys in the `stringData` map is made up of
plain text strings. Entries in the `stringData` map are converted to base64 and the entry will then be moved to the `data` map automatically. This field is write-only; the value will only be returned via the `data` field.

. Click *Create*.
. Click *Add Secret to workload*.
.. From the drop-down menu, select the workload to add.
.. Click *Save*.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-updating_{context}"]
= Understanding how to update secrets

[role="_abstract"]
To update the values in a secret, you must re-create the pods that use that secret. Because running pods do not automatically detect changes to secret data, restarting the pods ensures they consume the updated configuration.

Updating a secret follows the same workflow as deploying a new container image. You can use the `kubectl rolling-update` command.

The `resourceVersion` value in a secret is not specified when it is referenced. Therefore, if a secret is updated at the same time as pods are starting, the version of the secret that is used for the pod is not defined.

[NOTE]
====
Currently, it is not possible to check the resource version of a secret object that was used when a pod was created. It is planned that pods will report this information, so that a controller could restart ones using an old `resourceVersion`. In the interim, do not update the data of existing secrets, but create new ones with distinct names.
====

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-application-secrets-creating-using-sa_{context}"]
= Creating and using secrets

[role="_abstract"]
As an administrator, you can create a service account token secret, which you can distribute to applications that must authenticate to the API.

.Procedure

. Create a service account in your namespace by running the following command:
+
[source,terminal]
----
$ oc create sa <service_account_name> -n <your_namespace>
----

. Save the following YAML example to a file named `service-account-token-secret.yaml`. The example includes a `Secret` object configuration that you can use to generate a service account token:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <secret_name>
  annotations:
    kubernetes.io/service-account.name: "sa-name"
type: kubernetes.io/service-account-token
----
where:

`metadata.name`:: Specifies a name for your service token secret.
`metadata.annotations`:: Specifies an existing service account name. If you are creating both the `ServiceAccount` and the `Secret` objects, create the `ServiceAccount` object first.
`type`:: Specifies a service account token secret type.

. Generate the service account token by applying the file:
+
[source,terminal]
----
$ oc apply -f service-account-token-secret.yaml
----

. Get the service account token from the secret by running the following command:
+
[source,terminal]
-----
$ oc get secret <sa_token_secret> -o jsonpath='{.data.token}' | base64 --decode
-----
+
.Example output
[source,terminal]
----
ayJhbGciOiJSUzI1NiIsImtpZCI6IklOb2dtck1qZ3hCSWpoNnh5YnZhSE9QMkk3YnRZMVZoclFfQTZfRFp1YlUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImJ1aWxkZXItdG9rZW4tdHZrbnIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiYnVpbGRlciIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjNmZGU2MGZmLTA1NGYtNDkyZi04YzhjLTNlZjE0NDk3MmFmNyIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmJ1aWxkZXIifQ.OmqFTDuMHC_lYvvEUrjr1x453hlEEHYcxS9VKSzmRkP1SiVZWPNPkTWlfNRp6bIUZD3U6aN3N7dMSN0eI5hu36xPgpKTdvuckKLTCnelMx6cxOdAbrcw1mCmOClNscwjS1KO1kzMtYnnq8rXHiMJELsNlhnRyyIXRTtNBsy4t64T3283s3SLsancyx0gy0ujx-Ch3uKAKdZi5iT-I8jnnQ-ds5THDs2h65RJhgglQEmSxpHrLGZFmyHAQI-_SjvmHZPXEc482x3SkaQHNLqpmrpJorNqh1M8ZHKzlujhZgVooMvJmWPXTb2vnvi3DGn2XI-hZxl1yD2yGH1RBpYUHA
----
+
Replace `<sa_token_secret>` with the name of your service token secret.

. Use your service account token to authenticate with the API of your cluster:
+
[source,terminal]
----
$ curl -X GET <openshift_cluster_api> --header "Authorization: Bearer <token>" <1> <2>
----
+
Replace `<openshift_cluster_api>` with the OpenShift cluster API and replace `<token>` with the service account token that is output in the preceding command.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-certificates-about_{context}"]
= About using signed certificates with secrets

[role="_abstract"]
To secure communication to your service, you can configure OpenShift Container Platform to generate a signed
serving certificate/key pair that you can add into a secret in a project.

A _service serving certificate secret_ is intended to support complex middleware
applications that need out-of-the-box certificates. It has the same settings as
the server certificates generated by the administrator tooling for nodes and
masters.

.Service `Pod` spec configured for a service serving certificates secret.

[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: registry
  annotations:
    service.beta.openshift.io/serving-cert-secret-name: registry-cert
# ...
----

Replace `registry-cert` with a name for the certificate

Other pods can trust cluster-created certificates (which are only signed for
internal DNS names), by using the CA bundle in the
*_/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt_* file that is
automatically mounted in their pod.

The signature algorithm for this feature is `x509.SHA256WithRSA`. To manually
rotate, delete the generated secret. A new certificate is created.

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-certificates-creating_{context}"]
= Generating signed certificates for use with secrets

[role="_abstract"]
You can use a signed serving certificate/key pair with a pod by adding
the `service.beta.openshift.io/serving-cert-secret-name` annotation to the service, then add the secret to the pod.

Use the following procedure to create a _service serving certificate secret_.

.Procedure

. Edit the `Pod` spec for your service.

. Add the `service.beta.openshift.io/serving-cert-secret-name` annotation
with the name you want to use for your secret.
+
[source,yaml]
----
kind: Service
apiVersion: v1
metadata:
  name: my-service
  annotations:
      service.beta.openshift.io/serving-cert-secret-name: my-cert <1>
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
----
+
Replace `my-cert` with the name for the secret. The certificate and key are in PEM format, stored in `tls.crt` and `tls.key`
respectively.

. Create the service:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

. View the secret to make sure it was created:

.. View a list of all secrets:
+
[source,terminal]
----
$ oc get secrets
----
+
.Example output
[source,terminal]
----
NAME                     TYPE                                  DATA      AGE
my-cert                  kubernetes.io/tls                     2         9m
----
+
.. View details on your secret:
+
[source,terminal]
----
$ oc describe secret my-cert
----
+
.Example output
[source,terminal]
----
Name:         my-cert
Namespace:    openshift-console
Labels:       <none>
Annotations:  service.beta.openshift.io/expiry: 2023-03-08T23:22:40Z
              service.beta.openshift.io/originating-service-name: my-service
              service.beta.openshift.io/originating-service-uid: 640f0ec3-afc2-4380-bf31-a8c784846a11
              service.beta.openshift.io/expiry: 2023-03-08T23:22:40Z

Type:  kubernetes.io/tls

Data
====
tls.key:  1679 bytes
tls.crt:  2595 bytes
----

. Edit your `Pod` spec with that secret.
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-service-pod
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: my-container
      mountPath: "/etc/my-path"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  volumes:
  - name: my-volume
    secret:
      secretName: my-cert
      items:
      - key: username
        path: my-group/my-username
        mode: 511
----
+
When it is available, your pod will run.
The certificate will be good for the internal service DNS name,
`<service.name>.<service.namespace>.svc`.
+
The certificate/key pair is automatically replaced when it gets
close to expiration. View the expiration date in the
`service.beta.openshift.io/expiry` annotation on the secret, which is in
RFC3339 format.
+
[NOTE]
====
In most cases, the service DNS name
`<service.name>.<service.namespace>.svc` is not externally routable. The
primary use of `<service.name>.<service.namespace>.svc` is for intracluster or
intraservice communication, and with re-encrypt routes.
====

// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

[id="nodes-pods-secrets-troubleshooting_{context}"]
= Troubleshooting secrets

[role="_abstract"]
Review the following information for troubleshooting tips for working with secrets.

If a service certificate generation fails with (service's
`service.beta.openshift.io/serving-cert-generation-error` annotation
contains):

[source,terminal]
----
secret/ssl-key references serviceUID 62ad25ca-d703-11e6-9d6f-0e9c0057b608, which does not match 77b6dd80-d716-11e6-9d6f-0e9c0057b60
----

The service that generated the certificate no longer exists, or has a different
`serviceUID`. You must force certificates regeneration by removing the old
secret, and clearing the following annotations on the service
`service.beta.openshift.io/serving-cert-generation-error`,
`service.beta.openshift.io/serving-cert-generation-error-num`:

. Delete the secret:
+
[source,terminal]
----
$ oc delete secret <secret_name>
----

. Clear the annotations:
+
[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-
----
+
[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-num-
----

[NOTE]
====
The command removing annotation has a `-` after the annotation name to be
removed.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Understanding how to create secrets

* Configuring bound service account tokens using volume projection

* Understanding and creating service accounts

* Identifiers and Names in Kubernetes (Kubernetes documentation)

* Long-lived service account API tokens in OpenShift Container Platform (Red Hat Knowledgebase article)
