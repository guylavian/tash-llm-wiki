---
title: "Chapter 23. Checking if rolling updates are possible - Red Hat build of Keycloak 26.2 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-update-compatibility
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/update-compatibility-
guide: server_configuration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "Execute the update compatibility command to check if Red Hat build of Keycloak supports a rolling update for a change in your deployment. Use the update compatibility command to determine if you can update your deployment with a rolling update strategy when enabling or disabling features or changing the Red Hat build of Keycloak version, configurations or providers and themes. The outcome shows wh…"
---

# Chapter 23. Checking if rolling updates are possible - Red Hat build of Keycloak 26.2 Server Configuration Guide

Chapter 23. Checking if rolling updates are possible
Execute the update compatibility command to check if Red Hat build of Keycloak supports a rolling update for a change in your deployment.
Use the update compatibility command to determine if you can update your deployment with a rolling update strategy when enabling or disabling features or changing the Red Hat build of Keycloak version, configurations or providers and themes. The outcome shows whether a rolling update is possible or if a recreate update is required.
In its current version, it shows that a rolling update is possible when the Red Hat build of Keycloak version is the same for the old and the new version. Future versions of Red Hat build of Keycloak might change that behavior to use additional information from the configuration, the image and the version to determine if a rolling update is possible.
This is fully scriptable, so your update procedure can use that information to perform a rolling or recreate strategy depending on the change performed. It is also GitOps friendly, as it allows storing the metadata of the previous configuration in a file. Use this file in a CI/CD pipeline with the new configuration to determine if a rolling update is possible or if a recreate update is needed.
If you are using the Red Hat build of Keycloak Operator, continue to the Avoiding downtime with rolling updates chapter and the Auto
strategy for more information.
23.1. Supported update strategies
- Rolling Update
- In this guide, a rolling update is an update that can be performed with zero downtime for your deployment, which consists of at least two nodes. Update your Red Hat build of Keycloak one by one; shut down one of your old deployment nodes and start a new deployment node. Wait until the new node’s start-up probe returns success before proceeding to the next Red Hat build of Keycloak node. See chapter Tracking instance status with health checks for details on how to enable and use the start-up probe.
- Recreate Update
- A recreate update is not compatible with zero-downtime and requires downtime to be applied. Shut down all nodes of the cluster running the old version before starting the nodes with the new version.
23.2. Determining the update strategy for an updated configuration
To determine if a rolling update is possible, run the update compatibility command:
- Generate the required metadata with the old configuration.
- Check the metadata with the new configuration to determine the update strategy.
This command currently offers only a limited functionality. At the moment, it takes into consideration only the version of Red Hat build of Keycloak and the embedded Infinispan to determine if a rolling update is possible. If those are unchanged, it reports that a rolling update is possible.
The current version does not yet verify configuration changes and assumes all configuration changes are eligible for a rolling update. The same applies to changes to custom extensions and themes.
A good use case when to use this is, for example, when you want to do a rolling update when you change the Red Hat build of Keycloak theme or your custom extensions, and only want run recreate update when the version of Red Hat build of Keycloak changes which does not yet allow a rolling update.
While consumers of these commands should know the limitations that exist today, they should not rely on the internal behavior or the structure of the metadata file. Instead, they should rely only on the exit code of the check
command to benefit from future enhancements on the internal logic to determine when a rolling update is possible.
23.2.1. Generating the Metadata
To generate the metadata, execute the following command using the same Red Hat build of Keycloak version and configuration options:
Generate and save the metadata from the current deployment.
bin/kc.[sh|bat] update-compatibility metadata --file=/path/to/file.json
This command accepts all options used by the start
command. The command displays the metadata, in JSON format, in the console for debugging purposes. The --file
parameter allows you to save the metadata to a file. Use this file with the subsequent check
command.
Ensure that all configuration options, whether set via environment variables or CLI arguments, are included when running the above command.
Omitting any configuration options results in incomplete metadata, and could lead to a wrong reported result in the next step.
23.2.2. Checking the Metadata
This command checks the metadata generated by the previous command and compares it with the current configuration and Red Hat build of Keycloak version. If you are upgrading to a new Red Hat build of Keycloak version, this command must be executed with the new version.
Check the metadata from a previous deployment.
bin/kc.[sh|bat] update-compatibility check --file=/path/to/file.json
- Ensure that all configuration options, whether set via environment variables or CLI arguments, are included when running this command.
- Verify that the correct Red Hat build of Keycloak version is used.
Failure to meet these requirements results in an incorrect outcome.
The command prints the result to the console. For example, if a rolling update is possible, it displays:
Rolling Update possible message
[OK] Rolling Update is available.
If no rolling update is possible, the command provides details about the incompatibility:
Rolling Update not possible message
[keycloak] Rolling Update is not available. 'keycloak.version' is incompatible: 26.2.0 -> 26.2.1
- 1
- In this example, the Keycloak version
26.2.0
is not compatible with version26.2.1
and a rolling update is not possible.
Command exit code
Use the command’s exit code to determine the update type in your automation pipeline:
| Exit Code | Description |
|---|---|
|
| Rolling Update is possible. |
|
| Unexpected error occurred (such as the metadata file is missing or corrupted). |
|
| Invalid CLI option. |
|
| Rolling Update is not possible. The deployment must be shut down before applying the new configuration. |
|
|
Rolling Update is not possible. The feature |
23.3. Further reading
The Red Hat build of Keycloak Operator uses the functionality described above to determine if a rolling update is possible. See the Avoiding downtime with rolling updates chapter and the Auto
strategy for more information.
