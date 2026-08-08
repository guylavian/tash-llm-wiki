---
title: "Getting started with service binding on {ibm-power-title}, {ibm-z-title}, and {ibm-linuxone-title}"
type: reference
domain: openshift
slug: applications-4-22-getting-started-with-service-binding-ibm-power-ibm-z
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/getting-started-with-service-binding-ibm-power-ibm-z
version: 4.22
family: applications
documentKind: "Documentation"
---

# Getting started with service binding on {ibm-power-title}, {ibm-z-title}, and {ibm-linuxone-title}

[id="getting-started-with-service-binding-ibm-power-ibm-z"]
= Getting started with service binding on {ibm-power-title}, {ibm-z-title}, and {ibm-linuxone-title}

[role="_abstract"]
The {servicebinding-title} manages the data plane for workloads and backing services. This guide provides instructions with examples to help you create a database instance, deploy an application, and use the {servicebinding-title} to create a binding connection between the application and the database service.

// Prerequisites for getting started with Service Binding Operator
[discrete]
== Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have installed the `oc` CLI.
* You have installed the {servicebinding-title} from the software catalog.

//Deploying PostgreSQL operator
[id="sbo-deploying-a-postgresql-operator-instance-power-z_{context}"]
= Deploying a PostgreSQL Operator

.Procedure

. To deploy the Dev4Devs PostgreSQL Operator in the `my-petclinic` namespace run the following command in shell:

[source,terminal]
----
$ oc apply -f - << EOD
---
apiVersion: v1
kind: Namespace
metadata:
  name: my-petclinic
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: postgres-operator-group
  namespace: my-petclinic
---
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: ibm-multiarch-catalog
  namespace: openshift-marketplace
spec:
  sourceType: grpc
  image: quay.io/ibm/operator-registry-<architecture> <1>
  imagePullPolicy: IfNotPresent
  displayName: ibm-multiarch-catalog
  updateStrategy:
    registryPoll:
      interval: 30m
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: postgresql-operator-dev4devs-com
  namespace: openshift-operators
spec:
  channel: alpha
  installPlanApproval: Automatic
  name: postgresql-operator-dev4devs-com
  source: ibm-multiarch-catalog
  sourceNamespace: openshift-marketplace
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: database-view
  labels:
    servicebinding.io/controller: "true"
rules:
  - apiGroups:
      - postgresql.dev4devs.com
    resources:
      - databases
    verbs:
      - get
      - list
EOD
----
<1> The Operator image.
* For {ibm-power-name}: `quay.io/ibm/operator-registry-ppc64le:release-4.9`
* For {ibm-z-name} and {ibm-linuxone-name}: `quay.io/ibm/operator-registry-s390x:release-4.8`

.Verification

. After the operator is installed, list the operator subscriptions in the `openshift-operators` namespace:
+
[source,terminal]
----
$ oc get subs -n openshift-operators
----
+
.Example output
[source,terminal]
----
NAME                               PACKAGE                            SOURCE                  CHANNEL
postgresql-operator-dev4devs-com   postgresql-operator-dev4devs-com   ibm-multiarch-catalog   alpha
rh-service-binding-operator        rh-service-binding-operator        redhat-operators        stable
----

//Creating a PostgreSQL database instance
[id="sbo-creating-a-postgresql-database-instance-power-z_{context}"]
= Creating a PostgreSQL database instance

[role="_abstract"]
To create a PostgreSQL database instance, you must create a `Database` custom resource (CR) and configure the database.

.Procedure

. Create the `Database` CR in the `my-petclinic` namespace by running the following command in shell:
+
[source,terminal]
----
$ oc apply -f - << EOD
apiVersion: postgresql.dev4devs.com/v1alpha1
kind: Database
metadata:
  name: sampledatabase
  namespace: my-petclinic
  annotations:
    host: sampledatabase
    type: postgresql
    port: "5432"
    service.binding/database: 'path={.spec.databaseName}'
    service.binding/port: 'path={.metadata.annotations.port}'
    service.binding/password: 'path={.spec.databasePassword}'
    service.binding/username: 'path={.spec.databaseUser}'
    service.binding/type: 'path={.metadata.annotations.type}'
    service.binding/host: 'path={.metadata.annotations.host}'
spec:
  databaseCpu: 30m
  databaseCpuLimit: 60m
  databaseMemoryLimit: 512Mi
  databaseMemoryRequest: 128Mi
  databaseName: "sampledb"
  databaseNameKeyEnvVar: POSTGRESQL_DATABASE
  databasePassword: "samplepwd"
  databasePasswordKeyEnvVar: POSTGRESQL_PASSWORD
  databaseStorageRequest: 1Gi
  databaseUser: "sampleuser"
  databaseUserKeyEnvVar: POSTGRESQL_USER
  image: registry.redhat.io/rhel8/postgresql-13:latest
  databaseStorageClassName: nfs-storage-provisioner
  size: 1
EOD
----
+
The annotations added in this `Database` CR enable the service binding connection and trigger the Operator reconciliation.
+
The output verifies that the database instance is created:
+
.Example output
[source,terminal]
----
database.postgresql.dev4devs.com/sampledatabase created
----

. After you have created the database instance, ensure that all the pods in the `my-petclinic` namespace are running:
+
[source,terminal]
----
$ oc get pods -n my-petclinic
----
+
The output, which takes a few minutes to display, verifies that the database is created and configured:
+
.Example output
[source,terminal]
----
NAME                                     READY    STATUS      RESTARTS   AGE
sampledatabase-cbc655488-74kss            0/1     Running        0       32s
----

After the database is configured, you can deploy the sample application and connect it to the database service.

//Deploying the Spring PetClinic sample application
[id="sbo-deploying-the-spring-petclinic-sample-application-ibm-power-z_{context}"]
= Deploying the Spring PetClinic sample application

[role="_abstract"]
To deploy the Spring PetClinic sample application on an OpenShift Container Platform cluster, you must use a deployment configuration and configure your local environment to be able to test the application.

[discrete]
.Procedure

. Deploy the `spring-petclinic` application with the `PostgresCluster` custom resource (CR) by running the following command in shell:
+
[source,terminal]
----
$ oc apply -n my-petclinic -f - << EOD
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-petclinic
  labels:
    app: spring-petclinic
spec:
  replicas: 1
  selector:
    matchLabels:
      app: spring-petclinic
  template:
    metadata:
      labels:
        app: spring-petclinic
    spec:
      containers:
        - name: app
          image: quay.io/service-binding/spring-petclinic:latest
          imagePullPolicy: Always
          env:
          - name: SPRING_PROFILES_ACTIVE
            value: postgres
          - name: org.springframework.cloud.bindings.boot.enable
            value: "true"
          ports:
          - name: http
            containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: spring-petclinic
  name: spring-petclinic
spec:
  type: NodePort
  ports:
    - port: 80
      protocol: TCP
      targetPort: 8080
  selector:
    app: spring-petclinic
EOD
----
+
The output verifies that the Spring PetClinic sample application is created and deployed:
+
.Example output
[source,terminal]
----
deployment.apps/spring-petclinic created
service/spring-petclinic created
----
+
[NOTE]
====
If you are deploying the application using *Container images* in the *Developer* perspective of the web console, you must enter the following environment variables under the *Deployment* section of the *Advanced options*:

* Name: SPRING_PROFILES_ACTIVE
* Value: postgres
====

. Verify that the application is not yet connected to the database service by running the following command:

+
[source,terminal]
----
$ oc get pods -n my-petclinic
----
+
It takes take a few minutes until the `CrashLoopBackOff` status is displayed:
+
.Example output
[source,terminal]
----
NAME                                READY   STATUS             RESTARTS      AGE
spring-petclinic-5b4c7999d4-wzdtz   0/1     CrashLoopBackOff   4 (13s ago)   2m25s
----
+
At this stage, the pod fails to start. If you try to interact with the application, it returns errors.

You can now use the {servicebinding-title} to connect the application to the database service.

//Connecting the Spring PetClinic sample application to the PostgreSQL database service
[id="sbo-connecting-spring-petclinic-sample-app-to-postgresql-database-service-ibm-power-z_{context}"]
= Connecting the Spring PetClinic sample application to the PostgreSQL database service

[role="_abstract"]
To connect the sample application to the database service, you must create a `ServiceBinding` custom resource (CR) that triggers the {servicebinding-title} to project the binding data into the application.

[discrete]
.Procedure

. Create a `ServiceBinding` CR to project the binding data:
+
[source,terminal]
----
$ oc apply -n my-petclinic -f - << EOD
---
apiVersion: binding.operators.coreos.com/v1alpha1
kind: ServiceBinding
metadata:
    name: spring-petclinic-pgcluster
spec:
  services: <1>
    - group: postgresql.dev4devs.com
      kind: Database <2>
      name: sampledatabase
      version: v1alpha1
  application: <3>
    name: spring-petclinic
    group: apps
    version: v1
    resource: deployments
EOD
----
<1> Specifies a list of service resources.
<2> The CR of the database.
<3> The sample application that points to a Deployment or any other similar resource with an embedded PodSpec.
+
The output verifies that the `ServiceBinding` CR is created to project the binding data into the sample application.
+
.Example output
[source,terminal]
----
servicebinding.binding.operators.coreos.com/spring-petclinic created
----

. Verify that the request for service binding is successful:
+
[source,terminal]
----
$ oc get servicebindings -n my-petclinic
----
+
.Example output
[source,terminal]
----
NAME                          READY   REASON              AGE
spring-petclinic-postgresql   True    ApplicationsBound   47m
----
+
By default, the values from the binding data of the database service are projected as files into the workload container that runs the sample application. For example, all the values from the Secret resource are projected into the `bindings/spring-petclinic-pgcluster` directory.

. Once this is created, you can go to the topology to see the visual connection.
+
.Connecting spring-petclinic to a sample database
image::img_power.png[]

. Set up the port forwarding from the application port to access the sample application from your local environment:
+
[source,terminal]
----
$ oc port-forward --address 0.0.0.0 svc/spring-petclinic 8080:80 -n my-petclinic
----
+
.Example output
[source,terminal]
----
Forwarding from 0.0.0.0:8080 -> 8080
Handling connection for 8080
----

. Access http://localhost:8080.
+
You can now remotely access the Spring PetClinic sample application at localhost:8080 and see that the application is now connected to the database service.

[role="_additional-resources"]
[id="additional-resources_getting-started-with-service-binding-ibm-power-ibm-z"]
== Additional resources
* Installing Service Binding Operator
* Creating applications using the Developer perspective
* Managing resources from custom resource definitions
