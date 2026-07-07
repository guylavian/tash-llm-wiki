---
title: "Configuring {KMS}"
type: reference
domain: openshift
slug: etcd-4-22-kms-configuring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/kms-configuring
version: 4.22
family: etcd
documentKind: "Documentation"
---

# Configuring {KMS}

[id="kms-configuring"]
= Configuring {KMS}

[role="_abstract"]
You can configure external KMS encryption for etcd to centralize key management and meet regulatory compliance requirements.

// Enabling KMS encryption
// Module included in the following assemblies:
//
// * etcd/KMS_v2/kms-configuring.adoc

[id="kms-configuring_{context}"]
= Enable KMS encryption

[role="_abstract"]
You can enable external Key Management Service (KMS) encryption for etcd data to centralize key management and meet compliance requirements.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have enabled the `TechPreviewNoUpgrade` feature set to enable the `KMSEncryption` feature gate.
* You have a `HashiCorp Vault Enterprise` instance accessible from your control plane nodes. Vault Community Edition is not available.
* Your control plane nodes have network access to the Vault server.
* You have configured your Vault instance with:
** Transit secrets engine enabled at the default `transit/` mount path
** Encryption key created with type `aes256-gcm96` (recommended for FIPS 140-3 compliance)
** Vault policy allowing the {KMS} plugin to encrypt, decrypt, and read key information
** Authentication method (token, `AppRole`, or `userpass`) configured with the policy attached

The {KMS} plugin requires a Vault policy with the following capabilities:

[source,hcl]
----
path "transit/encrypt/kms-key" {
  capabilities = ["update"]
}

path "transit/decrypt/kms-key" {
  capabilities = ["update"]
}

path "transit/keys/kms-key" {
  capabilities = ["read"]
}

path "auth/token/lookup-self" {
  capabilities = ["read"]
}
----
Replace `kms-key` with your Vault Transit key name if using a different name.

[IMPORTANT]
====
Create an etcd backup before enabling KMS encryption.
====

.Procedure

. Deploy the KMS plugin on each control plane host as a static pod:
+
--
* Configure the plugin to listen at `unix:///var/run/kmsplugin/kms.sock`
* For your static pod, mount `/var/run/kmsplugin` as `hostPath`
* Configure KMS provider connection details and authentication credentials

The following steps show how to deploy the `HashiCorp` Vault KMS plugin as a static pod.
--

. Create a static pod manifest file:
+
[source,terminal]
----
$ cat > /tmp/vault-kms-plugin.yaml <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: vault-kms-plugin
  namespace: kube-system
  labels:
    app: vault-kms-plugin
    tier: control-plane
spec:
  priorityClassName: system-node-critical
  hostNetwork: true
  containers:
  - name: vault-kms-plugin
    image: quay.io/redhat-isv-containers/698df066f8d1ddf179c15ef9:<version>
    command:
    - /vault-kubernetes-kms
    - -vault-address=<https://vault.example.com:8200>
    - -<vault_namespace>=admin
    - -auth-method=userpass
    - -userpass-username=<vault_username>
    - -userpass-password=<vault_password>
    - -transit-mount=transit
    - -transit-key=kms-key
    - -socket=unix:///var/run/kmsplugin/kms.sock
    volumeMounts:
    - name: kmsplugin
      mountPath: /var/run/kmsplugin
    resources:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 500m
        memory: 512Mi
    securityContext:
      privileged: true
  volumes:
  - name: kmsplugin
    hostPath:
      path: /var/run/kmsplugin
      type: DirectoryOrCreate
EOF
----
+
Replace the following values to match your environment:
+
<version>:: The Vault KMS plugin image version tag. Use `0.1.0-beta-ubi`.
<vault_username>:: Your Vault username for authentication.
<vault_password>:: Your Vault password for authentication.
<https://vault.example.com:8200>:: The Vault address. Update this field to match your Vault server URL.
<vault_namespace>:: Optional field.
+
The manifest uses the Red Hat certified container image from Quay.io (`quay.io/redhat-isv-containers/698df066f8d1ddf179c15ef9`), which is the recommended image for OpenShift Container Platform.
+
[NOTE]
====
Alternatively, you can use the HashiCorp image from Docker Hub by replacing the image field with `docker.io/hashicorp/vault-kube-kms:0.1.0-beta-ubi`.
====

. Deploy the static pod manifest to each control plane node by running the following commands:
+
[source,terminal]
----
$ MANIFEST=$(cat /tmp/vault-kms-plugin.yaml | base64)
$ for node in $(oc get nodes --selector=node-role.kubernetes.io/master -o name | cut -d/ -f2); do
    echo "Deploying to $node..."
    oc debug node/$node -- chroot /host bash -c \
      "echo '$MANIFEST' | base64 -d > /etc/kubernetes/manifests/vault-kms-plugin.yaml"
  done
----
+
The kubelet automatically detects and starts static pods from `/etc/kubernetes/manifests/`.

. Verify the static pods are running by entering the following command:
+
[source,terminal]
----
$ oc get pods -n kube-system -o wide | grep vault-kms
----
+
.Example output
[source,terminal]
----
vault-kms-plugin-ip-10-0-16-7.compute.internal    1/1  Running  0  2m  10.0.16.7
vault-kms-plugin-ip-10-0-32-93.compute.internal   1/1  Running  0  2m  10.0.32.93
vault-kms-plugin-ip-10-0-69-106.compute.internal  1/1  Running  0  2m  10.0.69.106
----
+
Static pod names include the node name as a suffix. You should see one pod per control plane node.

. Verify the socket exists on a control plane node by entering the following command:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host ls -la /var/run/kmsplugin/kms.sock
----
+
.Example output
[source,terminal]
----
srwxr-xr-x. 1 root root 0 <timestamp> /var/run/kmsplugin/kms.sock
----
+
[NOTE]
====
Static pods are managed by kubelet on each node and cannot be deleted with `oc delete pod`. To remove a static pod, delete the manifest file from `/etc/kubernetes/manifests/` on each control plane node.
====

. Edit the `APIServer` custom resource by entering the following command:
+
[source,terminal]
----
$ oc edit apiserver cluster
----

. Add the KMS configuration to the `spec.encryption` section:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  encryption:
    type: KMS
----

. Save and exit.
+
Migration begins automatically. The `kube-apiserver`, `openshift-apiserver` and `oauth-apiserver` Operators will restart and roll out new revisions.
+
[NOTE]
====
The `openshift-apiserver` and `authentication` operators typically complete migration in 5-10 minutes. The `kube-apiserver` operator uses a conservative rollout strategy, updating one control plane node at a time and waiting for health checks before proceeding to the next node. This process can take 30 minutes or longer depending on cluster load.
====

.Verification

. Verify the encryption type by entering the following command:
+
[source,terminal]
----
$ oc get apiserver cluster -o jsonpath='{.spec.encryption.type}'
----
+
Output should show `KMS`.

. Monitor the `kube-apiserver` rollout progress by entering the following command:
+
[source,terminal]
----
$ oc get kubeapiserver cluster -o jsonpath='{.status.nodeStatuses}' | jq -r '.[] | "\(.nodeName | split(".")[0]): current=\(.currentRevision) target=\(.targetRevision)"'
----
+
.Example output during rollout
[source,terminal]
----
ip-10-0-16-166: current=10 target=0
ip-10-0-32-93: current=9 target=10
ip-10-0-69-106: current=9 target=0
----
+
The operator rolls out one node at a time. When all nodes show the same `current` revision and `target` is `0`, the rollout is complete.

. Check the encryption migration status by entering the following command:
+
[source,terminal]
----
$ oc get kubeapiserver cluster -o jsonpath='{.status.conditions[?(@.type=="Encrypted")]}' | jq .
----
+
.Example output when complete
[source,terminal]
----
{
  "lastTransitionTime": "2026-05-15T17:39:02Z",
  "message": "All resources encrypted: secrets, configmaps",
  "reason": "EncryptionCompleted",
  "status": "True",
  "type": "Encrypted"
}
----
+
Wait for `reason` to show `EncryptionCompleted` before proceeding to verify encryption in etcd.

. Verify secrets are encrypted in etcd:
+
[WARNING]
====
Wait for the `kube-apiserver` rollout to complete on all control plane nodes before verifying encryption. During the rollout, API requests are distributed across nodes, and secrets created while some nodes are still on an earlier revision will not be encrypted with {KMS}.
====
+
--
.. Create a test secret by entering the following command:
+
[source,terminal]
----
$ oc create secret generic test-secret --from-literal=key=value -n default
----

.. Get an etcd pod name by entering the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-etcd -l app=etcd -o name | head -1
----

.. Check the secret data in etcd by entering the following command:
+
[source,terminal]
----
$ oc exec -n openshift-etcd <etcd_pod_name> -- etcdctl get /kubernetes.io/secrets/default/test-secret --print-value-only | hexdump -C | head -1
----
+
Output should begin with `k8s:enc:kms:v2:` followed by encrypted binary data.

.. Delete the test secret by entering the following command:
+
[source,terminal]
----
$ oc delete secret test-secret -n default
----
--

[role="_additional-resources"]
.Additional resources

* Vault Transit Secrets Engine
* Vault API: Create Key
* Vault Policies
* Vault Authentication Methods

// Rotating the encryption key
// Module included in the following assemblies:
//
// * etcd/KMS_v2/kms-configuring.adoc

[id="kms-rotating-encryption-key_{context}"]
= Rotate the Vault encryption key

[role="_abstract"]
You can rotate your Vault Transit encryption key to generate a new key version while maintaining access to data encrypted with earlier versions.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to your Vault instance with permissions to rotate keys.
* {KMS} encryption is enabled and functioning.

.Procedure

. Rotate the Vault encryption key by entering the following command:
+
[source,terminal]
----
$ vault write -f transit/keys/kms-key/rotate
----
+
Vault creates a new key version while maintaining earlier versions for decryption. The API server automatically uses the correct key version for each secret.

. Verify the new key version by entering the following command:
+
[source,terminal]
----
$ vault read transit/keys/kms-key
----
+
The `latest_version` field shows the current key version number.

.Verification

* Verify that existing secrets remain accessible by entering the following command:
+
[source,terminal]
----
$ oc get secret -A
----

All secrets should be readable without errors.

[NOTE]
====
Existing encrypted secrets do not need re-encryption. Vault maintains all key versions and automatically uses the appropriate version for decryption.
====

[role="_additional-resources"]
.Additional resources

* Vault Transit: Rotate Key
* Vault Transit: Rewrap Data
* Vault Transit: Key Rotation

// Migrating from local encryption to KMS encryption
// Module included in the following assemblies:
//
// * etcd/KMS_v2/kms-configuring.adoc

[id="kms-migrating-from-local-encryption_{context}"]
= Migrate from local encryption to KMS encryption

[role="_abstract"]
You can migrate from local etcd encryption to external KMS encryption to centralize key management and improve compliance.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have enabled the `TechPreviewNoUpgrade` feature set to enable the `KMSEncryption` feature gate.
* Your cluster is currently using `aescbc` or `aesgcm` encryption.
* You have deployed the KMS plugin on all control plane nodes.
* Control plane nodes have network access to the KMS provider.

[IMPORTANT]
====
Create an etcd backup before migrating.
====

.Procedure

. Back up the current etcd encryption configuration by entering the following command:
+
[source,terminal]
----
$ oc get apiserver cluster -o yaml > apiserver-backup.yaml
----

. Edit the APIServer custom resource by entering the following command:
+
[source,terminal]
----
$ oc edit apiserver cluster
----

. Change the encryption type from `aescbc` or `aesgcm` to `KMS`:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  encryption:
    type: KMS
----

. Save and exit.
+
Migration starts automatically and typically takes several minutes.

. Verify migration completion for all API servers by running the following commands:
+
[source,terminal]
----
$ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{end}'
----
+
[source,terminal]
----
$ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{end}'
----
+
[source,terminal]
----
$ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{end}'
----
+
All outputs should show `EncryptionCompleted`.

// Monitoring KMS encryption status
// Module included in the following assemblies:
//
// * etcd/KMS_v2/kms-configuring.adoc

[id="kms-monitoring-status_{context}"]
= Monitor KMS encryption status

[role="_abstract"]
You can monitor KMS encryption status by using Operator and API server logs to verify successful configuration and detect issues.

.Procedure

. Check the kube-apiserver operator logs for KMS-related events by entering the following command:
+
[source,terminal]
----
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i kms
----

. View API server logs for KMS-related events by entering the following command:
+
[source,terminal]
----
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=100 | grep -i kms
----

. Verify the KMS encryption configuration by entering the following command:
+
[source,terminal]
----
$ oc get apiserver cluster -o jsonpath='{.spec.encryption}' | jq
----

[role="_additional-resources"]
.Additional resources

* Kubernetes KMS provider documentation

// Troubleshooting KMS encryption
// Module included in the following assemblies:
//
// * etcd/KMS_v2/kms-configuring.adoc

[id="kms-troubleshooting_{context}"]
= KMS encryption troubleshooting

[role="_abstract"]
You can diagnose and resolve common KMS encryption issues to maintain secure key management and cluster availability.

[id="kms-invalid-configuration_{context}"]
== Invalid KMS configuration

*Symptom:* APIServer resource shows validation errors during KMS encryption configuration.

*Diagnosis:* Check kube-apiserver Operator logs:
[source,terminal]
----
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i "kms\|validation\|error"
----

*Solutions:*

* Verify plugin configuration follows provider requirements
* Ensure all required fields are specified
* Verify plugin is running on all control plane nodes:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host ls -la /var/run/kmsplugin/kms.sock
----

[id="kms-permissions-errors_{context}"]
== KMS permissions errors

*Symptom:* Encryption migration fails with permission errors.

*Diagnosis:* Check Operator and plugin logs:
[source,terminal]
----
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i "kms\|permission\|access denied"
----

[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host journalctl -u kms-plugin
----

*Solutions:*

* Verify plugin has valid authentication credentials
* Check if credentials have expired
* Ensure plugin principal has encrypt and decrypt permissions
* Verify KMS provider key policy allows plugin access
* Confirm encryption key is enabled and not scheduled for deletion

[id="kms-expired-deleted-key_{context}"]
== Expired or deleted KMS key

*Symptom:* API server cannot decrypt secrets when accessing encrypted resources.

*Diagnosis:* Check logs and verify key status:
[source,terminal]
----
$ oc logs -n openshift-kube-apiserver -l apiserver=true | grep -i "decrypt\|kms.*error"
----

[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host journalctl -u kms-plugin | grep -i "key\|error"
----

*Solutions:*

* Re-enable the encryption key if disabled
* Restore from backup if key was permanently deleted
* Cancel key deletion if scheduled
* Ensure KMS provider maintains access to previous key versions

[WARNING]
====
Deleted KMS keys prevent data recovery. Align key retention with backup policies.
====

[id="kms-api-server-degraded_{context}"]
== API server degraded or unavailable

*Symptom:* API server becomes degraded or unresponsive after enabling KMS encryption.

*Diagnosis:* Check Operator status and logs:
[source,terminal]
----
$ oc get clusteroperator kube-apiserver
----

[source,terminal]
----
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=200 | grep -i kms
----

*Solutions:*

* Check network connectivity between control plane and KMS provider
* Verify network policies, firewalls, and routes allow communication
* Monitor KMS provider rate limits and request increases if needed
* Verify DNS resolution and TLS certificate validation
* Confirm plugin is running on all control plane nodes:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host systemctl status kms-plugin
----

[id="kms-migration-stuck-slow_{context}"]
== Encryption migration stuck or slow

*Symptom:* KMS encryption migration takes unusually long or becomes stuck.

*Diagnosis:* Check Operator status and migration logs:
[source,terminal]
----
$ oc get clusteroperator kube-apiserver
----

[source,terminal]
----
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i migration
----

*Solutions:*

* Migration time depends on data size; monitor progress
* Monitor KMS provider audit logs for rate limiting or throttling events
* Check network performance between control plane and KMS provider

[id="kms-collecting-debug-info_{context}"]
== Collecting debug information

Collect cluster logs:

[source,terminal]
----
$ oc adm must-gather
----

[source,terminal]
----
$ oc get apiserver cluster -o yaml > apiserver.yaml
----

[source,terminal]
----
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator > kube-apiserver-operator.log
----

[source,terminal]
----
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=500 > kube-apiserver.log
----

Collect KMS provider information:

* KMS plugin logs from control plane nodes
* KMS provider audit logs
* KMS provider key policy and permissions
* Authentication credentials status
* Network connectivity test results

[NOTE]
====
Redact credentials, tokens, and sensitive data before sharing logs.
====

[role="_additional-resources"]
[id="additional-resources_kms-configuring"]
== Additional resources

* Using a KMS provider for data encryption
* HashiCorp Vault Transit Secrets Engine
* Use Vault as a Kubernetes KMS provider
* HashiCorp Vault KMS plugin container image
