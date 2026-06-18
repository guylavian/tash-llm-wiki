---
title: "Chapter 1. Federation using Red Hat OpenStack Platform and single sign-on - Red Hat OpenStack Platform 17.1 Integrating OpenStack Identity with external user management services"
type: reference
domain: keycloak
slug: doc-assembly-federation-using-rhosp-and-keycloak
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/integrating_openstack_identity_with_external_user_management_services/assembly_federation-using-rhosp-and-keycloak
guide: integrating_openstack_identity_with_external_user_management_services
documentKind: "Documentation"
---

# Chapter 1. Federation using Red Hat OpenStack Platform and single sign-on - Red Hat OpenStack Platform 17.1 Integrating OpenStack Identity with external user management services

Chapter 1. Federation using Red Hat OpenStack Platform and single sign-on
Red Hat supports using Red Hat’s single sign-on (SSO) technology as an identity provider for Red Hat OpenStack Platform (RHOSP) so that you can use the same federated solution for SSO in RHOSP, that exists in your wider organization.
1.1. Deploying Red Hat OpenStack Platform with single sign-on
Use the enable-federation-openidc.yaml
environment file to deploy Red Hat OpenStack Platform (RHOSP) so that it can be integrated into your federated authentication solution. Federation allows users to log in to the OpenStack Dashboard using single sign-on (SSO). You must use the OpenStack Dashboard for SSO.
By default, users who log out of the OpenStack Dashboard are not logged out of SSO.
Prerequisites
- You have installed Red Hat OpenStack Platform director.
- You have Red Hat’s single sign-on (SSO) federated authentication in your environment.
Procedure
Obtain your OpenStack Identity service (keystone) endpoint, which has the following construction:
https://<FQDN>:<port>
-
Replace
<FQDN>
with the Fully Qualified Domain Name (FQDN) value you assign to theCloudName
parameter in thecustom-domain.yaml
heat template. Replace
<port>
with the number of the required port. For example, if you deploy TLS then the port number is13000
.NoteIf you do not deploy TLS then
<port>
is5000
. Use TLS when deploying production systems.
-
Replace
Provide your SSO administrator with the following redirect URIs:
https://<keystone_endpoint>/v3/auth/OS-FEDERATION/identity_providers/kcipaIDP/protocols/openid/websso https://<keystone_endpoint>/v3/auth/OS-FEDERATION/websso/openid
Replace
<keystone_endpoint>
with your Identity service (keystone) endpoint that you determined in step 1.In response, your SSO administrator provides you with a
ClientID
and aClientSecret
.
Copy the
enable-federation-openidc.yaml
heat template into the stack home directory:$ cp /usr/share/openstack-tripleo-heat-templates/environments/enable-federation-openidc.yaml \ /home/stack/
Edit your copy of the
enable-federation-openidc.yaml
environment file. Below is a sample configuration:parameter_defaults: KeystoneAuthMethods: password,token,oauth1,mapped,application_credential,openid KeystoneOpenIdcClientId: <ClientID> KeystoneOpenIdcClientSecret: <ClientSecret> KeystoneOpenIdcCryptoPassphrase: <user-defined-passphrase> KeystoneOpenIdcIdpName: kcipaIDP KeystoneOpenIdcIntrospectionEndpoint: https://rh-sso.local.com/realms/master/protocol/openid-connect/token/introspect KeystoneOpenIdcProviderMetadataUrl: https://rh-sso.local.com/realms/master/.well-known/openid-configuration KeystoneOpenIdcRemoteIdAttribute: HTTP_OIDC_ISS KeystoneOpenIdcResponseType: id_token KeystoneTrustedDashboards: https://overcloud.redhat.local/dashboard/auth/websso/ WebSSOChoices: [['OIDC', 'OpenID Connect']] WebSSOIDPMapping: {'OIDC': ['kcipaIDP', 'openid']} WebSSOInitialChoice: OIDC KeystoneFederationEnable: True KeystoneOpenIdcEnable: True KeystoneOpenIdcEnableOAuth: True WebSSOEnable: True
-
The
KeystoneAuthMethods
parameter specifies a comma delimited list of acceptable methods for authentication. -
Replace
<ClientID>
with theClientID
for the OpenID Connect provider handshake that your SSO administrator provides. Replace
<ClientSecret>
with theClientSecret
for the OpenID Connect provider handshake that your SSO administrator provides.NoteYou must get this from your SSO administrator after providing your redirect URLs.
-
Replace
<user-defined-passphrase>
with your passphrase that is used when encrypting data for OpenID Connect handshake. -
The
KeystoneOpenIdcIntrospectionEndpoint
parameter must specify the Identity service introspection endpoint, in which you must replace<FQDN>
with yourCloudName
FQDN and replace<realm>
with the SSO realm, the default realm ismaster
: https://<FQDN>/realms/<realm>/protocol/openid-connect/token/introspect -
The
KeystoneOpenIdcProviderMetadataUrl
parameter must specify the URL that points to your OpenID Connect provider metadata. -
The
KeystoneOpenIdcRemoteIdAttribute
parameter must specify the attribute to obtain the entity ID of the Identity Provider from the environment. -
The
KeystoneOpenIdcResponseType
parameter must specify the expected response type from the OpenID Connect provider. -
The
KeystoneTrustedDashboards
parameter must specify the dashboard URL trusted for single sign-on. This can also be a comma delimited list. -
The
WebSSOChoices
parameter specifies the list of SSO authentication choices that you want to present. Each item is a list of an SSO choice identifier and a display message. -
The
WebSSOIDPMapping
parameter provides a mapping from the SSO authentication choice to each identity provider and protocol. The identity provider and protocol names must match the resources defined in the Identity service.
-
The
Add the
enable-federation-openidc.yaml
to the stack with your other environment files and deploy the overcloud:(undercloud)$ openstack overcloud deploy --templates \ -e [your environment files] \ -e /home/stack/templates/enable-federation-openidc.yaml
Next steps
1.2. Integrating Red Hat OpenStack Platform with single sign-on
After you deploy Red Hat OpenStack Platform (RHOSP) with Red Hat’s single sign-on (SSO) for federation, you must integrate SSO with RHOSP.
Procedure
Create a federated domain:
$ openstack domain create <federated_domain_name>
Replace
<federated_domain_name>
with the name of the federated domain, for example,my_domain
.Example output:
+-------------+----------------------------------+ | Field | Value | +-------------+----------------------------------+ | description | | | enabled | True | | id | b493634c9dbf4546a2d1988af181d7c9 | | name | my_domain | | options | {} | | tags | [] | +-------------+----------------------------------+
Set up the federation identity provider:
$ openstack identity provider create --remote-id https://<sso_fqdn>:9443/realms/<realm> --domain <federated_domain_name> kcipaIDP
-
Replace
<sso_fqdn>
with the fully qualified domain name for SSO. Replace
<realm>
with the SSO realm. The default realm ismaster
.Example output:
+-------------------+-----------------------------------------------------+ | Field | Value | +-------------------+-----------------------------------------------------+ | authorization_ttl | None | | description | None | | domain_id | b493634c9dbf4546a2d1988af181d7c9 | | enabled | True | | id | kcipaIDP | | remote_ids | https://sso.fqdn.local:9443/realms/master | +-------------------+-----------------------------------------------------+
-
Replace
Create a mapping file that is unique to the identity needs of your cloud.
Example:
$ cat > mapping.json << EOF [ { "local": [ { "user": { "name": "{0}" }, "group": { "domain": { "name": "<federated_domain_name>" }, "name": "<federated_group_name>" } } ], "remote": [ { "type": "OIDC-preferred_username" } ] } ] EOF
-
Replace
<federated_domain_name>
with the name of the domain that you created in step 1. -
Replace
<federated_group_name>
with the name of the federated group that you will create in a later step.
-
Replace
Use this mapping file to create the federation mapping rules for RHOSP:
openstack mapping create --rules <mapping_file> <mapping_rules>
-
Replace
<mapping_file>
with the name of the mapping file that you created in the previous step, for example,mapping.json
. -
Replace
<mapping_rules>
with the name of the mapping rules created from this file, for example,IPAmap
.
-
Replace
Create a federated group:
$ openstack group create --domain <federation_domain_name> <federation_group_name>
-
Replace
<federated_domain_name>
with the name of the domain that you created in step 1. -
Replace
<federated_group_name>
with the name of the federated group that have specified in the mapping file.
-
Replace
Create an Identity service (keystone) project:
$ openstack project create --domain <federation_domain_name> <federation_project_name>
-
Replace
<federation_project_name>
with the name of the Identity service project.
-
Replace
Add the Identity service federation group to a role:
$ openstack role add --group <federation_group_name> --group-domain <federation_domain_name> --project <federation_project_name> --project-domain <federation_domain_name> member
Create the OpenID federation protocol:
$ openstack federation protocol create openid --mapping <mapping_rules> --identity-provider kcipaIDP
-
Replace
<mapping_rules>
with the name of the mapping rules you created from your mapping file, for example,IPAmap
.
-
Replace
