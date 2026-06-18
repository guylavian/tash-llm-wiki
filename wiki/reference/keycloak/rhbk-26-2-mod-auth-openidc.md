---
title: "Chapter 5. Configuring the mod_auth_openidc Apache HTTPD Module - Red Hat build of Keycloak 26.2 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-mod-auth-openidc
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/securing_applications_and_services_guide/mod-auth-openidc-
guide: securing_applications_and_services_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 5. Configuring the mod_auth_openidc Apache HTTPD Module - Red Hat build of Keycloak 26.2 Securing Applications and Services Guide

Chapter 5. Configuring the mod_auth_openidc Apache HTTPD Module
Configure the mod_auth_openidc Apache module with Red Hat build of Keycloak.
Red Hat build of Keycloak does not provide any official support to mod_auth_openidc. The instructions below are best-effort and may not be up-to-date. We recommend that you stick to official mod_auth_openidc documentation for more details.
The mod_auth_openidc is an Apache HTTP plugin for OpenID Connect. If your language/environment supports using Apache HTTPD as a proxy, then you can use mod_auth_openidc to secure your web application with OpenID Connect. Configuration of this module is beyond the scope of this document. Please see the mod_auth_openidc GitHub repo for more details on configuration.
To configure mod_auth_openidc you’ll need
- The client_id.
- The client_secret.
- The redirect_uri to your application.
- The Red Hat build of Keycloak openid-configuration url
- mod_auth_openidc specific Apache HTTPD module config.
An example configuration would look like the following.
LoadModule auth_openidc_module modules/mod_auth_openidc.so
ServerName ${HOSTIP}
<VirtualHost *:80>
ServerAdmin webmaster@localhost
DocumentRoot /var/www/html
#this is required by mod_auth_openidc
OIDCCryptoPassphrase a-random-secret-used-by-apache-oidc-and-balancer
OIDCProviderMetadataURL ${KC_ADDR}/realms/${KC_REALM}/.well-known/openid-configuration
OIDCClientID ${CLIENT_ID}
OIDCClientSecret ${CLIENT_SECRET}
OIDCRedirectURI http://${HOSTIP}/${CLIENT_APP_NAME}/redirect_uri
# maps the preferred_username claim to the REMOTE_USER environment variable
OIDCRemoteUserClaim preferred_username
<Location /${CLIENT_APP_NAME}/>
AuthType openid-connect
Require valid-user
</Location>
</VirtualHost>
Further information on how to configure mod_auth_openidc can be found on the mod_auth_openidc project page.
