---
title: "Configuring proxy support in Operator Lifecycle Manager"
type: reference
domain: openshift
slug: operators-4-22-olm-configuring-proxy-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-configuring-proxy-support
version: 4.22
family: operators
documentKind: "Documentation"
---

# Configuring proxy support in Operator Lifecycle Manager

[id="olm-configuring-proxy-support"]
= Configuring proxy support in Operator Lifecycle Manager

If a global proxy is configured on your OpenShift Container Platform cluster, Operator Lifecycle Manager (OLM) automatically configures Operators that it manages with the cluster-wide proxy. However, you can also configure installed Operators to override the global proxy or inject a custom CA certificate.

[role="_additional-resources"]
.Additional resources

// Configuring the cluster-wide proxy is a different topic in OSD/ROSA.
* Configuring the cluster-wide proxy
* Configuring a cluster-wide proxy

// This xref points to a topic that is not currently included in the OSD and ROSA docs.
* Configuring a custom PKI (custom CA certificate)

// Module included in the following assemblies:
//
// * operators/admin/olm-configuring-proxy-support.adoc

[id="olm-overriding-proxy-settings_{context}"]
= Overriding proxy settings of an Operator

If a cluster-wide egress proxy is configured, Operators running with Operator Lifecycle Manager (OLM) inherit the cluster-wide proxy settings on their deployments.
Cluster administrators
Administrators with the `dedicated-admin` role
can also override these proxy settings by configuring the subscription of an Operator.

[IMPORTANT]
====
Operators must handle setting environment variables for proxy settings in the pods for any managed Operands.
====

.Prerequisites

* Access to an OpenShift Container Platform cluster using an account with
`cluster-admin` permissions.
* Access to a OpenShift Container Platform cluster as a user with the `dedicated-admin` role.

.Procedure

. Navigate in the web console to the *Ecosystem → Software Catalog* page.

. Select the Operator and click *Install*.

. On the *Install Operator* page, modify the `Subscription` object to include one or more of the following environment variables in the `spec` section:
+
--
* `HTTP_PROXY`
* `HTTPS_PROXY`
* `NO_PROXY`
--
+
For example:
+
.`Subscription` object with proxy setting overrides
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: etcd-config-test
  namespace: openshift-operators
spec:
  config:
    env:
    - name: HTTP_PROXY
      value: test_http
    - name: HTTPS_PROXY
      value: test_https
    - name: NO_PROXY
      value: test
  channel: clusterwide-alpha
  installPlanApproval: Automatic
  name: etcd
  source: community-operators
  sourceNamespace: openshift-marketplace
  startingCSV: etcdoperator.v0.9.4-clusterwide
----
+
[NOTE]
====
These environment variables can also be unset using an empty value to remove any previously set cluster-wide or custom proxy settings.
====
+
OLM handles these environment variables as a unit; if at least one of them is set, all three are considered overridden and the cluster-wide defaults are not used for the deployments of the subscribed Operator.

. Click *Install* to make the Operator available to the selected namespaces.

. After the CSV for the Operator appears in the relevant namespace, you can verify that custom proxy environment variables are set in the deployment. For example, using the CLI:
+
[source,terminal]
----
$ oc get deployment -n openshift-operators \
    etcd-operator -o yaml \
    | grep -i "PROXY" -A 2
----
+
.Example output
[source,terminal]
----
        - name: HTTP_PROXY
          value: test_http
        - name: HTTPS_PROXY
          value: test_https
        - name: NO_PROXY
          value: test
        image: quay.io/coreos/etcd-operator@sha256:66a37fd61a06a43969854ee6d3e21088a98b93838e284a6086b13917f96b0d9c
...
----

// Module included in the following assemblies:
//
// * operators/admin/olm-configuring-proxy-support.adoc

[id="olm-inject-custom-ca_{context}"]
= Injecting a custom CA certificate

When a cluster administrator
When an administrator with the `dedicated-admin` role
adds a custom CA certificate to a cluster using a config map, the Cluster Network Operator merges the user-provided certificates and system CA certificates into a single bundle. You can inject this merged bundle into your Operator running on Operator Lifecycle Manager (OLM), which is useful if you have a man-in-the-middle HTTPS proxy.

.Prerequisites

* Access to an OpenShift Container Platform cluster using an account with
`cluster-admin` permissions.
* Access to a OpenShift Container Platform cluster as a user with the `dedicated-admin` role.
* Custom CA certificate added to the cluster using a config map.
* Desired Operator installed and running on OLM.

.Procedure

. Create an empty config map in the namespace where the subscription for your Operator exists and include the following label:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: trusted-ca <1>
  labels:
    config.openshift.io/inject-trusted-cabundle: "true" <2>
----
<1> Name of the config map.
<2> Requests the Cluster Network Operator to inject the merged bundle.
+
After creating this config map, it is immediately populated with the certificate contents of the merged bundle.

. Update the `Subscription` object to include a `spec.config` section that mounts the `trusted-ca` config map as a volume to each container within a pod that requires a custom CA:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: my-operator
spec:
  package: etcd
  channel: alpha
  config: <1>
    selector:
      matchLabels:
        <labels_for_pods> <2>
    volumes: <3>
    - name: trusted-ca
      configMap:
        name: trusted-ca
        items:
          - key: ca-bundle.crt <4>
            path: tls-ca-bundle.pem <5>
    volumeMounts: <6>
    - name: trusted-ca
      mountPath: /etc/pki/ca-trust/extracted/pem
      readOnly: true
----
<1> Add a `config` section if it does not exist.
<2> Specify labels to match pods that are owned by the Operator.
<3> Create a `trusted-ca` volume.
<4> `ca-bundle.crt` is required as the config map key.
<5> `tls-ca-bundle.pem` is required as the config map path.
<6> Create a `trusted-ca` volume mount.
+
[NOTE]
====
Deployments of an Operator can fail to validate the authority and display a `x509 certificate signed by unknown authority` error. This error can occur even after injecting a custom CA when using the subscription of an Operator. In this case, you can set the `mountPath` as `/etc/ssl/certs` for trusted-ca by using the subscription of an Operator.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Proxy certificates
* Replacing the default ingress certificate
* Updating the CA bundle
