---
title: "Advanced managed cluster configuration with ClusterInstance resources"
type: reference
domain: openshift
slug: edge-computing-4-22-ztp-advanced-install-ztp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-advanced-install-ztp
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Advanced managed cluster configuration with ClusterInstance resources

[id="ztp-advanced-install-ztp"]
= Advanced managed cluster configuration with ClusterInstance resources

You can use `ClusterInstance` custom resources (CRs) to deploy custom functionality and configurations in your managed clusters at installation time.

// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-install-ztp.adoc

[id="ztp-customizing-the-install-extra-manifests_{context}"]
= Customizing extra installation manifests in the {ztp} pipeline

[role="_abstract"]
You can define a set of extra manifests for inclusion in the installation phase of the {ztp-first} pipeline. These manifests are linked to the `ClusterInstance` custom resources (CRs) and are applied to the cluster during installation. Including `MachineConfig` CRs at install time makes the installation process more efficient.

Extra manifests must be packaged in `ConfigMap` resources and referenced in the `extraManifestsRefs` field of the `ClusterInstance` CR.

.Prerequisites

* Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

.Procedure

. Create a set of extra manifest CRs that the {ztp} pipeline uses to customize the cluster installs.

. In your `/clusterinstance` directory, create a subdirectory with your extra manifests. The following example illustrates a sample folder structure:
+
[source,text]
----
clusterinstance/
├── site1-sno-du.yaml
├── extra-manifest/
│   ├── 01-example-machine-config.yaml
│   ├── enable-crun-master.yaml
│   └── enable-crun-worker.yaml
└── kustomization.yaml
----

. Create or update the `kustomization.yaml` file to use `configMapGenerator` to package your extra manifests into a `ConfigMap`:
+
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - site1-sno-du.yaml
configMapGenerator:
  - name: extra-manifests-cm
    namespace: site1-sno-du
    files:
      - extra-manifest/01-example-machine-config.yaml
      - extra-manifest/enable-crun-master.yaml
      - extra-manifest/enable-crun-worker.yaml
generatorOptions:
  disableNameSuffixHash: true
----
+
* The `configMapGenerator.namespace` value must match the `ClusterInstance` namespace.
* Setting `generatorOptions.disableNameSuffixHash` to `true` disables the hash suffix so the `ConfigMap` name is predictable.

. In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "site1-sno-du"
  namespace: "site1-sno-du"
spec:
  clusterName: "site1-sno-du"
  networkType: "OVNKubernetes"
  extraManifestsRefs:
    - name: extra-manifests-cm
  # ...
----
+
* The `extraManifestsRefs` field references the `ConfigMap` containing the extra manifests.

. Commit the `ClusterInstance` CR, extra manifest files, and `kustomization.yaml` to your Git repository and push the changes.
+
During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests.
+
[NOTE]
====
You can reference multiple `ConfigMap` resources in `extraManifestsRefs` to organize your manifests logically. For example, you might have separate `ConfigMap` resources for crun configuration, custom `MachineConfig` CRs, and other Day 0 configurations.
====

// Module included in the following assemblies:
//
// * edge_computing/ztp-advanced-install-ztp.adoc

[id="ztp-deleting-node-clusterinstance_{context}"]
= Deleting a node by using the ClusterInstance CR

[role="_abstract"]
By using a `ClusterInstance` custom resource (CR), you can delete and reprovision a node.
This method is more efficient than manually deleting the node.

.Prerequisites

* You have configured the hub cluster to generate the required installation and policy CRs.

* You have created a Git repository in which you can manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as the source repository for the Argo CD application.

.Procedure

. Update the `ClusterInstance` CR to add the `bmac.agent-install.openshift.io/remove-agent-and-node-on-delete=true` annotation to the `BareMetalHost` resource for the node, and push the changes to the Git repository:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-cluster"
  namespace: "example-cluster"
spec:
  # ...
  nodes:
    - hostName: "worker-node2.example.com"
      role: "worker"
      extraAnnotations:
        BareMetalHost:
          bmac.agent-install.openshift.io/remove-agent-and-node-on-delete: "true"
# ...
----

. Verify that the `BareMetalHost` object is annotated by running the following command:
+
[source,terminal]
----
$ oc get bmh -n <cluster_namespace> <bmh_name> -ojsonpath='{.metadata}' | jq -r '.annotations["bmac.agent-install.openshift.io/remove-agent-and-node-on-delete"]'
----
+
.Example output
[source,terminal]
----
true
----

. Delete the `BareMetalHost` CR by configuring the `pruneManifests` field in the `ClusterInstance` CR to remove the target `BareMetalHost` resource:
+
[source,yaml]
----
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-cluster"
  namespace: "example-cluster"
spec:
  # ...
  nodes:
    - hostName: "worker-node2.example.com"
      role: "worker"
      pruneManifests:
        - apiVersion: metal3.io/v1alpha1
          kind: BareMetalHost
# ...
----

. Push the changes to the Git repository and wait for deprovisioning to start.
The status of the `BareMetalHost` CR should change to `deprovisioning`. Wait for the `BareMetalHost` to finish deprovisioning, and be fully deleted.

.Verification

. Verify that the `BareMetalHost` and `Agent` CRs for the worker node have been deleted from the hub cluster by running the following commands:
+
[source,terminal]
----
$ oc get bmh -n <cluster_namespace>
----
+
[source,terminal]
----
$ oc get agent -n <cluster_namespace>
----

. Verify that the node record has been deleted from the spoke cluster by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
[NOTE]
====
If you are working with secrets, deleting a secret too early can cause an issue because ArgoCD needs the secret to complete resynchronization after deletion.
Delete the secret only after the node cleanup, when the current ArgoCD synchronization is complete.
====

. After the `BareMetalHost` object is successfully deleted, remove the worker node definition from the `spec.nodes` section in the `ClusterInstance` CR and push the changes to the Git repository.

.Next steps

To reprovision a node, add the node definition back to the `spec.nodes` section in the `ClusterInstance` CR, push the changes to the Git repository, and wait for the synchronization to complete.
This regenerates the `BareMetalHost` CR of the worker node and triggers the re-install of the node.
