---
title: "Using {rhoai-full} with {microshift-short}"
type: reference
domain: openshift
slug: microshift-ai-4-22-microshift-rhoai
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_ai/microshift-rhoai
version: 4.22
family: microshift_ai
documentKind: "Documentation"
---

# Using {rhoai-full} with {microshift-short}

[id="microshift-rh-openshift-ai"]
= Using {rhoai-full} with {microshift-short}

[role="_abstract"]
Learn how to serve artificial intelligence and machine learning (AI/ML) models with {ai-first} on your {microshift-short} edge deployments.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-con_{context}"]
= How {rhoai-full} works in {microshift-short}

[role="_abstract"]
Edge deployments are where data happens and decisions need to be made. You can use {rhoai-full} ({rhoai}) to integrate a fleet of {microshift-short}-driven edge devices into the artificial intelligence and machine learning (AI/ML) operations cycle.

{microshift-short} is compatible with a single-model serving platform based on the KServe component of Kubernetes. KServe is a platform that orchestrates model serving.

{rhoai} is a platform for data scientists and developers of AI/ML applications. First, use {rhoai} in the cloud or data center to develop, train, and test an AI model. Then, run your model in your edge deployments on {microshift-short}.

After you deploy your AI model, application data can be sent to the model, so that the model can make data-driven decisions without a human user. This is an ideal scenario for edge applications where interaction with an administrator is naturally limited.

Implemented with KServe::

The KServe component includes model-serving runtimes that implement the loading of various types of model servers. These runtimes are configured with custom resources (CRs). KServe custom resource definitions (CRDs) also define the life cycle of the deployment object, storage access, and networking setup.

Specifics of using {rhoai} with {microshift-short}::

As an edge-optimized Kubernetes deployment, {microshift-short} has the following limitations when using {rhoai}:

* AI model serving on {microshift-short} is only available on the x86_64 architecture.

* A subset of {rhoai} Operator components are supported on {microshift-short}.

* As a single-node Kubernetes distribution, {microshift-short} does not support multi-model deployments. You must use the single-model serving platform.

* You must develop the AI models you want to run on the {microshift-short} model-serving platform in the cloud or your data center. Using {microshift-short} as a development platform for AI models is not supported.

* You must plan for any additional RAM, disk space, and storage configurations required to serve your AI model.

* Not all model servers support the IPv6 networking protocol. Check each model server's documentation to verify that your networking configuration is supported.

* You must secure the exposed model server endpoint, for example, with OAUTH2.

* `ClusterServingRuntimes` CRDs are not supported by {rhoai}, which means that you must copy the `ServingRuntime` CR shipped within the `microshift-ai-model-serving` RPM to your workload namespace.

* To administer model serving on {microshift-short}, you must use the CLI. The {rhoai} dashboard is not supported.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-workflow_{context}"]
= Workflow for using {rhoai} with {microshift-short}

[role="_abstract"]
You can review the following information to learn about the workflow for using {rhoai} with {microshift-short}.

Getting your AI model ready::

* Choose the artificial intelligence (AI) model that best aligns with your edge application and the decisions that need to be made at {microshift-short} deployment sites.
* Develop, train, and test your model in your cloud or data center.
* Plan for the system requirements and additional resources your AI model requires to run.

Setting up the deployment environment::

* Configure your {op-system-bundle} for the specific hardware your deployment runs on, including driver and device plugins.

* To enable GPU or other hardware accelerators for {microshift-short}, follow the guidance specific for your edge device about what you need to install. For example, to use an NVIDIA GPU accelerator, begin by reading the following NVIDIA documentation: Running a GPU-Accelerated Workload on Red Hat Device Edge (NVIDIA documentation).

* For troubleshooting, consult the device documentation or product support.
+
[TIP]
====
Using only a driver and device plugin instead of an Operator might be more resource-efficient.
====

Installing the {microshift-short} {rhoai} RPM::

* Install the `microshift-ai-model-serving` RPM package.

* Restart {microshift-short} if you are adding the RPM while {microshift-short} is running.

Getting ready to deploy::

* Package your AI model into an OCI image, otherwise known as the ModelCar format. If you already have S3-compatible storage or a persistent volume claim set up, you can skip this step, but only the ModelCar format is tested and supported for {microshift-short}.

* Select a model-serving runtime, which acts as your model server. Configure the runtime with the serving runtime and inference service.

** Copy the `ServingRuntime` custom resource (CR) from the default `redhat-ods-applications` namespace to your own namespace.

** Create the `InferenceService` CR.

* Optional: Create a `Route` object so that your model can connect outside the node.

Using your model::

* Make requests against the model server. For example, another pod running in your {microshift-short} deployment that is attached to a camera can stream an image back to the model-serving runtime. The model-serving runtime prepares that image as data for model inferencing. If the model was trained in the binary identification of a bee, the AI model outputs the likelihood that the image data is a bee.

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

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-create-namespace_{context}"]
= Creating a namespace for your AI model on {microshift-short}

[role="_abstract"]
Create a namespace for your AI model and all other resources. Namespaces offer resource isolation, resource management, and access control.

.Prerequisites

* You have root user access to your machine.
* The {oc-first} is installed.

.Procedure

* Create a new namespace by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create ns _<namespace_name>_
----
where:

`_<namespace_name>_`:: Specifies the namespace name to use. In the following examples, `ai-demo` is used.

.Verification

* Verify that you created the namespace by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc get ns _<namespace_name>_
----
where:
+
--
`_<namespace_name>_`:: Specifies the namespace name you want to use. In the following examples, `ai-demo` is used.
--
+
.Example output
[source,text]
----
NAME                STATUS  AGE
ai-demo             Active  1h
----

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-model-package-oci_{context}"]
= Packaging your AI model into an OCI image

[role="_abstract"]
You can package your model into an OCI image and use the ModelCar approach to help you set up offline environments. With the ModelCar approach, your model can be embedded just like any other container image.

[NOTE]
====
If you already have S3-compatible object storage or a configured persistent volume claim, you can upload your AI model to those resources, but only the ModelCar approach is tested and supported.
====

.Prerequisites

* You have root user access to your machine.
* The {oc-first} is installed.
* Podman is installed.
* Your model is ready to use.
* You understand the concepts in the "How to build a ModelCar container" section of the following article about building an OCI image suitable for an vLLM model server, Build and deploy a ModelCar container in OpenShift AI.
+
[NOTE]
====
The exact directory structure depends on the model server. The following example uses a Containerfile with a ResNet-50 model that is compatible with the {ovms} {ov}. {ov} generally does not require an additional hardware accelerator.
====

.Procedure

. Prepare a Containerfile with a compatible model and model server.
+
.Example Containerfile with a ResNet-50 model used with the OVMS
[source,text]
----
FROM registry.access.redhat.com/ubi9/ubi-minimal:latest
RUN microdnf install -y wget && microdnf clean all
RUN mkdir -p /models/1 && chmod -R 755 /models/1
RUN wget -q -P /models/1 \
  https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.1/models_bin/2/resnet50-binary-0001/FP32-INT1/resnet50-binary-0001.bin \
  https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.1/models_bin/2/resnet50-binary-0001/FP32-INT1/resnet50-binary-0001.xml
----

. Set the `IMAGE_REF` environment variable to simplify your process by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ IMAGE_REF=_<ovms-resnet50:test>_
----
where:

`_<ovms-resnet50:test>_`:: Specifies the name of your image reference. In this example, the `_<repo:tag>_` format is used. Your image reference name is specific to your use case.

. Build the Containerfile by running the following command:
+
[source,terminal]
----
$ sudo podman build -t $IMAGE_REF
----
+
Because CRI-O and Podman share storage, using `sudo` is required to make the image part of the root's container storage and usable by {microshift-short}.
+
.Example output
[source,text]
----
STEP 1/4: FROM registry.access.redhat.com/ubi9/ubi-minimal:latest
Trying to pull registry.access.redhat.com/ubi9/ubi-minimal:latest...
Getting image source signatures
Checking if image destination supports signatures
Copying blob 533b69cfd644 done   |
Copying blob 863e9a7e2102 done   |
Copying config 098048e6f9 done   |
Writing manifest to image destination
Storing signatures
STEP 2/4: RUN microdnf install -y wget && microdnf clean all
<< SNIP >>
--> 4c74352ad42e
STEP 3/4: RUN mkdir -p /models/1 && chmod -R 755 /models/1
--> bfd31acb1e81
STEP 4/4: RUN wget -q -P /models/1   https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.1/models_bin/2/resnet50-binary-0001/FP32-INT1/resnet50-binary-0001.bin   https://storage.openvinotoolkit.org/repositories/open_model_zoo/2022.1/models_bin/2/resnet50-binary-0001/FP32-INT1/resnet50-binary-0001.xml
COMMIT ovms-resnet50:test
--> 375b265c1c4b
Successfully tagged localhost/ovms-resnet50:test
375b265c1c4bc6f0a059c8739fb2b3a46e1b563728f6d9c51f26f29bb2c87
----

. Optional: Push the Containerfile to your registry by running the following command:
+
[source,terminal]
----
$ sudo podman push $IMAGE_REF
----
+
[IMPORTANT]
====
For offline use cases, include a tag other than `latest`. If you use the `latest` tag, the container that fetches and sets up the model is configured with the `imagePullPolicy:` parameter set to `Always` and the local image is ignored. If you use any other tag than `latest`, the `imagePullPolicy:` parameter is set to `IfNotPresent`.
====

.Verification

* Verify that the image exists by running the following command:
+
[source,terminal]
----
$ sudo podman images _<ovms-resnet50>_
----
where:
+
--
`_<ovms-resnet50>_`:: Specifies the name of your image reference.
--
+
.Example output
[source,text]
----
REPOSITORY                TAG   IMAGE ID        CREATED         SIZE
localhost/ovms-resnet50   test  375b265c1c4b    3 minutes ago   136 MB
----

.Next steps

* Configure a model-serving runtime.
* Confirm that your AI model is ready for inferencing.
* Make requests against the model server.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-serving-ai-models-con_{context}"]
= Serving AI models on {microshift-short}

[role="_abstract"]
You can review the following information to learn how to serve models on the {rhoai} single-model serving platform in {microshift-short} by configuring a model-serving runtime using the `ServingRuntime` and `InferenceService` custom resource (CRs).

Model-serving runtimes for AI models in {microshift-short}::

A model-serving runtime is an environment for deploying and managing an AI model, providing integration with a specified model server and the model frameworks that it supports. Creating the model-serving runtime means configuring the objects that select the right model format for the AI model and serve the queries, among other detailed functions specific your deployment.

The `ServingRuntime` custom resource::

The `ServingRuntime` CR is a YAML file that defines the templates for pods that can dynamically load and unload AI model formats and exposes a service endpoint for querying the model through the API. Each `ServingRuntime` CR contains the information needed to run AI models, including the container image of the runtime and a list of the model formats that the model-serving runtime supports. Other configuration settings for the model-serving runtime can be set with environment variables defined in the container specification.

The `InferenceService` custom resource::

The `InferenceService` CR is a YAML file that creates a server or inference service to process inference queries, pass them to the model, then return the inference output. In {microshift-short}, the output is returned in the CLI. This inference service configuration file can also include many other options, such as specifying a hardware accelerator.

[IMPORTANT]
====
As a single-node Kubernetes distribution, {microshift-short} does not support multi-model deployments. You must use the single-model serving platform. In each {microshift-short} deployment, you can use one AI model, but potentially more than one model runtime.
====

Workflow for configuring a model-serving runtime::

* Select the model-serving runtime that supports the format of your AI model.

* Create the `ServingRuntime` CR in your workload namespace.
//CRD is shipped with product; the CR is what users are creating.

* If the {microshift-short} node is already running, you can export the required `ServingRuntime` CR to a file and edit it.

* If the {microshift-short} node is not running, or if you want to manually prepare a manifest, you can use the original definition on the disk, which is part of the `microshift-ai-model-serving` RPM.

* Create the `InferenceService` CR in your workload namespace.
//CRD is shipped with product; the CR is what users are creating.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-supported-crds_{context}"]
= Supported {rhoai} custom resource definitions

[role="_abstract"]
You can review the following information to learn about the {rhoai} custom resource definitions (CRDs).

The following CRD are supported:

* `InferenceServices`
* `TrainedModels`
* `ServingRuntimes`
* `InferenceGraphs`
* `ClusterStorageContainers`
* `ClusterLocalModels`
* `LocalModelNodeGroups`

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-supported-models_{context}"]
= Supported {rhoai} model-serving runtimes

[role="_abstract"]
You can review the following information to learn about the {rhoai} model-serving runtimes that are verified for {microshift-short} deployments.

The following {rhoai} model-serving runtimes that are verified for {microshift-short} deployments:

* vLLM ServingRuntime for KServe
* {ovms}
+
[IMPORTANT]
====
The {ovms} does not support the IPv6 networking protocol. Check each model server before use to ensure that it supports your networking configuration.
====

The following runtimes are available for development purposes with {microshift-short}:

* Caikit Text Generation Inference Server (Caikit-TGIS) ServingRuntime for KServe
* Caikit Standalone ServingRuntime for KServe
* Text Generation Inference Server (TGIS) Standalone ServingRuntime for KServe
* vLLM ServingRuntime with Gaudi accelerators support for KServe
* vLLM ROCm ServingRuntime for KServe
* Custom runtimes that you create and test

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-servingruntimes-ex_{context}"]
= Creating a ServingRuntime CR for use in {microshift-short}

[role="_abstract"]
You can create a `ServingRuntime` custom resource (CR) based on installed manifests and release information.

The included steps are an example of reusing the included `microshift-ai-model-serving` manifest files to re-create the {ovms} ({ov}) model-serving runtime in the workload namespace.

[NOTE]
====
This approach does not require a live node, so it can be part of CI/CD automation.
====

.Prerequisites

* Both the `microshift-ai-model-serving` and `microshift-ai-model-serving-release-info` RPMs are installed.
* You have root user access to your machine.
* The {oc-first} is installed.

.Procedure

. Extract the image reference of the `ServingRuntime` CR you want to use from the {microshift-short} release information file by running the following command:
+
[source,terminal]
----
$ OVMS_IMAGE="$(jq -r '.images | with_entries(select(.key == "ovms-image")) | .[]' /usr/share/microshift/release/release-ai-model-serving-"$(uname -i)".json)"
----
+
In this example, the image reference for the {ov} model-serving runtime is extracted.

. Copy the original `ServingRuntime` YAML file by running the following command:
+
[source,terminal]
----
$ cp /usr/lib/microshift/manifests.d/050-microshift-ai-model-serving-runtimes/ovms-kserve.yaml ./ovms-kserve.yaml
----

. Add the actual image reference to the `image:` parameter field value of the `ServingRuntime` YAML by running the following command:
+
[source,terminal]
----
$ sed -i "s,image: ovms-image,image: ${OVMS_IMAGE}," ./ovms-kserve.yaml
----

. Create the `ServingRuntime` object in a custom namespace using the YAML file by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create -n _<ai_demo>_ -f ./ovms-kserve.yaml
----
where:
+
--
`_<ai_demo>_`:: Specifies the name of your namespace.
--
+
[IMPORTANT]
====
If the `ServingRuntime` CR is part of a new manifest, set the namespace in the `kustomization.yaml` file, for example:

.Example Kustomize manifest namespace value
[source,yaml]
----
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: ai-demo
resources:
  - ovms-kserve.yaml
#...
----
====

.Next steps

* Create the `InferenceService` object.
* Verify that your model is ready for inferencing.
* Query the model.
* Optional: Examine the model metrics.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-inferenceservice-ex_{context}"]
= Creating an InferenceService custom resource

[role="_abstract"]
You can create an `InferenceService` custom resource (CR) that instructs KServe how to create a deployment for serving your AI model. KServe uses the `ServingRuntime` based on the `modelFormat` value specified in the `InferenceService` CR.

.Prerequisites

* You configured the `ServingRuntimes` CR.
* You have root user access to your machine.
* The {oc-first} is installed.

.Procedure

. Create the `InferenceService` CR.
+
.Example `InferenceService` object with an `openvino_ir` model format
[source,yaml]
----
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: ovms-resnet50
spec:
  predictor:
    model:
      protocolVersion: v2
      modelFormat:
        name: openvino_ir
      storageUri: "oci://localhost/ovms-resnet50:test"
      args:
      - --layout=NHWC:NCHW
----
where:

`spec.predictor.model.args.layout`:: Specifies an additional argument to make {ovms} ({ov}) accept the request input data in a different layout than the model was originally exported with. Extra arguments are passed through to the {ov} container.

. Save the `InferenceService` example to a file, then create it on the cluster by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc create -n _<ai_demo>_ -f ./FILE.yaml
----
where:
+
--
`_<ai_demo>_`:: Specifies your namespace name.
--
+
.Example output
[source,terminal]
----
inferenceservice.serving.kserve.io/ovms-resnet50 created
----
+
[NOTE]
====
A deployment and a pod are expected to appear in the specified namespace. Depending on the size of the image specified in the `ServingRuntime` CR and the size of the ModelCar OCI image, it might take several minutes for the pod to be ready.
====

.Next steps

* Verify that the model-serving runtime is ready.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-export-metrics-otel_{context}"]
= Exporting model-server metrics by using Open Telemetry

[role="_abstract"]
You can export model-server metrics by using Open Telemetry if you installed the `microshift-observability` RPM for {microshift-short}.

[NOTE]
====
You can alternatively get the Prometheus-format metrics of the model server by making a request on the `/metrics` endpoint. See "Getting the model-server metrics" for more information.
====

.Prerequisites

* You configured the `ServingRuntimes` CR.
* You have root user access to your machine.
* The {oc-first} is installed.
* You installed the `microshift-observability` RPM.
* Your {microshift-short} Open Telemetry configuration includes the Prometheus Receiver. For more information, see Prometheus Receiver.

.Procedure

* Add the following Open Telemetry annotation to your `InferenceService` custom resource:
+
.Example `InferenceService` object with Open Telemetry
[source,yaml]
----
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: ovms-resnet50
#...
  annotations:
    prometheus.io/scrape: "true"
#...
----

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-inferenceservice-more-options_{context}"]
= More InferenceService CR options

[role="_abstract"]
You can include many different options in the inference service YAML file, as described in the Control Plane API Reference (KServe documentation).

For example, you can include a `resources` section that is passed first to the deployment and then to the pod, so that the model server gets access to your hardware through the device plugin.

.Example NVIDIA device `resources` snippet in an `InferenceService` CR
[source,yaml]
----
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: is-name
spec:
  predictor:
    model:
      resources:
        limits:
          nvidia.com/gpu: 1
        requests:
          nvidia.com/gpu: 1
#...
----

For complete `InferenceService` specifications, see the Control Plane API Reference (KServe documentation).

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-model-serving-rt-verify_{context}"]
= Verifying that the model-serving runtime is ready

[role="_abstract"]
You can use the {oc-first} to verify that your model-serving runtime is ready for use by checking that the downstream generation activities are complete.

.Prerequisites

* You configured the `ServingRuntimes` CR.
* You created the `InferenceService` CR.
* You have root user access to your machine.
* The {oc-first} is installed.

.Procedure

. Check that the AI model is deployed in your custom namespace by running the following command:
+
[source,terminal]
----
$ oc get -n ai-demo deployment
----
+
.Example output
[source,terminal]
----
NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
ovms-resnet50-predictor   1/1     1            1           72s
----

. Confirm that your deployment is in progress by running the following command:
+
[source,terminal]
----
$ oc rollout status -n ai-demo deployment ovms-resnet50-predictor
----
+
.Example output
[source,terminal]
----
deployment "ovms-resnet50-predictor" successfully rolled out
----

. Check that the AI model workload pod is deployed in your custom namespace by running the following command:
+
[source,terminal]
----
$ oc get -n ai-demo pod
----
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS      AGE
ovms-resnet50-predictor-6fdb566b7f-bc9k5   2/2     Running   1 (72s ago)   74s
----

. Check for the service that KServe created by running the following command:
+
[source,terminal]
----
$ oc get svc -n ai-demo
----
+
.Example output
[source,terminal]
----
NAME                      TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
ovms-resnet50-predictor   ClusterIP   None         <none>        80/TCP    119s
----

.Next steps

* Create a `Route` object so that your applications can reach the {microshift-short} node.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-create-route_{context}"]
= Creating a route to use for AI queries in {microshift-short}

[role="_abstract"]
You can create a route so that your AI model can receive queries and give output by using the `oc expose svc` command or creating a definition in a YAML file and apply it.

.Prerequisites

* You have root user access to your machine.
* The {oc-first} is installed.

.Procedure

* Create a route using the following command:
+
[source,terminal]
----
$ oc expose svc -n ai-demo ovms-resnet50-predictor
----
+
.Example output
[source,terminal]
----
route.route.openshift.io/ovms-resnet50-predictor exposed
----

.Verification

* Verify that the route you created exists by running the following command:
+
[source,terminal]
----
$ oc get route -n ai-demo
----
+
.Example output
[source,terminal]
----
NAME                      HOST                                               ADMITTED   SERVICE                   TLS
ovms-resnet50-predictor   ovms-resnet50-predictor-ai-demo.apps.example.com   True       ovms-resnet50-predictor
----

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-query-model-con_{context}"]
= About querying your AI model

[role="_abstract"]
Querying your model through the API is also called model inferencing. Model inferencing is most often used to retrieve information, automate tasks, make predictions, provide data insights, or perform actions.

In general, queries must be constructed using a format compatible with the AI model being used. A model-serving runtime formats queries automatically. The model processes the query according to the underlying training and data, then provides an output. The output is expected to align with the purpose of the model itself, whether that be to give an answer, make a prediction, or perform a task.

The following examples outline general steps to make sure your model is ready for inferencing, and what you might expect in a query output from the serving runtime.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-verify-model-connected_{context}"]
= Verifying that your AI model is accessible

[role="_abstract"]
Before querying the model through the API, you can verify that the model is accessible and ready to provide answers based on the connected data.

The following examples continue with the {ovms}.

.Prerequisites

* You configured the AI model-serving runtime.
* You uploaded your AI model to {microshift-short}.
* {microshift-short} is running.
* You installed {oc-first}.

.Procedure

. Get the IP address of the {microshift-short} node and assign it to the `IP` variable as the following example command shows:
+
[source,terminal]
----
$ IP=$(oc get nodes -o json | jq -r '.items[0].status.addresses[0].address')
----

. Identify the name of the route you created by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc get route -n ai-test _<route_name>_ -o yaml
----
where:

`_<route_name>_`:: Specifies the actual name of your route.

. Extract and assign the `HOST` value of the route to the `DOMAIN` variable by running the following command:
+
[source,terminal,subs="+quotes"]
----
DOMAIN=$(oc get route -n ai-test _<route_name>_ -o=jsonpath="{ .status.ingress[0].host }")
----
where:

`_<route_name>_`:: Specifies the actual name of your route.

. Enable data transfer from the route to the {microshift-short} IP address by running the following command:
+
[source,terminal]
----
$ curl -i "${DOMAIN}/v2/models/ovms-resnet50/ready" --connect-to "${DOMAIN}::${IP}:"
----
+
Instead of using the `--connect-to "${DOMAIN}::${IP}:"` flag, you can also use real DNS, or add the IP address and the domain to the `/etc/hosts` file.
+
.Example output
[source,text]
----
HTTP/1.1 200 OK
content-type: application/json
date: Wed, 12 Mar 2025 16:01:32 GMT
content-length: 0
set-cookie: 56bb4b6df4f80f0b59f56aa0a5a91c1a=4af1408b4a1c40925456f73033d4a7d1; path=/; HttpOnly
----

. Query the model metadata by running the following command:
+
[source,terminal]
----
$ curl "${DOMAIN}/v2/models/ovms-resnet50" --connect-to "${DOMAIN}::${IP}:"
----
+
.Example output
[source,json]
----
{"name":"ovms-resnet50","versions":["1"],"platform":"OpenVINO","inputs":[{"name":"0","datatype":"FP32","shape":[1,224,224,3]}],"outputs":[{"name":"1463","datatype":"FP32","shape":[1,1000]}]
----

.Next steps

* Verify that your model is ready for inferencing.
* Query the model.
* Verify the model response.
* Optional: Get the model server metrics.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-get-model-ready-inference_{context}"]
= Getting your AI model ready for inference

[role="_abstract"]
Before querying your AI model through the API, you can get the model ready to provide answers based on the training data.

The following examples continue with the OVMS model.

.Prerequisites

* {microshift-short} is running.
* You have the `xxd` utility, which is part of the `vim-common` package.
* You configured the model-serving runtime.
* You uploaded your AI model to {microshift-short}.

.Procedure

. Download an image of a bee from the {ovms} examples by running the following command:
+
[source,terminal]
----
$ curl -O https://raw.githubusercontent.com/openvinotoolkit/model_server/main/demos/common/static/images/bee.jpeg
----

. Create the request data by running the following script:
+
[source,bash]
----
IMAGE=./bee.jpeg
REQ=./request.json

# Add an inference header
echo -n '{"inputs" : [{"name": "0", "shape": [1], "datatype": "BYTES"}]}' > "${REQ}"
# Get the size of the inference header
HEADER_LEN="$(stat -c %s "${REQ}")"
# Add size of the data (image) in binary format (4 bytes, little endian)
printf "%08X" $(stat --format=%s "${IMAGE}") | sed 's/\(..\)/\1\n/g' | tac | tr -d '\n' | xxd -r -p >> "${REQ}"
# Add the data, that is, append the image to the request file
cat "${IMAGE}" >> "${REQ}"
----
+
* The inference header size must be passed to {ovms} later in the form of an HTTP header.
* The {ovms} requires 4 bytes in little endian byte order.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-query-model_{context}"]
= Querying your AI model

[role="_abstract"]
You can make an inference request against the AI model server that is using the `ovms-resnet50` model.

.Prerequisites

* {microshift-short} is running.
* You configured the model-serving runtime.
* You uploaded your AI model to {microshift-short}.

.Procedure

* Make an inference request against the model server that is using the `ovms-resnet50` model by running the following command:
+
[source,terminal]
----
$ curl \
    --data-binary "@./request.json" \
    --header "Inference-Header-Content-Length: ${HEADER_LEN}" \
    "${DOMAIN}/v2/models/ovms-resnet50/infer" \
    --connect-to "${DOMAIN}::${IP}:" > response.json
----
+
.Example inferencing output, saved to a `response.json`
[source,json]
----
{
    "model_name": "ovms-resnet50",
    "model_version": "1",
    "outputs": [{
            "name": "1463",
            "shape": [1, 1000],
            "datatype": "FP32",
            "data": [ ....... ] <1>
        }]
}
----
+
The contents of `.outputs[0].data` were omitted from the example for brevity.

.Verification

. To determine the model's prediction, get the index of the highest element in the `.outputs[0].data` to determine the model's predicted value by using the following Python script:
+
[source,python]
----
import json
with open('response.json') as f:
    response = json.load(f)
data = response["outputs"][0]["data"]
argmax = data.index(max(data))
print(argmax)
----
+
.Example output
[source,text]
----
309
----
+
In this example, the element labeled `309` is the model's response.

. Validate the output against resnet's input data, for example:
+
[source,text]
----
../../../../demos/common/static/images/bee.jpeg 309
----

.Next steps

* Optional. Query the AI model using other images available in the resnet input data.

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-get-model-server-metrics_{context}"]
= Getting the model-server metrics

[role="_abstract"]
After making a query, you can get the model server's metrics to identify bottlenecks, optimize resource allocation, and ensure efficient infrastructure utilization.

[NOTE]
====
You can alternatively configure Open Telemetry for {microshift-short} to get model-server metrics. See "Adding Open Telemetry to an InferenceService custom resource" for more information.
====

.Prerequisites

* {microshift-short} is running.
* There have been enough queries to provide the metrics data you want to see.

.Procedure

* Get the Prometheus-format metrics of the model server by making a request on the `/metrics` endpoint by running the following command:
+
[source,terminal]
----
$ curl "${DOMAIN}/metrics" --connect-to "${DOMAIN}::${IP}:"
----
+
.Partial example output
[source,terminal]
----
# HELP ovms_requests_success Number of successful requests to a model or a DAG.
# TYPE ovms_requests_success counter
ovms_requests_success{api="KServe",interface="REST",method="ModelReady",name="ovms-resnet50"} 4
ovms_requests_success{api="KServe",interface="REST",method="ModelMetadata",name="ovms-resnet50",version="1"} 1
----

// Module included in the following assemblies:
//
// * microshift_ai/microshift-rhoai.adoc

[id="microshift-rhoai-override-kserve-config_{context}"]
= Overriding KServe configuration

[role="_abstract"]
You can override KServe settings to customize your model-serving environment.

Follow the general steps for your operating system.

Option 1::

. Make a copy of the existing `inferenceservice-config` config map file in the `redhat-ods-applications` namespace.

. Edit the settings you want to change.

. Overwrite the existing `ConfigMap` object.

. Restart KServe by either deleting the pod or scaling the `Deployment` pod parameter down to `0` and then back up to `1`.

Option 2::

. Copy the `/usr/lib/microshift/manifests.d/010-microshift-ai-model-serving-kserve/inferenceservice-config-microshift-patch.yaml` config map file.

. Edit the settings you want to change.

. Apply the `ConfigMap` object.

. Restart KServe by either deleting the pod or scaling the `Deployment` pod parameter down to `0` and then back up to `1`.

For {op-system-ostree} and {op-system-image} systems::

. Create a new manifest with the `ConfigMap` file, based on either the `/usr/lib/microshift/manifests.d/010-microshift-ai-model-serving-kserve/inferenceservice-config-microshift-patch.yaml` or `inferenceservice-config` file, in the `redhat-ods-applications` namespace.

. Place the new manifest in the `/usr/lib/microshift/manifests.d/` directory. Staring with prefix `011` is recommended so that your manifest is applied after the `/usr/lib/microshift/manifests.d/010-microshift-ai-model-serving-kserve/` directory contents.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Configuring routes

* Serving models with OCI images (KServe documentation)

* About model serving ({rhoai-full}  documentation)

* Model-serving runtimes ({rhoai-full} documentation)

* Serving models on the single-model serving platform ({rhoai-full} documentation)

* Tested and verified model-serving runtimes ({rhoai-full} documentation)
//the `2-latest` link is not working (2-latest in place of `1`)

* Adding a tested and verified model-serving runtime for the single-model serving platform ({rhoai-full} documentation)

* Serving Runtimes (KServe documentation)

* V1 Inference Protocol (KServe documentation)

* Open Inference Protocol (V2) (KServe documentation)

* InferenceService
