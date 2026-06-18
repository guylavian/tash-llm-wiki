---
title: "Chapter 8. Configuring a reverse proxy - Red Hat build of Keycloak 26.2 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-reverseproxy
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/reverseproxy-
guide: server_configuration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "Configure Red Hat build of Keycloak with a reverse proxy, API gateway, or load balancer. Distributed environments frequently require the use of a reverse proxy. Red Hat build of Keycloak offers several options to securely integrate with such environments. 8.1. Port to be proxied Red Hat build of Keycloak runs on the following ports by default: 8443 (8080 when you enable HTTP explicitly by --http-e…"
---

# Chapter 8. Configuring a reverse proxy - Red Hat build of Keycloak 26.2 Server Configuration Guide

Chapter 8. Configuring a reverse proxy
Configure Red Hat build of Keycloak with a reverse proxy, API gateway, or load balancer.
Distributed environments frequently require the use of a reverse proxy. Red Hat build of Keycloak offers several options to securely integrate with such environments.
8.1. Port to be proxied
Red Hat build of Keycloak runs on the following ports by default:
-
8443
(8080
when you enable HTTP explicitly by--http-enabled=true
) -
9000
The port 8443
(or 8080
if HTTP is enabled) is used for the Admin UI, Account Console, SAML and OIDC endpoints and the Admin REST API as described in the Configuring the hostname (v2) chapter.
The port 9000
is used for management, which includes endpoints for health checks and metrics as described in the Configuring the Management Interface chapter.
You only need to proxy port 8443
(or 8080
) even when you use different host names for frontend/backend and administration as described at Configuring Red Hat build of Keycloak for production. You should not proxy port 9000
as health checks and metrics use those ports directly, and you do not want to expose this information to external callers.
8.2. Configure the reverse proxy headers
Red Hat build of Keycloak will parse the reverse proxy headers based on the proxy-headers
option which accepts several values:
- By default if the option is not specified, no reverse proxy headers are parsed. This should be used when no proxy is in use or with https passthrough.
-
forwarded
enables parsing of theForwarded
header as per RFC7239. -
xforwarded
enables parsing of non-standardX-Forwarded-*
headers, such asX-Forwarded-For
,X-Forwarded-Proto
,X-Forwarded-Host
, andX-Forwarded-Port
.
If you are using a reverse proxy for anything other than https passthrough and do not set the proxy-headers
option, then by default you will see 403 Forbidden responses to requests via the proxy that perform origin checking.
For example:
bin/kc.[sh|bat] start --proxy-headers forwarded
If either forwarded
or xforwarded
is selected, make sure your reverse proxy properly sets and overwrites the Forwarded
or X-Forwarded-*
headers respectively. To set these headers, consult the documentation for your reverse proxy. Do not use forwarded
or xforwarded
with https passthrough. Misconfiguration will leave Red Hat build of Keycloak exposed to security vulnerabilities.
Take extra precautions to ensure that the client address is properly set by your reverse proxy via the Forwarded
or X-Forwarded-For
headers. If this header is incorrectly configured, rogue clients can set this header and trick Red Hat build of Keycloak into thinking the client is connected from a different IP address than the actual address. This precaution can be more critical if you do any deny or allow listing of IP addresses.
When using the xforwarded
setting, the X-Forwarded-Port
takes precedence over any port included in the X-Forwarded-Host
.
If the TLS connection is terminated at the reverse proxy (edge termination), enabling HTTP through the http-enabled
setting is required.
8.3. Different context-path on reverse proxy
Red Hat build of Keycloak assumes it is exposed through the reverse proxy under the same context path as Red Hat build of Keycloak is configured for. By default Red Hat build of Keycloak is exposed through the root (/
), which means it expects to be exposed through the reverse proxy on /
as well. You can use a full URL for the hostname
option in these cases, for example using --hostname=https://my.keycloak.org/auth
if Red Hat build of Keycloak is exposed through the reverse proxy on /auth
.
For more details on exposing Red Hat build of Keycloak on different hostname or context-path incl. Administration REST API and Console, see Configuring the hostname (v2).
Alternatively you can also change the context path of Red Hat build of Keycloak itself to match the context path for the reverse proxy using the http-relative-path
option, which will change the context-path of Red Hat build of Keycloak itself to match the context path used by the reverse proxy.
8.4. Enable sticky sessions
Typical cluster deployment consists of the load balancer (reverse proxy) and 2 or more Red Hat build of Keycloak servers on private network. For performance purposes, it may be useful if load balancer forwards all requests related to particular browser session to the same Red Hat build of Keycloak backend node.
The reason is, that Red Hat build of Keycloak is using Infinispan distributed cache under the covers for save data related to current authentication session and user session. The Infinispan distributed caches are configured with limited number of owners. That means that session related data are stored only in some cluster nodes and the other nodes need to lookup the data remotely if they want to access it.
For example if authentication session with ID 123 is saved in the Infinispan cache on node1, and then node2 needs to lookup this session, it needs to send the request to node1 over the network to return the particular session entity.
It is beneficial if particular session entity is always available locally, which can be done with the help of sticky sessions. The workflow in the cluster environment with the public frontend load balancer and two backend Red Hat build of Keycloak nodes can be like this:
- User sends initial request to see the Red Hat build of Keycloak login screen
- This request is served by the frontend load balancer, which forwards it to some random node (eg. node1). Strictly said, the node doesn’t need to be random, but can be chosen according to some other criteria (client IP address etc). It all depends on the implementation and configuration of underlying load balancer (reverse proxy).
- Red Hat build of Keycloak creates authentication session with random ID (eg. 123) and saves it to the Infinispan cache.
- Infinispan distributed cache assigns the primary owner of the session based on the hash of session ID. See Infinispan documentation for more details around this. Let’s assume that Infinispan assigned node2 to be the owner of this session.
- Red Hat build of Keycloak creates the cookie AUTH_SESSION_ID with the format like <session-id>.<owner-node-id> . In our example case, it will be 123.node2 .
- Response is returned to the user with the Red Hat build of Keycloak login screen and the AUTH_SESSION_ID cookie in the browser
From this point, it is beneficial if load balancer forwards all the next requests to the node2 as this is the node, who is owner of the authentication session with ID 123 and hence Infinispan can lookup this session locally. After authentication is finished, the authentication session is converted to user session, which will be also saved on node2 because it has same ID 123 .
The sticky session is not mandatory for the cluster setup, however it is good for performance for the reasons mentioned above. You need to configure your loadbalancer to stick over the AUTH_SESSION_ID cookie. The appropriate procedure to make this change depends on your loadbalancer.
If your proxy supports session affinity without processing cookies from backend nodes, you should set the spi-sticky-session-encoder-infinispan-should-attach-route
option to false
in order to avoid attaching the node to cookies and just rely on the reverse proxy capabilities.
bin/kc.[sh|bat] start --spi-sticky-session-encoder-infinispan-should-attach-route=false
By default, the spi-sticky-session-encoder-infinispan-should-attach-route
option value is true
so that the node name is attached to cookies to indicate to the reverse proxy the node that subsequent requests should be sent to.
8.5. Exposed path recommendations
When using a reverse proxy, Red Hat build of Keycloak only requires certain paths to be exposed. The following table shows the recommended paths to expose.
| Red Hat build of Keycloak Path | Reverse Proxy Path | Exposed | Reason |
|---|---|---|---|
| / | - | No | When exposing all paths, admin paths are exposed unnecessarily. |
| /admin/ | - | No | Exposed admin paths lead to an unnecessary attack vector. |
| /realms/ | /realms/ | Yes | This path is needed to work correctly, for example, for OIDC endpoints. |
| /resources/ | /resources/ | Yes | This path is needed to serve assets correctly. It may be served from a CDN instead of the Red Hat build of Keycloak path. |
| /metrics | - | No | Exposed metrics lead to an unnecessary attack vector. |
| /health | - | No | Exposed health checks lead to an unnecessary attack vector. |
We assume you run Red Hat build of Keycloak on the root path /
on your reverse proxy/gateway’s public API. If not, prefix the path with your desired one.
8.6. Trusted Proxies
To ensure that proxy headers are used only from proxies you trust, set the proxy-trusted-addresses
option to a comma separated list of IP addresses (IPv4 or IPv6) or Classless Inter-Domain Routing (CIDR) notations.
For example:
bin/kc.[sh|bat] start --proxy-headers forwarded --proxy-trusted-addresses=192.168.0.32,127.0.0.0/8
8.7. PROXY Protocol
The proxy-protocol-enabled
option controls whether the server should use the HA PROXY protocol when serving requests from behind a proxy. When set to true, the remote address returned will be the one from the actual connecting client. The value cannot be true
when using the proxy-headers
option.
This is useful when running behind a compatible https passthrough proxy because the request headers cannot be manipulated.
For example:
bin/kc.[sh|bat] start --proxy-protocol-enabled true
8.8. Enabling client certificate lookup
When the proxy is configured as a TLS termination proxy the client certificate information can be forwarded to the server through specific HTTP request headers and then used to authenticate clients. You are able to configure how the server is going to retrieve client certificate information depending on the proxy you are using.
Client certificate lookup via a proxy header for X.509 authentication is considered security-sensitive. If misconfigured, a forged client certificate header can be used for authentication. Extra precautions need to be taken to ensure that the client certificate information can be trusted when passed via a proxy header.
- Double check your use case needs reencrypt or edge TLS termination which implies using a proxy header for client certificate lookup. TLS passthrough is recommended as a more secure option when X.509 authentication is desired as it does not require passing the certificate via a proxy header. Client certificate lookup from a proxy header is applicable only to reencrypt and edge TLS termination.
If passthrough is not an option, implement the following security measures:
- Configure your network so that Red Hat build of Keycloak is isolated and can accept connections only from the proxy.
-
Make sure that the proxy overwrites the header that is configured in
spi-x509cert-lookup-<provider>-ssl-client-cert
option. -
Pay extra attention to the
spi-x509cert-lookup-<provider>-trust-proxy-verification
setting. Make sure you enable it only if you can trust your proxy to verify the client certificate. Settingspi-x509cert-lookup-<provider>-trust-proxy-verification=true
without the proxy verifying the client certificate chain will expose Red Hat build of Keycloak to security vulnerability when a forged client certificate can be used for authentication.
The server supports some of the most commons TLS termination proxies such as:
| Proxy | Provider |
|---|---|
| Apache HTTP Server | apache |
| HAProxy | haproxy |
| NGINX | nginx |
To configure how client certificates are retrieved from the requests you need to:
Enable the corresponding proxy provider
bin/kc.[sh|bat] build --spi-x509cert-lookup-provider=<provider>
Configure the HTTP headers
bin/kc.[sh|bat] start --spi-x509cert-lookup-<provider>-ssl-client-cert=SSL_CLIENT_CERT --spi-x509cert-lookup-<provider>-ssl-cert-chain-prefix=CERT_CHAIN --spi-x509cert-lookup-<provider>-certificate-chain-length=10
When configuring the HTTP headers, you need to make sure the values you are using correspond to the name of the headers forwarded by the proxy with the client certificate information.
The available options for configuring a provider are:
| Option | Description |
|---|---|
| ssl-client-cert | The name of the header holding the client certificate |
| ssl-cert-chain-prefix |
The prefix of the headers holding additional certificates in the chain and used to retrieve individual certificates accordingly to the length of the chain. For instance, a value |
| certificate-chain-length | The maximum length of the certificate chain. |
| trust-proxy-verification | Enable trusting NGINX proxy certificate verification, instead of forwarding the certificate to Red Hat build of Keycloak and verifying it in Red Hat build of Keycloak. |
| cert-is-url-encoded |
Whether the forwarded certificate is url-encoded or not. In NGINX, this corresponds to the |
8.8.1. Configuring the NGINX provider
The NGINX SSL/TLS module does not expose the client certificate chain. Red Hat build of Keycloak’s NGINX certificate lookup provider rebuilds it by using the Red Hat build of Keycloak truststore.
If you are using this provider, see Configuring trusted certificates for how to configure a Red Hat build of Keycloak Truststore.
8.9. Relevant options
| Value | |
|---|---|
|
Available only when hostname:v2 feature is enabled | |
|
Available only when hostname:v2 feature is enabled | |
| 🛠
| (default) |
|
|
|
|
|
|
|
|
