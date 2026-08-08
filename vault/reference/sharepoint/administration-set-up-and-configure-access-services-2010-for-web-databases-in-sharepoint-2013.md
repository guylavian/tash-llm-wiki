---
title: "Set up and configure Access Services 2010 for web databases in SharePoint Server 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-set-up-and-configure-access-services-2010-for-web-databases-in-sharepoint-2013
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/set-up-and-configure-access-services-2010-for-web-databases-in-sharepoint-2013
family: administration
documentKind: "install-set-up-deploy"
abstract: "Learn how to use Access Services 2010 to modify and publish an Access web database in SharePoint Server 2013 that was previously created in SharePoint Server 2010."
---

# Set up and configure Access Services 2010 for web databases in SharePoint Server 2013 - SharePoint Server

Note

Set up and configure Access Services 2010 for web databases in SharePoint Server 2013

# Set up and configure Access Services 2010 for web databases in SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Access Services 2010 is a service application that allows users to modify and publish in SharePoint 2013 an Access web database that was previously created in SharePoint Server 2010.

The Access client is not required to use the published web database. However, the Access client is required to make any changes to the database structure.

Note

Access Services 2010 has been removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps and Power Automate as potential alternatives to Access Services 2010.

Set up SQL Server Reporting Services

## Set up SQL Server Reporting Services

You can update existing reports in an Access web database, but these reports require the installation and configuration of SQL Server Reporting Services Mode for SharePoint and the content database must be running SQL Server 2012. For more information, see Install Reporting Services SharePoint Mode for SharePoint 2013 in SQL Server Books Online.

Start Access Database Service 2010

## Start Access Database Service 2010

If for some reason Access Database Service 2010 has not been started, do the following:

On the SharePoint Central Administration website, under **System Settings**, click **Manage services on the server**.

On the same row as the **Access Database Service 2010** service, under **Action**, click **Start**.

Create an Access Services 2010 service application

## Create an Access Services 2010 service application

If for some reason an Access Services 2010 service application has not been created, do the following:

In Central Administration, under **Application Management**, click **Manage service applications**.

On the **Manage Service Applications** page, click **New**, and then click **Access Services 2010**.

In the **Access Services Application Name** section, type Access Services 2010 in the text box.

Do one of the following:

Select the **Use existing application pool** option, and then select an **Application pool name** from the list.

Select the **Create new application pool** option, and then type AccessServicesAppPool in the **Application pool name** text box.

Select the **Configurable** option, and then from the drop-down list, select the Farm administrator account.

Click **OK**.

Configure Access Services 2010 settings

## Configure Access Services 2010 settings

There are no additional settings required after the initial installation of Access Services 2010. The services are ready to use as soon as the SharePoint 2013 installation is complete. However, you can change the default configuration settings to suit your business need. The following table contains the configurable Access Services settings.

Verify that the user account that is performing this procedure is a site administrator for the Access Services 2010 service application and also has Designer permissions.

In Central Administration, in the **Application Management** section, click **Manage service applications**.

Click the Access Services 2010 service application that you want to change.

On the Access Services 2010 settings page, change any of the settings shown in the following table.

| **Setting** | **Description** |
| --- | --- |
| **Lists and Queries** | **Settings for queries used against Microsoft SharePoint Foundation lists** |
| Maximum Columns per query | The maximum number of columns that can be referenced in a query. Note that some columns may automatically be reference by the query engine and will be included in this limit.  
 Valid values: from 1 to 255  
 Default value: 40 |
| Maximum Rows per query | The maximum number of rows that a list used in a query can have, or that the output of the query can have.  
 Valid values: from 1 to 200000  
 Default value: 25000 |
| Maximum Sources per query | The maximum number of lists that may be used as input to one query.  
 Valid values: from 1 to 20  
 Default value: 12 |
| Maximum Calculated Columns per query | The maximum number of inline calculated columns that can be included in a query, either in the query itself or in any sub-query on which it is based. Calculated columns in the underlying SharePoint Foundation list are not included.  
 Valid values: from 0 to 32  
 Default value: 10 |
| Maximum Order by Clauses per query | The maximum number of Order By clauses in the query.  
 Valid values: from 0 to 8  
 Default value: 4 |
| Allow Outer Joins | Allow left and right outer joins in a query. Inner Joins are always allowed.  
 Check box: selected or cleared for **Outer Joins allowed**. |
| Allow Non Remote-able Queries | Allow queries that cannot be remoted to the database tier to run.  
 Check box: selected or cleared for **Remotable Queries allowed**. |
| Maximum Records Per Table | The maximum number of records that a table in an application can contain.  
 Valid values: -1 (indicates no limit), any positive integer  
 Default value: 500000 |
| **Application Objects** | **Limitations on the types of objects an Access Services application can contain** |
| Maximum Application Log Size | The maximum number of records for an Access Services Application Log list.  
 Valid values: -1 (indicates no limit), from 1 to any positive integer  
 Default value: 3000 |
| **Session Management** | **Behavior of Access Database Service sessions** |
| Maximum Request Duration | The maximum duration (in seconds) allowed for a request from an application.  
 Valid values: -1 (indicates no limit), 1 through 2007360 (24 days)  
 Default value: 30 |
| Maximum Sessions Per User | The maximum number of sessions allowed per anonymous user. If a user has this many sessions and starts a new session, the user's oldest session is deleted.  
 Valid values: -1 (no limit), from 1 to any positive integer  
 Default value: 10 |
| Maximum Sessions Per Anonymous User | The maximum number of sessions allowed per user. If a user has this many sessions and starts a new session, the user's oldest session is deleted.  
 Valid values: -1 (no limit), from 1 to any positive integer  
 Default value: 25 |
| Cache Timeout | The maximum time (in seconds) that a data cache can remain available, as measured from the end of each request for data in that cache.  
 Valid values: -1 (indicates no limit), 1 through 2007360 (24 days)  
 Default value: 1500 |
| Maximum Session Memory | The maximum amount of memory (in MB) that a single session can use.  
 Valid values: 0 (disable) through 4095.  
 Default value: 64 |
| **Memory Utilization** | **Allocation of memory on Access Database Service** |
| Maximum Private Bytes | The maximum number of private bytes (in MB) allocated by the Access Database Service process.  
 Valid values: -1 (the limit is set to 50% of physical memory on the computer), any positive integer  
 Default value: -1 |
| **Templates** | **Settings related to template management** |
| Maximum Template Size | The maximum size (in MB) allowed for Access Templates (ACCDT).  
 Valid values: -1 (no limit), from 1 to any positive integer  
 Default value: 30 |

See also

## See also

Concepts

#### Concepts

Set up and configure Access Services for Access apps in SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
