---
title: "Cluster API configuration options for Amazon Web Services"
type: reference
domain: openshift
slug: machine-management-4-22-cluster-api-config-options-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cluster-api-config-options-aws
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Cluster API configuration options for Amazon Web Services

[id="cluster-api-config-options-aws"]
= Cluster API configuration options for Amazon Web Services

You can change the configuration of your {aws-first} Cluster API machines by updating values in the Cluster API custom resource manifests.

[id="cluster-api-sample-yaml-aws_{context}"]
== Sample YAML for configuring {aws-full} clusters

The following example YAML files show configurations for an {aws-full} cluster.

//Sample YAML for CAPI AWS machine template resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="capi-yaml-machine-template-aws_{context}"]
= Sample YAML for a Cluster API machine template resource on {aws-full}

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates.
The compute machine set references this template when creating machines.

[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate # <1>
metadata:
  name: <template_name> # <2>
  namespace: openshift-cluster-api
spec:
  template:
    spec: # <3>
      iamInstanceProfile: # ...
      instanceType: m5.large
      ignition:
        storageType: UnencryptedUserData
        version: "3.4"
      ami:
        id: # ...
      subnet:
        filters:
        - name: tag:Name
          values:
          - # ...
      additionalSecurityGroups:
      - filters:
        - name: tag:Name
          values:
          - # ...
----
<1> Specify the machine template kind.
This value must match the value for your platform.
<2> Specify a name for the machine template.
<3> Specify the details for your environment.
The values here are examples.

//Sample YAML for a CAPI AWS compute machine set resource
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="capi-yaml-machine-set-aws_{context}"]
= Sample YAML for a Cluster API compute machine set resource on {aws-full}

The compute machine set resource defines additional properties of the machines that it creates.
The compute machine set also references the cluster resource and machine template when creating machines.

[source,yaml]
----
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name> # <1>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name> # <2>
spec:
  clusterName: <cluster_name> # <2>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AWSMachineTemplate # <3>
        name: <template_name> # <4>
----
<1> Specify a name for the compute machine set.
The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.
<2> Specify the cluster ID as the name of the cluster.
<3> Specify the machine template kind.
This value must match the value for your platform.
<4> Specify the machine template name.

[id="cluster-api-supported-features-aws_{context}"]
== Enabling {aws-full} features with the Cluster API

You can enable the following features by updating values in the Cluster API custom resource manifests.

//Not yet supported, relies on Cluster API CAS support
// Cluster autoscaler GPU labels

[role="_additional-resources"]
.Additional resources
* Cluster autoscaler resource definition

// Elastic Fabric Adapter instances and placement group options
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-existing-placement-group_{context}"]
= Elastic Fabric Adapter instances and placement group options

You can deploy compute machines on Elastic Fabric Adapter (EFA) instances within an existing AWS placement group.

EFA instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA.
The following example uses an EFA and placement group together to demonstrate a configuration that can improve network performance for machines within the specified placement group.

.Sample EFA instance and placement group configuration
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: <supported_instance_type> # <1>
      networkInterfaceType: efa # <2>
      placementGroupName: <placement_group> # <3>
      placementGroupPartition: <placement_group_partition_number> # <4>
# ...
----
<1> Specifies an instance type that supports EFAs.
<2> Specifies the `efa` network interface type.
<3> Specifies the name of the existing AWS placement group to deploy machines in.
<4> Optional: Specifies the partition number of the existing AWS placement group where you want your machines deployed.

[NOTE]
====
Ensure that the rules and limitations for the type of placement group that you create are compatible with your intended use case.
====

The MAPI version of this has additional parameters in the providerSpec:

----
placement:
  availabilityZone: <zone> # <3>
  region: <region> # <4>
----
<3> Specifies the zone, for example, `us-east-1a`.
<4> Specifies the region, for example, `us-east-1`.

Do we need to say anything specific about this, or is this just redundant with the failure domain?

Note:
CAPI has networkInterfaceType: efa
MAPI has networkInterfaceType: EFA
Capitalization matters!

// Amazon EC2 Instance Metadata Service configuration options
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-imds-options_{context}"]
= Amazon EC2 Instance Metadata Service configuration options

You can restrict the version of the Amazon EC2 Instance Metadata Service (IMDS) that machines on {aws-first} clusters use.
Machines can require the use of IMDSv2 (AWS documentation), or allow the use of IMDSv1 in addition to IMDSv2.

This is true but does not apply to TP clusters, reassess for Cluster API GA
[NOTE]
====
To use IMDSv2 on AWS clusters that were created with OpenShift Container Platform version 4.6 or earlier, you must update your boot image.
For more information, see "Boot image management".
====

[IMPORTANT]
====
Before creating machines that require IMDSv2, ensure that any workloads that interact with the IMDS support IMDSv2.
====

.Sample IMDS configuration
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceMetadataOptions:
        httpEndpoint: enabled
        httpPutResponseHopLimit: 1 <1>
        httpTokens: optional <2>
        instanceMetadataTags: disabled
# ...
----
<1> Specifies the number of network hops allowed for IMDSv2 calls.
If no value is specified, this parameter is set to `1` by default.
<2> Specifies whether to require the use of IMDSv2.
If no value is specified, this parameter is set to `optional` by default.
The following values are valid:
`optional`:: Allow the use of both IMDSv1 and IMDSv2.
`required`:: Require IMDSv2.

[NOTE]
====
The Machine API does not support the `httpEndpoint`, `httpPutResponseHopLimit`, and `instanceMetadataTags` fields.
If you migrate a Cluster API machine template that uses this feature to a Machine API compute machine set, any Machine API machines that it creates will not have these fields and the underlying instances will not use these settings.
Any existing machines that the migrated machine set manages will retain these fields and the underlying instances will continue to use these settings.
====

Requiring the use of IMDSv2 might cause timeouts.
For more information, including mitigation strategies, see Instance metadata access considerations (AWS documentation).

//This link is for a note that does not apply to TP clusters, reassess for Cluster API GA
[role="_additional-resources"]
.Additional resources
* Boot image management

// Dedicated Instances configuration options
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-dedicated-instances_{context}"]
= Dedicated Instance configuration options

You can deploy machines that are backed by Dedicated Instances on {aws-first} clusters.

Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer.
These Amazon EC2 instances are physically isolated at the host hardware level.
The isolation of Dedicated Instances occurs even if the instances belong to different AWS accounts that are linked to a single payer account.
However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same AWS account.

OpenShift Container Platform supports instances with public or dedicated tenancy.

.Sample Dedicated Instances configuration
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: dedicated <1>
# ...
----
<1> Specifies using instances with dedicated tenancy that run on single-tenant hardware.
If you do not specify this value, instances with public tenancy that run on shared hardware are used by default.

// Dedicated Hosts configuration options
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-dedicated-hosts_{context}"]
= Place machines on Dedicated Hosts by using machine templates

[role="_abstract"]
You can configure a machine template to place machines on {aws-first} Dedicated Hosts. With dynamic host allocation, the Cluster API requests a Dedicated Host from {aws-short} and applies the specified tags to the Dedicated Host.

.Procedure

* Configure the following fields in your `AWSMachineTemplate` resource:
+
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: host
      hostAffinity: host
      dynamicHostAllocation:
        tags:
          <tag_name>: <tag_value>
# ...
----
where:

`spec.template.spec.dynamicHostAllocation.tags`:: Optional: Specifies tags to apply to the dynamically allocated Dedicated Host. If you specify tags, you must specify both a key and a value. For `<tag_name>`, specify the tag key, for example `Environment`. For `<tag_value>`, specify the tag value, for example `production`.

// Dedicated Hosts configuration options for a specific host
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-dedicated-hosts-byo-template_{context}"]
= Place machines on a specific Dedicated Host by using machine templates

[role="_abstract"]
You can configure a machine template to place machines on a specific {aws-first} Dedicated Host by specifying the host ID.

.Procedure

* Configure the following fields in your `AWSMachineTemplate` resource:
+
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: host
      hostAffinity: host
      hostID: <dedicated_host_id>
# ...
----
where:

`<dedicated_host_id>`:: Specifies the ID of the {aws-short} Dedicated Host on which to place the machine, for example `h-0123456789abcdef0`.

// Non-guaranteed Spot Instances and hourly cost limits
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc
// There are parallel features in Azure and GCP so this module is set up for reuse.

[id="machine-feature-agnostic-nonguaranteed-instances_{context}"]

You can deploy machines as non-guaranteed Spot Instances on {aws-first}.
Spot Instances use spare AWS EC2 capacity and are less expensive than On-Demand Instances.
You can use Spot Instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

[IMPORTANT]
====
AWS EC2 can reclaim the capacity for a Spot Instance at any time.
====

.Sample Spot Instance configuration
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      spotMarketOptions: <1>
        maxPrice: <price_per_hour> <2>
# ...
----
<1> Specifies the use of Spot Instances.
<2> Optional: Specifies an hourly cost limit in US dollars for the Spot Instance.
For example, setting the `<price_per_hour>` value to `2.50` limits the cost of the Spot Instance to USD 2.50 per hour.
When this value is not set, the maximum price charges up to the On-Demand Instance price.
+
[WARNING]
====
Setting a specific `maxPrice: <price_per_hour>` value might increase the frequency of interruptions compared to using the default On-Demand Instance price.
It is strongly recommended to use the default On-Demand Instance price and to not set the maximum price for Spot Instances.
====

Interruptions can occur when using Spot Instances for the following reasons:

* The instance price exceeds your maximum price
* The demand for Spot Instances increases
* The supply of Spot Instances decreases

AWS gives a two-minute warning to the user when an interruption occurs.
OpenShift Container Platform begins to remove the workloads from the affected instances when AWS issues the termination warning.

When AWS terminates an instance, a termination handler running on the Spot Instance node deletes the machine resource.
To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot Instance.

// Throughput for gp3 drives
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-throughput-capi_{context}"]
= Configuring storage throughput for gp3 drives

[role="_abstract"]
You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an {aws-short} cluster.
You can configure the storage throughput for the root volume, non root volumes, or both.

.Prerequisites

* You use gp3 storage volume(s).

.Procedure

* On the machine template in which you want to configure throughput, add the `throughput` parameter:
+
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      nonRootVolumes:
      - throughput: <throughput_value>
      rootVolume:
        throughput: <throughput_value>
# ...
----
where:

`<throughput_value>`::
Specifies a value in MiB per second between 125 and 2,000.
You can only edit this value on gp3 volumes.
The default value is `125`.

// Capacity Reservation configuration options
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc
// There are parallel features in Azure so this module is set up for reuse.

[id="machine-feature-agnostic-capacity-reservation_{context}"]
= Capacity Reservation configuration options

OpenShift Container Platform version  and later supports

You can deploy machines on any available resources that match the parameters of a capacity request that you define.
These parameters specify the
region, and number of instances that you want to reserve.
If your
can accommodate the capacity request, the deployment succeeds.

[NOTE]
====
You cannot change an existing Capacity Reservation configuration for a machine set.
To use a different Capacity Reservation group, you must replace the machine set and the machines that the previous machine set deployed.
====

.Sample Capacity Reservation configuration
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      capacityReservationId: <capacity_reservation> # <1>
      capacityReservationPreference: <reservation_preference> # <2>
      marketType: <market_type> # <3>
# ...
----
<1> Specify the ID of the
that you want to deploy machines on.
<2> Specify your preferred capacity reservation behavior.
The following values are valid:
`CapacityReservationsOnly`:: Use this option to require a matching capacity reservation.
If no matching capacity reservation is available, the instance fails to launch.
`Open`:: Use this option to allow using an open capacity reservation that matches the availability zone and instance type.
`None`:: Use this option to prohibit using a capacity reservation.
You might use this option to help keep capacity reservations available for workloads that you want to use them.
<3> Specify the market type to use.
The following values are valid:
`CapacityBlock`:: Use this market type with Capacity Blocks for ML.
`OnDemand`:: Use this market type with On-Demand Capacity Reservations.
`Spot`:: Use this market type with Spot Instances.
This option is not compatible with Capacity Reservations.

For more information, including limitations and suggested use cases for this offering, see

//Adding a GPU node to a machine set (stesmith)
// Module included in the following assemblies:
//
// * machine_management/cluster_api_machine_management/cluster_api_provider_configurations/cluster-api-config-options-aws.adoc

[id="machine-feature-aws-add-nvidia-gpu-node_{context}"]
= GPU-enabled machine options

You can deploy GPU-enabled compute machines on {aws-first}.
The following sample configuration uses an {aws-short} G4dn instance type, which includes an NVIDIA Tesla T4 Tensor Core GPU, as an example.

For more information about supported instance types, see the following pages in the NVIDIA documentation:

* NVIDIA GPU Operator Community support matrix

* NVIDIA AI Enterprise support matrix

// Cluster API machine template spec
.Sample GPU-enabled machine template configuration
[source,yaml]
----
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: g4dn.xlarge <1>
# ...
----
<1> Specifies a G4dn instance type.

// Cluster API machine set spec
.Sample GPU-enabled machine set configuration
[source,yaml]
----
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <cluster_name>-gpu-<region> <1>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region> <2>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region> <3>
        node-role.kubernetes.io/<role>: ""
# ...
----
<1> Specifies a name that includes the `gpu` role. The name includes the cluster ID as a prefix and the region as a suffix.
<2> Specifies a selector label that matches the machine set name.
<3> Specifies a template label that matches the machine set name.

// //Deploying the Node Feature Discovery Operator (stesmith)
// include::modules/nvidia-gpu-aws-deploying-the-node-feature-discovery-operator.adoc[leveloffset=+1]
