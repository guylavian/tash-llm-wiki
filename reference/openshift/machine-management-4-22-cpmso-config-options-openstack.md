---
title: "Control plane configuration options for {rh-openstack-first}"
type: reference
domain: openshift
slug: machine-management-4-22-cpmso-config-options-openstack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/cpmso-config-options-openstack
version: 4.22
family: machine_management
documentKind: "Documentation"
---

# Control plane configuration options for {rh-openstack-first}

[id="cpmso-config-options-openstack"]
= Control plane configuration options for {rh-openstack-first}

[role="_abstract"]
You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for an {rh-openstack} cluster.

//Sample OpenStack provider specification
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-provider-spec-openstack_{context}"]
= Sample {rh-openstack} provider specification

[role="_abstract"]
You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for an {rh-openstack-first} cluster.

//True for OpenStack?
You can omit any field that has a value set in the failure domain section of the CR.

.Sample OpenStack `providerSpec` values
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
            apiVersion: machine.openshift.io/v1alpha1
            cloudName: openstack
            cloudsSecret:
              name: openstack-cloud-credentials
              namespace: openshift-machine-api
            flavor: m1.xlarge
            image: <cluster_id>-rhcos
            kind: OpenstackProviderSpec
            metadata:
              creationTimestamp: null
            networks:
            - filter: {}
              subnets:
              - filter:
                  name: <cluster_id>-nodes
                  tags: openshiftClusterID=<cluster_id>
            securityGroups:
            - filter: {}
              name: <cluster_id>-master
            serverGroupName: <cluster_id>-master
            serverMetadata:
              Name: <cluster_id>-master
              openshiftClusterID: <cluster_id>
            tags:
            - openshiftClusterID=<cluster_id>
            trunk: true
            userDataSecret:
              name: master-user-data
----
where:

`spec.template.spec.providerSpec.value.cloudsSecret.name`::
Specifies the secret name for the cluster.
Do not change this value.

`spec.template.spec.providerSpec.value.flavor`::
Specifies the {rh-openstack} flavor type for the control plane.

`spec.template.spec.providerSpec.value.kind`::
Specifies the cloud provider platform type.
Do not change this value.

`spec.template.spec.providerSpec.value.securityGroups`::
Specifies the control plane machines security group.

//Sample OpenStack failure domain configuration
// Module included in the following assemblies:
//
// * machine_management/cpmso-configuration.adoc

[id="cpmso-yaml-failure-domain-openstack_{context}"]
= Sample {rh-openstack} failure domain configuration

[role="_abstract"]
To prevent downtime for your application due to the failure of a single {rh-openstack-first} region, you can configure failure domains in the control plane machine set.
To use failure domains, you configure appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` custom resource (CR).

// TODO: Replace that link.
The control plane machine set concept of a failure domain is analogous to the existing {rh-openstack} concept of an availability zone.
The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

.Sample OpenStack failure domain values
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
        openstack:
        - availabilityZone: nova-az0
          rootVolume:
            availabilityZone: cinder-az0
        - availabilityZone: nova-az1
          rootVolume:
            availabilityZone: cinder-az1
        - availabilityZone: nova-az2
          rootVolume:
            availabilityZone: cinder-az2
        platform: OpenStack
# ...
----
where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.openstack`::
Specifies the availability zones for the failure domains.
This example demonstrates the use of more than one Nova availability zone and corresponding Cinder availability zones.
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`::
Specifies the cloud provider platform name.
Do not change this value.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources
* Updating the control plane configuration
* Configuring {rh-openstack} features for control plane machines
