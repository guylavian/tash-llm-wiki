---
title: "Certificate maintenance"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-troubleshooting-cert-maintenance
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/troubleshooting-cert-maintenance
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Certificate maintenance

[id="troubleshooting-cert-maintenance"]
= Certificate maintenance

Certificate maintenance is required for continuous cluster authentication.
As a cluster administrator, you must manually renew certain certificates, while others are automatically renewed by the cluster.

Learn about certificates in OpenShift Container Platform and how to maintain them by using the following resources:

* Which OpenShift certificates do rotate automatically and which do not in Openshift 4.x?
* Checking etcd certificate expiry in OpenShift 4

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-manual_{context}"]
= Certificates manually managed by the administrator

[role="_abstract"]
The following certificates must be renewed by a cluster administrator:

* Proxy certificates
* User-provisioned certificates for the API server
// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-manual-proxy_{context}"]
= Managing proxy certificates

[role="_abstract"]
Proxy certificates allow users to specify one or more custom certificate authority (CA) certificates that are used by platform components when making egress connections.

[NOTE]
====
Certain CAs set expiration dates and you might need to renew these certificates every two years.
====

If you did not originally set the requested certificates, you can determine the certificate expiration in several ways.
Most Cloud-native Network Functions (CNFs) use certificates that are not specifically designed for browser-based connectivity.
Therefore, you need to pull the certificate from the `ConfigMap` object of your deployment.

.Procedure

* To get the expiration date, run the following command against the certificate file:
+
[source,terminal]
----
$ openssl x509 -enddate -noout -in <cert_file_name>.pem
----
+
For more information about determining how and when to renew your proxy certificates, see "Proxy certificates" in _Security and compliance_.

[role="_additional-resources"]
.Additional resources

* Proxy certificates

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-manual-user-provisioned_{context}"]
= User-provisioned API server certificates

[role="_abstract"]
The API server is accessible by clients that are external to the cluster at `api.<cluster_name>.<base_domain>`.
You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients.
You must set a custom default certificate to be used by the API server when serving content.

For more information, see "User-provided certificates for the API server" in _Security and compliance_

[role="_additional-resources"]
.Additional resources

* User-provisioned certificates for the API server

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-auto_{context}"]
= Certificates managed by the cluster

[role="_abstract"]
You only need to check cluster-managed certificates if you detect an issue in the logs.
The following certificates are automatically managed by the cluster:

* Service CA certificates
* Node certificates
* Bootstrap certificates
* etcd certificates
* OLM certificates
* Machine Config Operator certificates
* Monitoring and cluster logging Operator component certificates
* Control plane certificates
* Ingress certificates

[role="_additional-resources"]
.Additional resources

* Service CA certificates
* Node certificates
* Bootstrap certificates
* etcd certificates
* OLM certificates
* Machine Config Operator certificates
* Monitoring and cluster logging Operator component certificates
* Control plane certificates
* Ingress certificates

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-auto-etcd_{context}"]
= Certificates managed by etcd

[role="_abstract"]
The etcd certificates are used for encrypted communication between etcd member peers as well as encrypted client traffic.
The certificates are renewed automatically within the cluster provided that communication between all nodes and all services is current.
Therefore, if your cluster might lose communication between components during a specific period of time, which is close to the end of the etcd certificate lifetime, it is recommended to renew the certificate in advance.
For example, communication can be lost during an upgrade due to nodes rebooting at different times.

* You can manually renew etcd certificates by running the following command:
+
[source,terminal]
----
$ for each in $(oc get secret -n openshift-etcd | grep "kubernetes.io/tls" | grep -e \
"etcd-peer\|etcd-serving" | awk '{print $1}'); do oc get secret $each -n openshift-etcd -o \
jsonpath="{.data.tls\.crt}" | base64 -d | openssl x509 -noout -enddate; done
----

For more information about updating etcd certificates, see Checking etcd certificate expiry in OpenShift 4.
For more information about etcd certificates, see "etcd certificates" in _Security and compliance_.

[role="_additional-resources"]
.Additional resources

* etcd certificates

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-auto-node_{context}"]
= Node certificates

[role="_abstract"]
Node certificates are self-signed certificates, which means that they are signed by the cluster and they originate from an internal certificate authority (CA) that is generated by the bootstrap process.

After the cluster is installed, the cluster automatically renews the node certificates.

For more information, see "Node certificates" in _Security and compliance_.

[role="_additional-resources"]
.Additional resources

* Node certificates

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-cert-maintenance.adoc

[id="troubleshooting-certs-auto-service-ca_{context}"]
= Service CA certificates

[role="_abstract"]
The `service-ca` is an Operator that creates a self-signed certificate authority (CA) when an OpenShift Container Platform cluster is deployed.
This allows user to add certificates to their deployments without manually creating them.
Service CA certificates are self-signed certificates.

For more information, see "Service CA certificates" in _Security and compliance_.

[role="_additional-resources"]
.Additional resources

* Service CA certificates
