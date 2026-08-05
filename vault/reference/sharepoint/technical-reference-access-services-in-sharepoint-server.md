---
title: "Access Services in SharePoint Server knowledge articles - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-access-services-in-sharepoint-server
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/access-services-in-sharepoint-server
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve alerts about Access Services in the SharePoint Server management pack for Systems Center Operations Manager (SCOM)."
---

# Access Services in SharePoint Server knowledge articles - SharePoint Server

Note

Access Services in SharePoint Server knowledge articles

# Access Services in SharePoint Server knowledge articles

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn how to resolve alerts about Access Services in the SharePoint Servers 2019, 2016 and 2013 management pack for Systems Center Operations Manager (SCOM).

The articles in this section are knowledge articles for Access Services in SharePoint Server. Typically, you would see these articles after clicking a link in an alert in the Operations Manager console. You can use these articles to help you troubleshoot and resolve problems in Access Services in SharePoint Server.

Note

Access Services 2010 has been removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps and Power Automate as potential alternatives to Access Services 2010.

Download and install:

System Center Management Pack for SharePoint Server 2019

System Center Monitoring Pack for SharePoint Server 2016

System Center Monitoring Pack for SharePoint Server 2013

System Center Monitoring Pack for SharePoint Foundation 2013

Use the following information to resolve the Access Services error messages:

No application info from content database

WFE to ADS communication failure

No servers available for database creation

Partitioned SSS communication failure

Unpartitioned SSS communication failure

Trigger for excessive failed SQL connections requests

Excessive failed SQL connections

Trigger for excessive SQL connection retries

Excessive SQL connection retries

Trigger for excessive SQL write failures

Excessive SQL write failures

No available ADS servers

No default proxy

Failed to register database server

No application info from content database

## No application info from content database

**Alert Name:** Access Services: No application info from content database

**Summary:** Access Data Services tries to retrieve application information from the SharePoint Content Database, but cannot find the relevant app's information. If this occurs, the application will not be available for use.

Cause

### Cause

Someone creates a site that uses an Access template that is not actually an Access application.

Resolution

### Resolution

Delete the site that is created incorrectly.

WFE to ADS communication failure

## WFE to ADS communication failure

**Alert Name:** Access Services: WFE to ADS communication failure

**Summary:** Access Data Services WFE (Web Front End) is unable to communicate with the ADS (Access Data Services) middle tier.

Cause

### Cause

One or more of the following might be the cause:

Network issues

Hardware failure

SharePoint service failure

Disabled Access Database Services on the server

Resolution

### Resolution

Ensure that network is healthy.

Ensure that ADS server is available.

Ensure that ADS server can be accessed from WFE.

Ensure IIS Process for ADS application pool is running.

Ensure that the ADS service is enabled on the failing ADS server.

No servers available for database creation

## No servers available for database creation

**Alert Name:** Access Services: No servers available for database creation

**Summary:** During application creation, Access Data services cannot find an available SQL Server to provision the new database.

Cause

### Cause

No SQL database servers are configured for Access to provision new databases.

Resolution

### Resolution

If the creation failure occurs while creating from the Access client, check the Database Server group mappings to determine where the shortage has occurred:

Use  `Get-SPAccessServicesDatabaseServerGroupMapping` to determine whether there is a mapping from the Object Model to the Server Group.

Use  `Get-SPAccessServicesDatabaseServerGroup` to determine whether the server group has at least one database.

Use  `Get-SPAccessServicesDatabaseServer` to determine whether there is at least one database in the server group marked as "AvailableForCreate".

If the creation failure occurs while creating from the Corporate Catalog, check the Database Server group mappings to determine where the shortage has occurred:

Use  `Get-SPAccessServicesDatabaseServerGroupMapping` to determine whether there is a mapping from the Corporate Catalog to the Server Group.

Use  `Get-SPAccessServicesDatabaseServerGroup` to determine whether the server group has at least one database.

Use  `Get-SPAccessServicesDatabaseServer` to determine whether there is at least one database in the server group marked as "AvailableForCreate".

Related topics

### Related topics

Get-SPAccessServicesDatabaseServerGroupMapping

Get-SPAccessServicesDatabaseServerGroup

Get-SPAccessServicesDatabaseServer

Partitioned SSS communication failure

## Partitioned SSS communication failure

**Alert Name:** Access Services: Partitioned SSS communication failure

**Summary:** Access Data Services tries to communicate with SharePoint partitioned Secure Store Service, but is unable to communicate with it.

Cause

### Cause

Partitioned Secure Store Service in the farm is down or unreachable because of Network issues or incorrect configurations.

Resolution

### Resolution

Ensure partitioned Secure Store Service Application exists and is running.

Ensure Proxy for partitioned Secure Store Service exists and is in the default Proxy group.

Related topics

### Related topics

Configure the Secure Store Service in SharePoint Server

Unpartitioned SSS communication failure

## Unpartitioned SSS communication failure

**Alert Name:** Access Services: Unpartitioned SSS communication failure

**Summary:** Access Data Services tries to communicate with SharePoint unpartitioned Secure Store Service, but is unable to communicate with it.

Cause

### Cause

Unpartitioned Secure Store Service in the farm is down or unreachable because of Network issues or incorrect configurations.

Resolution

### Resolution

Ensure unpartitioned Secure Store Service Application exists and is running.

Ensure Proxy for unpartitioned Secure Store Service exists and is in the default Proxy group.

Related topics

### Related topics

Configure the Secure Store Service in SharePoint Server

Trigger for excessive failed SQL connections requests

## Trigger for excessive failed SQL connections requests

**Alert Name:** Access Services: Trigger for excessive failed SQL connections requests

**Summary:** This alert occurs when Access Data services exceed the expected number of retries when the services connect to the SQL Server Databases.

Cause

### Cause

SQL Server database server is down, unavailable, or unreachable.

Resolution

### Resolution

Check network health.

Make sure that the SQL Server database server is available and healthy.

Excessive failed SQL connections

## Excessive failed SQL connections

**Alert Name:** Access Services: Excessive failed SQL connections

**Summary:** This tracks the number of failed SQL connections.

Cause

### Cause

N/A

Resolution

### Resolution

N/A

Trigger for excessive SQL connection retries

## Trigger for excessive SQL connection retries

**Alert Name:** Access Services: Trigger for excessive SQL connection retries

**Summary:** This alert occurs when Access Data services exceed the expected number of retries when the services connect to the Application SQL Databases.

Cause

### Cause

One or more of the following might be the cause:

Network issues

Application SQL databases are unavailable or unreachable.

Resolution

### Resolution

Check network health.

Check Application SQL databases availability and healthy states.

Excessive SQL connection retries

## Excessive SQL connection retries

**Alert Name:** Access Services: Excessive SQL connection retries

**Summary:** This monitors the number of SQL Database Server Connection retries.

Cause

### Cause

N/A

Resolution

### Resolution

N/A

Trigger for excessive SQL write failures

## Trigger for excessive SQL write failures

**Alert Name:** Access Services: Trigger for excessive SQL write failures

**Summary:** This alert occurs if there are too many SQL Write failures.

Cause

### Cause

Excessive number of SQL Write failures.

Resolution

### Resolution

Check network health.

Check status of SQL Azure service.

Raise an incident with SQL Azure for resolution.

Excessive SQL write failures

## Excessive SQL write failures

**Alert Name:** Access Services: Excessive SQL write failures

**Summary:** Monitors the number of failed SQL Database Server writes

Cause

### Cause

One or more of the following might be the cause:

Application SQL Databases are unavailable or unreachable.

Deadlock occurs on the server.

Excessive server load makes the database server unresponsive.

Resolution

### Resolution

Ensure that the Database server is available, is not overloaded, and has no deadlocks.

No available ADS servers

## No available ADS servers

**Alert Name:** Access Services: No available ADS servers

**Summary:** There are no Access Data Services Servers or the available Access Data Services Servers are not healthy enough to serve the request.

Cause

### Cause

One or more of the following might be the cause:

Excessive memory consumption overloads your ADS Servers.

Network problems

A number of Access Database Server instances fail or are down.

Resolution

### Resolution

Ensure that Access Database Services is enabled on at least one server in the farm.

Reboot Access Database Service instances to free memory.

Ensure Access Database Service instances are available and are configured correctly.

No default proxy

## No default proxy

**Alert Name:** Access Services: No default proxy

**Summary:** There is no Access Data Services Proxy in the Default Proxy group.

Cause

### Cause

No default proxy is established during configuration, or there is a problem during provisions and a default proxy is not established.

Resolution

### Resolution

Use  `new-SPAccessServicesApplicationProxy` to create a new default proxy.

Related topics

### Related topics

New-SPAccessServicesApplication

Failed to register database server

## Failed to register database server

**Alert Name:** Access Services: Failed to register database server

**Summary:** During Database server configuration, a server fails to register.

Cause

### Cause

One or more of the following might be the cause:

Network issues connecting to the server

Incorrect Database server version

Server does not have required features or insufficient permissions

Resolution

### Resolution

Check network health.

Update the database server version.

Install required features or update permissions.

Note

App pool user must have DBCreator and SecurityAdmin permissions.

See also

## See also

Concepts

#### Concepts

Plan for monitoring in SharePoint Server

Other Resources

#### Other Resources

System Center Monitoring Pack for SharePoint Foundation

System Center Monitoring Pack for SharePoint Server 2013

System Center Monitoring Pack for SharePoint Server 2016

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
