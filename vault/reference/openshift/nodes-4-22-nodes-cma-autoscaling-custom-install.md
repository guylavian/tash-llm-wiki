---
title: "Installing the custom metrics autoscaler"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-install
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Installing the custom metrics autoscaler

[id="nodes-cma-autoscaling-custom-install"]
= Installing the custom metrics autoscaler

You can use the OpenShift Container Platform web console to install the Custom Metrics Autoscaler Operator.

The installation creates the following five CRDs:

* `ClusterTriggerAuthentication`
* `KedaController`
* `ScaledJob`
* `ScaledObject`
* `TriggerAuthentication`

The installation process also creates the `KedaController` custom resource (CR). You can modify the default `KedaController` CR, if needed. For more information, see "Editing the Keda Controller CR".

[NOTE]
====
If you are installing a Custom Metrics Autoscaler Operator version lower than 2.17.2, you must manually create the Keda Controller CR. You can use the procedure described in "Editing the Keda Controller CR" to create the CR.
====

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-install.adoc

[id="nodes-cma-autoscaling-custom-install_{context}"]
= Installing the custom metrics autoscaler

You can use the following procedure to install the Custom Metrics Autoscaler Operator.

.Prerequisites
* Ensure that you have downloaded the {cluster-manager-url-pull} as shown in _Obtaining the installation program_ in the installation documentation for your platform.
+
If you have the pull secret, add the `redhat-operators` catalog to the OperatorHub custom resource (CR) as shown in _Configuring OpenShift Container Platform to use Red Hat Operators_.

* Remove any previously-installed Technology Preview versions of the Cluster Metrics Autoscaler Operator.

* Remove any versions of the community-based KEDA.
+
Also, remove the KEDA 1.x custom resource definitions by running the following commands:
+
[source,terminal]
----
$ oc delete crd scaledobjects.keda.k8s.io
----
+
[source,terminal]
----
$ oc delete crd triggerauthentications.keda.k8s.io
----

* Optional: If you need the Custom Metrics Autoscaler Operator to connect to off-cluster services, such as an external Kafka cluster or an external Prometheus service, put any required service CA certificates into a config map. The config map must exist in the same namespace where the Operator is installed. For example:
+
[source,terminal]
----
$ oc create configmap -n openshift-keda thanos-cert  --from-file=ca-cert.pem
----

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

. Choose *Custom Metrics Autoscaler* from the list of available Operators, and click *Install*.

. On the *Install Operator* page, ensure that the *All namespaces on the cluster (default)* option
is selected for *Installation Mode*. This installs the Operator in all namespaces.

. Ensure that the *openshift-keda* namespace is selected for *Installed Namespace*. OpenShift Container Platform creates the namespace, if not present in your cluster.

. Click *Install*.

. Verify the installation by listing the Custom Metrics Autoscaler Operator components:

.. Navigate to *Workloads* -> *Pods*.

.. Select the `openshift-keda` project from the drop-down menu and verify that the `custom-metrics-autoscaler-operator-*` pod is running.

.. Navigate to *Workloads* -> *Deployments* to verify that the `custom-metrics-autoscaler-operator` deployment is running.

. Optional: Verify the installation in the OpenShift CLI using the following commands:
+
[source,terminal]
----
$ oc get all -n openshift-keda
----
+
The output appears similar to the following:
+
.Example output
[source,terminal]
----
NAME                                                      READY   STATUS    RESTARTS   AGE
pod/custom-metrics-autoscaler-operator-5fd8d9ffd8-xt4xp   1/1     Running   0          18m

NAME                                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/custom-metrics-autoscaler-operator   1/1     1            1           18m

NAME                                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/custom-metrics-autoscaler-operator-5fd8d9ffd8   1         1         1       18m
----

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-install.adoc

[id="sd-nodes-cma-autoscaling-custom-install_{context}"]
= Install the custom metrics autoscaler

[role="_abstract"]
Install the Custom Metrics Autoscaler Operator to enable autoscaling of your workloads based on custom metrics from external sources such as Kafka or Prometheus.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
+
If your OpenShift Container Platform cluster is in a cloud account that is owned by Red{nbsp}Hat (non-CCS), you must request `cluster-admin` privileges.

* Any previously installed Technology Preview versions of the Cluster Metrics Autoscaler Operator are removed.

* Any versions of the community-based KEDA are removed, including the KEDA 1.x custom resource definitions (CRDs). To learn how to delete CRDs, see step 5 in
Uninstalling the Custom Metrics Autoscaler Operator.
Uninstalling the Custom Metrics Autoscaler Operator.
Uninstalling the Custom Metrics Autoscaler Operator.

* The `keda` namespace exists. If the namespace does not exist, you must create it manually.

* Optional: If you need the Custom Metrics Autoscaler Operator to connect to off-cluster services, such as an external Kafka cluster or an external Prometheus service, put any required service CA certificates into a config map. The config map must exist in the same namespace where the Operator is installed. For more information, see
Creating a config map from a file.
Creating a config map from a file.
Creating a config map from a file.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

. From the list of available Operators, choose *Custom Metrics Autoscaler*, and click *Install*.

. On the *Install Operator* page, ensure that the *A specific namespace on the cluster* option is selected for *Installation Mode*.

. For *Installed Namespace*, click *Select a namespace*.

. Click *Select Project*:
+
* If the `keda` namespace exists, select *keda* from the list.
* If the `keda` namespace does not exist:
+
.. Select *Create Project* to open the *Create Project* window.
.. In the *Name* field, enter `keda`.
.. In the *Display Name* field, enter a descriptive name, such as `keda`.
.. Optional: In the *Display Name* field, add a description for the namespace.
.. Click *Create*.

. Click *Install*.

. Verify the installation by listing the Custom Metrics Autoscaler Operator components:

.. Navigate to *Workloads* -> *Pods*.

.. Select the `keda` project from the drop-down menu and verify that the `custom-metrics-autoscaler-operator-*` pod is running.

.. Navigate to *Workloads* -> *Deployments* to verify that the `custom-metrics-autoscaler-operator` deployment is running.

. Optional: Verify the installation in the {oc-first} using the following command:
+
[source,terminal]
----
$ oc get all -n keda
----
+
*Example output*
+
[source,text]
----
NAME                                                      READY   STATUS    RESTARTS   AGE
pod/custom-metrics-autoscaler-operator-5fd8d9ffd8-xt4xp   1/1     Running   0          18m

NAME                                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/custom-metrics-autoscaler-operator   1/1     1            1           18m

NAME                                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/custom-metrics-autoscaler-operator-5fd8d9ffd8   1         1         1       18m
----

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-install.adoc

[id="nodes-cma-autoscaling-keda-controller-edit_{context}"]
= Editing the Keda Controller CR

You can use the following procedure to modify the `KedaController` custom resource (CR), which is automatically installed during the installation of the Custom Metrics Autoscaler Operator.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Installed Operators*.

. Click *Custom Metrics Autoscaler*.

. On the *Operator Details* page, click the *KedaController* tab.

. On the *KedaController* tab, click *Create KedaController* and edit the file.
+
[source,yaml]
----
kind: KedaController
apiVersion: keda.sh/v1alpha1
metadata:
  name: keda
  namespace: openshift-keda
spec:
  watchNamespace: '' <1>
  operator:
    logLevel: info <2>
    logEncoder: console <3>
    caConfigMaps: <4>
    - thanos-cert
    - kafka-cert
    volumeMounts: <5>
    - mountPath: /<path_to_directory>
      name: <name>
    volumes: <6>
    - name: <volume_name>
      emptyDir:
        medium: Memory
  metricsServer:
    logLevel: '0' <7>
    auditConfig: <8>
      logFormat: "json"
      logOutputVolumeClaim: "persistentVolumeClaimName"
      policy:
        rules:
        - level: Metadata
        omitStages: ["RequestReceived"]
        omitManagedFields: false
      lifetime:
        maxAge: "2"
        maxBackup: "1"
        maxSize: "50"
  serviceAccount: {}
----
<1> Specifies a single namespace in which the Custom Metrics Autoscaler Operator scales applications. Leave it blank or leave it empty to scale applications in all namespaces. This field should have a namespace or be empty. The default value is empty.
<2> Specifies the level of verbosity for the Custom Metrics Autoscaler Operator log messages. The allowed values are `debug`, `info`, `error`. The default is `info`.
<3> Specifies the logging format for the Custom Metrics Autoscaler Operator log messages. The allowed values are `console` or `json`. The default is `console`.
<4> Optional: Specifies one or more config maps with CA certificates, which the Custom Metrics Autoscaler Operator can use to connect securely to TLS-enabled metrics sources.
<5> Optional: Add the container mount path.
<6> Optional: Add a `volumes` block to list each projected volume source.
<7> Specifies the logging level for the Custom Metrics Autoscaler Metrics Server. The allowed values are `0` for `info` and `4` for `debug`. The default is `0`.
<8> Activates audit logging for the Custom Metrics Autoscaler Operator and specifies the audit policy to use, as described in the "Configuring audit logging" section.

. Click *Save* to save the changes.
