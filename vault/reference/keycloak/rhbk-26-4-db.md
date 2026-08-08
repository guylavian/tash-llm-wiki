---
title: "Chapter 9. Configuring the database - Red Hat build of Keycloak 26.4 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-db
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/db-
guide: server_configuration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Configure a relational database for Red Hat build of Keycloak to store user, client, and realm data. This chapter explains how to configure the Red Hat build of Keycloak server to store data in a relational database. 9.1. Supported databases The server has built-in support for different databases. You can query the available databases by viewing the expected values for the db configuration option.…"
---

# Chapter 9. Configuring the database - Red Hat build of Keycloak 26.4 Server Configuration Guide

Chapter 9. Configuring the database
Configure a relational database for Red Hat build of Keycloak to store user, client, and realm data.
This chapter explains how to configure the Red Hat build of Keycloak server to store data in a relational database.
9.1. Supported databases
The server has built-in support for different databases. You can query the available databases by viewing the expected values for the db
configuration option. The following table lists the supported databases and their tested versions.
| Database | Option value | Tested Version | Supported Versions |
|---|---|---|---|
| MariaDB Server |
| 11.8 | 11.8 (LTS), 11.4 (LTS), 10.11 (LTS), 10.6 (LTS) |
| Microsoft SQL Server |
| 2022 | 2022, 2019 |
| MySQL |
| 8.4 | 8.4 (LTS), 8.0 (LTS) |
| Oracle Database |
| 23.5 | 23.x (i.e 23.5+), 19c (19.3+) (Note: Oracle RAC is also supported if using the same database engine version, e.g 23.5+, 19.3+) |
| PostgreSQL |
| 17 | 17.x, 16.x, 15.x, 14.x |
| EnterpriseDB Advanced |
| 17 | 17 |
| Amazon Aurora PostgreSQL |
| 17.5 | 17.x, 16.x, 15.x |
| Azure SQL Database |
| latest | latest |
| Azure SQL Managed Instance |
| latest | latest |
It is not a supported configuration if the underlying database specific Hibernate dialect allows the use of a version that differs from those shown.
By default, the server uses the dev-file
database. This is the default database that the server will use to persist data and only exists for development use-cases. The dev-file
database is not suitable for production use-cases, and must be replaced before deploying to production.
9.2. Installing a database driver
Database drivers are shipped as part of Red Hat build of Keycloak except for the Oracle Database and Microsoft SQL Server drivers.
Install the necessary missing driver manually if you want to connect to one of these databases or skip this section if you want to connect to a different database for which the database driver is already included.
Overriding the built-in database drivers or supplying your own drivers is considered unsupported. The only supported exceptions are explicitly documented in this guide, such as the Oracle Database driver.
9.2.1. Installing the Oracle Database driver
To install the Oracle Database driver for Red Hat build of Keycloak:
Download the
ojdbc17
andorai18n
JAR files from one of the following sources:- Zipped JDBC driver and Companion Jars version 23.6.0.24.10 from the Oracle driver download page.
-
Maven Central via
ojdbc17
andorai18n
. - Installation media recommended by the database vendor for the specific database in use.
-
When running the unzipped distribution: Place the
ojdbc17
andorai18n
JAR files in Red Hat build of Keycloak’sproviders
folder When running containers: Build a custom Red Hat build of Keycloak image and add the JARs in the
providers
folder. When building a custom image for the Operator, those images need to be optimized images with all build-time options of Red Hat build of Keycloak set.A minimal Containerfile to build an image which can be used with the Red Hat build of Keycloak Operator and includes Oracle Database JDBC drivers downloaded from Maven Central looks like the following:
FROM registry.redhat.io/rhbk/keycloak-rhel9:26.4 ADD --chown=keycloak:keycloak --chmod=644 https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc17/23.6.0.24.10/ojdbc17-23.6.0.24.10.jar /opt/keycloak/providers/ojdbc17.jar ADD --chown=keycloak:keycloak --chmod=644 https://repo1.maven.org/maven2/com/oracle/database/nls/orai18n/23.6.0.24.10/orai18n-23.6.0.24.10.jar /opt/keycloak/providers/orai18n.jar # Setting the build parameter for the database: ENV KC_DB=oracle # Add all other build parameters needed, for example enable health and metrics: ENV KC_HEALTH_ENABLED=true ENV KC_METRICS_ENABLED=true # To be able to use the image with the Red Hat build of Keycloak Operator, it needs to be optimized, which requires Red Hat build of Keycloak's build step: RUN /opt/keycloak/bin/kc.sh build
See the Running Red Hat build of Keycloak in a container chapter for details on how to build optimized images.
Then continue configuring the database as described in the next section.
9.2.2. Installing the Microsoft SQL Server driver
To install the Microsoft SQL Server driver for Red Hat build of Keycloak:
Download the
mssql-jdbc
JAR file from one of the following sources:- Download a version from the Microsoft JDBC Driver for SQL Server page.
-
Maven Central via
mssql-jdbc
. - Installation media recommended by the database vendor for the specific database in use.
-
When running the unzipped distribution: Place the
mssql-jdbc
in Red Hat build of Keycloak’sproviders
folder When running containers: Build a custom Red Hat build of Keycloak image and add the JARs in the
providers
folder. When building a custom image for the Red Hat build of Keycloak Operator, those images need to be optimized images with all build-time options of Red Hat build of Keycloak set.A minimal Containerfile to build an image which can be used with the Red Hat build of Keycloak Operator and includes Microsoft SQL Server JDBC drivers downloaded from Maven Central looks like the following:
FROM registry.redhat.io/rhbk/keycloak-rhel9:26.4 ADD --chown=keycloak:keycloak --chmod=644 https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/13.2.1.jre11/mssql-jdbc-13.2.1.jre11.jar /opt/keycloak/providers/mssql-jdbc.jar # Setting the build parameter for the database: ENV KC_DB=mssql # Add all other build parameters needed, for example enable health and metrics: ENV KC_HEALTH_ENABLED=true ENV KC_METRICS_ENABLED=true # To be able to use the image with the Red Hat build of Keycloak Operator, it needs to be optimized, which requires Red Hat build of Keycloak's build step: RUN /opt/keycloak/bin/kc.sh build
See the Running Red Hat build of Keycloak in a container chapter for details on how to build optimized images.
Then continue configuring the database as described in the next section.
9.3. Configuring a database
For each supported database, the server provides some opinionated defaults to simplify database configuration. You complete the configuration by providing some key settings such as the database host and credentials.
The configuration can be set during a build
command OR a start
command:
Using a
build
command followed by an optimizedstart
command (recommended)First, the minimum settings needed to connect to the database can be specified in
conf/keycloak.conf
:# The database vendor. db=postgres # The username of the database user. db-username=keycloak # The password of the database user. db-password=change_me # Sets the hostname of the default JDBC URL of the chosen vendor db-url-host=keycloak-postgres
Then, the following commands create a new and optimized server image based on the configuration options and start the server.
bin/kc.[sh|bat] build bin/kc.[sh|bat] start --optimized
Using only a
start
command (without--optimized
)bin/kc.[sh|bat] start --db postgres --db-url-host keycloak-postgres --db-username keycloak --db-password change_me
The examples above include the minimum settings needed to connect to the database but it exposes the database password and is not recommended. Use the conf/keycloak.conf
as shown above, environment variables, or keystore for at least the password.
The default schema is keycloak
, but you can change it by using the db-schema
configuration option.
It is also possible to configure the database when Importing and exporting realms or Bootstrapping and recovering an admin account:
bin/kc.[sh|bat] import --help
bin/kc.[sh|bat] export --help
bin/kc.[sh|bat] bootstrap-admin --help
For more information, see Configuring Red Hat build of Keycloak.
9.4. Overriding default connection settings
The server uses JDBC as the underlying technology to communicate with the database. If the default connection settings are insufficient, you can specify a JDBC URL using the db-url
configuration option.
The following is a sample command for a PostgreSQL database.
bin/kc.[sh|bat] start --db postgres --db-url jdbc:postgresql://mypostgres/mydatabase
Be aware that you need to escape characters when invoking commands containing special shell characters such as ;
using the CLI, so you might want to set it in the configuration file instead.
9.5. Configuring Unicode support for the database
Unicode support for all fields depends on whether the database allows VARCHAR and CHAR fields to use the Unicode character set.
- If these fields can be set, Unicode is likely to work, usually at the expense of field length.
- If the database only supports Unicode in the NVARCHAR and NCHAR fields, Unicode support for all text fields is unlikely to work because the server schema uses VARCHAR and CHAR fields extensively.
The database schema provides support for Unicode strings only for the following special fields:
- Realms: display name, HTML display name, localization texts (keys and values)
- Federation Providers: display name
- Users: username, given name, last name, attribute names and values
- Groups: name, attribute names and values
- Roles: name
- Descriptions of objects
Otherwise, characters are limited to those contained in database encoding, which is often 8-bit. However, for some database systems, you can enable UTF-8 encoding of Unicode characters and use the full Unicode character set in all text fields. For a given database, this choice might result in a shorter maximum string length than the maximum string length supported by 8-bit encodings.
9.5.1. Configuring Unicode support for an Oracle database
Unicode characters are supported in an Oracle database if the database was created with Unicode support in the VARCHAR and CHAR fields. For example, you configured AL32UTF8 as the database character set. In this case, the JDBC driver requires no special settings.
If the database was not created with Unicode support, you need to configure the JDBC driver to support Unicode characters in the special fields. You configure two properties. Note that you can configure these properties as system properties or as connection properties.
-
Set
oracle.jdbc.defaultNChar
totrue
. Optionally, set
oracle.jdbc.convertNcharLiterals
totrue
.NoteFor details on these properties and any performance implications, see the Oracle JDBC driver configuration documentation.
9.5.2. Unicode support for a Microsoft SQL Server database
Unicode characters are supported only for the special fields for a Microsoft SQL Server database. The database requires no special settings.
The sendStringParametersAsUnicode
property of JDBC driver should be set to false
to significantly improve performance. Without this parameter, the Microsoft SQL Server might be unable to use indexes.
9.5.3. Configuring Unicode support for a MySQL database
Unicode characters are supported in a MySQL database if the database was created with Unicode support in the VARCHAR and CHAR fields when using the CREATE DATABASE command.
Note that the utf8mb4 character set is not supported due to different storage requirements for the utf8 character set. See MySQL documentation for details. In that situation, the length restriction on non-special fields does not apply because columns are created to accommodate the number of characters, not bytes. If the database default character set does not allow Unicode storage, only the special fields allow storing Unicode values.
- Start MySQL Server.
- Under JDBC driver settings, locate the JDBC connection settings.
-
Add this connection property:
characterEncoding=UTF-8
9.5.4. Configuring Unicode support for a PostgreSQL database
Unicode is supported for a PostgreSQL database when the database character set is UTF8. Unicode characters can be used in any field with no reduction of field length for non-special fields. The JDBC driver requires no special settings. The character set is determined when the PostgreSQL database is created.
Check the default character set for a PostgreSQL cluster by entering the following SQL command.
show server_encoding;
If the default character set is not UTF 8, create the database with the UTF8 as the default character set using a command such as:
create database keycloak with encoding 'UTF8';
9.6. Preparing for PostgreSQL
9.6.1. Writer and reader instances
When running PostgreSQL reader and writer instances, Red Hat build of Keycloak needs to always connect to the writer instance to do its work. When using the original PostgreSQL driver, Red Hat build of Keycloak sets the targetServerType
property of the PostgreSQL JDBC driver to primary
to ensure that it always connects to a writable primary instance and never connects to a secondary reader instance in failover or switchover scenarios.
You can override this behavior by setting your own value for targetServerType
in the DB URL or additional properties.
The targetServerType
is only applied automatically to the primary datasource, as requirements might be different for additional datasources.
9.6.2. Permissions of the database user
Ensure that the database user has SELECT
permissions to the following tables to ensure an efficient upgrade: pg_class
, pg_namespace
.
This is used during upgrades of Red Hat build of Keycloak to determine an estimated number of rows in a table. If Red Hat build of Keycloak does not have permissions to access these tables, it will log a warning and proceed with the less efficient SELECT COUNT(*) ...
operation during the upgrade to determine the number of rows in tables affected by schema changes.
9.7. Preparing for Amazon Aurora PostgreSQL
When using Amazon Aurora PostgreSQL, the Amazon Web Services JDBC Driver offers additional features like transfer of database connections when a writer instance changes in a Multi-AZ setup. This driver is not part of the distribution and needs to be installed before it can be used.
To install this driver, apply the following steps:
-
When running the unzipped distribution: Download the JAR file from the Amazon Web Services JDBC Driver releases page and place it in Red Hat build of Keycloak’s
providers
folder. When running containers: Build a custom Red Hat build of Keycloak image and add the JAR in the
providers
folder.A minimal Containerfile to build an image which can be used with the Red Hat build of Keycloak Operator looks like the following:
FROM registry.redhat.io/rhbk/keycloak-rhel9:26.4 ADD --chmod=0666 https://github.com/awslabs/aws-advanced-jdbc-wrapper/releases/download/2.5.6/aws-advanced-jdbc-wrapper-2.5.6.jar /opt/keycloak/providers/aws-advanced-jdbc-wrapper.jar
See the Running Red Hat build of Keycloak in a container chapter for details on how to build optimized images, and the Using custom Red Hat build of Keycloak images chapter on how to run optimized and non-optimized images with the Red Hat build of Keycloak Operator.
Configure Red Hat build of Keycloak to run with the following parameters:
db-url
-
Insert
aws-wrapper
to the regular PostgreSQL JDBC URL resulting in a URL likejdbc:aws-wrapper:postgresql://...
. db-driver
-
Set to
software.amazon.jdbc.Driver
to use the AWS JDBC wrapper.
When overriding the wrapperPlugins
option of the AWS JDBC Driver, always include the failover
or failover2
plugin to ensure that Red Hat build of Keycloak always connects to the writer instance even in failover or switchover scenarios.
9.8. Preparing for MySQL server
Beginning with MySQL 8.0.30, MySQL supports generated invisible primary keys for any InnoDB table that is created without an explicit primary key (more information here). If this feature is enabled, the database schema initialization and also migrations will fail with the error message Multiple primary key defined (1068)
. You then need to disable it by setting the parameter sql_generate_invisible_primary_key
to OFF
in your MySQL server configuration before installing or upgrading Red Hat build of Keycloak.
9.9. Changing database locking timeout in a cluster configuration
Because cluster nodes can boot concurrently, they take extra time for database actions. For example, a booting server instance may perform some database migration, importing, or first time initializations. A database lock prevents start actions from conflicting with each other when cluster nodes boot up concurrently.
The maximum timeout for this lock is 900 seconds. If a node waits on this lock for more than the timeout, the boot fails. The need to change the default value is unlikely, but you can change it by entering this command:
bin/kc.[sh|bat] start --spi-dblock--jpa--lock-wait-timeout 900
9.10. Using Database Vendors with XA transaction support
Red Hat build of Keycloak uses non-XA transactions and the appropriate database drivers by default.
If you wish to use the XA transaction support offered by your driver, enter the following command:
bin/kc.[sh|bat] build --db=<vendor> --transaction-xa-enabled=true
Red Hat build of Keycloak automatically chooses the appropriate JDBC driver for your vendor.
Certain vendors, such as Azure SQL and MariaDB Galera, do not support or rely on the XA transaction mechanism.
XA recovery defaults to enabled and will use the file system location KEYCLOAK_HOME/data/transaction-logs
to store transaction logs.
Enabling XA transactions in a containerized environment does not fully support XA recovery unless stable storage is available at that path.
9.11. Setting JPA provider configuration option for migrationStrategy
To setup the JPA migrationStrategy (manual/update/validate) you should setup JPA provider as follows:
Setting the migration-strategy
for the quarkus
provider of the connections-jpa
SPI
bin/kc.[sh|bat] start --spi-connections-jpa--quarkus--migration-strategy=manual
If you want to get a SQL file for DB initialization, too, you have to add this additional SPI initializeEmpty (true/false):
Setting the initialize-empty
for the quarkus
provider of the connections-jpa
SPI
bin/kc.[sh|bat] start --spi-connections-jpa--quarkus--initialize-empty=false
In the same way the migrationExport to point to a specific file and location:
Setting the migration-export
for the quarkus
provider of the connections-jpa
SPI
bin/kc.[sh|bat] start --spi-connections-jpa--quarkus--migration-export=<path>/<file.sql>
For more information, check the Migrating the database documentation.
9.12. Configuring the connection pool
9.12.1. MySQL and MariaDB
In order to prevent 'No operations allowed after connection closed' exceptions from being thrown, it is necessary to ensure that Red Hat build of Keycloak’s connection pool has a connection maximum lifetime that is less than the server’s configured wait_timeout
. When using the MySQL and MariaDB database, Red Hat build of Keycloak configures a default max lifetime of 7 hours and 50 minutes, as this is less than the default server value of 8 hours.
If you are explicitly configuring the wait_timeout
in your database, it is necessary to ensure that you configure a db-pool-max-lifetime
value that is less than the wait_timeout
. The recommended best practice, is to define this value to be your wait_timeout
minus a few minutes. Failure to correctly configure the db-pool-max-lifetime
will result in Red Hat build of Keycloak logging a warning on startup.
9.13. Configure multiple datasources
Red Hat build of Keycloak allows you to specify additional datasources in case you need to access another database from your extensions. This is useful when using the main Red Hat build of Keycloak datasource is not a viable option for storing custom data, like users.
You can find more details on how to connect to your own users database in the {developerguide_userstoragespi_name} documentation.
Defining multiple datasources works like defining a single datasource, with one important change - you have to specify a name for each datasource as part of the config option name.
9.13.1. Required configuration
In order to enable an additional datasource, you need to set up 2 things - the JPA persistence.xml
file and Red Hat build of Keycloak configuration. The persistence.xml
file serves to specify persistence units as part of the Jakarta Persistence API standard, and is required for proper configuration propagation to the Hibernate ORM framework. When you complete the part with the persistence.xml
file, you need to set up Red Hat build of Keycloak configuration accordingly.
The additional datasource properties might be specified via the standard config sources like CLI, keycloak.conf
, or environment variables.
The additional datasources can be configured in a similar way as the main datasource. This is achieved by using analogous names for config options, which additionally include the name of the additional datasource. For example, when the main datasource uses the db-username
, the additional one would be db-username-<datasource>
. See the Relevant options chapter for the complete list of them.
9.13.1.1. 1. JPA persistence.xml file
The persistence.xml
provides configuration for Jakarta Persistence API (JPA) such as what entities it should manage, the datasource name, JDBC settings, JPA/Hibernate custom settings, and more. The file needs to be placed in the META-INF/persistence.xml
folder of your custom Red Hat build of Keycloak extension.
Be aware that Quarkus provides the ability to set up the JPA persistence unit via Hibernate ORM properties instead of using the persistence.xml
file. However, the supported way for Red Hat build of Keycloak is using the persistence.xml
file, and if the file is present, the Quarkus properties are ignored.
In Red Hat build of Keycloak, most of the configuration is automatic, and you just need to provide fundamental configuration details - the datasource name and transaction type.
Red Hat build of Keycloak requires setting the transaction type for the additional datasource to JTA
. You can set the transaction type and datasource name as follows for this minimal persistence.xml
file:
<persistence xmlns="https://jakarta.ee/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="https://jakarta.ee/xml/ns/persistence https://jakarta.ee/xml/ns/persistence/persistence_3_0.xsd"
version="3.0">
<persistence-unit name="user-store-pu" transaction-type="JTA">
<class>org.your.extension.UserEntity</class>
<properties>
<property name="jakarta.persistence.jtaDataSource" value="user-store" />
</properties>
</persistence-unit>
</persistence>
To properly set the datasource name, you should set the jakarta.persistence.jtaDataSource
property. If it is not set, the persistence unit name will be used as the datasource name instead (so user-store-pu
in this case). In the example above, the resulting datasource name is user-store
. The datasource name can be the same as the persistence unit name.
In order to use your own JPA entities, you need to provide the <class>
properties that mark JPA entities that will be managed by this persistence unit, directed to a specific datasource. In the example above, the org.your.extension.UserEntity
JPA entity will be managed by the persistence unit user-store-pu
, directed to the user-store
datasource.
9.13.1.2. 2. Required properties
Once you have set up your persistence.xml
, the minimal configuration on the Red Hat build of Keycloak side is the setup of the DB kind/vendor for the specified datasource. You need to specify the build time option db-kind-<name>
, where the <name>
is the name of your datasource and must be the same as specified in the persistence.xml
file.
Therefore, you can enable the additional datasource user-store
as follows (postgres
as an example):
bin/kc.[sh|bat] start --db-kind-user-store=postgres
After specifying the db-kind for the datasource, all database-kind–specific defaults (such as the driver and dialect) are automatically applied, just like for the main datasource.
9.13.2. Configuration via environment variables
If you do not want to configure the datasource via CLI or keycloak.conf
properties, you can use the environment variables.
You can set the DB kind via environment variables (for the user-store
datasource) as follows:
export KC_DB_KIND_USER_STORE=postgres
export KC_DB_USERNAME_USER_STORE=my-username
It maps to the db-kind-user-store
and db-username-user-store
Red Hat build of Keycloak properties due to the default mapping of the _
(underscore) to the -
(dash) for environment variables. However, sometimes, the name of the datasource might contain some special characters like _
, $
or .
In order to have it properly configured via the Red Hat build of Keycloak environment variables, you need to explicitly say what the key for the datasource should look like. You can use a pair of unique Red Hat build of Keycloak environment variables with a special case of the KCKEY_
.
For instance, for a datasource with the name user_store$marketing, you can set environment variables as follows:
export KC_USER_STORE_DB_KIND=mariadb
export KCKEY_USER_STORE_DB_KIND=db-kind-user_store$marketing
You can find more information in the guide Configuring Red Hat build of Keycloak, in subsection Formats for environment variable keys with special characters.
9.13.3. Backward compatibility for the quarkus.properties
In the past, we instructed users to use raw Quarkus properties to configure additional datasources in some places. However, as using Quarkus properties in the conf/quarkus.properties
file is considered unsupported, it is strongly recommended to use the dedicated additional datasources options as described above.
Before you are able to migrate to the dedicated options, you can still specify the datasource settings via the Quarkus properties as follows:
quarkus.datasource.user-store.db-kind=h2
quarkus.datasource.user-store.username=sa
quarkus.datasource.user-store.jdbc.url=jdbc:h2:mem:user-store;DB_CLOSE_DELAY=-1
quarkus.datasource.user-store.jdbc.transactions=xa
Use Quarkus properties without quotation for the datasource name, as properties with the quoted datasource name clash with the new datasource options mapping. Therefore, use quarkus.datasource.user-store.db-kind=h2
, instead of quarkus.datasource."user-store".db-kind=h2
to prevent any issues.
9.14. Relevant options
| Value | |
|---|---|
| 🛠
|
|
|
|
|
| 🛠
| |
|
| (default) |
|
| |
|
| |
|
| |
|
| (default) |
|
| |
|
| |
|
| |
|
| |
|
| |
|
| |
|
| |
|
| |
| 🛠
|
|
9.14.1. Additional datasources options
| Value | |
|---|---|
|
|
|
| 🛠
| |
|
|
|
| 🛠
|
|
|
| (default) |
|
| |
|
| |
|
| (default) |
|
| |
|
| |
|
| |
|
| |
|
| |
|
| |
|
| |
|
| |
| 🛠
|
|
