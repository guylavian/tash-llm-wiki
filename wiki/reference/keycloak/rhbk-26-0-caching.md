---
title: "Chapter 10. Configuring distributed caches - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-caching
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/caching-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 10. Configuring distributed caches - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 10. Configuring distributed caches
Red Hat build of Keycloak is designed for high availability and multi-node clustered setups. The current distributed cache implementation is built on top of Infinispan, a high-performance, distributable in-memory data grid.
10.1. Enable distributed caching
When you start Red Hat build of Keycloak in production mode, by using the start
command, caching is enabled and all Red Hat build of Keycloak nodes in your network are discovered.
By default, caches are using a UDP transport stack so that nodes are discovered using IP multicast transport based on UDP. For most production environments, there are better discovery alternatives to UDP available. Red Hat build of Keycloak allows you to either choose from a set of pre-defined default transport stacks, or to define your own custom stack, as you will see later in this chapter.
To explicitly enable distributed infinispan caching, enter this command:
bin/kc.[sh|bat] start --cache=ispn
When you start Red Hat build of Keycloak in development mode, by using the start-dev
command, Red Hat build of Keycloak uses only local caches and distributed caches are completely disabled by implicitly setting the --cache=local
option. The local
cache mode is intended only for development and testing purposes.
10.2. Configuring caches
Red Hat build of Keycloak provides a cache configuration file with sensible defaults located at conf/cache-ispn.xml
.
The cache configuration is a regular Infinispan configuration file.
The following table gives an overview of the specific caches Red Hat build of Keycloak uses. You configure these caches in conf/cache-ispn.xml
:
| Cache name | Cache Type | Description |
|---|---|---|
| realms | Local | Cache persisted realm data |
| users | Local | Cache persisted user data |
| authorization | Local | Cache persisted authorization data |
| keys | Local | Cache external public keys |
| work | Replicated | Propagate invalidation messages across nodes |
| authenticationSessions | Distributed | Caches authentication sessions, created/destroyed/expired during the authentication process |
| sessions | Distributed | Cache persisted user session data |
| clientSessions | Distributed | Cache persisted client session data |
| offlineSessions | Distributed | Cache persisted offline user session data |
| offlineClientSessions | Distributed | Cache persisted offline client session data |
| loginFailures | Distributed | keep track of failed logins, fraud detection |
| actionTokens | Distributed | Caches action Tokens |
10.2.1. Cache types and defaults
Local caches
Red Hat build of Keycloak caches persistent data locally to avoid unnecessary round-trips to the database.
The following data is kept local to each node in the cluster using local caches:
- realms and related data like clients, roles, and groups.
- users and related data like granted roles and group memberships.
- authorization and related data like resources, permissions, and policies.
- keys
Local caches for realms, users, and authorization are configured to hold up to 10,000 entries per default. The local key cache can hold up to 1,000 entries per default and defaults to expire every one hour. Therefore, keys are forced to be periodically downloaded from external clients or identity providers.
In order to achieve an optimal runtime and avoid additional round-trips to the database you should consider looking at the configuration for each cache to make sure the maximum number of entries is aligned with the size of your database. More entries you can cache, less often the server needs to fetch data from the database. You should evaluate the trade-offs between memory utilization and performance.
Invalidation of local caches
Local caching improves performance, but adds a challenge in multi-node setups.
When one Red Hat build of Keycloak node updates data in the shared database, all other nodes need to be aware of it, so they invalidate that data from their caches.
The work
cache is a replicated cache and used for sending these invalidation messages. The entries/messages in this cache are very short-lived, and you should not expect this cache growing in size over time.
Authentication sessions
Authentication sessions are created whenever a user tries to authenticate. They are automatically destroyed once the authentication process completes or due to reaching their expiration time.
The authenticationSessions
distributed cache is used to store authentication sessions and any other data associated with it during the authentication process.
By relying on a distributable cache, authentication sessions are available to any node in the cluster so that users can be redirected to any node without losing their authentication state. However, production-ready deployments should always consider session affinity and favor redirecting users to the node where their sessions were initially created. By doing that, you are going to avoid unnecessary state transfer between nodes and improve CPU, memory, and network utilization.
User sessions
Once the user is authenticated, a user session is created. The user session tracks your active users and their state so that they can seamlessly authenticate to any application without being asked for their credentials again. For each application, the user authenticates with a client session, so that the server can track the applications the user is authenticated with and their state on a per-application basis.
User and client sessions are automatically destroyed whenever the user performs a logout, the client performs a token revocation, or due to reaching their expiration time.
The session data are stored in the database by default and loaded on-demand to the following caches:
-
sessions
-
clientSessions
By relying on a distributable cache, cached user and client sessions are available to any node in the cluster so that users can be redirected to any node without the need to load session data from the database. However, production-ready deployments should always consider session affinity and favor redirecting users to the node where their sessions were initially created. By doing that, you are going to avoid unnecessary state transfer between nodes and improve CPU, memory, and network utilization.
These in-memory caches for user sessions and client sessions are limited to, by default, 10000 entries per node which reduces the overall memory usage of Red Hat build of Keycloak for larger installations. The internal caches will run with only a single owner for each cache entry. Consider trade-off between memory consumption and the database utilization and set different sizes for the caches, edit Red Hat build of Keycloak’s cache config file (conf/cache-ispn.xml
) to set a <memory max-count="..."/>
for those caches.
Volatile user sessions
By default, user sessions are stored in the database and loaded on-demand to the cache. It is possible to configure Red Hat build of Keycloak to store user sessions in the cache only and minimize the database utilization.
Since all the sessions in this setup are stored in-memory, there are two side effects related to this:
- Losing sessions on when all Red Hat build of Keycloak nodes restart.
- Increased memory consumption.
Follow these steps to enable this setup:
Since the cache is the only source of truth for user and client sessions, configure caches to not limit the number of entries and to replicate each entry to at least two nodes. To do so, edit Red Hat build of Keycloak’s cache config file (
conf/cache-ispn.xml
) for cachessessions
andclientSessions
with the following update:-
Remove the
<memory max-count="..."/>
-
Change
owners
attribute of thedistributed-cache
tag to 2 or more
An example of the resulting configuration for the
sessions
cache would look as follows.<distributed-cache name="sessions" owners="2"> <expiration lifespan="-1"/> </distributed-cache>
-
Remove the
Disable
persistent-user-sessions
feature using the following command:bin/kc.sh start --features-disabled=persistent-user-sessions ...
Disabling persistent-user-sessions
is not possible when multi-site
feature is enabled.
Offline user sessions
As an OpenID Connect Provider, the server is also capable of authenticating users and issuing offline tokens. Similarly to regular user and client sessions, when an offline token is issued by the server upon successful authentication, the server also creates an offline user session and an offline client session.
The following caches are used to store offline sessions:
- offlineSessions
- offlineClientSessions
Similarly to regular user and client sessions caches, also the offline user and client session caches are limited to 10000 entries per node by default. Items which are evicted from the memory will be loaded on-demand from the database when needed. Consider trade-off between memory consumption and the database utilization and set different sizes for the caches, edit Red Hat build of Keycloak’s cache config file (conf/cache-ispn.xml
) to set a <memory max-count="..."/>
for those caches.
Password brute force detection
The loginFailures
distributed cache is used to track data about failed login attempts. This cache is needed for the Brute Force Protection feature to work in a multi-node Red Hat build of Keycloak setup.
Action tokens
Action tokens are used for scenarios when a user needs to confirm an action asynchronously, for example in the emails sent by the forgot password flow. The actionTokens
distributed cache is used to track metadata about action tokens.
10.2.2. Configuring cache maximum size
In order to reduce memory usage, it’s possible to place an upper bound on the number of entries which are stored in a given cache. To specify an upper bound of on a cache, you must provide the following command line argument --cache-embedded-${CACHE_NAME}-max-count=
, with ${CACHE_NAME}
replaced with the name of the cache you would like to apply the upper bound to. For example, to apply an upper-bound of 1000
to the offlineSessions
cache you would configure --cache-embedded-offline-sessions-max-count=1000
. An upper bound can not be defined on the following caches: actionToken
, authenticationSessions
, loginFailures
, work
.
10.2.3. Configuring caches for availability
Distributed caches replicate cache entries on a subset of nodes in a cluster and assigns entries to fixed owner nodes.
Each distributed cache, that is a primary source of truth of the data (authenticationSessions
, loginFailures
and actionTokens
) has two owners per default, which means that two nodes have a copy of the specific cache entries. Non-owner nodes query the owners of a specific cache to obtain data. When both owner nodes are offline, all data is lost.
The default number of owners is enough to survive 1 node (owner) failure in a cluster setup with at least three nodes. You are free to change the number of owners accordingly to better fit into your availability requirements. To change the number of owners, open conf/cache-ispn.xml
and change the value for owners=<value>
for the distributed caches to your desired value.
10.2.4. Specify your own cache configuration file
To specify your own cache configuration file, enter this command:
bin/kc.[sh|bat] start --cache-config-file=my-cache-file.xml
The configuration file is relative to the conf/
directory.
10.2.5. CLI options for remote server
For configuration of Red Hat build of Keycloak server for high availability and multi-node clustered setup there was introduced following CLI options cache-remote-host
, cache-remote-port
, cache-remote-username
and cache-remote-password
simplifying configuration within the XML file. Once any of declared CLI parameters are present, it is expected there is no configuration related to remote store present in the XML file.
10.2.5.1. Connecting to an insecure Infinispan server
Disabling security is not recommended in production!
In a development or test environment, it is easier to start an unsecured Infinispan server. For these use case, the CLI options cache-remote-tls-enabled
disables the encryption (TLS) between Red Hat build of Keycloak and Data Grid. Red Hat build of Keycloak will fail to start if the Data Grid server is configured to accept only encrypted connections.
The CLI options cache-remote-username
and cache-remote-password
are optional and, if not set, Red Hat build of Keycloak will connect to the Data Grid server without presenting any credentials. If the Data Grid server has authentication enabled, Red Hat build of Keycloak will fail to start.
10.3. Transport stacks
Transport stacks ensure that distributed cache nodes in a cluster communicate in a reliable fashion. Red Hat build of Keycloak supports a wide range of transport stacks:
- tcp
- udp
- kubernetes
- ec2
- azure
To apply a specific cache stack, enter this command:
bin/kc.[sh|bat] start --cache-stack=<stack>
The default stack is set to udp
when distributed caches are enabled.
10.3.1. Available transport stacks
The following table shows transport stacks that are available without any further configuration than using the --cache-stack
build option:
| Stack name | Transport protocol | Discovery |
|---|---|---|
| tcp | TCP | MPING (uses UDP multicast). |
| udp | UDP | UDP multicast |
The following table shows transport stacks that are available using the --cache-stack
runtime option and a minimum configuration:
| Stack name | Transport protocol | Discovery |
|---|---|---|
| kubernetes | TCP |
DNS_PING (requires |
10.3.2. Additional transport stacks
The following table shows transport stacks that are supported by Red Hat build of Keycloak, but need some extra steps to work. Note that none of these stacks are Kubernetes / OpenShift stacks, so no need exists to enable the google
stack if you want to run Red Hat build of Keycloak on top of the Google Kubernetes engine. In that case, use the kubernetes
stack. Instead, when you have a distributed cache setup running on AWS EC2 instances, you would need to set the stack to ec2
, because ec2 does not support a default discovery mechanism such as UDP.
| Stack name | Transport protocol | Discovery |
|---|---|---|
| ec2 | TCP | NATIVE_S3_PING |
| | TCP | GOOGLE_PING2 |
| azure | TCP | AZURE_PING |
Cloud vendor specific stacks have additional dependencies for Red Hat build of Keycloak. For more information and links to repositories with these dependencies, see the Infinispan documentation.
To provide the dependencies to Red Hat build of Keycloak, put the respective JAR in the providers
directory and build Red Hat build of Keycloak by entering this command:
bin/kc.[sh|bat] start --cache-stack=<ec2|google|azure>
10.3.3. Custom transport stacks
If none of the available transport stacks are enough for your deployment, you are able to change your cache configuration file and define your own transport stack.
For more details, see Using inline JGroups stacks.
Defining a custom stack with encryption using UDP
<jgroups>
<stack name="my-encrypt-udp" extends="udp">
<SSL_KEY_EXCHANGE keystore_name="server.jks"
keystore_password="password"
stack.combine="INSERT_AFTER"
stack.position="VERIFY_SUSPECT2"/>
<ASYM_ENCRYPT asym_keylength="2048"
asym_algorithm="RSA"
change_key_on_coord_leave = "false"
change_key_on_leave = "false"
use_external_key_exchange = "true"
stack.combine="INSERT_BEFORE"
stack.position="pbcast.NAKACK2"/>
</stack>
</jgroups>
<cache-container name="keycloak">
<transport lock-timeout="60000" stack="my-encrypt-udp"/>
...
</cache-container>
When IP multicast (or UDP) is unavailable in your environment, configure Red Hat build of Keycloak using a static list of IP addresses as shown in the following example.
Defining a custom stack without multicast discovery
<jgroups>
<stack name="tcpping" extends="tcp">
<TCPPING initial_hosts="192.168.1.1[7800],192.168.1.2[7800]"
stack.combine="REPLACE"
stack.position="MPING"/>
</stack>
</jgroups>
<cache-container name="keycloak">
<transport lock-timeout="60000" stack="tcpping"/>
...
</cache-container>
- 1
- The
initial_hosts
is a comma separated list of IP and port, using the formatIP[PORT]
.
By default, the value set to the cache-stack
option has precedence over the transport stack you define in the cache configuration file. If you are defining a custom stack, make sure the cache-stack
option is not used for the custom changes to take effect.
10.4. Network Ports
To ensure a healthy Red Hat build of Keycloak clustering, two network ports need to be open.
Red Hat build of Keycloak uses jgroups.bind.port
for the data transport in UDP- and TCP-based stacks.
-
For the TCP-based stacks like
tcp
,ec2
,google
andkubernetes
it picks7800
by default. For the UDP-based stack
udp
it picks a random port by default.To set a fixed port for the
udp
stack as well, for example, to simplify the configuration of firewalls, set the propertyjgroups.bind.port
to7800
.
For failure detection, Red Hat build of Keycloak uses another TCP-based port at an offset of jgroups.fd.port-offset
relative to the first port that defaults to 50000
. If the property jgroups.bind.port
is set to 7800
, it will open a TCP port on 57800
.
Use -D<property>=<value>
to modify the ports above in your JAVA_OPTS_APPEND
environment variable or in your CLI command.
10.5. Securing cache communication
The current Infinispan cache implementation should be secured by various security measures such as RBAC, ACLs, and transport stack encryption.
JGroups handles all the communication between Red Hat build of Keycloak server, and it supports Java SSL sockets for TCP communication. Red Hat build of Keycloak uses CLI options to configure the TLS communication without having to create a customized JGroups stack or modifying the cache XML file.
To enable TLS, cache-embedded-mtls-enabled
must be set to true
. It requires a keystore with the certificate to use: cache-embedded-mtls-key-store-file
sets the path to the keystore, and cache-embedded-mtls-key-store-password
sets the password to decrypt it. The truststore contains the valid certificates to accept connection from, and it can be configured with cache-embedded-mtls-trust-store-file
(path to the truststore), and cache-embedded-mtls-trust-store-password
(password to decrypt it). To restrict unauthorized access, use a self-signed certificate for each Red Hat build of Keycloak deployment.
For JGroups stacks with UDP
or TCP_NIO2
, see the JGroups Encryption documentation on how to set up the protocol stack.
For more information about securing cache communication, see the Infinispan security guide.
10.6. Exposing metrics from caches
Metrics from caches are automatically exposed when the metrics are enabled.
To enable histograms for the cache metrics, set cache-metrics-histograms-enabled
to true
. While these metrics provide more insights into the latency distribution, collecting them might have a performance impact, so you should be cautious to activate them in an already saturated system.
bin/kc.[sh|bat] start --metrics-enabled=true --cache-metrics-histograms-enabled=true
For more details about how to enable metrics, see Enabling Red Hat build of Keycloak Metrics.
10.7. Relevant options
| Value | |
|---|---|
|
|
|
|
| |
|
| |
|
Available only when embedded Infinispan clusters configured | |
|
| |
|
|
|
|
| |
|
| |
|
| |
|
| |
|
Available only when embedded Infinispan clusters configured | |
|
Available only when embedded Infinispan clusters configured | |
|
| |
|
Available only when embedded Infinispan clusters configured | |
|
| |
|
Available only when metrics are enabled |
|
|
| |
|
Available only when remote host is set | |
|
Available only when remote host is set | (default) |
|
Available only when remote host is set |
|
|
Available only when remote host is set | |
|
|
|
