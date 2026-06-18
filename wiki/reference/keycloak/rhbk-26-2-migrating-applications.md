---
title: "Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6 - Red Hat build of Keycloak 26.2 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-migrating-applications
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/migration_guide/migrating-applications
guide: migration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6 - Red Hat build of Keycloak 26.2 Migration Guide

Chapter 5. Migrating applications secured by Red Hat Single Sign-On 7.6
Red Hat build of Keycloak introduces key changes to how applications are using some of the Red Hat Single Sign-On 7.6 Client Adapters.
In addition to no longer releasing some client adapters, Red Hat build of Keycloak also introduces fixes and improvements that impact how client applications use OpenID Connect and SAML protocols.
In this chapter, you will find the instructions to address these changes and migrate your application to integrate with Red Hat build of Keycloak .
5.1. Migrating OpenID Connect Clients
The following Java Client OpenID Connect Adapters are no longer released starting with this release of Red Hat build of Keycloak
- Red Hat JBoss Enterprise Application Platform 6.x
- Red Hat JBoss Enterprise Application Platform 7.x
- Spring Boot
- Red Hat Fuse
Compared to when these adapters were first released, OpenID Connect is now widely available across the Java Ecosystem. Also, much better interoperability and support is achieved by using the capabilities available from the technology stack, such as your application server or framework.
These adapters have reached their end of life and are only available from Red Hat Single Sign-On 7.6. It is highly recommended to look for alternatives to keep your applications updated with the latest updates from OAuth2 and OpenID connect protocols.
5.1.1. Upgrading the JBoss EAP OpenID connect adapter
The supported adapter for OIDC is supplied by JBoss EAP 8.0. To upgrade a JBoss EAP OIDC adapter that has been copied to your web application, perform the following procedure.
Procedure
-
Remove the previous adapter modules by deleting the
EAP_HOME/modules/system/add-ons/keycloak/
directory. - Install the OIDC client supplied by JBoss EAP 8.0. For details, see Securing Applications with OIDC.
5.1.2. Key changes in OpenID Connect protocol and client settings
5.1.2.1. Access Type client option no longer available
When you create or update an OpenID Connect client, Access Type is no longer available. However, you can use other methods to achieve this capability.
- To achieve the Bearer Only capability, create a client with no authentication flow. In the Capability config section of the client details, make sure that no flow is selected. The client cannot obtain any tokens from Keycloak, which is equivalent to using the Bearer Only access type.
- To achieve the Public capability, make sure that client authentication is disabled for this client and at least one flow is enabled.
- To achieve Confidential capability, make sure that Client Authentication is enabled for the client and at least one flow is enabled.
The boolean flags bearerOnly and publicClient still exist on the client JSON object. They can be used when creating or updating a client by the admin REST API or when importing this client by partial import or realm import. However, these options are not directly available in the Admin Console v2.
5.1.2.2. Changes in validating schemes for valid redirect URIs
If an application client is using non http(s) custom schemes, the validation now requires that a valid redirect pattern explicitly allows that scheme. Example patterns for allowing custom scheme are custom:/test, custom:/test/* or custom:. For security reasons, a general pattern such as * no longer covers them.
5.1.2.3. Support for the client_id parameter in OpenID Connect Logout Endpoint
Support for the client_id
parameter, which is based on the OIDC RP-Initiated Logout 1.0 specification. This capability is useful to detect what client should be used for Post Logout Redirect URI verification in case that id_token_hint
parameter cannot be used. The logout confirmation screen still needs to be displayed to the user when only the client_id
parameter is used without parameter id_token_hint
, so clients are encouraged to use id_token_hint
parameter if they do not want the logout confirmation screen to be displayed to the user.
5.1.3. Valid Post Logout Redirect URIs
The Valid Post Logout Redirect URIs
configuration option is added to the OIDC client and is aligned with the OIDC specification. You can use a different set of redirect URIs for redirection after login and logout. The value +
used for Valid Post Logout Redirect URIs
means that the logout uses the same set of redirect URIs as specified by the option of Valid Redirect URIs
. This change also matches the default behavior when migrating from a previous version due to backwards compatibility.
5.1.3.1. UserInfo Endpoint Changes
5.1.3.1.1. Error response changes
The UserInfo endpoint is now returning error responses fully compliant with RFC 6750 (The OAuth 2.0 Authorization Framework: Bearer Token Usage). Error code and description (if available) are provided as WWW-Authenticate
challenge attributes rather than JSON object fields.
The responses will be the following, depending on the error condition:
In case no access token is provided:
401 Unauthorized WWW-Authenticate: Bearer realm="myrealm"
In case several methods are used simultaneously to provide an access token (for example, Authorization header + POST access_token parameter), or POST parameters are duplicated:
400 Bad Request WWW-Authenticate: Bearer realm="myrealm", error="invalid_request", error_description="..."
In case an access token is missing
openid
scope:403 Forbidden WWW-Authenticate: Bearer realm="myrealm", error="insufficient_scope", error_description="Missing openid scope"
In case of inability to resolve cryptographic keys for UserInfo response signing/encryption:
500 Internal Server Error
In case of a token validation error, a
401 Unauthorized
is returned in combination with theinvalid_token
error code. This error includes user and client related checks and actually captures all the remaining error cases:401 Unauthorized WWW-Authenticate: Bearer realm="myrealm", error="invalid_token", error_description="..."
5.1.3.1.2. Other Changes to the UserInfo endpoint
It is now required for access tokens to have the openid
scope, which is stipulated by UserInfo being a feature specific to OpenID Connect and not OAuth 2.0. If the openid
scope is missing from the token, the request will be denied as 403 Forbidden
. See the preceding section.
UserInfo now checks the user status, and returns the invalid_token
response if the user is disabled.
5.1.3.1.3. Change of the default Client ID mapper of Service Account Client.
Default Client ID
mapper of Service Account Client
has been changed. Token Claim Name
field value has been changed from clientId
to client_id
. client_id
claim is compliant with OAuth2 specifications:
clientId
userSession note still exists.
5.1.3.1.4. Added iss parameter to OAuth 2.0/OpenID Connect Authentication Response
RFC 9207 OAuth 2.0 Authorization Server Issuer Identification specification adds the parameter iss
in the OAuth 2.0/OpenID Connect Authentication Response for realizing secure authorization responses.
In past releases, we did not have this parameter, but now Red Hat build of Keycloak adds this parameter by default, as required by the specification. However, some OpenID Connect / OAuth2 adapters, and especially older Red Hat build of Keycloak adapters, may have issues with this new parameter. For example, the parameter will be always present in the browser URL after successful authentication to the client application.
In these cases, it may be useful to disable adding the iss
parameter to the authentication response. This can be done for the particular client in the Admin Console, in client details in the section with OpenID Connect Compatibility Modes
. You can enable Exclude Issuer From Authentication Response
to prevent adding the iss
parameter to the authentication response.
5.2. Migrating Red Hat JBoss Enterprise Application Platform applications
5.2.1. Red Hat JBoss Enterprise Application Platform 8.x
Your applications no longer need any additional dependency to integrate with Red Hat build of Keycloak or any other OpenID Provider.
Instead, you can leverage the OpenID Connect support from the JBoss EAP native OpenID Connect Client. For details, see Securing Applications with OIDC.
The JBoss EAP native adapter relies on a configuration schema very similar to the Red Hat build of Keycloak Adapter JSON Configuration. For instance, a deployment using a keycloak.json
configuration file can be mapped to the following configuration in JBoss EAP:
{
"realm": "quickstart",
"auth-server-url": "http://localhost:8180",
"ssl-required": "external",
"resource": "jakarta-servlet-authz-client",
"credentials": {
"secret": "secret"
}
}
For examples about integrating Jakarta-based applications using the JBoss EAP native adapter with Red Hat build of Keycloak, see the following examples at the Red Hat build of Keycloak Quickstart Repository:
It is strongly recommended to migrate to JBoss EAP native OpenID Connect client as it is the best candidate for Jakarta applications deployed to JBoss EAP 8 and newer.
5.2.2. Red Hat JBoss Enterprise Application Platform 7.x
As Red Hat JBoss Enterprise Application Platform 7.x is close to ending full support, Red Hat build of Keycloak will not provide support for it. For existing applications deployed to Red Hat JBoss Enterprise Application Platform 7.x adapters with maintenance support are available through Red Hat Single Sign-On 7.6.
Red Hat Single Sign-On 7.6 adapters are supported to be used in combination with the Red Hat build of Keycloak 26.2 server.
5.2.3. Red Hat JBoss Enterprise Application Platform 6.x
As Red Hat JBoss Enterprise Application PlatformJBoss EAP 6.x has reached end of maintenance support, going forward neither Red Hat Single Sign-On 7.6 or Red Hat build of Keycloak will provide support for it.
5.3. Migrating Spring Boot applications
The Spring Framework ecosystem is evolving fast and you should have a much better experience by leveraging the OpenID Connect support already available there.
Your applications no longer have an additional dependency to integrate with Red Hat build of Keycloak or any other OpenID Provider. Instead, they rely on comprehensive OAuth2/OpenID Connect support from Spring Security. For more details, see this OAuth2 page.
In terms of capabilities, it provides a standard-based OpenID Connect client implementation. An example of a capability that you might want to review, if not already using the standard protocols, is Logout
. Red Hat build of Keycloak provides full support for standard-based logout protocols from the OpenID Connect ecosystem.
For examples of how to integrate Spring Security applications with Red Hat build of Keycloak, see the Quickstart Repository.
If migrating from the Red Hat build of Keycloak Client Adapter for Spring Boot is not an option, you still have access to the adapter from Red Hat Single Sign-On 7.6, which is now in maintenance only support.
Red Hat Single Sign-On 7.6 adapters are supported to be used in combination with the Red Hat build of Keycloak 26.2 server.
5.4. Migrating Red Hat Fuse applications
As Red Hat Fuse has reached the end of full support, Red Hat build of Keycloak 26.2 will not provide any support for it. Red Hat Fuse adapters are still available with maintenance support through Red Hat Single Sign-On 7.6.
Red Hat Single Sign-On 7.6 adapters are supported to be used in combination with the Red Hat build of Keycloak 26.2 server.
5.5. Migrating Applications Using the Authorization Services Policy Enforcer
To support integration with the Red Hat build of Keycloak Authorization Services, the policy enforcer is available separately from the Java Client Adapters.
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-policy-enforcer</artifactId>
<version>${Red Hat build of Keycloak .version}</version>
</dependency>
By decoupling it from the Java Client Adapters, it is possible now to integrate Red Hat build of Keycloak to any Java technology that provides built-in support for OAuth2 or OpenID Connect. The Red Hat build of Keycloak Policy Enforcer provides built-in support for the following types of applications:
- Servlet Application Using Fine-grained Authorization
- Spring Boot REST Service Protected Using Red Hat build of Keycloak Authorization Services
For integration of the Red Hat build of Keycloak Policy Enforcer with different types of applications, consider the following examples:
If migrating from the Red Hat Single Sign-On 7.6 Java Adapter you are using is not an option, you still have access to the adapter from Red Hat Single Sign-On 7.6, which is now in maintenance support.
Red Hat Single Sign-On 7.6 adapters are supported to be used in combination with the Red Hat build of Keycloak 26.2 server.
5.6. Migrating Single Page Applications (SPA) using the Red Hat build of Keycloak JavaScript Adapter
For applications secured by the JavaScript Red Hat Single Sign-On 7.6 adapter, Red Hat build of Keycloak 26.2 includes a new version of the adapter, version 26.2.0.
To upgrade a JavaScript adapter to 26.2.0, perform the following procedure.
Procedure
- Remove the previous version of the JavaScript adapter.
Use these NPM commands to install the 26.2.0 version of this adapter:
npm config set @redhat:registry https://npm.registry.redhat.com install: npm install @redhat/keycloak-js@latest
Depending on how the Javascript adapter is used, some minor changes are required, as described in the following sections.
5.6.1. Legacy Promise API removed
With this release, the legacy Promise API methods from the Red Hat build of Keycloak JS adapter is removed. This means that calling .success()
and .error()
on promises returned from the adapter is no longer possible.
5.6.2. Required to be instantiated with the new operator
In a previous release, deprecation warnings were logged when the Red Hat build of Keycloak JS adapter is constructed without the new operator. Starting with this release, doing so will throw an exception instead. This change is to align with the expected behavior of JavaScript classes, which will allow further refactoring of the adapter in the future.
To migrate applications secured with the Red Hat Single Sign-On 7.6 adapter, upgrade to Red Hat build of Keycloak 26.2, which provides a more recent version of the adapter.
5.7. Migrating SAML applications
5.7.1. Migrating Red Hat JBoss Enterprise Application Platform applications
As of Red Hat build of Keycloak 26.0, the JBoss EAP adapter for SAML is no longer shipped with Red Hat build of Keycloak. If you deployed an application with version 6.x or 7.x of that adapter, that adapter is not supported by Red Hat build of Keycloak. These adapters are only supported to be used in combination with the Red Hat Single Sign-On 7.6.
The fully supported adapter for SAML is the Keycloak SAML Adapter feature pack or RPM for JBoss EAP 8.0.
5.7.1.1. Red Hat JBoss Enterprise Application Platform 8.0
Red Hat build of Keycloak 26.2 includes client adapters for Red Hat JBoss Enterprise Application Platform 8.x, including support for Jakarta EE.
To install the new version of the adapter, see Installing JBoss EAP by using the RPM installation method.
5.7.1.2. Red Hat JBoss Enterprise Application Platform 7.x
As Red Hat JBoss Enterprise Application Platform 7.x is close to ending full support, Red Hat build of Keycloak will not provide support for it. For existing applications deployed to Red Hat JBoss Enterprise Application Platform 7.x adapters with maintenance support are available through Red Hat Single Sign-On 7.6.
Red Hat Single Sign-On 7.6 adapters are supported to be used in combination with the Red Hat build of Keycloak 26.2 server.
5.7.1.3. Red Hat JBoss Enterprise Application Platform 6.x
As Red Hat JBoss Enterprise Application PlatformJBoss EAP 6.x has reached end of maintenance support, going forward neither Red Hat Single Sign-On 7.6 or Red Hat build of Keycloak will provide support for it..
5.7.2. Key changes in SAML protocol and client settings
5.7.2.1. SAML SP metadata changes
Prior to this release, SAML SP metadata contained the same key for both signing and encryption use. Starting with this version of Keycloak, we include only encryption intended realm keys for encryption use in SP metadata. For each encryption key descriptor we also specify the algorithm that it is supposed to be used with. The following table shows the supported XML-Enc algorithms with the mapping to Red Hat build of Keycloak realm keys.
| XML-Enc algorithm | Realm key algorithm |
|---|---|
| rsa-oaep-mgf1p | RSA-OAEP |
| rsa-1_5 | RSA1_5 |
5.7.2.2. Deprecated RSA_SHA1 and DSA_SHA1 algorithms for SAML
Algorithms RSA_SHA1
and DSA_SHA1
, which can be configured as Signature algorithms
on SAML adapters, clients and identity providers are deprecated. We recommend to use safer alternatives based on SHA256
or SHA512
. Also, verifying signatures on signed SAML documents or assertions with these algorithms do not work on Java 17 or higher. If you use this algorithm and the other party consuming your SAML documents is running on Java 17 or higher, verifying signatures will not work.
The possible workaround is to remove algorithms such as the following:
-
http://www.w3.org/2000/09/xmldsig#rsa-sha1
orhttp://www.w3.org/2000/09/xmldsig#dsa-sha1
from the list -
"disallowed algorithms" configured on property
jdk.xml.dsig.secureValidationPolicy
in the file$JAVA_HOME/conf/security/java.security
