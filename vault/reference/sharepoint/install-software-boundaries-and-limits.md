---
title: "Software boundaries and limits for SharePoint 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: install-software-boundaries-and-limits
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/software-boundaries-and-limits
family: install
documentKind: "interactive-tutorial"
abstract: "Learn about tested performance and capacity limits of SharePoint Server and how the limits relate to acceptable performance."
---

# Software boundaries and limits for SharePoint 2013 - SharePoint Server

Note

Software boundaries and limits for SharePoint 2013

# Software boundaries and limits for SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article describes software boundaries and limits of SharePoint Server 2013, which include:

**Boundaries:** Static limits that can't be exceeded by design

**Thresholds:** Configurable limits that can be exceeded to accommodate specific requirements

**Supported limits:** Configurable limits that have been set by default to a tested value

Important

Some values in this article are based on test results from SharePoint 2010 Products and may not represent the final values for SharePoint Server 2013. This article will be updated with appropriate values as SharePoint Server 2013 test data becomes available. > For information about current hardware and software requirements, see Hardware and software requirements for SharePoint 2013.

Note

The capacity planning information in this document provides guidelines for you to use in your planning. It is based on testing performed at Microsoft, on live properties. However, your results are likely to vary based on the equipment you use and the features and functionality that you implement for your sites.

Learn about SharePoint limits in Microsoft 365.

Overview of boundaries and limits

## Overview of boundaries and limits

This article contains information to help you understand the tested performance and capacity limits of SharePoint Server 2013, and offers guidelines for how limits relate to acceptable performance. Use the information in this article to determine whether your planned deployment falls within acceptable performance and capacity limits, and to appropriately configure limits in your environment.

The test results and guidelines provided in this article apply to a single SharePoint Server 2013 farm. Adding servers to the installation might not increase the capacity limits of the objects that are listed in the tables in the Limits and boundaries section later in this article. On the other hand, adding server computers increases the throughput of a server farm, which might be necessary to achieve acceptable performance with many objects. In some cases, the requirements for high numbers of objects in a solution might require more servers in the farm.

There are many factors that can affect performance in a given environment, and each of these factors can affect performance in different areas. Some of the test results and recommendations in this article might be related to features or user operations that don't exist in your environment, and therefore don't apply to your solution. Only thorough testing can give you exact data related to your own environment.

Boundaries, thresholds, and supported limits

### Boundaries, thresholds, and supported limits

In SharePoint Server 2013, there are certain limits that are by design and can't be exceeded. Some other limits are set to default values that may be changed by the farm administrator. There are also certain limits that aren't represented by a configurable value, such as the number of site collections per web application.

Boundaries are absolute limits that can't be exceeded by design. It's important to understand these limits to ensure that you don't make incorrect assumptions when you design your farm.

An example of a boundary is the 2-GB document size limit; you can't configure SharePoint Server 2013 to store documents that are larger than 2 GB. This boundary is a built-in absolute value, and can't be exceeded by design.

A threshold is a parameter that has a default value that can't be exceeded unless the value is modified. Thresholds can, in certain circumstances, be exceeded to accommodate variances in your farm design. However, it's important to understand that exceeding threshold might affect the performance of the farm in addition to the effective value of other limits.

The default value of certain thresholds can only be exceeded up to an absolute maximum value. A good example is the document size limit. By default, the default document size threshold is set to 250 MB, but can be changed to support the maximum boundary of 2 GB.

Supported limits define the tested value for a given parameter. The default values for these limits were defined by testing, and represent the known limitations of the product. Exceeding supported limits may cause unexpected results, significant decrease in performance, or other harmful effects.

Some supported limits are configurable parameters that are set by default to the recommended value, while other supported limits relate to parameters that aren't represented by a configurable value.

An example of a supported limit is the number of site collections per farm. The supported limit is the largest number of site collections per web application that met performance benchmarks during testing.

It's important to know that many of the limit values that are provided in this document represent a point in a curve that describes an increasing resource load and concomitant decrease in performance as the value increases. Therefore, exceeding certain limits, such as the number of site collections per web application, may only result in a fractional decrease in farm performance. However, in most cases, operating at or near an established limit isn't a best practice, as acceptable performance and reliability targets are best achieved when a farm's design provides for a reasonable balance of limits values.

Thresholds and supported limits guidelines are determined by performance. In other words, you can exceed the default values of the limits, but as you increase the limit value, farm performance and the effective value of other limits may be affected. Many limits in SharePoint Server 2013 can be changed, but it's important to understand how changing a given limit affects other parts of the farm.

How limits are established

### How limits are established

In SharePoint Server 2013, thresholds and supported limits are established through testing and observation of farm behavior under increasing loads up to the point where farm services and operations reach their effective operational limits. Some farm services and components can support a higher load than others so that in some cases you must assign a limit value based on an average of several factors.

For example, observations of farm behavior under load when site collections are added indicate that certain features exhibit unacceptably high latency while other features are still operating within acceptable parameters. Therefore, the maximum value assigned to the number of site collections isn't absolute, but is calculated based on an expected set of usage characteristics in which overall farm performance would be acceptable at the given limit under most circumstances.

Obviously, if some services are operating under parameters that are higher than those parameters used for limits testing, the maximum effective limits of other services will be reduced. It's therefore important to execute rigorous capacity management and scale testing exercises for specific deployments in order to establish effective limits for that environment.

Note: We don't describe the hardware that was used to validate the limits in this document, because the limits were collected from multiple farms and environments.

The Pie Metaphor

#### The Pie Metaphor

In order to understand the relationship between hardware resources, load, and performance, it's important to have a way to visualize the factors involved and how they affect each other.

Consider the capacity of a farm as a pie, the size of which represents the aggregate of factors such as servers, hardware resources such as CPUs and RAM, storage capacity, disk IOPS, network bandwidth, and latency. The size of the pie is therefore related to the overall resources of the farm; adding resources (such as farm servers) increases the size of the pie.

This pie is divided into slices that represent load from various sources: user requests, search queries, operations against installed features, timer jobs, and operating system overhead. Each of these sections must share available farm resources. If the size of one slice increases, the size of others must decrease proportionally. Since load on a farm isn't static (user requests, for example, might only be significant during certain hours of the day), the relative size of the slices is constantly in flux. However, each slice must maintain a required minimum size to operate normally, and since the functions represented by each slice are interdependent, increasing the size of one slice may place more load on other slices in addition to reducing the resources available for them to consume.

Using this metaphor, the goal of the farm's design is to make the pie large enough to accommodate the required size of each pie slice under peak load.

Now, consider a scenario where user requests increase by 100% over baseline. Let's say that about half of the requests are search queries, and the other half editing lists and documents. This increased load squeezes the other pie slices, but some farm features must also work harder to compensate. The Search service has to process more queries, most of which are handled by the cache, but some queries are passed on to the database servers, increasing their load as well. If load on the database servers becomes too great, disk queue lengths increase, which in turn increases the latency of all other requests.

Limits and boundaries

## Limits and boundaries

This section lists the objects that can be a part of a solution and provides guidelines for acceptable performance for each kind of object. Acceptable performance means that the system as tested can support that number of objects, but that the number can't be exceeded without some decrease in performance or a reduction in the value of related limits. Objects are listed both by scope and by feature. Limits data is provided, together with notes that describe the conditions under which the limit is obtained and links to additional information where available.

Use the guidelines in this article to review your overall solution plans. If your solution plans exceed the recommended guidelines for one or more objects, take one or more of the following actions:

Evaluate the solution to ensure that compensations are made in other areas.

Flag these areas for testing and monitoring as you build your deployment.

Redesign or partition the solution to ensure that you don't exceed capacity guidelines.

Limits by hierarchy

### Limits by hierarchy

This section provides limits sorted by the logical hierarchy of a SharePoint Server 2013 farm.

Web application limits

#### Web application limits

The following table lists the recommended guidelines for web applications.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Web application | 20 per farm | Supported | We recommended limiting the number of web applications as much as possible. Create more host named site collections where possible instead of adding web applications. |
| Zone | 5 per web application | Boundary | The number of zones defined for a farm is hard-coded to 5. Zones include Default, Intranet, Extranet, Internet, and custom. |
| Managed path for host-named site collections | 20 per farm | Supported | Managed paths for host-named site collections apply at the farm level. Each managed path that is created can be applied in any Web application. |
| Managed path for path-based site collections | 20 per web application | Supported | Managed paths are cached on the web server, and CPU resources are used to process incoming requests against the managed path list.  
 Managed paths for path-based site collections apply at the Web application level. You can create a different set of managed paths for each Web application. Exceeding 20 managed paths per web application adds more load to the web server for each request.  
 If you plan to exceed 20 managed paths in a given web application, we recommend that you test for acceptable system performance. |
| Solution cache size | 300 MB per web application | Threshold | The solution cache allows the InfoPath Forms service to hold solutions in cache in order to speed up retrieval of the solutions. If the cache size is exceeded, solutions are retrieved from disk, which may slow down response times. You can configure the size of the solution cache by using the PowerShell cmdlet Set-SPInfoPathFormsService. For more information, see Set-SPInfoPathFormsService. |

Web server and application server limits

#### Web server and application server limits

The following table lists the recommended guidelines for web servers on the farm.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Application pools | 10 per web server | Threshold | The maximum number is determined by hardware capabilities.  
  This limit is dependent largely upon:  
  The amount of memory allocated to the web servers  
  The workload that the farm is serving, that is, the user base and the usage characteristics (a single highly active application pool can utilize 10 GB or more) |

Content database limits

#### Content database limits

The following table lists the recommended guidelines for content databases.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Number of content databases | 500 per farm | Supported | The maximum number of content databases per farm is 500. With 500 content databases per web application, end user operations such as opening the site or site collections aren't affected. But administrative operations such as creating a new site collection will experience decrease in performance. We recommend that you use PowerShell to manage the web application when a large number of content databases are present, because the management interface might become slow and difficult to navigate.  
 With 200 GB per content database, and 500 content databases per farm, SharePoint Server 2013 supports 100 TB of data per farm. |
| Content database size (general usage scenarios) | 200 GB per content database | Supported | We recommended limiting the size of content databases to 200 GB, except when the circumstances in the following rows in this table apply.  
 If you're using Remote BLOB Storage (RBS), the total volume of remote BLOB storage and metadata in the content database must not exceed the 200-GB limit. |
| Content database size (all usage scenarios) | 4 TB per content database | Supported | Content databases of up to 4 TB are supported when the following requirements are met:  
  Disk subsystem performance of 0.25 IOPs per GB, two IOPs per GB is recommended for optimal performance.  
  You must have developed plans for high availability, disaster recovery, future capacity, and performance testing.  
  Consider the following factors:  
  Requirements for backup and restore may not be met by the native SharePoint Server 2013 backup for content databases larger than 200 GB. Evaluate and test SharePoint Server 2013 backup and alternative backup solutions to determine the best solution for your specific environment.  
  It's recommended to have proactive skilled administrator management of the SharePoint Server 2013 and SQL Server installations.  
  The complexity of customizations and configurations on SharePoint Server 2013 may necessitate refactoring (or splitting) of data into multiple content databases. Seek advice from a skilled professional architect and perform testing to determine the optimum content database size for your implementation. Examples of complexity may include custom code deployments, use of more than 20 columns in property promotion, or features listed as not to be used in the over-4-TB section, below.  
  Refactoring of site collections allows for scale out of a SharePoint Server 2013 implementation across multiple content databases. This provision permits SharePoint Server 2013 implementations to scale indefinitely. This refactoring will be easier and faster when content databases are less than 200 GB.  
  It's suggested that for ease of backup and restore that individual site collections within a content database be limited to 100 GB. For more information, see Site collection limits. 
 IMPORTANT:  We don't recommend the use of content databases that exceed 4 TB, except in document archive scenarios (described in the next row in this table). If, in the future, you need to upgrade your SharePoint Server 2013 installation, upgrading the site collections within the content databases can be difficult and time consuming. >  It's recommended that you scale out across multiple content databases, rather than exceed 4 TB of data in a single content database. |
| Content database size (document archive scenario) | No explicit content database limit | Supported | Content databases with no explicit size limit for use in document archive scenarios are supported when the following requirements are met:  
  Fulfill all requirements from the "Content database size (all usage scenarios)" limit earlier in this table, and you should ensure that you have carefully considered all the factors discussed in the Notes field of that limit.  
  SharePoint Server 2013 sites must be based on **Document Center** or **Records Center** site templates.  
  Less than 5% of the content in the content database is accessed each month on average, and less than 1% of content is modified or written each month on average.  
  Don't use alerts, workflows, link fix-ups, or item level security on any SharePoint Server 2013 objects in the content database.  
 **Note:** Document archive content databases can be configured to accept documents from Content Routing workflows.  
  For more information about large-scale document repositories, see Estimate performance and capacity requirements for large scale document repositories in SharePoint Server 2010, and the Typical large-scale content management scenarios section of the article Enterprise content storage planning (SharePoint Server 2010). |
| Content database items | 60 million items including documents and list items | Supported | The largest number of items per content database that has been tested on SharePoint Server 2013 is 60 million items, including documents and list items. If you plan to store more than 60 million items in SharePoint Server 2013, you must deploy multiple content databases. |
| Site collections per content database | 10,000 maximum (2,500 non-Personal site collections and 7,500 Personal Sites, or 10,000 Personal Sites alone) | Supported | We recommended limiting the number of site collections in a content database to 5,000. However, up to 10,000 site collections in a database are supported. In a content database with up to 10,000 total site collections, a maximum of 2,500 of these collections can be non-Personal site collections. It's possible to support 10,000 Personal site collections if they're the only site collections within the content database.  
 These limits relate to speed of upgrade. The larger the number of site collections in a database, the slower the upgrade with respect to both database upgrade and site collection upgrades.  
 The limit on the number of site collections in a database is subordinate to the limit on the size of a content database that has more than one site collection. Therefore, as the number of site collections in a database increases, the average size of the site collections it contains must decrease.  
 Exceeding the 5,000 site collection limit puts you at risk of longer downtimes during upgrades. If you plan to exceed 5,000 site collections, we recommend that you have a clear upgrade strategy to address outage length and operations impact, and obtain extra hardware to speed up the software updates and upgrades that affect databases.  
 To set the warning and maximum levels for the number of sites in a content database, use the PowerShell cmdlet Set-SPContentDatabase with the -WarningSiteCount parameter. For more information, see [Set-SPContentDatabase]/powershell/module/sharepoint-server/Set-SPContentDatabase?view=sharepoint-ps&preserve-view=true). |
| Remote BLOB Storage (RBS) storage subsystem on Network Attached Storage (NAS) | Time to first byte of any response from the NAS should remain within 40 milliseconds 95% of the time. | Boundary | When SharePoint Server 2013 is configured to use RBS, and the BLOBs reside on NAS storage, consider the following supported limit.  
 From the time that SharePoint Server 2013 requests a BLOB, until it receives the first byte from the NAS, 95% of the time no more than 40 milliseconds can pass. |

Site collection limits

#### Site collection limits

The following table lists the recommended guidelines for site collections.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Site collections per farm | 750,000 per farm (500,000 rooted with the Personal Sites template and 250,000 rooted with other sites types) | Supported | The maximum recommended number of sites per farm is 500,000 site collections containing only one Personal Sites plus 250,000 site collections containing any other for all other site templates. The Sites can all reside on one web application, or can be distributed across multiple web applications.  
 This limit is affected by other factors that might reduce the effective number of site collections that can be supported by a given content database. Care must be exercised to avoid exceeding supported limits when a container object, such as a content database, contains a large number of other objects. For example, if a farm contains a smaller total number of content databases, each of which contains a large number of site collections, farm performance might be adversely affected long before the supported limit for the number of site collections is reached.  
 For example, Farm A contains a web application that has 200 content databases, a supported configuration. If each of these content databases contains 1,000 site collections, the total number of site collections in the web application will be 200,000, which falls within supported limits. However, if each content database contains 10,000 site collections, even though this number is supported for a content database, the total number of site collections in the farm will be 2,000,000, which exceeds the limit for the number of site collections per web application and per farm.  
 Memory usage on the web servers should be monitored, as memory usage is dependent on usage patterns and how many sites are being accessed in given timeframe. Similarly, the crawl targets might also exhibit memory pressure, and if so the application pool should be configured to recycle before available memory on any web server drops to less than 2 GB. |
| Web site | 250,000 per site collection / 250,000 per farm / 500,000 personal sites per farm. | Supported | The maximum recommended number of web sites is 500,000 sites based on the Personal Site template, and 250,000 sites based on all other templates. This limit applies per site collection and per farm.  
  Performance can degrade as the number of subsites surpasses 2,000 at the site collection level.  
 IMPORTANT:  Staying below 2,000 subsites per site collection is recommended. You can create a large total number of web sites by creating multiple site collections with up to 2,000 webs per site collection. For example, 125 site collections that contain 2,000 webs each equates to 250,000 sites in the farm. However, this threshold would be considered the maximum recommended limit for non-personal sites.  
  If you have 250,000 site collections, all containing a root web site that isn't the Personal Site template, adding a subsite to any of those root sites would exceed the 250,000 web site boundary.  
  If the recommended limit of 2,000 sites per site collection is exceeded, the following issues may occur:  
  Deleting or creating a site or subsite can significantly affect a site's availability. Access to the site and subsites will be limited while the site is being deleted. Attempting to create many subsites at the same time may also fail.  
  When having more than 2,000 subsites, the performance of actions such as executing PSConfig when adding a new server to an existing farm, or after installing SharePoint updates may drastically decrease.  
  Executing the **stsadm -o checklocalupgradestatus** operation, or the daily execution of the **Product Version Job** timer job may take many hours to complete.  
  Browsing the **Review database status** page (<your_SharePoint_CentralAdmin_URL>/_admin/UpgradeStatus.aspx) on the Central Administration web site may result in a timeout. |
| Site collection size | Maximum size of the content database | Supported | A site collection can be as large as the content database size limit for the applicable usage scenario. For more information about the different content database size limits for specific usage scenarios, see the Content database limits table in this article.  
  In general, we recommend limiting the size of site collections to 100 GB for the following reasons:  
  Certain site collection actions, such as site collection backup/restore or the PowerShell cmdlet Move-SPSite, cause large SQL Server operations that can affect performance or fail if other site collections are active in the same database. For more information, see Move-SPSite. 
 SharePoint site collection backup and restore is only supported for a maximum site collection size of 100 GB. For larger site collections, the complete content database must be backed up. If multiple site collections larger than 100 GB are contained in a single content database, backup and restore operations can take a long time and are at risk of failure. |
| Number of device channels per publishing site collection | 10 | Boundary | The maximum allowed number of device channels per publishing site collection is 10. |

List and library limits

#### List and library limits

The following table lists the recommended guidelines for lists and libraries. For more information, see Designing large Lists and maximizing list performance (SharePoint Server 2010).

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| List row size | 8,000 bytes per row | Boundary | Each list or library item can only occupy 8,000 bytes in total in the database. 300 bytes are reserved, leaving 7700 bytes for end-user columns. For details on how much space each kind of field consumes, see Column limits. |
| File size | 2 GB | Boundary | The default maximum file size is 250 MB. This boundary is a configurable limit that can be increased up to 2 GB (2,047 MB). However, a large volume of large files can affect farm performance. |
| Documents | 30,000,000 per library | Supported | You can create large document libraries by nesting folders, or using standard views and site hierarchy. This value may vary depending on how documents and folders are organized, and by the type and size of documents stored. |
| Major versions | 400,000 | Supported | If you exceed this limit, basic file operations—such as file open or save, delete, and viewing the version history— may not succeed.  
 This value is set on the library level for files. |
| Minor versions | 511 | Boundary | The maximum number of minor file versions is 511. This limit can't be exceeded.  
 This value is set on the library level for files. |
| Items | 30,000,000 per list | Supported | You can create large lists using standard views, site hierarchies, and metadata navigation. This value may vary depending on the number of columns in the list and the usage of the list. |
| Bulk operations | 100 items per bulk operation | Boundary | The user interface allows a maximum of 100 items to be selected for bulk operations. |
| List view lookup threshold | 12 join operations per query | Threshold | Specifies the maximum number of joins allowed per query, such as those values based on lookup, person/group, or workflow status columns. If the query uses more than eight joins, the operation is blocked. This condition doesn't apply to single item operations. When using the maximal view via the object model (by not specifying any view fields), SharePoint will return up to the first 12 lookups.  
 Note: After applying the SharePoint Server 2013 cumulative update package released on August 13, 2013 (https://support.microsoft.com/kb/2817616), the default value is increased from 8 to 12. |
| List view threshold | 5,000 | Threshold | Specifies the maximum number of list or library items that a database operation, such as a query, can process at the same time outside the daily time window set by the administrator during which queries are unrestricted. |
| List view threshold for auditors and administrators | 20,000 | Threshold | Specifies the maximum number of list or library items that a database operation, such as a query, can process at the same time when they're performed by an auditor or administrator with appropriate permissions. This setting works with Allow Object Model Override.  
 **Note**: This threshold must be enabled by using custom code to set the SPQueryThrottleOption. |
| Subsite | 2,000 per site view | Threshold | The interface for enumerating subsites of a given web site doesn't perform well as the number of subsites surpasses 2,000. Similarly, the All Site Content page and the Tree View Control performance will decrease significantly as the number of subsites grows. |
| Coauthoring in Word, PowerPoint and Excel for .docx, .pptx, .ppsx and .xlsx files | 10 concurrent editors per document | Threshold | Recommended maximum number of concurrent editors is 10. The boundary is 99.  
 If there are 99 co-authors who have a single document opened for concurrent editing, each successive user sees a "File in use" error, and can only open a read-only copy.  
 More than 10 co-editors will lead to a gradually degraded user experience with more conflicts, and users might have to go through more iterations to successfully upload their changes to the server. |
| Security scope | 50,000 per list | Threshold | The maximum number of unique security scopes set for a list can't exceed 50,000.  
 For most farms, we recommend that you consider lowering this limit to 5,000 unique scopes. For large lists, consider using a design that uses as few unique permissions as possible.  
 When the number of unique security scopes for a list exceeds the value of the list view threshold (set by default at 5,000 list items), more SQL Server round trips take place when the list is viewed, which can adversely affect list view performance.  
 A scope is the security boundary for a securable object and any of its children that don't have a separate security boundary defined. A scope contains an Access Control List (ACL), but unlike NTFS ACLs, a scope can include security principals that are specific to SharePoint Server 2013. The members of an ACL for a scope can include Windows users, user accounts other than Windows users (such as forms-based accounts), Active Directory groups, or SharePoint groups. |

Column limits

#### Column limits

SharePoint Server 2013 data is stored in SQL Server tables. Each column type has a size value listed in bytes. The sum of all columns in a SharePoint list can't exceed 8,000 bytes.

| **Limit** | **Maximum # columns** | **Limit type** | **Size per column** | **Notes** |
| --- | --- | --- | --- | --- |
| Single line of text | 255 | Threshold | 30 bytes |  |
| Multiple Lines of Text | 350 | Threshold | 22 bytes |  |
| Choice | 255 | Threshold | 30 bytes |  |
| Choice (multiple selections) | 350 | Threshold | 22 bytes |  |
| Number | 550 | Threshold | 14 bytes |  |
| Currency | 550 | Threshold | 14 bytes |  |
| Date and Time | 550 | Threshold | 14 bytes |  |
| Lookup | 750 | Threshold | 10 bytes |  |
| Yes / No | 1000 | Threshold | 7 bytes |  |
| Person or group | 750 | Threshold | 10 bytes |  |
| Hyperlink or picture | 127 | Threshold | 60 bytes |  |
| Calculated | 255 | Threshold | 30 bytes |  |
| GUID | 350 | Threshold | 22 bytes |  |
| Int | 750 | Threshold | 10 bytes |  |
| Managed metadata | 190 | Threshold | 60 bytes for the first, 40 bytes for each subsequent | The first Managed Metadata field added to a list is allocated four columns:  
  A lookup field for the actual tag  
  A hidden text field for the string value  
  A lookup field for the catch all  
  A lookup field for spillover of the catch all  
  Each subsequent Managed Metadata field added to a list adds two more columns:  
  A lookup field for the actual tag  
  A hidden text field for the string value |
| Geolocation | 2 | Threshold | 30 bytes |  |

External Data columns have the concept of a primary column and secondary columns. When you add an external data column, you can select some secondary fields of the external content type that you want to be added to the list. For example, given an External Content Type "Customer" that has fields like "ID," "Name," "Country," and "Description," when you add an External Data column of type "Customer" to a list, you can add secondary fields to show the "ID", "Name" and "Description" of the Customer. Overall, these columns are the ones that get added:

Primary column: A text field.

Hidden Id column: A multi-line text field.

Secondary columns: Each secondary column is a text/number/Boolean/multi-line text that is based on the data type of the secondary column as defined in the Business Data Catalog model. For example, ID might be mapped to a  *Number*  column; Name might be mapped to a  *Single line of text column; Description might be mapped to a  *Multiple lines of text*  column.

Page limits

#### Page limits

The following table lists the recommended guidelines for pages.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Web parts | 25 per wiki or Web Part page | Threshold | This figure is an estimate based on simple Web Parts. The complexity of the Web Parts dictates how many Web Parts can be used on a page before performance is affected. |

Security limits

#### Security limits

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Number of SharePoint groups a user can belong to | 5,000 | Supported | This type isn't a hard limit but it's consistent with Active Directory guidelines. There are several things that affect this number:  
  The size of the user token  
  The groups cache: SharePoint Server 2013 has a table that caches the number of groups a user belongs to as soon as those groups are used in access control lists (ACLs).  
  The security check time: as the number of groups that a user is a member of increases, the time that is required for the access check increases also. |
| Users in a site collection | 2 million per site collection | Supported | You can add millions of people to your web site by using Microsoft Windows security groups to manage security instead of using individual users.  
 This limit is based on manageability and ease of navigation in the user interface.  
 When you have many entries (security groups of users) in the site collection (more than 1,000), you should use PowerShell to manage users instead of the UI. This platform will provide a better management experience. |
| Active Directory Principles/Users in a SharePoint group | 5,000 per SharePoint group | Supported | SharePoint Server 2013 enables you to add users or Active Directory groups to a SharePoint group.  
  Having up to 5,000 users (or Active Directory groups or users) in a SharePoint group provides acceptable performance.  
  The activities most affected by this limit are as follows:  
  Fetching users to validate permissions. This operation takes incrementally longer with growth in number of users in a group.  
  Rendering the membership of the view. This operation will always require time. |
| SharePoint groups | 10,000 per site collection | Supported | Above 10,000 groups, the time to execute operations is increased significantly. This implication is especially true of adding a user to an existing group, creating a new group, and rendering group views. |
| Security principal: size of the Security Scope | 5,000 per Access Control List (ACL) | Supported | The size of the scope affects the data that is used for a security check calculation. This calculation occurs every time that the scope changes. There's no hard limit, but the bigger the scope, the longer the calculation takes. |

Limits by feature

### Limits by feature

This section lists limits sorted by feature.

Search limits

#### Search limits

The recommended guidelines for search are organized according to the aspects of search that they impact: the topology, the size of items, dictionaries, crawling, schema, queries and results, ranking, and the index.

Note

Limits for Search have changed significantly as the feature has been updated. For more information, see Plan search in SharePoint Server.

Search: topology limits

#### Search: topology limits

The topology limits ensure efficient communication between search components. Exceeding these limits slows down the communication between search components, which can result in longer query latencies and ultimately outage of search.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Analytics processing components | 6 per Search service application; 1 per server | Supported |  |
| Analytics reporting databases | 4 per Search service application | Threshold | You can exceed this limit to accommodate specific requirements. When scaling, add an analytics reporting database when the size of any of the deployed analytics databases reaches 250-GB total size, or 20-M total rows. This way repartitioning is as balanced as possible. |
| Link databases | 4 per Search service application | Supported | The highest tested number of items a link database can contain is 100 million. |
| Crawl components | 16 per Search service application; 1 per server | Supported |  |
| Index components | 60 per Search service application; 4 per server | Supported | To calculate the number of index components you have, multiply the number of index partitions with the number of index replicas.  
 For SharePoint Foundation 2013, this limit is one index component per Search service application and can't be exceeded. |
| Index partitions | 25 per Search service application | Supported | An index partition holds a subset of the Search service application index. Increasing the number of index partitions results in each partition holding a smaller subset of the index, reducing the RAM and disk space that is needed on the servers hosting the index components.  
 For SharePoint Foundation 2013, the maximum number of index components per Search service application is one, so the maximum number of index partitions per Search service application is limited to one. |
| Index replicas | 3 per index partition | Supported | Each index partition can have a set of replica. If you increase the number of index replicas, this change has a positive effect on the query performance and it provides better fault tolerance. But, if you add too many replicas to your index partition, this excess can adversely affect indexing.  
 For Internet sites scenarios, which typically have a high query rate but low content volume (less than 4 million items per partition), the supported limit is six index replicas per partition.  
 For SharePoint Foundation 2013, the maximum number of index components per Search service application is one, so the maximum number of index partitions per Search service application is limited to one. |
| Content-processing components | 1 per server | Supported | The search topology supports scaling out the number of content-processing components. Although a specific physical host or virtual machine does support multiple content-processing components, you achieve better usage of the CPU capacity by using one content-processing component. The reason is that a built-in mechanism maximizes CPU usage by adjusting the number of feeding sessions according to available CPU cores. Multiple feeding sessions allow the content-processing component to process incoming documents in parallel. This mechanism assumes a single content-processing component per host.  
 If the number of physical cores on the host equals N, then the content-processing component will have N*K feeding sessions. K is a constant coefficient with the initial value 3. A 4-core server will have 12 feeding sessions, which means that the content-processing component can process 12 documents in parallel. You can change the value of K by setting the **NumberOfCssFeedersPerCPUForRegularCrawl** property of the Search Service Application. SharePoint Server 2013 limits the value of N upward to 12, even if a server has more than 12 physical cores. Therefore a 16-core server will have N*K = 12 * 3 = 36 feeding sessions.  
 In the case that there still is idle CPU time, consider increasing the K coefficient instead of adding an extra content-processing component. If you increase the K coefficient, you must make sure that the host has sufficient available memory. |
| Query processing components | 1 per server | Supported | SharePoint Server 2013 only supports one query processing component per physical machine or virtual machine. |
| Search components | 64 per Search service application | Supported | This limit doesn't include crawl components. The sum of all the other search components must stay within this limit. |
| Search service applications | 20 per farm | Supported | Multiple Search service applications can be deployed on the same farm, because you can assign search components and databases to separate servers. This limit is lower than the limit for the total number of service applications in a farm. |
| Content sources | 500 per Search service application | Boundary | There's overhead associated with each content source, so we recommend that you create the smallest number of content sources that satisfy your other operational requirements, for example differences in crawl priority and scheduling. |

Search: item size limits

#### Search: item size limits

The item size limits safeguard crawling performance and the size of the index. Here are some examples of how the limits can affect searching:

If you can't get results when you search for an item, the item could be too large. A warning will show up in the Crawl Log, stating that the file exceeded the maximum size that the crawler can download.

If you search for text in an item and only get results from the first part of the text, the content-processing component may have truncated the item because it exceeded some of item size limits. When the content-processing component truncates an item, it indicates this truncation by setting the managed property IsPartiallyProcessed to True. A warning will also show up in the Crawl Log, stating why the item was truncated.

If you tune item size limits, we recommend that you work with them in the order they appear in this table.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Document size crawl component can download | 64 MB (3 MB for Excel documents) | Threshold | Search downloads meta data and content from a document until it reaches the maximum document size. The rest of the content isn't downloaded. Search always downloads a document's meta data.  
 You can change the default limit for the maximum document size. Do this change by using Microsoft PowerShell cmdlets to change the Search service application property **MaxDownLoadSize** or **MaxDownloadSizeExcel**. **MaxDownLoadSize** doesn't impact the maximum size for Excel documents. Enter the value in megabytes. The maximum value for the maximum document size is 1024 MB, also for Excel documents.  
 If you increase the limit for the maximum document size, search indexes more content and needs more disk space. |
| Parsed content size | 2 million characters | Boundary | Search stops parsing an item after it has parsed up to 2 million characters of content from it, including the item's attachments. The actual amount of parsed characters can be lower than this limit because search uses maximum 30 seconds on parsing a single item and its attachments. When search stops parsing an item, the item is marked as partially processed. Any unparsed content isn't processed and therefore isn't indexed. |
| Characters processed by the word breaker | 1,000,000 | Boundary | Search breaks content into individual words (tokens). The word breaker produces tokens from the first 1,000,000 characters of a single item, including the item's attachments. The actual number of processed characters can be lower than this limit because search uses maximum 30 seconds on word breaking. Any remaining content isn't processed and therefore isn't indexed. |
| Indexed managed property size | 512 KB per searchable/queryable managed property | Threshold | This threshold is the default value for the maximum size of a managed property that is set to either "searchable" or "queryable". You can configure this limit by using PowerShell cmdlets and the schema object model to set the **MP.MaxCharactersInPropertyStoreIndex** attribute. Enter the value in bytes. The maximum value for this maximum size is 2,097,152 bytes.  
 If you increase this limit, you enable indexing of more data per managed property. Indexing more data per managed property uses more disk space and increases the overall load on the search system. |
| Retrievable managed property size | 16 KB per managed property | Threshold | This threshold is the default value for the maximum size of a retrievable managed property. You can configure this limit per managed property by using PowerShell cmdlets and the schema object model to set the **P.MaxCharactersInPropertyStoreForRetrieval**attribute. Enter the value in bytes. The maximum value for this maximum size is 2,097,152 bytes.  
 If you increase this limit, you enable indexing of more data per managed property. Indexing and retrieving more data per managed property increases the overall load on the system and uses more disk space. |
| Sortable and refinable managed property size | 16 KB per managed property | Boundary | This boundary is the maximum size of a sortable and refinable managed property. |
| Token size | Variable | Boundary | Search can index tokens of any length. But the word breaker that search uses to produce tokens can limit the token length. Word breakers are language-aware components that break content into single words (tokens). You can also create custom word breakers. The token size limit therefore depends on the word breaker.  
  Here's the limit of the word breaker for western languages:  
  The word breaker only considers the first 1000 characters of a token for splitting, it ignores any remaining characters.  
  The word breaker splits tokens that are longer than 300 characters into two or more tokens where no token has more than 300 characters. For example, a 612 character token is split into two 300 character tokens and one 12 character token. |

Search: dictionary limits

#### Search: dictionary limits

The dictionary limits safeguard memory, content-processing efficiency, and query results.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Number of entries in a thesaurus | 1 million | Supported | The thesaurus contains synonyms for query terms. Exceeding this tested limit may result in increased use of memory and an increased query response time. |
| Number of entries in a custom entity extraction dictionary | 1 million | Supported | Exceeding this tested limit may result in increased use of memory, slower indexing, and an increased query response time. |
| Number of entries in a custom search dictionary | 5,000 terms per tenant | Boundary | This boundary limits the number of terms allowed for inclusions and exclusions dictionaries for query spelling correction and company extraction. You can store more terms than this limit in the Termstore, but search only uses 5000 terms per tenant. |

Search: schema limits

#### Search: schema limits

The schema limits safeguard memory resources and keep the management operation overhead at an acceptable level.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Crawled properties | 500,000 per Search service application | Supported | The contents and metadata of the items that you crawl are represented as crawled properties. You can map these crawled properties to managed properties. If the number of crawled properties exceeds this supported limit, this excess reduces indexing speed. |
| Managed properties | 50,000 per Search service application | Supported | Search uses managed propertied in queries. Crawled properties are mapped to managed properties. Exceeding the supported limit for managed properties reduces indexing speed. |
| Managed property mappings | 100 per managed property | Supported | Crawled properties can be mapped to managed properties. Exceeding this limit might decrease crawl speed and query performance. |
| Values per managed property | 1000 | Boundary | A managed property can have multiple values of the same type. This figure is the maximum number of values per managed multi-valued managed property per document. If this number is exceeded, the remaining values are discarded. |
| Metadata properties recognized | 100,000 per crawled item | Supported | This is the maximum number of metadata properties that the crawl component can determine when crawling an item. These metadata properties can be mapped or used for queries. Approaching this number of crawled properties might result in a low crawl rate. |

Search: crawl limits

#### Search: crawl limits

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Start addresses | 500 per content source | Supported |  |
| Length of machine host name | 15 characters | Threshold | NetBIOS limits the maximum machine host name length to this value. |
| Crawl databases | 15 per Search service application | Supported |  |

Search: query and result limits

#### Search: query and result limits

The limits for queries and results safeguard the search engine against executing large query expressions and returning large result sets. Preventing the search engine from executing large query expressions and returning large result sets prevents Denial-of-service (DoS) attacks and makes sure that results return timely. If you have to retrieve more results, we recommend that you use paging.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Text length for queries using Keyword Query Language | 4 KB (4,096 characters) | Supported | This value is the tested and default one for the maximum text length for a query built by using Keyword Query Language, except for Discovery queries. For Discovery queries 16 KB (16,384 characters) is the default maximum value.  
 The default value for the maximum text length can be increased up to the boundary of 20 KB (20,480) for all query types. |
| Number of rows in a result set | 500 rows | Supported | This value is the tested and default one for the maximum number of rows in a result set, except for a Discovery query. For Discovery queries 10,000 rows is the default value. To display the entire result set, issue more paging queries.  
 You can change the value for the maximum number of rows in a result set by using PowerShell cmdlets to change the Search service application property **MaxRowLimit**. **MaxRowLimit** defines the maximum value of the query property **RowLimit** and the Discovery query property **RowLimit**. **RowLimit** defines the number of rows each page contains in a result set. You can increase **MaxRowLimit** up to 10,000 rows, this is the supported boundary. |
| Results removal | No limit | Supported |  |
| Search alert quota | 100,000 alerts per Search service application | Supported | End-users can set search alerts for the result set of a query. When the results are changed or updated, search notifies the end-user. This is the tested limit for a Search service application that has a mix of end-user queries (75%) and alert queries (25%). The limit for a Search service application that has only alert queries is 400,000 alerts. These limits are based on a system with five queries per second (QPS). |

Search: ranking limits

#### Search: ranking limits

The ranking limits safeguard application server memory, query latency, and the size of the index.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Ranking models | 1,000 per tenant | Boundary | Approaching this limit can adversely affect the overall system performance. |
| Unique contexts used for ranking | 15 unique contexts per rank model | Boundary | This is the maximum number of unique contexts per rank model. |
| Authoritative pages | 1 top level and minimal second and third level pages per Search service application | Supported | Use as few second- and third-level pages as possible while still achieving the desired relevance.  
 The boundary is 200 authoritative pages per relevance level per Search service application. If you add more pages, you may not achieve the desired relevance. Add the key site to the first relevance level. Add more key sites at either second or third relevance levels, one at a time. Evaluate relevance after each addition to make sure that you have achieved the desired relevance effect. |

Search: index limits

#### Search: index limits

The index limits safeguard the index from growing out of bounds and exceeding the available resources.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Unique terms in the index | 2^31 (>2 billion terms) | Boundary | This is the maximum number of unique terms that can exist in the index of a Search service application. |
| User defined full text indexes | 10 | Boundary | This is the maximum number of full text indexes. |
| Indexed items | 10 million per index partition | Supported | Each index partition contains a subset of the whole search index. If the number of indexed items is high in relation to how much memory the server has, affects the query response time negatively.  
 For SharePoint Foundation 2013, the maximum number of indexed items is 2 million items per index partition.  
 For SharePoint Foundation 2013, the maximum number of indexed items is 2 million items per index partition, before applying the June 2016 Public Update. The June 2016 Public Update, increases this limit to 10 million items per index partition. |

User Profile Service limits

#### User Profile Service limits

The following table lists the recommended guidelines for User Profile Service.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| User profiles | 2,000,000 per service application | Supported | A user profile service application can support up to 2 million user profiles with full social features functionality. This number represents the number of profiles that can be imported into the people profile store from a directory service, and also the number of profiles a user profile service application can support without leading to performance decreases in social features. |
| Social tags, notes and ratings | 500,000,000 per social database | Supported | Up to 500 million total social tags, notes and ratings are supported in a social database without significant decreases in performance. However, database maintenance operations such as backup and restore may show decreased performance at that point. |

Content deployment limits

#### Content deployment limits

The following table lists the recommended guidelines for content deployment.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Content deployment jobs running on different paths | 20 | Supported | For concurrently running jobs on paths that are connected to site collections in the same source content database, there's an increased risk of deadlocks on the database. For jobs that must run concurrently, we recommend that you move the site collections into different source content databases.  
 Note: Concurrent running jobs on the same path aren't possible.           If you're using SQL Server snapshots for content deployment, each path creates a snapshot. This increases the I/O requirements for the source database.  
 For more information, see About deployment paths and jobs. |

Blog limits

#### Blog limits

The following table lists the recommended guidelines for blogs.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Blog posts | 5,000 per site | Supported | The maximum number of blog posts is 5,000 per site. |
| Comments | 1,000 per post | Supported | The maximum number of comments is 1,000 per post. |

Business Connectivity Services limits

#### Business Connectivity Services limits

The following table lists the recommended guidelines for Business Connectivity Services.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| ECT (in-memory) | 5,000 per web server (per tenant) | Boundary | Total number of external content type (ECT) definitions loaded in memory at a given point in time on a web server. |
| External system connections | 500 per web server | Boundary | Number of active/open external system connections at a given point in time. The default maximum value is 200; the boundary is 500. This limit is enforced at the web server scope, regardless of the kind of external system (for example, database, .NET assembly, and so on) The default maximum is used to restrict the number of connections. An application can specify a larger limit via execution context; the boundary enforces the maximum even for applications that don't respect the default. |
| Database items returned per request | 2,000 per database connector | Threshold | Number of items per request the database connector can return.  
 The default maximum of 2,000 is used by the database connector to restrict the number of result that can be returned per page. The application can specify a larger limit via execution context; the Absolute Max enforces the maximum even for applications that don't respect the default. The boundary for this limit is 1,000,000. |
| Response latency | 600 seconds | Threshold | Timeout used by the external data connector per request. The default value is 180 seconds, but applications can be configured to specify a larger value up to the maximum of 600 seconds. |
| Service response size | 150,000,000 bytes | Threshold | The upper volume of data per request the external data connector can return. The default value is 3,000,000 bytes, but applications can be configured to specify a larger value up to the maximum of 150,000,000 bytes. |
| Filter Descriptor (in-store) | 200 per ECT method | Boundary | The maximum number of Filter Descriptors per ECT method is 200. |
| ECT Identifier (in-store) | 20 per ECT | Boundary | The maximum number of identifiers per ECT is 20. |
| Database Item | 1,000,000 per request | Threshold | The default maximum number of items per request the database connector can return is 2,000, and the absolute maximum is 1,000,000.  
 The default max is used by the database connector to restrict the number of results that can be returned per page. The application can specify a larger limit via execution context; the absolute max enforces the allowed maximum even for applications that don't respect the default such as indexing. |

Workflow limits

#### Workflow limits

The following table lists the recommended guidelines for workflow.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Workflow postpone threshold | 15 | Threshold | 15 is the maximum number of workflows allowed to be executing against a content database at the same time, excluding instances that are running in the timer service. When this threshold is reached, new requests to activate workflows will be queued to be run by the workflow timer service later. As non-timer execution is completed, new requests will count against this threshold. This is limit can be configured by using the Set-SPFarmConfig PowerShell cmdlet. For more information, see Set-SPFarmConfig.  
 Note: This limit doesn't refer to the total number of workflow instances that can be in progress. Instead, it's the number of instances that are being processed. Increasing this limit increases the throughput of starting and completing workflow tasks but also increases load against the content database and system resources. |
| Workflow timer batch size | 100 | Threshold | The number of events that each run of the workflow timer job will collect and deliver to workflows. It's configurable by using PowerShell. To allow for additional events, you can run additional instances of the SharePoint Foundation Workflow Timer Service. |
| Workflow associations | 100 per list | Supported | Exceeding this limit will degrade browser performance due to the large volume of data that is loaded for more than 100 associations and their status columns. |
| List items or documents that can be bulk created or uploaded to start workflow instances | 5,000 items | Supported | Testing has verified that all workflow activation events are processed for an on-item-creation workflow association when up to 5,000 items are created in a single bulk upload. Exceeding this limit could cause workflow initiation to time out. |
| Published workflow definitions per web site | 1,000 per web site | Supported | The maximum supported number of published workflow definitions per web site is 1,000. |
| Total workflow associations per site | 1,799 per site | Boundary | The Service Bus supports a maximum of 1,799 subscriptions per scope. This maximum value includes the sum of both published and unpublished associations. |
| Maximum workflow definition (xaml) size | 5,120 KB | Boundary | Attempts to publish xaml files that exceed the size limit will fail. |
| Maximum depth of a workflow sub-step in xaml (workflow complexity) | 121 levels | Boundary | There's a hard limit of 125 for node depth in xaml. The maximum value of 121 levels accounts for the default activities (stage, sequence, etc.) that SharePoint Designer inserts automatically. |
| Workflow instance activations per second per web server | 6 per second | Boundary | Testing has confirmed that a SharePoint web server can activate a maximum of 6 workflow instances per second. This number is cumulative, and therefore scales with the number of web servers in the farm. For example, 2 web servers can activate 12 workflow instances per second, and 3 web servers can activate 18. |
| Rest calls from SharePoint workflow per second per web server | 60 per second | Supported | Testing has confirmed that a SharePoint web server can effectively process up to 60 rest calls per second from SharePoint workflow. If this level of volume will be exceeded, we recommend that an additional load-balanced web server be added to the SharePoint farm. In testing, 120 rest calls per second against a single web server resulted in sustained 90-100% CPU utilization. Adding a second web server reduced CPU utilization to 30-40% on both servers. Adding a third web server enabled processing of 180 calls per second, with 30-40% CPU utilization on all three servers, and so on. The servers used for this test were Hyper-V virtual machines with 16 core processor and 24 GBs RAM each. |
| Workflow variable value size | 256 KB | Boundary | The maximum amount of data that can be stored in a single workflow variable is 256 KB. Exceeding this limit will cause the workflow instance to terminate. |
| Maximum list size for workflow lookups to non-indexed fields | 5,000 items per list view | Threshold | This limit is a result of the maximum view size limit. When this limit is exceeded, workflow lookups to non-indexed fields will fail for non-administrative users. At this threshold, an index must be created for the field, in order for workflows to be able to successfully perform lookups against the field. |
| Maximum list size for auto-start workflow associations | 10 million items per list | Supported | Testing has confirmed that the performance of auto-start workflow associations isn't affected when list size grows to 1 million items. Because response time doesn't change as list size scales, the effective limit is the same as the maximum number of items in a non-workflow list. |

Managed Metadata limits

#### Managed Metadata limits

The following table lists the recommended guidelines for managed metadata configuration.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Number of folders with location-based defaults | 1,000 folders per site, or data file size of 256 Mb | Boundary | Location-based default metadata allows you to set default values for list columns per folder. You can only apply location-based default values on up to 1,000 folders per site, or up to the point at which the data file in which location-based default metadata is stored for the site (client_LocationBasedDefaults.html) reaches 265 Mb.  
 When the number of folders in the data file exceeds 1,000, or the data file size exceeds 256 Mb, default values added for additional folders will be ignored. |
| Number of links in or file size of a document that are updated when the target location changes | 1,000 links or file size of 256 Mb per document | Boundary | When a document containing links is added to a folder, SharePoint Foundation 2013 will update links automatically when the link target is moved to a new location. In a document with more than 1,000 links, or a document with a file size that exceeds 256 Mb, the document is treated as though it contains no links, and updates to link targets are ignored for the entire document. |

Managed Metadata term store (database) limits

#### Managed Metadata term store (database) limits

The following table lists the recommended guidelines for managed metadata term stores.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Maximum number of levels of nested terms in a term store | 7 | Supported | Terms in a term set can be represented hierarchically. A term set can have up to seven levels of terms (a parent term, and six levels of nesting below it.) |
| Maximum number of term sets in a term store | 1,000 | Supported | You can have up to 1,000 term sets in a term store.  
 Note: Both local term set and global term set follow the limit of 30,000 terms per term site. Use global term sets to store the reusable data for all site collections, instead of using a large amount of site collection term sets or creating a new Managed Metadata service. A web application can have connections to multiple services. |
| Maximum number of terms in a term set | 30,000 | Supported | 30,000 is the maximum number of terms in a term set.  
 Note: Additional labels for the same term, such as synonyms and translations, don't count as separate terms. |
| Total number of items in a term store | 1,000,000 | Supported | An item is either a term or a term set. The sum of the number of terms and term sets can't exceed 1,000,000. Additional labels for the same term, such as synonyms and translations, don't count as separate terms.  
 Note: You can't have both the maximum number of term sets and the maximum number of terms simultaneously in a term store. |
| Number of Variation Labels | 209 per term store | Supported | The maximum number of Variation Labels per term store is 209. |
| Number of terms in managed navigation term set | 2,000 | Supported | The maximum supported number of terms in a managed navigation term set is 2,000. |

See also Overview of Managed Metadata service in SharePoint 2013 and The impact of having multiple Managed Metadata services per farm

Visio Services limits

#### Visio Services limits

The following table lists the recommended guidelines for instances of Visio Services in SharePoint.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| File size of Visio web drawings | 50 MB | Threshold | Visio Services has a configuration setting that enables the administrator to change the maximum size of web drawings that Visio processes.  
  Larger file sizes have the following side effects:  
  Increase in the memory footprint of Visio Services.  
  Increase in CPU usage.  
  Reduction in application server requests per second.  
  Increase overall latency.  
  Increase SharePoint farm network load |
| Visio web drawing recalculation time-out | 120 seconds | Threshold | Visio Services has a configuration setting that enables the administrator to change the maximum time that it can spend recalculating a drawing after a data refresh.  
  A larger recalculation time-out leads to:  
  Reduction in CPU and memory availability.  
  Reduction in application requests per second.  
  Increase in average latency across all documents.  
  A smaller recalculation time-out leads to:  
  Reduction of the complexity of diagrams that can be displayed.  
  Increase in requests per second.  
  Decrease in average latency across all documents. |
| Visio Services minimum cache age (data connected diagrams) | Minimum cache age: 0 to 24 hrs | Threshold | Minimum cache age applies to data connected diagrams. It determines the earliest point at which the current diagram can be removed from cache.  
 Setting Min Cache Age to a very low value will reduce throughput and increase latency, because invalidating the cache too often forces Visio to recalculate often and reduces CPU and memory availability. |
| Visio Services maximum cache age (non-data connected diagrams) | Maximum cache age: 0 to 24 hrs | Threshold | Maximum cache age applies to non-data connected diagrams. This value determines how long to keep the current diagram in memory.  
 Increasing Max Cache Age decreases latency for commonly requested drawings.  
 However, setting Max Cache Age to a very high value increases latency and slows throughput for items that aren't cached, because the items already in cache consume and reduce available memory. |

SharePoint Web Analytics service limits

#### SharePoint Web Analytics service limits

The SharePoint Web Analytics service has been deprecated in SharePoint Server 2013.

PerformancePoint Services limits

#### PerformancePoint Services limits

The following table lists the recommended guidelines for PerformancePoint Services in SharePoint.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Cells | 1,000,000 per query on Excel Services data source | Boundary | A PerformancePoint scorecard that calls an Excel Services data source is subject to a limit of no more than 1,000,000 cells per query. |
| Columns and rows | 15 columns by 60,000 rows | Threshold | The maximum number of columns and rows when rendering any PerformancePoint dashboard object that uses a Excel workbook as a data source. The number of rows could change based on the number of columns. |
| Query on a SharePoint list | 15 columns by 5,000 rows | Supported | The maximum number of columns and row when rendering any PerformancePoint dashboard object that uses a SharePoint list as a data source. The number of rows could change based on the number of columns. |
| Query on a SQL Server data source | 15 columns by 20,000 rows | Supported | The maximum number of columns and row when rendering any PerformancePoint dashboard object that uses a SQL Server table data source. The number of rows could change based on the number of columns. |

Word Automation Services limits

#### Word Automation Services limits

The following table lists the recommended guidelines for Word Automation Services.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Input file Size | 512 MB | Boundary | Maximum file size that can be processed by Word Automation Services. |
| Frequency with which to start conversions (minutes) | 1 minute (recommended)  
 15 minutes (default)  
 59 minutes (boundary) | Threshold | This setting determines how often the Word Automation Services timer job executes. A lower number leads to the timer job running faster. Our testing shows that it's most useful to run this timer job once per minute. |
| Number of conversions to start per conversion process | For PDF/XPS output formats: 30 x MFor all other output formats: 72 x M Where M is the value of Frequency with which to start conversions (minutes) | Threshold | The number of conversions to start affects the throughput of Word Automation Services.  
 If these values are set higher than the recommended levels, then some conversion items may start to fail intermittently, and user permissions may expire. User permissions expire 24 hours from the time that a conversion job is started. |
| Conversion job size | 100,000 conversion items | Supported | A conversion job includes one or more conversion items, each of which represents a single conversion to be performed on a single input file in SharePoint. When a conversion job is started (using the ConversionJob.Start method), the conversion job and all conversion items are transmitted over to an application server which then stores the job in the Word Automation Services database. A large number of conversion items increase both the execution time of the Start method and the number of bytes transmitted to the application server. |
| Total active conversion processes | N-1, where N is the number of cores on each application server | Threshold | An active conversion process can consume a single processing core. Therefore, customers should not run more conversion processes than they have processing cores in their application servers. The conversion timer job and other SharePoint activities also require occasional use of a processing core.  
 We recommend that you always leave 1 core free for use by the conversion timer job and SharePoint. |
| Word Automation Services database size | 2 million conversion items | Supported | Word Automation Services maintains a persistent queue of conversion items in its database. Each conversion request generates one or more records.  
 Word Automation Services doesn't delete records from the database automatically, so the database can grow indefinitely without maintenance. Administrators can manually remove conversion job history by using the PowerShell cmdlet Remove-SPWordConversionServiceJobHistory. For more information, see Remove-SPWordConversionServiceJobHistory. |

Excel Services limits

#### Excel Services limits

The following table lists the recommended guidelines for Excel Services in SharePoint.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Maximum workbook size | 10 MB | Supported | The maximum size of a workbook that can be opened in Excel Services is 10 megabytes. |

Machine Translation Service limits

#### Machine Translation Service limits

The following table lists the recommended guidelines for the Machine Translation Service.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Input file size for binary files | 524,288 KB per file | Threshold | Files larger than the limit take too long to transfer and process, decreasing the throughput of the service. |
| Input file size for text files | 15,360 KB per file | Threshold | Files larger than the limit have too much text to translate, decreasing the throughput of the service. |
| Maximum character count for Microsoft Word Documents | 10,000,000 per document | Threshold | Documents with more characters than the limit have too much text to translate, decreasing the throughput of the service. |
| Total concurrent translation processes | 5 | Threshold | Using more processes than the limit doesn't increase throughput because there's a limit to how much text can be translated at a time. Using more processes increases the demands on the server resources. |
| Delay between translations | 59 minutes | Threshold | Starting translations at a larger interval than the limit causes the time taken to translate documents to grow too large and can cause the number of queued translations to grow too large. |
| Number of translations per translation process | 1,000 per process | Threshold | Starting more translations than the limit causes translations to fail due to timing out because they can't be processed before the timeout period. |
| Maximum concurrent translation requests | 300 | Threshold | More than 300 concurrent translation requests could cause translations to time out because requests are queued for longer than the timeout period. |
| Files per translation job | 100,000 files | Supported | Submitting jobs with a number of files that exceeds the limit causes job submittal time and processing time to be too long. |
| Machine Translation Service database size | 1,000,000 files | Supported | Operations to maintain the queue of jobs become slow if the database grows beyond the maximum number of files in the database. |

Office Web Application Service limits

#### Office Web Application Service limits

The following table lists the recommended guidelines for Office Online. Office client application limits also apply when an application is running as a web app.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Cache size | 100 GB | Threshold | Space available to render documents, created as part of a content database. By default, the cache available to render documents is 100 GB. We don't recommend that you increase the available cache. |
| Renders | One per document per second per CPU core per application server (maximum eight cores) | Boundary | This is the measured average number of renders that can be performed of "typical" documents on the application server over a period of time. |
| OneNote concurrent merge operations | 8 per document | Threshold | OneNote merges combine changes from multiple users who are co-authoring a notebook. If too many concurrent merges are already in progress, a conflict page is generated instead, which forces the user to perform the merge manually. |

Project Server limits

#### Project Server limits

The following table lists the recommended guidelines for Project Server. For more information about how to plan for Project Server, see Planning and architecture for Project Server 2010.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| End of project time | Date: 12/31/2149 | Boundary | Project plans can't extend past the date 12/31/2149. |
| Deliverables per project plan | 1,500 deliverables | Boundary | Project plans can't contain more than 1,500 deliverables. |
| Number of fields in a view | 256 | Boundary | A user can't have more than 256 fields added to a view that they have defined in Project Web App. |
| Number of clauses in a filter for a view | 50 | Boundary | A user can't add a filter to a view that has more than 50 clauses in it. |

SharePoint Apps limits

#### SharePoint Apps limits

The following table lists the recommended guidelines for apps for SharePoint.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Maximum Access/SharePoint App Package size | 100 Mb | Boundary | 100 MB is the limit for an app package created in the Access client.  
 Note: Access compresses the database when it creates the app package, so the app package may include more than 100 MB of data. |
| Maximum Access app database storage size in SQL Azure | 1 Gb | Boundary | Each Access app created on SharePoint creates a database on SQL Azure. 1 GB is the limit for the database storage on SQL Azure. In an on-premises installation, the administrator controls the size of the associated SQL database. |
| Apps displayed in Manage Licenses page | 2,000 | Boundary | Up to 2,000 apps (purchased from the store) can be displayed on the Manage Licenses page. You can still manage the license of any app by going to the All Site Contents page of the site where the app is installed and clicking on Licenses, or by searching for the app using Marketplace Search. |
| Number of app licenses per tenant | 1,000,000 | Supported | The maximum supported number of licenses (purchase of apps from the store) for a single SharePoint deployment, either on-premises or SharePoint in Microsoft 365. Exceeding this limit might cause severe performance degradation. |
| Number of apps displayed in the Add an App page | 240 | Boundary | After this limit is reached, only the first 240 apps are displayed, and a message guiding you to search to find your app is displayed. |
| Number of managers per app license | 30 | Boundary | Only 30 people can manage a license. License managers can add or remove users or delete a license. |
| Number of app licenses assigned to a user viewable by that user | 2,000 | Boundary | When more than 2,000 licenses are assigned to a user, that user will no longer see any apps in the default Add an App view. Instead, a message guiding you to search the app catalog or the SharePoint Store will appear. |
| Number of apps in the corporate catalog viewable by a single user | 500 | Boundary | When more than 500 apps from the corporate catalog are available to a single user, that user will no longer see any apps in the default Add an App view. Instead, a message guiding you to search the app catalog or the SharePoint Store will appear. |

Distributed cache service limits

#### Distributed cache service limits

The following table lists the recommended guidelines for the distributed cache service.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Number of followable entities (users, documents, sites and hashtags) per cache host | 400,000 | Supported | The total number of entities that can be followed by a single user on a distributed cache host with 16 GB RAM assigned to the distributed cache service is 400,000. |
| Number of cache hosts in a cluster | 16 | Boundary | The total number of cache hosts a single distributed cache cluster can support is 16. |
| Maximum amount of memory dedicated to a cache host | 16 GB | Boundary | The total amount of memory that can be dedicated to the distributed cache service on any one cache host in a cluster is 16 GB. |

Miscellaneous limits

#### Miscellaneous limits

The following table lists limits and recommended guidelines for services and features not covered in other sections.

| **Limit** | **Maximum value** | **Limit type** | **Notes** |
| --- | --- | --- | --- |
| Number of User agent substrings per device channel | 150 | Boundary | The maximum number of user agent substrings per mobile device channel is 150. |
| Number of SharePoint sources per EDiscovery case | 100 | Boundary | The maximum number of SharePoint sources that can be added to an EDiscovery case is 100. |
| Number of Exchange sources (mailboxes) per EDiscovery case | 1,500 | Boundary | The maximum number of Exchange sources (mailboxes) per EDiscovery case is 1,500. |
| Maximum size of EDiscovery Query | 16K characters or 500 keywords | Boundary | The size of an EDiscovery query is limited to 500 keywords or 16,000 characters, whichever is reached first. |

Related articles

## Related articles

Hardware and software requirements for SharePoint 2013

Performance planning in SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
