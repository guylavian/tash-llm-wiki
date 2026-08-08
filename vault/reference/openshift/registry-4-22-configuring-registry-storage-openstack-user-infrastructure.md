---
title: "Configuring the registry for OpenStack user-provisioned infrastructure"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-storage-openstack-user-infrastructure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-storage-openstack-user-infrastructure
version: 4.22
family: registry
documentKind: "Documentation"
---

# Configuring the registry for OpenStack user-provisioned infrastructure

[id="configuring-registry-storage-openstack-user-infrastructure"]
= Configuring the registry for OpenStack user-provisioned infrastructure

[role="_abstract"]
You can configure the registry of a cluster that runs on your own {rh-openstack-first} infrastructure.

// Module included in the following assemblies:
//
// * registry/installing-openstack- .adoc
// * registry/configuring-registry-operator.adoc
// * registry/configuring-registry-storage-openstack-user-infrastructure.adoc
[id="registry-configuring-registry-storage-swift-trust_{context}"]
= Configuring Image Registry Operator redirects

[role="_abstract"]
By disabling redirects, you can configure the Image Registry Operator to control whether clients such as OpenShift Container Platform cluster builds or external systems like developer machines are redirected to pull images directly from {rh-openstack-first} Swift storage. This configuration is optional and depends on whether the clients trust the storage's SSL/TLS certificates.

[NOTE]
====
In situations where clients to not trust the storage certificate, setting the `disableRedirect` option can be set to `true` proxies traffic through the image registry. Consequently, however, the image registry might require more resources, especially network bandwidth, to handle the increased load.

Alternatively, if clients trust the storage certificate, the registry can allow redirects. This reduces resource demand on the registry itself.

Some users might prefer to configure their clients to trust their self-signed certificate authorities (CAs) instead of disabling redirects. If you are using a self-signed CA, you must decide between trusting the custom CAs or disabling redirects.
====
// to allow the client to pull the image layers from the image registry rather than from links directly from Swift.

.Procedure

* To ensures that the image registry proxies traffic instead of relying on Swift storage, change the value of the `spec.disableRedirect` field in the `config.imageregistry` object to `true` by running the following command:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"disableRedirect":true}}'
----

// Module included in the following assemblies:
//
// * registry/configuring-registry-operator.adoc

[id="registry-operator-config-resources-secret-openstack_{context}"]
= Configuring a secret for the Image Registry Operator

[role="_abstract"]
In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap
resources, configuration is provided to the Operator by a separate secret
resource located within the `openshift-image-registry` namespace.

The `image-registry-private-configuration-user` secret provides
credentials needed for storage access and management. It overrides the default
credentials used by the Operator, if default credentials were found.

For Swift on {rh-openstack-first} storage, the secret is expected to contain the following two keys:

* `REGISTRY_STORAGE_SWIFT_USERNAME`
* `REGISTRY_STORAGE_SWIFT_PASSWORD`

.Procedure

* Create an OpenShift Container Platform secret that contains the required keys.
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_SWIFT_USERNAME=<username> --from-literal=REGISTRY_STORAGE_SWIFT_PASSWORD=<password> -n openshift-image-registry
----

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage-openstack-user-infrastructure.adoc

[id="registry-configuring-storage-openstack-user-infra_{context}"]
= Registry storage for {rh-openstack} with user-provisioned infrastructure

[role="_abstract"]
If the Registry Operator cannot create a Swift bucket, you must set up the storage medium manually and configure the settings in the registry custom resource (CR).

.Prerequisites

* A cluster on {rh-openstack-first} with user-provisioned infrastructure.
* To configure registry storage for {rh-openstack}, you need to provide Registry Operator
cloud credentials.
* For Swift on {rh-openstack} storage, the secret is expected to contain the following two keys:

** `REGISTRY_STORAGE_SWIFT_USERNAME`
** `REGISTRY_STORAGE_SWIFT_PASSWORD`

.Procedure

* Fill in the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io/cluster
----
+
.Example configuration
[source,yaml]
----
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  storage:
    swift:
      container: <container_id>
----

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage/configuring-registry-storage-openstack-user-infrastructure.adoc

[id="registry-operator-configuration-resource-overview-openstack-swift_{context}"]
= Image Registry Operator configuration parameters for {rh-openstack} Swift

[role="_abstract"]
The following parameters are available for you to configure your {rh-openstack-first} Swift
registry storage.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`authURL`
|Defines the URL for obtaining the authentication token. This value is optional.

|`authVersion`
|Specifies the Auth version of {rh-openstack}, for example, `authVersion: "3"`. This value is optional.

|`container`
|Defines the name of a Swift container for storing registry data. This value is optional.

|`domain`
|Specifies the {rh-openstack} domain name for the Identity v3 API. This value is optional.

|`domainID`
|Specifies the {rh-openstack} domain ID for the Identity v3 API. This value is optional.

|`tenant`
|Defines the {rh-openstack} tenant name to be used by the registry. This value is optional.

|`tenantID`
|Defines the {rh-openstack} tenant ID to be used by the registry. This value is optional.

|`regionName`
|Defines the {rh-openstack} region in which the container exists. This value is optional.

|===
