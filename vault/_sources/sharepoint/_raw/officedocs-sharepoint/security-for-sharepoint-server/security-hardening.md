---
title: "Plan security hardening for SharePoint Server - SharePoint Server"
description: "Learn about security hardening for SharePoint Server and database server roles, including specific hardening requirements for ports, protocols, and services."
ms.topic: article
---
Note

Plan security hardening for SharePoint Server

# Plan security hardening for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Secure server snapshots

## Secure server snapshots

In a server farm environment, individual servers have specific roles. Security hardening recommendations for these servers depend on the role each server plays. This article contains secure snapshots for two categories of server roles:

SharePoint servers

Database server role

The snapshots are divided into common configuration categories. The characteristics defined for each category represent the optimal hardened state for SharePoint Server. This article doesn't include hardening guidance for other software in the environment.

In addition to hardening servers for specific roles, it's important to protect the SharePoint farm by placing a firewall between the farm servers and outside requests. The guidance in this article can be used to configure a firewall.

SharePoint servers

### SharePoint servers

This section identifies hardening characteristics for SharePoint servers. Some of the guidance applies to specific service applications; in these cases, the corresponding characteristics need to be applied only on the servers that are running the services associated with the specified service applications.

| **Category** | **Characteristic** |
| --- | --- |
| Services listed in the Services MMC snap-in | Enable the following services:  
  ASP.NET State service (if you're using InfoPath Forms Services or Project Server 2016)  
  View State service (if you're using InfoPath Forms Services)  
  World Wide Web Publishing Service  
  Ensure that these services aren't disabled:  
  Claims to Windows Token Service  
  SharePoint Administration  
  SharePoint Timer Service  
  SharePoint Tracing Service  
  SharePoint VSS Writer  
  Ensure that these services aren't disabled on the servers that host the corresponding roles:  
  AppFabric Caching Service  
  SharePoint User Code Host  
  SharePoint Search Host Controller  
  SharePoint Server Search  
  Ports and protocols |
|  | TCP 80, TCP 443 (SSL)  
  Custom ports for search crawling, if configured (such as for crawling a file share or a website on a non-default port)  
  Ports used by the search index component — TCP 16500-16519 (intra-farm only)  
  Ports required for the AppFabric Caching Service — TCP 22233-22236  
  Ports required for Windows Communication Foundation communication — TCP 808  
  Ports required for communication between SharePoint servers and service applications (the default is HTTP):  
  HTTP binding: TCP 32843  
  HTTPS binding: TCP 32844  
  net.tcp binding: TCP 32845 (only if a third party has implemented this option for a service application)  
  If your computer network environment uses Windows Server 2012, Windows Server 2008, Windows Server 2008 R2, Windows 7, or Windows Vista together with versions of Windows earlier than Windows Server 2012 and Windows Vista, you must enable connectivity over both the following port ranges:  
  High port range 49152 through 65535  
  Low port range 1025 through 5000  
  Default ports for SQL Server communication — TCP 1433, UDP 1434. If these ports are blocked on the SQL Server computer and databases are installed on a named instance, configure a SQL Server client alias for connecting to the named instance.  
  Microsoft SharePoint Foundation User Code Service (for sandbox solutions) — TCP 32846. This port must be open for outbound connections on all Front-end and Front-end with Distributed Cache servers. This port must be open for inbound connections on Front-end and Front-end with Distributed Cache servers where this service is turned on.  
  Ensure that ports remain open for Web applications that are accessible to users.  
  Block external access to the port that is used for the Central Administration site.  
  SMTP for e-mail integration — TCP 25, or a custom TCP port if you've configured outbound e-mail to use a non-default port.  
 ICMP for echo request – each Distributed Cache server should have inbound/outbound firewall rules of enabling ICMP for echo request. |
| Registry | No additional guidance |
| Auditing and logging | If log files are relocated, ensure that the log file locations are updated to match. Update directory access control lists (ACLs) also. |
| Web.config | Follow these recommendations for each Web.config file that is created after you run Setup:  
  Don't allow compilation or scripting of database pages via the PageParserPaths elements.  
  Ensure <SafeMode> CallStack="false" and AllowPageLevelTrace="false".  
  Ensure that the Web Part limits around maximum controls per zone are set low.  
  Ensure that the SafeControls list is set to the minimum set of controls needed for your sites.  
  Ensure that your Workflow SafeTypes list is set to the minimum level of SafeTypes needed.  
  Ensure that customErrors is turned on (<customErrors mode="On"/>).  
  Consider your Web proxy settings as needed (<system.net>/<defaultProxy>).  
  Set the Upload.aspx limit to the highest size you reasonably expect users to upload. Performance can be affected by uploads that exceed 100 MB. |

Database server role

### Database server role

Note

With the addition to the MinRole feature in SharePoint Server 2016, the concept of roles has changed. For information about roles, see Planning for a MinRole server deployment in SharePoint Server 2016.

The primary recommendation for SharePoint Server is to secure inter-farm communication by blocking the default ports used for SQL Server communication and establishing custom ports for this communication instead. For more information about how to configure ports for SQL Server communication, see Blocking the standard SQL Server ports, later in this article.

| **Category** | **Characteristic** |
| --- | --- |
| Ports | Block UDP 1434.  
  Consider blocking TCP 1433. |

This article doesn't describe how to secure SQL Server. For more information about how to secure SQL Server, see Securing SQL Server (https://go.microsoft.com/fwlink/p/?LinkId=186828).

Specific port, protocol, and service guidance

## Specific port, protocol, and service guidance

The rest of this article describes in greater detail the specific hardening requirements for SharePoint Server.

In this section:

Blocking the standard SQL Server ports

Service application communication

Connections to external servers

Service requirements for e-mail integration

Service requirements for session state

SharePoint Server Products services

Web.config file

Blocking the standard SQL Server ports

### Blocking the standard SQL Server ports

The specific ports used to connect to SQL Server are affected by whether databases are installed on a default instance of SQL Server or a named instance of SQL Server. The default instance of SQL Server listens for client requests on TCP 1433. A named instance of SQL Server listens on a randomly assigned port number. Additionally, the port number for a named instance can be reassigned if the instance is restarted (depending on whether the previously assigned port number is available).

By default, client computers that connect to SQL Server first connect by using TCP 1433. If this communication is unsuccessful, the client computers query the SQL Server Resolution Service that is listening on UDP 1434 to determine the port on which the database instance is listening.

The default port-communication behavior of SQL Server introduces several issues that affect server hardening. First, the ports used by SQL Server are well-publicized ports and the SQL Server Resolution Service has been the target of buffer overrun attacks and denial-of-service attacks, including the "Slammer" worm virus. Even if SQL Server is updated to mitigate security issues in the SQL Server Resolution Service, the well-publicized ports remain a target. Second, if databases are installed on a named instance of SQL Server, the corresponding communication port is randomly assigned and can change. This behavior can potentially prevent server-to-server communication in a hardened environment. The ability to control which TCP ports are open or blocked is essential to securing your environment.

Note

We recommend to use the standard SQL ports, but ensure the firewall is configured to only allow communication with the servers that need access to the SQL Server. Servers that don't need access to the SQL Server should be blocked from connecting to the SQL Server over TCP port 1433 and UDP port 1444.

There are several methods you can use to block ports. You can block these ports by using a firewall. However, unless you can be sure that there are no other routes into the network segment and that there are no malicious users that have access to the network segment, the recommendation is to block these ports directly on the server that hosts SQL Server. This can be accomplished by using Windows Firewall in Control Panel.

Configuring SQL Server database instances to listen on a nonstandard port

#### Configuring SQL Server database instances to listen on a nonstandard port

SQL Server provides the ability to reassign the ports that are used by the default instance and any named instances. In SQL Server, you reassign ports by using SQL Server Configuration Manager.

Configuring SQL Server client aliases

#### Configuring SQL Server client aliases

In a server farm, all front-end Web servers and application servers are SQL Server client computers. If you block UDP 1434 on the SQL Server computer, or you change the default port for the default instance, you must configure a SQL Server client alias on all servers that connect to the SQL Server computer. In this scenario, the SQL Server client alias specifies the TCP port that the named instance is listening on.

To connect to an instance of SQL Server, you install SQL Server client components on the target computer and then configure the SQL Server client alias by using SQL Server Configuration Manager. To install SQL Server client components, run Setup and select only the following client components to install:

Connectivity Components

Management Tools (includes SQL Server Configuration Manager)

For specific hardening steps for blocking the standard SQL Server ports, see Configure SQL Server security for SharePoint Server.

Service application communication

### Service application communication

By default, communication between SharePoint servers and service applications within a farm takes place by using HTTP with a binding to TCP 32843. When you publish a service application, you can select either HTTP or HTTPS with the following bindings:

HTTP binding: TCP 32843

HTTPS binding: TCP 32844

Additionally, third parties that develop service applications can implement a third choice:

- net.tcp binding: TCP 32845

You can change the protocol and port binding for each service application. On the Service Applications page in Central Administration, select the service application, and then select **Publish**.

The HTTP/HTTPS/net.tcp bindings can also be viewed and changed by using the Get-SPServiceHostConfig and Set-SPServiceHostConfig Microsoft PowerShell cmdlets.

Communication between service applications and SQL Server takes place over the standard SQL Server ports or the ports that you configure for SQL Server communication.

Connections to external servers

### Connections to external servers

Several features of SharePoint Server can be configured to access data that resides on server computers outside of the server farm. If you configure access to data that is located on external server computers, ensure that you enable communication between the appropriate computers. In most cases, the ports, protocols, and services that are used depend on the external resource. For example:

Connections to file shares use the File and Printer Sharing service.

Connections to external SQL Server databases use the default or customized ports for SQL Server communication.

Connections to Oracle databases typically use OLE DB.

Connections to Web services use both HTTP and HTTPS.

The following table lists features that can be configured to access data that resides on server computers outside the server farm.

| **Feature** | **Description** |
| --- | --- |
| Content crawling | You can configure crawl rules to crawl data that resides on external resources, including Web sites, file shares, Exchange public folders, and business data applications. When crawling external data sources, the crawl role communicates directly with these external resources.  
 For more information, see Manage crawling in SharePoint Server. |
| Business Data Connectivity connections | Web servers and application servers communicate directly with computers that are configured for Business Data Connectivity connections. |

Service requirements for e-mail integration

### Service requirements for e-mail integration

E-mail integration requires the use of two services:

SMTP service

Microsoft SharePoint Directory Management service

SMTP service

#### SMTP service

E-mail integration requires the use of the Simple Mail Transfer Protocol (SMTP) service on at least one of the front-end Web servers in the server farm. The SMTP service is required for incoming e-mail. For outgoing e-mail, you can either use the SMTP service or route outgoing email through a dedicated e-mail server in your organization, such as a Microsoft Exchange Server computer.

Microsoft SharePoint Directory Management service

#### Microsoft SharePoint Directory Management service

SharePoint Server includes an internal service, the Microsoft SharePoint Directory Management Service, for creating e-mail distribution groups. When you configure e-mail integration, you have the option to enable the Directory Management Service feature, which lets users create distribution lists. When users create a SharePoint group and they select the option to create a distribution list, the Microsoft SharePoint Directory Management Service creates the corresponding Active Directory distribution list in the Active Directory environment.

In security-hardened environments, the recommendation is to restrict access to the Microsoft SharePoint Directory Management Service by securing the file associated with this service, which is SharePointEmailws.asmx. For example, you might allow access to this file by the server farm account only.

Additionally, this service requires permissions in the Active Directory environment to create Active Directory distribution list objects. The recommendation is to set up a separate organizational unit (OU) in Active Directory for SharePoint Server objects. Only this OU should allow write access to the account that is used by the Microsoft SharePoint Directory Management Service.

Service requirements for session state

### Service requirements for session state

Both Project Server 2016 and InfoPath Forms Services maintain session state. If you're deploying these features or products within your server farm, don't disable the ASP.NET State service. Additionally, if you're deploying InfoPath Forms Services, don't disable the View State service.

SharePoint Server Products services

### SharePoint Server Products services

Don't disable services that are installed by SharePoint Server (listed in the snapshot previously).

If your environment disallows services that run as a local system, you can consider disabling the SharePoint Administration service only if you're aware of the consequences and can work around them. This service is a Win32 service that runs as a local system.

This service is used by the SharePoint Timer service to perform actions that require administrative permissions on the server, such as creating Internet Information Services (IIS) Web sites, deploying code, and stopping and starting services. If you disable this service, you can't complete deployment-related tasks from the Central Administration site. You must use Microsoft PowerShell to run the Start-SPAdminJob cmdlet (or use the Stsadm.exe command-line tool to run the **execadmsvcjobs** operation) to complete multiple-server deployments for SharePoint Server and to run other deployment-related tasks.

Web.config file

### Web.config file

The .NET Framework, and ASP.NET in particular, use XML-formatted configuration files to configure applications. The .NET Framework relies on configuration files to define configuration options. The configuration files are text-based XML files. Multiple configuration files can, and typically do, exist on a single system.

System-wide configuration settings for the .NET Framework are defined in the Machine.config file. The Machine.config file is located in the %SystemRoot%\Microsoft.NET\Framework%VersionNumber%\CONFIG\ folder. The default settings that are contained in the Machine.config file can be modified to affect the behavior of applications that use the .NET Framework on the whole system.

You can change the ASP.NET configuration settings for a single application if you create a Web.config file in the root folder of the application. When you do this, the settings in the Web.config file override the settings in the Machine.config file.

When you extend a Web application by using Central Administration, SharePoint Server automatically creates a Web.config file for the Web application.

The Web server and application server snapshot presented earlier in this article lists recommendations for configuring Web.config files. These recommendations are intended to be applied to each Web.config file that is created, including the Web.config file for the Central Administration site.

For more information about ASP.NET configuration files and editing a Web.config file, see ASP.NET Configuration (https://go.microsoft.com/fwlink/p/?LinkID=73257).

See also

## See also

Concepts

#### Concepts

Security for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
