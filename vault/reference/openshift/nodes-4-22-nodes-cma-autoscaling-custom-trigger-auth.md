---
title: "Understanding custom metrics autoscaler trigger authentications"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-trigger-auth
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-trigger-auth
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Understanding custom metrics autoscaler trigger authentications

[id="nodes-cma-autoscaling-custom-trigger-auth"]
= Understanding custom metrics autoscaler trigger authentications

A trigger authentication allows you to include authentication information in a scaled object or a scaled job that can be used by the associated containers. You can use trigger authentications to pass OpenShift Container Platform secrets, platform-native pod authentication mechanisms, environment variables, and so on.

You define a `TriggerAuthentication` object in the same namespace as the object that you want to scale. That trigger authentication can be used only by objects in that namespace.

Alternatively, to share credentials between objects in multiple namespaces, you can create a `ClusterTriggerAuthentication` object that can be used across all namespaces.

Trigger authentications and cluster trigger authentication use the same configuration. However, a cluster trigger authentication requires an additional `kind` parameter in the authentication reference of the scaled object.

.Example trigger authentication that uses a bound service account token
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace <1>
spec:
  boundServiceAccountToken: <2>
    - parameter: bearerToken
      serviceAccountName: thanos <3>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint.
<3> Specifies the name of the service account to use.

.Example cluster trigger authentication that uses a bound service account token
[source,yaml]
----
kind: ClusterTriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: bound-service-account-token-triggerauthentication <1>
spec:
  boundServiceAccountToken: <2>
    - parameter: bearerToken
      serviceAccountName: thanos <3>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this cluster trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint.
<3> Specifies the name of the service account to use.

.Example trigger authentication that uses a secret for Basic authentication
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace <1>
spec:
  secretTargetRef: <2>
  - parameter: username <3>
    name: my-basic-secret <4>
    key: username <5>
  - parameter: password
    name: my-basic-secret
    key: password
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint.
<3> Specifies the authentication parameter to supply by using the secret.
<4> Specifies the name of the secret to use. See the following example secret for Basic authentication.
<5> Specifies the key in the secret to use with the specified parameter.

.Example secret for Basic authentication
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-basic-secret
  namespace: default
data:
  username: "dXNlcm5hbWU=" <1>
  password: "cGFzc3dvcmQ="
----
<1> User name and password to supply to the trigger authentication. The values in the `data` stanza must be base-64 encoded.

.Example trigger authentication that uses a secret for CA details
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace <1>
spec:
  secretTargetRef: <2>
    - parameter: key <3>
      name: my-secret <4>
      key: client-key.pem <5>
    - parameter: ca <6>
      name: my-secret <7>
      key: ca-cert.pem <8>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint.
<3> Specifies the type of authentication to use.
<4> Specifies the name of the secret to use.
<5> Specifies the key in the secret to use with the specified parameter.
<6> Specifies the authentication parameter for a custom CA when connecting to the metrics endpoint.
<7> Specifies the name of the secret to use. See the following example secret with certificate authority (CA) details.
<8> Specifies the key in the secret to use with the specified parameter.

.Example secret with certificate authority (CA) details
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-namespace
data:
  ca-cert.pem: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0... <1>
  client-cert.pem: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0... <2>
  client-key.pem: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0t...
----
<1> Specifies the TLS CA Certificate for authentication of the metrics endpoint. The value must be base-64 encoded.
<2> Specifies the TLS certificates and key for TLS client authentication. The values must be base-64 encoded.

.Example trigger authentication that uses a bearer token
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: token-triggerauthentication
  namespace: my-namespace <1>
spec:
  secretTargetRef: <2>
  - parameter: bearerToken <3>
    name: my-secret <4>
    key: bearerToken <5>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint.
<3> Specifies the type of authentication to use.
<4> Specifies the name of the secret to use. See the following example secret for a bearer token.
<5> Specifies the key in the token to use with the specified parameter.

.Example secret for a bearer token
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-namespace
data:
  bearerToken: "<bearer_token>" <1>
----
<1> Specifies a bearer token to use with bearer authentication. The value must be base-64 encoded.

.Example trigger authentication that uses an environment variable
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: env-var-triggerauthentication
  namespace: my-namespace <1>
spec:
  env: <2>
  - parameter: access_key <3>
    name: ACCESS_KEY <4>
    containerName: my-container <5>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses environment variables for authorization when connecting to the metrics endpoint.
<3> Specify the parameter to set with this variable.
<4> Specify the name of the environment variable.
<5> Optional: Specify a container that requires authentication. The container must be in the same resource as referenced by `scaleTargetRef` in the scaled object.

.Example trigger authentication that uses pod authentication providers
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: pod-id-triggerauthentication
  namespace: my-namespace <1>
spec:
  podIdentity: <2>
    provider: aws-eks <3>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses a platform-native pod authentication when connecting to the metrics endpoint.
<3> Specifies a pod identity. Supported values are `none`, `azure`, `gcp`, `aws-eks`, or `aws-kiam`. The default is `none`.

// Remove ifdef after https://github.com/openshift/openshift-docs/pull/62147 merges
// ifndef::openshift-rosa,openshift-dedicated[]
.Additional resources

* Understanding and creating service accounts
* Providing sensitive data to pods.
// endif::openshift-rosa,openshift-dedicated[]

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-trigger-auth.adoc

[id="nodes-cma-autoscaling-custom-trigger-auth-using_{context}"]
= Using trigger authentications

You use trigger authentications and cluster trigger authentications by using a custom resource to create the authentication,  then add a reference to a scaled object or scaled job.

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

* If you are using a bound service account token, the service account must exist.

* If you are using a bound service account token, a role-based access control (RBAC) object that enables the Custom Metrics Autoscaler Operator to request service account tokens from the service account must exist.
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: keda-operator-token-creator
  namespace: <namespace_name> <1>
rules:
- apiGroups:
  - ""
  resources:
  - serviceaccounts/token
  verbs:
  - create
  resourceNames:
  - thanos <2>
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: keda-operator-token-creator-binding
  namespace: <namespace_name> <3>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: keda-operator-token-creator
subjects:
- kind: ServiceAccount
  name: keda-operator
  namespace: openshift-keda
----
<1> Specifies the namespace of the service account.
<2> Specifies the name of the service account.
<3> Specifies the namespace of the service account.

* If you are using a secret, the `Secret` object must exist.

.Procedure

. Create the `TriggerAuthentication` or  `ClusterTriggerAuthentication` object.

.. Create a YAML file that defines the object:
+
.Example trigger authentication with a bound service account token
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: prom-triggerauthentication
  namespace: my-namespace <1>
  spec:
  boundServiceAccountToken: <2>
    - parameter: token
      serviceAccountName: thanos <3>
----
<1> Specifies the namespace of the object you want to scale.
<2> Specifies that this trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint.
<3> Specifies the name of the service account to use.

.. Create the `TriggerAuthentication` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. Create or edit a `ScaledObject` YAML file that uses the trigger authentication:

.. Create a YAML file that defines the object by running the following command:
+
.Example scaled object with a trigger authentication
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: scaledobject
  namespace: my-namespace
spec:
  scaleTargetRef:
    name: example-deployment
  maxReplicaCount: 100
  minReplicaCount: 0
  pollingInterval: 30
  triggers:
  - type: prometheus
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest # replace <NAMESPACE>
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "basic"
    authenticationRef:
      name: prom-triggerauthentication <1>
      kind: TriggerAuthentication <2>
----
<1> Specify the name of your trigger authentication object.
<2> Specify `TriggerAuthentication`. `TriggerAuthentication` is the default.
+
.Example scaled object with a cluster trigger authentication
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: scaledobject
  namespace: my-namespace
spec:
  scaleTargetRef:
    name: example-deployment
  maxReplicaCount: 100
  minReplicaCount: 0
  pollingInterval: 30
  triggers:
  - type: prometheus
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest # replace <NAMESPACE>
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "basic"
    authenticationRef:
      name: prom-cluster-triggerauthentication <1>
      kind: ClusterTriggerAuthentication <2>
----
<1> Specify the name of your trigger authentication object.
<2> Specify `ClusterTriggerAuthentication`.

.. Create the scaled object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----
