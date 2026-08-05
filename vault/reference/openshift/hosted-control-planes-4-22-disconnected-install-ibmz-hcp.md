---
title: "Deploying {hcp} on {ibm-z-title} in a disconnected environment"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-disconnected-install-ibmz-hcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/disconnected-install-ibmz-hcp
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Deploying {hcp} on {ibm-z-title} in a disconnected environment

[id="disconnected-install-ibmz-hcp"]
= Deploying {hcp} on {ibm-z-title} in a disconnected environment

[role="_abstract"]
{hcp-capital} deployments in disconnected environments function differently than in a standalone OpenShift Container Platform.

{hcp-capital} involves two distinct environments:

* Control plane: Located in the management cluster, where the {hcp} pods are run and managed by the Control Plane Operator.
* Data plane: Located in the workers of the hosted cluster, where the workload and a few other pods run, managed by the Hosted Cluster Config Operator.

The `ImageContentSourcePolicy` (ICSP) custom resource for the data plane is managed through the `ImageContentSources` API in the hosted cluster manifest.

For the control plane, ICSP objects are managed in the management cluster. These objects are parsed by the HyperShift Operator and are shared as `registry-overrides` entries with the Control Plane Operator. These entries are injected into any one of the available  deployments in the {hcp} namespace as an argument.

To work with disconnected registries in the {hcp}, you must first create the appropriate ICSP in the management cluster. Then, to deploy disconnected workloads in the data plane, you need to add the entries that you want into the `ImageContentSources` field in the hosted cluster manifest.

[id="hcp-ibm-z-dc-prereqs_{context}"]
= Prerequisites to deploy {hcp} on {ibm-z-title} in a disconnected environment

[role="_abstract"]
To deploy {hcp} on {ibm-z-title} in a disconnected environment, you must meet a few prerequisites.

You need the following resources:

* A mirror registry. For more information, see "Mirror registry for Red{nbsp}Hat OpenShift introduction".
* A mirrored image for a disconnected installation. For more information, see "Mirroring images for a disconnected installation using the oc-mirror plugin".

[role="_additional-resources"]
.Additional resources
* Mirror registry for Red{nbsp}Hat OpenShift introduction
* Mirroring images for a disconnected installation by using the oc-mirror plugin v2

[id="hcp-ibm-z-adding-credentials-registry_{context}"]
= Adding credentials and the registry certificate authority to the management cluster

[role="_abstract"]
To pull the mirror registry images from the management cluster, you must first add credentials and the certificate authority of the mirror registry to the management cluster.

.Procedure

. Create a `ConfigMap` with the certificate of the mirror registry by running the following command:
+
[source,terminal]
----
$ oc apply -f registry-config.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: registry-config
  namespace: openshift-config
data:
  <mirror_registry>: |
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
#...
----

. Patch the `image.config.openshift.io` cluster-wide object to include the following entries:
+
[source,yaml]
----
spec:
  additionalTrustedCA:
    - name: registry-config
----

. Update the management cluster pull secret to add the credentials of the mirror registry.

.. Fetch the pull secret from the cluster in a JSON format by running the following command:
+
[source,terminal]
----
$ oc get secret/pull-secret -n openshift-config -o json \
  | jq -r '.data.".dockerconfigjson"' \
  | base64 -d > authfile
----

.. Edit the fetched secret JSON file to include a section with the credentials of the certificate authority:
+
[source,terminal]
----
  "auths": {
    "<mirror_registry>": {
      "auth": "<credentials>",
      "email": "you@example.com"
    }
  },
----
+
* `<mirror_registry>` specifies the name of the mirror registry.
* `<credentials>` specifies the credentials for the mirror registry to allow fetch of images.

.. Update the pull secret on the cluster by running the following command:
+
[source,terminal]
----
$ oc set data secret/pull-secret -n openshift-config \
  --from-file=.dockerconfigjson=authfile
----

[id="hcp-ibm-z-update-registry-ca_{context}"]
= Update the registry certificate authority in the AgentServiceConfig resource with the mirror registry

[role="_abstract"]
When you use a mirror registry for images, agents need to trust the registry's certificate to securely pull images. You can add the certificate authority of the mirror registry to the `AgentServiceConfig` custom resource by creating a `ConfigMap`.

.Prerequisites

* You must have installed {mce}.

.Procedure

. In the same namespace where you installed {mce-short}, create a `ConfigMap` resource with the mirror registry details. This `ConfigMap` resource ensures that you grant the hosted cluster workers the capability to retrieve images from the mirror registry.
+
.Example ConfigMap file
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: mirror-config
  namespace: multicluster-engine
  labels:
    app: assisted-service
data:
  ca-bundle.crt: |
    -----BEGIN CERTIFICATE-----
    -----END CERTIFICATE-----
  registries.conf: |

    [[registry]]
      location = "registry.stage.redhat.io"
      insecure = false
      blocked = false
      mirror-by-digest-only = true
      prefix = ""

      [[registry.mirror]]
        location = "<mirror_registry>"
        insecure = false

    [[registry]]
      location = "registry.redhat.io/multicluster-engine"
      insecure = false
      blocked = false
      mirror-by-digest-only = true
      prefix = ""

      [[registry.mirror]]
        location = "<mirror_registry>/multicluster-engine"
        insecure = false
----
+
Replace `<mirror_registry>` with the name of the mirror registry.

. Patch the `AgentServiceConfig` resource to include the `ConfigMap` resource that you created. If the `AgentServiceConfig` resource is not present, create the `AgentServiceConfig` resource with the following content embedded into it:
+
[source,terminal]
----
spec:
  mirrorRegistryRef:
    name: mirror-config
----

[id="hcp-ibm-z-adding-registry-ca-hostedcluster_{context}"]
= Adding the registry certificate authority to the hosted cluster

[role="_abstract"]
When you are deploying {hcp} on {ibm-z-title} in a disconnected environment, include the `additional-trust-bundle` and `image-content-sources` resources. The hosted cluster uses those resources to inject the certificate authority into the data plane compute nodes so that the images are pulled from the registry.

.Procedure

. Create the `icsp.yaml` file with the `image-content-sources` information.
+
The `image-content-sources` information is available in the `ImageContentSourcePolicy` YAML file that is generated after you mirror the images by using `oc-mirror`.
+
.Example ImageContentSourcePolicy file
[source,terminal]
----
# cat icsp.yaml
- mirrors:
  - <mirror_registry>/openshift/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
- mirrors:
  - <mirror_registry>/openshift/release-images
  source: quay.io/openshift-release-dev/ocp-release
----

. Create a hosted cluster and provide the `additional-trust-bundle` certificate to update the compute nodes with the certificates as in the following example:
+
[source,terminal]
----
$ hcp create cluster agent \
    --name=my-hosted-cluster \
    --pull-secret=/user/name/pullsecret \
    --agent-namespace=clusters-hosted \
    --base-domain=example.com \
    --api-server-address=api.my-hosted-cluster.example.com \
    --etcd-storage-class=lvm-storageclass \
    --ssh-key ~/.ssh/id_rsa.pub \
    --namespace <hosted_cluster_namespace> \
    --control-plane-availability-policy SingleReplica \
    --release-image=quay.io/openshift-release-dev/ocp-release:4.22.0-multi \
    --additional-trust-bundle <path for cert> \
    --image-content-sources icsp.yaml
----
+
* `--name` specifies the name of your hosted cluster.
* `--pull-secret` specifies the path to your pull secret.
* `--agent-namespace` specifies the name of the hosted control plane namespace.
* `--base-domain` specifies the name of your base domain.
* `--etcd-storage-class` specifies the etcd storage class name.
* `--ssh-key` specifies the path to your SSH public key. The default file path is `~/.ssh/id_rsa.pub`.
* `--namespace` specifies the name of the hosted cluster namespace.
* `--release-image` specifies the supported OpenShift Container Platform version that you want to use.
* `--additional-trust-bundle` specifies the path to the Certificate Authority of the mirror registry.
