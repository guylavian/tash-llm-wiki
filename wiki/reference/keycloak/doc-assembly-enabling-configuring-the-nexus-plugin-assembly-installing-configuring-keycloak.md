---
title: "Chapter 5. Enabling and configuring the Nexus Repository Manager plugin - Red Hat Developer Hub 1.8 Configuring dynamic plugins"
type: reference
domain: keycloak
slug: doc-assembly-enabling-configuring-the-nexus-plugin-assembly-installing-configuring-keycloak
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.8/html/configuring_dynamic_plugins/assembly-enabling-configuring-the-nexus-plugin_assembly-installing-configuring-keycloak
guide: configuring_dynamic_plugins
documentKind: "Documentation"
---

# Chapter 5. Enabling and configuring the Nexus Repository Manager plugin - Red Hat Developer Hub 1.8 Configuring dynamic plugins

Chapter 5. Enabling and configuring the Nexus Repository Manager plugin
The Nexus Repository Manager plugin displays the information about your build artifacts in your Developer Hub application. The build artifacts are available in the Nexus Repository Manager.
The Nexus Repository Manager plugin is a Technology Preview feature only.
Technology Preview features are not supported with Red Hat production service level agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
For more information on Red Hat Technology Preview features, see Technology Preview Features Scope.
Additional detail on how Red Hat provides support for bundled community dynamic plugins is available on the Red Hat Developer Support Policy page.
5.1. Enabling the Nexus Repository Manager plugin
The Nexus Repository Manager plugin is pre-loaded in Developer Hub with basic configuration properties. To enable it, set the disabled property to false
as follows:
global:
dynamic:
includes:
- dynamic-plugins.default.yaml
plugins:
- package: ./dynamic-plugins/dist/backstage-community-plugin-nexus-repository-manager
disabled: false
5.2. Configuring the Nexus Repository Manager plugin
Set the proxy to the desired Nexus Repository Manager server in the
app-config.yaml
file as follows:proxy: '/nexus-repository-manager': target: 'https://<NEXUS_REPOSITORY_MANAGER_URL>' headers: X-Requested-With: 'XMLHttpRequest' # Uncomment the following line to access a private Nexus Repository Manager using a token # Authorization: 'Bearer <YOUR TOKEN>' changeOrigin: true # Change to "false" in case of using self hosted Nexus Repository Manager instance with a self-signed certificate secure: true
Optional: Change the base URL of Nexus Repository Manager proxy as follows:
nexusRepositoryManager: # default path is `/nexus-repository-manager` proxyPath: /custom-path
Optional: Enable the following experimental annotations:
nexusRepositoryManager: experimentalAnnotations: true
Annotate your entity using the following annotations:
metadata: annotations: # insert the chosen annotations here # example nexus-repository-manager/docker.image-name: `<ORGANIZATION>/<REPOSITORY>`,
