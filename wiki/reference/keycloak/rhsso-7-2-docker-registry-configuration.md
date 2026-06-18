---
title: "Chapter 4. Docker Registry Configuration - Red Hat Single Sign-On 7.2 Securing Applications and Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-2-docker-registry-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.2/html/securing_applications_and_services_guide/docker_registry_configuration
guide: securing_applications_and_services_guide
version: 7.2
family: rhsso
documentKind: "Documentation"
---

# Chapter 4. Docker Registry Configuration - Red Hat Single Sign-On 7.2 Securing Applications and Services Guide

Chapter 4. Docker Registry Configuration
Docker authentication is disabled by default. To enable see Profiles.
This section describes how you can configure a Docker registry to use Red Hat Single Sign-On as its authentication server.
For more information on how to set up and configure a Docker registry, see the Docker Registry Configuration Guide.
4.1. Docker Registry Configuration File Installation
For users with more advanced docker registry configurations, it is generally recommended to provide your own registry configuration file. The Red Hat Single Sign-On docker provider supports this mechanism via the Registry Config File Format Option. Choosing this option will generate output similar to the following:
auth:
token:
realm: http://localhost:8080/auth/auth/realms/master/protocol/docker-v2/auth
service: docker-test
issuer: http://localhost:8080/auth/auth/realms/master
This output can then be copied into any existing registry config file. See the registry config file specification for more information on how the file should be set up, or start with href:https://github.com/docker/distribution/blob/master/cmd/registry/config-example.yml[a basic example].
Don’t forget to configure the rootcertbundle
field with the location of the Red Hat Single Sign-On realm’s pulic certificate. The auth configuration will not work without this argument.
4.2. Docker Registry Environment Variable Override Installation
Often times it is appropriate to use a simple environment variable override for develop or POC Docker registries. While this approach is usually not recommended for production use, it can be helpful when one requires quick-and-dirty way to stand up a registry. Simply use the Variable Override Format Option from the client installation tab, and an output should appear like the one below:
REGISTRY_AUTH_TOKEN_REALM: http://localhost:8080/auth/auth/realms/master/protocol/docker-v2/auth
REGISTRY_AUTH_TOKEN_SERVICE: docker-test
REGISTRY_AUTH_TOKEN_ISSUER: http://localhost:8080/auth/auth/realms/master
Don’t forget to configure the REGISTRY_AUTH_TOKEN_ROOTCERTBUNDLE
override with the location of the Red Hat Single Sign-On realm’s pulic certificate. The auth configuration will not work without this argument.
4.3. Docker Compose YAML File
This installation method is meant to be an easy way to get a docker registry authenticating against a keycloak server. It is intended for development purposes only and should never be used in a production or production-like environment.
The zip file installation mechanism provides a quickstart for developers who want to understand how the keycloak server can interact with the docker registry. In order to configure:
- From the desired realm, create a client configuration. At this point you won’t have a docker registry - the quickstart will take care of that part.
- Choose the "Docker Compose YAML" option from the installation tab and download the .zip file
- Unzip the archive to the desired location, and open the directory.
-
Start the docker registry with
docker-compose up
INFO: it is recommended that you configure the docker registry client in a realm other than 'master', since the HTTP Basic auth flow will not present forms.
Once the above configuration has taken place, and the keycloak server and docker registry are running, docker authentication should be successful:
[user ~]# docker login localhost:5000 -u $username
Password: *******
Login Succeeded
