---
title: "Zero Trust Workload Identity Manager OIDC federation"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-oidc-federation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-oidc-federation
version: 4.22
family: security
documentKind: "Documentation"
---

# Zero Trust Workload Identity Manager OIDC federation

[id="zero-trust-manager-oidc-federation"]
= Zero Trust Workload Identity Manager OIDC federation

[role="_abstract"]
Ensure that your workloads can receive verifiable JSON Web Tokens (JWT-SVIDs) and allow external systems, such as cloud providers, to retrieve public keys from the discovery endpoint. Configure {zero-trust-full} to act as an OpenID Connect (OIDC) provider through the SPIRE server.

The following providers are verified to work with SPIRE OIDC federation:

* Azure Entra ID

* Vault

// About the Entra ID OIDC
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-entraid-oidc-about_{context}"]

= About the Entra ID OpenID Connect

[role="_abstract"]
Integrate Entra ID OpenID Connect (OIDC) with SPIRE to provide workloads with automatic, short-lived cryptographic identities. This configuration allows you to securely authenticate services without maintaining static secrets.

// configure OIDC route
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-create-route-oidc_{context}"]
= Configuring the external certificate for the managed OIDC discovery provider route

[role="_abstract"]
Configure the managed OIDC discovery provider route to use an externally managed TLS certificate. By referencing a TLS secret, you can secure the OIDC endpoint with your own certificate credentials.

.Prerequisites

* You have installed {zero-trust-full} 0.2.0 or later.

* You have deployed the SPIRE Server, SPIRE Agent, SPIFFEE CSI Driver, and the SPIRE OIDC Discovery Provider operands in the cluster.

* You have installed the {cert-manager-operator}. For more information, Installing the cert-manager Operator for Red{nbsp}Hat OpenShift.

* You have created a `ClusterIssuer` or `Issuer` configured with a publicly trusted CA service. For example, an Automated Certificate Management Environment (ACME) type `Issuer` with the "Let's Encrypt ACME" service. For more information, see Configuring an ACME issuer

.Procedure

. Create a `Role` to provide the router service account permissions to read the referenced secret by running the following command:
+
[source,terminal]
----
$ oc create role secret-reader \
  --verb=get,list,watch \
  --resource=secrets \
  --resource-name=$TLS_SECRET_NAME \
  -n zero-trust-workload-identity-manager
----

. Create a `RoleBinding` resource to bind the router service account with the newly created Role resource by running the following command:
+
[source,terminal]
----
$ oc create rolebinding secret-reader-binding \
  --role=secret-reader \
  --serviceaccount=openshift-ingress:router \
  -n zero-trust-workload-identity-manager
----

. Configure the `SpireOIDCDIscoveryProvider` Custom Resource (CR) object to reference the Secret generated in the earlier step by running the following command:
+
[source,terminal]
----
$ oc patch SpireOIDCDiscoveryProvider cluster --type=merge -p='
spec:
  externalSecretRef: ${TLS_SECRET_NAME}
'
----

.Verification

. In the `SpireOIDCDiscoveryProvider` CR, check if the `ManageRouteReady` condition is set to `True` by running the following command:
+
[source,terminal]
----
$ oc wait --for=jsonpath='{.status.conditions[?(@.type=="ManagedRouteReady")].status}'=True SpireOIDCDiscoveryProvider/cluster --timeout=120s
----

. Verify that the OIDC endpoint can be accessed securely through HTTPS by running the following command:
+
[source,terminal]
----
$ curl https://$JWT_ISSUER_ENDPOINT/.well-known/openid-configuration

{
  "issuer": "https://$JWT_ISSUER_ENDPOINT",
  "jwks_uri": "https://$JWT_ISSUER_ENDPOINT/keys",
  "authorization_endpoint": "",
  "response_types_supported": [
    "id_token"
  ],
  "subject_types_supported": [],
  "id_token_signing_alg_values_supported": [
    "RS256",
    "ES256",
    "ES384"
  ]
}%
----

// disable a route
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-disabling-route_{context}"]
= Disabling a managed route

[role="_abstract"]
If you want to fully control the behavior of exposing the OIDC Discovery Provider service, you can disable the managed route based on your requirements.

.Procedure

* To manually configure the OIDC Discovery Provider, set `managedRoute` to `false` by running the following command:
+
[source,terminal]
----
$ oc patch SpireOIDCDiscoveryProvider cluster --type=merge -p='
spec:
  managedRoute: "false"
----

// configure Azure
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-configure-azure_{context}"]
= Using Entra ID with {azure-first}

[role="_abstract"]
Configure your {azure-first} environment to enable Entra ID integration with {azure-short}. By defining variables and creating a resource group, you establish the infrastructure needed to securely manage workload identities.

.Prerequisites

* You have configured the SPIRE OIDC Discovery Provider Route to serve the TLS certificates from a publicly trusted CA.

.Procedure

. Log in to Azure by running the following command:
+
[source,terminal]
----
$ az login
----

. Configure variables for your Azure subscription and tenant by running the following commands:
+
[source,terminal]
----
$ export SUBSCRIPTION_ID=$(az account list --query "[?isDefault].id" -o tsv)
----
+
[source,terminal]
----
$ export TENANT_ID=$(az account list --query "[?isDefault].tenantId" -o tsv)
----
+
[source,terminal]
----
$ export LOCATION=centralus
----
where:

`SUBSCRIPTION_ID`:: Specifies your unique subscription identifier.

`TENANT_ID`:: Specifies the ID for your Azure Active Directory instance.

`LOCATION`:: The Azure region where your resource is created.

. Define resource variable names by running the following commands:
+
[source,terminal]
----
$ export NAME=ztwim
----
+
[source,terminal]
----
$ export RESOURCE_GROUP="${NAME}-rg"
----
+
[source,terminal]
----
$ export STORAGE_ACCOUNT="${NAME}storage"
----
+
[source,terminal]
----
$ export STORAGE_CONTAINER="${NAME}storagecontainer"
----
+
[source,terminal]
----
$ export USER_ASSIGNED_IDENTITY_NAME="${NAME}-identity"
----
where:

`NAME`:: Specifies A base name for all resources.

`RESOURCE_GROUP`:: Specifies the name of the resource group.

`STORAGE_ACCOUNT`:: Specifies the name for the storage account.

`STORAGE_CONTAINER`:: Specifies the name for the storage container.

`USER_ASSIGNED_IDENTITY_NAME`:: Specifies the name for a managed identity.

. Create the resource group by running the following command:
+
[source,terminal]
----
$ az group create \
  --name "${RESOURCE_GROUP}" \
  --location "${LOCATION}"
----

// configure azure blog
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-configure-azure-blob_{context}"]
= Configuring Azure blob storage

[role="_abstract"]
Create a new {azure-first} storage account and container to provide a dedicated location for your content. Configuring this storage ensures that the {zero-trust-full} can successfully store and retrieve blobs for your environment.

.Procedure

. Create a new storage account that is used to store content by running the following command:
+
[source,terminal]
----
$ az storage account create \
  --name ${STORAGE_ACCOUNT} \
  --resource-group ${RESOURCE_GROUP} \
  --location ${LOCATION} \
  --encryption-services blob
----

. Obtain the storage ID for the newly created storage account by running the following command:
+
[source,terminal]
----
$ export STORAGE_ACCOUNT_ID=$(az storage account show -n ${STORAGE_ACCOUNT} -g ${RESOURCE_GROUP} --query id --out tsv)
----

. Create a storage container inside the newly created storage account to provide a location to support the storage of blobs by running the following command:
+
[source,terminal]
----
$ az storage container create \
  --account-name ${STORAGE_ACCOUNT} \
  --name ${STORAGE_CONTAINER} \
  --auth-mode login
----

// configure azure managed identity
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-configure-azure-identity_{context}"]
= Configuring an Azure user managed identity

[role="_abstract"]
Create a user-assigned managed identity in Azure to manage access control for your resources. You must also obtain the Client ID to associate roles with the service principal.

.Procedure

. Create a new User Managed Identity and then obtain the Client ID of the related Service Principal associated with the User Managed Identity by running the following command:
+
[source,terminal]
----
$ az identity create \
  --name ${USER_ASSIGNED_IDENTITY_NAME} \
  --resource-group ${RESOURCE_GROUP}
----
+
[source,terminal]
----
$ export IDENTITY_CLIENT_ID=$(az identity show --resource-group "${RESOURCE_GROUP}" --name "${USER_ASSIGNED_IDENTITY_NAME}" --query 'clientId' -otsv)
----

. Retrieve the `CLIENT_ID` of an Azure user-assigned managed identity and save it as an environment variable by running the following command:
+
[source,terminal]
----
$ export IDENTITY_CLIENT_ID=$(az identity show --resource-group "${RESOURCE_GROUP}" --name "${USER_ASSIGNED_IDENTITY_NAME}" --query 'clientId' -otsv)
----

. Associate a role with the Service Principal associated with the User Managed Identity by running the following command:
+
[source,terminal]
----
$ az role assignment create \
  --role "Storage Blob Data Contributor" \
  --assignee "${IDENTITY_CLIENT_ID}" \
  --scope ${STORAGE_ACCOUNT_ID}
----

// create demo application
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-create-demo-app_{context}"]
= Creating the demonstration application

[role="_abstract"]
Create the demonstration application to verify that the entire system functions correctly. This process validates the configuration of your application secrets and namespaces.

.Procedure

. Set the application name and namespace by running the following commands:
+
[source,terminal]
----
$ export APP_NAME=workload-app
----
+
[source,terminal]
----
$ export APP_NAMESPACE=demo
----

. Create the namespace by running the following command:
+
[source,terminal]
----
$ oc create namespace $APP_NAMESPACE
----

. Create the application Secret by running the following command:
+
[source,terminal]
----
$ oc apply -f - << EOF
apiVersion: v1
kind: Secret
metadata:
  name: $APP_NAME
  namespace: $APP_NAMESPACE
stringData:
  AAD_AUTHORITY: https://login.microsoftonline.com/
  AZURE_AUDIENCE: "api://AzureADTokenExchange"
  AZURE_TENANT_ID: "${TENANT_ID}"
  AZURE_CLIENT_ID: "${IDENTITY_CLIENT_ID}"
  BLOB_STORE_ACCOUNT: "${STORAGE_ACCOUNT}"
  BLOB_STORE_CONTAINER: "${STORAGE_CONTAINER}"
EOF
----

// deploy demo application
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-deploy-app_{context}"]
= Deploying the workload application

[role="_abstract"]
Deploy the workload application to your cluster to validate the {zero-trust-full} environment. This application confirms that the SPIFFE Workload API is functioning and can successfully retrieve JWT tokens.

.Prerequisites

* The demonstration application has been created and deployed.

.Procedure

. To deploy the application, copy the entire command block provided and paste it directly into your terminal. Press *Enter*.
+
[source,terminal]
----
$ oc apply -f - << EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: $APP_NAME
  namespace: $APP_NAMESPACE
---
kind: Deployment
apiVersion: apps/v1
metadata:
  name: $APP_NAME
  namespace: $APP_NAMESPACE
spec:
  selector:
    matchLabels:
      app: $APP_NAME
  template:
    metadata:
      labels:
        app: $APP_NAME
        deployment: $APP_NAME
    spec:
      serviceAccountName: $APP_NAME
      containers:
        - name: $APP_NAME
          image: "registry.redhat.io/ubi9/python-311:latest"
          command:
            - /bin/bash
            - "-c"
            - |
              #!/bin/bash
              pip install spiffe azure-cli

              cat << EOF > /opt/app-root/src/get-spiffe-token.py
              #!/opt/app-root/bin/python
              from spiffe import JwtSource
              import argparse
              parser = argparse.ArgumentParser(description='Retrieve SPIFFE Token.')
              parser.add_argument("-a", "--audience", help="The audience to include in the token", required=True)
              args = parser.parse_args()
              with JwtSource() as source:
                jwt_svid = source.fetch_svid(audience={args.audience})
                print(jwt_svid.token)
              EOF

              chmod +x /opt/app-root/src/get-spiffe-token.py
              while true; do sleep 10; done
          envFrom:
          - secretRef:
              name: $APP_NAME
          env:
            - name: SPIFFE_ENDPOINT_SOCKET
              value: unix:///run/spire/sockets/spire-agent.sock
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
            readOnlyRootFilesystem: false
            runAsNonRoot: true
            seccompProfile:
              type: RuntimeDefault
          ports:
            - containerPort: 8080
              protocol: TCP
          volumeMounts:
            - name: spiffe-workload-api
              mountPath: /run/spire/sockets
              readOnly: true
      volumes:
        - name: spiffe-workload-api
          csi:
            driver: csi.spiffe.io
            readOnly: true
EOF
----

.Verification
. Ensure that the `workload-app` pod is running successfully by running the following command:
+
[source,terminal]
----
$ oc get pods -n $APP_NAMESPACE
----
+
.Example output
[source, terminal]
----
NAME                             READY     STATUS      RESTARTS      AGE
workload-app-5f8b9d685b-abcde    1/1       Running     0             60s
----

. Retrieve the SPIFFE JWT Token (SVID-JWT):

.. Get the pod name dynamically by running the following command:
+
[source,terminal]
----
$ POD_NAME=$(oc get pods -n $APP_NAMESPACE -l app=$APP_NAME -o jsonpath='{.items[0].metadata.name}')
----

.. Run the script inside the pod by running the following command:
+
[source,terminal]
----
$ oc exec -it $POD_NAME -n $APP_NAMESPACE -- \
  /opt/app-root/src/get-spiffe-token.py -a "api://AzureADTokenExchange"
----

// deploy demo application
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-spiffe-identity-federation_{context}"]
= Configuring Azure with the SPIFFE identity federation

[role="_abstract"]
Configure {azure-first} with SPIFFE identity federation to enable password-free, automated authentication for the demonstration application. This federates the User Managed Identity with the SPIFFE identity associated with your workload application.

.Procedure

* Federate the identities between the User Managed Identity and the SPIFFE identity associated with the workload application by running the following command:
+
[source,terminal]
----
$ az identity federated-credential create \
 --name ${NAME} \
 --identity-name ${USER_ASSIGNED_IDENTITY_NAME} \
 --resource-group ${RESOURCE_GROUP} \
 --issuer https://$JWT_ISSUER_ENDPOINT \
 --subject spiffe://$APP_DOMAIN/ns/$APP_NAMESPACE/sa/$APP_NAME \
 --audience api://AzureADTokenExchange
----

// verify access to Azure Blob
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-verify-blob-access_{context}"]
= Verifying that the application workload can access the content in the Azure Blob Storage

[role="_abstract"]
Verify that your application workload can connect to the Azure Blob Storage. By uploading a test file, you validate the authentication token and ensure that the workload has the correct permissions.

.Prerequisites

* An Azure Blob Storage has been created.

.Procedure

. Retrieve a JWT token from the SPIFFE Workload API by running the following command:
+
[source,terminal]
----
$ oc rsh -n $APP_NAMESPACE deployment/$APP_NAME
----

. Create and export an environment variable named `TOKEN` by running the following command:
+
[source,terminal]
----
$ export TOKEN=$(/opt/app-root/src/get-spiffe-token.py --audience=$AZURE_AUDIENCE)
----

. Log in to {azure-short} CLI included within the pod by running the following command:
+
[source,terminal]
----
$ az login --service-principal \
  -t ${AZURE_TENANT_ID} \
  -u ${AZURE_CLIENT_ID} \
  --federated-token ${TOKEN}
----

. Create a new file with the application workload pod and upload the file to the Blob Storage by running the following command:
+
[source,terminal]
----
$ echo “Hello from OpenShift” > openshift-spire-federated-identities.txt
----

. Upload a file to the {azure-short} Blog Storage by running the following command:
+
[source,terminal]
----
$ az storage blob upload \
  --account-name ${BLOB_STORE_ACCOUNT} \
  --container-name ${BLOB_STORE_CONTAINER} \
  --name openshift-spire-federated-identities.txt \
  --file openshift-spire-federated-identities.txt \
  --auth-mode login
----

.Verification
* Confirm the file uploaded successfully by listing the files contained by running the following command:
+
[source,terminal]
----
$ az storage blob list \
  --account-name ${BLOB_STORE_ACCOUNT} \
  --container-name ${BLOB_STORE_CONTAINER} \
  --auth-mode login \
  -o table
----

// About the Vault OIDC
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-vault-oidc-about_{context}"]

= About Vault OpenID Connect

[role="_abstract"]
Use Vault OpenID Connect (OIDC) with SPIRE to securely authenticate workloads. Vault uses SPIRE as a trusted OIDC provider to validate workload identities. This configuration enables workloads to receive short-lived tokens to access secrets and perform actions within Vault.

// Install the Vault OIDC
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-install-vault-oidc_{context}"]

= Installing Vault

[role="_abstract"]
Install HashiCorp Vault to serve as an OpenID Connect (OIDC) provider. This establishes the necessary infrastructure to manage workload identities securely in your {zero-trust-full} environment.

.Prerequisites

* Configure a route. For more information, see Configuring routes

* Helm is installed.

* A command-line JSON processor for easily reading the output from the Vault API.

* A HashiCorp Helm repository is added.

.Procedure

. Create the `vault-helm-value.yaml` file.
+
[source,yaml]
----
global:
  enabled: true
  openshift: true
  tlsDisable: true
injector:
  enabled: false
server:
  ui:
    enabled: true
  image:
    repository: docker.io/hashicorp/vault
    tag: "1.19.0"
  dataStorage:
    enabled: true
    size: 1Gi
  standalone:
    enabled: true
    config: |
      listener "tcp" {
        tls_disable = 1
        address = "[::]:8200"
        cluster_address = "[::]:8201"
      }
      storage "file" {
        path = "/vault/data"
      }
  extraEnvironmentVars: {}
----
+
* The `openshift` field optimizes the deployment for OpenShift-specific security contexts.

* The `tlsDisable` field disables TLS for Kubernetes objects created by the chart.

* The `datastorage.enabled` field creates a 1Gi persistent volume to store Vault data.

* The `standalone.enabled` field deploys a single Vault pod.

* The `tls_disabled` field tells the Vault server to not use TLS.

. Run the `helm install` command:
+
[source,terminal]
----
$ helm install vault hashicorp/vault \
  --create-namespace -n vault \
  --values ./vault-helm-value.yaml
----

. Expose the Vault service by running the following command:
+
[source,terminal]
----
$ oc expose service vault -n vault
----

. Set the `VAULT_ADDR` environment variable to retrieve the hostname from the new route and then export it by running the following command:
+
[source,terminal]
----
$ export VAULT_ADDR="http://$(oc get route vault -n vault -o jsonpath='{.spec.host}')"
----
+
[NOTE]
====
`http://` is prepended because TLS is disabled.
====

.Verification

* To ensure your Vault instance is running, run the following command:
+
[source,terminal]
----
$ curl -s $VAULT_ADDR/v1/sys/health | jq
----
+
.Example output

[source,JSON]
----
{
  "initialized": true,
  "sealed": true,
  "standby": true,
  "performance_standby": false,
  "replication_performance_mode": "disabled",
  "replication_dr_mode": "disabled",
  "server_time_utc": 1663786574,
  "version": "1.19.0",
  "cluster_name": "vault-cluster-a1b2c3d4",
  "cluster_id": "5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b"
}
----

// Initialize the Vault OIDC
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-initialize-vault-oidc_{context}"]

= Initializing and unsealing Vault

[role="_abstract"]
To prepare a newly installed Vault server for operation, initialize and unseal it. This process loads the primary encryption key into memory so that Vault can decrypt data and protect other encryption keys.

The steps to initialize a Vault server are:

. Initialize and unseal Vault

. Enable the key-value (KV) secrets engine and store a test secret

. Configure JSON Web Token (JWT) authentication with SPIRE

. Deploy a demonstration application

. Authenticate and retrieve the secret

.Prerequisites

* Ensure that Vault is running.

* Ensure that Vault is not initialized. You can only initialize a Vault server once.

.Procedure

. Open a remote shell into the `vault` pod by running the following command:
+
[source,terminal]
----
$ oc rsh -n vault statefulset/vault
----

. Initialize Vault to get your unseal key and root token by running the following command:
+
[source,terminal]
----
$ vault operator init -key-shares=1 -key-threshold=1 -format=json
----

. Export the unseal key and root token you received from the earlier command by running the following commands:
+
[source,terminal]
----
$ export UNSEAL_KEY=<Your-Unseal-Key>
----
+
[source,terminal]
----
$ export ROOT_TOKEN=<Your-Root-Token>
----

. Unseal Vault using your unseal key by running the following command:
+
[source,terminal]
----
$ vault operator unseal -format=json $UNSEAL_KEY
----

. Exit the pod by entering `exit`.

.Verification

* To verify that the Vault pod is ready, run the following command:
+
[source,terminal]
----
$ oc get pod -n vault
----
+
.Example output
[source, terminal]
----
NAME        READY        STATUS      RESTARTS     AGE
vault-0     1/1          Running     0            65d
----

// Enable kv secret
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-vault-enable-kv_{context}"]
= Enabling the key-value secrets engine and store a test secret

[role="_abstract"]
Enable the key-value secrets engine to create a secure, centralized location for managing credentials. You can also store a test secret to verify that the engine is working.

.Prerequisites

* Make sure that Vault is initialized and unsealed.

.Procedure

. Open another shell session in the `Vault` pod by running the following command:
+
[source,terminal]
----
$ oc rsh -n vault statefulset/vault
----

. Export your root token again within this new session and log in by running the following command:
+
[source,terminal]
----
$ export ROOT_TOKEN=<Your-Root-Token>
----
+
[source,terminal]
----
$ vault login "${ROOT_TOKEN}"
----

. Enable the KV secrets engine at the `secret/` path and create a test secret by running the following commands:
+
[source,terminal]
----
$ export NAME=ztwim
----
+
[source,terminal]
----
$ vault secrets enable -path=secret kv
----
+
[source,terminal]
----
$ vault kv put secret/$NAME version=v0.1.0
----

.Verification

* To verify that the secret is stored correctly, run the following command:
+
[source,terminal]
----
$ vault kv get secret/$NAME
----

// Authenticate the JWT
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-vault-authenticate-jwt_{context}"]
= Configuring JSON Web Token authentication with SPIRE

[role="_abstract"]
To help your applications securely log in to Vault using SPIFFE identities, configure JSON Web Token (JWT) authentication.

.Prerequisites

* Make sure that Vault is initialized and unsealed.

* Ensure that a test secret is stored in the key-value secrets engine.

.Procedure

. On your local machine, retrieve the SPIRE Certificate Authority (CA) bundle and save it to a file by running the following command:
+
[source,terminal]
----
$ oc get cm -n zero-trust-workload-identity-manager spire-bundle -o jsonpath='{ .data.bundle\.crt }' > oidc_provider_ca.pem
----

. Back in the Vault pod shell, create a temporary file and paste the contents of `oidc_provider_ca.pem` into it by running the following command:
+
[source,terminal]
----
$ cat << EOF > /tmp/oidc_provider_ca.pem
-----BEGIN CERTIFICATE-----
<Paste-Your-Certificate-Content-Here>
-----END CERTIFICATE-----
EOF>
----

. Set up the necessary environment variables for the JWT configuration by running the following commands:
+
[source,terminal]
----
$ export APP_DOMAIN=<Your-App-Domain>
----
+
[source,terminal]
----
$ export JWT_ISSUER_ENDPOINT="oidc-discovery.$APP_DOMAIN"
----
+
[source,terminal]
----
$ export OIDC_URL="https://$JWT_ISSUER_ENDPOINT"
----
+
[source,terminal]
----
$ export OIDC_CA_PEM="$(cat /tmp/oidc_provider_ca.pem)"
----

. Crate a new environment variable by running the following command:
+
[source,terminal]
----
$ export ROLE="${NAME}-role"
----

. Enable the JWT authentication method by running the following command:
+
[source,terminal]
----
$ vault auth enable jwt
----

. Configure you ODIC authentication method by running the following command:
+
[source,terminal]
----
$ vault write auth/jwt/config \
  oidc_discovery_url=$OIDC_URL \
  oidc_discovery_ca_pem="$OIDC_CA_PEM" \
  default_role=$ROLE
----

. Create a policy named `ztwim-policy` by running the following command:
+
[source,terminal]
----
$ export POLICY="${NAME}-policy"
----

. Grant read access to the secret you created earlier by running the following command:
+
[source,terminal]
----
$ vault policy write $POLICY -<<EOF
path "secret/$NAME" {
    capabilities = ["read"]
}
EOF
----

. Create the following environment variables by running the following commands:
+
[source,terminal]
----
$ export APP_NAME=client
----
+
[source,terminal]
----
$ export APP_NAMESPACE=demo
----
+
[source,terminal]
----
$ export AUDIENCE=$APP_NAME
----

. Create a JWT role that binds the policy to workload with a specific SPIFFE ID by running the following command:
+
[source,terminal]
----
$ vault write auth/jwt/role/$ROLE -<<EOF
{
  "role_type": "jwt",
  "user_claim": "sub",
  "bound_audiences": "$AUDIENCE",
  "bound_claims_type": "glob",
  "bound_claims": {
    "sub": "spiffe://$APP_DOMAIN/ns/$APP_NAMESPACE/sa/$APP_NAME"
  },
  "token_ttl": "24h",
  "token_policies": "$POLICY"
}
EOF
----

// deploy a demonstration application
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-vault-deploy-demo_{context}"]

= Deploying a demonstration application

[role="_abstract"]
Deploy a demonstration application to create a simple client that uses its SPIFFE identity to authenticate with Vault. By doing this you can verify that the client can successfully authenticate using the configured identity.

.Procedure

. On your local machine, set the environment variables for your application by running the following commands:
+
[source,terminal]
----
$ export APP_NAME=client
----
+
[source,terminal]
----
$ export APP_NAMESPACE=demo
----
+
[source,terminal]
----
$ export AUDIENCE=$APP_NAME
----

. Apply the Kubernetes manifest to create the namespace, service account, and deployment for the demo app by running the following command. This deployment mounts the SPIFFE CSI driver socket.
+
[source,terminal]
----
$ oc apply -f - <<EOF
# ... (paste the full YAML from your provided code here) ...
EOF>>
----

.Verification

* Verify that the client deployment is ready by running the following command:
+
[source,terminal]
----
$ oc get deploy -n $APP_NAMESPACE
----
+
.Example output
[source, terminal]
----
NAME             READY        UP-TO-DATE      AVAILABLE     AGE
frontend-app     2/2          2               2             120d
backend-api      3/3          3               3             120d
----

// authenticate and retrieve secret
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-oidc-federation.adoc

[id="zero-trust-manager-vault-authenticate-secret_{context}"]
= Authenticating and retrieving the secret

[role="_abstract"]
Use the demonstration application to fetch a JWT token from the SPIFFE Workload API. Use the token to authenticate with Vault so that you can securely retrieve the secret and verify the workflow.

.Procedure

. Fetch a JWT-SVID by running the following command inside the running client pod:
+
[source,terminal]
----
$ oc -n $APP_NAMESPACE exec -it $(oc get pod -o=jsonpath='{.items[*].metadata.name}' -l app=$APP_NAME -n $APP_NAMESPACE) \
  -- /opt/spire/bin/spire-agent api fetch jwt \
  -socketPath /run/spire/sockets/spire-agent.sock \
  -audience $AUDIENCE
----

. Copy the token from the output and export it as an environment variable on your local machine by running the following command:
+
[source,terminal]
----
$ export IDENTITY_TOKEN=<Your-JWT-Token>
----

. Crate a new environment variable by running the following command:
+
[source,terminal]
----
$ export ROLE="${NAME}-role"
----

. Use `curl` to send the JWT token to the Vault login endpoint to get a Vault client token by running the following command:
+
[source,terminal]
----
$ VAULT_TOKEN=$(curl -s --request POST --data '{ "jwt": "'"${IDENTITY_TOKEN}"'", "role": "'"${ROLE}"'"}' "${VAULT_ADDR}"/v1/auth/jwt/login | jq -r '.auth.client_token')
----

.Verification

* Use the newly acquired Vault token to read the secret from the KV store by running the following command:
+
[source,terminal]
----
$ curl -s -H "X-Vault-Token: $VAULT_TOKEN" $VAULT_ADDR/v1/secret/$NAME | jq
----
+
You should see the contents of the secret (`"version": "v0.1.0"`) in the output, confirming the entire workflow is successful
