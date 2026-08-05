---
title: "Chapter 3. Upgrading the Red Hat build of Keycloak server - Red Hat build of Keycloak 26.4 Upgrading Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-upgrading
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/upgrading_guide/upgrading
guide: upgrading_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "You upgrade the server before you upgrade the adapters. 3.1. Preparing for an upgrade Perform the following steps before you upgrade the server. Procedure Shut down Red Hat build of Keycloak. Back up the old installation, such as configuration, themes, and so on. If XA transactions are enabled, handle any open transactions and delete the data/transaction-logs/ transaction directory. Back up the da…"
---

# Chapter 3. Upgrading the Red Hat build of Keycloak server - Red Hat build of Keycloak 26.4 Upgrading Guide

Chapter 3. Upgrading the Red Hat build of Keycloak server
You upgrade the server before you upgrade the adapters.
3.1. Preparing for an upgrade
Perform the following steps before you upgrade the server.
Procedure
- Shut down Red Hat build of Keycloak.
- Back up the old installation, such as configuration, themes, and so on.
-
If XA transactions are enabled, handle any open transactions and delete the
data/transaction-logs/
transaction directory. - Back up the database using the instructions in the documentation for your relational database.
The database schema will no longer be compatible with the old server after the upgrade. Because Red Hat build of Keycloak does not support rolling back the database changes, if you need to roll back to the previous version, first restore the old installation, and then restore the database from the backup copy.
If the persistent-user-sessions
feature is disabled in your current setup and the server is upgraded, all user sessions will be lost except for offline user sessions. Users with these sessions will have to log in again. Note that the persistent-user-sessions
feature is disabled by default in Red Hat build of Keycloak server releases prior to 26.0.0.
Information about failed logins for brute force detection and currently ongoing authentication flows is only stored in the internal caches that are cleared when Red Hat build of Keycloak is shut down. Users currently authenticating, changing their passwords, or resetting their passwords will need to restart the authentication flow once Red Hat build of Keycloak is up and running again.
3.2. Downloading the Red Hat build of Keycloak server
Once you have prepared for the upgrade, you can download the server.
Procedure
Download and extract rhbk-26.4.11.zip from the Red Hat build of Keycloak website.
After extracting this file, you should have a directory that is named
rhbk-26.4.11
.- Move this directory to the desired location.
-
Copy
providers/
andthemes/
from the previous installation to the new installation. -
Copy all files except
cache-ispn.xml
fromconf/
from the previous installation to the new installation. If you modified
cache-ispn.xml
or created a custom cache configuration file:-
Re-apply your changes based on the
cache-ispn.xml
file shipped with the new installation, and place them in the new installation. - Review the latest Red Hat build of Keycloak configuration options for cache sizes and transport stacks if they can be used instead of your modifications as they provide better documentation, additional validations and functionality, and a simpler upgrade experience.
-
Re-apply your changes based on the
3.3. Migrating the database
Red Hat build of Keycloak can automatically migrate the database schema, or you can choose to do it manually. By default the database is automatically migrated when you start the new installation for the first time.
Before you migrate the database, shut down all Red Hat build of Keycloak nodes running the old version of Red Hat build of Keycloak.
Migration is not supported with the default H2 based dev-file
database type.
3.3.1. Automatic relational database migration
To perform an automatic migration, start the server connected to the desired database. If the database schema has changed for the new server version, the migration starts automatically unless the database has too many records.
For example, creating an index on tables with millions of records can be time-consuming and cause a major service disruption. Therefore, a threshold of 300000
records exists for automatic migration. If the number of records exceeds this threshold, the index is not created. Instead, you find a warning in the server logs with the SQL commands that you can apply manually.
To change the threshold, set the index-creation-threshold
property, value for the connections-liquibase
provider:
kc.[sh|bat] start --spi-connections-liquibase--quarkus--index-creation-threshold=300000
You can disable this feature by setting it to zero or a negative number:
kc.[sh|bat] start --spi-connections-liquibase--quarkus--index-creation-threshold=0
3.3.2. Manual relational database migration
To enable manual upgrading of the database schema, set the migration-strategy
property value to "manual" for the default connections-jpa
provider:
kc.[sh|bat] start --spi-connections-jpa--quarkus--migration-strategy=manual
When you start the server with this configuration, the server checks if the database needs to be migrated. If migration is needed, the required changes are written to the bin/keycloak-database-update.sql
SQL file. You can review and manually run these commands against the database.
To change the path and name of the exported SQL file, set the migration-export
property for the default connections-jpa
provider:
kc.[sh|bat] start --spi-connections-jpa--quarkus--migration-export=<path>/<file.sql>
For further details on how to apply this file to the database, see the documentation for your relational database. After the changes have been written to the file, the server exits.
3.4. Migrating themes
If you created custom themes, those themes must be migrated to the new server. Also, any changes to the built-in themes might need to be reflected in your custom themes, depending on which aspects you customized.
Procedure
-
Copy your custom themes from the old server
themes
directory to the new serverthemes
directory. Use the following sections to migrate templates, messages, and styles.
- If you customized any of the updated templates listed in Migration Changes, compare the template from the base theme to check for any changes you need to apply.
- If you customized messages, you might need to change the key or value or to add additional messages.
- If you customized any styles and you are extending the Red Hat build of Keycloak themes, review the changes to the styles. If you are extending the base theme, you can skip this step.
3.4.1. Migrating templates
If you customized any template, compare it to the new version of that template. This comparison shows you what changes you need to apply to your customized template. You can use a diff tool to compare the templates. The following screenshot compares the info.ftl
template from the Login theme and an example custom theme:
Updated version of a Login theme template versus a custom Login theme template
This comparison shows that the first change (Hello world!!
) is a customization, while the second change (if pageRedirectUri
) is a change to the base theme. By copying the second change to your custom template, you have successfully updated your customized template.
In an alternative approach, the following screenshot compares the info.ftl
template from the old installation with the updated info.ftl
template from the new installation:
Login theme template from the old installation versus the updated Login theme template
This comparison shows what has been changed in the base template. You can then manually make the same changes to your modified template. Since this approach is more complex, use this approach only if the first approach is not feasible.
3.4.2. Migrating messages
If you added support for another language, you need to apply all the changes listed above. If you have not added support for another language, you might not need to change anything. You need to make changes only if you have changed an affected message in your theme.
Procedure
- For added values, review the value of the message in the base theme to determine if you need to customize that message.
- For renamed keys, rename the key in your custom theme.
- For changed values, check the value in the base theme to determine if you need to make changes to your custom theme.
3.4.3. Migrating styles
You might need to update your custom styles to reflect changes made to the styles from the built-in themes. Consider using a diff tool to compare the changes to stylesheets between the old server installation and the new server installation.
For example:
$ diff RHSSO_HOME_OLD/themes/keycloak/login/resources/css/login.css \
RHSSO_HOME_NEW/themes/keycloak/login/resources/css/login.css
Review the changes and determine if they affect your custom styling.
