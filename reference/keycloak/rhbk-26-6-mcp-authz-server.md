---
title: "Chapter 12. Integrating with Model Context Protocol (MCP) - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-mcp-authz-server
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/securing_applications_and_services_guide/mcp-authz-server-
guide: securing_applications_and_services_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Using Red Hat build of Keycloak as an authorization server for Model Context Protocol (MCP) servers. There are currently four versions of the Model Context Protocol (MCP) specification: 2025-11-25 (latest version) 2025-06-18 2025-03-26 2024-11-05 (initial version) The initial version (2024-11-05) does not cover authorization, as such is not covered in this guide. This guide shows you the following…"
---

# Chapter 12. Integrating with Model Context Protocol (MCP) - Red Hat build of Keycloak 26.6 Securing Applications and Services Guide

Chapter 12. Integrating with Model Context Protocol (MCP)
Using Red Hat build of Keycloak as an authorization server for Model Context Protocol (MCP) servers.
There are currently four versions of the Model Context Protocol (MCP) specification:
- 2025-11-25 (latest version)
- 2025-06-18
- 2025-03-26
- 2024-11-05 (initial version)
The initial version (2024-11-05) does not cover authorization, as such is not covered in this guide.
This guide shows you the following:
- Which MCP version Red Hat build of Keycloak supports.
- How to set up Red Hat build of Keycloak as an authorization server in MCP.
However, the guide does not cover everything you need to know. Therefore, you are recommended to read the authorization section of the relevant MCP version as well.
12.1. Standards Compliance MCP requires
According to the MCP specification, there are several standards regarding an authorization server in MCP. The following table shows:
- Which MCP version requires an authorization server to support which standards in which level (MUST, SHOULD, MAY).
- With which standards Red Hat build of Keycloak complies.
| Standard | 2025-11-25 | 2025-06-18 | 2025-03-26 | Red Hat build of Keycloak |
|---|---|---|---|---|
| MUST | MUST | MUST | Supported | |
| MUST | MUST | MUST | Supported | |
| MUST | MUST | - | Not supported | |
| MAY | SHOULD | SHOULD | Supported | |
| SHOULD | - | - | Supported |
The OAuth Client ID Metadata Document support in Red Hat build of Keycloak is an experimental feature. It may introduce breaking changes in future versions of Red Hat build of Keycloak.
The MCP specification adopts OAuth 2.0 Protected Resource Metadata (RFC 9728). The standard is for an MCP server and not for an authorization server like Red Hat build of Keycloak. Therefore, it is not included in the above table.
12.2. MCP version compliance
In this guide, as criteria for compliance, "Red Hat build of Keycloak supports MCP" means that Red Hat build of Keycloak meets all MUST and SHOULD requirements by MCP.
According to these criteria, the following table shows which MCP version Red Hat build of Keycloak supports.
| MCP Version | Conformance |
|---|---|
| Supported | |
| Partially Supported without Resource Indicators for OAuth 2.0 | |
| Partially Supported without Resource Indicators for OAuth 2.0 |
12.3. Setup
12.3.1. For MCP 2025-03-26
No special setup is required.
12.3.2. For MCP 2025-06-18 and 2025-11-25
12.3.2.1. Token Audience Binding and Validation
To gain security benefit, the MCP specification requires an access token to be bound with its audience. In order to do so, the MCP specification requires the following:
-
An MCP client MUST include the
resource
parameter defined in Resource Indicators for OAuth 2.0 (RFC 8707) in an authorization request and token request. The parameter’s value MUST identify an MCP server that the MCP client intends to use the token with. - An MCP server MUST validate that tokens presented to them were specifically issued for their use.
The MCP specification does not describe how to do this binding. One method for the binding is to set a value of resource
parameter to an aud
claim in an access token. However, Red Hat build of Keycloak cannot recognize resource
parameter.
The Keycloak community is planning to support Resource Indicators for OAuth 2.0 (RFC 8707) to Red Hat build of Keycloak to make Red Hat build of Keycloak recognize and process the resource
parameter as the MCP specification expects. Until this support is completed, you can use OAuth 2.0’s scope
parameter instead of the resource
parameter. To show the binding, please consider the following situation:
-
An MCP server’s URL is
https://example.com/mcp
-
The MCP supports the following three scopes:
mcp:tools
,mcp:prompts
andmcp:resources
. -
To get an access token for accessing the MCP server, an MCP client sends to Red Hat build of Keycloak an authorization request whose
resource
parameter value ishttps://example.com/mcp
andscope
parameter includes any combination of the three scopes. -
We want Red Hat build of Keycloak to issue an access token whose
aud
claim’s value is MCP server’s URL, namelyhttps://example.com/mcp
.
To make Red Hat build of Keycloak issue such the access token, we could configure Red Hat build of Keycloak as follows:
-
Add a client scope
mcp:tools
whose type isOptional
. -
Add to the client scope a new
Audience
mapper whoseIncluded Custom Audience
field ishttps://example.com/mcp
. -
Add a client scope
mcp:prompts
whose type isOptional
. -
Add to the client scope a new
Audience
mapper whoseIncluded Custom Audience
field ishttps://example.com/mcp
. -
Add a client scope
mcp:resources
whose type isOptional
. -
Add to the client scope a new
Audience
mapper whoseIncluded Custom Audience
field ishttps://example.com/mcp
.
Please not that the client scope’s Included Custom Audience
field needs to be the same as the authorization request’s resource
parameter value and the MCP server’s URL.
With the configuration, if the MCP client send to Red Hat build of Keycloak an authorization request whose resource
parameter value is https://example.com/mcp
and scope
parameter includes mcp:resources
, mcp:tools
and mcp:prompts
, Red Hat build of Keycloak can issue the following access token:
{
...
"aud": "https://example.com/mcp",
"scope": "mcp:resources mcp:tools mcp:prompts"
...
}
12.3.3. MCP Inspector integration
If you want to use MCP Inspector, an official debugging tools for MCP server, with Red Hat build of Keycloak as an authorization server, you need to do an appropriate setup regarding CORS on Red Hat build of Keycloak’s' client registration endpoint because MCP Inspector executes JavaScript downloaded from the MCP Inspector’s backend server to register an MCP client dynamically to Red Hat build of Keycloak.
You need to do an appropriate setup for Client Registration’s anonymous access policies as follows:
- Allowed Client Scopes: Needs to include scopes supported by an MCP server.
- Allowed Registration Web Origins: Needs to include web origin of MCP inspector’s backend server.
- Trusted Hosts: Needs to include hostname or IP address of the machine that sends a dynamic client registration request to Red Hat build of Keycloak, namely the machine your browser runs on.
12.3.4. For MCP 2025-11-25
12.3.4.1. Client Registration
According to Client Registration Approaches section of the MCP specification, the following three client registration mechanisms are supported and you can choose based on your scenario:
- Client ID Metadata Documents: When client and server have no prior relationship (most common)
- Pre-registration: When client and server have an existing relationship
- Dynamic Client Registration: For backwards compatibility or specific requirements
Red Hat build of Keycloak supports OAuth Client ID Metadata Document. To use Client ID Metadata Documents, you need to enable the feature and set up a client policy so that Red Hat build of Keycloak processes the client_id
parameter formatted as a URL and fetches the client metadata from that URL.
The OAuth Client ID Metadata Document support is an experimental feature in Red Hat build of Keycloak. As such, it may introduce breaking changes in future versions of Red Hat build of Keycloak. To enable it, start Red Hat build of Keycloak with --features=cimd
.
12.3.4.1.1. Setting up the client profile for OAuth Client ID Metadata Document
To process an authorization request whose client_id
metadata is a URL pointing to a Client ID Metadata Document, you need to create the profile including client-id-metadata-document
executor.
To configure the executor, create a client policy profile in the Red Hat build of Keycloak Admin Console:
-
Navigate to Realm Settings
Client Policies Profiles tab. - Click Create client profile.
-
Give the profile a name such as
cimd-profile
and click Save. -
Click Add executor and select
client-id-metadata-document
from the list. Configure the executor with the following options:
-
Allow http scheme: If
ON
, allowshttp
scheme for the Client ID URL and Client Metadata URLs (e.g.,client_uri
,logo_uri
,tos_uri
,policy_uri
,jwks_uri
). This should only beON
in a development environment and must beOFF
in a production environment. -
Trusted domains: A list of domain patterns (wildcard) that the executor accepts for the Client ID URL and Client Metadata URL properties. For example, use
*.example.org
to accept any subdomain ofexample.org
. If empty, all domains are denied. -
Restrict same domain: If
ON
, the executor verifies that the Client ID URL and Redirect URI in an authorization request, as well as URL-valued properties of the client metadata, are all under the same trusted domain. - Required properties: A list of client metadata properties that must be present in the Client ID Metadata Document. If the fetched document does not include all the listed properties, the request is rejected.
-
Only Allow Confidential Client: If
ON
, the executor only accepts a Client Metadata Document representing a confidential client. In this case, the client metadata must include either ajwks
orjwks_uri
property and must useprivate_key_jwt
ortls_client_auth
as the token endpoint authentication method.
-
Allow http scheme: If
- Click Save.
12.3.4.1.2. Setting up the client policy for OAuth Client ID Metadata Document
To trigger the profile created above when the client_id
parameter in an authorization request is a URI matching a specified scheme (e.g., https
), you need to create the policy including client-id-uri
condition.
To configure the condition, create a client policy in the Red Hat build of Keycloak Admin Console:
-
Navigate to Realm Settings
Client Policies Policies tab. - Click Create client policy.
-
Give the policy a name such as
cimd-policy
and click Save. -
Under Conditions, click Add condition and select
client-id-uri
from the list. Configure the condition with the following options:
-
URI scheme: A list of URI schemes to match against the
client_id
parameter (e.g.,https
). In a production environment, onlyhttps
should be used. -
Trusted domains: A list of domain patterns (wildcard) that the condition accepts for the host part of the
client_id
URI. If domains are filled, the condition evaluates to true only when the host part of theclient_id
matches one of the domains. If not filled, the condition evaluates to false regardless. For example, use*.example.org
to accept any subdomain ofexample.org
.
-
URI scheme: A list of URI schemes to match against the
- Click Save.
-
Under Associated client profiles, add the
cimd-profile
profile created in the previous step. - Click Save.
With this configuration, when an MCP client sends an authorization request with a client_id
value that is an https
URL matching a trusted domain, Red Hat build of Keycloak fetches the Client ID Metadata Document from that URL and uses the metadata to process the request.
12.3.4.1.3. System-wide settings for the Client ID Metadata Document executor
The client-id-metadata-document
executor has the following system-wide settings that control caching and metadata size limits. These settings cannot be configured through the Admin Console. Instead, they are configured as SPI options when starting Red Hat build of Keycloak.
-
min-cache-time: The minimum time (in seconds) that a fetched Client ID Metadata Document is cached. Default:
300
(5 minutes). -
max-cache-time: The maximum time (in seconds) that a fetched Client ID Metadata Document is cached. Default:
259200
(3 days). -
upper-limit-metadata-bytes: The maximum size (in bytes) of a Client ID Metadata Document that Red Hat build of Keycloak accepts. Default:
5000
(5 KB).
To configure these settings, use the --spi-client-policy-executor—client-id-metadata-document--<property>=<value>
command-line option when starting Red Hat build of Keycloak. For example:
bin/kc.[sh|bat] start --spi-client-policy-executor--client-id-metadata-document--min-cache-time=600 --spi-client-policy-executor--client-id-metadata-document--max-cache-time=86400 --spi-client-policy-executor--client-id-metadata-document--upper-limit-metadata-bytes=10000
12.3.5. Visual Studio Code desktop integration
Microsoft Visual Studio Code (VS Code) desktop is an MCP client that supports OAuth Client ID Metadata Document. When VS Code desktop connects to an MCP server that requires authorization, it sends an authorization request with a client_id
parameter that is an https
URL hosted on vscode.dev
(e.g., https://vscode.dev/mcp-client
). Red Hat build of Keycloak fetches the Client ID Metadata Document from this URL and uses the metadata to process the request.
VS Code desktop uses localhost callbacks for the OAuth redirect. It starts a local HTTP server and uses a redirect URI such as http://127.0.0.1:<port>/callback
. Because the redirect URI is on 127.0.0.1
rather than on the vscode.dev
domain, the Restrict same domain option in the client profile executor must be set to OFF
.
To configure Red Hat build of Keycloak for VS Code desktop’s MCP client, follow the steps below.
VS Code desktop is a public client that uses PKCE (Proof Key for Code Exchange) for OAuth. It does not use a client secret.
12.3.5.1. Starting Red Hat build of Keycloak with the CIMD feature
Start Red Hat build of Keycloak with the cimd
feature flag enabled:
bin/kc.[sh|bat] start --features=cimd
12.3.5.2. Setting up the client profile for VS Code desktop
-
Navigate to Realm Settings
Client Policies Profiles tab. - Click Create client profile.
-
Give the profile a name such as
vscode-cimd-profile
and click Save. -
Click Add executor and select
client-id-metadata-document
from the list. Configure the executor with the following options:
-
Allow http scheme:
OFF
-
Trusted domains:
vscode.dev
,127.0.0.1
-
Restrict same domain:
OFF
(VS Code desktop uses a localhost redirect URI such ashttp://127.0.0.1:<port>/callback
, which is not on the same domain asvscode.dev
) -
Only Allow Confidential Client:
OFF
(VS Code desktop is a public client)
-
Allow http scheme:
- Click Save.
12.3.5.3. Setting up the client policy for VS Code desktop
-
Navigate to Realm Settings
Client Policies Policies tab. - Click Create client policy.
-
Give the policy a name such as
vscode-cimd-policy
and click Save. -
Under Conditions, click Add condition and select
client-id-uri
from the list. Configure the condition with the following options:
-
URI scheme:
https
-
Trusted domains:
vscode.dev
-
URI scheme:
- Click Save.
-
Under Associated client profiles, add the
vscode-cimd-profile
profile created in the previous step. - Click Save.
With this configuration, when VS Code desktop sends an authorization request, Red Hat build of Keycloak recognizes the client_id
as a URL on vscode.dev
, fetches the Client ID Metadata Document, and uses a localhost callback to complete the OAuth flow.
