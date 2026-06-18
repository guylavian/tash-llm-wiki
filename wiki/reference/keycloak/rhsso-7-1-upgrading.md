---
title: "Chapter 3. Upgrading Red Hat Single Sign-On Server - Red Hat Single Sign-On 7.1 Upgrading Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-upgrading
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/upgrading_guide/upgrading
guide: upgrading_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
---

# Chapter 3. Upgrading Red Hat Single Sign-On Server - Red Hat Single Sign-On 7.1 Upgrading Guide

Chapter 3. Upgrading Red Hat Single Sign-On Server
The upgrade process for the Red Hat Single Sign-On Server is different if you are upgrading to a different minor release or not.
If you are upgrading to a new minor release, for example from 7.0.0 to 7.1.0, follow the steps in Minor Upgrades.
If you are upgrading to a new micro release, for example from 7.1.0 to 7.1.1, follow the steps in Micro Upgrades.
3.1. Minor Upgrades
3.1.1. Preparing for Upgrading
Before you upgrade RH-SSO 7.0 to 7.1, be aware of the order in which you need to perform the upgrade steps. Also note potential issues that can occur within the upgrade process. In general, you must upgrade RH-SSO Server first, and then upgrade the adapters.
- Prior to applying the upgrade, handle any open transactions and delete the data/tx-object-store/ transaction directory.
- Back up RH-SSO 7.0 (configuration, themes, and so on).
- Back up the database. For detailed information on how to back up the database, see the documentation for the relational database you’re using.
Upgrade RH-SSO Server.
- Testing the upgrade in a non-production environment first, to prevent any installation issues from being exposed in production, is a best practice.
- Be aware that after the upgrade the database will no longer be compatible with RH-SSO 7.0.
- Ensure the upgraded server is functional before upgrading adapters in production.
- If you need to revert the upgrade, first restore the RH-SSO 7.0 installation, and then restore the database from the backup copy.
- Upgrade the adapters.
3.1.2. Upgrading RH-SSO Server
It is important that you upgrade RH-SSO Server before upgrading the adapters.
If you are using RH-SSO 7.0 SAML adapters with the isPassive option set to "true" in combination with RH-SSO 7.1 Server, there is a known issue that prevents correct handling of the SAML response. When the user is not authenticated and tries to access a protected page it results in an exception rather than a redirect to authenticate. To prevent this issue from occurring, you must upgrade both RH-SSO Server and the SAML adapter at the same time.
To upgrade RH-SSO Server from 7.0 to 7.1, complete the following steps:
- Prior to applying the upgrade, handle any open transactions and delete the data/tx-object-store/ transaction directory.
- Download the ZIP or TAR archive: rh-sso-7.1.[zip|tar.gz]
- Move the downloaded ZIP or TAR archive to the desired location.
-
Run the
unzip
orgunzip
andtar
utilities. This step installs a clean instance of the latest RH-SSO release. For standalone installations, copy the RHSSO_HOME/standalone/ directory from the previous installation over the RH-SSO 7.1 installation directories.
For domain installations, copy the RHSSO_HOME/domain/ directory from the previous installation over the RH-SSO 7.1 installation directories.
For standalone installations, create the empty directory RHSSO_HOME/standalone/deployments.
For domain installations, create the empty directory RHSSO_HOME/domain/deployments.
Review the changes made to the bin directory of the RH-SSO 7.0 installation, and make the equivalent modifications to the RH-SSO 7.1 directory.
NOTE: Files in the bin directory should not be overwritten by the files from previous versions. Changes should be made manually.
- Copy any custom modules that have been added to the modules directory.
- Run the applicable upgrade script below.
3.1.2.1. Running the Standalone Mode Upgrade Script
To run the upgrade script for standalone mode, complete the following steps:
- If you are using a different configuration file than the default one, edit the migration script to specify the new file name.
- Stop the server.
Run the upgrade script:
bin/jboss-cli.sh --file=bin/migrate-standalone.cli
3.1.2.2. Running the Standalone-High Availability Mode Upgrade Script
For standalone-high availability (HA) mode, all instances must be upgraded at the same time.
To run the upgrade script for standalone-HA mode, complete the following steps:
- If you are using a different configuration file than the default one, edit the migration script to specify the new file name.
- Stop the server.
Run the upgrade script:
bin/jboss-cli.sh --file=bin/migrate-standalone-ha.cli
3.1.2.3. Running the Domain Mode Upgrade Script
For domain mode, all instances must be upgraded at the same time.
To run the upgrade script for domain mode, complete the following steps:
- If you have changed the profile name, you must edit the upgrade script to change a variable near the beginning of the script.
- Edit the domain script to include the location of the keycloak-server.json file.
- Stop the server.
Run the upgrade script on the domain controller only:
bin/jboss-cli.sh --file=bin/migrate-domain.cli
3.1.2.4. Running the Domain-clustered Mode Upgrade Script
For domain-clustered mode, all instances must be upgraded at the same time.
To run the upgrade script for domain-clustered mode, complete the following steps:
- If you have changed the profile name, you must edit the upgrade script to change a variable near the beginning of the script.
- Edit the domain-clustered script to include the location of the keycloak-server.json file.
- Stop the server.
Run the upgrade script on the domain controller only:
bin/jboss-cli.sh --file=bin/migrate-domain-clustered.cli
3.1.3. Migrating the Database
Red Hat Single Sign-On can automatically migrate the database schema, or you can choose to do it manually. By default the database is automatically migrated when you start RH-SSO 7.1 for the first time.
3.1.3.1. Automatic Relational Database Migration
To enable automatic upgrading of the database schema, set the migrationStrategy property value to "update" for the default connectionsJpa provider:
<spi name="connectionsJpa">
<provider name="default" enabled="true">
<properties>
...
<property name="migrationStrategy" value="update"/>
</properties>
</provider>
</spi>
Or run this CLI command:
/subsystem=keycloak-server/spi=connectionsJpa/provider=default/:map-put(name=properties,key=migrationStrategy,value=update)
When you start the server with this setting your database is automatically migrated if the database schema has changed in the new version.
3.1.3.2. Manual Relational Database Migration
To enable manual upgrading of the database schema, set the migrationStrategy property value to "manual" for the default connectionsJpa provider:
<spi name="connectionsJpa">
<provider name="default" enabled="true">
<properties>
...
<property name="migrationStrategy" value="manual"/>
</properties>
</provider>
</spi>
Or run this CLI command:
/subsystem=keycloak-server/spi=connectionsJpa/provider=default/:map-put(name=properties,key=migrationStrategy,value=manual)
When you start the server with this configuration it checks if the database needs to be migrated. The required changes are written to an SQL file that you can review and manually run against the database. For further details on how to apply this file to the database, see the documentation for the relational database you’re using. After the changes have been written to the file, the server exits.
3.1.4. Migrating Themes
If you have created any custom themes they must be migrated to the RH-SSO 7.1 server. For RH-SSO 7.1 any changes to the built-in themes might need to be reflected in your custom themes, depending on which aspects you have customized.
You must copy your custom themes from the RH-SSO 7.0 “themes” directory to the “themes” directory in RH-SSO 7.1. After that you need to review the changes below and consider if the changes need to be applied to your custom theme. In summary:
- If you have customized any of the changed templates for RH-SSO 7.1 listed below you need to compare the template from the base theme to see if there are changes you need to apply.
- If you have customized any of the styles and are extending the Red Hat Single Sign-On themes you need to review the changes to the styles. If you are extending the base theme you can skip this step.
- If you have customized messages you might need to change the key or value or to add additional messages.
Each step is described in more detail below the list of changes.
The changes that have been made for RH-SSO 7.1 include:
Templates
- Account: account.ftl
- Account: federatedIdentity.ftl
- Account: totp.ftl
- Login: info.ftl
- Login: login-config-totp.ftl
- Login: login-reset-password.ftl
- Login: login.ftl
Messages
- Account: editAccountHtmlTtile renamed to editAccountHtmlTitle
- Account: role_uma_authorization added
- Login: loginTotpStep1 value changed
- Login: invalidPasswordGenericMessage added
- Login: invlidRequesterMessage renamed to invalidRequesterMessage
- Login: clientDisabledMessage added
Styles
- Account: account.css
- Login: login.css
3.1.4.1. Migrating Templates
If you have customized any of the templates listed above you need to carefully review the changes that have been made to the templates for RH-SSO 7.1 to decide if you need to apply these changes to your customized templates. Most likely you will need to apply the same changes to your customized templates. If you have not customized any of the listed templates you can skip this section.
A best practice is to use a diff tool to compare the templates to see what changes you might need to make to your customized template. If you have only made minor changes it is simpler to compare the updated RH-SSO 7.1 template to your customized template. However, if you have made many changes it might be easier to compare the RH-SSO 7.1 template to your customized RH-SSO 7.0 template from the RH-SSO 7.0 installation, as this will show you what changes you need to make.
The following screenshot compares the info.ftl template from the Login theme and an example custom theme:
Comparison of the updated version of a Login theme template with an example custom Login theme template
From this comparison it is easy to identify that the first change (“Hello world!!”) was a customization, while the second change (“if pageRedirectUri”) is a change to the base theme. By copying the second change to your custom template, you have successfully updated your customized template.
For the alternative approach the following screenshot compares the info.ftl template from the RH-SSO 7.0 server installation with the updated info.ftl template from the RH-SSO 7.1 server installation:
Comparison of an example custom Login theme template with the updated version of the Login theme template
From this comparison it is easy to identify what has been changed in the base template. You will then manually have to make the same changes to your modified template. Since this approach is not as simple as the first approach, only use this approach if the first one is not feasible.
3.1.4.2. Migrating Messages
If you have added support for another language, you need to apply all the changes listed above. If you have not added support for another language, you might not need to change anything; you only have to make changes if you have changed an affected message in your theme.
For added values, review the value of the message in the base theme to determine if you need to customize that message.
For renamed keys, rename the key in your custom theme.
For changed values, check the value in the base theme to determine if you need to make changes to your custom theme.
3.1.4.3. Migrating Styles
If you are inheriting styles from the keycloak or rh-sso themes you might need to update your custom styles to reflect changes made to the styles from the built-in themes.
A best practice is to use a diff tool to compare the changes to stylesheets between the RH-SSO 7.0 server installation and the RH-SSO 7.1 server installation.
For example, using the diff command: $ diff rh-sso-7.0/themes/keycloak/login/resources/css/login.css \
rh-sso-7.1/themes/keycloak/login/resources/css/login.css
Review the changes and determine if they affect your custom styling.
3.2. Micro Upgrades
3.2.1. Patching a ZIP/Installer Installation
Patches for a ZIP installation of RH-SSO are available to download from the Red Hat Customer Portal.
For multiple RH-SSO hosts in a managed domain environment, individual hosts can be patched from your RH-SSO domain controller.
In addition to applying a patch, you can also roll back the application of a patch.
3.2.1.1. Important Notes on ZIP Installation Patching
-
If you apply a patch that updates a module, the new patched JARs that are used at runtime are stored in
RHSSO_HOME/modules/system/layers/base/.overlays/PATCH_ID/MODULE
. The original unpatched files are left inRHSSO_HOME/modules/system/layers/base/MODULE
, but these JARs are not used at runtime. In order to significantly decrease the size of cumulative patch releases for RH-SSO 7 you cannot perform a partial roll back of a cumulative patch. For a patch that has been applied, you will only be able to roll back the whole patch.
For example, if you apply CP03 to RH-SSO 7.0.0, you will not be able to roll back to CP01 or CP02. If you would like the ability to roll back to each cumulative patch release, each cumulative patch must be applied separately in the order they were released.
3.2.1.2. Applying a Patch
RH-SSO servers that have been installed using the RPM method cannot be updated using these instructions. See the RPM instructions for applying a patch instead.
You can apply downloaded patches to a RH-SSO server using either the management CLI or the management console.
Applying a Patch to RH-SSO Using the Management CLI
- Download the patch file from the Red Hat Customer Portal at https://access.redhat.com/downloads/.
From the management CLI, apply the patch using the following command, including the appropriate path to the patch file:
patch apply /path/to/downloaded-patch.zip
NoteTo patch another RH-SSO host in a managed domain, you can specify the RH-SSO host name using the
--host=
argument. For example:patch apply /path/to/downloaded-patch.zip --host=my-host
The patch tool will warn if there are any conflicts in attempting to apply the patch. If there are conflicts, enter
patch --help
for the available arguments to re-run the command with an argument specifying how to resolve the conflicts.Restart the RH-SSO server for the patch to take effect:
shutdown --restart=true
Applying a Patch to RH-SSO Using the Management Console
- Download the patch file from the Red Hat Customer Portal at https://access.redhat.com/downloads/.
Open the management console and navigate to the Patch Management view.
For a standalone server, click the Patching tab.
The Patch Management Screen for a Standalone Server
For a server in a managed domain, click the Patching tab, then select the host that you want to patch from the table, and click View.
The Patch Management Screen for a Managed Domain
Click Apply a New Patch.
- If you are patching a managed domain host, on the next screen select whether to shutdown the servers on the host, and click Next.
Click the Browse button, select the downloaded patch you want to apply, and then click Next.
Apply Patch Screen
.. If there are any conflicts in attempting to apply the patch, a warning will be displayed. Click View error details to see the detail of the conflicts. If there is a conflict, you can either cancel the operation, or select the Override all conflicts check box and click Next. Overriding conflicts will result in the content of the patch overriding any user modifications.
- After the patch has been successfully applied, select whether to restart RH-SSO now for the patch to take effect, and click Finish.
3.2.1.3. Rolling Back a Patch
You can roll back a previously applied RH-SSO patch using either the management CLI or the management console.
Rolling back a patch using the patch management system is not intended as a general uninstall functionality. It is only intended to be used immediately after the application of a patch that had undesirable effects.
Prerequisites
- A patch that was previously applied.
When following either procedure, use caution when specifying the value of the Reset Configuration
option:
If set to TRUE
, the patch rollback process will also roll back the RH-SSO server configuration files to their pre-patch state. Any changes that were made to the RH-SSO server configuration files after the patch was applied will be lost.
If set to FALSE
, the server configuration files will not be rolled back. In this situation, it is possible that the server will not start after the rollback, as the patch may have altered configurations, such as namespaces, which may no longer be valid and will have to be fixed manually.
Rolling Back a Patch Using the Management CLI
From the management CLI, use the
patch history
command to find the ID of the patch that you want to roll back.NoteIf you are using a managed domain, you must add the
--host=HOSTNAME
argument to the commands in this procedure to specify the RH-SSO host.Roll back the patch with the appropriate patch ID from the previous step.
patch rollback --patch-id=PATCH_ID --reset-configuration=TRUE
The patch tool will warn if there are any conflicts in attempting to roll back the patch. If there are conflicts, enter
patch --help
for the available arguments to re-run the command with an argument specifying how to resolve the conflicts.Restart the RH-SSO server for the patch roll back to take effect:
shutdown --restart=true
Rolling Back a Patch Using the Management Console
Open the management console and navigate to the Patch Management view.
- For a standalone server, click the Patching tab.
- For a server in a managed domain, click the Patching tab, then select the host that you want to patch from the table, and click View.
Select the patch that you want to rollback from those listed in the table, then click Rollback.
Recent Patch History Screen
.. If you are rolling back a patch on a managed domain host, on the next screen select whether to shutdown the servers on the host, and click Next.
Choose your options for the rollback process, then click Next.
Patch Rollback Options
Confirm the options and the patch to be rolled back, then click Next.
- If there are any conflicts in attempting to rollback the patch and the Override all option was not selected, a warning will be displayed. Click View error details to see the detail of the conflicts. If there is a conflict, you can either cancel the operation, or click Choose Options and try the operation again with the Override all check box selected. Overriding conflicts will result in the rollback operation overriding any user modifications.
- After the patch has been successfully rolled back, select whether to restart the RH-SSO server now for the changes to take effect, and click Finish.
3.2.1.4. Clearing Patch History
When patches are applied to a RH-SSO server, the content and history of the patches are preserved for use in rollback operations. If multiple cumulative patches are applied, the patch history may use a significant amount of disk space.
You can use the following management CLI command to remove all older patches that are not currently in use. When using this command, only the latest cumulative patch is preserved along with the GA release. This is only useful for freeing space if multiple cumulative patches have previously been applied.
/core-service=patching:ageout-history
If you clear the patch history, you will not be able to roll back a previously applied patch.
3.2.2. Patching an RPM Installation
Prerequisites
- Ensure that the base operating system is up to date, and is subscribed and enabled to get updates from the standard Red Hat Enterprise Linux repositories.
- Ensure that you are subscribed to the relevant RH-SSO repository for the update.
- Back up all configuration files, deployments, and user data.
For a managed domain, the RH-SSO domain controller should be updated first.
To install a RH-SSO patch via RPM from your subscribed repository, update your Red Hat Enterprise Linux system using the following command:
yum update
