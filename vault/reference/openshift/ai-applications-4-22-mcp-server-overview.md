---
title: "Inspect clusters with MCP server for Red Hat {product-title}"
type: reference
domain: openshift
slug: ai-applications-4-22-mcp-server-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_applications/mcp-server-overview
version: 4.22
family: ai_applications
documentKind: "Documentation"
---

# Inspect clusters with MCP server for Red Hat {product-title}

[id="mcp-server-overview"]
= Inspect clusters with MCP server for Red Hat OpenShift Container Platform

[role="_abstract"]
When a problem occurs on your OpenShift Container Platform cluster, you want to determine exactly what is happening, so that you can fix the issue as soon as possible. The MCP server for Red Hat OpenShift Container Platform feature provides an AI tool for this purpose to quickly and easily diagnose your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-ai-safety_{context}"]
= AI safety

[role="_abstract"]
When using MCP (Model Context Protocol) server for Red Hat OpenShift Container Platform, it is advised that you adhere to the following AI safety processes and best practices.

[IMPORTANT]
====
This feature uses AI technology. Do not include any personal information or other sensitive information in your input. Interactions may be used to improve Red Hat's products or services. Always review AI-generated content before using it.
====

[id="ai-app-mcp-server-ai-safety-data-ownership_{context}"]
== Data ownership
The MCP server for Red Hat OpenShift Container Platform does not store any information or state of the cluster. If you opt in, there are several telemetry metrics that are collected to understand the overall usage levels of the MCP server for Red Hat OpenShift Container Platform:

* Cluster:k8s_mcp_tool_calls:sum:

* Total count of all MCP tool invocations across the cluster

* Cluster:k8s_mcp_tool_errors:sum:

* Total count of all failed MCP tool invocations across the cluster

* Cluster:k8s_mcp_http_requests:sum:

* Total count of all HTTP requests received by the MCP server

These metrics do not collect specific details of the calls, requests, or errors themselves; they only provide aggregate overall sums of the usage.

To opt in, edit TOML config:
[source,toml]
----
[telemetry]
enabled = true
----

To opt out, edit TOML config:

[source,toml]
----
[telemetry]
enabled = false
----

[id="ai-app-mcp-server-ai-safety-hitl_{context}"]
== Required verification workflow: Human in the loop (HITL) enforcement

* It is recommended that you assess the AI agent's proposed action in the MCP client.

* You should manually check suggested resource versions (for example, ensure the model is not suggesting deprecated APIs).

* It is recommended that you use a human approval mechanism in the AI client interface for "write" actions.

[id="ai-app-mcp-server-ai-safety-privacy-redaction_{context}"]
== Data privacy and redaction
The MCP server for Red Hat OpenShift Container Platform has no internal mechanisms for PII and data redaction. To ensure that cluster information within allowed Custom Resources (CRs) complies with data privacy standards, deploy TrustyAI to monitor and sanitize outgoing payloads. For how to scope and limit MCP access to specific CRs, see Section _Revoke access to Custom Resources_.

[id="ai-app-mcp-server-ai-safety-audit-trail_{context}"]
== Audit trail recommendation
The MCP server for Red Hat OpenShift Container Platform is configured to append a user-agent string in audit logs to identify that requests were made by an AI agent through the MCP server. Ensure that authorization is enabled via OAuth or MCP gateway. For more information, see Section _Install MCP server for Red Hat OpenShift Container Platform_.

[id="ai-app-mcp-server-ai-safety-mcp-servers-hitl_{context}"]
== Recommendations regarding 3rd-party MCP servers
For better security and control, it is recommended that third-party MCP hosts implement a HITL requirement to approve any "write" operations performed via the MCP server for Red Hat OpenShift Container Platform.

[id="ai-app-mcp-server-ai-safety-governance-guardrails_{context}"]
== AI governance and guardrails
MCP gateway acts as a centralized control point and enforces strict governance over agent-tool interactions through centralized authentication and identity management, using correctly scoped tokens and OAuth 2.0 to ensure agents only possess the specific permissions required for any given task. The MCP gateway further secures the environment using identity-based tool filtering, which removes unauthorized tools from the tools/list discovery process entirely, thus preventing agents from attempting to access forbidden capabilities.

To mitigate AI-specific risks, the gateway should be deployed with safety guardrails. Guardrails would include inspecting traffic payloads for prompt injections and safety violations by integrating with external engines like Trusty AI or NVIDIA Nemo. Additionally, the MCP gateway ensures operational stability and accountability by implementing rate limiting to prevent agent-driven denial-of-service attacks and providing comprehensive audit logging to track and analyze all tool usage.

== Emergency removal of AI agent access
In an emergency, you can use any of the following possible actions to revoke access for the AI agent (via the MCP server):

* *Remove access to the offending tool* in `config.toml`.
+
Only enable specific tools:
+
[source,toml]
----
enabled_tools = ["pods_list", "pods_get", "pods_log"]
----

* *Disable specific tools* from enabled toolsets.
+
Disable destructive tool calls in `config.toml`.
+
[source,toml]
----
disabled_tools = ["resources_delete", "pods_delete"].
----

* *Create a production-safe configuration*.
+
[source,toml]
----
read_only = true
----

* *Allow writes, but prevent deletions*.
+
[source,toml]
----
disable_destructive = true
----

* *Uninstall the MCP server completely* by running the following command:
+
[source,terminal]
----
$ helm uninstall openshift-mcp-server
----

* *RBAC revocation*:
+
Remove the user's rolebinding or clusterrolebinding. For more information, see Section _Install MCP server for Red Hat OpenShift Container Platform_.

* *Remove access through the MCP gateway*
+
To remove access through the gateway, you can delete the MCPServerRegistration CR by running the following command:
+
[source,terminal]
----
$ oc delete mcpsr <name of registration>
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-model-context-protocol-overview_{context}"]
= Model Context Protocol overview

[role="_abstract"]
MCP (Model Context Protocol) is an open source standard for connecting AI applications to external systems.

Using MCP, AI applications, such as Claude Code or Cursor, can connect to the following items, enabling them to access key information and perform tasks:

* *Data sources*: for example, local files, databases

* *Tools*: for example, search engines, calculators

* *Workflows*: for example, specialized prompts

MCP works similarly to a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-mcp-server-overview_{context}"]
= MCP server overview

[role="_abstract"]
In the Model Context Protocol (MCP) ecosystem, the server's goal is to turn a specific data source or service into something an AI can understand and use.

== The Goals of an MCP server
The primary goal of an MCP server is to expose specific capabilities to an AI model in a structured, safe, and predictable way.
Here are the key objectives an MCP server achieves:

* *Capability exposure*: The server defines exactly what the AI is allowed to do or see. It does this by exposing three specific things:

** *Tools*: Executable functions that do things (for example, "Delete this file," "Post to Slack," or "Calculate mortgage").

** *Resources*: Read-only data sources that provide context (for example, "Read the contents of README.md" or "Fetch the logs from the last hour").

** *Prompts*: Predefined templates that guide the AI model's behavior (for example, a "Code Reviewer" prompt that tells the AI exactly how to look for bugs in a specific language).

* *Abstraction of complexity*: An MCP server hides the complicated parts of an integration. The LLM does not need to know how to write a SQL query or use a specific GitHub API. The server handles the code, the formatting, and the technical unique complexities, giving the LLM a clean, standardized result.

* *Execution and action*: Unlike the MCP gateway, which just routes traffic, the server is where the logic lives. When an AI decides to use a tool, the MCP server is the component that actually executes using that tool. For example, runs a Python script, queries a database, or calls an external API.

* *Sandboxing and security*: The server provides a layer of isolation. By running as a separate process, it can be restricted to only accessing specific folders or specific API endpoints. If the AI model attempts to undesired or unintended action, for example, tries to delete your entire hard drive, the server can deny the behavior based on its internal rules.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-mcp-gateway-overview_{context}"]
= MCP gateway overview

[role="_abstract"]
The primary goal of a Model Context Protocol (MCP) gateway is to standardize and simplify how AI models interact with external data and tools. Without a gateway, an AI model would need a custom integration for every single database, API, or local file system it needs to access.

== Aggregation and orchestration
A gateway connects to multiple MCP servers simultaneously. Instead of the LLM (Large Language Model) managing ten different connections, it communicates only with the gateway. The gateway then routes the LLM's request to the specific server that holds the relevant information (for example, fetching Jira tickets from one server and Google Drive docs from another).

== Security and access control
The gateway acts as a security perimeter.

It manages:

* *Authentication*: Holding the API keys or tokens required for various servers.

* *Permissions*: Ensuring the AI model only accesses the specific data or tools that the user authorized.

* *Privacy*: Stripping sensitive information before it is sent back to the model provider.

== Protocol translation
The gateway ensures that the communication between the AI model and the servers follows the MCP standard. It translates the high-level "intent" of the AI model into the specific JSON-RPC calls that the MCP servers understand.

== Scalability
By decoupling the AI model from the data sources, you can add, remove, or update MCP servers without ever needing to change the core configuration of your AI application.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-model-context-prompting-workflow_{context}"]
= MCP server for Red Hat OpenShift Container Platform Prompting workflow

[role="_abstract"]
Prompting in the Model Context Protocol (MCP) server for OpenShift Container Platform follows a specific workflow.

When you prompt a Large Language Model (LLM), the execution happens according to the following steps:

. User types a prompt: "Are there any pods that keep restarting?".

. MCP Host (for example, Claude Desktop): receives your prompt. It looks at its connected MCP servers and sees one has a tool called pods_list.

. MCP gateway (If used): If you are in an enterprise environment, the Host talks to the gateway first. The gateway checks "Is this user allowed to access the cluster?" and "Is the cluster currently online?"

. MCP server: The gateway (or Host) sends the command to the server. The server runs the actual code (the API call to OpenShift), gets the data, and sends it back.

. LLM: Receives that raw data, "reads" it, and gives you the final summary.

[id="ai-mcp-server-install_{context}"]
= Install MCP server for Red Hat OpenShift Container Platform

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, complete the following procedures.

.Prerequisites

* Access to OpenShift console with admin rights.
* Installed MCP-compatible client, such as Claude Code, Visual Studio Code (VS Code), Cursor, or OpenShift LightSpeed (OLS).

.Procedure

. Install the MCP server for Red Hat OpenShift Container Platform Helm chart.

. Connect an MCP-compatible client, such as Claude Code, to the MCP server.

. Install the MCP gateway.

. Verify the MCP gateway deployment.

. Configure the MCP gateway.

. Configure RBAC enforcement.

. Revoke access to Custom Resources.

. Set up the MCP gateway authentication.

. Set up MCP gateway authorization.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-install-helm_{context}"]
= Install the MCP server Helm chart

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, install the MCP server for Red Hat OpenShift Container Platform Helm chart.

.Prerequisites

* Access to OpenShift console with admin rights.

.Procedure

. Install the MCP server for Red Hat OpenShift Container Platform Helm chart by running one of the following commands:
+
* For read-only access (recommended for most use cases):
+
[source,terminal]
----
$ helm upgrade -i -n openshift-mcp-server --create-namespace openshift-mcp-server \
    openshift-helm-charts/redhat-openshift-mcp-server \
    --set config.toolsets=<toolset-names> \
    --set ingress.host=<hostname> \
    --set openshift=true \
    --set-json 'rbac.extraClusterRoleBindings=[{"name":"use-view-role","roleRef":{"name":"view","external":true}}]'
----
+
* For full cluster access:
+
[source,terminal]
----
$ helm upgrade -i -n openshift-mcp-server --create-namespace openshift-mcp-server \
    openshift-helm-charts/redhat-openshift-mcp-server \
    --set config.toolsets=<toolset-names> \
    --set ingress.host=<hostname> \
    --set openshift=true \
    --set-json 'rbac.extraClusterRoleBindings=[{"name":"admin-access","roleRef":{"name":"cluster-admin","external":true}}]'
----

* Where `<hostname>` is a fully qualified domain name (FQDN) that serves as the entry point for the OpenShift Container Platform MCP server. This host address is used by the Ingress controller to route external traffic to the MCP server service. This should be a URL such as `mcp-server.apps.cluster-name.domain.com`.

* Where `<toolset-names>` can include toolsets from the following table.
+
.Available toolsets
|===
|Toolset |Description |Default |Status

|`core`
|Most common tools for Kubernetes management (Pods, Generic Resources, Events, etc.)
|Yes
|Technology Preview

|`config`
|View and manage the current local Kubernetes configuration (kubeconfig)
|Yes
|Technology Preview

|`netedge`
|NetEdge troubleshooting tools for OpenShift Container Platform
|No
|Technology Preview

|`helm`
|Tools for managing Helm charts and releases
|No
|Technology Preview

|`metrics`
|Toolset for querying Prometheus and Alertmanager endpoints in efficient ways
|No
|Technology Preview

|`ossm`
|Most common tools for managing OSSM
|No
|Technology Preview

|`kubevirt`
|KubeVirt virtual machine management tools
|No
|Developer Preview

|`tekton`
|Tekton pipeline management tools for Pipelines, PipelineRuns, Tasks, and TaskRuns
|No
|Developer Preview
|===

.Verification

The command returns output similar to the following:

.Example
[source,terminal]
----
Release "openshift-mcp-server" does not exist. Installing it now.
NAME: openshift-mcp-server
LAST DEPLOYED: Mon Apr 20 09:28:13 2026
NAMESPACE: openshift-mcp-server
STATUS: deployed
REVISION: 1
TEST SUITE: None
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-connect-client_{context}"]
= Connect a client to the MCP server

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, connect an MCP-compatible client, such as Claude Code, to the MCP server.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.

.Procedure

. Add the following lines to your client configuration file:
+
* For Claude Desktop: `claude_desktop_config.json` file

* For Claude Code (CLI): `.mcp.json` file
+
[source,json]
----
{
  "mcpServers": {
    "openshift": {
      "type": "http",
      "url": "<url of the route created in the Helm chart>/mcp"
    }
  }
}
----
+
Where `<url of the route created in the Helm chart>` is the hostname you configured during Helm installation.

. Accept the CA certificate when prompted by the client.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-install-gateway_{context}"]
= Install the MCP gateway

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, install the MCP gateway to route traffic through security guardrails and authorization features.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.

.Procedure

. Install the MCP gateway.
+
For information about how to install the MCP gateway, see the _Red Hat Connectivity Link_ documentation, Section _Installing the MCP gateway_.
+
After installation, the controller automatically creates the HTTPRoute for gateway access. The MCP gateway acts as a reverse proxy that aggregates multiple MCP servers into a single endpoint and provides a layer for authentication and rate limiting.

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-verify-deployment_{context}"]
= Verify the MCP gateway deployment

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, verify that the MCP gateway is deployed and running correctly.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed.

.Procedure

. Check the status of your deployment by running the following command:
+
[source,terminal]
----
$ oc get pods -n mcp-system -l "app.kubernetes.io/instance=mcp-gateway"
----
+
[NOTE]
====
This example uses the namespace "mcp-system" for installing the gateway. If you install the gateway in a different namespace than "mcp-system", use that namespace instead throughout the procedure.
====
+
.Example
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
mcp-gateway-controller-594b9649cf-zstfw   1/1     Running   0          22s
----

. Ensure that the MCP gateway Extension exists by running the following command:
+
[source,terminal]
----
$ oc get mcpgatewayextension -A
----
+
.Example
+
[source,terminal]
----
NAMESPACE   NAME          READY   AGE
mcp-system  mcp-gateway           105s
----

. Verify the broker-router deployment by running the following command:
+
[source,terminal]
----
$ oc logs -n mcp-system deployment/mcp-gateway-broker-router
----

. Verify EnvoyFilter was created in the gateway namespace by running the following command:
+
[source,terminal]
----
$ oc get envoyfilter -n mcp-system -l app.kubernetes.io/managed-by=mcp-gateway-controller
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-configure-gateway_{context}"]
= Configure the MCP gateway

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, configure the MCP gateway by creating HTTPRoute and MCPServerRegistration resources.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.

.Procedure

. Create the HTTPRoute for the MCP server by running the following command:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: mcp-api-key-server-route
  namespace: openshift-mcp-server
spec:
  parentRefs:
  - group: gateway.networking.k8s.io
    kind: Gateway
    name: mcp-gateway
    namespace: gateway-system
    sectionName: mcp
  hostnames:
  - ${MCP_SERVER_HOST}
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /mcp
    backendRefs:
    - name: openshift-mcp-server
      port: 8080
EOF
----
+
Where `${MCP_SERVER_HOST}` is the hostname you configured during Helm installation.
+
This HTTPRoute enables the MCP gateway to route traffic to your MCP server instance and is referenced in the MCPServerRegistration resource.

. Create an MCP server Registration Resource by running the following command:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: mcp.kuadrant.io/v1alpha1
kind: MCPServerRegistration
metadata:
  name: my-mcp-server-reg
  namespace: openshift-mcp-server
spec:
  toolPrefix: "openshift_"
  targetRef:
    group: "gateway.networking.k8s.io"
    kind: "HTTPRoute"
    name: "mcp-api-key-server-route"
    namespace: openshift-mcp-server
EOF
----
* `metadata.name`: Provide a name for the MCP server registration object.

* `metadata.namespace`: The namespace for the MCP server, which is `openshift-mcp-server`.

* `spec.targetRef.name`:  The name of your MCP server HTTPRoute. You can find this by running the command: `oc get httproute -n openshift-mcp-server`.

* `spec.targetRef.namespace`: The namespace for the MCP server HTTPRoute, which is `openshift-mcp-server`.

. Verify the registration status by running the following commands:
+
[source,terminal]
----
$ oc wait --for=condition=Ready mcpsr/my-mcp-server-reg -n openshift-mcp-server --timeout=120s
$ oc get mcpsr -A
----
+
.Example
+
[source,terminal]
----
NAMESPACE             NAME                PREFIX      TARGET                     PATH   READY   TOOLS   CREDENTIALS   AGE
openshift-mcp-server  my-mcp-server-reg   myserver_   mcp-api-key-server-route   /mcp   True    4                     30s
----
+
The *READY* column should display `True` and the *TOOLS* column should show the number of tools discovered.
+
If the status is not ready, check the MCP server Registration conditions for details by running the following command:
+
[source,terminal]
----
$ oc describe mcpsr my-mcp-server-reg -n openshift-mcp-server
----

. Check the controller logs by running the following command:
+
[source,terminal]
----
$ oc logs -n mcp-system deployment/mcp-gateway-controller
----

. Check the broker logs for tool discovery by running the following command:
+
[source,terminal]
----
$ oc logs -n mcp-system deployment/mcp-gateway-broker-router
----

. Verify that your MCP server tools are available through the MCP gateway:

.. Initialize the MCP session and capture session ID by using -D to dump headers to a file, and then reading the session ID by running the following command:
+
[source,terminal]
----
$ curl -s -D /tmp/mcp_headers -X POST http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/mcp  \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}'
----
+
Where <cluster-name>.<domain-name> is the name and domain of your cluster.

.. Extract the MCP session ID from response headers by running the following commands:
+
[source,terminal]
----
$ SESSION_ID=$(grep -i "mcp-session-id:" /tmp/mcp_headers | cut -d' ' -f2 | tr -d '\r')

$ echo "MCP Session ID: $SESSION_ID"
----

.. List tools by using the session ID in the following command:
+
[source,terminal]
----
$ curl -X POST http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/mcp \
  -H "Content-Type: application/json" \
  -H "mcp-session-id: $SESSION_ID" \
  -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'
----
+
Where <cluster-name>.<domain-name> is the name and domain of your cluster.

.. Clean up by running the following command:
+
[source,terminal]
----
$ rm -f /tmp/mcp_headers
----
+
You should now see your MCP server tools in the response, prefixed with your configured toolPrefix (for example, myserver_).

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-configure-rbac_{context}"]
= Configure RBAC enforcement

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, configure role-based access control (RBAC) to control access to cluster resources through the MCP server. By default, RBAC is enabled, and you can extend the ClusterRoles, ClusterRoleBindings, Roles, and Rolebindings.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* The MCP gateway is configured.

.Procedure

. Configure RBAC enforcement by extending ClusterRoles, ClusterRoleBindings, Roles, and Rolebindings.
+
Use the following example RBAC YAML file to extend ClusterRoles, ClusterRoleBindings, Roles, and Rolebindings:
+
.Example RBAC settings YAML file
[source,yaml]
----
extraClusterRoles:
  - name: acm-managed-clusters
    rules:
      # Required for discovering and watching managed clusters
      - apiGroups: ["cluster.open-cluster-management.io"]
        resources: ["managedclusters"]
        verbs: ["list", "watch"]

# -- ClusterRoleBinding for the ACM managed clusters role
extraClusterRoleBindings:
  - name: acm-managed-clusters
    roleRef:
      name: acm-managed-clusters

# -- Role for accessing cluster-proxy-addon service in multicluster-engine namespace
extraRoles:
  - name: acm-cluster-proxy-discovery
    namespace: multicluster-engine
    rules:
      # Required for auto-discovering cluster-proxy-addon service
      - apiGroups: [""]
        resources: ["services"]
        verbs: ["get"]

# -- RoleBinding for the cluster-proxy-discovery role
extraRoleBindings:
  - name: acm-cluster-proxy-discovery
    namespace: multicluster-engine
    roleRef:
      name: acm-cluster-proxy-discovery
----

. Apply the RBAC configuration by saving the preceding example to a file (for example, `rbac-values.yaml`), and then run the following command:
+
[source,terminal]
----
$ helm upgrade openshift-mcp-server openshift-helm-charts/redhat-openshift-mcp-server \
    -n openshift-mcp-server \
    -f rbac-values.yaml
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-revoke-cr-access_{context}"]
= Revoke access to Custom Resources

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, revoke access to specific Custom Resource (CR) level resources to enhance security. It is highly recommended that you limit access to Secrets, ConfigMaps, and RBAC resources (RoleBindings, ClusterRoles).

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* The MCP gateway is configured.
* RBAC is configured.

.Procedure

. Configure denied resources to limit access to sensitive CRs.
+
Use the following example file to revoke access to Secrets, ConfigMaps, and RBAC resources:
+
.Example
[source,toml]
----
# Deny access to Secrets
[[denied_resources]]
group = ""
version = "v1"
kind = "Secret"

# Deny access to ConfigMaps
[[denied_resources]]
group = ""
version = "v1"
kind = "ConfigMap"

# Deny access to RBAC resources for additional security
[[denied_resources]]
group = "rbac.authorization.k8s.io"
version = "v1"
kind = "Role"

[[denied_resources]]
group = "rbac.authorization.k8s.io"
version = "v1"
kind = "RoleBinding"

[[denied_resources]]
group = "rbac.authorization.k8s.io"
version = "v1"
kind = "ClusterRole"

[[denied_resources]]
group = "rbac.authorization.k8s.io"
version = "v1"
kind = "ClusterRoleBinding"
----

. Apply this configuration by doing one of the following:
+
* Save the configuration to a file (for example, `deny-resources.toml`) and pass it using a Helm values file:
+
[source,terminal]
----
$ helm upgrade openshift-mcp-server openshift-helm-charts/redhat-openshift-mcp-server \
    -n openshift-mcp-server \
    --set-file config.deniedResources=deny-resources.toml
----
+
* Or use `--set-json` to pass the configuration inline:
+
[source,terminal]
----
$ helm upgrade openshift-mcp-server openshift-helm-charts/redhat-openshift-mcp-server \
    -n openshift-mcp-server \
    --set-json 'config.deniedResources=[{"group":"","version":"v1","kind":"Secret"},{"group":"","version":"v1","kind":"ConfigMap"}]'
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-setup-authentication_{context}"]
= Set up MCP gateway authentication

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, set up OAuth-based authentication for the MCP gateway, including OAuth discovery.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* RBAC is configured.
* You have revoked access to specific Custom Resources (CRs) as needed.
* You have access to an Identity Provider (Entra ID).

.Procedure

. Configure OAuth metadata discovery by setting environment variables on the MCP gateway broker-router deployment by running the following command:
+
[source,terminal]
----
$ oc set env deployment/mcp-gateway-broker-router -n mcp-system\
OAUTH_RESOURCE_NAME="MCP Server" \
OAUTH_RESOURCE="http://mcp.127-0-0-1.sslip.io:8001/mcp" \
OAUTH_AUTHORIZATION_SERVERS="https://login.microsoftonline.com/<tenant-id>/v2.0" \
OAUTH_BEARER_METHODS_SUPPORTED="header" \
OAUTH_SCOPES_SUPPORTED="openid,mcp-server,offline_access"
----
+
These environment variables enable the OAuth 2.0 Protected Resource Metadata endpoint that clients use for authentication discovery.

. Create the HTTPRoute for OAuth discovery by running the following command:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: mcp-gateway-oauth-metadata
  namespace: mcp-system
spec:
  parentRefs:
  - group: gateway.networking.k8s.io
    kind: Gateway
    name: mcp-gateway
    namespace: gateway-system
    sectionName: mcp
  hostnames:
  - ${MCP_GATEWAY_HOST}
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /.well-known/oauth-protected-resource
    backendRefs:
    - name: mcp-gateway
      port: 8080
EOF
----
+
Where `${MCP_GATEWAY_HOST}` is the fully qualified domain name for your MCP gateway (for example, `mcp.127-0-0-1.sslip.io`).
+
This route enables clients to discover OAuth metadata, which is required for the authentication flow. Without this route, clients receive a 404 error when attempting OAuth discovery.

. Configure the Identity Provider (Entra ID) App Registration:

.. In the Azure Portal or Entra admin center, go to your Entra ID App Registration.

.. Under *Expose an API*, add a custom scope named `mcp-server`.

.. Ensure that the following scopes are available: `openid`, `offline_access`, and `mcp-server`.

.. If required by your organization, grant admin consent for these scopes.
+
For more information about configuring Entra ID, see the Microsoft Entra ID documentation about configuring app registrations.

. Configure certificate trust for JWT validation by mounting the Entra ID CA certificate into the Authorino deployment by running the following commands:
+
[source,terminal]
----
$ oc create configmap entra-ca --from-file=ca.crt=/path/to/entra-ca.crt -n kuadrant-system
----
+
[source,terminal]
----
$ oc patch deployment authorino -n kuadrant-system --type=json -p='[
  {
    "op": "add",
    "path": "/spec/template/spec/volumes/-",
    "value": {"name": "entra-ca", "configMap": {"name": "entra-ca"}}
  },
  {
    "op": "add",
    "path": "/spec/template/spec/containers/0/volumeMounts/-",
    "value": {"name": "entra-ca", "mountPath": "/etc/ssl/certs/entra-ca.crt", "subPath": "ca.crt"}
  }
]'
----
+
This ensures that Authorino can verify JWT token signatures from Microsoft Entra ID.

. Configure the MCP gateway authentication by applying the authentication policy that validates JWT tokens by running the following command:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: kuadrant.io/v1
kind: AuthPolicy
metadata:
  name: mcp-auth-policy
  namespace: mcp-system
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: mcp-gateway
    sectionName: mcp
  defaults:
    when:

      - predicate: "!request.path.contains('/.well-known')"
    rules:
      authentication:
        'entra-id':
          jwt:
            issuerUrl: https://login.microsoftonline.com/<tenant-id>/v2.0
      response:
        unauthenticated:
          code: 401
          headers:
            'WWW-Authenticate':
              value: Bearer resource_metadata=http://mcp.127-0-0-1.sslip.io:8001/.well-known/oauth-protected-resource/mcp
          body:
            value: |
              {
                "error": "Unauthorized",
                "message": "Authentication required."
              }
EOF
----

.Verification

. Verify OAuth Discovery by testing that the broker now serves OAuth discovery information by running the following command:
+
[source,terminal]
----
curl http://mcp.127-0-0-1.sslip.io:8001/.well-known/oauth-protected-resource
----
+
The command should show OAuth 2.0 Protected Resource Metadata similar to the following:
+
.Example
+
[source,terminal]
----
{
  "resource_name": "MCP Server",
  "resource": "http://mcp.127-0-0-1.sslip.io:8001/mcp",
  "authorization_servers": [
    "https://login.microsoftonline.com/<tenant-id>/v2.0"
  ],
  "bearer_methods_supported": [
    "header"
  ],
  "scopes_supported": [
    "openid",
    "mcp-server",
    "offline_access"
  ]
}
----

. Test that protected endpoints now require authentication by running the following command:
+
[source,terminal]
----
$ curl -v http://mcp.127-0-0-1.sslip.io:8001/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'
----
+
.Example
+
[source,terminal]
----
{
  "error": "Unauthorized",
  "message": "Authentication required."
}
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-setup-authorization_{context}"]
= Set up MCP gateway authorization

[role="_abstract"]
To install the Model Context Protocol (MCP) server for Red Hat OpenShift Container Platform feature, set up tool-level authorization for the MCP gateway to control which users can access specific MCP tools.

.Prerequisites

* Access to OpenShift console with admin rights.
* The MCP server Helm chart is installed.
* MCP-compatible client connected.
* MCP gateway is installed and verified.
* RBAC is configured.
* You have revoked access to specific Custom Resources (CRs) as needed.
* MCP gateway authentication is configured.
* Your identity provider is configured to include group/role claims in JWT tokens.

.Procedure

. Ensure that your identity provider includes necessary group/role claims in the issued JWT tokens.
+
The issued OAuth token should include claims similar to:
+
.Example
[source,json]
----
{
  "resource_access": {
    "mcp-ns/openshift-mcp-server": {
      "roles": ["pods_list", "events_list", "nodes_list", "deployments_get"]
    },
    "mcp-ns/geometry-mcp-server": {
      "roles": ["pods_list", "events_list", "nodes_list", "deployments_get"]
    }
  }
}
----
+
* The namespace should match the namespace of the `MCPServerRegistration` CR.

* The "`roles`" represent the allowed tools. In this example, pods_list, events_list, nodes_list, deployments_get.

. Configure tool-level authorization by applying an AuthPolicy that enforces tool-level access control by running the following command:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: kuadrant.io/v1
kind: AuthPolicy
metadata:
  name: mcp-tool-auth-policy
  namespace: openshift-mcp-server
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: mcp-gateway
    sectionName: mcp
  rules:
    authentication:
      'sso-server':
        jwt:
          issuerUrl: https://login.microsoftonline.com/<tenant-id>/v2.0
    authorization:
      'tool-access-check':
        patternMatching:
          patterns:
            - predicate: |
                request.headers['x-mcp-toolname'] in (has(auth.identity.resource_access) && auth.identity.resource_access.exists(p, p == request.headers['x-mcp-servername']) ? auth.identity.resource_access[request.headers['x-mcp-servername']].roles : [])
    response:
      unauthenticated:
        headers:
          'WWW-Authenticate':
            value: Bearer resource_metadata=http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/.well-known/oauth-protected-resource/mcp
        body:
          value: |
            {
              "error": "Unauthorized",
              "message": "MCP Tool Access denied: Authentication required."
            }
      unauthorized:
        body:
          value: |
            {
              "error": "Forbidden",
              "message": "MCP Tool Access denied: Insufficient permissions for this tool."
            }
EOF
----
+
Where:

* `spec.sectionName` targets the MCP server Listener.

* `<cluster-name>.<domain-name>` is the name and domain of your cluster.

.Verification

. Test that authorization now controls tool access by setting up the MCP Inspector:

.. Start MCP Inspector (requires Node.js/npm) by running the following command:
+
[source,terminal]
----
$ npx @modelcontextprotocol/inspector@latest &
INSPECTOR_PID=$!
----

.. Wait for services to start by running the following command:
+
[source,terminal]
----
$ sleep 3
----

.. Open MCP Inspector by going to the following URL: http://localhost:6274/?transport=streamable-http&serverUrl=http://mcp-gateway.apps.<cluster-name>.<domain-name>:8001/mcp.
+
Where <cluster-name>.<domain-name> is the name and domain of your cluster.

. To stop the services later, run the following command:
+
[source,terminal]
----
$ kill $INSPECTOR_PID
----

. Authenticate using a user account configured with the required role claims in your identity provider.

. Try the following allowed tools:
+
* pods_list

* events_list

* nodes_list

* deployments_get

. Try this restricted tool: pods_delete
+
Since this tool is restricted, you should get a 403 Forbidden error.

. Monitor authorization decisions:

.. Check the AuthPolicy status by running the following command:
+
[source,terminal]
----
$ oc get authpolicy -A
----
.. View the authorization logs by running the following command:
+
[source,terminal]
----
$ oc logs -n kuadrant-system -l authorino-resource=authorino
----

// Module included in the following assemblies:
//
// * ai_applications/mcp_server/mcp-server-overview.adoc

[id="ai-app-mcp-server-overview-prompting-instructions_{context}"]
= MCP server for Red Hat OpenShift Container Platform prompting

[role="_abstract"]
With MCP server for OpenShift Container Platform installed, you can now prompt the Large Language Model (LLM) to learn more about your cluster.

// ???AI warning. Get legal blurb as an OCP snippet: https://docs.google.com/document/d/1eVk8pMiSTqjfQSwU_h21BBXJ5PN8jbSLcU0wBtUt7bs/edit?tab=t.0#heading=h.dyq1r89dkf3e???

[NOTE]
=====
To ensure that you get the best results when prompting be sure to:

 * Specify the namespace.

 * For Red Hat Advanced Cluster Management (ACM) for Kubernetes environments, specify the cluster.
=====

== MCP prompts
MCP Prompts are predefined templates that guide AI assistants through specific workflows.

They combine:

* *Structured guidance*: Step-by-step instructions for common tasks
* *Parameterization*: Arguments that customize the prompt for specific contexts
* *Conversation templates*: Preformatted messages that guide the interaction

== Creating custom prompts
Define custom prompts in your `config.toml` file. Code changes and recompilation are not needed.

.Example custom prompts
[source,toml]
----
[[prompts]]
name = "check-pod-logs"
title = "Check Pod Logs"
description = "Quick way to check pod logs"

[[prompts.arguments]]
name = "pod_name"
description = "Name of the pod"
required = true

[[prompts.arguments]]
name = "namespace"
description = "Namespace of the pod"
required = false

[[prompts.messages]]
role = "user"
content = "Show me the logs for pod {{pod_name}} in {{namespace}}"

[[prompts.messages]]
role = "assistant"
content = "I'll retrieve and analyze the logs for you."
----

.Configuration reference
[cols="1,1", options="header"]
|===
2+| Prompt Fields
| name (required) | Unique identifier for the prompt
| title (optional) | Human-readable display name
| description (required) | Brief explanation of what the prompt does
| arguments (optional) | List of parameters the prompt accepts
| messages (required) | Conversation template with role/content pairs

2+| Argument Fields
| name (required) | Argument identifier
| description (optional) | Explanation of the argument's purpose
| required (optional) | Whether the argument must be provided (default: false)

2+| Argument Substitution
2+| Use {{argument_name}} placeholders in message content. The template engine replaces these with actual values when the prompt is called. If an optional argument is not provided, its placeholder is removed from the output.
|===

== Built-in prompts
The MCP server for Red Hat OpenShift Container Platform includes several built-in prompts that are always available:

`Cluster-health-check` performs a comprehensive health assessment of your OpenShift cluster.

Arguments:

* namespace (optional): Limit the health check to a specific namespace. Default: all namespaces.

* check_events (optional): Include recent warning/error events in the analysis. Values: true or false. Default: true.

What it checks:

* *Nodes*: Status and conditions (for example, Ready, MemoryPressure, DiskPressure)

* *Cluster Operators*: Available and degraded status

* *Pods*: Phase, container statuses, restart counts, and common issues (for example, CrashLoopBackOff, ImagePullBackOff)

* *Workload Controllers*: Deployments, StatefulSets, and DaemonSets replica status

* *Persistent Volume Claims*: Binding status

* *Events*: Recent warning and error events from the last hour

Example usage:

[source,terminal]
----
Check the health of my cluster
----

Or with specific parameters:
[source,terminal]
----
Check the health of namespace production
----

You can also skip event checking for faster results:

[source,terminal]
----
Check the health of my cluster without events
----

The prompt gathers comprehensive diagnostic data and presents it to the LLM for analysis, which provides:

* Overall health status (Healthy, Warning, or Critical)

* Critical issues requiring immediate attention

* Warnings and recommendations

* Summary by component

== Configuration file location
Place your prompts in the `config.toml` file used by the MCP server. Specify the config file path by using the `--config flag` when starting the server.

== Toolset prompts
Some toolsets contain prompts and enabling the toolset enables the prompt(s).

== Prompt merging
When both toolset and config prompts exist, config-defined prompts override toolset prompts with the same name. This allows administrators to customize built-in workflows. Prompts with unique names from both sources are available.
