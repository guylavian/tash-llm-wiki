---
title: "Chapter 2. Migrating a Red Hat Single Sign-On 7.6 server - Red Hat build of Keycloak 26.6 Migration Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-migrating-server
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/migration_guide/migrating-server
guide: migration_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
---

# Chapter 2. Migrating a Red Hat Single Sign-On 7.6 server - Red Hat build of Keycloak 26.6 Migration Guide

Chapter 2. Migrating a Red Hat Single Sign-On 7.6 server
Migrating a standalone server involves the use of a ZIP distribution of the software. Red Hat build of Keycloak 26.6 is built with Quarkus, which replaces the Red Hat JBoss Enterprise Application Platform (JBoss EAP) that was used by Red Hat Single Sign-On 7.6.
The main changes to the server are the following:
- A revamped configuration experience, which is streamlined and supports great flexibility in setting configuration options.
- An RPM distribution of the server is no longer available
2.1. Prerequisites
- The previous instance of Red Hat Single Sign-On 7.6 was shut down so that it does not use the same database instance that will be used by Red Hat build of Keycloak .
- You backed up the database.
- OpenJDK 21 is installed.
- You reviewed the Release Notes.
You also reviewed release notes from earlier versions for additional changes:
2.2. Migration process overview
The migration involves the following high-level steps:
- Download Red Hat build of Keycloak .
- Migrate the configuration.
- Migrate the database.
- Start the Red Hat build of Keycloak server.
2.3. Downloading Red Hat build of Keycloak
The Red Hat build of Keycloak server download ZIP file contains the scripts and binaries to run the Red Hat build of Keycloak server.
Procedure
- Download the Red Hat build of Keycloak server distribution file from the Red Hat customer portal.
- Unpack the ZIP file using the unzip command.
2.4. Migrating the configuration
A new unified way to configure the Red Hat build of Keycloak server is through configuration options. The Red Hat Single Sign-On 7.6 configuration mechanism, such as standalone.xml, jboss-cli, and so on, no longer applies.
Each option can be defined through the following configuration sources:
- CLI parameters
- Environment variables
- Configuration file
- Java KeyStore file
If the same configuration option is specified through different configuration sources, the first source in the list above is used.
All configuration options are available in all the different configuration sources, where the main difference is the format of the key. For example, here are four ways to configure the database hostname:
| Source | Format |
|---|---|
| CLI parameters | --db-url-host cliValue |
| Environment variables | KC_DB_URL_HOST=envVarValue |
| Configuration file | db-url-host=confFileValue |
| Java KeyStore file | kc.db-url-host=keystoreValue |
The kc.sh --help
command as well as the Red Hat build of Keycloak documentation provides a complete list of all available configuration options, where options are grouped by categories such as cache, database, and so on. Also, separate chapters exist for each area to configure, such as the chapter for Configuring Keycloak.
2.4.1. Migrating the database configuration
In contrast to Red Hat Single Sign-On 7.6, Red Hat build of Keycloak has built-in support for the supported databases removing the need to manually install and configure the database drivers. The exception is Oracle and Microsoft SQL Server, which still require manual installation of the drivers.
In terms of configuration, consider the datasource subsystem from your existing Red Hat Single Sign-On 7.6 installation and map those configurations to the options available from the Database configuration category in Red Hat build of Keycloak . For example, a previous configuration appears as follows:
<datasource jndi-name="java:jboss/datasources/KeycloakDS" pool-name="KeycloakDS" enabled="true" use-java-context="true" statistics-enabled="true">
<connection-url>jdbc:postgresql://mypostgres:5432/mydb?currentSchema=myschema</connection-url>
<driver>postgresql</driver>
<pool>
<min-pool-size>5</min-pool-size>
<max-pool-size>50</max-pool-size>
</pool>
<security>
<user-name>myuser</user-name>
<password>myuser</password>
</security>
</datasource>
In Red Hat build of Keycloak , the equivalent configuration using CLI parameters would be:
kc.sh start
--db postgres
--db-url-host mypostgres
--db-url-port 5432
--db-url-database mydb
--db-schema myschema
--db-pool-min-size 5 --db-pool-max-size 50
--db-username myser --db-password myuser
Consider storing database credentials in a secure KeyStore configuration source.
2.4.2. Migrating additional datasources configuration
With Red Hat build of Keycloak, you can specify additional datasources in case you need to access another database from your extensions. This option is useful if the main Red Hat build of Keycloak datasource is not viable for storing custom data, such as users.
For more details on how to connect to your own users database, see the User Storage SPI. Defining multiple datasources is similar to defining a single datasource with a key difference. You specify a name for each datasource as part of the config option name.
To use additional datasources, you first set up the JPA Persistence layer by using the persistence.xml
file and the datasource configuration. The datasource configuration is essential, because you set up the JDBC connection, configuring JPA/Hibernate properties, managed entities, and so on.
For the persistence.xml
file, no major changes exist. The form is almost the same as in Red Hat Single Sign-On 7.6. However, in the Red Hat build of Keycloak, some properties are set automatically based on the CLI configuration.
The following is the previous configuration of the persistence.xml
file:
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.0"
xmlns="http://java.sun.com/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="
http://java.sun.com/xml/ns/persistence
http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
<persistence-unit name="user-storage-jpa-example">
<jta-data-source>java:jboss/datasources/UsersXADS</jta-data-source>
<class>org.keycloak.quickstart.storage.user.UserEntity</class>
<properties>
<property name="hibernate.hbm2ddl.auto" value="update" />
<property name="hibernate.show_sql" value="false" />
</properties>
</persistence-unit>
</persistence>
In Red Hat build of Keycloak, the equivalent persistence.xml
file would be:
<?xml version="1.0" encoding="UTF-8"?>
<persistence xmlns="https://jakarta.ee/xml/ns/persistence"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="https://jakarta.ee/xml/ns/persistence https://jakarta.ee/xml/ns/persistence/persistence_3_0.xsd"
version="3.0">
<persistence-unit name="user-storage-jpa-example" transaction-type="JTA">
<class>org.keycloak.quickstart.storage.user.UserEntity</class>
<properties>
<property name="jakarta.persistence.jtaDataSource" value="user-store" />
<property name="hibernate.hbm2ddl.auto" value="update" />
<property name="hibernate.show_sql" value="false" />
</properties>
</persistence-unit>
</persistence>
For example, a previous configuration of additional datasources inside the datasource subsystem might have appeared as follows:
<xa-datasource jndi-name="java:jboss/datasources/UsersXADS" pool-name="UsersXADS" enabled="true">
<connection-url>jdbc:postgresql://mypostgres:5444/users</connection-url>
<driver>postgresql</driver>
<security>
<user-name>myuser</user-name>
<password>myuser</password>
</security>
</xa-datasource>
In the Red Hat build of Keycloak, the equivalent configuration using CLI parameters would be:
kc.sh start
--db-kind-user-store postgres
--db-url-full-user-store jdbc:postgresql://mypostgres:5444/users
--db-username-user-store myuser
--db-password-user-store myuser
2.4.3. Migrating HTTP and TLS configuration
HTTP is disabled and TLS configuration is required by default, whenever the production mode (represented by the start
option) is used.
You can enable HTTP with the --http-enabled=true
configuration option, but it is not recommended unless the Red Hat build of Keycloak server is within a fully isolated network, and no risk exists of internal or external attackers being able to observe networking traffic.
A Red Hat build of Keycloak instance has a different context root (URL path) as it uses the root of the server while Red Hat Single Sign-On 7.6 by default appends /auth
. To mimic the old behavior, the --http-relative-path=/auth
configuration option can be used. The default ports remain the same, but they can also be changed by the --http-port
and --https-port
options.
Two ways exist to configure TLS, either through files in the PEM format or with a Java Keystore. For example, a previous configuration by Java Keystore appears as follows:
<tls>
<key-stores>
<key-store name="applicationKS">
<credential-reference
clear-text="password"/>
<implementation type="JKS"/>
<file
path="/path/to/application.keystore”/>
</key-store>
</key-stores>
<key-managers>
<key-manager name="applicationKM"
key-store="applicationKS">
<credential-reference
clear-text="password"/>
</key-manager>
</key-managers>
<server-ssl-contexts>
<server-ssl-context name="applicationSSC"
key-manager="applicationKM"/>
</server-ssl-contexts>
</tls>
In Red Hat build of Keycloak , the equivalent configuration using CLI parameters would be as follows:
kc.sh start
--https-key-store-file /path/to/application.keystore
--https-key-store-password password
In Red Hat build of Keycloak , you can configure TLS by providing certificates in PEM format as follows:
kc.sh start
--https-certificate-file /path/to/certfile.pem
--https-certificate-key-file /path/to/keyfile.pem
2.4.4. Migrating clustering and cache configuration
Red Hat Single Sign-On 7.6 provided distinct operating modes for running the server as standalone, standalone clustered, and domain clustered. These modes differed in the start script and configuration files. Red Hat build of Keycloak offers a simplified solution with a single start script: kc.sh
.
To run the server as standalone or standalone clustered, use the kc.sh
script:
| Red Hat build of Keycloak | Red Hat Single Sign-On 7.6 |
|---|---|
|
|
|
|
|
|
The default values for the --cache
parameter is start mode aware:
-
local
- when the start-dev command is executed -
ispn
- when the start command is executed
In Red Hat Single Sign-On 7.6, clustering and cache configuration was done through the Infinispan subsystem, while in Red Hat build of Keycloak the majority of the configuration is done through a separate Infinispan configuration file. For example, a previous configuration of Infinispan appears as follows:
<subsystem xmlns="urn:jboss:domain:infinispan:13.0">
<cache-container name="keycloak" marshaller="JBOSS" modules="org.keycloak.keycloak-model-infinispan">
<local-cache name="realms">
<heap-memory size="10000"/>
</local-cache>
<local-cache name="users">
<heap-memory size="10000"/>
</local-cache>
<local-cache name="sessions"/>
<local-cache name="authenticationSessions"/>
<local-cache name="offlineSessions"/>
...
</cache-container>
</subsystem>
The most relevant configuration options are available as configuration options. For example, use the option cache-embedded-realms-max-count
to configure the maximum number of entries in the realms cache.
Domain clustered mode is not supported with Red Hat build of Keycloak.
2.4.4.1. Transport stacks
The default transport stack is now jdbc-ping
which leverages the database to discover other nodes, uses TCP as a transport, and automatically encrypts it via TLS. It works well in cloud and non-cloud environments.
All other transport stacks are deprecated. You should migrate your cache configuration to jdbc-ping
.
We recommend to set the cache-embedded-network-bind-address
parameter to ensure that Red Hat build of Keycloak binds to the correct interface. In environments without transparent networking, set the parameters cache-embedded-network-external-port
and cache-embedded-network-external-address
to specify how a Red Hat build of Keycloak node can be reached from other nodes.
2.4.5. Migrating hostname and proxy configuration
In Red Hat build of Keycloak, you are now obligated to configure the Hostname SPI in order to set how front and back end URLs are going to be created by the server when redirecting users or communicating with their clients.
For example, consider if you have a configuration similar as the follows in your Red Hat Single Sign-On 7.6 installation:
<spi name="hostname">
<default-provider>default</default-provider>
<provider name="default" enabled="true">
<properties>
<property name="frontendUrl" value="myFrontendUrl"/>
<property name="forceBackendUrlToFrontendUrl" value="true"/>
</properties>
</provider>
</spi>
You can translate it to the following configuration options in Red Hat build of Keycloak:
kc.sh start
--hostname myFrontendUrl
The hostname
configuration option allows you to set the base URL where the cluster is exposed to the public from an ingress layer running in front of your cluster. You can also set the URL for administration resources by setting the hostname-admin
configuration option.
Red Hat build of Keycloak allows you to configure which reverse proxy headers should be reflected. You can use either the Forwarded
header or the set of X-Forwarded-*
headers. For example:
kc.sh start --proxy-headers xforwarded
The hostname and proxy configuration are used for determining the resource URLs (redirect URIs, CSS and JavaScript links, OIDC well-known endpoints, and so on) and not for actively blocking incoming requests. None of the hostname/proxy options change the actual binding addresses or ports that the Red Hat build of Keycloak server listens on - this is a responsibility of the HTTP/TLS options. In Red Hat Single Sign-On 7.6, setting a hostname was highly recommended, but not enforced. In Red Hat build of Keycloak , when the start command is used this is now required, unless explicitly disabled with the --hostname-strict=false
option.
2.4.6. Migrating truststore configuration
The truststore is used for external TLS communication, for example HTTPS requests and LDAP servers. To use a truststore, you import the remote server’s or CA’s certificate into the trustore. Then, you can start the Red Hat build of Keycloak server specifying the system truststore.
For example, a previous configuration appears as follows:
<spi name="truststore">
<provider name="file" enabled="true">
<properties>
<property name="file" value="path/to/myTrustStore.jks"/>
<property name="password" value="password"/>
<property name="hostname-verification-policy" value="WILDCARD"/>
</properties>
</provider>
</spi>
Red Hat build of Keycloak supports truststores in the following formats: PEM files, or PKCS12 files with the extensions .p12 and .pfx. For the PKCS12 files, the certs must be unencrypted, which means that no password is expected. The JKS truststores need to be converted. Since the Java keytool
enforces a minimum password length of 6 characters, openssl
can be used as an alternative to create an unencrypted PKCS12 truststore.
Procedure
Create a PKCS12 truststore with a temporary password using keytool by importing the contents of an old JKS truststore.
keytool -importkeystore -srckeystore path/to/myTrustStore.jks \ -destkeystore path/to/myTrustStore.p12 \ -srcstoretype jks \ -deststoretype pkcs12 \ -srcstorepass password \ -deststorepass temp-password
Export the contents of the new PKCS12 truststore using
openssl
.openssl pkcs12 -in path/to/myTrustStore.p12 \ -out path/to/myTrustStore.pem \ -nodes -passin pass:temp-password
Reimport the contents into a new unencrypted PKCS12 truststore using
openssl
.openssl pkcs12 -export -in path/to/myTrustStore.pem \ -out path/to/myUnencryptedTrustStore.p12 \ -nokeys -passout pass:
In this example, the resulting CLI parameter would be as follows:
kc.sh start --truststore-paths path/to/myUnencryptedTrustStore.p12 --tls-hostname-verifier WILDCARD
2.4.7. Migrating vault configuration
The Keystore Vault is an implementation of the Vault SPI and it is useful for storing secrets in bare metal installations. This vault is a replacement of the Elytron Credential Store in Red Hat Single Sign-On 7.6.
<spi name="vault">
<provider name="elytron-cs-keystore" enabled="true">
<properties>
<property name="location" value="path/to/keystore.p12"/>
<property name="secret" value="password"/>
</properties>
</provider>
</spi>
In Red Hat build of Keycloak, the equivalent configuration using CLI parameters would be:
kc.sh start
--vault keystore
--vault-file /path/to/keystore.p12
--vault-pass password
Secrets stored in the vault can be then accessed at multiple places within the Admin Console. When it comes to the migration from the existing Elytron vault to the new Java KeyStore-based vault, no realm configuration changes are required. If a newly created Java keystore contains the same secrets, your existing realm configuration should work.
Given that you use the default REALM_UNDERSCORE_KEY
key resolver, the secret can be accessed by ${vault.realm-name_alias}
(for example, in your LDAP User federation configuration) the same way as before.
2.4.8. Migrating JVM settings
The approach for JVM settings in Red Hat build of Keycloak is similar to the Red Hat Single Sign-On 7.6 approach. You still need to set particular environment variables, however, the /bin
folder contains no configuration files, such as standalone.conf
.
Red Hat build of Keycloak provides various default JVM arguments, which proved to be suitable for the majority of deployments as it provides good throughput and efficiency in memory allocation and CPU overhead. Also, other default JVM arguments ensure a smooth run of the Red Hat build of Keycloak instance, so use caution when you change the arguments for your use case.
To change JVM arguments or GC settings, you set particular environment variables, which are specified as Java options. For a complete override of these settings, you specify the JAVA_OPTS
environment variable.
When only an append of a particular Java property is required, you specify the JAVA_OPTS_APPEND
environment variable. When no JAVA_OPTS
environment variable is specified, the default Java properties are used and can be found inside the ./kc.sh
script.
For instance, you can specify a particular Java option as follows:
export JAVA_OPTS_APPEND=-XX:+HeapDumpOnOutOfMemoryError
kc.sh start
2.4.9. Migrating SPI provider configuration
Configuration for SPI providers is available through the new configuration system. This is the old format:
<spi name="<spi-id>">
<provider name="<provider-id>" enabled="true">
<properties>
<property name="<property>" value="<value>"/>
</properties>
</provider>
</spi>
This is the new format:
spi-<spi-id>--<provider-id>--<property>=<value>
| Source | Format |
|---|---|
| CLI | ./kc.sh start --spi-connections-http-client—default—connection-pool-size 10 |
| Environment Variable | KC_SPI_CONNECTIONS_HTTP_CLIENTDEFAULTCONNECTION_POOL_SIZE=10 |
| Configuration file | spi-connections-http-client—default—connection-pool-size=10 |
| Java Keystore file | kc.spi-connections-http-client—default—connection-pool-size=10 |
2.4.10. Troubleshooting the configuration
Use these commands for troubleshooting:
-
kc.sh show-config
- shows you the configuration sources from which particular properties are loaded and what their values are. You can check whether a property and its value is propagated correctly. -
kc.sh --verbose start
- prints out the whole error stack trace, when there is an error.
2.5. Migrating the database
Red Hat build of Keycloak can automatically migrate the database schema, or you can choose to do it manually. By default the database is automatically migrated when you start the new installation for the first time.
2.5.1. Automatic relational database migration
To perform an automatic migration, start the server connected to the desired database. If the database schema has changed for the new version of the server, it will be migrated.
2.5.2. Manual relational database migration
To enable manual upgrading of the database schema, set the migration-strategy
property value to manual for the default connections-jpa provider:
kc.sh start --spi-connections-jpa-quarkus-migration-strategy=manual
When you start the server with this configuration, it checks if the database needs to be migrated. The required changes are written to the bin/keycloak-database-update.sql
SQL file that you can review and manually run against the database.
To change the path and name of the exported SQL file, set the migration-export
property for the default connections-jpa
provider:
kc.sh start
--spi-connections-jpa-quarkus-migration-export=<path>/<file.sql>
For further details on how to apply this file to the database, see the documentation for your relational database. After the changes have been written to the file, the server exits.
2.6. Starting the Red Hat build of Keycloak Server
The difference in starting the distribution of Red Hat Single Sign-On 7.6 and Red Hat build of Keycloak is in the executed script. These scripts live in the /bin
folder of the server distribution.
2.6.1. Starting the server in development mode
To try out Red Hat build of Keycloak without worrying about supplying any properties, you can start the distribution in the development mode as described in the table below. However, note that this mode is strictly for development and should not be used in production.
| Red Hat build of Keycloak | Red Hat Single Sign-On 7.6 |
|---|---|
| ./kc.sh start-dev | ./standalone.sh |
The development mode should NOT be used in production.
2.6.2. Starting the server in production mode
Red Hat build of Keycloak has a dedicated start mode for production: ./kc.sh start
. The difference from running with start-dev
is different default configuration values. It automatically uses a strict and by-default secured configuration setup. In the production mode, HTTP is disabled, and explicit TLS and hostname configuration is required.
