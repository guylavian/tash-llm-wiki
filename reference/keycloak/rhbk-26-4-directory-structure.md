---
title: "Chapter 4. Directory Structure - Red Hat build of Keycloak 26.4 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-directory-structure
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/directory-structure-
guide: server_configuration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Understand the purpose of the directories under the installation root. 4.1. Installation Locations If you are installing from a zip file then by default there will be an install root directory of rhbk-26.4.11, which can be created anywhere you choose on your filesystem. /opt/keycloak is the root install location for the server in all containerized usage shown for Red Hat build of Keycloak. Note In…"
---

# Chapter 4. Directory Structure - Red Hat build of Keycloak 26.4 Server Configuration Guide

Chapter 4. Directory Structure
Understand the purpose of the directories under the installation root.
4.1. Installation Locations
If you are installing from a zip file then by default there will be an install root directory of rhbk-26.4.11
, which can be created anywhere you choose on your filesystem.
/opt/keycloak
is the root install location for the server in all containerized usage shown for Red Hat build of Keycloak.
In the rest of the documentation, relative paths are understood to be relative to the install root - for example, conf/file.xml
means <install root>/conf/file.xml
4.2. Directory Structure
Under the Red Hat build of Keycloak install root there exists a number of folders:
bin/ - contains all the shell scripts for the server, including
kc.sh|bat
,kcadm.sh|bat
, andkcreg.sh|bat
- client/ - used internally
conf/ - directory used for configuration files, including
keycloak.conf
- see Configuring Red Hat build of Keycloak. Many options for specifying a configuration file expect paths relative to this directory.-
truststores/ - default path used by the
truststore-paths
option - see Configuring trusted certificates
-
truststores/ - default path used by the
data/ - directory for the server to store runtime information, such as transaction logs
- logs/ - default directory for file logging - see Configuring logging
- lib/ - used internally
- providers/ - directory for user provided dependencies - see Configuring providers for extending the server and Configuring the database for an example of adding a JDBC driver.
- themes/ - directory for customizations to the Admin Console - see Developing Themes
