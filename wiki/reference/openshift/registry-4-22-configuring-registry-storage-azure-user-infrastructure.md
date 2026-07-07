---
title: "Configuring the registry for Azure user-provisioned infrastructure"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-storage-azure-user-infrastructure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-storage-azure-user-infrastructure
version: 4.22
family: registry
documentKind: "Documentation"
---

# Configuring the registry for Azure user-provisioned infrastructure

[id="configuring-registry-storage-azure-user-infrastructure"]
= Configuring the registry for Azure user-provisioned infrastructure

[role="_abstract"]
Save your container images to a durable storage location by configuring the built-in image registry to use dedicated Azure storage. This setup provides persistent scalable storage for your registry, separate from ephemeral cluster storage.

// Module included in the following assemblies:
//
// * registry/configuring_registry_storage/configuring-registry-storage-azure-user-infrastructure.adoc

[id="registry-operator-config-resources-secret-azure_{context}"]
= Configuring a secret for the Image Registry Operator

[role="_abstract"]
In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap
resources, configuration is provided to the Operator by a separate secret
resource located within the `openshift-image-registry` namespace.

The `image-registry-private-configuration-user` secret provides
credentials needed for storage access and management. It overrides the default
credentials used by the Operator, if default credentials were found.

For Azure registry storage, the secret is expected to contain one key whose value is the
contents of a credentials file provided by Azure:

* `REGISTRY_STORAGE_AZURE_ACCOUNTKEY`

.Procedure

* Create an OpenShift Container Platform secret that contains the required key.
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_AZURE_ACCOUNTKEY=<accountkey> --namespace openshift-image-registry
----

// Undefine the attribute to catch any errors at the end

// Module included in the following assemblies:
//
//* registry/configuring_registry_storage-azure.adoc

[id="registry-configuring-storage-azure-user-infra_{context}"]
= Configuring registry storage for Azure

[role="_abstract"]
During installation, your cloud credentials are sufficient to create Azure Blob
Storage, and the Registry Operator automatically configures storage.

.Prerequisites

* A cluster on Azure with user-provisioned infrastructure.
* To configure registry storage for Azure, provide Registry Operator
cloud credentials.
* For Azure storage the secret is expected to contain one key:
** `REGISTRY_STORAGE_AZURE_ACCOUNTKEY`

.Procedure

. Create an Azure storage container.

. Fill in the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:
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
    azure:
      accountName: <storage_account_name>
      container: <container_name>
----

// Module included in the following assemblies:
//
//* registry/configuring_registry_storage-azure.adoc

[id="registry-configuring-storage-azure-gov-cloud_{context}"]
= Configuring registry storage for Azure Government

[role="_abstract"]
During installation, your cloud credentials are sufficient to create Azure Blob
Storage, and the Registry Operator automatically configures storage.

.Prerequisites

* A cluster on Azure with user-provisioned infrastructure in a government region.
* To configure registry storage for Azure, provide Registry Operator
cloud credentials.
* For Azure storage, the secret is expected to contain one key:
** `REGISTRY_STORAGE_AZURE_ACCOUNTKEY`

.Procedure

. Create an Azure storage container.

. Fill in the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:
+
[source,terminal]
----
$ oc edit configs.imageregistry.operator.openshift.io/cluster
----
+
.Example configuration
[source,yaml]
----
storage:
  azure:
    accountName: <storage-account-name>
    container: <container-name>
    cloudName: AzureUSGovernmentCloud
----
+
`cloudName` is the name of the Azure cloud environment, which can be used to configure the Azure SDK with the appropriate Azure API endpoints. Defaults to `AzurePublicCloud`. You can also set `cloudName` to `AzureUSGovernmentCloud`, `AzureChinaCloud`, or `AzureGermanCloud` with sufficient credentials.
