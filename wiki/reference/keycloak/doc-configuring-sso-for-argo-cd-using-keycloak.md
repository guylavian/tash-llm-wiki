---
title: "Chapter 3. Configuring SSO for Argo CD using Keycloak - Red Hat OpenShift GitOps 1.16 Access control and user management"
type: reference
domain: keycloak
slug: doc-configuring-sso-for-argo-cd-using-keycloak
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.16/html/access_control_and_user_management/configuring-sso-for-argo-cd-using-keycloak
guide: access_control_and_user_management
documentKind: "Documentation"
---

# Chapter 3. Configuring SSO for Argo CD using Keycloak - Red Hat OpenShift GitOps 1.16 Access control and user management

Chapter 3. Configuring SSO for Argo CD using Keycloak
After the Red Hat OpenShift GitOps Operator is installed, Argo CD automatically creates a user with admin
permissions. To manage multiple users, cluster administrators can use Argo CD to configure Single Sign-On (SSO).
3.1. Prerequisites
- Red Hat SSO is installed on the cluster.
- The Red Hat OpenShift GitOps Operator is installed on your OpenShift Container Platform cluster.
- Argo CD is installed on the cluster.
-
The
DeploymentConfig
API is available in the cluster. For more information, see "DeploymentConfig [apps.openshift.io/v1]". - When the Red Hat OpenShift GitOps Operator is deployed on an OpenShift Container Platform cluster configured for FIPS mode, Single Sign-on (SSO) configuration for Argo CD using Keycloak is not supported.
3.2. Configuring a new client in Keycloak
Dex is installed by default for all the Argo CD instances created by the Operator. However, you can delete the Dex configuration and add Keycloak instead to log in to Argo CD using your OpenShift credentials. Keycloak acts as an identity broker between Argo CD and OpenShift.
Procedure
To configure Keycloak, follow these steps:
Delete the Dex configuration by removing the
.spec.sso.dex
parameter from the Argo CD custom resource (CR), and save the CR:dex: openShiftOAuth: true resources: limits: cpu: memory: requests: cpu: memory:
-
Set the value of the
provider
parameter tokeycloak
in the Argo CD CR. Configure Keycloak by performing one of the following steps:
For a secure connection, set the value of the
rootCA
parameter as shown in the following example:apiVersion: argoproj.io/v1beta1 kind: ArgoCD metadata: name: example-argocd labels: example: basic spec: sso: provider: keycloak keycloak: rootCA: "<PEM-encoded-root-certificate>"
1 server: route: enabled: true
- 1
- A custom certificate used to verify the Keycloak’s TLS certificate.
The Operator reconciles changes in the
.spec.sso.keycloak.rootCA
parameter and updates theoidc.config
parameter with the PEM encoded root certificate in theargocd-cm
configuration map.For an insecure connection, leave the value of the
rootCA
parameter empty and use theoidc.tls.insecure.skip.verify
parameter as shown below:apiVersion: argoproj.io/v1beta1 kind: ArgoCD metadata: name: example-argocd labels: example: basic spec: extraConfig: oidc.tls.insecure.skip.verify: "true" sso: provider: keycloak keycloak: rootCA: ""
Optional: Customize the
spec.sso.keycloak
field to add the route name for thekeycloak
provider in theArgoCD
CR. Use this feature to support advanced routing use cases, such as balancing incoming traffic load among multiple Ingress Controller sharding.Add a
host
parameter in theArgoCD
CR by using the following example YAML:Example
ArgoCD
CRapiVersion: argoproj.io/v1alpha1 kind: ArgoCD metadata: name: <resource_name>
1 labels: example: route spec: sso: provider: keycloak keycloak: host: <hostname>
2 server: ingress: enabled: true insecure: true
To create the
ArgoCD CR
, run the following command:$ oc create -f <argocd_filename>.yaml -n <your-namespace>
To edit the
ArgoCD CR
, run the following command:$ oc edit -f <argocd_filename>.yaml -n <your_namespace>
- Save the file to apply the changes.
To apply the
ArgoCD
CR, run the following command:$ oc apply -f <argocd_filename>.yaml -n <your_namespace>
Verify that the
host
attribute is added by running the following command:$ oc get route keycloak -n <your_namespace> -o yaml
Example output
kind: Route metadata: name: keycloak
1 labels: application: keycloak spec: host: sso.test.example.com status: ingress: - host: sso.test.example.com
2 NoteThe Keycloak instance takes 2-3 minutes to install and run.
3.3. Logging in to Keycloak
Log in to the Keycloak console to manage identities or roles and define the permissions assigned to the various roles.
Prerequisites
- The default configuration of Dex is removed.
- Your Argo CD CR must be configured to use the Keycloak SSO provider.
Procedure
Get the Keycloak route URL for login:
$ oc -n argocd get route keycloak NAME HOST/PORT PATH SERVICES PORT TERMINATION WILDCARD keycloak keycloak-default.apps.ci-ln-******.origin-ci-int-aws.dev.**.com keycloak <all> reencrypt None
Get the Keycloak pod name that stores the user name and password as environment variables:
$ oc -n argocd get pods NAME READY STATUS RESTARTS AGE keycloak-1-2sjcl 1/1 Running 0 45m
Get the Keycloak user name:
$ oc -n argocd exec keycloak-1-2sjcl -- "env" | grep SSO_ADMIN_USERNAME SSO_ADMIN_USERNAME=Cqid54Ih
Get the Keycloak password:
$ oc -n argocd exec keycloak-1-2sjcl -- "env" | grep SSO_ADMIN_PASSWORD SSO_ADMIN_PASSWORD=GVXxHifH
On the login page, click LOG IN VIA KEYCLOAK.
NoteYou only see the option LOGIN VIA KEYCLOAK after the Keycloak instance is ready.
Click Login with OpenShift.
NoteLogin using
kubeadmin
is not supported.- Enter the OpenShift credentials to log in.
Optional: By default, any user logged in to Argo CD has read-only access. You can manage the user level access by updating the
argocd-rbac-cm
config map:policy.csv: <name>, <email>, role:admin
3.4. Uninstalling Keycloak
You can delete the Keycloak resources and their relevant configurations by removing the SSO
field from the Argo CD Custom Resource (CR) file. After you remove the SSO
field, the values in the file look similar to the following:
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
name: example-argocd
labels:
example: basic
spec:
server:
route:
enabled: true
A Keycloak application created by using this method is currently not persistent. Additional configurations created in the Argo CD Keycloak realm are deleted when the server restarts.
3.5. Modifying Keycloak resource requests/limits
By default, the Keycloak container is created with resource requests and limitations. You can change and manage the resource requests.
| Resource | Requests | Limits |
|---|---|---|
| CPU | 500m | 1000m |
| Memory | 512 Mi | 1024 Mi |
Procedure
- Modify the default resource requirements patching the Argo CD custom resource (CR):
$ oc -n openshift-gitops patch argocd openshift-gitops --type='json' -p='[{"op": "add", "path": "/spec/sso", "value": {"provider": "keycloak", "resources": {"requests": {"cpu": "512m", "memory": "512Mi"}, "limits": {"cpu": "1024m", "memory": "1024Mi"}} }}]'
Keycloak created by the Red Hat OpenShift GitOps Operator only persists the changes that are made by the Operator. If the Keycloak restarts, any additional configuration created by the administrator in Keycloak is deleted.
