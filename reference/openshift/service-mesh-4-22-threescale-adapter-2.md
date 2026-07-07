---
title: "Using the 3scale Istio adapter"
type: reference
domain: openshift
slug: service-mesh-4-22-threescale-adapter-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/threescale-adapter
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Using the 3scale Istio adapter

[id="threescale-adapter-v1x"]
= Using the 3scale Istio adapter

The 3scale Istio Adapter is an optional adapter that allows you to label a service running within the {SMProductName} and integrate that service with the 3scale API Management solution.
It is not required for {SMProductName}.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-integrate-1x_{context}"]
= Integrate the 3scale adapter with {SMProductName}

You can use these examples to configure requests to your services using the 3scale Istio Adapter.

.Prerequisites

* {SMProductName} version 1.x
* A working 3scale account (SaaS or 3scale 2.5 On-Premises)
* Enabling backend cache requires 3scale 2.9 or greater
* {SMProductName} prerequisites

[NOTE]
====
To configure the 3scale Istio Adapter, refer to {SMProductName} custom resources for instructions on adding adapter parameters to the custom resource file.
====

[NOTE]
====
Pay particular attention to the `kind: handler` resource. You must update this with your 3scale account credentials. You can optionally add a `service_id` to a handler, but this is kept for backwards compatibility only, since it would render the handler only useful for one service in your 3scale account. If you add `service_id` to a handler, enabling 3scale for other services requires you to create more handlers with different `service_ids`.
====

Use a single handler per 3scale account by following the steps below:

.Procedure

. Create a handler for your 3scale account and specify your account credentials. Omit any service identifier.
+
[source,yaml]
----
  apiVersion: "config.istio.io/v1alpha2"
  kind: handler
  metadata:
   name: threescale
  spec:
   adapter: threescale
   params:
     system_url: "https://<organization>-admin.3scale.net/"
     access_token: "<ACCESS_TOKEN>"
   connection:
     address: "threescale-istio-adapter:3333"
----
+
Optionally, you can provide a `backend_url` field within the _params_ section to override the URL provided by the 3scale configuration. This may be useful if the adapter runs on the same cluster as the 3scale on-premise instance, and you wish to leverage the internal cluster DNS.
+
. Edit or patch the Deployment resource of any services belonging to your 3scale account as follows:
.. Add the `"service-mesh.3scale.net/service-id"` label with a value corresponding to a valid `service_id`.
.. Add the `"service-mesh.3scale.net/credentials"` label with its value being the _name of the handler resource_ from step 1.
. Do step 2 to link it to your 3scale account credentials and to its service identifier, whenever you intend to add more services.
. Modify the rule configuration with your 3scale configuration to dispatch the rule to the threescale handler.
+
.Rule configuration example
[source,yaml]
----
  apiVersion: "config.istio.io/v1alpha2"
  kind: rule
  metadata:
    name: threescale
  spec:
    match: destination.labels["service-mesh.3scale.net"] == "true"
    actions:
      - handler: threescale.handler
        instances:
          - threescale-authorization.instance
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-cr_{context}"]
= Generating 3scale custom resources

The adapter includes a tool that allows you to generate the `handler`, `instance`, and `rule` custom resources.

.Usage
|===
|Option |Description |Required | Default value

|`-h, --help`
|Produces help output for available options
|No
|

|`--name`
|Unique name for this URL, token pair
|Yes
|

|`-n, --namespace`
|Namespace to generate templates
|No
|istio-system

|`-t, --token`
|3scale access token
|Yes
|

|`-u, --url`
|3scale Admin Portal URL
|Yes
|

|`--backend-url`
|3scale backend URL. If set, it overrides the value that is read from system configuration
|No
|

|`-s, --service`
|3scale API/Service ID
|No
|

|`--auth`
|3scale authentication pattern to specify (1=API Key, 2=App Id/App Key, 3=OIDC)
|No
|Hybrid

|`-o, --output`
|File to save produced manifests to
|No
|Standard output

|`--version`
|Outputs the CLI version and exits immediately
|No
|
|===

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-templates_{context}"]
= Generate templates from URL examples

[NOTE]
====
* Run the following commands via `oc exec` from the 3scale adapter container image in Generating manifests from a deployed adapter.
* Use the `3scale-config-gen` command to help avoid YAML syntax and indentation errors.
* You can omit the `--service` if you use the annotations.
* This command must be invoked from within the container image via `oc exec`.
====

.Procedure

* Use the `3scale-config-gen` command to autogenerate templates files allowing the token, URL pair to be shared by multiple services as a single handler:
+
----
$ 3scale-config-gen --name=admin-credentials --url="https://<organization>-admin.3scale.net:443" --token="[redacted]"
----
+
* The following example generates the templates with the service ID embedded in the handler:
+
----
$ 3scale-config-gen --url="https://<organization>-admin.3scale.net" --name="my-unique-id" --service="123456789" --token="[redacted]"
----

[role="_additional-resources"]
.Additional resources
* Tokens.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-manifests_{context}"]
= Generating manifests from a deployed adapter

[NOTE]
====
* `NAME` is an identifier you use to identify with the service you are managing with 3scale.
* The `CREDENTIALS_NAME` reference is an identifier that corresponds to the `match` section in the rule configuration. This is automatically set to the `NAME` identifier if you are using the CLI tool.
* Its value does not need to be anything specific: the label value should just match the contents of the rule. See Routing service traffic through the adapter for more information.
====

. Run this command to generate manifests from a deployed adapter in the `istio-system` namespace:
+
----
$ export NS="istio-system" URL="https://replaceme-admin.3scale.net:443" NAME="name" TOKEN="token"
oc exec -n ${NS} $(oc get po -n ${NS} -o jsonpath='{.items[?(@.metadata.labels.app=="3scale-istio-adapter")].metadata.name}') \
-it -- ./3scale-config-gen \
--url ${URL} --name ${NAME} --token ${TOKEN} -n ${NS}
----

. This will produce sample output to the terminal. Edit these samples if required and create the objects using the `oc create` command.

. When the request reaches the adapter, the adapter needs to know how the service maps to an API on 3scale. You can provide this information in two ways:

.. Label the workload (recommended)
.. Hard code the handler as `service_id`

. Update the workload with the required annotations:
+
[NOTE]
====
You only need to update the service ID provided in this example if it is not already embedded in the handler. *The setting in the handler takes precedence*.
====
+
----
$ export CREDENTIALS_NAME="replace-me"
export SERVICE_ID="replace-me"
export DEPLOYMENT="replace-me"
patch="$(oc get deployment "${DEPLOYMENT}"
patch="$(oc get deployment "${DEPLOYMENT}" --template='{"spec":{"template":{"metadata":{"labels":{ {{ range $k,$v := .spec.template.metadata.labels }}"{{ $k }}":"{{ $v }}",{{ end }}"service-mesh.3scale.net/service-id":"'"${SERVICE_ID}"'","service-mesh.3scale.net/credentials":"'"${CREDENTIALS_NAME}"'"}}}}}' )"
oc patch deployment "${DEPLOYMENT}" --patch ''"${patch}"''

----

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-routing_{context}"]
= Routing service traffic through the adapter
Follow these steps to drive traffic for your service through the 3scale adapter.

.Prerequisites

* Credentials and service ID from your 3scale administrator.

.Procedure

. Match the rule `destination.labels["service-mesh.3scale.net/credentials"] == "threescale"` that you previously created in the configuration, in the `kind: rule` resource.

. Add the above label to `PodTemplateSpec` on the Deployment of the target workload to integrate a service. the value, `threescale`, refers to the name of the generated handler. This handler stores the access token required to call 3scale.

. Add the `destination.labels["service-mesh.3scale.net/service-id"] == "replace-me"` label to the workload to pass the service ID to the adapter via the instance at request time.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-integration-settings_{context}"]
= Configure the integration settings in 3scale

Follow this procedure to configure the 3scale integration settings.

[NOTE]
====
For 3scale SaaS customers, {SMProductName} is enabled as part of the Early Access program.
====

.Procedure

. Navigate to *[your_API_name]* -> *Integration*

. Click *Settings*.

. Select the *Istio* option under _Deployment_.
+
* The *API Key (user_key)* option under _Authentication_ is selected by default.

. Click *Update Product* to save your selection.

. Click *Configuration*.

. Click *Update Configuration*.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-caching_{context}"]
= Caching behavior
Responses from 3scale System APIs are cached by default within the adapter. Entries will be purged from the cache when they become older than the `cacheTTLSeconds` value. Also by default, automatic refreshing of cached entries will be attempted seconds before they expire, based on the `cacheRefreshSeconds` value. You can disable automatic refreshing by setting this value higher than the `cacheTTLSeconds` value.

Caching can be disabled entirely by setting `cacheEntriesMax` to a non-positive value.

By using the refreshing process, cached values whose hosts become unreachable will be retried before eventually being purged when past their expiry.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-authentication_{context}"]
= Authenticating requests
This release supports the following authentication methods:

* *Standard API Keys*: single randomized strings or hashes acting as an identifier and a secret token.
* *Application identifier and key pairs*: immutable identifier and mutable secret key strings.
* *OpenID authentication method*: client ID string parsed from the JSON Web Token.

[id="ossm-threescale-authentication-patterns_{context}"]
== Applying authentication patterns
Modify the `instance` custom resource, as illustrated in the following authentication method examples, to configure authentication behavior. You can accept the authentication credentials from:

* Request headers
* Request parameters
* Both request headers and query parameters

[NOTE]
====
When specifying values from headers, they must be lower case. For example, if you want to send a header as `User-Key`, this must be referenced in the configuration as `request.headers["user-key"]`.
====

[id="ossm-threescale-apikey-authentication_{context}"]
=== API key authentication method
{SMProductShortName} looks for the API key in query parameters and request headers as specified in the `user` option in the `subject` custom resource parameter. It checks the values in the order given in the custom resource file. You can restrict the search for the API key to either query parameters or request headers by omitting the unwanted option.

In this example, {SMProductShortName} looks for the API key in the `user_key` query parameter. If the API key is not in the query parameter, {SMProductShortName} then checks the `user-key` header.

.API key authentication method example

[source,yaml]
----
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
  namespace: istio-system
spec:
  template: authorization
  params:
    subject:
      user: request.query_params["user_key"] | request.headers["user-key"] | ""
    action:
      path: request.url_path
      method: request.method | "get"
----

If you want the adapter to examine a different query parameter or request header, change the name as appropriate. For example, to check for the API key in a query parameter named “key”, change `request.query_params["user_key"]` to `request.query_params["key"]`.

[id="ossm-threescale-appidapikey-authentication_{context}"]
=== Application ID and application key pair authentication method
{SMProductShortName} looks for the application ID and application key in query parameters and request headers, as specified in the `properties` option in the `subject` custom resource parameter. The application key is optional. It checks the values in the order given in the custom resource file. You can restrict the search for the credentials to either query parameters or request headers by not including the unwanted option.

In this example, {SMProductShortName} looks for the application ID and application key in the query parameters first, moving on to the request headers if needed.

.Application ID and application key pair authentication method example

[source,yaml]
----
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
  namespace: istio-system
spec:
  template: authorization
  params:
    subject:
        app_id: request.query_params["app_id"] | request.headers["app-id"] | ""
        app_key: request.query_params["app_key"] | request.headers["app-key"] | ""
    action:
      path: request.url_path
      method: request.method | "get"
----

If you want the adapter to examine a different query parameter or request header, change the name as appropriate. For example, to check for the application ID in a query parameter named `identification`, change `request.query_params["app_id"]` to `request.query_params["identification"]`.

[id="ossm-threescale-openid-authentication_{context}"]
=== OpenID authentication method
To use the _OpenID Connect (OIDC) authentication method_, use the `properties` value on the `subject` field to set `client_id`, and optionally `app_key`.

You can manipulate this object using the methods described previously. In the example configuration shown below, the client identifier (application ID) is parsed from the JSON Web Token (JWT) under the label _azp_. You can modify this as needed.

.OpenID authentication method example

[source,yaml]
----
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
spec:
  template: threescale-authorization
  params:
    subject:
      properties:
        app_key: request.query_params["app_key"] | request.headers["app-key"] | ""
        client_id: request.auth.claims["azp"] | ""
      action:
        path: request.url_path
        method: request.method | "get"
        service: destination.labels["service-mesh.3scale.net/service-id"] | ""
----

For this integration to work correctly, OIDC must still be done in 3scale for the client to be created in the identity provider (IdP). You should create a Request authorization for the service you want to protect in the same namespace as that service. The JWT is passed in the `Authorization` header of the request.

In the sample `RequestAuthentication` defined below, replace `issuer`, `jwksUri`, and `selector` as appropriate.

.OpenID Policy example

[source,yaml]
----
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: jwt-example
  namespace: bookinfo
spec:
  selector:
    matchLabels:
      app: productpage
  jwtRules:
  - issuer: >-
      http://keycloak-keycloak.34.242.107.254.nip.io/auth/realms/3scale-keycloak
    jwksUri: >-
      http://keycloak-keycloak.34.242.107.254.nip.io/auth/realms/3scale-keycloak/protocol/openid-connect/certs
----

[id="ossm-threescale-hybrid-authentication_{context}"]
=== Hybrid authentication method
You can choose to not enforce a particular authentication method and accept any valid credentials for either method. If both an API key and an application ID/application key pair are provided, {SMProductShortName} uses the API key.

In this example, {SMProductShortName} checks for an API key in the query parameters, then the request headers. If there is no API key, it then checks for an application ID and key in the query parameters, then the request headers.

.Hybrid authentication method example

[source,yaml]
----
apiVersion: "config.istio.io/v1alpha2"
kind: instance
metadata:
  name: threescale-authorization
spec:
  template: authorization
  params:
    subject:
      user: request.query_params["user_key"] | request.headers["user-key"] |
      properties:
        app_id: request.query_params["app_id"] | request.headers["app-id"] | ""
        app_key: request.query_params["app_key"] | request.headers["app-key"] | ""
        client_id: request.auth.claims["azp"] | ""
    action:
      path: request.url_path
      method: request.method | "get"
      service: destination.labels["service-mesh.3scale.net/service-id"] | ""
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-metrics-1x_{context}"]
= 3scale Adapter metrics
The adapter, by default reports various Prometheus metrics that are exposed on port `8080` at the `/metrics` endpoint. These metrics provide insight into how the interactions between the adapter and 3scale are performing. The service is labeled to be automatically discovered and scraped by Prometheus.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-istio-adapter-verification_{context}"]
= 3scale Istio adapter verification

You might want to check whether the 3scale Istio adapter is working as expected. If your adapter is not working, use the following steps to help troubleshoot the problem.

.Procedure

. Ensure the _3scale-adapter_ pod is running in the {SMProductShortName} control plane namespace:
+
[source,terminal]
----
$ oc get pods -n istio-system
----
. Check that the _3scale-adapter_ pod has printed out information about itself booting up, such as its version:
+
[source,terminal]
----
$ oc logs istio-system
----
. When performing requests to the services protected by the 3scale adapter integration, always try requests that lack the right credentials and ensure they fail. Check the 3scale adapter logs to gather additional information.

[role="_additional-resources"]
.Additional resources
* Inspecting pod and container logs.

// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-istio-adapter-troubleshooting-checklist_{context}"]
= 3scale Istio adapter troubleshooting checklist

As the administrator installing the 3scale Istio adapter, there are a number of scenarios that might be causing your integration to not function properly. Use the following list to troubleshoot your installation:

* Incorrect YAML indentation.
* Missing YAML sections.
* Forgot to apply the changes in the YAML to the cluster.
* Forgot to label the service workloads with the `service-mesh.3scale.net/credentials` key.
* Forgot to label the service workloads with `service-mesh.3scale.net/service-id` when using handlers that do not contain a `service_id` so they are reusable per account.
* The _Rule_ custom resource points to the wrong handler or instance custom resources, or the references lack the corresponding namespace suffix.
* The _Rule_ custom resource `match` section cannot possibly match the service you are configuring, or it points to a destination workload that is not currently running or does not exist.
* Wrong access token or URL for the 3scale Admin Portal in the handler.
* The _Instance_ custom resource's `params/subject/properties` section fails to list the right parameters for `app_id`, `app_key`, or `client_id`, either because they specify the wrong location such as the query parameters, headers, and authorization claims, or the parameter names do not match the requests used for testing.
* Failing to use the configuration generator without realizing that it actually lives in the adapter container image and needs `oc exec` to invoke it.
