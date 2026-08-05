---
title: "Verifying container signatures for supply chain security"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-verify-container-signatures
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-verify-container-signatures
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Verifying container signatures for supply chain security

[id="microshift-verify-container-signatures"]
= Verifying container signatures for supply chain security

[role="_abstract"]
You can enhance supply chain security by using the sigstore signing methodology.

//TP in 4.19, expected to GA 4.20

// Module included in the following assemblies:
//
// * microshift/microshift_auth_security/microshift-verify-container-signatures.adoc

[id="microshift-verify-container-signatures-sigstore-con_{context}"]
= Understanding how to use sigstore to verify container signatures

[role="_abstract"]
To verify image integrity within your {microshift-short} environment, you can configure the container runtime to use the sigstore signing methodology. This ensures a safer chain of custody by enabling the digital signing and verification of build artifacts.

* For user-specific images, you must update the configuration file to point to the appropriate public key, or disable signature verification for those image sources.

[IMPORTANT]
====
For disconnected or offline configurations, you must embed the public key contents into the operating system image.
====

// Module included in the following assemblies:
//
// * microshift/microshift_auth_security/microshift-verify-container-signatures.adoc

[id="microshift-verify-container-signatures-sigstore_{context}"]
= Verifying container signatures using sigstore

[role="_abstract"]
To secure your {microshift-short} environment against unauthorized image deployments, you can configure the container runtime to verify container signatures. By using sigstore with Red{nbsp}Hat public keys, you ensure that only authentic, signed images from trusted registries are used.

You can access Red{nbsp}Hat public keys at the following Product Signing Keys

You must use the release key 3 for verifying {microshift-short} container signatures.

.Prerequisites

* You have admin access to the {microshift-short} host.
* You installed {microshift-short}.

.Procedure

. Download the relevant public key and save it as `/etc/containers/RedHat_ReleaseKey3.pub` by running the following command:
+
[source,terminal]
----
$ sudo curl -sL https://access.redhat.com/security/data/63405576.txt -o /etc/containers/RedHat_ReleaseKey3.pub
----

. To configure the container runtime to verify images from Red Hat sources, edit the `/etc/containers/policy.json` file to contain the following configuration:
+
.Example policy JSON file
[source,json]
----
{
    "default": [
        {
            "type": "reject"
        }
    ],
    "transports": {
        "docker": {
            "quay.io/openshift-release-dev": [{
                "type": "sigstoreSigned",
                "keyPath": "/etc/containers/RedHat_ReleaseKey3.pub",
                "signedIdentity": {
                    "type": "matchRepoDigestOrExact"
                }
            }],
            "registry.redhat.io": [{
                "type": "sigstoreSigned",
                "keyPath": "/etc/containers/RedHat_ReleaseKey3.pub",
                "signedIdentity": {
                    "type": "matchRepoDigestOrExact"
                }
            }]
        }
    }
}
----

. Configure Red Hat remote registries to use sigstore attachments when pulling images to the local storage, by editing the `/etc/containers/registries.d/registry.redhat.io.yaml` file to contain the following configuration:
+
[source,terminal]
----
$ cat /etc/containers/registries.d/registry.redhat.io.yaml
docker:
     registry.redhat.io:
         use-sigstore-attachments: true
----

. Configure Red Hat remote registries to use sigstore attachments when pulling images to the local storage, by editing the `/etc/containers/registries.d/registry.quay.io.yaml` file to contain the following configuration:
+
[source,terminal]
----
$ cat /etc/containers/registries.d/quay.io.yaml
docker:
  quay.io/openshift-release-dev:
    use-sigstore-attachments: true
----

. Create user-specific registry configuration files if your use case requires signature verification for those image sources. You can use the example here to start with and add your own requirements.

.Next steps

. If you are using a mirror registry, enable sigstore attachments.
. Otherwise, proceed to wiping the local container storage clean.

// Module included in the following assemblies:
//
// * microshift/microshift_auth_security/microshift-verify-container-signatures.adoc

[id="microshift-enable-sigstore-mirror-registries_{context}"]
= Enabling sigstore attachments for mirror registries

[role="_abstract"]
If you are using mirror registries, you must apply additional configuration to enable sigstore attachments and mirroring by digest.

.Prerequisites

* You have admin access to the {microshift-short} host.
* You completed the steps in "Verifying container signatures using sigstore."

.Procedure

. Enable sigstore attachments by creating the `/etc/containers/registries.d/mirror.registry.local.yaml` file.
+
[source,terminal,subs="+quotes"]
----
$ cat /etc/containers/registries.d/_<mirror.registry.local.yaml>_
docker:
   mirror.registry.local:
        use-sigstore-attachments: true
----
+
Name the `_<mirror.registry.local.yaml>_` file after your mirror registry URL.

. Enable mirroring by digest by creating the `/etc/containers/registries.conf.d/999-microshift-mirror.conf` with the following contents:
+
[source,terminal]
----
$ cat /etc/containers/registries.conf.d/999-microshift-mirror.conf
[[registry]]
    prefix = "quay.io/openshift-release-dev"
    location = "mirror.registry.local"
    mirror-by-digest-only = true

[[registry]]
    prefix = "registry.redhat.io"
    location = "mirror.registry.local"
    mirror-by-digest-only = true
----

.Next steps
. Wipe the local container storage clean.

// Module included in the following assemblies:
//
// * microshift/microshift_auth_security/microshift-verify-container-signatures.adoc

[id="microshift-wiping-local-container-storage_{context}"]
= Wiping local container storage clean

[role="_abstract"]
To ensure that container images with sigstore signatures are correctly downloaded and verified, you must clear existing local storage. Removing previous container data prevents configuration conflicts when you update security policies for {microshift-short}.

.Prerequisites

* You have administrator access to the {microshift-short} host.
* You enabled sigstore on your mirror registries.

.Procedure

. Stop the CRI-O container runtime service and {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl stop crio microshift
----

. Wipe the CRI-O container runtime storage clean by running the following command:
+
[source,terminal]
----
$ sudo crio wipe --force
----

. Restart the CRI-O container runtime service and {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl start crio microshift
----

.Verification

Verify that all pods are running in a healthy state by entering the following command:
