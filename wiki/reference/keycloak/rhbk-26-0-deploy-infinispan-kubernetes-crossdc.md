---
title: "Chapter 9. Deploy Data Grid for HA with the Data Grid Operator - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-deploy-infinispan-kubernetes-crossdc
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/deploy-infinispan-kubernetes-crossdc-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 9. Deploy Data Grid for HA with the Data Grid Operator - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 9. Deploy Data Grid for HA with the Data Grid Operator
This chapter describes the procedures required to deploy Data Grid in a multiple-cluster environment (cross-site). For simplicity, this topic uses the minimum configuration possible that allows Red Hat build of Keycloak to be used with an external Data Grid.
This chapter assumes two OpenShift clusters named Site-A
and Site-B
.
This is a building block following the concepts described in the Concepts for multi-site deployments chapter. See the Multi-site deployments chapter for an overview.
Only Data Grid version 8.5.2 or more recent patch releases are supported for external Data Grid deployments.
9.1. Architecture
This setup deploys two synchronously replicating Data Grid clusters in two sites with a low-latency network connection. An example of this scenario could be two availability zones in one AWS region.
Red Hat build of Keycloak, loadbalancer and database have been removed from the following diagram for simplicity.
9.2. Prerequisites
- OpenShift or Kubernetes cluster running
- Understanding of the Data Grid Operator
9.3. Procedure
- Install the Data Grid Operator
Configure the credential to access the Data Grid cluster.
Red Hat build of Keycloak needs this credential to be able to authenticate with the Data Grid cluster. The following
identities.yaml
file sets the username and password with admin permissionscredentials: - username: developer password: strong-password roles: - admin
The
identities.yaml
could be set in a secret as one of the following:As a Kubernetes Resource:
Credential Secret
apiVersion: v1 kind: Secret type: Opaque metadata: name: connect-secret namespace: keycloak data: identities.yaml: Y3JlZGVudGlhbHM6CiAgLSB1c2VybmFtZTogZGV2ZWxvcGVyCiAgICBwYXNzd29yZDogc3Ryb25nLXBhc3N3b3JkCiAgICByb2xlczoKICAgICAgLSBhZG1pbgo=
1 - 1
- The
identities.yaml
from the previous example base64 encoded.
Using the CLI
oc create secret generic connect-secret --from-file=identities.yaml
Check the Configuring Authentication documentation for more details.
These commands must be executed on both OpenShift clusters.
Create a service account.
A service account is required to establish a connection between clusters. The Data Grid Operator uses it to inspect the network configuration from the remote site and to configure the local Data Grid cluster accordingly.
For more details, see the Managing Cross-Site Connections documentation.
Create a
service-account-token
secret type as follows. The same YAML file can be used in both OpenShift clusters.xsite-sa-secret-token.yaml
apiVersion: v1 kind: Secret metadata: name: ispn-xsite-sa-token
1 annotations: kubernetes.io/service-account.name: "xsite-sa"
2 type: kubernetes.io/service-account-token
Create the service account and generate an access token in both OpenShift clusters.
Create the service account in
Site-A
oc create sa -n keycloak xsite-sa oc policy add-role-to-user view -n keycloak -z xsite-sa oc create -f xsite-sa-secret-token.yaml oc get secrets ispn-xsite-sa-token -o jsonpath="{.data.token}" | base64 -d > Site-A-token.txt
Create the service account in
Site-B
oc create sa -n keycloak xsite-sa oc policy add-role-to-user view -n keycloak -z xsite-sa oc create -f xsite-sa-secret-token.yaml oc get secrets ispn-xsite-sa-token -o jsonpath="{.data.token}" | base64 -d > Site-B-token.txt
The next step is to deploy the token from
Site-A
intoSite-B
and the reverse:Deploy
Site-B
token intoSite-A
oc create secret generic -n keycloak xsite-token-secret \ --from-literal=token="$(cat Site-B-token.txt)"
Deploy
Site-A
token intoSite-B
oc create secret generic -n keycloak xsite-token-secret \ --from-literal=token="$(cat Site-A-token.txt)"
Create TLS secrets
In this chapter, Data Grid uses an OpenShift Route for the cross-site communication. It uses the SNI extension of TLS to direct the traffic to the correct Pods. To achieve that, JGroups use TLS sockets, which require a Keystore and Truststore with the correct certificates.
For more information, see the Securing Cross Site Connections documentation or this Red Hat Developer Guide.
Upload the Keystore and the Truststore in an OpenShift Secret. The secret contains the file content, the password to access it, and the type of the store. Instructions for creating the certificates and the stores are beyond the scope of this chapter.
To upload the Keystore as a Secret, use the following command:
Deploy a Keystore
oc -n keycloak create secret generic xsite-keystore-secret \ --from-file=keystore.p12="./certs/keystore.p12" \
1 --from-literal=password=secret \
2 --from-literal=type=pkcs12
3 To upload the Truststore as a Secret, use the following command:
Deploy a Truststore
oc -n keycloak create secret generic xsite-truststore-secret \ --from-file=truststore.p12="./certs/truststore.p12" \
1 --from-literal=password=caSecret \
2 --from-literal=type=pkcs12
3 NoteKeystore and Truststore must be uploaded in both OpenShift clusters.
Create a Cluster for Data Grid with Cross-Site enabled
The Setting Up Cross-Site documentation provides all the information on how to create and configure your Data Grid cluster with cross-site enabled, including the previous steps.
A basic example is provided in this chapter using the credentials, tokens, and TLS Keystore/Truststore created by the commands from the previous steps.
The
Infinispan
CR forSite-A
apiVersion: infinispan.org/v1 kind: Infinispan metadata: name: infinispan
1 namespace: keycloak annotations: infinispan.org/monitoring: 'true'
2 spec: replicas: 3 jmx: enabled: true security: endpointSecretName: connect-secret
3 service: type: DataGrid sites: local: name: site-a
4 expose: type: Route
5 maxRelayNodes: 128 encryption: transportKeyStore: secretName: xsite-keystore-secret
6 alias: xsite
7 filename: keystore.p12
8 routerKeyStore: secretName: xsite-keystore-secret
9 alias: xsite
10 filename: keystore.p12
11 trustStore: secretName: xsite-truststore-secret
12 filename: truststore.p12
13 locations: - name: site-b
14 clusterName: infinispan namespace: keycloak
15 url: openshift://api.site-b
16 secretName: xsite-token-secret
17 - 1
- The cluster name
- 2
- Allows the cluster to be monitored by Prometheus.
- 3
- If using a custom credential, configure here the secret name.
- 4
- The name of the local site, in this case
Site-A
. - 5
- Exposing the cross-site connection using OpenShift Route.
- 6 9
- The secret name where the Keystore exists as defined in the previous step.
- 7 10
- The alias of the certificate inside the Keystore.
- 8 11
- The secret key (filename) of the Keystore as defined in the previous step.
- 12
- The secret name where the Truststore exists as defined in the previous step.
- 13
- The Truststore key (filename) of the Keystore as defined in the previous step.
- 14
- The remote site’s name, in this case
Site-B
. - 15
- The namespace of the Data Grid cluster from the remote site.
- 16
- The OpenShift API URL for the remote site.
- 17
- The secret with the access token to authenticate into the remote site.
For
Site-B
, theInfinispan
CR looks similar to the above. Note the differences in point 4, 11 and 13.The
Infinispan
CR forSite-B
apiVersion: infinispan.org/v1 kind: Infinispan metadata: name: infinispan
1 namespace: keycloak annotations: infinispan.org/monitoring: 'true'
2 spec: replicas: 3 jmx: enabled: true security: endpointSecretName: connect-secret
3 service: type: DataGrid sites: local: name: site-b
4 expose: type: Route
5 maxRelayNodes: 128 encryption: transportKeyStore: secretName: xsite-keystore-secret
6 alias: xsite
7 filename: keystore.p12
8 routerKeyStore: secretName: xsite-keystore-secret
9 alias: xsite
10 filename: keystore.p12
11 trustStore: secretName: xsite-truststore-secret
12 filename: truststore.p12
13 locations: - name: site-a
14 clusterName: infinispan namespace: keycloak
15 url: openshift://api.site-a
16 secretName: xsite-token-secret
17 Creating the caches for Red Hat build of Keycloak.
Red Hat build of Keycloak requires the following caches to be present:
actionTokens
,authenticationSessions
,loginFailures
, andwork
.The Data Grid Cache CR allows deploying the caches in the Data Grid cluster. Cross-site needs to be enabled per cache as documented by Cross Site Documentation. The documentation contains more details about the options used by this chapter. The following example shows the
Cache
CR forSite-A
.-
In
Site-A
create aCache
CR for each of the caches mentioned above with the following content. This is an example for theauthenticationSessions
cache:
apiVersion: infinispan.org/v2alpha1 kind: Cache metadata: name: authenticationsessions namespace: keycloak spec: clusterName: infinispan name: authenticationSessions template: |- distributedCache: mode: "SYNC" owners: "2" statistics: "true" remoteTimeout: "5000" encoding: media-type: "application/x-protostream" locking: acquireTimeout: "4000" transaction: mode: "NON_XA"
1 locking: "PESSIMISTIC"
2 stateTransfer: chunkSize: "16" backups: site-b:
3 backup: strategy: "SYNC"
4 timeout: "4500"
5 failurePolicy: "FAIL"
6 stateTransfer: chunkSize: "16"
The example above is the recommended configuration to achieve the best data consistency.
Background information
Deadlocks may occur in an active-active setup as entries are modified concurrently in both sites.
The
transaction.mode: NON_XA
ensures that the transaction is rolled back keeping the data consistent if this occurs. The settingbackup.failurePolicy: FAIL
is required in this case. It will throw an error that allows the transaction to be safely rolled back. When this occurs, Red Hat build of Keycloak will attempt a retry.The
transaction.locking: PESSIMISTIC
is the only supported locking mode;OPTIMISTIC
is not recommended due to its network costs. The same settings also prevent that one site is updated while the other site is unreachable.The
backup.strategy: SYNC
ensures the data is visible and stored in the other site when the Red Hat build of Keycloak request is completed.NoteThe
locking.acquireTimeout
can be reduced to fail fast in a deadlock scenario. Thebackup.timeout
must always be higher than thelocking.acquireTimeout
.For
Site-B
, theCache
CR is similar, except for thebackups.<name>
outlined in point 3 of the above diagram.authenticationSessions
Cache
CR inSite-B
apiVersion: infinispan.org/v2alpha1 kind: Cache metadata: name: authenticationsessions namespace: keycloak spec: clusterName: infinispan name: authenticationSessions template: |- distributedCache: mode: "SYNC" owners: "2" statistics: "true" remoteTimeout: "5000" encoding: media-type: "application/x-protostream" locking: acquireTimeout: "4000" transaction: mode: "NON_XA"
1 locking: "PESSIMISTIC"
2 stateTransfer: chunkSize: "16" backups: site-a:
3 backup: strategy: "SYNC"
4 timeout: "4500"
5 failurePolicy: "FAIL"
6 stateTransfer: chunkSize: "16"
-
In
9.4. Verifying the deployment
Confirm that the Data Grid cluster is formed, and the cross-site connection is established between the OpenShift clusters.
Wait until the Data Grid cluster is formed
oc wait --for condition=WellFormed --timeout=300s infinispans.infinispan.org -n keycloak infinispan
Wait until the Data Grid cross-site connection is established
oc wait --for condition=CrossSiteViewFormed --timeout=300s infinispans.infinispan.org -n keycloak infinispan
9.5. Connecting Data Grid with Red Hat build of Keycloak
Now that the Data Grid server is running, here are the relevant Red Hat build of Keycloak CR changes necessary to connect it to Red Hat build of Keycloak. These changes will be required in the Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator chapter.
Create a Secret with the username and password to connect to the external Data Grid deployment:
apiVersion: v1 kind: Secret metadata: name: remote-store-secret namespace: keycloak type: Opaque data: username: ZGV2ZWxvcGVy # base64 encoding for 'developer' password: c2VjdXJlX3Bhc3N3b3Jk # base64 encoding for 'secure_password'
Extend the Red Hat build of Keycloak Custom Resource with
additionalOptions
as shown below.NoteAll the memory, resource and database configurations are skipped from the CR below as they have been described in the Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator chapter already. Administrators should leave those configurations untouched.
apiVersion: k8s.keycloak.org/v2alpha1 kind: Keycloak metadata: labels: app: keycloak name: keycloak namespace: keycloak spec: additionalOptions: - name: cache-remote-host
1 value: "infinispan.keycloak.svc" - name: cache-remote-port
2 value: "11222" - name: cache-remote-username
3 secret: name: remote-store-secret key: username - name: cache-remote-password
4 secret: name: remote-store-secret key: password - name: spi-connections-infinispan-quarkus-site-name
5 value: keycloak
- 1 1
- The hostname of the remote Data Grid cluster.
- 2 2
- The port of the remote Data Grid cluster. This is optional and it defaults to
11222
. - 3 3
- The Secret
name
andkey
with the Data Grid username credential. - 4 4
- The Secret
name
andkey
with the Data Grid password credential. - 5 5
- The
spi-connections-infinispan-quarkus-site-name
is an arbitrary Data Grid site name which Red Hat build of Keycloak needs for its Infinispan caches deployment when a remote store is used. This site-name is related only to the Infinispan caches and does not need to match any value from the external Data Grid deployment. If you are using multiple sites for Red Hat build of Keycloak in a cross-DC setup such as Deploy Data Grid for HA with the Data Grid Operator, the site name must be different in each site.
9.5.1. Architecture
This connects Red Hat build of Keycloak to Data Grid using TCP connections secured by TLS 1.3. It uses the Red Hat build of Keycloak’s truststore to verify Data Grid’s server certificate. As Red Hat build of Keycloak is deployed using its Operator on OpenShift in the prerequisites listed below, the Operator already added the service-ca.crt
to the truststore which is used to sign Data Grid’s server certificates. In other environments, add the necessary certificates to Red Hat build of Keycloak’s truststore.
9.6. Next steps
After the Aurora AWS database and Data Grid are deployed and running, use the procedure in the Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator chapter to deploy Red Hat build of Keycloak and connect it to all previously created building blocks.
9.7. Relevant options
| Value | |
|---|---|
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
Available only when remote host is set |
