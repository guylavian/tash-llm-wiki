---
title: "Chapter 11. Configuring outgoing HTTP requests - Red Hat build of Keycloak 26.2 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-outgoinghttp
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/outgoinghttp-
guide: server_configuration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 11. Configuring outgoing HTTP requests - Red Hat build of Keycloak 26.2 Server Configuration Guide

Chapter 11. Configuring outgoing HTTP requests
Configure the client used for outgoing HTTP requests.
Red Hat build of Keycloak often needs to make requests to the applications and services that it secures. Red Hat build of Keycloak manages these outgoing connections using an HTTP client. This chapter shows how to configure the client, connection pool, proxy environment settings, timeouts, and more.
11.1. Configuring trusted certificates for TLS connections
See Configuring trusted certificates for how to configure a Red Hat build of Keycloak Truststore so that Red Hat build of Keycloak is able to perform outgoing requests using TLS.
11.2. Client Configuration Command
The HTTP client that Red Hat build of Keycloak uses for outgoing communication is highly configurable. To configure the Red Hat build of Keycloak outgoing HTTP client, enter this command:
bin/kc.[sh|bat] start --spi-connections-http-client-default-<configurationoption>=<value>
The following are the command options:
- establish-connection-timeout-millis
- Maximum time in milliseconds until establishing a connection times out. Default: Not set.
- socket-timeout-millis
- Maximum time of inactivity between two data packets until a socket connection times out, in milliseconds. Default: 5000ms
- connection-pool-size
- Size of the connection pool for outgoing connections. Default: 128.
- max-pooled-per-route
- How many connections can be pooled per host. Default: 64.
- connection-ttl-millis
- Maximum connection time to live in milliseconds. Default: Not set.
- max-connection-idle-time-millis
- Maximum time an idle connection stays in the connection pool, in milliseconds. Idle connections will be removed from the pool by a background cleaner thread. Set this option to -1 to disable this check. Default: 900000.
- disable-cookies
- Enable or disable caching of cookies. Default: true.
- client-keystore
- File path to a Java keystore file. This keystore contains client certificates for mTLS.
- client-keystore-password
-
Password for the client keystore. REQUIRED, when
client-keystore
is set. - client-key-password
- Password for the private key of the client. REQUIRED, when client-keystore is set.
- proxy-mappings
- Specify proxy configurations for outgoing HTTP requests. For more details, see Section 11.3, “Proxy mappings for outgoing HTTP requests”.
- disable-trust-manager
- If an outgoing request requires HTTPS and this configuration option is set to true, you do not have to specify a truststore. This setting should be used only during development and never in production because it will disable verification of SSL certificates. Default: false.
11.3. Proxy mappings for outgoing HTTP requests
To configure outgoing requests to use a proxy, you can use the following standard proxy environment variables to configure the proxy mappings: HTTP_PROXY
, HTTPS_PROXY
, and NO_PROXY
.
-
The
HTTP_PROXY
andHTTPS_PROXY
variables represent the proxy server that is used for outgoing HTTP requests. Red Hat build of Keycloak does not differentiate between the two variables. If you define both variables,HTTPS_PROXY
takes precedence regardless of the actual scheme that the proxy server uses. -
The
NO_PROXY
variable defines a comma separated list of hostnames that should not use the proxy. For each hostname that you specify, all its subdomains are also excluded from using proxy.
The environment variables can be lowercase or uppercase. Lowercase takes precedence. For example, if you define both HTTP_PROXY
and http_proxy
, http_proxy
is used.
Example of proxy mappings and environment variables
HTTPS_PROXY=https://www-proxy.acme.com:8080
NO_PROXY=google.com,login.facebook.com
In this example, the following results occur:
-
All outgoing requests use the proxy
https://www-proxy.acme.com:8080
except for requests to google.com or any subdomain of google.com, such as auth.google.com. - login.facebook.com and all its subdomains do not use the defined proxy, but groups.facebook.com uses the proxy because it is not a subdomain of login.facebook.com.
11.4. Proxy mappings using regular expressions
An alternative to using environment variables for proxy mappings is to configure a comma-delimited list of proxy-mappings for outgoing requests sent by Red Hat build of Keycloak. A proxy-mapping consists of a regex-based hostname pattern and a proxy-uri, using the format hostname-pattern;proxy-uri
.
For example, consider the following regex:
.*\.(google|googleapis)\.com
You apply a regex-based hostname pattern by entering this command:
bin/kc.[sh|bat] start --spi-connections-http-client-default-proxy-mappings='.*\\.(google|googleapis)\\.com;http://www-proxy.acme.com:8080'
The backslash character \
is escaped again because micro-profile config is used to parse the array of mappings.
To determine the proxy for the outgoing HTTP request, the following occurs:
- The target hostname is matched against all configured hostname patterns.
- The proxy-uri of the first matching pattern is used.
- If no configured pattern matches the hostname, no proxy is used.
When your proxy server requires authentication, include the credentials of the proxy user in the format username:password@
. For example:
.*\.(google|googleapis)\.com;http://proxyuser:password@www-proxy.acme.com:8080
Example of regular expressions for proxy-mapping:
# All requests to Google APIs use http://www-proxy.acme.com:8080 as proxy
.*\.(google|googleapis)\.com;http://www-proxy.acme.com:8080
# All requests to internal systems use no proxy
.*\.acme\.com;NO_PROXY
# All other requests use http://fallback:8080 as proxy
.*;http://fallback:8080
In this example, the following occurs:
- The special value NO_PROXY for the proxy-uri is used, which means that no proxy is used for hosts matching the associated hostname pattern.
- A catch-all pattern ends the proxy-mappings, providing a default proxy for all outgoing requests.
11.5. Relevant options
| Value | |
|---|---|
|
|
