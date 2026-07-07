---
title: "Validating an installation"
type: reference
domain: openshift
slug: installing-4-22-validating-an-installation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/validating-an-installation
version: 4.22
family: installing
documentKind: "Documentation"
---

# Validating an installation

[id="validating-an-installation"]
= Validating an installation

[role="_abstract"]
You can check the status of an OpenShift Container Platform cluster after an installation or validate boot artifacts before an installation.

After you complete the procedures, you can move onto postinstallation cluster tasks. If you experience installation issues, see "Troubleshooting installations" in the _Additional resources_" section.

//Validating RHCOS live media
// Module included in the following assemblies:
//
// * installing/validation_and_troubleshooting/valiadting-an-installation.adoc

[id="rhcos-validate-live-media_{context}"]
= Validating {op-system} live media

[role="_abstract"]
For user-provisioned infrastructure installations, you can access information and use the OpenShift Container Platform installer to indirectly validate {op-system} bootimage artifacts using their SHA-256 checksums.

The OpenShift Container Platform installation program contains pinned versions of {op-system} bootimages. Fully automated installations use these pinned artifacts by default. The mirror registry where you downloaded the installation program contains a `sha256sum` encrypted with the Red{nbsp}Hat product key.

.Procedure

* Run the following command to print the metadata for any bootimage artifact:
+
[source,terminal]
----
$ openshift-install coreos print-stream-json | jq <bootimage>
----
+
where:
+
`<bootimage>`: Specifies the query for the bootimage you want to obtain information on. For validation purposes, the bootimage artifact must have a generated `sha256sum`. This can include OVA, VHD, QCOW2, and others. For example, to get information on an `x86_64` architecture `iso` file for bare metal platforms, use `.architectures.x86_64.artifacts.metal.formats.iso`.
+
.Example output
[source,text]
----
{
  "disk": {
    "location": "<url>/art/storage/prod/streams/<release>/builds/rhcos-<release>-live.<architecture>.<artifact>",
    "sha256": "abc2add9746eb7be82e6919ec13aad8e9eae8cf073d8da6126d7c95ea0dee962"
  }
}
----

//Reviewing the installation log
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="reviewing-the-installation-log_{context}"]
= Reviewing the installation log

[role="_abstract"]
The OpenShift Container Platform installation log contains a summary of the installation, including the information required to access the cluster after installation.

.Prerequisites

* You have access to the installation host.

.Procedure

* Review the `.openshift_install.log` log file in the installation directory on your installation host:
+
[source,terminal]
----
$ cat <install_dir>/.openshift_install.log
----
+
Cluster credentials are included at the end of the log if the installation is successful, as outlined in the following example:
+
[source,terminal]
----
...
time="2020-12-03T09:50:47Z" level=info msg="Install complete!"
time="2020-12-03T09:50:47Z" level=info msg="To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'"
time="2020-12-03T09:50:47Z" level=info msg="Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com"
time="2020-12-03T09:50:47Z" level=info msg="Login to the console with user: \"kubeadmin\", and password: \"password\""
time="2020-12-03T09:50:47Z" level=debug msg="Time elapsed per stage:"
time="2020-12-03T09:50:47Z" level=debug msg="    Infrastructure: 6m45s"
time="2020-12-03T09:50:47Z" level=debug msg="Bootstrap Complete: 11m30s"
time="2020-12-03T09:50:47Z" level=debug msg=" Bootstrap Destroy: 1m5s"
time="2020-12-03T09:50:47Z" level=debug msg=" Cluster Operators: 17m31s"
time="2020-12-03T09:50:47Z" level=info msg="Time elapsed: 37m26s"
----

//Viewing the image pull source
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="viewing-the-image-pull-source_{context}"]
= Viewing the image pull source

[role="_abstract"]
For clusters with unrestricted network connectivity, you can view the source of your pulled images by using a command on a node, such as `crictl images`.

However, for disconnected installations, to view the source of pulled images, you must review the CRI-O logs to locate the `Trying to access` log entry, as shown in the following procedure. Other methods to view the image pull source, such as the `crictl images` command, show the non-mirrored image name, even though the image is pulled from the mirrored location.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

* Review the CRI-O logs for a master or worker node:
+
[source,terminal]
----
$ oc adm node-logs <node_name> -u crio
----
+
.Example output
[source,terminal]
----
...
Mar 17 02:52:50 ip-10-0-138-140.ec2.internal crio[1366]: time="2021-08-05 10:33:21.594930907Z" level=info msg="Pulling image: quay.io/openshift-release-dev/ocp-release:4.10.0-ppc64le" id=abcd713b-d0e1-4844-ac1c-474c5b60c07c name=/runtime.v1alpha2.ImageService/PullImage
Mar 17 02:52:50 ip-10-0-138-140.ec2.internal crio[1484]: time="2021-03-17 02:52:50.194341109Z" level=info msg="Trying to access \"li0317gcp1.mirror-registry.qe.gcp.devcluster.openshift.com:5000/ocp/release@sha256:1926eae7cacb9c00f142ec98b00628970e974284b6ddaf9a6a086cb9af7a6c31\""
Mar 17 02:52:50 ip-10-0-138-140.ec2.internal crio[1484]: time="2021-03-17 02:52:50.226788351Z" level=info msg="Trying to access \"li0317gcp1.mirror-registry.qe.gcp.devcluster.openshift.com:5000/ocp/release@sha256:1926eae7cacb9c00f142ec98b00628970e974284b6ddaf9a6a086cb9af7a6c31\""
...
----
+
The `Trying to access` log entry indicates where the image is being pulled from.
+
The log might show the image pull source twice, as shown in the preceding example.
+
If your `ImageContentSourcePolicy` object lists multiple mirrors, OpenShift Container Platform attempts to pull the images in the order listed in the configuration, for example:
+
----
Trying to access \"li0317gcp1.mirror-registry.qe.gcp.devcluster.openshift.com:5000/ocp/release@sha256:1926eae7cacb9c00f142ec98b00628970e974284b6ddaf9a6a086cb9af7a6c31\"
Trying to access \"li0317gcp2.mirror-registry.qe.gcp.devcluster.openshift.com:5000/ocp/release@sha256:1926eae7cacb9c00f142ec98b00628970e974284b6ddaf9a6a086cb9af7a6c31\"
----

//Getting cluster version, status, and update details
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="getting-cluster-version-and-update-details_{context}"]
= Getting cluster version, status, and update details

[role="_abstract"]
You can view the cluster version and status by running the `oc get clusterversion` command. If the status shows that the installation is still progressing, you can review the status of the Operators for more information.

You can also list the current update channel and review the available cluster updates.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {oc-first}.

.Procedure

. Obtain the cluster version and overall status:
+
[source,terminal]
----
$ oc get clusterversion
----
+
.Example output
[source,terminal]
----
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.6.4     True        False         6m25s   Cluster version is 4.6.4
----
+
The example output indicates that the cluster has been installed successfully.

. If the cluster status indicates that the installation is still progressing, you can obtain more detailed progress information by checking the status of the Operators:
+
[source,terminal]
----
$ oc get clusteroperators.config.openshift.io
----

. View a detailed summary of cluster specifications, update availability, and update history:
+
[source,terminal]
----
$ oc describe clusterversion
----

. List the current update channel:
+
[source,terminal]
----
$ oc get clusterversion -o jsonpath='{.items[0].spec}{"\n"}'
----
+
.Example output
[source,terminal]
----
{"channel":"stable-4.6","clusterID":"245539c1-72a3-41aa-9cec-72ed8cf25c5c"}
----

. Review the available cluster updates:
+
[source,terminal]
----
$ oc adm upgrade
----
+
.Example output
[source,terminal]
----
Cluster version is 4.6.4

Updates:

VERSION IMAGE
4.6.6   quay.io/openshift-release-dev/ocp-release@sha256:c7e8f18e8116356701bd23ae3a23fb9892dd5ea66c8300662ef30563d7104f39
----

[role="_additional-resources"]
.Additional resources

* Querying Operator status after installation

* Troubleshooting Operator issues

* Updating a cluster using the web console

* Understanding update channels and releases

// Verification steps for the Cloud Credential Operator utility (`ccoctl`)
// Module included in the following assemblies:
//
// * installing/validation_and_troubleshooting/validating-an-installation.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="cco-ccoctl-install-verifying_{context}"]
= Verifying that a cluster uses short-term credentials

[role="_abstract"]
You can verify that a cluster uses short-term security credentials for individual components by checking the Cloud Credential Operator (CCO) configuration and other values in the cluster.

.Prerequisites

* You deployed an OpenShift Container Platform cluster using the Cloud Credential Operator utility (`ccoctl`) to implement short-term credentials.

* You installed the {oc-first}.

* You are logged in as a user with `cluster-admin` privileges.

.Procedure

* Verify that the CCO is configured to operate in manual mode by running the following command:
+
[source,terminal]
----
$ oc get cloudcredentials cluster \
  -o=jsonpath={.spec.credentialsMode}
----
+
The following output confirms that the CCO is operating in manual mode:
+
.Example output
[source,text]
----
Manual
----

* Verify that the cluster does not have `root` credentials by running the following command:
+
[source,terminal]
----
$ oc get secrets \
  -n kube-system <secret_name>
----
+
where `<secret_name>` is the name of the root secret for your cloud provider.
+
[cols=2,options=header]
|===
|Platform
|Secret name

|{aws-first}
|`aws-creds`

|{azure-first}
|`azure-credentials`

|{gcp-first}
|`gcp-credentials`

|===
+
An error confirms that the root secret is not present on the cluster.
+
.Example output for an {aws-short} cluster
[source,text]
----
Error from server (NotFound): secrets "aws-creds" not found
----

* Verify that the components are using short-term security credentials for individual components by running the following command:
+
[source,terminal]
----
$ oc get authentication cluster \
  -o jsonpath \
  --template='{ .spec.serviceAccountIssuer }'
----
+
This command displays the value of the `.spec.serviceAccountIssuer` parameter in the cluster `Authentication` object.
An output of a URL that is associated with your cloud provider indicates that the cluster is using manual mode with short-term credentials that are created and managed from outside of the cluster.

* {azure-short} clusters: Verify that the components are assuming the {azure-short} client ID that is specified in the secret manifests by running the following command:
+
[source,terminal]
----
$ oc get secrets \
  -n openshift-image-registry installer-cloud-credentials \
  -o jsonpath='{.data}'
----
+
An output that contains the `azure_client_id` and `azure_federated_token_file` fields confirms that the components are assuming the {azure-short} client ID.

* {azure-short} clusters: Verify that the pod identity webhook is running by running the following command:
+
[source,terminal]
----
$ oc get pods \
  -n openshift-cloud-credential-operator
----
+
.Example output
[source,text]
----
NAME                                         READY   STATUS    RESTARTS   AGE
cloud-credential-operator-59cf744f78-r8pbq   2/2     Running   2          71m
pod-identity-webhook-548f977b4c-859lz        1/1     Running   1          70m
----

//Querying the status of the cluster nodes by using the CLI
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="querying-the-status-of-cluster-nodes-using-the-cli_{context}"]
= Querying the status of the cluster nodes by using the CLI

[role="_abstract"]
You can verify the status of the cluster nodes after an installation.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {oc-first}.

.Procedure

. List the status of the cluster nodes by entering the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Verify that the output lists all of the expected control plane and compute nodes and that each node has a `Ready` status:
+
.Example output
[source,terminal]
----
NAME                          STATUS   ROLES    AGE   VERSION
compute-1.example.com         Ready    worker   33m   v1.35.4
control-plane-1.example.com   Ready    master   41m   v1.35.4
control-plane-2.example.com   Ready    master   45m   v1.35.4
compute-2.example.com         Ready    worker   38m   v1.35.4
compute-3.example.com         Ready    worker   33m   v1.35.4
control-plane-3.example.com   Ready    master   41m   v1.35.4
----

. Review CPU and memory resource availability for each cluster node:
+
[source,terminal]
----
$ oc adm top nodes
----
+
.Example output
[source,terminal]
----
NAME                          CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
compute-1.example.com         128m         8%     1132Mi          16%
control-plane-1.example.com   801m         22%    3471Mi          23%
control-plane-2.example.com   1718m        49%    6085Mi          40%
compute-2.example.com         935m         62%    5178Mi          75%
compute-3.example.com         111m         7%     1131Mi          16%
control-plane-3.example.com   942m         26%    4100Mi          27%
----

[role="_additional-resources"]
.Additional resources

* Verifying node health

//Reviewing the cluster status from the OpenShift Container Platform web console
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="reviewing-cluster-status-from-the-openshift-web-console_{context}"]
= Reviewing the cluster status from the OpenShift Container Platform web console

[role="_abstract"]
You can view specific information in the *Overview* page in the OpenShift Container Platform web console.

The *Overview* page displays the following information:

* The general status of your cluster

* The status of the control plane, cluster Operators, and storage

* CPU, memory, file system, network transfer, and pod availability

* The API address of the cluster, the cluster ID, and the name of the provider

* Cluster version information

* Cluster update status, including details of the current update channel and available updates

* A cluster inventory detailing node, pod, storage class, and persistent volume claim (PVC) information

* A list of ongoing cluster activities and recent events

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

* Navigate to *Home* -> *Overview*.

//Reviewing the cluster status from {cluster-manager}
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="reviewing-cluster-status-from-the-openshift-cluster-manager_{context}"]
= Reviewing the cluster status from {cluster-manager-first}

[role="_abstract"]
From the OpenShift Container Platform web console, you can review detailed information about the status of your cluster on {cluster-manager}.

.Prerequisites
* You have logged in to {cluster-manager-url}.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Go to the *Cluster List* in {cluster-manager-url} and locate your OpenShift Container Platform cluster.

. Click the *Overview* tab for your cluster.

. Review the following information about your cluster:
+
* vCPU and memory availability and resource usage
+
* The cluster ID, status, type, region, and the provider name
+
* Node counts by node type
+
* Cluster version details, the creation date of the cluster, and the name of the cluster owner
+
* The life cycle support status of the cluster
+
* Subscription information, including the service level agreement (SLA) status, the subscription unit type, the production status of the cluster, the subscription obligation, and the service level
+
[TIP]
====
To view the history for your cluster, click the *Cluster history* tab.
====

. Go to the *Monitoring* page to review the following information:
+
* A list of any issues that have been detected
+
* A list of alerts that are firing
+
* The cluster Operator status and version
+
* The cluster's resource usage

. Optional: Go to the *Overview* menu to view information that {red-hat-lightspeed} collects about your cluster:
+
* Potential issues that your cluster might be exposed to, categorized by risk level
+
* Health-check status by category

[role="_additional-resources"]
.Additional resources

* Using {red-hat-lightspeed} to identify issues with your cluster

//Checking cluster resource availability and utilization
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="checking-cluster-resource-availability-and-utilization_{context}"]
= Checking cluster resource availability and utilization

[role="_abstract"]
OpenShift Container Platform provides a comprehensive set of monitoring dashboards that you can analyze to better understand the state of cluster components.

As an administrator, you can access dashboards for core OpenShift Container Platform components, including:

* etcd

* Kubernetes compute resources

* Kubernetes network resources

* Prometheus

* Dashboards relating to cluster and node performance

.Example compute resources dashboard
image::monitoring-dashboard-compute-resources.png[Screenshot of the OpenShift Container Platform monitoring dashboard showing compute resources including CPU usage, memory consumption, and pod metrics with time-series graphs]

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Observe* -> *Dashboards*.

. Choose a dashboard in the *Dashboard* list. Some dashboards, such as the *etcd* dashboard, produce additional sub-menus when selected.

. Optional: Select a time range for the graphs in the *Time Range* list.
+
** Select a pre-defined time period.
+
** Set a custom time range by selecting *Custom time range* in the *Time Range* list.
+
.. Input or select the *From* and *To* dates and times.
+
.. Click *Save* to save the custom time range.

. Optional: Select a *Refresh Interval*.

. Hover over each of the graphs within a dashboard to display detailed information about specific items.

[role="_additional-resources"]
.Additional resources

* About OpenShift Container Platform monitoring

//Listing alerts that are firing
// Module included in the following assemblies:
//
// *installing/validation_and_troubleshooting/validating-an-installation.adoc

[id="listing-alerts-that-are-firing_{context}"]
= Listing alerts that are firing

[role="_abstract"]
Alerts provide notifications when a set of defined conditions are true in an OpenShift Container Platform cluster. The Alerting UI in the OpenShift Container Platform web console displays alerts that are firing and provides detailed information about each alert.

.Prerequisites

* You have access to the OpenShift Container Platform web console.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. In the *Administrator* perspective, navigate to the *Observe* -> *Alerting* -> *Alerts* page.

. Review the alerts that are firing, including their *Severity*, *State*, and *Source*. Use this information to identify which alerts require immediate attention.

. Select an alert to view more detailed information in the *Alert Details* page.

[role="_additional-resources"]
.Additional resources

* Managing alerts as an Administrator
* Troubleshooting installations
* Postinstallation cluster tasks
