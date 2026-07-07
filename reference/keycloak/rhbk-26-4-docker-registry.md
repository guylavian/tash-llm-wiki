---
title: "Chapter 9. Configuring a Docker registry - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-docker-registry
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/securing_applications_and_services_guide/docker-registry-
guide: securing_applications_and_services_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Configure a Docker registry to use Red Hat build of Keycloak. Note Docker authentication is disabled by default. To enable see the Enabling and disabling features chapter. This section describes how you can configure a Docker registry to use Red Hat build of Keycloak as its authentication server. For more information on how to set up and configure a Docker registry, see the Docker Registry Configu…"
---

# Chapter 9. Configuring a Docker registry - Red Hat build of Keycloak 26.4 Securing Applications and Services Guide

Chapter 9. Configuring a Docker registry
Configure a Docker registry to use Red Hat build of Keycloak.
Docker authentication is disabled by default. To enable see the Enabling and disabling features chapter.
This section describes how you can configure a Docker registry to use Red Hat build of Keycloak as its authentication server.
For more information on how to set up and configure a Docker registry, see the Docker Registry Configuration Guide.
9.1. Docker registry configuration file installation
For users with more advanced Docker registry configurations, it is generally recommended to provide your own registry configuration file. The Red Hat build of Keycloak Docker provider supports this mechanism via the Registry Config File Format Option. Choosing this option will generate output similar to the following:
auth:
token:
realm: http://localhost:8080/realms/master/protocol/docker-v2/auth
service: docker-test
issuer: http://localhost:8080/realms/master
This output can then be copied into any existing registry config file. See the registry config file specification for more information on how the file should be set up, or start with a basic example.
Don’t forget to configure the rootcertbundle
field with the location of the Red Hat build of Keycloak realm’s public key. The auth configuration will not work without this argument.
9.2. Docker registry environment variable override installation
Often times it is appropriate to use a simple environment variable override for develop or POC Docker registries. While this approach is usually not recommended for production use, it can be helpful when one requires quick-and-dirty way to stand up a registry. Simply use the Variable Override Format Option from the client details, and an output should appear like the one below:
REGISTRY_AUTH_TOKEN_REALM: http://localhost:8080/realms/master/protocol/docker-v2/auth
REGISTRY_AUTH_TOKEN_SERVICE: docker-test
REGISTRY_AUTH_TOKEN_ISSUER: http://localhost:8080/realms/master
Don’t forget to configure the REGISTRY_AUTH_TOKEN_ROOTCERTBUNDLE
override with the location of the Red Hat build of Keycloak realm’s public key. The auth configuration will not work without this argument.
9.3. Docker Compose YAML File
This installation method is meant to be an easy way to get a docker registry authenticating against a Red Hat build of Keycloak server. It is intended for development purposes only and should never be used in a production or production-like environment.
The zip file installation mechanism provides a quickstart for developers who want to understand how the Red Hat build of Keycloak server can interact with the Docker registry. In order to configure:
Procedure
- From the desired realm, create a client configuration. At this point you will not have a Docker registry - the quickstart will take care of that part.
- Choose the Docker Compose YAML option from the from Action menu and select the Download adapter config option to download the ZIP file.
- Unzip the archive to the desired location, and open the directory.
-
Start the Docker registry with
docker-compose up
it is recommended that you configure the Docker registry client in a realm other than 'master', since the HTTP Basic auth flow will not present forms.
Once the above configuration has taken place, and the keycloak server and Docker registry are running, docker authentication should be successful:
[user ~]# docker login localhost:5000 -u $username
Password: *******
Login Succeeded
