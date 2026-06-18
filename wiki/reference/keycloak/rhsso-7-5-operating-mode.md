---
title: "Chapter 3. Using operating modes - Red Hat Single Sign-On 7.5 Server Installation and Configuration Guide"
type: reference
domain: keycloak
slug: rhsso-7-5-operating-mode
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.5/html/server_installation_and_configuration_guide/operating-mode
guide: server_installation_and_configuration_guide
version: 7.5
family: rhsso
documentKind: "Documentation"
---

# Chapter 3. Using operating modes - Red Hat Single Sign-On 7.5 Server Installation and Configuration Guide

Chapter 3. Using operating modes
Before deploying Red Hat Single Sign-On in a production environment you need to decide which type of operating mode you are going to use.
- Will you run Red Hat Single Sign-On within a cluster?
- Do you want a centralized way to manage your server configurations?
Your choice of operating mode affects how you configure databases, configure caching and even how you boot the server.
The Red Hat Single Sign-On is built on top of the JBoss EAP Application Server. This guide will only go over the basics for deployment within a specific mode. If you want specific information on this, a better place to go would be the JBoss EAP Configuration Guide.
3.1. Using standalone mode
Standalone operating mode is only useful when you want to run one, and only one Red Hat Single Sign-On server instance. It is not usable for clustered deployments and all caches are non-distributed and local-only. It is not recommended that you use standalone mode in production as you will have a single point of failure. If your standalone mode server goes down, users will not be able to log in. This mode is really only useful to test drive and play with the features of Red Hat Single Sign-On
3.1.1. Booting in standalone mode
When running the server in standalone mode, there is a specific script you need to boot the server depending on your operating system. These scripts live in the bin/ directory of the server distribution.
Standalone Boot Scripts
To boot the server:
Linux/Unix
$ .../bin/standalone.sh
Windows
> ...\bin\standalone.bat
3.1.2. Standalone configuration
The bulk of this guide walks you through how to configure infrastructure level aspects of Red Hat Single Sign-On. These aspects are configured in a configuration file that is specific to the application server that Red Hat Single Sign-On is a derivative of. In the standalone operation mode, this file lives in …/standalone/configuration/standalone.xml. This file is also used to configure non-infrastructure level things that are specific to Red Hat Single Sign-On components.
Standalone Config File
Any changes you make to this file while the server is running will not take effect and may even be overwritten by the server. Instead use the command line scripting or the web console of JBoss EAP. See the JBoss EAP Configuration Guide for more information.
3.2. Using standalone clustered mode
Standalone clustered operation mode applies when you want to run Red Hat Single Sign-On within a cluster. This mode requires that you have a copy of the Red Hat Single Sign-On distribution on each machine where you want to run a server instance. This mode can be very easy to deploy initially, but can become quite cumbersome. To make a configuration change, you modify each distribution on each machine. For a large cluster, this mode can become time consuming and error prone.
3.2.1. Standalone clustered configuration
The distribution has a mostly pre-configured app server configuration file for running within a cluster. It has all the specific infrastructure settings for networking, databases, caches, and discovery. This file resides in …/standalone/configuration/standalone-ha.xml. There’s a few things missing from this configuration. You can’t run Red Hat Single Sign-On in a cluster without configuring a shared database connection. You also need to deploy some type of load balancer in front of the cluster. The clustering and database sections of this guide walk you through these things.
Standalone HA Config
Any changes you make to this file while the server is running will not take effect and may even be overwritten by the server. Instead use the command line scripting or the web console of JBoss EAP. See the JBoss EAP Configuration Guide for more information.
3.2.2. Booting in standalone clustered mode
You use the same boot scripts to start Red Hat Single Sign-On as you do in standalone mode. The difference is that you pass in an additional flag to point to the HA config file.
Standalone Clustered Boot Scripts
To boot the server:
Linux/Unix
$ .../bin/standalone.sh --server-config=standalone-ha.xml
Windows
> ...\bin\standalone.bat --server-config=standalone-ha.xml
3.3. Using domain clustered mode
Domain mode is a way to centrally manage and publish the configuration for your servers.
Running a cluster in standard mode can quickly become aggravating as the cluster grows in size. Every time you need to make a configuration change, you perform it on each node in the cluster. Domain mode solves this problem by providing a central place to store and publish configurations. It can be quite complex to set up, but it is worth it in the end. This capability is built into the JBoss EAP Application Server which Red Hat Single Sign-On derives from.
The guide will go over the very basics of domain mode. Detailed steps on how to set up domain mode in a cluster should be obtained from the JBoss EAP Configuration Guide.
Here are some of the basic concepts of running in domain mode.
- domain controller
- The domain controller is a process that is responsible for storing, managing, and publishing the general configuration for each node in the cluster. This process is the central point from which nodes in a cluster obtain their configuration.
- host controller
- The host controller is responsible for managing server instances on a specific machine. You configure it to run one or more server instances. The domain controller can also interact with the host controllers on each machine to manage the cluster. To reduce the number of running process, a domain controller also acts as a host controller on the machine it runs on.
- domain profile
- A domain profile is a named set of configuration that can be used by a server to boot from. A domain controller can define multiple domain profiles that are consumed by different servers.
- server group
- A server group is a collection of servers. They are managed and configured as one. You can assign a domain profile to a server group and every service in that group will use that domain profile as their configuration.
In domain mode, a domain controller is started on a master node. The configuration for the cluster resides in the domain controller. Next a host controller is started on each machine in the cluster. Each host controller deployment configuration specifies how many Red Hat Single Sign-On server instances will be started on that machine. When the host controller boots up, it starts as many Red Hat Single Sign-On server instances as it was configured to do. These server instances pull their configuration from the domain controller.
In some environments, such as Microsoft Azure, the domain mode is not applicable. Please consult the JBoss EAP documentation.
3.3.1. Domain configuration
Various other chapters in this guide walk you through configuring various aspects like databases, HTTP network connections, caches, and other infrastructure related things. While standalone mode uses the standalone.xml file to configure these things, domain mode uses the …/domain/configuration/domain.xml configuration file. This is where the domain profile and server group for the Red Hat Single Sign-On server are defined.
domain.xml
Any changes you make to this file while the domain controller is running will not take effect and may even be overwritten by the server. Instead use the command line scripting or the web console of JBoss EAP. See the JBoss EAP Configuration Guide for more information.
Let’s look at some aspects of this domain.xml file. The auth-server-standalone
and auth-server-clustered
profile
XML blocks are where you are going to make the bulk of your configuration decisions. You’ll be configuring things here like network connections, caches, and database connections.
auth-server profile
<profiles>
<profile name="auth-server-standalone">
...
</profile>
<profile name="auth-server-clustered">
...
</profile>
The auth-server-standalone
profile is a non-clustered setup. The auth-server-clustered
profile is the clustered setup.
If you scroll down further, you’ll see various socket-binding-groups
defined.
socket-binding-groups
<socket-binding-groups>
<socket-binding-group name="standard-sockets" default-interface="public">
...
</socket-binding-group>
<socket-binding-group name="ha-sockets" default-interface="public">
...
</socket-binding-group>
<!-- load-balancer-sockets should be removed in production systems and replaced with a better software or hardware based one -->
<socket-binding-group name="load-balancer-sockets" default-interface="public">
...
</socket-binding-group>
</socket-binding-groups>
This configration defines the default port mappings for various connectors that are opened with each Red Hat Single Sign-On server instance. Any value that contains ${…}
is a value that can be overridden on the command line with the -D
switch, i.e.
$ domain.sh -Djboss.http.port=80
The definition of the server group for Red Hat Single Sign-On resides in the server-groups
XML block. It specifies the domain profile that is used (default
) and also some default boot arguments for the Java VM when the host controller boots an instance. It also binds a socket-binding-group
to the server group.
server group
<server-groups>
<!-- load-balancer-group should be removed in production systems and replaced with a better software or hardware based one -->
<server-group name="load-balancer-group" profile="load-balancer">
<jvm name="default">
<heap size="64m" max-size="512m"/>
</jvm>
<socket-binding-group ref="load-balancer-sockets"/>
</server-group>
<server-group name="auth-server-group" profile="auth-server-clustered">
<jvm name="default">
<heap size="64m" max-size="512m"/>
</jvm>
<socket-binding-group ref="ha-sockets"/>
</server-group>
</server-groups>
3.3.2. Host controller configuration
Red Hat Single Sign-On comes with two host controller configuration files that reside in the …/domain/configuration/ directory: host-master.xml and host-slave.xml. host-master.xml is configured to boot up a domain controller, a load balancer, and one Red Hat Single Sign-On server instance. host-slave.xml is configured to talk to the domain controller and boot up one Red Hat Single Sign-On server instance.
The load balancer is not a required service. It exists so that you can easily test drive clustering on your development machine. While usable in production, you have the option of replacing it if you have a different hardware or software based load balancer you want to use.
Host Controller Config
To disable the load balancer server instance, edit host-master.xml and comment out or remove the "load-balancer"
entry.
<servers>
<!-- remove or comment out next line -->
<server name="load-balancer" group="loadbalancer-group"/>
...
</servers>
Another interesting thing to note about this file is the declaration of the authentication server instance. It has a port-offset
setting. Any network port defined in the domain.xml socket-binding-group
or the server group will have the value of port-offset
added to it. For this sample domain setup, we do this so that ports opened by the load balancer server don’t conflict with the authentication server instance that is started.
<servers>
...
<server name="server-one" group="auth-server-group" auto-start="true">
<socket-bindings port-offset="150"/>
</server>
</servers>
3.3.3. Server instance working directories
Each Red Hat Single Sign-On server instance defined in your host files creates a working directory under …/domain/servers/{SERVER NAME}. Additional configuration can be put there, and any temporary, log, or data files the server instance needs or creates go there too. The structure of these per server directories ends up looking like any other JBoss EAP booted server.
Working Directories
3.3.4. Booting in domain clustered mode
When running the server in domain mode, there is a specific script you need to run to boot the server depending on your operating system. These scripts live in the bin/ directory of the server distribution.
Domain Boot Script
To boot the server:
Linux/Unix
$ .../bin/domain.sh --host-config=host-master.xml
Windows
> ...\bin\domain.bat --host-config=host-master.xml
When running the boot script you will need to pass in the host controlling configuration file you are going to use via the --host-config
switch.
3.3.5. Testing with a sample clustered domain
You can test drive clustering using the sample domain.xml configuration. This sample domain is meant to run on one machine and boots up:
- a domain controller
- an HTTP load balancer
- two Red Hat Single Sign-On server instances
Procedure
Run the
domain.sh
script twice to start two separate host controllers.The first one is the master host controller that starts a domain controller, an HTTP load balancer, and one Red Hat Single Sign-On authentication server instance. The second one is a slave host controller that starts up only an authentication server instance.
Configure the slave host controller so that it can talk securely to the domain controller. Perform these steps:
If you omit these steps, the slave host cannot obtain the centralized configuration from the domain controller.
Set up a secure connection by creating a server admin user and a secret that are shared between the master and the slave.
Run the
…/bin/add-user.sh
script.Select
Management User
when the script asks about the type of user to add.This choice generates a secret that you cut and paste into the …/domain/configuration/host-slave.xml file.
Add App Server Admin
$ add-user.sh What type of user do you wish to add? a) Management User (mgmt-users.properties) b) Application User (application-users.properties) (a): a Enter the details of the new user to add. Using realm 'ManagementRealm' as discovered from the existing property files. Username : admin Password recommendations are listed below. To modify these restrictions edit the add-user.properties configuration file. - The password should not be one of the following restricted values {root, admin, administrator} - The password should contain at least 8 characters, 1 alphabetic character(s), 1 digit(s), 1 non-alphanumeric symbol(s) - The password should be different from the username Password : Re-enter Password : What groups do you want this user to belong to? (Please enter a comma separated list, or leave blank for none)[ ]: About to add user 'admin' for realm 'ManagementRealm' Is this correct yes/no? yes Added user 'admin' to file '/.../standalone/configuration/mgmt-users.properties' Added user 'admin' to file '/.../domain/configuration/mgmt-users.properties' Added user 'admin' with groups to file '/.../standalone/configuration/mgmt-groups.properties' Added user 'admin' with groups to file '/.../domain/configuration/mgmt-groups.properties' Is this new user going to be used for one AS process to connect to another AS process? e.g. for a slave host controller connecting to the master or for a Remoting connection for server to server EJB calls. yes/no? yes To represent the user add the following to the server-identities definition <secret value="bWdtdDEyMyE=" />
NoteThe add-user.sh script does not add the user to the Red Hat Single Sign-On server but to the underlying JBoss Enterprise Application Platform. The credentials used and generated in this script are only for demonstration purposes. Please use the ones generated on your system.
Cut and paste the secret value into the …/domain/configuration/host-slave.xml file as follows:
<management> <security-realms> <security-realm name="ManagementRealm"> <server-identities> <secret value="bWdtdDEyMyE="/> </server-identities>
Add the username of the created user in the …/domain/configuration/host-slave.xml file:
<remote security-realm="ManagementRealm" username="admin">
Run the boot script twice to simulate a two node cluster on one development machine.
Boot up master
$ domain.sh --host-config=host-master.xml
Boot up slave
$ domain.sh --host-config=host-slave.xml
- Open your browser and go to http://localhost:8080/auth to try it out.
3.4. Using cross-site replication mode
Cross-site replication, which was introduced as a Technology Preview feature in Red Hat Single Sign-On 7.2, is no longer available as a supported feature in any Red Hat SSO 7.x release including the latest RH-SSO 7.6 release. Red Hat does not recommend any customer implement or use this feature in their environment because it is not supported. Also, support exceptions for this feature are no longer considered or accepted.
A new solution for cross-site replication is being discussed and tentatively considered for a future release of Red Hat build of Keycloak (RHBK), which is the product that will be introduced instead of Red Hat SSO 8. More details will be available soon.
