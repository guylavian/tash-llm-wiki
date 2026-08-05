---
title: "Installing optional RPM packages"
type: reference
domain: openshift
slug: microshift-install-rpm-opt-4-22-microshift-install-optional-rpms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm_opt/microshift-install-optional-rpms
version: 4.22
family: microshift_install_rpm_opt
documentKind: "Documentation"
---

# Installing optional RPM packages

[id="microshift-install-optional-rpms"]
= Installing optional RPM packages

[role="_abstract"]
When you install {microshift-short}, you can add optional RPM packages to help manage your deployments. Examples of optional RPMs include those designed to expand your network, add and manage Operators, and manage applications. Use the following procedures to add the packages that you need.

// Module included in the following assemblies:
//
// microshift/microshift-install-optional-rpms.adoc
// microshift_running_apps/microshift.gitops.adoc

[id="microshift-installing-rpms-for-gitops_{context}"]
= Installing the {gitops} Argo CD manifests from an RPM package

[role="_abstract"]
You can use a lightweight version of {gitops-title} with {microshift-short} to help manage your applications by installing the `microshift-gitops` RPM package.

The `microshift-gitops` RPM package includes the necessary manifests to run core Argo CD.

[IMPORTANT]
====
The Argo CD web console is not available on {microshift-short}. This process installs basic {gitops} functions.
====

.Prerequisites

* You installed {microshift-short} version 4.16 or later.
* You configured 250MB RAM of additional storage.

.Procedure

. Enable the {gitops} repository with the subscription manager by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager repos --enable=gitops-{gitops-ver}-for-{rhel-major}-$(uname -m)-rpms
----

. Install the {microshift-short} {gitops} package by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y microshift-gitops
----

. To deploy Argo CD pods, restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

.Verification

* You can verify that your pods are running properly by entering the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-gitops
----
+
.Example output
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS   AGE
argocd-application-controller-0       1/1     Running   0          4m11s
argocd-redis-56844446bc-dzmhf         1/1     Running   0          4m12s
argocd-repo-server-57b4f896cf-7qk8l   1/1     Running   0          4m12s
----

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="microshift-installing-multus_{context}"]
= Installing the multiple networks plugin

[role="_abstract"]
You can install the {microshift-short} Multus Container Network Interface (CNI) plugin alongside a new {microshift-short} installation. If you want to attach additional networks to a pod for high-performance network configurations, install the `microshift-multus` RPM package.

[IMPORTANT]
====
The {microshift-short} Multus CNI plugin manifests are included in the {microshift-short} binary. To enable multiple networks, you can either set the value in the {microshift-short} `config.yaml` file to `Enabled`, or use the configuration snippet in the `microshift-multus` RPM. Uninstalling the {microshift-short} Multus CNI is not supported in either case.
====

.Procedure

* Install the Multus RPM package by running the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-multus
----
+
[TIP]
====
If you create your custom resources (CRs) while you are completing your installation of {microshift-short}, you can avoid restarting the service to apply them.
====

.Next steps

* Continue with your new {microshift-short} installation, including any add-ons.
* Create the custom resources (CRs) needed for your {microshift-short} Multus CNI plugin.
* Configure other networking CNIs as needed.
* After you have finished installing all of the RPMs that you want to include, start the {microshift-short} service. The {microshift-short} Multus CNI plugin is automatically deployed.

// Module included in the following assemblies:
//
// microshift/microshift-install-rpm.adoc

[id="microshift-installing-with-olm-from-rpm-package_{context}"]
= Installing the Operator Lifecycle Manager (OLM) from an RPM package

[role="_abstract"]
When you install {microshift-short}, the Operator Lifecycle Manager (OLM) package is not installed by default. You can install the OLM on your {microshift-short} instance by using an RPM package. OLM helps you install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running in each {microshift-short} node.

.Procedure

. Install the OLM package by running the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-olm
----

. To apply the manifest from the package to an active node, run the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

// Module included in the following assemblies:
//
//  microshift_running_apps/microshift-observability-service.adoc

[id="microshift-otel-install_{context}"]
= Installing and enabling {microshift-short} Observability

[role="_abstract"]
You can install {microshift-short} Observability at any time, including during the initial {microshift-short} installation. Observability collects and transmits system data for monitoring and analysis, such as performance and usage metrics and error reporting.

.Procedure
. Install the `microshift-observability` RPM by entering the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-observability
----

. Enable the `microshift-observability` system service by entering the following command:
+
[source,terminal]
----
$ sudo systemctl enable microshift-observability
----

. Start the `microshift-observability` system service by entering the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift-observability
----

. Restart {microshift-short} after the initial installation.
+
[source,terminal]
----
$ sudo systemctl restart microshift-observability
----
+
The installation is successful if there is no output after you start the `microshift-observability` RPM.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-install_{context}"]
= Installing the {rhoai-full} RPM

[role="_abstract"]
To use AI models in {microshift-short} deployments, install the {rhoai-full} ({rhoai}) RPM with a new {microshift-short} installation. You can also install the RPM on an existing {microshift-short} instance if you restart the system.

[NOTE]
====
The `microshift-ai-model-serving` RPM contains manifests that deploy `kserve`, with the raw deployment mode enabled, and `ServingRuntimes` objects in the `redhat-ods-applications` namespace.
====

.Prerequisites

* The system requirements for installing {microshift-short} have been met.
* You have root user access to your machine.
* The {oc-first} is installed.
* You configured your LVM VG with the capacity needed for the PVs of your workload.
* You have the RAM and disk space required for your AI model.
* You configured the required accelerators, hardware, operating system, and {microshift-short} to provide the resources your model needs.
* Your AI model is ready to use.

.Procedure

. Install the {microshift-short} AI-model-serving RPM package by running the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-ai-model-serving
----

. As a root user, restart the {microshift-short} service by entering the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

. Optional: Install the release information package by running the following command:
+
[source,terminal]
----
$ sudo dnf install microshift-ai-model-serving-release-info
----
+
[NOTE]
====
The `microshift-ai-model-serving-release-info` RPM contains a JSON file with image references useful for offline procedures or deploying a copy of a `ServingRuntime` custom resource (CR) to your namespace during a bootc image build.
====

.Verification

* Verify that the `kserve` pod is running in the `redhat-ods-applications` namespace by entering the following command:
+
[source,terminal]
----
$ oc get pods -n redhat-ods-applications
----
+
.Example output
[source,text]
----
NAME                                        READY   STATUS    RESTARTS   AGE
kserve-controller-manager-7fc9fc688-kttmm   1/1     Running   0          1h
----

.Next steps

* Create a namespace for your AI model.
* Package your model into an OCI image.
* Configure a model-serving runtime.
* Verify that your model is ready for inferencing.
* Make requests against the model server.

[id="additional-resources_microshift-install-optional-rpms"]
[role="_additional-resources"]
== Additional resources

* Automating application management with the {gitops-short} controller
* About using multiple networks
* Using Operator Lifecycle Manager with {microshift-short}
* Using {microshift-short} Observability
* Using {rhoai} with {microshift-short}
