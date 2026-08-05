---
title: "Providing sensitive data to pods by using an external secrets store"
type: reference
domain: openshift
slug: nodes-4-22-nodes-pods-secrets-store
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-pods-secrets-store
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Providing sensitive data to pods by using an external secrets store

[id="nodes-pods-secrets-store"]
= Providing sensitive data to pods by using an external secrets store

[role="_abstract"]
As an alternative to using `secret` objects to provide sensitive information, such as passwords and user names, to applications, you can use an external secret management system to store the information. You can then use the {secrets-store-operator} to access the information and mount the secret content as a pod volume. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

// About the {secrets-store-operator}
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-secrets-store.adoc
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="persistent-storage-csi-secrets-store-driver-overview_{context}"]
= Overview

= About the {secrets-store-operator}

[role="_abstract"]
To store and manage your secrets securely, you can configure the OpenShift Container Platform {secrets-store-operator} to mount secrets from an external secret management system, such as Azure Key Vault, by using a provider plugin. Applications can then use the secret, but the secret does not persist on the system after the application pod is destroyed.

Secret objects are stored with Base64 encoding. etcd provides encryption at rest for these secrets, but when secrets are retrieved, they are decrypted and presented to the user. If role-based access control is not configured properly on your cluster, anyone with API or etcd access can retrieve or modify a secret. Additionally, anyone who is authorized to create a pod in a namespace can use that access to read any secret in that namespace.

The {secrets-store-operator}, `secrets-store.csi.k8s.io`, enables OpenShift Container Platform to mount multiple secrets, keys, and certificates stored in enterprise-grade external secrets stores into pods as a volume. The {secrets-store-operator} communicates with the provider using gRPC to fetch the mount contents from the specified external secrets store. After the volume is attached, the data in it is mounted into the container's file system. Secrets store volumes are mounted in-line.

// Secrets store providers
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-providers_{context}"]
= Secrets store providers

[role="_abstract"]
You can store sensitive information needed by your applications in an external secret management system and use the {secrets-store-operator} to mount the secret content as a pod volume. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

The {secrets-store-operator} has been tested with the following secrets store providers:

* AWS Secrets Manager
* AWS Systems Manager Parameter Store
* Azure Key Vault
* Google Secret Manager
* HashiCorp Vault

[IMPORTANT]
====
{ibm-z-title} supports only HashiCorp Vault.
====

[NOTE]
====
Red{nbsp}Hat does not test all factors associated with third-party secrets store provider functionality. For more information about third-party support, see the "Red{nbsp}Hat third-party support policy".
====

// Automatic rotation
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-auto-rotation_{context}"]
= Automatic rotation

[role="_abstract"]
To maintain synchronization with your external secret provider, the {secrets-store-operator} automatically rotates secret content in mounted volumes. The {secrets-store-operator} uses this process to ensure that updates in the external store are automatically reflected in your pods and secrets.

If you enabled synchronization of mounted content as Kubernetes secrets, the Kubernetes secrets are also rotated.

Applications consuming the secret data must watch for updates to the secrets.

// Installing the {secrets-store-driver}
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-secrets-store.adoc
//

[id="persistent-storage-csi-secrets-store-driver-install_{context}"]
= Installing the {secrets-store-driver}

[role="_abstract"]
You can use the OpenShift Container Platform web console to install the {secrets-store-driver}.

.Prerequisites
* Access to the OpenShift Container Platform web console.

* Administrator access to the cluster.

.Procedure

. Install the {secrets-store-operator}:
.. Log in to the web console.
.. Click *Ecosystem* -> *Software Catalog*.
.. Locate the {secrets-store-operator} by typing "Secrets Store CSI" in the filter box.
.. Click the *Secrets Store CSI Driver Operator* button.
.. On the *Secrets Store CSI Driver Operator* page, click *Install*.
.. On the *Install Operator* page, ensure that:
+
* *All namespaces on the cluster (default)* is selected.

* *Installed Namespace* is set to *openshift-cluster-csi-drivers*.
.. Click *Install*.
+
After the installation finishes, the {secrets-store-operator} is listed in the *Installed Operators* section of the web console.

. Create the `ClusterCSIDriver` instance for the driver (`secrets-store.csi.k8s.io`):
.. Click *Administration* -> *CustomResourceDefinitions* -> *ClusterCSIDriver*.
.. On the *Instances* tab, click *Create ClusterCSIDriver*.
+
Use the following YAML file:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: ClusterCSIDriver
metadata:
    name: secrets-store.csi.k8s.io
spec:
  managementState: Managed
----
.. Click *Create*.

// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc
//
// IMPORTANT: This file requires you to define :secrets-store-provider: before including this module.

[id="mounting-secrets-external-secrets-store_{context}"]
= Mounting secrets from an external secrets store to a CSI volume

[role="_abstract"]
After installing the {secrets-store-operator}, you can mount secrets from your external secret store. Using an external secret store protects information that you do not want developers to have and can be more secure than secret objects.

The {secrets-store-operator} has been tested with the following secrets store providers:

* AWS Secrets Manager
* AWS Systems Manager Parameter Store
* Azure Key Vault
* Google Secret Manager
* HashiCorp Vault

// Mounting secrets from AWS Secrets Manager
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc
//
// IMPORTANT: This file requires you to define :secrets-store-provider: before including this module.

[id="secrets-store-aws_{context}"]
= Mounting secrets from {secrets-store-provider}

[role="_abstract"]
You can use the {secrets-store-operator} to mount secrets from {secrets-store-provider} external secrets store to a Container Storage Interface (CSI) volume in OpenShift Container Platform. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the `jq` tool.
* You have extracted and prepared the `ccoctl` utility.
* You have installed the cluster on {aws-first} and the cluster uses {aws-short} Security Token Service (STS).
* You have installed the {secrets-store-operator}. For more information, see "Installing the {secrets-store-driver}".
* You have configured {secrets-store-provider} to store the required secrets.

.Procedure

. Install the {secrets-store-provider} provider:

.. Create a YAML file by using the following example configuration:
+
[IMPORTANT]
====
The {secrets-store-provider} provider for the {secrets-store-driver} is an upstream provider.

This configuration is modified from the configuration provided in the upstream AWS documentation so that it works properly with OpenShift Container Platform. Changes to this configuration might impact functionality.
====
+
.Example `aws-provider.yaml` file
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: csi-secrets-store-provider-aws
  namespace: openshift-cluster-csi-drivers
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: csi-secrets-store-provider-aws-cluster-role
rules:
- apiGroups: [""]
  resources: ["serviceaccounts/token"]
  verbs: ["create"]
- apiGroups: [""]
  resources: ["serviceaccounts"]
  verbs: ["get"]
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: csi-secrets-store-provider-aws-cluster-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: csi-secrets-store-provider-aws-cluster-role
subjects:
- kind: ServiceAccount
  name: csi-secrets-store-provider-aws
  namespace: openshift-cluster-csi-drivers
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  namespace: openshift-cluster-csi-drivers
  name: csi-secrets-store-provider-aws
  labels:
    app: csi-secrets-store-provider-aws
spec:
  updateStrategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: csi-secrets-store-provider-aws
  template:
    metadata:
      labels:
        app: csi-secrets-store-provider-aws
    spec:
      serviceAccountName: csi-secrets-store-provider-aws
      hostNetwork: false
      containers:
        - name: provider-aws-installer
          image: public.ecr.aws/aws-secrets-manager/secrets-store-csi-driver-provider-aws:1.0.r2-50-g5b4aca1-2023.06.09.21.19
          imagePullPolicy: Always
          args:
              - --provider-volume=/etc/kubernetes/secrets-store-csi-providers
          resources:
            requests:
              cpu: 50m
              memory: 100Mi
            limits:
              cpu: 50m
              memory: 100Mi
          securityContext:
            privileged: true
          volumeMounts:
            - mountPath: "/etc/kubernetes/secrets-store-csi-providers"
              name: providervol
            - name: mountpoint-dir
              mountPath: /var/lib/kubelet/pods
              mountPropagation: HostToContainer
      tolerations:
      - operator: Exists
      volumes:
        - name: providervol
          hostPath:
            path: "/etc/kubernetes/secrets-store-csi-providers"
        - name: mountpoint-dir
          hostPath:
            path: /var/lib/kubelet/pods
            type: DirectoryOrCreate
      nodeSelector:
        kubernetes.io/os: linux
----

.. Grant privileged access to the `csi-secrets-store-provider-aws` service account by running the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user privileged -z csi-secrets-store-provider-aws -n openshift-cluster-csi-drivers
----

.. Create the provider resources by running the following command:
+
[source,terminal]
----
$ oc apply -f aws-provider.yaml
----

. Grant the read permission to the service account for the AWS secret object:

.. Create a directory to contain the credentials request by running the following command:
+
[source,terminal]
----
$ mkdir <aws_creds_directory_name>
----

.. Create a YAML file that defines the `CredentialsRequest` resource configuration. See the following example configuration:
+
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: aws-creds-request
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - action:
      - "secretsmanager:GetSecretValue"
      - "secretsmanager:DescribeSecret"
      effect: Allow
      resource: "arn:*:secretsmanager:*:*:secret:testSecret-??????"
    statementEntries:
    - action:
      - "ssm:GetParameter"
      - "ssm:GetParameters"
      effect: Allow
      resource: "arn:*:ssm:*:*:parameter/testParameter*"
  secretRef:
    name: aws-creds
    namespace: my-namespace
  serviceAccountNames:
  - <service_account_name>
----

.. Retrieve the OpenID Connect (OIDC) provider by running the following command:
+
[source,terminal]
----
$ oc get --raw=/.well-known/openid-configuration | jq -r '.issuer'
----
+
.Example output
[source,terminal]
----
https://<oidc_provider_name>
----
Copy the OIDC provider name `<oidc_provider_name>` from the output to use in the next step.

.. Use the `ccoctl` tool to process the credentials request by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-iam-roles \
    --name my-role --region=<aws_region> \
    --credentials-requests-dir=<aws_creds_dir_name> \
    --identity-provider-arn arn:aws:iam::<aws_account_id>:oidc-provider/<oidc_provider_name> --output-dir=<output_dir_name>
----
+
.Example output
[source,terminal]
----
2023/05/15 18:10:34 Role arn:aws:iam::<aws_account_id>:role/my-role-my-namespace-aws-creds created
2023/05/15 18:10:34 Saved credentials configuration to: credrequests-ccoctl-output/manifests/my-namespace-aws-creds-credentials.yaml
2023/05/15 18:10:35 Updated Role policy for Role my-role-my-namespace-aws-creds
----
+
Copy the `<aws_role_arn>` from the output to use in the next step. For example, `arn:aws:iam::<aws_account_id>:role/my-role-my-namespace-aws-creds`.

.. Bind the service account with the role ARN by running the following command:
+
[source,terminal]
----
$ oc annotate -n my-namespace sa/aws-provider eks.amazonaws.com/role-arn="<aws_role_arn>"
----

. Create a secret provider class to define your secrets store provider:

.. Create a YAML file that defines the `SecretProviderClass` object:
+
.Example `secret-provider-class-aws.yaml`
[source,yaml]
----
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-aws-provider
  namespace: my-namespace
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "testSecret"
        objectType: "secretsmanager"
    objects: |
      - objectName: "testParameter"
        objectType: "ssmparameter"
----
where:

`metadata.name`:: Specifies the name for the secret provider class.
`metadata.namespace`:: Specifies the namespace for the secret provider class.
`spec.provider`:: Specifies the provider as `aws`.
`spec.parameters`:: Specifies the provider-specific configuration parameters.

.. Create the `SecretProviderClass` object by running the following command:
+
[source,terminal]
----
$ oc create -f secret-provider-class-aws.yaml
----

. Create a deployment to use this secret provider class:

.. Create a YAML file that defines the `Deployment` object:
+
.Example `deployment.yaml`
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-aws-deployment
  namespace: my-namespace
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-storage
  template:
    metadata:
      labels:
        app: my-storage
    spec:
      serviceAccountName: aws-provider
      containers:
      - name: busybox
        image: k8s.gcr.io/e2e-test-images/busybox:1.29
        command:
          - "/bin/sleep"
          - "10000"
        volumeMounts:
        - name: secrets-store-inline
          mountPath: "/mnt/secrets-store"
          readOnly: true
      volumes:
        - name: secrets-store-inline
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: "my-aws-provider"
----
where:

`metadata.name`:: Specifies the name for the deployment.
`metadata.namespace`:: Specifies the namespace for the deployment. This must be the same namespace as the secret provider class.
`spec.template.spec.volumes.csi.volumeAttributes.secretProviderClass`:: Specifies the name of the secret provider class.

.. Create the `Deployment` object by running the following command:
+
[source,terminal]
----
$ oc create -f deployment.yaml
----

.Verification

* Verify that you can access the secrets from {secrets-store-provider} in the pod volume mount:

.. List the secrets in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec my-aws-deployment-<hash> -n my-namespace -- ls /mnt/secrets-store/
----
+
.Example output
[source,terminal]
----
testSecret
testParameter
----

.. View a secret in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec my-aws-deployment-<hash> -n my-namespace -- cat /mnt/secrets-store/testSecret
----
+
.Example output
[source,terminal]
----
<secret_value>
----

// --- START OF CONTEXT CHANGE ---
// Setting a unique context for including the secrets-store-aws.adoc module a second time in this assembly

// Mounting secrets from AWS Systems Manager Parameter Store

// Resetting the context back to original context
// --- END OF CONTEXT CHANGE ---

// Mounting secrets from Azure Key Vault
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-azure_{context}"]
= Mounting secrets from {azure-short} Key Vault

[role="_abstract"]
You can use the {secrets-store-operator} to mount secrets from {azure-first} Key Vault to a Container Storage Interface (CSI) volume in OpenShift Container Platform. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

.Prerequisites

* Your have installed a cluster on {azure-short}.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {azure-short} CLI (`az`).
* You have installed the {secrets-store-operator}. See "Installing the {secrets-store-driver}" for instructions.
* You have configured {azure-short} Key Vault to store the required secrets.

.Procedure

. Install the {azure-short} Key Vault provider:

.. Create a YAML file named `azure-provider.yaml` that defines the `ServiceAccount` resource configuration. See the following example configuration:
+
[IMPORTANT]
====
The {azure-short} Key Vault provider for the {secrets-store-driver} is an upstream provider.

This configuration is modified from the configuration provided in the upstream {azure-short} documentation so that it works properly with OpenShift Container Platform. Changes to this configuration might impact functionality.
====
+
.Example `azure-provider.yaml` file
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: csi-secrets-store-provider-azure
  namespace: openshift-cluster-csi-drivers
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: csi-secrets-store-provider-azure-cluster-role
rules:
- apiGroups: [""]
  resources: ["serviceaccounts/token"]
  verbs: ["create"]
- apiGroups: [""]
  resources: ["serviceaccounts"]
  verbs: ["get"]
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: csi-secrets-store-provider-azure-cluster-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: csi-secrets-store-provider-azure-cluster-role
subjects:
- kind: ServiceAccount
  name: csi-secrets-store-provider-azure
  namespace: openshift-cluster-csi-drivers
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  namespace: openshift-cluster-csi-drivers
  name: csi-secrets-store-provider-azure
  labels:
    app: csi-secrets-store-provider-azure
spec:
  updateStrategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: csi-secrets-store-provider-azure
  template:
    metadata:
      labels:
        app: csi-secrets-store-provider-azure
    spec:
      serviceAccountName: csi-secrets-store-provider-azure
      hostNetwork: true
      containers:
        - name: provider-azure-installer
          image: mcr.microsoft.com/oss/azure/secrets-store/provider-azure:v1.4.1
          imagePullPolicy: IfNotPresent
          args:
            - --endpoint=unix:///provider/azure.sock
            - --construct-pem-chain=true
            - --healthz-port=8989
            - --healthz-path=/healthz
            - --healthz-timeout=5s
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8989
            failureThreshold: 3
            initialDelaySeconds: 5
            timeoutSeconds: 10
            periodSeconds: 30
          resources:
            requests:
              cpu: 50m
              memory: 100Mi
            limits:
              cpu: 50m
              memory: 100Mi
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            runAsUser: 0
            capabilities:
              drop:
              - ALL
          volumeMounts:
            - mountPath: "/provider"
              name: providervol
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: type
                operator: NotIn
                values:
                - virtual-kubelet
      volumes:
        - name: providervol
          hostPath:
            path: "/var/run/secrets-store-csi-providers"
      tolerations:
      - operator: Exists
      nodeSelector:
        kubernetes.io/os: linux
----

.. Grant privileged access to the `csi-secrets-store-provider-azure` service account by running the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user privileged -z csi-secrets-store-provider-azure -n openshift-cluster-csi-drivers
----

.. Create the provider resources by running the following command:
+
[source,terminal]
----
$ oc apply -f azure-provider.yaml
----

. Create a service principal to access the key vault:

.. Set the service principal client secret as an environment variable by running the following command:
+
[source,terminal]
----
$ SERVICE_PRINCIPAL_CLIENT_SECRET="$(az ad sp create-for-rbac --name https://$KEYVAULT_NAME --query 'password' -otsv)"
----

.. Set the service principal client ID as an environment variable by running the following command:
+
[source,terminal]
----
$ SERVICE_PRINCIPAL_CLIENT_ID="$(az ad sp list --display-name https://$KEYVAULT_NAME --query '[0].appId' -otsv)"
----

.. Create a generic secret with the service principal client secret and ID by running the following command:
+
[source,terminal]
----
$ oc create secret generic secrets-store-creds -n my-namespace --from-literal clientid=${SERVICE_PRINCIPAL_CLIENT_ID} --from-literal clientsecret=${SERVICE_PRINCIPAL_CLIENT_SECRET}
----

.. Apply the `secrets-store.csi.k8s.io/used=true` label to allow the provider to find this `nodePublishSecretRef` secret:
+
[source,terminal]
----
$ oc -n my-namespace label secret secrets-store-creds secrets-store.csi.k8s.io/used=true
----

. Create a secret provider class to define your secrets store provider:

.. Create a YAML file that defines the `SecretProviderClass` object:
+
.Example `secret-provider-class-azure.yaml`
[source,yaml]
----
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-azure-provider
  namespace: my-namespace
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"
    useVMManagedIdentity: "false"
    userAssignedIdentityID: ""
    keyvaultName: "kvname"
    objects: |
      array:
        - |
          objectName: secret1
          objectType: secret
    tenantId: "tid"
----
where:

`metadata.name`:: Specifies the name for the secret provider class.
`metadata.namespace`:: Specifies the namespace for the secret provider class.
`spec.provider`:: Specifies the provider as `azure`.
`spec.parameters`:: Specifies the provider-specific configuration parameters.

.. Create the `SecretProviderClass` object by running the following command:
+
[source,terminal]
----
$ oc create -f secret-provider-class-azure.yaml
----

. Create a deployment to use this secret provider class:

.. Create a YAML file that defines the `Deployment` object:
+
.Example `deployment.yaml`
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-azure-deployment
  namespace: my-namespace
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-storage
  template:
    metadata:
      labels:
        app: my-storage
    spec:
      containers:
      - name: busybox
        image: k8s.gcr.io/e2e-test-images/busybox:1.29
        command:
          - "/bin/sleep"
          - "10000"
        volumeMounts:
        - name: secrets-store-inline
          mountPath: "/mnt/secrets-store"
          readOnly: true
      volumes:
        - name: secrets-store-inline
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: "my-azure-provider"
            nodePublishSecretRef:
              name: secrets-store-creds
----
where:

`metadata.name`:: Specifies the name for the deployment.
`metadata.namespace`:: Specifies the namespace for the deployment. This must be the same namespace as the secret provider class.
`spec.template.spec.volumes.csi.volumeAttributes.secretProviderClass`:: Specifies the name of the secret provider class.
`spec.template.spec.volumes.csi.nodePublishSecretRef.name`:: Specifies the name of the Kubernetes secret that contains the service principal credentials to access {azure-short} Key Vault.

.. Create the `Deployment` object by running the following command:
+
[source,terminal]
----
$ oc create -f deployment.yaml
----

.Verification

* Verify that you can access the secrets from {azure-short} Key Vault in the pod volume mount:

.. List the secrets in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec my-azure-deployment-<hash> -n my-namespace -- ls /mnt/secrets-store/
----
+
.Example output
[source,terminal]
----
secret1
----

.. View a secret in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec my-azure-deployment-<hash> -n my-namespace -- cat /mnt/secrets-store/secret1
----
+
.Example output
[source,terminal]
----
my-secret-value
----

// Mounting secrets from Google Secret Manager
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-google_{context}"]
= Mounting secrets from Google Secret Manager

[role="_abstract"]
You can use the {secrets-store-operator} to mount secrets from Google Secret Manager to a Container Storage Interface (CSI) volume in OpenShift Container Platform. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

.Prerequisites

* Your have installed a cluster on {gcp-first}.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {secrets-store-operator}. See "Installing the {secrets-store-driver}" for instructions.
* You have configured Google Secret Manager to store the required secrets.
* You have created a service account key named `key.json` from your {gcp-full} service account.

.Procedure

. Install the Google Secret Manager provider:

.. Create a YAML file Create a YAML file named `gcp-provider.yaml` that defines the `ServiceAccount` resource configuration. See the following example configuration:
+
.Example `gcp-provider.yaml` file
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: csi-secrets-store-provider-gcp
  namespace: openshift-cluster-csi-drivers
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: csi-secrets-store-provider-gcp-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: csi-secrets-store-provider-gcp-role
subjects:
  - kind: ServiceAccount
    name: csi-secrets-store-provider-gcp
    namespace: openshift-cluster-csi-drivers
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: csi-secrets-store-provider-gcp-role
rules:
  - apiGroups:
      - ""
    resources:
      - serviceaccounts/token
    verbs:
      - create
  - apiGroups:
      - ""
    resources:
      - serviceaccounts
    verbs:
      - get
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: csi-secrets-store-provider-gcp
  namespace: openshift-cluster-csi-drivers
  labels:
    app: csi-secrets-store-provider-gcp
spec:
  updateStrategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: csi-secrets-store-provider-gcp
  template:
    metadata:
      labels:
        app: csi-secrets-store-provider-gcp
    spec:
      serviceAccountName: csi-secrets-store-provider-gcp
      initContainers:
      - name: chown-provider-mount
        image: busybox
        command:
        - chown
        - "1000:1000"
        - /etc/kubernetes/secrets-store-csi-providers
        volumeMounts:
        - mountPath: "/etc/kubernetes/secrets-store-csi-providers"
          name: providervol
        securityContext:
          privileged: true
      hostNetwork: false
      hostPID: false
      hostIPC: false
      containers:
        - name: provider
          image: us-docker.pkg.dev/secretmanager-csi/secrets-store-csi-driver-provider-gcp/plugin@sha256:a493a78bbb4ebce5f5de15acdccc6f4d19486eae9aa4fa529bb60ac112dd6650
          securityContext:
            privileged: true
          imagePullPolicy: IfNotPresent
          resources:
            requests:
              cpu: 50m
              memory: 100Mi
            limits:
              cpu: 50m
              memory: 100Mi
          env:
            - name: TARGET_DIR
              value: "/etc/kubernetes/secrets-store-csi-providers"
          volumeMounts:
            - mountPath: "/etc/kubernetes/secrets-store-csi-providers"
              name: providervol
              mountPropagation: None
              readOnly: false
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: /live
              port: 8095
            initialDelaySeconds: 5
            timeoutSeconds: 10
            periodSeconds: 30
      volumes:
        - name: providervol
          hostPath:
            path: /etc/kubernetes/secrets-store-csi-providers
      tolerations:
        - key: kubernetes.io/arch
          operator: Equal
          value: amd64
          effect: NoSchedule
      nodeSelector:
        kubernetes.io/os: linux
----

.. Grant privileged access to the `csi-secrets-store-provider-gcp` service account by running the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user privileged -z csi-secrets-store-provider-gcp -n openshift-cluster-csi-drivers
----

.. Create the provider resources by running the following command:
+
[source,terminal]
----
$ oc apply -f gcp-provider.yaml
----

. Grant a read permission to the Google Secret Manager secret:

.. Create a new project by running the following command:
+
[source,terminal]
----
$ oc new-project my-namespace
----

.. Label the `my-namespace` namespace for pod security admission by running the following command:
+
[source,terminal]
----
$ oc label ns my-namespace security.openshift.io/scc.podSecurityLabelSync=false pod-security.kubernetes.io/enforce=privileged pod-security.kubernetes.io/audit=privileged pod-security.kubernetes.io/warn=privileged --overwrite
----

.. Create a service account for the pod deployment:
+
[source,terminal]
----
$ oc create serviceaccount my-service-account --namespace=my-namespace
----

.. Create a generic secret from the `key.json` file by running the following command:
+
[source,terminal]
----
$ oc create secret generic secrets-store-creds -n my-namespace --from-file=key.json
----
+
You created this `key.json` file from the Google Secret Manager.

.. Apply the `secrets-store.csi.k8s.io/used=true` label to allow the provider to find this `nodePublishSecretRef` secret:
+
[source,terminal]
----
$ oc -n my-namespace label secret secrets-store-creds secrets-store.csi.k8s.io/used=true
----

. Create a secret provider class to define your secrets store provider:

.. Create a YAML file that defines the `SecretProviderClass` object:
+
.Example `secret-provider-class-gcp.yaml`
[source,yaml]
----
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-gcp-provider
  namespace: my-namespace
spec:
  provider: gcp
  parameters:
    secrets: |
      - resourceName: "projects/my-project/secrets/testsecret1/versions/1"
        path: "testsecret1.txt"
----
where:

`metadata.name`:: Specifies the name for the secret provider class.
`metadata.namespace`:: Specifies the namespace for the secret provider class.
`spec.provider`:: Specifies the provider as `gcp`.
`spec.parameters`:: Specifies the provider-specific configuration parameters.

.. Create the `SecretProviderClass` object by running the following command:
+
[source,terminal]
----
$ oc create -f secret-provider-class-gcp.yaml
----

. Create a deployment to use this secret provider class:

.. Create a YAML file that defines the `Deployment` object:
+
.Example `deployment.yaml`
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-gcp-deployment
  namespace: my-namespace
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-storage
  template:
    metadata:
      labels:
        app: my-storage
    spec:
      serviceAccountName: my-service-account
      containers:
      - name: busybox
        image: k8s.gcr.io/e2e-test-images/busybox:1.29
        command:
          - "/bin/sleep"
          - "10000"
        volumeMounts:
        - name: secrets-store-inline
          mountPath: "/mnt/secrets-store"
          readOnly: true
      volumes:
        - name: secrets-store-inline
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: "my-gcp-provider"
            nodePublishSecretRef:
              name: secrets-store-creds
----
where:

`metadata.name`:: Specifies the name for the deployment.
`metadata.namespace`:: Specifies the namespace for the deployment. This must be the same namespace as the secret provider class.
`spec.template.spec.serviceAccountName`:: Specifies the service account you created.
`spec.template.spec.volumes.csi.volumeAttributes.secretProviderClass`:: Specifies the name of the secret provider class.
`spec.template.spec.volumes.csi.nodePublishSecretRef.name`:: Specifies the name of the Kubernetes secret that contains the service principal credentials to access Google Secret Manager.

.. Create the `Deployment` object by running the following command:
+
[source,terminal]
----
$ oc create -f deployment.yaml
----

.Verification

* Verify that you can access the secrets from Google Secret Manager in the pod volume mount:

.. List the secrets in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec my-gcp-deployment-<hash> -n my-namespace -- ls /mnt/secrets-store/
----
+
.Example output
[source,terminal]
----
testsecret1
----

.. View a secret in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec my-gcp-deployment-<hash> -n my-namespace -- cat /mnt/secrets-store/testsecret1
----
+
.Example output
[source,terminal]
----
<secret_value>
----

// Mounting secrets from HashiCorp Vault
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-vault_{context}"]
= Mounting secrets from HashiCorp Vault

[role="_abstract"]
You can use the {secrets-store-operator} to mount secrets from HashiCorp Vault to a Container Storage Interface (CSI) volume in OpenShift Container Platform. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

[IMPORTANT]
====
Mounting secrets from HashiCorp Vault by using the {secrets-store-operator} has been tested with the following cloud providers:

* Amazon Web Services (AWS)
* Microsoft Azure

Other cloud providers might work, but have not been tested yet. Additional cloud providers might be tested in the future.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the {secrets-store-operator}. See "Installing the {secrets-store-driver}" for instructions.
* You have installed Helm.

.Procedure

. Add the HashiCorp Helm repository by running the following command:
+
[source,terminal]
----
$ helm repo add hashicorp https://helm.releases.hashicorp.com
----

. Update all repositories to ensure that Helm is aware of the latest versions by running the following command:
+
[source,terminal]
----
$ helm repo update
----

. Install the HashiCorp Vault provider:

.. Create a new project for Vault by running the following command:
+
[source,terminal]
----
$ oc new-project vault
----

.. Label the `vault` namespace for pod security admission by running the following command:
+
[source,terminal]
----
$ oc label ns vault security.openshift.io/scc.podSecurityLabelSync=false pod-security.kubernetes.io/enforce=privileged pod-security.kubernetes.io/audit=privileged pod-security.kubernetes.io/warn=privileged --overwrite
----

.. Grant privileged access to the `vault` service account by running the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user privileged -z vault -n vault
----

.. Grant privileged access to the `vault-csi-provider` service account by running the following command:
+
[source,terminal]
----
$ oc adm policy add-scc-to-user privileged -z vault-csi-provider -n vault
----

.. If you are using {ibm-z-title}, create a `vault-license` secret for HashiCorp Vault Enterprise:
+
... Create a `vault-license.yaml` file with the following content:
+
[source,yaml]
----
apiVersion: v1
data:
  license: <license-string>
kind: Secret
metadata:
  name: vault-license
  namespace: vault
type: Opaque
----
+
... Create the secret by running the following command:
+
[source,terminal]
----
$ oc create -f vault-license.yaml
----

.. Deploy HashiCorp Vault by running the following command:
+
[source,terminal]
----
$ helm install vault hashicorp/vault --namespace=vault \
  --set "server.dev.enabled=true" \
  --set "injector.enabled=false" \
  --set "csi.enabled=true" \
  --set "global.openshift=true" \
  --set "injector.agentImage.repository=docker.io/hashicorp/vault" \
  --set "server.image.repository=docker.io/hashicorp/vault" \
  --set "csi.image.repository=docker.io/hashicorp/vault-csi-provider" \
  --set "csi.agent.image.repository=docker.io/hashicorp/vault" \
  --set "csi.daemonSet.providersDir=/var/run/secrets-store-csi-providers"
----
+
If you are using {ibm-z-title}, you must use Vault Enterprise images and the Vault license secret. Run the following command instead:
+
[source,terminal]
----
$ helm install vault hashicorp/vault \
  --namespace vault \
  --create-namespace \
  --set server.dev.enabled=true \
  --set server.image.repository="docker.io/hashicorp/vault-enterprise" \
  --set server.image.tag="1.21-ent" \
  --set server.enterpriseLicense.secretName="vault-license" \
  --set server.logLevel=debug \
  --set server.serviceAccount.name="vault" \
  --set "injector.enabled=false" \
  --set global.openshift=true \
  --set csi.enabled=true \
  --set "csi.daemonSet.providersDir=/var/run/secrets-store-csi-providers" \
  --set csi.image.repository="registry.connect.redhat.com/hashicorp/vault-csi-provider" \
  --set csi.image.tag="1.7.1-ubi" \
  --set csi.agent.enabled=false
----

.. Patch the `vault-csi-driver` daemon set to set the `securityContext` to `privileged` by running the following command:
+
[source,terminal]
----
$ oc patch daemonset -n vault vault-csi-provider --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/securityContext", "value": {"privileged": true} }]'
----

.. Verify that the `vault-csi-provider` pods have started properly by running the following command:
+
[source,terminal]
----
$ oc get pods -n vault
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS    RESTARTS   AGE
vault-0                    1/1     Running   0          24m
vault-csi-provider-87rgw   1/2     Running   0          5s
vault-csi-provider-bd6hp   1/2     Running   0          4s
vault-csi-provider-smlv7   1/2     Running   0          5s
----

. Configure HashiCorp Vault to store the required secrets:

.. Create a secret by running the following command:
+
[source,terminal]
----
$ oc exec vault-0 --namespace=vault -- vault kv put secret/example1 testSecret1=my-secret-value
----

.. Verify that the secret is readable at the path `secret/example1` by running the following command:
+
[source,terminal]
----
$ oc exec vault-0 --namespace=vault -- vault kv get secret/example1
----
+
.Example output
[source,terminal]
----
= Secret Path =
secret/data/example1

======= Metadata =======
Key                Value
---                -----
created_time       2024-04-05T07:05:16.713911211Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1

======= Data =======
Key            Value
---            -----
testSecret1    my-secret-value
----

. Configure Vault to use Kubernetes authentication:

.. Enable the Kubernetes auth method by running the following command:
+
[source,terminal]
----
$ oc exec vault-0 --namespace=vault -- vault auth enable kubernetes
----
+
.Example output
[source,terminal]
----
Success! Enabled kubernetes auth method at: kubernetes/
----

.. Configure the Kubernetes auth method:

... Set the token reviewer as an environment variable by running the following command:
+
[source,terminal]
----
$ TOKEN_REVIEWER_JWT="$(oc exec vault-0 --namespace=vault -- cat /var/run/secrets/kubernetes.io/serviceaccount/token)"
----
... Set the Kubernetes service IP address as an environment variable by running the following command:
+
[source,terminal]
----
$ KUBERNETES_SERVICE_IP="$(oc get svc kubernetes --namespace=default -o go-template="{{ .spec.clusterIP }}")"
----

... Update the Kubernetes auth method by running the following command:
+
[source,terminal]
----
$ oc exec -i vault-0 --namespace=vault -- vault write auth/kubernetes/config \
  issuer="https://kubernetes.default.svc.cluster.local" \
  token_reviewer_jwt="${TOKEN_REVIEWER_JWT}" \
  kubernetes_host="https://${KUBERNETES_SERVICE_IP}:443" \
  kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
----
+
.Example output
[source,terminal]
----
Success! Data written to: auth/kubernetes/config
----

.. Create a policy for the application by running the following command:
+
[source,terminal]
----
$ oc exec -i vault-0 --namespace=vault -- vault policy write csi -<<EOF
  path "secret/data/*" {
  capabilities = ["read"]
  }
  EOF
----
+
.Example output
[source,terminal]
----
Success! Uploaded policy: csi
----

.. Create an authentication role to access the application by running the following command:
+
[source,terminal]
----
$ oc exec -i vault-0 --namespace=vault -- vault write auth/kubernetes/role/csi \
  bound_service_account_names=default \
  bound_service_account_namespaces=default,test-ns,negative-test-ns,my-namespace \
  policies=csi \
  ttl=20m
----
+
.Example output
[source,terminal]
----
Success! Data written to: auth/kubernetes/role/csi
----

. Create a secret provider class to define your secrets store provider:

.. Create a YAML file that defines the `SecretProviderClass` object:
+
.Example `secret-provider-class-vault.yaml`
[source,yaml]
----
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-vault-provider
  namespace: my-namespace
spec:
  provider: vault
  parameters:
    roleName: "csi"
    vaultAddress: "http://vault.vault:8200"
    objects:  |
      - secretPath: "secret/data/example1"
        objectName: "testSecret1"
        secretKey: "testSecret1"
----
where:

`metadata.name`:: Specifies the name for the secret provider class.
`metadata.namespace`:: Specifies the namespace for the secret provider class.
`spec.provider`:: Specifies the provider as `vault`.
`spec.parameters`:: Specifies the provider-specific configuration parameters.

.. Create the `SecretProviderClass` object by running the following command:
+
[source,terminal]
----
$ oc create -f secret-provider-class-vault.yaml
----

. Create a deployment to use this secret provider class:

.. Create a YAML file that defines the `Deployment` object:
+
.Example `deployment.yaml`
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: busybox-deployment
  namespace: my-namespace
  labels:
    app: busybox
spec:
  replicas: 1
  selector:
    matchLabels:
      app: busybox
  template:
    metadata:
      labels:
        app: busybox
    spec:
      terminationGracePeriodSeconds: 0
      containers:
      - image: registry.k8s.io/e2e-test-images/busybox:1.29-4
        name: busybox
        imagePullPolicy: IfNotPresent
        command:
        - "/bin/sleep"
        - "10000"
        volumeMounts:
        - name: secrets-store-inline
          mountPath: "/mnt/secrets-store"
          readOnly: true
      volumes:
        - name: secrets-store-inline
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: "my-vault-provider"
----
where:

`metadata.name`:: Specifies the name for the deployment.
`metadata.namespace`:: Specifies the namespace for the deployment. This must be the same namespace as the secret provider class.
`spec.template.spec.volumes.csi.volumeAttributes.secretProviderClass`:: Specifies the name of the secret provider class.

.. Create the `Deployment` object by running the following command:
+
[source,terminal]
----
$ oc create -f deployment.yaml
----

.Verification

* Verify that all of the `vault` pods are running properly by running the following command:
+
[source,terminal]
----
$ oc get pods -n vault
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS    RESTARTS   AGE
vault-0                    1/1     Running   0          43m
vault-csi-provider-87rgw   2/2     Running   0          19m
vault-csi-provider-bd6hp   2/2     Running   0          19m
vault-csi-provider-smlv7   2/2     Running   0          19m
----

* Verify that all of the `secrets-store-csi-driver` pods are running by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-cluster-csi-drivers | grep -E "secrets"
----
+
.Example output
[source,terminal]
----
secrets-store-csi-driver-node-46d2g                  3/3     Running   0             45m
secrets-store-csi-driver-node-d2jjn                  3/3     Running   0             45m
secrets-store-csi-driver-node-drmt4                  3/3     Running   0             45m
secrets-store-csi-driver-node-j2wlt                  3/3     Running   0             45m
secrets-store-csi-driver-node-v9xv4                  3/3     Running   0             45m
secrets-store-csi-driver-node-vlz28                  3/3     Running   0             45m
secrets-store-csi-driver-operator-84bd699478-fpxrw   1/1     Running   0             47m
----

* Verify that you can access the secrets from your HashiCorp Vault in the pod volume mount:

.. List the secrets in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec busybox-deployment-<hash> -n my-namespace -- ls /mnt/secrets-store/
----
+
.Example output
[source,terminal]
----
testSecret1
----

.. View a secret in the pod mount by running the following command:
+
[source,terminal]
----
$ oc exec busybox-deployment-<hash> -n my-namespace -- cat /mnt/secrets-store/testSecret1
----
+
.Example output
[source,terminal]
----
my-secret-value
----

// Enabling synchronization of mounted content as Kubernetes secrets
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-sync-secrets_{context}"]
= Enabling synchronization of mounted content as Kubernetes secrets

[role="_abstract"]
You can enable a synchronization process that creates `secret` objects from the content on a mounted volume. Using secrets protects information that you do not want developers to have.

An example where you might want to enable synchronization is to use an environment variable in your deployment to reference the Kubernetes secret.

[WARNING]
====
Do not enable synchronization if you do not want to store your secrets on your OpenShift Container Platform cluster and in etcd. Enable this functionality only if you require it, such as when you want to use environment variables to refer to the secret.
====

If you enable synchronization, the secrets from the mounted volume are synchronized as Kubernetes secrets after you start a pod that mounts the secrets.

The synchronized Kubernetes secret is deleted when all pods that mounted the content are deleted.

.Prerequisites

* You have installed the {secrets-store-operator}.
* You have installed a secrets store provider.
* You have created the secret provider class.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `SecretProviderClass` resource by running the following command:
+
[source,terminal]
----
$ oc edit secretproviderclass my-azure-provider
----
+
Replace `my-azure-provider` with the name of your secret provider class.

. Add the `secretsObjects` section with the configuration for the synchronized Kubernetes secrets:
+
[source,yaml]
----
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-azure-provider
  namespace: my-namespace
spec:
  provider: azure
  secretObjects:
    - secretName: tlssecret
      type: kubernetes.io/tls
      labels:
        environment: "test"
      data:
        - objectName: tlskey
          key: tls.key
        - objectName: tlscrt
          key: tls.crt
  parameters:
    usePodIdentity: "false"
    keyvaultName: "kvname"
    objects:  |
      array:
        - |
          objectName: tlskey
          objectType: secret
        - |
          objectName: tlscrt
          objectType: secret
    tenantId: "tid"
----
where:

`spec.secretObjects`:: Specifies the configuration for synchronized Kubernetes secrets.
`spec.secretObjects.secretname`:: Specifies the name of the Kubernetes `Secret` object to create.
`spec.secretObjects.type`:: Specifies the type of Kubernetes `Secret` object to create. For example, `Opaque` or `kubernetes.io/tls`.
`spec.secretObjects.data.object.name`:: Specifies the object name or alias of the mounted content to synchronize.
`spec.secretObjects.data.object.key`:: Specifies the data field from the specified `objectName` to populate the Kubernetes secret with.

. Save the file to apply the changes.

// Viewing the status of secrets in the pod volume mount
// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

[id="secrets-store-viewing-secret-versions_{context}"]
= Viewing the status of secrets in the pod volume mount

[role="_abstract"]
You can view detailed information of the secrets, including the versions, in the pod volume mount. You can use this information to help you confirm that secrets from your external store are active within the pod environment.

The {secrets-store-operator} creates a `SecretProviderClassPodStatus` resource in the same namespace as the pod. You can review this resource to see detailed information, including versions, about the secrets in the pod volume mount.

.Prerequisites

* You have installed the {secrets-store-operator}.
* You have installed a secrets store provider.
* You have created the secret provider class.
* You have deployed a pod that mounts a volume from the {secrets-store-operator}.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

* View detailed information about the secrets in a pod volume mount by running the following command:
+
[source,terminal]
----
$ oc get secretproviderclasspodstatus <secret_provider_class_pod_status_name> -o yaml <1>
----
+
Replace `<secret_provider_class_pod_status_name>` with the name of the secret provider class pod status object is in the format of `<pod_name>-<namespace>-<secret_provider_class_name>`.
+
.Example output
[source,terminal]
----
...
status:
  mounted: true
  objects:
  - id: secret/tlscrt
    version: f352293b97da4fa18d96a9528534cb33
  - id: secret/tlskey
    version: 02534bc3d5df481cb138f8b2a13951ef
  podName: busybox-<hash>
  secretProviderClassName: my-azure-provider
  targetPath: /var/lib/kubelet/pods/f0d49c1e-c87a-4beb-888f-37798456a3e7/volumes/kubernetes.io~csi/secrets-store-inline/mount
----

// Uninstalling the {secrets-store-operator}
// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-secrets-store.adoc
//

[id="persistent-storage-csi-secrets-store-driver-uninstall_{context}"]
= Uninstalling the {secrets-store-operator}

[role="_abstract"]
You can use the OpenShift Container Platform web console to uninstall the {secrets-store-driver}.

.Prerequisites
* Access to the OpenShift Container Platform web console.

* Administrator access to the cluster.

.Procedure

. Stop all application pods that use the `secrets-store.csi.k8s.io` provider.
. Remove any third-party provider plug-in for your chosen secret store.
. Remove the Container Storage Interface (CSI) driver and associated manifests:
.. Click *Administration* → *CustomResourceDefinitions* → *ClusterCSIDriver*.
.. On the *Instances* tab, for *secrets-store.csi.k8s.io*, on the far left side, click the drop-down menu, and then click *Delete ClusterCSIDriver*.
.. When prompted, click *Delete*.
. Verify that the CSI driver pods are no longer running.
. Uninstall the {secrets-store-operator}:
+
[NOTE]
====
Before you can uninstall the Operator, you must remove the CSI driver first.
====
+
.. Click *Ecosystem* -> *Installed Operators*.
.. On the *Installed Operators* page, scroll or type "Secrets Store CSI" into the *Search by name* box to find the Operator, and then click it.
.. On the upper, right of the *Installed Operators* > *Operator details* page, click *Actions* → *Uninstall Operator*.
.. When prompted on the *Uninstall Operator* window, click the *Uninstall* button to remove the Operator from the namespace. Any applications deployed by the Operator on the cluster need to be cleaned up manually.
+
After uninstalling, the {secrets-store-operator} is no longer listed in the *Installed Operators* section of the web console.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Configuring the Cloud Credential Operator utility

* Installing Helm

* Red{nbsp}Hat third-party support policy
