---
title: "Chapter 4. Red Hat build of Keycloak Node.js adapter - Red Hat build of Keycloak 26.0 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-nodejs-adapter
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/securing_applications_and_services_guide/nodejs-adapter-
guide: securing_applications_and_services_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "Red Hat build of Keycloak provides a Node.js adapter built on top of Connect to protect server-side JavaScript apps - the goal was to be flexible enough to integrate with frameworks like Express.js. The adapter uses OpenID Connect protocol under the covers. You can take a look at the Secure applications and services with OpenID Connect chapter for the more generic information about OpenID Connect …"
---

# Chapter 4. Red Hat build of Keycloak Node.js adapter - Red Hat build of Keycloak 26.0 Securing Applications and Services Guide

Chapter 4. Red Hat build of Keycloak Node.js adapter
Red Hat build of Keycloak provides a Node.js adapter built on top of Connect to protect server-side JavaScript apps - the goal was to be flexible enough to integrate with frameworks like Express.js. The adapter uses OpenID Connect protocol under the covers. You can take a look at the Secure applications and services with OpenID Connect chapter for the more generic information about OpenID Connect endpoints and capabilities.
To use the Node.js adapter, first you must create a client for your application in the Red Hat build of Keycloak Admin Console. The adapter supports public, confidential, and bearer-only access type. Which one to choose depends on the use-case scenario.
Once the client is created, click Action at the top right and choose Download adapter config. For Format, choose *Keycloak OIDC JSON and click Download. The downloaded keycloak.json
file is at the root folder of your project.
4.1. Installation
Assuming you have already installed Node.js, create a folder for your application:
mkdir myapp && cd myapp
Use npm init
command to create a package.json
for your application. Now add the Red Hat build of Keycloak connect adapter in the dependencies list:
"dependencies": {
"keycloak-connect": "file:keycloak-connect-26.0.17.tgz"
}
4.2. Usage
- Instantiate a Keycloak class
-
The
Keycloak
class provides a central point for configuration and integration with your application. The simplest creation involves no arguments.
In the root directory of your project create a file called server.js
and add the following code:
const session = require('express-session');
const Keycloak = require('keycloak-connect');
const memoryStore = new session.MemoryStore();
const keycloak = new Keycloak({ store: memoryStore });
Install the express-session
dependency:
npm install express-session
To start the server.js
script, add the following command in the 'scripts' section of the package.json
:
"scripts": {
"test": "echo \"Error: no test specified\" && exit 1",
"start": "node server.js"
},
Now we have the ability to run our server with following command:
npm run start
By default, this will locate a file named keycloak.json
alongside the main executable of your application, in our case on the root folder, to initialize Red Hat build of Keycloak specific settings such as public key, realm name, various URLs.
In that case a Red Hat build of Keycloak deployment is necessary to access Red Hat build of Keycloak admin console.
Please visit links on how to deploy a Red Hat build of Keycloak admin console with Podman or Docker
Now we are ready to obtain the keycloak.json
file by visiting the Red Hat build of Keycloak Admin Console
Paste the downloaded file on the root folder of our project.
Instantiation with this method results in all the reasonable defaults being used. As alternative, it’s also possible to provide a configuration object, rather than the keycloak.json
file:
const kcConfig = {
clientId: 'myclient',
bearerOnly: true,
serverUrl: 'http://localhost:8080',
realm: 'myrealm',
realmPublicKey: 'MIIBIjANB...'
};
const keycloak = new Keycloak({ store: memoryStore }, kcConfig);
Applications can also redirect users to their preferred identity provider by using:
const keycloak = new Keycloak({ store: memoryStore, idpHint: myIdP }, kcConfig);
- Configuring a web session store
-
If you want to use web sessions to manage server-side state for authentication, you need to initialize the
Keycloak(…)
with at least astore
parameter, passing in the actual session store thatexpress-session
is using.
const session = require('express-session');
const memoryStore = new session.MemoryStore();
// Configure session
app.use(
session({
secret: 'mySecret',
resave: false,
saveUninitialized: true,
store: memoryStore,
})
);
const keycloak = new Keycloak({ store: memoryStore });
- Passing a custom scope value
-
By default, the scope value
openid
is passed as a query parameter to Red Hat build of Keycloak’s login URL, but you can add an additional custom value:
const keycloak = new Keycloak({ scope: 'offline_access' });
4.3. Installing middleware
Once instantiated, install the middleware into your connect-capable app:
In order to do so, first we have to install Express:
npm install express
then require Express in our project as outlined below:
const express = require('express');
const app = express();
and configure Keycloak middleware in Express, by adding at the code below:
app.use( keycloak.middleware() );
Last but not least, let’s set up our server to listen for HTTP requests on port 3000 by adding the following code to main.js
:
app.listen(3000, function () {
console.log('App listening on port 3000');
});
4.4. Configuration for proxies
If the application is running behind a proxy that terminates an SSL connection Express must be configured per the express behind proxies guide. Using an incorrect proxy configuration can result in invalid redirect URIs being generated.
Example configuration:
const app = express();
app.set( 'trust proxy', true );
app.use( keycloak.middleware() );
4.5. Protecting resources
- Simple authentication
-
To enforce that a user must be authenticated before accessing a resource, simply use a no-argument version of
keycloak.protect()
:
app.get( '/complain', keycloak.protect(), complaintHandler );
- Role-based authorization
- To secure a resource with an application role for the current app:
app.get( '/special', keycloak.protect('special'), specialHandler );
To secure a resource with an application role for a different app:
app.get( '/extra-special', keycloak.protect('other-app:special'), extraSpecialHandler );
To secure a resource with a realm role:
app.get( '/admin', keycloak.protect( 'realm:admin' ), adminHandler );
- Resource-Based Authorization
-
Resource-Based Authorization allows you to protect resources, and their specific methods/actions,** based on a set of policies defined in Keycloak, thus externalizing authorization from your application. This is achieved by exposing a
keycloak.enforcer
method which you can use to protect resources.*
app.get('/apis/me', keycloak.enforcer('user:profile'), userProfileHandler);
The keycloak-enforcer
method operates in two modes, depending on the value of the response_mode
configuration option.
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'token'}), userProfileHandler);
If response_mode
is set to token
, permissions are obtained from the server on behalf of the subject represented by the bearer token that was sent to your application. In this case, a new access token is issued by Keycloak with the permissions granted by the server. If the server did not respond with a token with the expected permissions, the request is denied. When using this mode, you should be able to obtain the token from the request as follows:
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'token'}), function (req, res) {
const token = req.kauth.grant.access_token.content;
const permissions = token.authorization ? token.authorization.permissions : undefined;
// show user profile
});
Prefer this mode when your application is using sessions and you want to cache previous decisions from the server, as well automatically handle refresh tokens. This mode is especially useful for applications acting as a client and resource server.
If response_mode
is set to permissions
(default mode), the server only returns the list of granted permissions, without issuing a new access token. In addition to not issuing a new token, this method exposes the permissions granted by the server through the request
as follows:
app.get('/apis/me', keycloak.enforcer('user:profile', {response_mode: 'permissions'}), function (req, res) {
const permissions = req.permissions;
// show user profile
});
Regardless of the response_mode
in use, the keycloak.enforcer
method will first try to check the permissions within the bearer token that was sent to your application. If the bearer token already carries the expected permissions, there is no need to interact with the server to obtain a decision. This is specially useful when your clients are capable of obtaining access tokens from the server with the expected permissions before accessing a protected resource, so they can use some capabilities provided by Keycloak Authorization Services such as incremental authorization and avoid additional requests to the server when keycloak.enforcer
is enforcing access to the resource.
By default, the policy enforcer will use the client_id
defined to the application (for instance, via keycloak.json
) to reference a client in Keycloak that supports Keycloak Authorization Services. In this case, the client can not be public given that it is actually a resource server.
If your application is acting as both a public client(frontend) and resource server(backend), you can use the following configuration to reference a different client in Keycloak with the policies that you want to enforce:
keycloak.enforcer('user:profile', {resource_server_id: 'my-apiserver'})
It is recommended to use distinct clients in Keycloak to represent your frontend and backend.
If the application you are protecting is enabled with Keycloak authorization services and you have defined client credentials in keycloak.json
, you can push additional claims to the server and make them available to your policies in order to make decisions. For that, you can define a claims
configuration option which expects a function
that returns a JSON with the claims you want to push:
app.get('/protected/resource', keycloak.enforcer(['resource:view', 'resource:write'], {
claims: function(request) {
return {
"http.uri": ["/protected/resource"],
"user.agent": // get user agent from request
}
}
}), function (req, res) {
// access granted
For more details about how to configure Keycloak to protected your application resources, please take a look at the Authorization Services Guide.
- Advanced authorization
- To secure resources based on parts of the URL itself, assuming a role exists for each section:
function protectBySection(token, request) {
return token.hasRole( request.params.section );
}
app.get( '/:section/:page', keycloak.protect( protectBySection ), sectionHandler );
Advanced Login Configuration:
By default, all unauthorized requests will be redirected to the Red Hat build of Keycloak login page unless your client is bearer-only. However, a confidential or public client may host both browsable and API endpoints. To prevent redirects on unauthenticated API requests and instead return an HTTP 401, you can override the redirectToLogin function.
For example, this override checks if the URL contains /api/ and disables login redirects:
Keycloak.prototype.redirectToLogin = function(req) {
const apiReqMatcher = /\/api\//i;
return !apiReqMatcher.test(req.originalUrl || req.url);
};
4.6. Additional URLs
- Explicit user-triggered logout
-
By default, the middleware catches calls to
/logout
to send the user through a Red Hat build of Keycloak-centric logout workflow. This can be changed by specifying alogout
configuration parameter to themiddleware()
call:
app.use( keycloak.middleware( { logout: '/logoff' } ));
When the user-triggered logout is invoked a query parameter redirect_url
can be passed:
https://example.com/logoff?redirect_url=https%3A%2F%2Fexample.com%3A3000%2Flogged%2Fout
This parameter is then used as the redirect url of the OIDC logout endpoint and the user will be redirected to https://example.com/logged/out
.
- Red Hat build of Keycloak Admin Callbacks
-
Also, the middleware supports callbacks from the Red Hat build of Keycloak console to log out a single session or all sessions. By default, these type of admin callbacks occur relative to the root URL of
/
but can be changed by providing anadmin
parameter to themiddleware()
call:
app.use( keycloak.middleware( { admin: '/callbacks' } );
4.7. Complete example
A complete example using the Node.js adapter usage can be found in Keycloak quickstarts for Node.js
