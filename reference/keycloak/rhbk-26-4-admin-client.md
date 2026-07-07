---
title: "Chapter 14. Red Hat build of Keycloak admin client - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-admin-client
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/securing_applications_and_services_guide/admin-client-
guide: securing_applications_and_services_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "Using the Red Hat build of Keycloak admin client to access the Red Hat build of Keycloak Admin REST API. The Red Hat build of Keycloak admin client is a Java library that facilitates the access and usage of the Red Hat build of Keycloak Admin REST API. The library requires Java 11 or higher at runtime (RESTEasy dependency enforces this requirement). To use it from your application add a dependency…"
---

# Chapter 14. Red Hat build of Keycloak admin client - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide

Chapter 14. Red Hat build of Keycloak admin client
Using the Red Hat build of Keycloak admin client to access the Red Hat build of Keycloak Admin REST API.
The Red Hat build of Keycloak admin client is a Java library that facilitates the access and usage of the Red Hat build of Keycloak Admin REST API. The library requires Java 11 or higher at runtime (RESTEasy dependency enforces this requirement). To use it from your application add a dependency on the keycloak-admin-client
library. For example using Maven:
<dependency>
<groupId>org.keycloak</groupId>
<artifactId>keycloak-admin-client</artifactId>
<version>999.0.0-SNAPSHOT</version>
</dependency>
The following example shows how to use the Java client library to get the details of the master realm:
import org.keycloak.admin.client.Keycloak;
import org.keycloak.representations.idm.RealmRepresentation;
...
Keycloak keycloak = Keycloak.getInstance(
"http://localhost:8080",
"master",
"admin",
"password",
"admin-cli");
RealmRepresentation realm = keycloak.realm("master").toRepresentation();
Complete Javadoc for the admin client is available at API Documentation.
14.1. Compatibility with Red Hat build of Keycloak server
The Red Hat build of Keycloak admin client aims to work with multiple versions of the Red Hat build of Keycloak server. For the details about supported Red Hat build of Keycloak server versions, see Upgrading the Red Hat build of Keycloak Client Libraries.
Due the fact that multiple Red Hat build of Keycloak server versions might be supported with the Red Hat build of Keycloak admin client, the Java fields of the underlying "representation" classes, which are representing JSON properties of the request/response body (such as the RealmRepresentation
class shown in the previous section) might not be exactly same for the client and the server.
To avoid compatibility issues, ensure that the com.fasterxml.jackson.databind.ObjectMapper
class, which is used by the admin client under the covers, is initialized with these two properties:
objectMapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
If you are using the basic ways of admin client creation as described above, then these properties are added by default as admin client uses by default the org.keycloak.admin.client.JacksonProvider
class for creating ObjectMapper
, which adds these properties automatically. However if you are injecting your own customJacksonProvider
when creating Keycloak
object, make sure that object mapper is initialized with the properties above if you want to avoid compatibility issues.
For example, consider the situation that the admin client is instantiated in a way as described below with your own MyCustomJacksonProvider
class:
Keycloak.getInstance(
"http://localhost:8080",
"master",
"admin",
"admin",
"admin-cli",
null,
null,
new MyCustomJacksonProvider()
);
In this case, please make sure that your class MyCustomJacksonProvider
extends from the class org.keycloak.admin.client.JacksonProvider
or make sure to configure the ObjectMapper
manually in a way described above. The similar care should be taken when using KeycloakBuilder
to create the admin client and the RestEasy client is manually injected and created.
