---
title: "Accessing monitoring APIs by using the CLI"
type: reference
domain: openshift
slug: observability-4-22-accessing-monitoring-apis-by-using-the-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/accessing-monitoring-apis-by-using-the-cli
version: 4.22
family: observability
documentKind: "Documentation"
---

# Accessing monitoring APIs by using the CLI

[id="accessing-monitoring-apis-by-using-the-cli"]
= Accessing monitoring APIs by using the CLI

In OpenShift Container Platform, you can access web service APIs for some monitoring components from the command-line interface (CLI).

[IMPORTANT]
====
In certain situations, accessing API endpoints can degrade the performance and scalability of your cluster, especially if you use endpoints to retrieve, send, or query large amounts of metrics data.

To avoid these issues, consider the following recommendations:

* Avoid querying endpoints frequently. Limit queries to a maximum of one every 30 seconds.
* Do not retrieve all metrics data through the `/federate` endpoint for Prometheus. Query the endpoint only when you want to retrieve a limited, aggregated data set. For example, retrieving fewer than 1,000 samples for each request helps minimize the risk of performance degradation.
====

// About accessing monitoring web service APIs
// Module included in the following assemblies:
//
// * observability/monitoring/accessing-metrics/accessing-monitoring-apis-by-using-the-cli.adoc

[id="about-accessing-monitoring-web-service-apis_{context}"]
= About accessing monitoring web service APIs

[role="_abstract"]
To interact with the monitoring stack by using the command line, you can access web service API endpoints for Prometheus, Alertmanager, Thanos Ruler, and Thanos Querier. Direct API access requires bearer token authentication and the correct namespace permissions.

[IMPORTANT]
====
To access Thanos Ruler and Thanos Querier service APIs, the requesting account must have `get` permission on the namespaces resource, which can be granted by binding the `cluster-monitoring-view` cluster role to the account.
====

When you access web service API endpoints for monitoring components, be aware of the following limitations:

* You can only use bearer token authentication to access API endpoints.
* You can only access endpoints in the `/api` path for a route.
If you try to access an API endpoint in a web browser, an `Application is not available` error occurs.
To access monitoring features in a web browser, use the OpenShift Container Platform web console to review monitoring dashboards.

[role="_additional-resources"]
.Additional resources

* Reviewing monitoring dashboards as a cluster administrator
* Reviewing monitoring dashboards as a developer

// Accessing a monitoring web service API
// Module included in the following assemblies:
//
// * observability/monitoring/accessing-third-party-monitoring-apis.adoc

[id="accessing-a-monitoring-web-service-api_{context}"]
= Accessing a monitoring web service API

The following example shows how to query the service API receivers for the Alertmanager service used in core platform monitoring.
You can use a similar method to access the `prometheus-k8s` service for core platform Prometheus and the `thanos-ruler` service for Thanos Ruler.

.Prerequisites

* You are logged in to an account that is bound against the `monitoring-alertmanager-edit` role in the `openshift-monitoring` namespace.
* You are logged in to an account that has permission to get the Alertmanager API route.
+
[NOTE]
====
If your account does not have permission to get the Alertmanager API route, a cluster administrator can provide the URL for the route.
====

.Procedure

. Extract an authentication token by running the following command:
+
[source,terminal]
----
$ TOKEN=$(oc whoami -t)
----

. Extract the `alertmanager-main` API route URL by running the following command:
+
[source,terminal]
----
$ HOST=$(oc -n openshift-monitoring get route alertmanager-main -ojsonpath='{.status.ingress[].host}')
----

. Query the service API receivers for Alertmanager by running the following command:
+
[source,terminal]
----
$ curl -H "Authorization: Bearer $TOKEN" -k "https://$HOST/api/v2/receivers"
----

// Querying metrics by using the federation endpoint for Prometheus
// Module included in the following assemblies:
//
// * observability/monitoring/accessing-third-party-monitoring-apis.adoc

[id="monitoring-querying-metrics-by-using-the-federation-endpoint-for-prometheus_{context}"]
= Querying metrics by using the federation endpoint for Prometheus

You can use the federation endpoint for Prometheus to scrape platform and user-defined metrics from a network location outside the cluster.
To do so, access the Prometheus `/federate` endpoint for the cluster via
an OpenShift Container Platform
a OpenShift Container Platform
route.

[IMPORTANT]
====
A delay in retrieving metrics data occurs when you use federation.
This delay can affect the accuracy and timeliness of the scraped metrics.

Using the federation endpoint can also degrade the performance and scalability of your cluster, especially if you use the federation endpoint to retrieve large amounts of metrics data.
To avoid these issues, follow these recommendations:

* Do not try to retrieve all metrics data via the federation endpoint for Prometheus.
Query it only when you want to retrieve a limited, aggregated data set.
For example, retrieving fewer than 1,000 samples for each request helps minimize the risk of performance degradation.

* Avoid frequent querying of the federation endpoint for Prometheus.
Limit queries to a maximum of one every 30 seconds.

If you need to forward large amounts of data outside the cluster, use remote write instead. For more information, see the _Configuring remote write storage_ section.
====

.Prerequisites

* You have installed the {oc-first}.
* You have access to the cluster as a user with the `cluster-monitoring-view` cluster role or have obtained a bearer token with `get` permission on the `namespaces` resource.
+
[NOTE]
====
You can only use bearer token authentication to access the Prometheus federation endpoint.
====

* You are logged in to an account that has permission to get the Prometheus federation route.
+
[NOTE]
====
If your account does not have permission to get the Prometheus federation route, a cluster administrator can provide the URL for the route.
====

.Procedure

. Retrieve the bearer token by running the following the command:
+
[source,terminal]
----
$ TOKEN=$(oc whoami -t)
----

. Get the Prometheus federation route URL by running the following command:
+
[source,terminal]
----
$ HOST=$(oc -n openshift-monitoring get route prometheus-k8s-federate -ojsonpath='{.status.ingress[].host}')
----

. Query metrics from the `/federate` route.
The following example command queries `up` metrics:
+
[source,terminal]
----
$ curl -G -k -H "Authorization: Bearer $TOKEN" https://$HOST/federate --data-urlencode 'match[]=up'
----
+
.Example output
+
[source,terminal]
----
# TYPE up untyped
up{apiserver="kube-apiserver",endpoint="https",instance="10.0.143.148:6443",job="apiserver",namespace="default",service="kubernetes",prometheus="openshift-monitoring/k8s",prometheus_replica="prometheus-k8s-0"} 1 1657035322214
up{apiserver="kube-apiserver",endpoint="https",instance="10.0.148.166:6443",job="apiserver",namespace="default",service="kubernetes",prometheus="openshift-monitoring/k8s",prometheus_replica="prometheus-k8s-0"} 1 1657035338597
up{apiserver="kube-apiserver",endpoint="https",instance="10.0.173.16:6443",job="apiserver",namespace="default",service="kubernetes",prometheus="openshift-monitoring/k8s",prometheus_replica="prometheus-k8s-0"} 1 1657035343834
...
----

// Accessing metrics from outside the cluster for custom applications
// Module included in the following assemblies:
//
// * observability/monitoring/accessing-third-party-monitoring-apis.adoc

[id="accessing-metrics-from-outside-cluster_{context}"]
= Accessing metrics from outside the cluster for custom applications

You can query Prometheus metrics from outside the cluster when monitoring your own services with user-defined projects. Access this data from outside the cluster by using the `thanos-querier` route.

This access only supports using a bearer token for authentication.

.Prerequisites

* You have deployed your own service, following the "Enabling monitoring for user-defined projects" procedure.
* You are logged in to an account with the `cluster-monitoring-view` cluster role, which provides permission to access the Thanos Querier API.
* You are logged in to an account that has permission to get the Thanos Querier API route.
+
[NOTE]
====
If your account does not have permission to get the Thanos Querier API route, a cluster administrator can provide the URL for the route.
====

.Procedure

. Extract an authentication token to connect to Prometheus by running the following command:
+
[source,terminal]
----
$ TOKEN=$(oc whoami -t)
----

. Extract the `thanos-querier` API route URL by running the following command:
+
[source,terminal]
----
$ HOST=$(oc -n openshift-monitoring get route thanos-querier -ojsonpath='{.status.ingress[].host}')
----

. Set the namespace to the namespace in which your service is running by using the following command:
+
[source,terminal]
----
$ NAMESPACE=ns1
----

. Query the metrics of your own services in the command line by running the following command:
+
[source,terminal]
----
$ curl -H "Authorization: Bearer $TOKEN" -k "https://$HOST/api/v1/query?" --data-urlencode "query=up{namespace='$NAMESPACE'}"
----
+
The output shows the status for each application pod that Prometheus is scraping:
+
.The formatted example output
[source,terminal]
----
{
  "status": "success",
  "data": {
    "resultType": "vector",
    "result": [
      {
        "metric": {
          "__name__": "up",
          "endpoint": "web",
          "instance": "10.129.0.46:8080",
          "job": "prometheus-example-app",
          "namespace": "ns1",
          "pod": "prometheus-example-app-68d47c4fb6-jztp2",
          "service": "prometheus-example-app"
        },
        "value": [
          1591881154.748,
          "1"
        ]
      }
    ],
  }
}
----
+
[NOTE]
====
* The formatted example output uses a filtering tool, such as `jq`, to provide the formatted indented JSON. See the jq Manual (jq documentation) for more information about using `jq`.

* The command requests an instant query endpoint of the Thanos Querier service, which evaluates selectors at one point in time.
====

// Resources reference for the Cluster Monitoring Operator
// DO NOT EDIT THE CONTENT IN THIS FILE. It is automatically generated from the
// source code for the Cluster Monitoring Operator. Any changes made to this
// file will be overwritten when the content is regenerated. If you wish to
// make edits or learn more about how this file is generated, read the docgen utility
// instructions in the source code for the CMO.
[id="resources-reference-for-the-cluster-monitoring-operator_{context}"]
= Resources reference for the Cluster Monitoring Operator

This document describes the following resources deployed and managed by the Cluster Monitoring Operator (CMO):

* Routes
* Services

Use this information when you want to configure API endpoint connections to retrieve, send, or query metrics data.

[IMPORTANT]
====
In certain situations, accessing endpoints can degrade the performance and scalability of your cluster, especially if you use endpoints to retrieve, send, or query large amounts of metrics data.

To avoid these issues, follow these recommendations:

* Avoid querying endpoints frequently. Limit queries to a maximum of one every 30 seconds.
* Do not try to retrieve all metrics data via the `/federate` endpoint. Query it only when you want to retrieve a limited, aggregated data set. For example, retrieving fewer than 1,000 samples for each request helps minimize the risk of performance degradation.
====
[id="cmo-routes-resources_{context}"]
== CMO routes resources

=== openshift-monitoring/alertmanager-main

Expose the `/api` endpoints of the `alertmanager-main` service via a router.

=== openshift-monitoring/prometheus-k8s

Expose the `/api` endpoints of the `prometheus-k8s` service via a router.

=== openshift-monitoring/prometheus-k8s-federate

Expose the `/federate` endpoint of the `prometheus-k8s` service via a router.

=== openshift-user-workload-monitoring/federate

Expose the `/federate` endpoint of the `prometheus-user-workload` service via a router.

=== openshift-monitoring/thanos-querier

Expose the `/api` endpoints of the `thanos-querier` service via a router.

=== openshift-user-workload-monitoring/thanos-ruler

Expose the `/api` endpoints of the `thanos-ruler` service via a router.

[id="cmo-services-resources_{context}"]
== CMO services resources

=== openshift-monitoring/prometheus-operator-admission-webhook

Expose the admission webhook service which validates `PrometheusRules` and `AlertmanagerConfig` custom resources on port 8443.

=== openshift-user-workload-monitoring/alertmanager-user-workload

Expose the user-defined Alertmanager web server within the cluster on the following ports:

* Port 9095 provides access to the Alertmanager endpoints. Granting access requires binding a user to the `monitoring-alertmanager-api-reader` role (for read-only operations) or the `monitoring-alertmanager-api-writer` role in the `openshift-user-workload-monitoring` project.
* Port 9092 provides access to the Alertmanager endpoints restricted to a given project. Granting access requires binding a user to the `monitoring-rules-edit` cluster role or `monitoring-edit` cluster role in the project.
* Port 9097 provides access to the `/metrics` endpoint only. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/alertmanager-main

Expose the Alertmanager web server within the cluster on the following ports:

* Port 9094 provides access to all the Alertmanager endpoints. Granting access requires binding a user to the `monitoring-alertmanager-view` role (for read-only operations) or the `monitoring-alertmanager-edit` role in the `openshift-monitoring` project.

Example monitoring-alertmanager-view permissions::
+
The following example exercises permissions granted by the `monitoring-alertmanager-view` role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-alertmanager-web-monitoring-alertmanager-view
----
+
[source,terminal]
----
$ oc create serviceaccount am-client --namespace=test-alertmanager-web-monitoring-alertmanager-view
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-alertmanager-web-monitoring-alertmanager-view \
  --namespace=openshift-monitoring \
  --role=monitoring-alertmanager-view \
  --serviceaccount=test-alertmanager-web-monitoring-alertmanager-view:am-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token am-client --namespace=test-alertmanager-web-monitoring-alertmanager-view)
----

. Access Alertmanager endpoints externally.
+
[source,terminal]
----
$ ROUTE=$(oc get route alertmanager-main --namespace=openshift-monitoring -ojsonpath={.spec.host})
----
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://$ROUTE/api/v2/alerts?filter=alertname=Watchdog"
----

. Access Alertmanager endpoints from within the cluster.
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://alertmanager-main.openshift-monitoring:9094/api/v2/alerts?filter=alertname=Watchdog"
----

Example monitoring-alertmanager-edit permissions::
+
The following example exercises permissions granted by the `monitoring-alertmanager-edit` role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-alertmanager-web-monitoring-alertmanager-edit
----
+
[source,terminal]
----
$ oc create serviceaccount am-client --namespace=test-alertmanager-web-monitoring-alertmanager-edit
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-alertmanager-web-monitoring-alertmanager-edit \
  --namespace=openshift-monitoring \
  --role=monitoring-alertmanager-edit \
  --serviceaccount=test-alertmanager-web-monitoring-alertmanager-edit:am-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token am-client --namespace=test-alertmanager-web-monitoring-alertmanager-edit)
----

. Access Alertmanager endpoints externally.
+
[source,terminal]
----
$ ROUTE=$(oc get route alertmanager-main --namespace=openshift-monitoring -ojsonpath={.spec.host})
----
+
[source,terminal]
----
$ curl -k -X POST  "https://$ROUTE/api/v2/silences" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{
    "matchers": [
      {
        "name": "alertname",
        "value": "MyTestAlert1",
        "isRegex": false
      }
    ],
    "startsAt": "2044-01-01T00:00:00Z",
    "endsAt": "2044-01-01T00:00:01Z",
    "createdBy": "test-alertmanager-web-monitoring-alertmanager-edit/am-client",
    "comment": "Silence test"
  }'
----

. Access Alertmanager endpoints from within the cluster.
+
[source,terminal]
----
$ curl -k -X POST  "https://alertmanager-main.openshift-monitoring:9094/api/v2/silences" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{
    "matchers": [
      {
        "name": "alertname",
        "value": "MyTestAlert2",
        "isRegex": false
      }
    ],
    "startsAt": "2044-01-01T00:00:00Z",
    "endsAt": "2044-01-01T00:00:01Z",
    "createdBy": "test-alertmanager-web-monitoring-alertmanager-edit/am-client",
    "comment": "Silence test"
  }'
----

* Port 9092 provides access to the Alertmanager endpoints restricted to a given project. Granting access requires binding a user to the `monitoring-rules-edit` cluster role or `monitoring-edit` cluster role in the project.

Example monitoring-rules-edit permissions::
+
The following example exercises permissions granted by the `monitoring-rules-edit` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-alertmanager-tenancy-monitoring-rules-edit
----
+
[source,terminal]
----
$ oc create serviceaccount am-client --namespace=test-alertmanager-tenancy-monitoring-rules-edit
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-alertmanager-tenancy-monitoring-rules-edit \
  --namespace=test-alertmanager-tenancy-monitoring-rules-edit \
  --clusterrole=monitoring-rules-edit \
  --serviceaccount=test-alertmanager-tenancy-monitoring-rules-edit:am-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token am-client --namespace=test-alertmanager-tenancy-monitoring-rules-edit)
----

. Access Alertmanager endpoints from within the cluster. The port is not exposed externally by default.
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://alertmanager-main.openshift-monitoring:9092/api/v2/alerts?namespace=test-alertmanager-tenancy-monitoring-rules-edit"
----
+
[source,terminal]
----
$ curl -k -X POST -f "https://alertmanager-main.openshift-monitoring:9092/api/v2/silences?namespace=test-alertmanager-tenancy-monitoring-rules-edit" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{
    "matchers": [
      {
        "name": "alertname",
        "value": "MyTestAlert",
        "isRegex": false
      }
    ],
    "startsAt": "2044-01-01T00:00:00Z",
    "endsAt": "2044-01-01T00:00:01Z",
    "createdBy": "test-alertmanager-tenancy-monitoring-rules-edit/am-client",
    "comment": "Silence test"
  }'
----

Example monitoring-edit permissions::
+
The following example exercises permissions granted by the `monitoring-edit` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-alertmanager-tenancy-monitoring-edit
----
+
[source,terminal]
----
$ oc create serviceaccount am-client --namespace=test-alertmanager-tenancy-monitoring-edit
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-alertmanager-tenancy-monitoring-edit \
  --namespace=test-alertmanager-tenancy-monitoring-edit \
  --clusterrole=monitoring-edit \
  --serviceaccount=test-alertmanager-tenancy-monitoring-edit:am-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token am-client --namespace=test-alertmanager-tenancy-monitoring-edit)
----

. Access Alertmanager endpoints from within the cluster. The port is not exposed externally by default.
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://alertmanager-main.openshift-monitoring:9092/api/v2/alerts?namespace=test-alertmanager-tenancy-monitoring-edit"
----
+
[source,terminal]
----
$ curl -k -X POST -f "https://alertmanager-main.openshift-monitoring:9092/api/v2/silences?namespace=test-alertmanager-tenancy-monitoring-edit" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{
    "matchers": [
      {
        "name": "alertname",
        "value": "MyTestAlert",
        "isRegex": false
      }
    ],
    "startsAt": "2044-01-01T00:00:00Z",
    "endsAt": "2044-01-01T00:00:01Z",
    "createdBy": "test-alertmanager-tenancy-monitoring-edit/am-client",
    "comment": "Silence test"
  }'
----

* Port 9097 provides access to the `/metrics` endpoint only. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/kube-state-metrics

Expose kube-state-metrics `/metrics` endpoints within the cluster on the following ports:

* Port 8443 provides access to the Kubernetes resource metrics. This port is for internal use, and no other usage is guaranteed.
* Port 9443 provides access to the internal kube-state-metrics metrics. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/metrics-server

Expose the metrics-server web server on port 443. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/monitoring-plugin

Expose the monitoring plugin service on port 9443. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/node-exporter

Expose the `/metrics` endpoint on port 9100. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/openshift-state-metrics

Expose openshift-state-metrics `/metrics` endpoints within the cluster on the following ports:

* Port 8443 provides access to the OpenShift resource metrics. This port is for internal use, and no other usage is guaranteed.
* Port 9443 provides access to the internal `openshift-state-metrics` metrics. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/prometheus-k8s

Expose the Prometheus web server within the cluster on the following ports:

* Port 9091 provides access to all the Prometheus endpoints. Granting access requires binding a user to the `cluster-monitoring-view` cluster role or `cluster-monitoring-metrics-api` cluster role in the `openshift-monitoring` project.

Example cluster-monitoring-view permissions::
+
The following example exercises permissions granted by the `cluster-monitoring-view` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-prometheus-web-cluster-monitoring-view
----
+
[source,terminal]
----
$ oc create serviceaccount prom-client --namespace=test-prometheus-web-cluster-monitoring-view
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-prometheus-web-cluster-monitoring-view \
  --namespace=openshift-monitoring \
  --clusterrole=cluster-monitoring-view \
  --serviceaccount=test-prometheus-web-cluster-monitoring-view:prom-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token prom-client --namespace=test-prometheus-web-cluster-monitoring-view)
----

. Access Prometheus endpoints externally.
+
[source,terminal]
----
$ ROUTE=$(oc get route prometheus-k8s --namespace=openshift-monitoring -ojsonpath={.spec.host})
----
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://$ROUTE/api/v1/query?query=up"
----

. Access Prometheus endpoints from within the cluster.
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://prometheus-k8s.openshift-monitoring:9091/api/v1/query?query=up"
----

Example cluster-monitoring-metrics-api permissions::
+
The following example exercises permissions granted by the `cluster-monitoring-metrics-api` role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-prometheus-web-cluster-monitoring-metrics-api
----
+
[source,terminal]
----
$ oc create serviceaccount prom-client --namespace=test-prometheus-web-cluster-monitoring-metrics-api
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-prometheus-web-cluster-monitoring-metrics-api \
  --namespace=openshift-monitoring \
  --role=cluster-monitoring-metrics-api  \
  --serviceaccount=test-prometheus-web-cluster-monitoring-metrics-api:prom-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token prom-client --namespace=test-prometheus-web-cluster-monitoring-metrics-api)
----

. Access Prometheus endpoints externally.
+
[source,terminal]
----
$ ROUTE=$(oc get route prometheus-k8s --namespace=openshift-monitoring -ojsonpath={.spec.host})
----
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://$ROUTE/api/v1/query?query=up"
----

. Access Prometheus endpoints from within the cluster.
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://prometheus-k8s.openshift-monitoring:9091/api/v1/query?query=up"
----

* Port 9092 provides access to the `/metrics` and `/federate` endpoints only. This port is for internal use, and no other usage is guaranteed.

=== openshift-user-workload-monitoring/prometheus-operator

Expose the `/metrics` endpoint on port 8443. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/prometheus-operator

Expose the `/metrics` endpoint on port 8443. This port is for internal use, and no other usage is guaranteed.

=== openshift-user-workload-monitoring/prometheus-user-workload

Expose the Prometheus web server within the cluster on the following ports:

* Port 9091 provides access to the `/metrics` endpoint only. This port is for internal use, and no other usage is guaranteed.
* Port 9092 provides access to the `/federate` endpoint only. Granting access requires binding a user to the `cluster-monitoring-view` cluster role.

This also exposes the `/metrics` endpoint of the Thanos sidecar web server on port 10902. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/telemeter-client

Expose the `/metrics` endpoint on port 8443. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/thanos-querier

Expose the Thanos Querier web server within the cluster on the following ports:

* Port 9091 provides access to all the Thanos Querier endpoints. Granting access requires binding a user to the `cluster-monitoring-view` cluster role or `cluster-monitoring-metrics-api` cluster role in the `openshift-monitoring` project.

Example cluster-monitoring-view permissions::
+
The following example exercises permissions granted by the `cluster-monitoring-view` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-thanos-querier-web-cluster-monitoring-view
----
+
[source,terminal]
----
$ oc create serviceaccount thanos-client --namespace=test-thanos-querier-web-cluster-monitoring-view
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-thanos-querier-web-cluster-monitoring-view \
  --namespace=openshift-monitoring \
  --clusterrole=cluster-monitoring-view \
  --serviceaccount=test-thanos-querier-web-cluster-monitoring-view:thanos-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token thanos-client --namespace=test-thanos-querier-web-cluster-monitoring-view)
----

. Access Thanos Querier endpoints externally.
+
[source,terminal]
----
$ ROUTE=$(oc get route thanos-querier --namespace=openshift-monitoring -ojsonpath={.spec.host})
----
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://$ROUTE/api/v1/query?query=up"
----

. Access Thanos Querier endpoints from within the cluster.
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9091/api/v1/query?query=up"
----

Example cluster-monitoring-metrics-api permissions::
+
The following example exercises permissions granted by the `cluster-monitoring-metrics-api` role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-thanos-querier-web-cluster-monitoring-metrics-api
----
+
[source,terminal]
----
$ oc create serviceaccount thanos-client --namespace=test-thanos-querier-web-cluster-monitoring-metrics-api
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-thanos-querier-web-cluster-monitoring-metrics-api \
  --namespace=openshift-monitoring \
  --role=cluster-monitoring-metrics-api  \
  --serviceaccount=test-thanos-querier-web-cluster-monitoring-metrics-api:thanos-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token thanos-client --namespace=test-thanos-querier-web-cluster-monitoring-metrics-api)
----

. Access Thanos Querier endpoints externally.
+
[source,terminal]
----
$ ROUTE=$(oc get route thanos-querier --namespace=openshift-monitoring -ojsonpath={.spec.host})
----
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://$ROUTE/api/v1/query?query=up"
----

. Access Thanos Querier endpoints from within the cluster.
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9091/api/v1/query?query=up"
----

* Port 9092 provides access to the `/api/v1/query`, `/api/v1/query_range/`, `/api/v1/labels`, `/api/v1/label/*/values`, and `/api/v1/series` endpoints restricted to a given project. Granting access requires binding a user to the `view` cluster role in the project.

Example view permissions::
+
The following example exercises permissions granted by the `view` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-thanos-querier-tenancy-view
----
+
[source,terminal]
----
$ oc create serviceaccount thanos-client --namespace=test-thanos-querier-tenancy-view
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-thanos-querier-tenancy-view \
  --namespace=test-thanos-querier-tenancy-view \
  --clusterrole=view \
  --serviceaccount=test-thanos-querier-tenancy-view:thanos-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token thanos-client --namespace=test-thanos-querier-tenancy-view)
----

. Access Thanos Querier endpoints from within the cluster. The port is not exposed externally by default.
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9092/api/v1/query?query=up&namespace=test-thanos-querier-tenancy-view"
----

* Port 9093 provides access to the `/api/v1/alerts`, and `/api/v1/rules` endpoints restricted to a given project. Granting access requires binding a user to the `monitoring-rules-edit`, `monitoring-edit`, or `monitoring-rules-view` cluster role in the project.

Example monitoring-rules-edit permissions::
+
The following example exercises permissions granted by the `monitoring-rules-edit` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-thanos-querier-tenancy-rules-monitoring-rules-edit
----
+
[source,terminal]
----
$ oc create serviceaccount thanos-client --namespace=test-thanos-querier-tenancy-rules-monitoring-rules-edit
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-thanos-querier-tenancy-rules-monitoring-rules-edit \
  --namespace=test-thanos-querier-tenancy-rules-monitoring-rules-edit \
  --clusterrole=monitoring-rules-edit \
  --serviceaccount=test-thanos-querier-tenancy-rules-monitoring-rules-edit:thanos-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token thanos-client --namespace=test-thanos-querier-tenancy-rules-monitoring-rules-edit)
----

. Access Thanos Querier endpoints from within the cluster. The port is not exposed externally by default.
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9093/api/v1/rules?namespace=test-thanos-querier-tenancy-rules-monitoring-rules-edit"
----
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9093/api/v1/alerts?namespace=test-thanos-querier-tenancy-rules-monitoring-rules-edit"
----

Example monitoring-edit permissions::
+
The following example exercises permissions granted by the `monitoring-edit` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-thanos-querier-tenancy-rules-monitoring-edit
----
+
[source,terminal]
----
$ oc create serviceaccount thanos-client --namespace=test-thanos-querier-tenancy-rules-monitoring-edit
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-thanos-querier-tenancy-rules-monitoring-edit \
  --namespace=test-thanos-querier-tenancy-rules-monitoring-edit \
  --clusterrole=monitoring-edit \
  --serviceaccount=test-thanos-querier-tenancy-rules-monitoring-edit:thanos-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token thanos-client --namespace=test-thanos-querier-tenancy-rules-monitoring-edit)
----

. Access Thanos Querier endpoints from within the cluster. The port is not exposed externally by default.
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9093/api/v1/rules?namespace=test-thanos-querier-tenancy-rules-monitoring-edit"
----
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9093/api/v1/alerts?namespace=test-thanos-querier-tenancy-rules-monitoring-edit"
----

Example monitoring-rules-view permissions::
+
The following example exercises permissions granted by the `monitoring-rules-view` cluster role. The binding commands must be run by a user with the necessary privileges.

. Create a test namespace and a service account.
+
[source,terminal]
----
$ oc create namespace test-thanos-querier-tenancy-rules-monitoring-rules-view
----
+
[source,terminal]
----
$ oc create serviceaccount thanos-client --namespace=test-thanos-querier-tenancy-rules-monitoring-rules-view
----

. Bind the role to the service account. The binding in this example is applied to a service account but can also be applied to any user.
+
[source,terminal]
----
$ oc create rolebinding test-thanos-querier-tenancy-rules-monitoring-rules-view \
  --namespace=test-thanos-querier-tenancy-rules-monitoring-rules-view \
  --clusterrole=monitoring-rules-view \
  --serviceaccount=test-thanos-querier-tenancy-rules-monitoring-rules-view:thanos-client
----

. Generate a token to access the endpoints.
+
[source,terminal]
----
$ TOKEN=$(oc create token thanos-client --namespace=test-thanos-querier-tenancy-rules-monitoring-rules-view)
----

. Access Thanos Querier endpoints from within the cluster. The port is not exposed externally by default.
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9093/api/v1/rules?namespace=test-thanos-querier-tenancy-rules-monitoring-rules-view"
----
+
[source,terminal]
----
$ curl -k -f -H "Authorization: Bearer $TOKEN" "https://thanos-querier.openshift-monitoring:9093/api/v1/alerts?namespace=test-thanos-querier-tenancy-rules-monitoring-rules-view"
----

* Port 9094 provides access to the `/metrics` endpoint only. This port is for internal use, and no other usage is guaranteed.

=== openshift-user-workload-monitoring/thanos-ruler

Expose the Thanos Ruler web server within the cluster on the following ports:

* Port 9091 provides access to all Thanos Ruler endpoints. Granting access requires binding a user to the `cluster-monitoring-view` cluster role.
* Port 9092 provides access to the `/metrics` endpoint only. This port is for internal use, and no other usage is guaranteed.

This also exposes the gRPC endpoints on port 10901. This port is for internal use, and no other usage is guaranteed.

=== openshift-monitoring/cluster-monitoring-operator

Expose the `/metrics` and `/validate-webhook` endpoints on port 8443. This port is for internal use, and no other usage is guaranteed.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Enabling monitoring for user-defined projects
* Configuring remote write storage for core platform monitoring
* Configuring remote write storage for monitoring of user-defined projects
* Accessing metrics as an administrator
* Accessing metrics as a developer
* Managing alerts as an Administrator
* Managing alerts as a Developer
