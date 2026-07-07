---
title: "Installing Operators for the image-based upgrade"
type: reference
domain: openshift
slug: edge-computing-4-22-cnf-image-based-upgrade-install-operators
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-image-based-upgrade-install-operators
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Installing Operators for the image-based upgrade

[id="cnf-image-based-upgrade-install-operators"]
= Installing Operators for the image-based upgrade

Prepare your clusters for the upgrade by installing the {lcao} and the {oadp-short} Operator.

To install the {oadp-short} Operator with the non-GitOps method, see "Installing the {oadp-short} Operator".

[role="_additional-resources"]
.Additional resources

* Installing the {oadp-short} Operator

* About backup and snapshot locations and their secrets

* Creating a Backup CR

* Creating a Restore CR

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-installing-lifecycle-agent-using-cli_{context}"]
= Installing the {lcao} by using the CLI

[role="_abstract"]
You can use the OpenShift CLI (`oc`) to install the {lcao}.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Create a `Namespace` object YAML file for the {lcao}:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-lifecycle-agent
  annotations:
    workload.openshift.io/allowed: management
----

.. Create the `Namespace` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <namespace_filename>.yaml
----

. Create an `OperatorGroup` object YAML file for the {lcao}:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-lifecycle-agent
  namespace: openshift-lifecycle-agent
spec:
  targetNamespaces:
  - openshift-lifecycle-agent
----

.. Create the `OperatorGroup` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <operatorgroup_filename>.yaml
----

. Create a `Subscription` CR for the {lcao}:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-lifecycle-agent-subscription
  namespace: openshift-lifecycle-agent
spec:
  channel: "stable"
  name: lifecycle-agent
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

.. Create the `Subscription` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <subscription_filename>.yaml
----

.Verification

. To verify that the installation succeeded, inspect the CSV resource by running the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-lifecycle-agent
----
+
Example output:
[source,terminal,subs="attributes+"]
----
NAME                              DISPLAY                     VERSION               REPLACES                           PHASE
lifecycle-agent.v.0           Openshift Lifecycle Agent   .0                Succeeded
----

. Verify that the {lcao} is up and running by running the following command:
+
[source,terminal]
----
$ oc get deploy -n openshift-lifecycle-agent
----

+
Example output:
[source,terminal]
----
NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
lifecycle-agent-controller-manager   1/1     1            1           14s
----

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="cnf-image-based-upgrade-installing-lifecycle-agent-using-web-console_{context}"]
= Installing the {lcao} by using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to install the {lcao}.

.Prerequisites

* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Search for the *{lcao}* from the list of available Operators, and then click *Install*.
. On the *Install Operator* page, under *A specific namespace on the cluster* select *openshift-lifecycle-agent*.
. Click *Install*.

.Verification

. To confirm that the installation is successful:

.. Click *Ecosystem* -> *Installed Operators*.
.. Ensure that the {lcao} is listed in the *openshift-lifecycle-agent* project with a *Status* of *InstallSucceeded*.
+
[NOTE]
====
During installation an Operator might display a *Failed* status. If the installation later succeeds with an *InstallSucceeded* message, you can ignore the *Failed* message.
====

If the Operator is not installed successfully:

. Click *Ecosystem* -> *Installed Operators*, and inspect the *Operator Subscriptions* and *Install Plans* tabs for any failure or errors under *Status*.
. Click *Workloads* -> *Pods*, and check the logs for pods in the *openshift-lifecycle-agent* project.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="ztp-image-based-upgrade-installing-lcao-with-gitops_{context}"]
= Installing the {lcao} with {ztp}

[role="_abstract"]
Install the {lcao} with {ztp-first} to do an image-based upgrade.

.Procedure

. Extract the following CRs from the `ztp-site-generate` container image and push them to the `source-cr` directory:
+
--
Example `LcaSubscriptionNS.yaml` file:

[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-lifecycle-agent
  annotations:
    workload.openshift.io/allowed: management
    ran.openshift.io/ztp-deploy-wave: "2"
  labels:
    kubernetes.io/metadata.name: openshift-lifecycle-agent
----

Example `LcaSubscriptionOperGroup.yaml` file:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: lifecycle-agent-operatorgroup
  namespace: openshift-lifecycle-agent
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  targetNamespaces:
    - openshift-lifecycle-agent
----

Example `LcaSubscription.yaml` file:

[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: lifecycle-agent
  namespace: openshift-lifecycle-agent
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  channel: "stable"
  name: lifecycle-agent
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
----

Example directory structure:

[source,terminal]
----
├── kustomization.yaml
├── sno
│   ├── example-cnf.yaml
│   ├── common-ranGen.yaml
│   ├── group-du-sno-ranGen.yaml
│   ├── group-du-sno-validator-ranGen.yaml
│   └── ns.yaml
├── source-crs
│   ├── LcaSubscriptionNS.yaml
│   ├── LcaSubscriptionOperGroup.yaml
│   ├── LcaSubscription.yaml
----
--

. Add the CRs to your common PolicyGenerator:
+
[source,yaml]
----
apiVersion: policy.open-cluster-management.io/v1
kind: PolicyGenerator
metadata:
  name: common-latest
placementBindingDefaults:
  name: common-placement-binding
policyDefaults:
  namespace: ztp-common
  placement:
    labelSelector:
      common: "true"
      du-profile: "latest"
  remediationAction: inform
  severity: low
  namespaceSelector:
    exclude:
      - kube-*
    include:
      - '*'
  evaluationInterval:
    compliant: 10m
    noncompliant: 10s
policies:
- name: common-latest-subscriptions-policy
  policyAnnotations:
    ran.openshift.io/ztp-deploy-wave: "2"
  manifests:
    - path: source-crs/LcaSubscriptionNS.yaml
    - path: source-crs/LcaSubscriptionOperGroup.yaml
    - path: source-crs/LcaSubscription.yaml
[...]
----

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-preparing-for-image-based-upgrade.adoc

[id="ztp-image-based-upgrade-installing-oadp_{context}"]
= Installing and configuring the {oadp-short} Operator with {ztp}

[role="_abstract"]
Install and configure the {oadp-short} Operator with {ztp} before starting the upgrade.

.Procedure

. Extract the following CRs from the `ztp-site-generate` container image and push them to the `source-cr` directory:
+
--
Example `OadpSubscriptionNS.yaml` file:

[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
  labels:
    kubernetes.io/metadata.name: openshift-adp
----

Example `OadpSubscriptionOperGroup.yaml` file:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: redhat-oadp-operator
  namespace: openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  targetNamespaces:
  - openshift-adp
----

Example `OadpSubscription.yaml` file:

[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: redhat-oadp-operator
  namespace: openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  channel: stable-1.4
  name: redhat-oadp-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
status:
  state: AtLatestKnown
----

Example `OadpOperatorStatus.yaml` file:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: Operator
metadata:
  name: redhat-oadp-operator.openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
status:
  components:
    refs:
    - kind: Subscription
      namespace: openshift-adp
      conditions:
      - type: CatalogSourcesUnhealthy
        status: "False"
    - kind: InstallPlan
      namespace: openshift-adp
      conditions:
      - type: Installed
        status: "True"
    - kind: ClusterServiceVersion
      namespace: openshift-adp
      conditions:
      - type: Succeeded
        status: "True"
        reason: InstallSucceeded
----

Example directory structure:

[source,terminal]
----
├── kustomization.yaml
├── sno
│   ├── example-cnf.yaml
│   ├── common-ranGen.yaml
│   ├── group-du-sno-ranGen.yaml
│   ├── group-du-sno-validator-ranGen.yaml
│   └── ns.yaml
├── source-crs
│   ├── OadpSubscriptionNS.yaml
│   ├── OadpSubscriptionOperGroup.yaml
│   ├── OadpSubscription.yaml
│   ├── OadpOperatorStatus.yaml
----
--

. Add the CRs to your common `PolicyGenTemplate`:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1
kind: PolicyGenTemplate
metadata:
  name: "example-common-latest"
  namespace: "ztp-common"
spec:
  bindingRules:
    common: "true"
    du-profile: "latest"
  sourceFiles:
    - fileName: OadpSubscriptionNS.yaml
      policyName: "subscriptions-policy"
    - fileName: OadpSubscriptionOperGroup.yaml
      policyName: "subscriptions-policy"
    - fileName: OadpSubscription.yaml
      policyName: "subscriptions-policy"
    - fileName: OadpOperatorStatus.yaml
      policyName: "subscriptions-policy"
[...]
----

. Create the `DataProtectionApplication` CR and the S3 secret only for the target cluster:

.. Extract the following CRs from the `ztp-site-generate` container image and push them to the `source-cr` directory:
+
--
Example `OadpDataProtectionApplication.yaml` file:

[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dataprotectionapplication
  namespace: openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "100"
spec:
  configuration:
    restic:
      enable: false
    velero:
      defaultPlugins:
        - aws
        - openshift
      resourceTimeout: 10m
  backupLocations:
    - velero:
        config:
          profile: "default"
          region: minio
          s3Url: $url
          insecureSkipTLSVerify: "true"
          s3ForcePathStyle: "true"
        provider: aws
        default: true
        credential:
          key: cloud
          name: cloud-credentials
        objectStorage:
          bucket: $bucketName
          prefix: $prefixName
status:
  conditions:
  - reason: Complete
    status: "True"
    type: Reconciled
----

* `spec.configuration.restic.enable` must be set to `false` for an image-based upgrade because persistent volume contents are retained and reused after the upgrade.
* `bucket` defines the bucket name created in S3 backend. `prefix` defines the name of the subdirectory that will be automatically created in the bucket. The combination of bucket and prefix must be unique for each target cluster to avoid interference between them. To ensure a unique storage directory for each target cluster, you can use the {rh-rhacm-title} hub template function, for example, `prefix: {{hub .ManagedClusterName hub}}`.

Example `OadpSecret.yaml` file:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: cloud-credentials
  namespace: openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "100"
type: Opaque
----

Example `OadpBackupStorageLocationStatus.yaml` file:

[source,yaml]
----
apiVersion: velero.io/v1
kind: BackupStorageLocation
metadata:
  name: dataprotectionapplication-1
  namespace: openshift-adp
  annotations:
    ran.openshift.io/ztp-deploy-wave: "100"
status:
  phase: Available
----

The `name` value in the `BackupStorageLocation` resource must follow a specific naming convention that aligns with the corresponding `DataProtectionApplication` resource.

* The name must use the `<DataProtectionApplication.metadata.name>-<index>` pattern.
* The `<index>` represents the position of the corresponding entry in the `spec.backupLocations` field in the `DataProtectionApplication` resource. The position starts at `1`.
* If you change the `metadata.name` value of the `DataProtectionApplication` resource in the `OadpDataProtectionApplication.yaml` file, you must also update the `metadata.name` field in the `BackupStorageLocation` resource to match the new value.

The `OadpBackupStorageLocationStatus.yaml` CR verifies the availability of backup storage locations created by OADP.
--

.. Add the CRs to your site `PolicyGenTemplate` with overrides:
+
[source,yaml]
----
apiVersion: ran.openshift.io/v1
kind: PolicyGenTemplate
metadata:
  name: "example-cnf"
  namespace: "ztp-site"
spec:
  bindingRules:
    sites: "example-cnf"
    du-profile: "latest"
  mcp: "master"
  sourceFiles:
    ...
    - fileName: OadpSecret.yaml
      policyName: "config-policy"
      data:
        cloud: <your_credentials>
    - fileName: OadpDataProtectionApplication.yaml
      policyName: "config-policy"
      spec:
        backupLocations:
          - velero:
              config:
                region: minio
                s3Url: <your_S3_URL>
                profile: "default"
                insecureSkipTLSVerify: "true"
                s3ForcePathStyle: "true"
              provider: aws
              default: true
              credential:
                key: cloud
                name: cloud-credentials
              objectStorage:
                bucket: <your_bucket_name>
                prefix: <cluster_name>
    - fileName: OadpBackupStorageLocationStatus.yaml
      policyName: "config-policy"
----

where:

`your_credentials`:: Specifies your credentials for your S3 storage backend.

`OadpDataProtectionApplication.yaml`:: If more than one `backupLocations` entries are defined in the `OadpDataProtectionApplication` CR, ensure that each location has a corresponding `OadpBackupStorageLocation` CR added for status tracking. Ensure that the name of each additional `OadpBackupStorageLocation` CR is overridden with the correct index as described in the example `OadpBackupStorageLocationStatus.yaml` file.

`your_S3_URL`:: Specifies the URL for your S3-compatible bucket.

`bucket` and `prefix`:: The `bucket` defines the bucket name that is created in S3 backend. The `prefix` defines the name of the subdirectory that will be automatically created in the `bucket`. The combination of `bucket` and `prefix` must be unique for each target cluster to avoid interference between them. To ensure a unique storage directory for each target cluster, you can use the {rh-rhacm-title} hub template function, for example, `prefix: {{hub .ManagedClusterName hub}}`.
