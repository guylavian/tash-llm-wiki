---
title: "Updating a cluster in a disconnected environment using the OpenShift Update Service"
type: reference
domain: openshift
slug: disconnected-4-22-disconnected-update-osus
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected/disconnected-update-osus
version: 4.22
family: disconnected
documentKind: "Documentation"
---

# Updating a cluster in a disconnected environment using the OpenShift Update Service

[id="updating-disconnected-cluster-osus"]
= Updating a cluster in a disconnected environment using the OpenShift Update Service

[role="_abstract"]
You can install and configure the OpenShift Update Service (OSUS) in a disconnected environment to get an update experience similar to the connected clusters.

The following steps outline the high-level workflow about updating a cluster in a disconnected environment by using OSUS:

. Configure access to a secured registry.

. Update the global cluster pull secret to access your mirror registry.

. Install the OSUS Operator.

. Create a graph data container image for the OpenShift Update Service.

. Install the OSUS application and configure your clusters to use the OpenShift Update Service in your environment.

. Perform a supported update procedure from the documentation as you would with a connected cluster.

// Using the OpenShift Update Service in a disconnected environment
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-overview_{context}"]
= Using the OpenShift Update Service in a disconnected environment

[role="_abstract"]
The OpenShift Update Service (OSUS) provides update recommendations to OpenShift Container Platform clusters. Red{nbsp}Hat publicly hosts the OpenShift Update Service, and clusters in a connected environment can connect to the service through public APIs to retrieve update recommendations.

However, clusters in a disconnected environment cannot access these public APIs to retrieve update information. To have a similar update experience in a disconnected environment, you can install and configure the OpenShift Update Service so that it is available within the disconnected environment.

A single OSUS instance is capable of serving recommendations to thousands of clusters.
OSUS can be scaled horizontally to cater to more clusters by changing the replica value.
So for most disconnected use cases, one OSUS instance is enough.
For example, Red{nbsp}Hat hosts just one OSUS instance for the entire fleet of connected clusters.

If you want to keep update recommendations separate in different environments, you can run one OSUS instance for each environment.
For example, in a case where you have separate test and stage environments, you might not want a cluster in a stage environment to receive update recommendations to version A if that version has not been tested in the test environment yet.

The following sections describe how to install an OSUS instance and configure it to provide update recommendations to a cluster.

[role="_additional-resources"]
.Additional resources
* About the OpenShift Update Service

* Understanding update channels and releases

// Configuring access to a secured registry for the OpenShift Update Service
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="registry-configuration-for-update-service_{context}"]
= Configuring access to a secured registry for the OpenShift Update Service

[role="_abstract"]
If your release images are contained in a registry whose HTTPS X.509 certificate is signed by a custom certificate authority, you must configure additional trust stores for image registry access for the update service.

.Prerequisites
* You must have the `oc` command-line interface (CLI) tool installed.
* You must provision a container image registry in your environment with the container images for your update.

.Procedure
. Complete the steps in "Configuring additional trust stores for image registry access" along with the following changes for the update service.
+
.Image registry CA config map example for the update service
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-registry-ca
data:
  updateservice-registry: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
  registry-with-port.example.com..5000: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
----
+
where:

`data.updateservice-registry`:: Specifies the required config map key name containing the registry certificate authority (CA) certificate.
+
[NOTE]
====
If a registry has the port, such as `registry-with-port.example.com:5000`, `:` should be replaced with `..`.
====

[role="_additional-resources"]
.Additional resources
* Configuring additional trust stores for image registry access

// Updating the global cluster pull secret
// Module included in the following assemblies:
// * openshift_images/managing_images/using-image-pull-secrets.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc
// * support/remote_health_monitoring/remote-health-reporting.adoc
//
// Not included, but linked to from:
// * operators/admin/olm-managing-custom-catalogs.adoc

[id="images-update-global-pull-secret_{context}"]
= Updating the global cluster pull secret

[role="_abstract"]
To add new registries or update authentication for your OpenShift Container Platform cluster, you can update the global pull secret by appending new credentials to the _additional-pull-secret_. To do this, you can use the `oc set data secret/additional-pull-secret -n kube-system` command. Hypershift manages the new credential propagation among the HostedCluster nodes.

This feature provides a dedicated mechanism to separate your private credentials from the pull secret managed by the service, ensuring cluster functionality while restricting external visibility of your sensitive data. This separation allows you to independently rotate secrets and maintain exclusive ownership for compliance without impacting core managed service operations.

OpenShift Container Platform already has some immutable entries in the file, and you will not be able to modify those. If you are in this situation, you can follow this approach to use the same registry with different credentials.
This is a sample of authentication that is already in place:

[source,terminal]
----
"auths":
  "<quay.io: xxxxYYYzzzz>"
----
In the following case you can add a more specific entry such as:

[source,terminal]
----
"auths":
  "<quay.io/sampleNamespace": 111445656>"
----
This adds a new layer to the pull secret without affecting the original registry entry.

Use this procedure when you need a separate registry to store images than the registry used during installation.

[IMPORTANT]
====
The global pull secret is a HostedControlPlane feature only and is not an OCP standalone feature.
The global pull secret is a HostedControlPlane feature only and is not an OCP standalone feature and is also only available on OpenShift Container Platform version 4.20.6 and later.

To transfer your cluster to another owner, you must initiate the transfer in {cluster-manager-url} and then update the pull secret on the cluster. Updating a cluster's pull secret without initiating the transfer in {cluster-manager} causes the cluster to stop reporting Telemetry metrics in {cluster-manager}.

For more information, see _Transferring cluster ownership_ under _Additional resources_ in the {cluster-manager-first} documentation.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Optional: To append a new pull secret to the existing pull secret:
+
.. Download the pull secret by entering the following command:
+
[source,terminal]
----
$ oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > <pull_secret_location>
----
+
--
where:

`<pull_secret_location>`:: Specifies the path to the pull secret file.
--

.. Add the new pull secret by entering the following command:
+
[source,terminal]
----
$ oc registry login --registry="<registry>" \
--auth-basic="<username>:<password>" \
--to=<pull_secret_location>
----
+
--
where:

`<registry>`:: Specifies the new registry. You can include many repositories within the same registry, for example: `--registry="<registry/my-namespace/my-repository>`.

`<username>:<password>`:: Specifies the credentials of the new registry.

`<pull_secret_location>`:: Specifies the path to the pull secret file.
--
. Update the global pull secret for your cluster by entering the following command. Note that this update rolls out to all nodes, which can take some time depending on the size of your cluster.
+
[source,terminal]
----
$ oc set data secret/pull-secret -n openshift-config \
  --from-file=.dockerconfigjson=<pull_secret_location>
----
+
--
where:

`<pull_secret_location>`:: Specifies the path to the new pull secret file.
--
+
This merges your additional pull secret with the original HostedCluster pull secret, making it available to all nodes in the cluster.

. Optional: Modify the additional pull secret added by entering the following command:
+
[source,terminal]
----
$ oc edit secret additional-pull-secret -n kube-system
----
+
The secret must contain a valid DockerConfigJSON format.
+
.Example pull secret
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: additional-pull-secret
  namespace: kube-system
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: <base64-encoded-docker-config-json>
----
+
This results in the following states of the each pull secret:

* *Original*: immutable
* *Additional*: mutable
* *Global*: final state of both the original and additional pull secrets

. Optional: Delete the additional pull secret added by entering the following command:
+
[source,terminal]
----
$ oc delete secret additional-pull-secret -n kube-system
----
+
This triggers the automatic cleanup process across your nodes.

[role="_additional-resources"]
.Additional resources
* Transferring cluster ownership

// Installing the OpenShift Update Service Operator
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-install_{context}"]
= Installing the OpenShift Update Service Operator

[role="_abstract"]
To install the OpenShift Update Service, you must first install the OpenShift Update Service Operator by using the OpenShift Container Platform web console or CLI.

[NOTE]
====
For clusters that are installed in disconnected environments, also known as disconnected clusters, Operator Lifecycle Manager by default cannot access the Red Hat-provided software catalog sources hosted on remote registries because those remote sources require full internet connectivity. For more information, see "Using Operator Lifecycle Manager in disconnected environments".
====

// Installing the OpenShift Update Service Operator by using the web console
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-install-web-console_{context}"]
= Installing the OpenShift Update Service Operator by using the web console

[role="_abstract"]
You can use the web console to install the OpenShift Update Service Operator.

.Procedure

. In the web console, click *Ecosystem* -> *Software Catalog*.
+
[NOTE]
====
Enter `Update Service` into the *Filter by keyword...* field to find the Operator faster.
====

. Choose *OpenShift Update Service* from the list of available Operators, and click *Install*.

.. Select an *Update channel*.

.. Select a *Version*.

.. Select *A specific namespace on the cluster* under *Installation Mode*.

.. Select a namespace for *Installed Namespace* or accept the recommended namespace `openshift-update-service`.

.. Select an *Update approval* strategy:
+
** The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
** The *Manual* strategy requires a cluster administrator to approve the Operator update.

.. Click *Install*.

. Go to *Ecosystem* -> *Installed Operators* and verify that the OpenShift Update Service Operator is installed.

. Ensure that *OpenShift Update Service* is listed in the correct namespace with a *Status* of *Succeeded*.

// Installing the OpenShift Update Service Operator by using the CLI
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-install-cli_{context}"]
= Installing the OpenShift Update Service Operator by using the CLI

[role="_abstract"]
You can use the OpenShift CLI (`oc`) to install the OpenShift Update Service Operator.

.Procedure

. Create a namespace for the OpenShift Update Service Operator:

.. Create a `Namespace` object YAML file, for example, `update-service-namespace.yaml`, for the OpenShift Update Service Operator:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-update-service
  annotations:
    openshift.io/node-selector: ""
  labels:
    openshift.io/cluster-monitoring: "true"
----
+
Set the `openshift.io/cluster-monitoring` label to `"true"` to enable Operator-recommended cluster monitoring on this namespace.
.. Create the namespace:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f update-service-namespace.yaml
----

. Install the OpenShift Update Service Operator by creating the following objects:

.. Create an `OperatorGroup` object YAML file, for example, `update-service-operator-group.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: update-service-operator-group
  namespace: openshift-update-service
spec:
  targetNamespaces:
  - openshift-update-service
----

.. Create an `OperatorGroup` object:
+
[source,terminal]
----
$ oc -n openshift-update-service create -f <filename>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc -n openshift-update-service create -f update-service-operator-group.yaml
----

.. Create a `Subscription` object YAML file, for example, `update-service-subscription.yaml`:
+
.Example Subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: update-service-subscription
  namespace: openshift-update-service
spec:
  channel: v1
  installPlanApproval: "Automatic"
  source: "redhat-operators"
  sourceNamespace: "openshift-marketplace"
  name: "cincinnati-operator"
----
+
where:

`spec.source`:: Specifies the name of the catalog source that provides the Operator. For clusters that do not use a custom Operator Lifecycle Manager (OLM), specify `redhat-operators`. If your OpenShift Container Platform cluster is installed in a disconnected environment, specify the name of the `CatalogSource` object created when you configured Operator Lifecycle Manager (OLM).

.. Create the `Subscription` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc -n openshift-update-service create -f update-service-subscription.yaml
----
+
The OpenShift Update Service Operator is installed to the `openshift-update-service` namespace and targets the `openshift-update-service` namespace.

. Verify the Operator installation:
+
[source,terminal]
----
$ oc -n openshift-update-service get clusterserviceversions
----
+
.Example output
[source,terminal]
----
NAME                             DISPLAY                    VERSION   REPLACES   PHASE
update-service-operator.v4.6.0   OpenShift Update Service   4.6.0                Succeeded
...
----
+
If the OpenShift Update Service Operator is listed, the installation was successful. The version number might be different from shown.

[role="_additional-resources"]
.Additional resources
* Using Operator Lifecycle Manager in disconnected environments
* Installing Operators in your namespace

// Creating the OpenShift Update Service graph data container image
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-graph-data_{context}"]
= Creating the OpenShift Update Service graph data container image

[role="_abstract"]
The OpenShift Update Service requires a graph data container image, from which the OpenShift Update Service retrieves information about channel membership and blocked update edges. Graph data is typically fetched directly from the update graph data repository. In environments where an internet connection is unavailable, loading this information from an init container is another way to make the graph data available to the OpenShift Update Service.

The role of the init container is to provide a local copy of the graph data, and during pod initialization, the init container copies the data to a volume that is accessible by the service.

[NOTE]
====
The oc-mirror OpenShift CLI (`oc`) plugin creates this graph data container image in addition to mirroring release images. If you used the oc-mirror plugin to mirror your release images, you can skip this procedure.
====

.Procedure

. Create a Dockerfile, for example, `./Dockerfile`, containing the following:
+
[source,terminal]
----
FROM registry.access.redhat.com/ubi9/ubi:latest

RUN curl -L -o cincinnati-graph-data.tar.gz https://api.openshift.com/api/upgrades_info/graph-data

RUN mkdir -p /var/lib/cincinnati-graph-data && tar xvzf cincinnati-graph-data.tar.gz -C /var/lib/cincinnati-graph-data/ --no-overwrite-dir --no-same-owner

CMD ["/bin/bash", "-c" ,"exec cp -rp /var/lib/cincinnati-graph-data/* /var/lib/cincinnati/graph-data"]
----

. Use the docker file created in the above step to build a graph data container image, for example, `registry.example.com/openshift/graph-data:latest`:
+
[source,terminal]
----
$ podman build -f ./Dockerfile -t registry.example.com/openshift/graph-data:latest
----

. Push the graph data container image created in the previous step to a repository that is accessible to the OpenShift Update Service, for example, `registry.example.com/openshift/graph-data:latest`:
+
[source,terminal]
----
$ podman push registry.example.com/openshift/graph-data:latest
----
+
[NOTE]
====
To push a graph data image to a registry in a disconnected environment, copy the graph data container image created in the previous step to a repository that is accessible to the OpenShift Update Service. Run `oc image mirror --help` for available options.
====

// Creating an OpenShift Update Service application
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-create-service_{context}"]
= Creating an OpenShift Update Service application

[role="_abstract"]
You can create an OpenShift Update Service application by using the OpenShift Container Platform web console or CLI.

// Creating an OpenShift Update Service application by using the web console
//Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-create-service-web-console_{context}"]
= Creating an OpenShift Update Service application by using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to create an OpenShift Update Service application by using the OpenShift Update Service Operator.

.Prerequisites

* The OpenShift Update Service Operator has been installed.
* The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service.
* The current release and update target releases have been mirrored to a registry in the disconnected environment.

.Procedure

. In the web console, click *Ecosystem* -> *Installed Operators*.

. Choose *OpenShift Update Service* from the list of installed Operators.

. Click the *Update Service* tab.

. Click *Create UpdateService*.

. Enter a name in the *Name* field, for example, `service`.

. Enter the local pullspec in the *Graph Data Image* field to the graph data container image created in "Creating the OpenShift Update Service graph data container image", for example, `registry.example.com/openshift/graph-data:latest`.
//TODO: Add xref to preceding step when allowed.

. In the *Releases* field, enter the registry and repository created to contain the release images in "Mirroring the OpenShift Container Platform image repository", for example, `registry.example.com/ocp4/openshift4-release-images`.
//TODO: Add xref to preceding step when allowed.

. Enter `2` in the *Replicas* field.

. Click *Create* to create the OpenShift Update Service application.

. Verify the OpenShift Update Service application:

** From the *UpdateServices* list in the *Update Service* tab, click the Update Service application just created.

** Click the *Resources* tab.

** Verify each application resource has a status of *Created*.

// Creating an OpenShift Update Service application by using the CLI
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-create-service-cli_{context}"]
= Creating an OpenShift Update Service application by using the CLI

[role="_abstract"]
You can use the OpenShift CLI (`oc`) to create an OpenShift Update Service application.

.Prerequisites

* The OpenShift Update Service Operator has been installed.
* The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service.
* The current release and update target releases have been mirrored to a registry in the disconnected environment.

.Procedure

. Configure the OpenShift Update Service target namespace, for example, `openshift-update-service`:
+
[source,terminal]
----
$ NAMESPACE=openshift-update-service
----
+
The namespace must match the `targetNamespaces` value from the operator group.

. Configure the name of the OpenShift Update Service application, for example, `service`:
+
[source,terminal]
----
$ NAME=service
----

. Configure the registry and repository for the release images as configured in "Mirroring the OpenShift Container Platform image repository", for example, `registry.example.com/ocp4/openshift4-release-images`:
//TODO: Add xref to the preceding step when allowed.
+
[source,terminal]
----
$ RELEASE_IMAGES=registry.example.com/ocp4/openshift4-release-images
----

. Set the local pullspec for the graph data image to the graph data container image created in "Creating the OpenShift Update Service graph data container image", for example, `registry.example.com/openshift/graph-data:latest`:
//TODO: Add xref to the preceding step when allowed.
+
[source,terminal]
----
$ GRAPH_DATA_IMAGE=registry.example.com/openshift/graph-data:latest
----

. Create an OpenShift Update Service application object:
+
[source,terminal]
----
$ oc -n "${NAMESPACE}" create -f - <<EOF
apiVersion: updateservice.operator.openshift.io/v1
kind: UpdateService
metadata:
  name: ${NAME}
spec:
  replicas: 2
  releases: ${RELEASE_IMAGES}
  graphDataImage: ${GRAPH_DATA_IMAGE}
EOF
----

. Verify the OpenShift Update Service application:

.. Use the following command to obtain a policy engine route:
+
[source,terminal]
----
$ while sleep 1; do POLICY_ENGINE_GRAPH_URI="$(oc -n "${NAMESPACE}" get -o jsonpath='{.status.policyEngineURI}/api/upgrades_info/v1/graph{"\n"}' updateservice "${NAME}")"; SCHEME="${POLICY_ENGINE_GRAPH_URI%%:*}"; if test "${SCHEME}" = http -o "${SCHEME}" = https; then break; fi; done
----
+
You might need to poll until the command succeeds.

.. Retrieve a graph from the policy engine. Be sure to specify a valid version for `channel`. For example, if running in OpenShift Container Platform , use `stable-`:
+
[source,terminal]
----
$ while sleep 10; do HTTP_CODE="$(curl --header Accept:application/json --output /dev/stderr --write-out "%{http_code}" "${POLICY_ENGINE_GRAPH_URI}?channel=stable-4.6")"; if test "${HTTP_CODE}" -eq 200; then break; fi; echo "${HTTP_CODE}"; done
----
+
This polls until the graph request succeeds; however, the resulting graph might be empty depending on which release images you have mirrored.

+
[NOTE]
====
The policy engine route name must not be more than 63 characters based on RFC-1123. If you see `ReconcileCompleted` status as `false`  with the reason `CreateRouteFailed` caused by `host must conform to DNS 1123 naming convention
and must be no more than 63 characters`, try creating the Update Service with a shorter name.
====

// Configuring the Cluster Version Operator (CVO)
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="update-service-configure-cvo"]
= Configuring the Cluster Version Operator (CVO)

[role="_abstract"]
After the OpenShift Update Service Operator has been installed and the OpenShift Update Service application has been created, the Cluster Version Operator (CVO) can be updated to pull graph data from the OpenShift Update Service installed in your environment.

.Prerequisites

* The OpenShift Update Service Operator has been installed.
* The OpenShift Update Service graph data container image has been created and pushed to a repository that is accessible to the OpenShift Update Service.
* The current release and update target releases have been mirrored to a registry in the disconnected environment.
* The OpenShift Update Service application has been created.

.Procedure

. Set the OpenShift Update Service target namespace, for example, `openshift-update-service`:
+
[source,terminal]
----
$ NAMESPACE=openshift-update-service
----

. Set the name of the OpenShift Update Service application, for example, `service`:
+
[source,terminal]
----
$ NAME=service
----

.  Obtain the policy engine route:
+
[source,terminal]
----
$ POLICY_ENGINE_GRAPH_URI="$(oc -n "${NAMESPACE}" get -o jsonpath='{.status.policyEngineURI}/api/upgrades_info/v1/graph{"\n"}' updateservice "${NAME}")"
----

. Set the patch for the pull graph data:
+
[source,terminal]
----
$ PATCH="{\"spec\":{\"upstream\":\"${POLICY_ENGINE_GRAPH_URI}\"}}"
----
+
. Patch the CVO to use the OpenShift Update Service in your environment:
+
[source,terminal]
----
$ oc patch clusterversion version -p $PATCH --type merge
----

+
[NOTE]
====
For more information about configuring the CA to trust the update server, see "Configuring the cluster-wide proxy".
====

[role="_additional-resources"]
.Additional resources
* Configuring the cluster-wide proxy

// Verifying your local OSUS installation
// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating_disconnected_cluster/disconnected-update-osus.adoc

[id="verifying-local-osus-installation_{context}"]
= Verifying your local OSUS installation

[role="_abstract"]
Before you proceed to update your cluster, verify that the local OSUS instance is correctly installed and configured in your environment.

.Procedure
. Confirm that the following conditions are met:
* The Cluster Version Operator (CVO) is configured to use your installed OpenShift Update Service application.
* The release image signature config map for the new release is applied to your cluster.
+
[NOTE]
====
The Cluster Version Operator (CVO) uses release image signatures to ensure that release images have not been modified, by verifying that the release image signatures match the expected result.
====
* The current release and update target release images are mirrored to a registry in the disconnected environment.
* A recent graph data container image has been mirrored to your registry.
* A recent version of the OpenShift Update Service Operator is installed.
+
[NOTE]
====
If you have not recently installed or updated the OpenShift Update Service Operator, there might be a more recent version available.
For more information about how to update your OLM catalog in a disconnected environment, see "Using Operator Lifecycle Manager in disconnected environments".
====
+
After you configure your cluster to use the installed OpenShift Update Service and local mirror registry, you can proceed to update your cluster.

[role="_additional-resources"]
.Additional resources
* Using Operator Lifecycle Manager in disconnected environments

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Mirroring OpenShift Container Platform images

* Updating a cluster using the web console

* Updating a cluster using the CLI

* Performing a Control Plane Only update

* Performing a canary rollout update
