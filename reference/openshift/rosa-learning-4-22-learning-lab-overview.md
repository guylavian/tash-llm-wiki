---
title: "Workshop overview"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-lab-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-lab-overview
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Workshop overview

[id="learning-lab-overview"]
= Workshop overview

[role="_abstract"]
After successfully provisioning your cluster, follow this workshop to deploy an application on it to understand the concepts of deploying and operating container-based applications.

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-lab-overview.adoc
[id="learning-lab-overview-introduction-objectives_{context}"]
= Workshop objectives

[role="_abstract"]
The following details the purpose of this cluster creation workshop.

* Deploy a Node.js-based application by using Source-to-Image (S2I) and Kubernetes deployment objects
* Set up a continuous delivery (CD) pipeline to automatically push source code changes
* Experience self-healing applications
* Explore configuration management through ConfigMaps, secrets, and environment variables
* Use persistent storage to share data across pod restarts
* Explore networking in Kubernetes and applications
* Familiarize yourself with OpenShift Container Platform and Kubernetes functionality
* Automatically scale pods based on loads from the Horizontal Pod Autoscaler (HPA)
//* Use AWS Controllers for Kubernetes (ACK) to deploy and use an S3 bucket

[id="learning-lab-overview-introduction-prereqs_{context}"]
== Prerequisites

* A provisioned OpenShift Container Platform cluster
* The OpenShift command-line interface (CLI)
* A GitHub account
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-lab-overview.adoc
[id="learning-lab-overview-about-ostoy_{context}"]
= About the OSToy application

[role="_abstract"]
OSToy is a Node.js application that deploys to a OpenShift Container Platform cluster to help explore the functionality of Kubernetes.

This application has a user interface where you can:

* Write messages to the log (stdout / stderr)
* Intentionally crash the application to view self-healing
* Toggle a liveness probe and monitor OpenShift behavior
* Read ConfigMaps, secrets, and environment variables
* Read and write files when connected to shared storage
* Check network connectivity, intra-cluster Domain Name System (DNS), and intra-communication with the included microservice
* Increase the load to view automatic scaling of the pods by using the Horizontal Pod Autoscaler (HPA)
//* Connect to an AWS S3 bucket to read and write objects

image::ostoy-arch.png[OSToy architecture diagram]
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-lab-overview.adoc
[id="learning-lab-overview-ui_{context}"]
= Understanding the OSToy UI

[role="_abstract"]
You can explore the different components of the OSToy application by reviewing its architectural breakdown. Understanding this structure prepares you to successfully deploy and manage its microservices.

image::ostoy-homepage.png[Preview of the OSToy homepage]

. Pod name
. *Home:* Application home page
. *Persistent Storage:* Writes data to the persistent volume bound to the application
. *Config Maps:*  Shows ConfigMaps available to the application and the key:value pairs
. *Secrets:* Shows secrets available to the application and the key:value pairs
. *ENV Variables:* Shows environment variables available to the application
. *Networking:* Networking tools
. *Pod Auto Scaling:* Increase the load of the pods and test the Horizontal Pod Autoscaler (HPA)
. *ACK S3:* Integrate with AWS S3 to read and write objects to a bucket
+
. *About:* Application information
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-lab-overview.adoc
[id="learning-lab-overview-lab-resources_{context}"]
= Lab resources

[role="_abstract"]
To successfully complete the lab tutorial, review the provided reference materials. These supporting materials guide you through the required configurations and core concepts.

* OSToy application source code
* OSToy front-end container image
* OSToy microservice container image
* Deployment definition YAML files:
+
`ostoy-frontend-deployment.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ostoy-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ostoy-frontend
  labels:
    app: ostoy
spec:
  selector:
    matchLabels:
      app: ostoy-frontend
  strategy:
    type: Recreate
  replicas: 1
  template:
    metadata:
      labels:
        app: ostoy-frontend
    spec:
      # Uncomment to use with ACK portion of the workshop
      # If you chose a different service account name please replace it.
      # serviceAccount: ostoy-sa
      containers:
      - name: ostoy-frontend
        securityContext:
          allowPrivilegeEscalation: false
          runAsNonRoot: true
          seccompProfile:
            type: RuntimeDefault
          capabilities:
            drop:
            - ALL
        image: quay.io/ostoylab/ostoy-frontend:1.6.0
        imagePullPolicy: IfNotPresent
        ports:
        - name: ostoy-port
          containerPort: 8080
        resources:
          requests:
            memory: "256Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "200m"
        volumeMounts:
        - name: configvol
          mountPath: /var/config
        - name: secretvol
          mountPath: /var/secret
        - name: datavol
          mountPath: /var/demo_files
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
        env:
        - name: ENV_TOY_SECRET
          valueFrom:
            secretKeyRef:
              name: ostoy-secret-env
              key: ENV_TOY_SECRET
        - name: MICROSERVICE_NAME
          value: OSTOY_MICROSERVICE_SVC
        - name: NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
      volumes:
        - name: configvol
          configMap:
            name: ostoy-configmap-files
        - name: secretvol
          secret:
            defaultMode: 420
            secretName: ostoy-secret
        - name: datavol
          persistentVolumeClaim:
            claimName: ostoy-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: ostoy-frontend-svc
  labels:
    app: ostoy-frontend
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: ostoy-port
      protocol: TCP
      name: ostoy
  selector:
    app: ostoy-frontend
---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: ostoy-route
spec:
  to:
    kind: Service
    name: ostoy-frontend-svc
---
apiVersion: v1
kind: Secret
metadata:
  name: ostoy-secret-env
type: Opaque
data:
  ENV_TOY_SECRET: VGhpcyBpcyBhIHRlc3Q=
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: ostoy-configmap-files
data:
  config.json:  '{ "default": "123" }'
---
apiVersion: v1
kind: Secret
metadata:
  name: ostoy-secret
data:
  secret.txt: VVNFUk5BTUU9bXlfdXNlcgpQQVNTV09SRD1AT3RCbCVYQXAhIzYzMlk1RndDQE1UUWsKU01UUD1sb2NhbGhvc3QKU01UUF9QT1JUPTI1
type: Opaque
----
+
`ostoy-microservice-deployment.yaml`:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ostoy-microservice
  labels:
    app: ostoy
spec:
  selector:
    matchLabels:
      app: ostoy-microservice
  replicas: 1
  template:
    metadata:
      labels:
        app: ostoy-microservice
    spec:
      containers:
      - name: ostoy-microservice
        securityContext:
          allowPrivilegeEscalation: false
          runAsNonRoot: true
          seccompProfile:
            type: RuntimeDefault
          capabilities:
            drop:
            - ALL
        image: quay.io/ostoylab/ostoy-microservice:1.5.0
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
          protocol: TCP
        resources:
          requests:
            memory: "128Mi"
            cpu: "50m"
          limits:
            memory: "256Mi"
            cpu: "100m"
---
apiVersion: v1
kind: Service
metadata:
  name: ostoy-microservice-svc
  labels:
    app: ostoy-microservice
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  selector:
    app: ostoy-microservice
----
* S3 bucket manifest for ACK S3
+
`s3-bucket.yaml`:
+
[source,yaml]
----
apiVersion: s3.services.k8s.aws/v1alpha1
kind: Bucket
metadata:
  name: ostoy-bucket
  namespace: ostoy
spec:
  name: ostoy-bucket
----

[NOTE]
====
To simplify deployment of the OSToy application, all of the objects required in the above deployment manifests are grouped together. For a typical enterprise deployment, a separate manifest file for each Kubernetes object is recommended.
====
