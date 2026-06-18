---
title: "Chapter 6. Relational Database Setup - Red Hat Single Sign-On 7.1 Server Installation and Configuration Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-database
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/server_installation_and_configuration_guide/database
guide: server_installation_and_configuration_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
abstract: "Red Hat Single Sign-On comes with its own embedded Java-based relational database called H2. This is the default database that Red Hat Single Sign-On will use to persist data and really only exists so that you can run the authentication server out of the box. We highly recommend that you replace it with a more production ready external database. The H2 database is not very viable in high concurren…"
---

# Chapter 6. Relational Database Setup - Red Hat Single Sign-On 7.1 Server Installation and Configuration Guide

Chapter 6. Relational Database Setup
Red Hat Single Sign-On comes with its own embedded Java-based relational database called H2. This is the default database that Red Hat Single Sign-On will use to persist data and really only exists so that you can run the authentication server out of the box. We highly recommend that you replace it with a more production ready external database. The H2 database is not very viable in high concurrency situations and should not be used in a cluster either. The purpose of this chapter is to show you how to connect Red Hat Single Sign-On to a more mature database.
Red Hat Single Sign-On uses two layered technologies to persist its relational data. The bottom layered technology is JDBC. JDBC is a Java API that is used to connect to a RDBMS. There are different JDBC drivers per database type that are provided by your database vendor. This chapter discusses how to configure Red Hat Single Sign-On to use one of these vendor-specific drivers.
The top layered technology for persistence is Hibernate JPA. This is a object to relational mapping API that maps Java Objects to relational data. Most deployments of Red Hat Single Sign-On will never have to touch the configuration aspects of Hibernate, but we will discuss how that is done if you run into that rare circumstance.
Datasource configuration is covered much more thoroughly in the datasource configuration chapter in the JBoss EAP Configuration Guide.
6.1. RDBMS Setup Checklist
These are the steps you will need to perform to get an RDBMS configured for Red Hat Single Sign-On.
- Locate and download a JDBC driver for your database
- Package the driver JAR into a module and install this module into the server
- Declare the JDBC driver in the configuration profile of the server
- Modify the datasource configuration to use your database’s JDBC driver
- Modify the datasource configuration to define the connection parameters to your database
This chapter will use PostgresSQL for all its examples. Other databases follow the same steps for installation.
6.2. Package the JDBC Driver
Find and download the JDBC driver JAR for your RDBMS. Before you can use this driver, you must package it up into a module and install it into the server. Modules define JARs that are loaded into the Red Hat Single Sign-On classpath and the dependencies those JARs have on other modules. They are pretty simple to set up.
Within the …/modules/ directory of your Red Hat Single Sign-On distribution, you need to create a directory structure to hold your module definition. The convention is use the Java package name of the JDBC driver for the name of the directory structure. For PostgreSQL, create the directory org/postgresql/main. Copy your database driver JAR into this directory and create an empty module.xml file within it too.
Module Directory
After you have done this, open up the module.xml file and create the following XML:
Module XML
<?xml version="1.0" ?>
<module xmlns="urn:jboss:module:1.3" name="org.postgresql">
<resources>
<resource-root path="postgresql-9.4.1212.jar"/>
</resources>
<dependencies>
<module name="javax.api"/>
<module name="javax.transaction.api"/>
</dependencies>
</module>
The module name should match the directory structure of your module. So, org/postgresql maps to org.postgresql
. The resource-root path
attribute should specify the JAR filename of the driver. The rest are just the normal dependencies that any JDBC driver JAR would have.
6.3. Declare and Load JDBC Driver
The next thing you have to do is declare your newly packaged JDBC driver into your deployment profile so that it loads and becomes available when the server boots up. Where you perform this action depends on your operating mode. If you’re deploying in standard mode, edit …/standalone/configuration/standalone.xml. If you’re deploying in standard clustering mode, edit …/standalone/configuration/standalone-ha.xml. If you’re deploying in domain mode, edit …/domain/configuration/domain.xml. In domain mode, you’ll need to make sure you edit the profile you are using: either auth-server-standalone
or auth-server-clustered
Within the profile, search for the drivers
XML block within the datasources
subsystem. You should see a pre-defined driver declared for the H2 JDBC driver. This is where you’ll declare the JDBC driver for your external database.
JDBC Drivers
<subsystem xmlns="urn:jboss:domain:datasources:4.0">
<datasources>
...
<drivers>
<driver name="h2" module="com.h2database.h2">
<xa-datasource-class>org.h2.jdbcx.JdbcDataSource</xa-datasource-class>
</driver>
</drivers>
</datasources>
</subsystem>
Within the drivers
XML block you’ll need to declare an additional JDBC driver. It needs to have a name
which you can choose to be anything you want. You specify the module
attribute which points to the module
package you created earlier for the driver JAR. Finally you have to specify the driver’s Java class. Here’s an example of installing PostgreSQL driver that lives in the module example defined earlier in this chapter.
Declare Your JDBC Drivers
<subsystem xmlns="urn:jboss:domain:datasources:4.0">
<datasources>
...
<drivers>
<driver name="postgresql" module="org.postgresql">
<xa-datasource-class>org.postgresql.xa.PGXADataSource</xa-datasource-class>
</driver>
<driver name="h2" module="com.h2database.h2">
<xa-datasource-class>org.h2.jdbcx.JdbcDataSource</xa-datasource-class>
</driver>
</drivers>
</datasources>
</subsystem>
6.4. Modify the Red Hat Single Sign-On Datasource
After declaring your JDBC driver, you have to modify the existing datasource configuration that Red Hat Single Sign-On uses to connect it to your new external database. You’ll do this within the same configuration file and XML block that you registered your JDBC driver in. Here’s an example that sets up the connection to your new database:
Declare Your JDBC Drivers
<subsystem xmlns="urn:jboss:domain:datasources:4.0">
<datasources>
...
<datasource jndi-name="java:jboss/datasources/KeycloakDS" pool-name="KeycloakDS" enabled="true" use-java-context="true">
<connection-url>jdbc:postgresql://localhost/keycloak</connection-url>
<driver>postgresql</driver>
<pool>
<max-pool-size>20</max-pool-size>
</pool>
<security>
<user-name>William</user-name>
<password>password</password>
</security>
</datasource>
...
</datasources>
</subsystem>
Search for the datasource
definition for KeycloakDS
. You’ll first need to modify the connection-url
. The documentation for your vendor’s JDBC implementation should specify the format for this connection URL value.
Next define the driver
you will use. This is the logical name of the JDBC driver you declared in the previous section of this chapter.
It is expensive to open a new connection to a database every time you want to perform a transaction. To compensate, the datasource implementation maintains a pool of open connections. The max-pool-size
specifies the maximum number of connections it will pool. You may want to change the value of this depending on the load of your system.
Finally, with PostgreSQL at least, you need to define the database username and password that is needed to connect to the database. You may be worried that this is in clear text in the example. There are methods to obfuscate this, but this is beyond the scope of this guide.
For more information about datasource features, see the datasource configuration chapter in the JBoss EAP Configuration Guide.
6.5. Database Configuration
The configuration for this component is found in the standalone.xml
, standalone-ha.xml
, or domain.xml
file in your distribution. The location of this file depends on your operating mode.
Database Config
<subsystem xmlns="urn:jboss:domain:keycloak-server:1.1">
...
<spi name="connectionsJpa">
<provider name="default" enabled="true">
<properties>
<property name="dataSource" value="java:jboss/datasources/KeycloakDS"/>
<property name="initializeEmpty" value="false"/>
<property name="migrationStrategy" value="manual"/>
<property name="migrationExport" value="${jboss.home.dir}/keycloak-database-update.sql"/>
</properties>
</provider>
</spi>
...
</subsystem>
Possible configuration options are:
- dataSource
- JNDI name of the dataSource
- jta
- boolean property to specify if datasource is JTA capable
- driverDialect
- Value of database dialect. In most cases you don’t need to specify this property as dialect will be autodetected by Hibernate.
- initializeEmpty
-
Initialize database if empty. If set to false the database has to be manually initialized. If you want to manually initialize the database set migrationStrategy to
manual
which will create a file with SQL commands to initialize the database. Defaults to true. - migrationStrategy
-
Strategy to use to migrate database. Valid values are
update
,manual
andvalidate
. Update will automatically migrate the database schema. Manual will export the required changes to a file with SQL commands that you can manually execute on the database. Validate will simply check if the database is up-to-date. - migrationExport
- Path for where to write manual database initialization/migration file.
- showSql
- Specify whether Hibernate should show all SQL commands in the console (false by default). This is very verbose!
- formatSql
- Specify whether Hibernate should format SQL commands (true by default)
- globalStatsInterval
- Will log global statistics from Hibernate about executed DB queries and other things. Statistics are always reported to server log at specified interval (in seconds) and are cleared after each report.
- schema
- Specify the database schema to use
These configuration switches and more are described in the JBoss EAP Development Guide.
6.6. Unicode Considerations for Databases
Database schema in Red Hat Single Sign-On only accounts for Unicode strings in the following special fields:
- Realms: display name, HTML display name
- Federation Providers: display name
- Users: username, given name, last name, attribute names and values
- Groups: name, attribute names and values
- Roles: name
- Descriptions of objects
Otherwise, characters are limited to those contained in database encoding which is often 8-bit. However, for some database systems, it is possible to enable UTF-8 encoding of Unicode characters and use full Unicode character set in all text fields. Often, this is counterbalanced by shorter maximum length of the strings than in case of 8-bit encodings.
Some of the databases require special settings to database and/or JDBC driver to be able to handle Unicode characters. Please find the settings for your database below. Note that if a database is listed here, it can still work properly provided it handles UTF-8 encoding properly both on the level of database and JDBC driver.
Technically, the key criterion for Unicode support for all fields is whether the database allows setting of Unicode character set for VARCHAR
and CHAR
fields. If yes, there is a high chance that Unicode will be plausible, usually at the expense of field length. If it only supports Unicode in NVARCHAR
and NCHAR
fields, Unicode support for all text fields is unlikely as Keycloak schema uses VARCHAR
and CHAR
fields extensively.
6.6.1. Oracle Database
Unicode characters are properly handled provided the database was created with Unicode support in VARCHAR
and CHAR
fields (e.g. by using AL32UTF8
character set as the database character set). No special settings is needed for JDBC driver.
If the database character set is not Unicode, then to use Unicode characters in the special fields, the JDBC driver needs to be configured with the connection property oracle.jdbc.defaultNChar
set to true
. It might be wise, though not strictly necessary, to also set the oracle.jdbc.convertNcharLiterals
connection property to true
. These properties can be set either as system properties or as connection properties. Please note that setting oracle.jdbc.defaultNChar
may have negative impact on performance. For details, please refer to Oracle JDBC driver configuration documentation.
6.6.2. Microsoft SQL Server Database
Unicode characters are properly handled only for the special fields. No special settings of JDBC driver or database is necessary.
6.6.3. IBM DB2 Database
Unicode characters are properly handled for all fields, length reduction applies to non-special fields. No special settings of JDBC driver or database is necessary.
6.6.4. MySQL Database
Unicode characters are properly handled provided the database was created with Unicode support in VARCHAR
and CHAR
fields in the CREATE DATABASE
command (e.g. by using utf8
character set as the default database character set in MySQL 5.5. Please note that utf8mb4
character set does not work due to different storage requirements to utf8
character set [1]). Note that in this case, length restriction to non-special fields does not apply because columns are created to accomodate given amount of characters, not bytes. If the database default character set does not allow storing Unicode, only the special fields allow storing Unicode values.
At the side of JDBC driver settings, it is necessary to add a connection property characterEncoding=UTF-8
to the JDBC connection settings.
6.6.5. PostgreSQL Database
Unicode is supported when the database character set is UTF8
. In that case, Unicode characters can be used in any field, there is no reduction of field length for non-special fields. No special settings of JDBC driver is necessary.
