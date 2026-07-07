---
title: "Binding workloads using Service Binding Operator"
type: reference
domain: openshift
slug: applications-4-22-binding-workloads-using-sbo
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/binding-workloads-using-sbo
version: 4.22
family: applications
documentKind: "Documentation"
---

# Binding workloads using Service Binding Operator

[id="binding-workloads-using-sbo"]
= Binding workloads using Service Binding Operator

Application developers must bind a workload to one or more backing services by using a binding secret. This secret is generated for the purpose of storing information to be consumed by the workload.

As an example, consider that the service you want to connect to is already exposing the binding data. In this case, you would also need a workload to be used along with the `ServiceBinding` custom resource (CR). By using this `ServiceBinding` CR, the workload sends a binding request with the details of the services to bind with.

.Example of `ServiceBinding` CR
[source,yaml]
----
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
    name: spring-petclinic-pgcluster
    namespace: my-petclinic
spec:
    services: <1>
    - group: postgres-operator.crunchydata.com
      version: v1beta1
      kind: PostgresCluster
      name: hippo
    application: <2>
      name: spring-petclinic
      group: apps
      version: v1
      resource: deployments
----
<1> Specifies a list of service resources.
<2> The sample application that points to a Deployment or any other similar resource with an embedded PodSpec.

As shown in the previous example, you can also directly use a `ConfigMap` or a `Secret` itself as a service resource to be used as a source of binding data.

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/binding-workloads-using-sbo.adoc

[id="sbo-naming-strategies_{context}"]
= Naming strategies

[role="_abstract"]
Naming strategies are available only for the `binding.operators.coreos.com` API group.

Naming strategies use Go templates to help you define custom binding names through the service binding request. Naming strategies apply for all attributes including the mappings in the `ServiceBinding` custom resource (CR).

A backing service projects the binding names as files or environment variables into the workload. If a workload expects the projected binding names in a particular format, but the binding names to be projected from the backing service are not available in that format, then you can change the binding names using naming strategies.

.Predefined post-processing functions
While using naming strategies, depending on the expectations or requirements of your workload, you can use the following predefined post-processing functions in any combination to convert the character strings:

* `upper`: Converts the character strings into capital or uppercase letters.
* `lower`: Converts the character strings into lowercase letters.
* `title`: Converts the character strings where the first letter of each word is capitalized except for certain minor words.

.Predefined naming strategies
// Binding names declared through annotations or Operator Lifecycle Manager (OLM) descriptors are processed for their name change before their projection into the workload according to the following predefined naming strategies:
// When the OLM descriptors are supported again, add this sentence.

Binding names declared through annotations are processed for their name change before their projection into the workload according to the following predefined naming strategies:

* `none`: When applied, there are no changes in the binding names.
+
.Example
After the template compilation, the binding names take the `{{ .name }}` form.
+
[source,yaml]
----
host: hippo-pgbouncer
port: 5432
----

* `upper`: Applied when no `namingStrategy` is defined. When applied, converts all the character strings of the binding name key into capital or uppercase letters.
+
.Example
After the template compilation, the binding names take the `{{ .service.kind | upper}}_{{ .name | upper }}` form.
+
[source,yaml]
----
DATABASE_HOST: hippo-pgbouncer
DATABASE_PORT: 5432
----
+
If your workload requires a different format, you can define a custom naming strategy and change the binding name using a prefix and a separator, for example, `PORT_DATABASE`.

[NOTE]
====
* When the binding names are projected as files, by default the predefined `none` naming strategy is applied, and the binding names do not change.
* When the binding names are projected as environment variables and no `namingStrategy` is defined, by default the predefined `uppercase` naming strategy is applied.
* You can override the predefined naming strategies by defining custom naming strategies using different combinations of custom binding names and predefined post-processing functions.
====

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/binding-workloads-using-sbo.adoc

[id="sbo-advanced-binding-options_{context}"]
= Advanced binding options

You can define the `ServiceBinding` custom resource (CR) to use the following advanced binding options:

* Changing binding names: This option is available only for the `binding.operators.coreos.com` API group.
* Composing custom binding data: This option is available only for the `binding.operators.coreos.com` API group.
* Binding workloads using label selectors: This option is available for both the `binding.operators.coreos.com` and `servicebinding.io` API groups.

[id="changing-binding-names_{context}"]
== Changing the binding names before projecting them into the workload
You can specify the rules to change the binding names in the `.spec.namingStrategy` attribute of the `ServiceBinding` CR. For example, consider a Spring PetClinic sample application that connects to the PostgreSQL database. In this case, the PostgreSQL database service exposes the `host` and `port` fields of the database to use for binding. The Spring PetClinic sample application can access this exposed binding data through the binding names.

.Example: Spring PetClinic sample application in the `ServiceBinding` CR
[source,yaml]
----
# ...
    application:
      name: spring-petclinic
      group: apps
      version: v1
      resource: deployments
# ...
----

.Example: PostgreSQL database service in the `ServiceBinding` CR
[source,yaml]
----
# ...
    services:
    - group: postgres-operator.crunchydata.com
      version: v1beta1
      kind: PostgresCluster
      name: hippo
# ...
----

If `namingStrategy` is not defined and the binding names are projected as environment variables, then the `host: hippo-pgbouncer` value in the backing service and the projected environment variable would appear as shown in the following example:

.Example
[source,yaml]
----
DATABASE_HOST: hippo-pgbouncer
----
where:
[horizontal]
`DATABASE`:: Specifies the `kind` backend service.
`HOST`:: Specifies the binding name.

After applying the `POSTGRESQL_{{ .service.kind | upper }}_{{ .name | upper }}_ENV` naming strategy, the  list of custom binding names prepared by the service binding request appears as shown in the following example:

.Example
[source,yaml]
----
POSTGRESQL_DATABASE_HOST_ENV: hippo-pgbouncer
POSTGRESQL_DATABASE_PORT_ENV: 5432
----

The following items describe the expressions defined in the `POSTGRESQL_{{ .service.kind | upper }}_{{ .name | upper }}_ENV` naming strategy:

* `.name`: Refers to the binding name exposed by the backing service. In the previous example, the binding names are `HOST` and `PORT`.
* `.service.kind`: Refers to the kind of service resource whose binding names are changed with the naming strategy.
* `upper`: String function used to post-process the character string while compiling the Go template string.
* `POSTGRESQL`: Prefix of the custom binding name.
* `ENV`: Suffix of the custom binding name.

Similar to the previous example, you can define the string templates in `namingStrategy` to define how each key of the binding names should be prepared by the service binding request.

[id="composing-custom-binding-data_{context}"]
== Composing custom binding data
As an application developer, you can compose custom binding data under the following circumstances:

* The backing service does not expose binding data.
* The values exposed are not available in the required format as expected by the workload.

For example, consider a case where the backing service CR exposes the host, port, and database user as binding data, but the workload requires that the binding data be consumed as a connection string.
You can compose custom binding data using attributes in the Kubernetes resource representing the backing service.

.Example
[source,yaml]
----
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
    name: spring-petclinic-pgcluster
    namespace: my-petclinic
spec:
    services:
    - group: postgres-operator.crunchydata.com
      version: v1beta1
      kind: PostgresCluster
      name: hippo <1>
      id: postgresDB <2>
    - group: ""
      version: v1
      kind: Secret
      name: hippo-pguser-hippo
      id: postgresSecret
    application:
      name: spring-petclinic
      group: apps
      version: v1
      resource: deployments
    mappings:
      ## From the database service
      - name: JDBC_URL
        value: 'jdbc:postgresql://{{ .postgresDB.metadata.annotations.proxy }}:{{ .postgresDB.spec.port }}/{{ .postgresDB.metadata.name }}'
      ## From both the services!
      - name: CREDENTIALS
        value: '{{ .postgresDB.metadata.name }}{{ translationService.postgresSecret.data.password }}'
      ## Generate JSON
      - name: DB_JSON <3>
        value: {{ json .postgresDB.status }} <4>
----
<1> Name of the backing service resource.
<2> Optional identifier.
<3> The JSON name that the {servicebinding-title} generates. The {servicebinding-title} projects this JSON name as the name of a file or environment variable.
<4> The JSON value that the {servicebinding-title} generates. The {servicebinding-title} projects this JSON value as a file or environment variable. The JSON value contains the attributes from your specified field of the backing service custom resource.

[id="binding-workloads-using-a-label-selector_{context}"]
== Binding workloads using a label selector
You can use a label selector to specify the workload to bind. If you declare a service binding using the label selectors to pick up workloads, the {servicebinding-title} periodically attempts to find and bind new workloads that match the given label selector.

For example, as a cluster administrator, you can bind a service to every `Deployment` in a namespace with the `environment: production` label by setting an appropriate `labelSelector` field in the `ServiceBinding` CR. This enables the {servicebinding-title} to bind each of these workloads with one `ServiceBinding` CR.

.Example `ServiceBinding` CR in the `binding.operators.coreos.com/v1alpha1` API
[source,yaml]
----
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
  name: multi-application-binding
  namespace: service-binding-demo
spec:
  application:
    labelSelector: <1>
      matchLabels:
        environment: production
    group: apps
    version: v1
    resource: deployments
  services:
    group: ""
    version: v1
    kind: Secret
    name: super-secret-data
----
<1> Specifies the workload that is being bound.

.Example `ServiceBinding` CR in the `servicebinding.io` API
[source,yaml]
----
apiVersion: servicebindings.io/v1beta1
kind: ServiceBinding
metadata:
  name: multi-application-binding
  namespace: service-binding-demo
spec:
  workload:
    selector: <1>
      matchLabels:
        environment: production
    apiVersion: app/v1
    kind: Deployment
  service:
    apiVersion: v1
    kind: Secret
    name: super-secret-data
----
<1> Specifies the workload that is being bound.

[IMPORTANT]
====
If you define the following pairs of fields, {servicebinding-title} refuses the binding operation and generates an error:

* The `name` and `labelSelector` fields in the `binding.operators.coreos.com/v1alpha1` API.
* The `name` and `selector` fields in the `servicebinding.io` API (Spec API).
====

.Understanding the rebinding behavior
Consider a case where, after a successful binding, you use the `name` field to identify a workload. If you delete and recreate that workload, the `ServiceBinding` reconciler does not rebind the workload, and the Operator cannot project the binding data to the workload. However, if you use the `labelSelector` field to identify a workload, the `ServiceBinding` reconciler rebinds the workload, and the Operator projects the binding data.

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/binding-workloads-using-sbo.adoc

[id="sbo-binding-workloads-that-are-not-compliant-with-PodSpec_{context}"]
= Binding secondary workloads that are not compliant with PodSpec

A typical scenario in service binding involves configuring the backing service, the workload (Deployment), and {servicebinding-title}. Consider a scenario that involves a secondary workload (which can also be an application Operator) that is not compliant with PodSpec and is between the primary workload (Deployment) and {servicebinding-title}.

For such secondary workload resources, the location of the container path is arbitrary. For service binding, if the secondary workload in a CR is not compliant with the PodSpec, you must specify the location of the container path. Doing so projects the binding data into the container path specified in the secondary workload of the `ServiceBinding` custom resource (CR), for example, when you do not want the binding data inside a pod.

In {servicebinding-title}, you can configure the path of where containers or secrets reside within a workload and bind these paths at a custom location.

[id="configuring-custom-location-of-container-path_{context}"]
== Configuring the custom location of the container path
This custom location is available for the `binding.operators.coreos.com` API group when {servicebinding-title} projects the binding data as environment variables.

Consider a secondary workload CR, which is not compliant with the PodSpec and has containers located at the `spec.containers` path:

.Example: Secondary workload CR
[source,yaml]
----
apiVersion: "operator.sbo.com/v1"
kind: SecondaryWorkload
metadata:
    name: secondary-workload
spec:
    containers:
    - name: hello-world
      image: quay.io/baijum/secondary-workload:latest
      ports:
      - containerPort: 8080
----

[discrete]
.Procedure
* Configure the `spec.containers` path by specifying a value in the `ServiceBinding` CR and bind this path to a `spec.application.bindingPath.containersPath` custom location:
+
.Example: `ServiceBinding` CR with the `spec.containers` path in a custom location
[source,yaml]
----
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
    name: spring-petclinic-pgcluster
spec:
    services:
    - group: postgres-operator.crunchydata.com
      version: v1beta1
      kind: PostgresCluster
      name: hippo
      id: postgresDB
    - group: ""
      version: v1
      kind: Secret
      name: hippo-pguser-hippo
      id: postgresSecret
    application: <1>
      name: spring-petclinic
      group: apps
      version: v1
      resource: deployments
    application: <2>
      name: secondary-workload
      group: operator.sbo.com
      version: v1
      resource: secondaryworkloads
      bindingPath:
        containersPath: spec.containers <3>
----
<1> The sample application that points to a Deployment or any other similar resource with an embedded PodSpec.
<2> The secondary workload, which is not compliant with the PodSpec.
<3> The custom location of the container path.

After you specify the location of the container path, {servicebinding-title} generates the binding data, which becomes available in the container path specified in the secondary workload of the `ServiceBinding` CR.

The following example shows the `spec.containers` path with the `envFrom` and `secretRef` fields:

.Example: Secondary workload CR with the `envFrom` and `secretRef` fields
[source,yaml]
----
apiVersion: "operator.sbo.com/v1"
kind: SecondaryWorkload
metadata:
    name: secondary-workload
spec:
    containers:
    - env: <1>
      - name: ServiceBindingOperatorChangeTriggerEnvVar
        value: "31793"
      envFrom:
      - secretRef:
          name: secret-resource-name <2>
      image: quay.io/baijum/secondary-workload:latest
      name: hello-world
      ports:
      - containerPort: 8080
      resources: {}
----
<1> Unique array of containers with values generated by the {servicebinding-title}. These values are based on the backing service CR.
<2> Name of the `Secret` resource generated by the {servicebinding-title}.

[id="configuring-custom-location-of-secret-path_{context}"]
== Configuring the custom location of the secret path
This custom location is available for the `binding.operators.coreos.com` API group when {servicebinding-title} projects the binding data as environment variables.

Consider a secondary workload CR, which is not compliant with the PodSpec, with only the secret at the `spec.secret` path:

.Example: Secondary workload CR
[source,yaml]
----
apiVersion: "operator.sbo.com/v1"
kind: SecondaryWorkload
metadata:
    name: secondary-workload
spec:
    secret: ""
----

[discrete]
.Procedure
* Configure the `spec.secret` path by specifying a value in the `ServiceBinding` CR and bind this path at a `spec.application.bindingPath.secretPath` custom location:
+
.Example: `ServiceBinding` CR with the `spec.secret` path in a custom location
[source,yaml]
----
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
    name: spring-petclinic-pgcluster
spec:
...
    application: <1>
      name: secondary-workload
      group: operator.sbo.com
      version: v1
      resource: secondaryworkloads
      bindingPath:
        secretPath: spec.secret <2>
...
----
<1> The secondary workload, which is not compliant with the PodSpec.
<2> The custom location of the secret path that contains the name of the `Secret` resource.

After you specify the location of the secret path, {servicebinding-title} generates the binding data, which becomes available in the secret path specified in the secondary workload of the `ServiceBinding` CR.

The following example shows the `spec.secret` path with the `binding-request` value:

.Example: Secondary workload CR with the `binding-request` value
[source,yaml]
----
...
apiVersion: "operator.sbo.com/v1"
kind: SecondaryWorkload
metadata:
    name: secondary-workload
spec:
    secret: binding-request-72ddc0c540ab3a290e138726940591debf14c581 <1>
...
----
<1> The unique name of the `Secret` resource that {servicebinding-title} generates.

[id="workload-resource-mapping_{context}"]
== Workload resource mapping

[NOTE]
====
* Workload resource mapping is available for the secondary workloads of the `ServiceBinding` custom resource (CR) for both the API groups: `binding.operators.coreos.com` and `servicebinding.io`.
* You must define `ClusterWorkloadResourceMapping` resources only under the `servicebinding.io` API group. However, the `ClusterWorkloadResourceMapping` resources interact with `ServiceBinding` resources under both the `binding.operators.coreos.com` and `servicebinding.io` API groups.
====

If you cannot configure custom path locations by using the configuration method for container path, you can define exactly where binding data needs to be projected. Specify where to project the binding data for a given workload kind by defining the `ClusterWorkloadResourceMapping` resources in the `servicebinding.io` API group.

The following example shows how to define a mapping for the `CronJob.batch/v1` resources.

.Example: Mapping for `CronJob.batch/v1` resources
[source,yaml]
----
apiVersion: servicebinding.io/v1beta1
kind: ClusterWorkloadResourceMapping
metadata:
 name: cronjobs.batch <1>
spec:
  versions:
  - version: "v1" <2>
    annotations: .spec.jobTemplate.spec.template.metadata.annotations <3>
    containers:
    - path: .spec.jobTemplate.spec.template.spec.containers[*] <4>
    - path: .spec.jobTemplate.spec.template.spec.initContainers[*]
      name: .name <5>
      env: .env <6>
      volumeMounts: .volumeMounts <7>
    volumes: .spec.jobTemplate.spec.template.spec.volumes <8>
----
<1> Name of the `ClusterWorkloadResourceMapping` resource, which must be qualified as the `plural.group` of the mapped workload resource.
<2> Version of the resource that is being mapped.  Any version that is not specified can be matched with the "*" wildcard.
<3> Optional: Identifier of the `.annotations` field in a pod, specified with a fixed JSONPath.  The default value is `.spec.template.spec.annotations`.
<4> Identifier of the `.containers` and `.initContainers` fields in a pod, specified with a JSONPath. If no entries under the `containers` field are defined, the {servicebinding-title} defaults to two paths: `.spec.template.spec.containers[\*]` and `.spec.template.spec.initContainers[\*]`, with all other fields set as their default. However, if you specify an entry, then you must define the `.path` field.
<5> Optional: Identifier of the `.name` field in a container, specified with a fixed JSONPath. The default value is `.name`.
<6> Optional: Identifier of the `.env` field in a container, specified with a fixed JSONPath. The default value is `.env`.
<7> Optional: Identifier of the `.volumeMounts` field in a container, specified with a fixed JSONPath. The default value is `.volumeMounts`.
<8> Optional: Identifier of the `.volumes` field in a pod, specified with a fixed JSONPath. The default value is `.spec.template.spec.volumes`.

[IMPORTANT]
====
* In this context, a fixed JSONPath is a subset of the JSONPath grammar that accepts only the following operations:
+
--
** Field lookup: `.spec.template`
** Array indexing: `.spec['template']`
--
+
All other operations are not accepted.

* Most of these fields are optional. When they are not specified, the {servicebinding-title} assumes defaults compatible with `PodSpec` resources.
* The {servicebinding-title} requires that each of these fields is structurally equivalent to the corresponding field in a pod deployment. For example, the contents of the `.env` field in a workload resource must be able to accept the same structure of data that the `.env` field in a Pod resource would. Otherwise, projecting binding data into such a workload might result in unexpected behavior from the {servicebinding-title}.
====

.Behavior specific to the `binding.operators.coreos.com` API group
You can expect the following behaviors when `ClusterWorkloadResourceMapping` resources interact with `ServiceBinding` resources under the `binding.operators.coreos.com` API group:

* If a `ServiceBinding` resource with the `bindAsFiles: false` flag value is created together with one of these mappings, then environment variables are projected into the `.envFrom` field underneath each `path` field specified in the corresponding `ClusterWorkloadResourceMapping` resource.
* As a cluster administrator, you can specify both a `ClusterWorkloadResourceMapping` resource and the `.spec.application.bindingPath.containersPath` field in a `ServiceBinding.bindings.coreos.com` resource for binding purposes.
+
The {servicebinding-title} attempts to project binding data into the locations specified in both a `ClusterWorkloadResourceMapping` resource and the `.spec.application.bindingPath.containersPath` field. This behavior is equivalent to adding a container entry to the corresponding `ClusterWorkloadResourceMapping` resource with the `path: $containersPath` attribute, with all other values taking their default value.

// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/binding-workloads-using-sbo.adoc

[id="sbo-unbinding-workloads-from-a-backing-service_{context}"]
= Unbinding workloads from a backing service

[role="_abstract"]
You can unbind a workload from a backing service by using the `oc` tool.

* To unbind a workload from a backing service, delete the `ServiceBinding` custom resource (CR) linked to it:
+
[source,terminal]
----
$ oc delete ServiceBinding <.metadata.name>
----
+
.Example
[source,terminal]
----
$ oc delete ServiceBinding spring-petclinic-pgcluster
----
where:
[horizontal]
`spring-petclinic-pgcluster`:: Specifies the name of the `ServiceBinding` CR.

[role="_additional-resources"]
[id="additional-resources_binding-workloads-sbo"]
== Additional resources
* Binding a workload together with a backing service.
* Connecting the Spring PetClinic sample application to the PostgreSQL database service.
* Creating custom resources from a file
* Example schema of the ClusterWorkloadResourceMapping resource.
