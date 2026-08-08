---
title: "Configuring secure communication with Redis"
type: reference
domain: openshift
slug: cicd-4-22-configuring-secure-communication-with-redis
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-secure-communication-with-redis
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring secure communication with Redis

[id="configuring-secure-communication-with-redis"]
= Configuring secure communication with Redis

Using the Transport Layer Security (TLS) encryption with {gitops-title}, you can secure the communication between the Argo CD components and Redis cache and protect the possibly sensitive data in transit.

You can secure communication with Redis by using one of the following configurations:

* Enable the `autotls` setting to issue an appropriate certificate for TLS encryption.
* Manually configure the TLS encryption by creating the `argocd-operator-redis-tls` secret with a key and certificate pair.

Both configurations are possible with or without the High Availability (HA) enabled.

.Prerequisites
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* {gitops-title} Operator is installed on your cluster.

// Module is included in the following assemblies:
//
// * /cicd/gitops/configuring-secure-communication-with-redis.adoc

[id="gitops-configuring-tls-for-redis-with-autotls-enabled_{context}"]
= Configuring TLS for Redis with autotls enabled

You can configure TLS encryption for Redis by enabling the `autotls` setting on a new or already existing Argo CD instance. The configuration automatically provisions the `argocd-operator-redis-tls` secret and does not require further steps. Currently, OpenShift Container Platform is the only supported secret provider.

[NOTE]
====
By default, the `autotls` setting is disabled.
====

.Procedure

. Log in to the OpenShift Container Platform web console.

. Create an Argo CD instance with `autotls` enabled:

.. In the *Administrator* perspective of the web console, use the left navigation panel to go to *Administration* -> *CustomResourceDefinitions*.

.. Search for `argocds.argoproj.io` and click `ArgoCD` custom resource definition (CRD).

.. On the *CustomResourceDefinition details* page, click the *Instances* tab, and then click *Create ArgoCD*.

.. Edit or replace the YAML similar to the following example:
+
.Example Argo CD CR with autotls enabled
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: argocd <1>
  namespace: openshift-gitops <2>
spec:
  redis:
    autotls: openshift <3>
  ha:
    enabled: true <4>
----
<1> The name of the Argo CD instance.
<2> The namespace where you want to run the Argo CD instance.
<3> The flag that enables the `autotls` setting and creates a TLS certificate for Redis.
<4> The flag value that enables the HA feature. If you do not want to enable HA, do not include this line or set the flag value as `false`.
+
[TIP]
====
Alternatively, you can enable the `autotls` setting on an already existing Argo CD instance by running the following command:

[source,terminal]
----
$ oc patch argocds.argoproj.io <instance-name> --type=merge -p '{"spec":{"redis":{"autotls":"openshift"}}}'
----
====

.. Click *Create*.

.. Verify that the Argo CD pods are ready and running:
+
[source,terminal]
----
$ oc get pods -n <namespace> <1>
----
<1> Specify a namespace where the Argo CD instance is running, for example `openshift-gitops`.
+
.Example output with HA disabled
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS   AGE
argocd-application-controller-0       1/1     Running   0          26s
argocd-redis-84b77d4f58-vp6zm         1/1     Running   0          37s
argocd-repo-server-5b959b57f4-znxjq   1/1     Running   0          37s
argocd-server-6b8787d686-wv9zh        1/1     Running   0          37s
----
+
[NOTE]
====
The HA-enabled TLS configuration requires a cluster with at least three worker nodes. It can take a few minutes for the output to appear if you have enabled the Argo CD instances with HA configuration.
====
+
.Example output with HA enabled
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
argocd-application-controller-0            1/1     Running   0          10m
argocd-redis-ha-haproxy-669757fdb7-5xg8h   1/1     Running   0          10m
argocd-redis-ha-server-0                   2/2     Running   0          9m9s
argocd-redis-ha-server-1                   2/2     Running   0          98s
argocd-redis-ha-server-2                   2/2     Running   0          53s
argocd-repo-server-576499d46d-8hgbh        1/1     Running   0          10m
argocd-server-9486f88b7-dk2ks              1/1     Running   0          10m
----

. Verify that the `argocd-operator-redis-tls` secret is created:
+
[source,terminal]
----
$ oc get secrets argocd-operator-redis-tls -n <namespace> <1>
----
<1> Specify a namespace where the Argo CD instance is running, for example `openshift-gitops`.
+
.Example output
[source,terminal]
----
NAME                        TYPE                DATA   AGE
argocd-operator-redis-tls   kubernetes.io/tls   2      30s
----
+
The secret must be of the `kubernetes.io/tls` type and a size of `2`.

// Module is included in the following assemblies:
//
// * /cicd/gitops/configuring-secure-communication-with-redis.adoc

[id="gitops-configuring-tls-for-redis-with-autotls-disabled_{context}"]
= Configuring TLS for Redis with autotls disabled

You can manually configure TLS encryption for Redis by creating the `argocd-operator-redis-tls` secret with a key and certificate pair. In addition, you must annotate the secret to indicate that it belongs to the appropriate Argo CD instance. The steps to create a certificate and secret vary for instances with High Availability (HA) enabled.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Create an Argo CD instance:

.. In the *Administrator* perspective of the web console, use the left navigation panel to go to *Administration* -> *CustomResourceDefinitions*.

.. Search for `argocds.argoproj.io` and click `ArgoCD` custom resource definition (CRD).

.. On the *CustomResourceDefinition details* page, click the *Instances* tab, and then click *Create ArgoCD*.

.. Edit or replace the YAML similar to the following example:
+
.Example ArgoCD CR with autotls disabled
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: argocd <1>
  namespace: openshift-gitops <2>
spec:
  ha:
    enabled: true <3>
----
<1> The name of the Argo CD instance.
<2> The namespace where you want to run the Argo CD instance.
<3> The flag value that enables the HA feature. If you do not want to enable HA, do not include this line or set the flag value as `false`.

.. Click *Create*.

.. Verify that the Argo CD pods are ready and running:
+
[source,terminal]
----
$ oc get pods -n <namespace> <1>
----
<1> Specify a namespace where the Argo CD instance is running, for example `openshift-gitops`.
+
.Example output with HA disabled
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS   AGE
argocd-application-controller-0       1/1     Running   0          26s
argocd-redis-84b77d4f58-vp6zm         1/1     Running   0          37s
argocd-repo-server-5b959b57f4-znxjq   1/1     Running   0          37s
argocd-server-6b8787d686-wv9zh        1/1     Running   0          37s
----
+
[NOTE]
====
The HA-enabled TLS configuration requires a cluster with at least three worker nodes. It can take a few minutes for the output to appear if you have enabled the Argo CD instances with HA configuration.
====
+
.Example output with HA enabled
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
argocd-application-controller-0            1/1     Running   0          10m
argocd-redis-ha-haproxy-669757fdb7-5xg8h   1/1     Running   0          10m
argocd-redis-ha-server-0                   2/2     Running   0          9m9s
argocd-redis-ha-server-1                   2/2     Running   0          98s
argocd-redis-ha-server-2                   2/2     Running   0          53s
argocd-repo-server-576499d46d-8hgbh        1/1     Running   0          10m
argocd-server-9486f88b7-dk2ks              1/1     Running   0          10m
----

. Create a self-signed certificate for the Redis server by using one of the following options depending on your HA configuration:

* For the Argo CD instance with HA disabled, run the following command:
+
[source,terminal]
----
$ openssl req -new -x509 -sha256 \
  -subj "/C=XX/ST=XX/O=Testing/CN=redis" \
  -reqexts SAN -extensions SAN \
  -config <(printf "\n[SAN]\nsubjectAltName=DNS:argocd-redis.<namespace>.svc.cluster.local\n[req]\ndistinguished_name=req") \ <1>
  -keyout /tmp/redis.key \
  -out /tmp/redis.crt \
  -newkey rsa:4096 \
  -nodes \
  -sha256 \
  -days 10
----
<1> Specify a namespace where the Argo CD instance is running, for example `openshift-gitops`.
+
.Example output
[source,terminal]
----
Generating a RSA private key
...............++++
............................++++
writing new private key to '/tmp/redis.key'
----

* For the Argo CD instance with HA enabled, run the following command:
+
[source,terminal]
----
$ openssl req -new -x509 -sha256 \
  -subj "/C=XX/ST=XX/O=Testing/CN=redis" \
  -reqexts SAN -extensions SAN \
  -config <(printf "\n[SAN]\nsubjectAltName=DNS:argocd-redis-ha-haproxy.<namespace>.svc.cluster.local\n[req]\ndistinguished_name=req") \ <1>
  -keyout /tmp/redis-ha.key \
  -out /tmp/redis-ha.crt \
  -newkey rsa:4096 \
  -nodes \
  -sha256 \
  -days 10
----
<1> Specify a namespace where the Argo CD instance is running, for example `openshift-gitops`.
+
.Example output
[source,terminal]
----
Generating a RSA private key
...............++++
............................++++
writing new private key to '/tmp/redis-ha.key'
----

. Verify that the generated certificate and key are available in the `/tmp` directory by running the following commands:
+
[source,terminal]
----
$ cd /tmp
----
+
[source,terminal]
----
$ ls
----
+
.Example output with HA disabled
[source,terminal]
----
...
redis.crt
redis.key
...
----
+
.Example output with HA enabled
[source,terminal]
----
...
redis-ha.crt
redis-ha.key
...
----

. Create the `argocd-operator-redis-tls` secret by using one of the following options depending on your HA configuration:

* For the Argo CD instance with HA disabled, run the following command:
+
[source,terminal]
----
$ oc create secret tls argocd-operator-redis-tls --key=/tmp/redis.key --cert=/tmp/redis.crt
----

* For the Argo CD instance with HA enabled, run the following command:
+
[source,terminal]
----
$ oc create secret tls argocd-operator-redis-tls --key=/tmp/redis-ha.key --cert=/tmp/redis-ha.crt
----
+
.Example output
[source,terminal]
----
secret/argocd-operator-redis-tls created
----

. Annotate the secret to indicate that it belongs to the Argo CD CR:
+
[source,terminal]
----
$ oc annotate secret argocd-operator-redis-tls argocds.argoproj.io/name=<instance-name> <1>
----
<1> Specify a name of the Argo CD instance, for example `argocd`.
+
.Example output
[source,terminal]
----
secret/argocd-operator-redis-tls annotated
----

. Verify that the Argo CD pods are ready and running:
+
[source,terminal]
----
$ oc get pods -n <namespace> <1>
----
<1> Specify a namespace where the Argo CD instance is running, for example `openshift-gitops`.
+
.Example output with HA disabled
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS   AGE
argocd-application-controller-0       1/1     Running   0          26s
argocd-redis-84b77d4f58-vp6zm         1/1     Running   0          37s
argocd-repo-server-5b959b57f4-znxjq   1/1     Running   0          37s
argocd-server-6b8787d686-wv9zh        1/1     Running   0          37s
----
+
[NOTE]
====
It can take a few minutes for the output to appear if you have enabled the Argo CD instances with HA configuration.
====
+
.Example output with HA enabled
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
argocd-application-controller-0            1/1     Running   0          10m
argocd-redis-ha-haproxy-669757fdb7-5xg8h   1/1     Running   0          10m
argocd-redis-ha-server-0                   2/2     Running   0          9m9s
argocd-redis-ha-server-1                   2/2     Running   0          98s
argocd-redis-ha-server-2                   2/2     Running   0          53s
argocd-repo-server-576499d46d-8hgbh        1/1     Running   0          10m
argocd-server-9486f88b7-dk2ks              1/1     Running   0          10m
----
