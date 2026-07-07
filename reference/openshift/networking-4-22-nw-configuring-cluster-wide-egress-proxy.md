---
title: "Configuring the cluster-wide proxy on the External DNS Operator"
type: reference
domain: openshift
slug: networking-4-22-nw-configuring-cluster-wide-egress-proxy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/nw-configuring-cluster-wide-egress-proxy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring the cluster-wide proxy on the External DNS Operator

[id="external-dns-operator-cluster-wide-proxy"]
= Configuring the cluster-wide proxy on the External DNS Operator

[role="_abstract"]
To propagate proxy settings to your deployed Operators, configure the cluster-wide proxy. The Operator Lifecycle Manager (OLM) automatically updates these Operators with the new `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables.

// Module included in the following assemblies:
//
// * networking/external_dns_operator/nw-configuring-cluster-wide-egress-proxy.adoc

[id="nw-configuring-cluster-wide-proxy_{context}"]
= Trusting the certificate authority of the cluster-wide proxy

[role="_abstract"]
You can configure the External DNS Operator to trust the certificate authority of the cluster-wide proxy.

.Procedure

. Create the config map to contain the CA bundle in the `external-dns-operator` namespace by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator create configmap trusted-ca
----

. To inject the trusted CA bundle into the config map, add the `config.openshift.io/inject-trusted-cabundle=true` label to the config map by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator label cm trusted-ca config.openshift.io/inject-trusted-cabundle=true
----

. Update the subscription of the External DNS Operator by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator patch subscription external-dns-operator --type='json' -p='[{"op": "add", "path": "/spec/config", "value":{"env":[{"name":"TRUSTED_CA_CONFIGMAP_NAME","value":"trusted-ca"}]}}]'
----

.Verification

* After deploying the External DNS Operator, verify that the trusted CA environment variable is added by running the following command. The output must show `trusted-ca` for the `external-dns-operator` deployment.
+
[source,terminal]
----
$ oc -n external-dns-operator exec deploy/external-dns-operator -c external-dns-operator -- printenv TRUSTED_CA_CONFIGMAP_NAME
----
