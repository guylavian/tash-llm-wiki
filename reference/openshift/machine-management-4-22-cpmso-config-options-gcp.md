---
title: "Control plane configuration options for {gcp-full}"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-config-options-gcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-config-options-gcp
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Control plane configuration options for {gcp-full}

[id="cpmso-config-options-gcp"]
= Control plane configuration options for {gcp-full}

[role="_abstract"]
You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for a {gcp-short} cluster.

//Sample GCP provider specification
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-provider-spec-gcp_{context}"]
= Sample {gcp-short} provider specification

[role="_abstract"]
You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for an {gcp-first} cluster.

You can omit any field that has a value set in the failure domain section of the CR.

In the following example, you can obtain some of the values for your cluster by using the {oc-first}.

Infrastructure ID:: The `<cluster_id>` string is the infrastructure ID.
The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning.
If you have `oc` installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----

Image path:: The `<path_to_image>` string is the path to the source image for the disk.
If you have `oc` installed, you can obtain the path to the image by running the following command:
+
[source,terminal]
----
$ oc -n openshift-machine-api \
  -o jsonpath='{.spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.disks[0].image}{"\n"}' \
  get ControlPlaneMachineSet/cluster
----

.Sample {gcp-short} `providerSpec` values
[source,yaml]
----
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            apiVersion: machine.openshift.io/v1beta1
            canIPForward: false
            credentialsSecret:
              name: gcp-cloud-credentials
            deletionProtection: false
            disks:
            - autoDelete: true
              boot: true
              image: <path_to_image>
              labels: null
              sizeGb: 200
              type: pd-ssd
            kind: GCPMachineProviderSpec
            machineType: e2-standard-4
            metadata:
              creationTimestamp: null
            metadataServiceOptions: {}
            networkInterfaces:
            - network: <cluster_id>-network
              subnetwork: <cluster_id>-master-subnet
            projectID: <project_name>
            region: <region>
            serviceAccounts:
            - email: <cluster_id>-m@<project_name>.iam.gserviceaccount.com
              scopes:
              - https://www.googleapis.com/auth/cloud-platform
            shieldedInstanceConfig: {}
            tags:
            - <cluster_id>-master
            targetPools:
            - <cluster_id>-api
            userDataSecret:
              name: master-user-data
            zone: ""
----
where:

`spec.template.spec.providerSpec.value.credentialsSecret.name`::
Specifies the secret name for the cluster.
Do not change this value.

`spec.template.spec.providerSpec.value.disk.image`::
Specifies the path to the source image for the disk.
+
To use a {gcp-short} Marketplace image, specify the offer to use:
+
--
* OpenShift Container Platform: `\https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-ocp-413-x86-64-202305021736`
* {opp}: `\https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-opp-413-x86-64-202305021736`
* {oke}: `\https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-oke-413-x86-64-202305021736`
--

`spec.template.spec.providerSpec.value.kind`::
Specifies the cloud provider platform type.
Do not change this value.

`spec.template.spec.providerSpec.value.projectID`::
Specifies the name of the {gcp-short} project that you use for your cluster.

`spec.template.spec.providerSpec.value.projectID.region`::
Specifies the {gcp-short} region for the cluster.

`spec.template.spec.providerSpec.value.serviceAccounts`::
Specifies a single service account.
Specifying more than one service account is not supported.

`spec.template.spec.providerSpec.value.userDataSecret`::
Specifies the control plane user data secret.
Do not change this value.

`spec.template.spec.providerSpec.value.zone`::
This parameter is in the failure domain configuration and has an empty value here.
+
--
--

//Sample GCP failure domain configuration
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-failure-domain-gcp_{context}"]
= Sample {gcp-short} failure domain configuration

[role="_abstract"]
To prevent downtime for your application due to the failure of a single {gcp-first} region, you can configure failure domains in the control plane machine set.
To use failure domains, you configure appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` custom resource (CR).

The control plane machine set concept of a failure domain is analogous to the existing {gcp-short} concept of a _zone_.
The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

When configuring {gcp-short} failure domains in the control plane machine set, you must specify the zone name to use.

.Sample {gcp-short} failure domain values
[source,yaml]
----
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        gcp:
        - zone: <gcp_zone_a>
        - zone: <gcp_zone_b>
        - zone: <gcp_zone_c>
        - zone: <gcp_zone_d>
        platform: GCP
# ...
----
where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.gcp.zone`::
Each instance of `zone` specifies a {gcp-short} zone for a failure domain.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`::
Specifies the cloud provider platform name.
Do not change this value.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Configuring {gcp-full} features for control plane machines
