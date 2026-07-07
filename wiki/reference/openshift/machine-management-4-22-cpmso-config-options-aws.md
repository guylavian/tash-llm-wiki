---
title: "Control plane configuration options for {aws-full}"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-config-options-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-config-options-aws
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Control plane configuration options for {aws-full}

[id="cpmso-config-options-aws"]
= Control plane configuration options for {aws-full}

[role="_abstract"]
You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for an {aws-short} cluster.

//Sample AWS provider specification
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-provider-spec-aws_{context}"]
= Sample {aws-short} provider specification

[role="_abstract"]
You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for an {aws-first} cluster.

You can omit any field that has a value set in the failure domain section of the CR.

.Sample AWS `providerSpec` values
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
            ami:
              id: ami-<ami_id_string>
            apiVersion: machine.openshift.io/v1beta1
            blockDevices:
            - ebs:
                encrypted: true
                iops: 0
                kmsKey:
                  arn: ""
                volumeSize: 120
                volumeType: gp3
            credentialsSecret:
              name: aws-cloud-credentials
            deviceIndex: 0
            iamInstanceProfile:
              id: <cluster_id>-master-profile
            instanceType: m6i.xlarge
            kind: AWSMachineProviderConfig
            loadBalancers:
            - name: <cluster_id>-int
              type: network
            - name: <cluster_id>-ext
              type: network
            metadata:
              creationTimestamp: null
            metadataServiceOptions: {}
            placement:
              region: <region>
              availabilityZone: ""
              tenancy:
            securityGroups:
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-node
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-lb
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-controlplane
            subnet: {}
            userDataSecret:
              name: master-user-data
----
where:

`<ami_id_string>`::
Specifies the {op-system-first} Amazon Machine Images (AMI) ID for the cluster.
The AMI must belong to the same region as the cluster.
If you want to use an AWS Marketplace image, you must complete the OpenShift Container Platform subscription from the AWS Marketplace to obtain an AMI ID for your region.

`spec.template.spec.providerSpec.value.blockDevices.ebs`::
Specifies the configuration of an encrypted Amazon Elastic Block Store (Amazon EBS) volume.

`spec.template.spec.providerSpec.value.credentialsSecret.name`::
Specifies the secret name for the cluster.
Do not change this value.

`spec.template.spec.providerSpec.value.iamInstanceProfile`::
Specifies the AWS Identity and Access Management (IAM) instance profile.
Do not change this value.

`spec.template.spec.providerSpec.value.instanceType`::
Specifies the AWS instance type for the control plane.

`spec.template.spec.providerSpec.value.kind`::
Specifies the cloud provider platform type.
Do not change this value.

`spec.template.spec.providerSpec.value.loadBalancers`::
Specifies the internal (`int`) and external (`ext`) load balancers for the cluster.
+
[NOTE]
====
You can omit the external (`ext`) load balancer parameters on private OpenShift Container Platform clusters.
====

`spec.template.spec.providerSpec.value.placement`::
Specifies where to create the control plane instance in AWS.
The following keys in this stanza specify additional details:
+
--
`region`::
Specifies the AWS region for the cluster.
`availabilityZone`::
This parameter is in the failure domain configuration and has an empty value here.
--
+
--
--

`tenancy`::
Specifies the AWS Dedicated Instance configuration for the control plane.
For more information, see AWS documentation about Dedicated Instances.
The following values are valid:
+
--
* `default`: The Dedicated Instance runs on shared hardware.
* `dedicated`: The Dedicated Instance runs on single-tenant hardware.
* `host`: The Dedicated Instance runs on a Dedicated Host, which is an isolated server with configurations that you can control.
--

`spec.template.spec.providerSpec.value.securityGroups`::
Specifies the control plane machines security group.

`spec.template.spec.providerSpec.value.subnet`::
This parameter is in the failure domain configuration and has an empty value here.
+
--
--
+
[NOTE]
====
If the failure domain configuration does not specify a value, the control plane machines use the value in the provider specification.
====

`spec.template.spec.providerSpec.value.userDataSecret`::
Specifies the control plane user data secret. Do not change this value.

//Sample AWS failure domain configuration
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-failure-domain-aws_{context}"]
= Sample {aws-short} failure domain configuration

[role="_abstract"]
To prevent downtime for your application due to the failure of a single {aws-first} region, you can configure failure domains in the control plane machine set.
To use failure domains, you configure appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` custom resource (CR).

The control plane machine set concept of a failure domain is analogous to the {aws-short} concept of an _Availability Zone (AZ)_.
The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

When configuring {aws-short} failure domains in the control plane machine set, you must specify the availability zone name and the subnet to use.

.Sample {aws-short} failure domain values
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
        aws:
        - placement:
            availabilityZone: <aws_zone_a>
          subnet:
            filters:
            - name: tag:Name
              values:
              - <cluster_id>-subnet-private-<aws_zone_a>
            type: Filters
        - placement:
            availabilityZone: <aws_zone_b>
          subnet:
            filters:
            - name: tag:Name
              values:
              - <cluster_id>-subnet-private-<aws_zone_b>
            type: Filters
        platform: AWS
# ...
----
where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.placement.availabilityZone: <aws_zone_a>`::
Specifies an {aws-short} availability zone for the first failure domain.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet`::
Specifies a subnet configuration.
In this example, the subnet type is `Filters`, so there is a `filters` stanza.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.filters.values: <cluster_id>-subnet-private-<aws_zone_a>`::
Specifies the subnet name for the first failure domain, using the infrastructure ID and the {aws-short} availability zone.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.type`::
Specifies the subnet type.
The following values are valid: `ARN`, `Filters` and `ID`.
The default value is `Filters`.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.placement.availabilityZone: <aws_zone_b>`::
Specifies an {aws-short} availability zone for an additional failure domain.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.filters.values: <cluster_id>-subnet-private-<aws_zone_b>`::
Specifies the subnet name for the additional failure domain, using the infrastructure ID and the {aws-short} availability zone.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`::
Specifies the cloud provider platform name.
Do not change this value.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Configuring {aws-full} features for control plane machines
