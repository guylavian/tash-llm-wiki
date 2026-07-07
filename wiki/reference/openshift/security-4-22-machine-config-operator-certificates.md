---
title: "Machine Config Operator certificates"
type: reference
domain: openshift
slug: security-4-22-machine-config-operator-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/machine-config-operator-certificates
version: 4.22
family: security
documentKind: "Documentation"
---

# Machine Config Operator certificates

[id="cert-types-machine-config-operator-certificates"]
= Machine Config Operator certificates

== Purpose

This certificate authority is used to secure connections from nodes to Machine Config Server (MCS) during initial provisioning.

There are two certificates:

. A self-signed CA, the `machine-config-server-ca` config map (MCS CA)
. A derived certificate, the `machine-config-server-tls` secret (MCS cert)

[id="cert-types-machine-config-operator-certificates-details"]
=== Provisioning details

OpenShift Container Platform installations that use {op-system-first} are installed by using Ignition. This process is split into two parts:

. An Ignition config is created that references a URL for the full configuration served by the MCS.
. For user-provisioned infrastucture installation methods, the Ignition config manifests as a `worker.ign` file created by the `openshift-install` command. For installer-provisioned infrastructure installation methods that use the Machine API Operator, this configuration appears as the `worker-user-data` secret.

[role="_additional-resources"]
.Additional resources

* Machine Config Operator

* About the OVN-Kubernetes network plugin

[id="cert-types-machine-config-operator-certificates-trust"]
=== Provisioning chain of trust

The MCS CA is injected into the Ignition configuration under the `security.tls.certificateAuthorities` configuration field. The MCS then provides the complete configuration using the MCS cert presented by the web server.

The client validates that the MCS cert presented by the server has a chain of trust to an authority it recognizes. In this case, the MCS CA is that authority, and it signs the MCS cert. This ensures that the client is accessing the correct server. The client in this case is Ignition running on a machine in the initramfs.

[id="cert-types-machine-config-operator-certificates-materials"]
=== Key material inside a cluster

The following objects are stored in the `openshift-machine-config-operator` namespace:

* The MCS CA bundle is stored as the `machine-config-server-ca` config map. The MCS CA bundle stores all valid CAs for the `MachineConfigServer` TLS certificate.
* The MCS CA signing key is stored as the `machine-config-server-ca` secret. The MCS CA signing key is used to sign the `MachineConfigServer` TLS certificate.
* The MCS cert is stored as the `machine-config-server-tls` secret, which contains the `MachineConfigServer` TLS certificate and key.

The `machine-config-server-ca` config map is used in the following ways:

* The certificate controller updates the `*-user-data` secrets in the `openshift-machine-api` namespace any time the `machine-config-server-ca` configmap is updated.
* The Machine Config Operator renders the `master-user-data-managed` and `worker-user-data-managed` secrets from the `machine-config-server-ca` configmap.

[id="cert-types-machine-config-operator-certificates-mgmt"]
== Management

At this time, directly modifying either of these certificates is not supported.

[id="cert-types-machine-config-operator-certificates-exp"]
== Expiration
The MCS CA and MCS cert are valid for 10 years and are automatically rotated by the MCO at 8 years.

The issued serving certificates are valid for 10 years.

[NOTE]
====
This automatic certificate rotation applies only to clusters that use machine sets. For clusters that do not use machine sets, such as vSphere user-provisioned infrastructure clusters, you are required to manually rotate these certificates. For more information on manual certificate rotation, see the Red{nbsp}Hat Knowledgebase article Regenerating CA certificates for the Machine Config Server.
====

[id="cert-types-machine-config-operator-certificates-custom"]
== Customization

You cannot customize the Machine Config Operator certificates.
