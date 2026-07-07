---
title: "Chapter 2. Admin REST API - Red Hat build of Keycloak 26.0 Server Developer Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-admin-rest-api
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_developer_guide/admin_rest_api
guide: server_developer_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "Red Hat build of Keycloak comes with a fully functional Admin REST API with all features provided by the Admin Console. To invoke the API you need to obtain an access token with the appropriate permissions. The required permissions are described in the Server Administration Guide. You can obtain a token by enabling authentication for your application using Red Hat build of Keycloak; see the Securi…"
---

# Chapter 2. Admin REST API - Red Hat build of Keycloak 26.0 Server Developer Guide

Chapter 2. Admin REST API
Red Hat build of Keycloak comes with a fully functional Admin REST API with all features provided by the Admin Console.
To invoke the API you need to obtain an access token with the appropriate permissions. The required permissions are described in the Server Administration Guide.
You can obtain a token by enabling authentication for your application using Red Hat build of Keycloak; see the Securing Applications and Services Guide. You can also use direct access grant to obtain an access token.
2.1. Examples of using CURL
2.1.1. Authenticating with a username and password
The following example assumes that you created the user admin
with the password password
in the master
realm as shown in the Getting Started Guide tutorial.
Procedure
Obtain an access token for the user in the realm
master
with usernameadmin
and passwordpassword
:curl \ -d "client_id=admin-cli" \ -d "username=admin" \ -d "password=password" \ -d "grant_type=password" \ "http://localhost:8080/realms/master/protocol/openid-connect/token"
NoteBy default this token expires in 1 minute
The result will be a JSON document.
-
Invoke the API you need by extracting the value of the
access_token
property. Invoke the API by including the value in the
Authorization
header of requests to the API.The following example shows how to get the details of the master realm:
curl \ -H "Authorization: bearer eyJhbGciOiJSUz..." \ "http://localhost:8080/admin/realms/master"
2.1.2. Authenticating with a service account
To authenticate against the Admin REST API using a client_id
and a client_secret
, perform this procedure.
Procedure
Make sure the client is configured as follows:
-
client_id
is a confidential client that belongs to the realm master -
client_id
hasService Accounts Enabled
option enabled client_id
has a custom "Audience" mapper-
Included Client Audience:
security-admin-console
-
Included Client Audience:
-
-
Check that
client_id
has the role 'admin' assigned in the "Service Account Roles" tab.
curl \
-d "client_id=<YOUR_CLIENT_ID>" \
-d "client_secret=<YOUR_CLIENT_SECRET>" \
-d "grant_type=client_credentials" \
"http://localhost:8080/realms/master/protocol/openid-connect/token"
