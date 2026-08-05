---
title: "Default timer jobs in SharePoint Server 2016 - SharePoint Server"
description: "Learn about the default timer jobs in SharePoint Server."
ms.topic: reference
---
Note

Default timer jobs in SharePoint Server 2016

# Default timer jobs in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Default timer jobs

## Default timer jobs

The following table lists the default timer jobs for SharePoint Server 2016.

| **Timer job** | **Description** | **Default schedule** |
| --- | --- | --- |
| Access Services monitor | Monitors the connectivity of Access Services on SharePoint and SQL Azure. | 5 minutes |
| Access Services provider for SQL connection statistics (SQL Azure only) | Provides the statistics on connections to SQL for Access Services (SQL Azure only). | Daily |
| Access Services provider for SQL Event Log (SQL Azure only) | Gathers the SQL Server Event Log for Access Services (SQL Azure only). | Daily |
| App installation service | Installs and uninstalls apps. | 5 minutes |
| App state update | Retrieves and applies updated information on apps from the SharePoint Store. It includes the availability of updates and information about disabled apps. | Hourly |
| Application addresses refresh | Synchronizes connection information for remote service applications. | 15 minutes |
| Application server administration service | Manages shared service instances that may perform highly privileged operations. Requires that the SharePoint Administration service is running. The Search service instance is managed by this job on deployments other than stand-alone server deployments. | 1 minute |
| Application server | Manages shared service instances that do not perform highly privileged operations. The Search service instance is managed by this job on stand-alone server deployments. | 1 minute |
| Audit log trimming | Trims audit trail entries from site collections. | Monthly |
| Autohosted app instance counter | Counts the number of autohosted app instances per site subscription. | Weekly |
| Bulk workflow task processing | Processes bulk workflow task completion. | Daily |
| CEIP data collection | Collects farm data for the Customer Experience Improvement Program. | Daily |
| Cell storage data cleanup | Deletes temporary cell storage data and frees SQL Server disk space. | 15 minutes |
| Change log | Records many types of changes that you make to SharePoint sites. Removes expired entries from the change log of the web application. | Weekly |
| Compliance Dar Processing | Processes data at rest compliance tasks. | 10 minutes |
| Compliance Dar task house keeping | Cleans up completed and failed data at rest compliance tasks. | Daily |
| Compliance high priority policy processing | Processes high priority data at rest compliance tasks. | 15 minutes |
| Compliance Policy Processing | Processes compliance policies as defined in Policy Center and invokes appropriate actions on items. | Daily |
| Content organizer processing | Processes documents in the drop-off library that match organizing rules. | Daily |
| Content type hub | Tracks content type log maintenance and manages unpublished content types. | Daily |
| Content type subscriber | Retrieves content type packages from the hub and applies them to the local content type gallery. | Hourly |
| Database Performance Metric Provider |  | 1 minute |
| Database wait statistics | Periodically gathers database wait statistics. | Hourly |
| Dead site delete | When auto site cleanup is enabled, sites that are not used in a certain period of time are deleted. | Weekly |
| Deferred access control list update | Applies updates to access control lists (ACLs) resulting from broad security changes. | 1 minute |
| Delete job history | Deletes old entries from the timer job history. | Daily |
| Delete upgrade evaluation site collections | Deletes upgrade evaluation site collections that are past their expiry date and sends notifications to those that are near expiry date. | Daily |
| Diagnostic data provider: app usage | Periodically collects App statistics. | Daily |
| Diagnostic data provider: Event Log | Collects Windows Event Log entries | 1 minute |
| Diagnostic data provider: IO Intensive SQL Queries | Collects a SQL trace of IO intensive SQL queries | 1 minute |
| Diagnostic data provider: Per-database IO | Collects IOs for each database file | 2 minutes |
| Diagnostic data provider: Performance Counters - Database Servers | Collects Performance Monitor Counters data on database servers.  
 **Important:** 
 The timer service account must have enough permissions to collect counters on the database server. It should at least be a member of Performance Monitor Users. | 1 minute |
| Diagnostic data provider: Performance Counters - Web Front Ends | Collects Performance Monitor Counters data on web front ends. | 1 minute |
| Diagnostic data provider: Site Size |  |  |
| Diagnostic data provider: SQL Blocking Queries |  | N/A |
| Diagnostic data provider: SQL Blocking Reports |  | 1 minute |
| Diagnostic data provider: SQL Deadlocks |  | 1 minute |
| Diagnostic data provider: SQL DMV |  | 30 minutes |
| Diagnostic data provider: SQL Memory DMV | Collects SQL Dynamic Management Views (DMV) data. | N/A |
| Diagnostic data provider: Trace Log | Collects trace log entries and stores the usage data in the logging database. |  |
| Disk over quota warning | Sends out disk over quota warning email notifications. | Daily |
| Disk quota warning | Looks for sites that have exceeded the storage quota, and sends out disk quota warning email notifications. | Weekly |
| Document changed anti-virus processing | NA | Hourly |
| Document full crawl anti-virus processing | NA | Hourly |
| Document ID assignment | Work item that assigns document ID to all items in the site collection. | Daily |
| Document ID enable/disable | Work item that propagates content type changes across all sites when the Document ID feature is reconfigured. | Daily |
| Document Set fields synchronization | Synchronizes metadata from the document set to the items inside the document library. | 15 minutes |
| Document Set template update | Propagates changes that are made to the document set template to the existing items. | Hourly |
| eDiscovery in-place hold processing | The in-place hold timer job starts and releases the holds of SharePoint websites. | Hourly |
| Enterprise Metadata site data update | Updates all site collections after a language pack addition or an Enterprise Metadata service application restore. | Hourly |
| Expiration policy | Enumerates list items and looks for those with an expiration date that has already occurred. For those items, runs disposition processing. Disposition processing most often results in deleting items. But it can perform other actions, such as processing disposition workflows. | Weekly |
| Extension map refresh | Checks for changes in the extension map data. | 1 minute |
| File post processor | Processes the files asynchronously after the file has been saved. The processing includes extraction of the file-specific metadata and generation of default thumbnails. | 1 minute |
| Fix site storage metrics | Fixes site storage metrics. | Hourly |
| Gradual site delete | Deletes all the data from the host content database for all deleted site collections. | Hourly |
| Health analysis (Daily, Central Administration, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Central Administration web application and the Usage and Health Data Collection service application. | Daily |
| Health analysis (Daily, Central Administration, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the Central Administration web application and the Usage and Health Data Collection service application. | Daily |
| Health analysis (Daily, Machine Translation service, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Machine Translation service application and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Machine Translation service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the Machine Translation service application and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Microsoft SharePoint Foundation Timer, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Microsoft SharePoint Foundation Timer, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Daily, Microsoft SharePoint Foundation web application, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run SharePoint web applications and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Daily, Microsoft SharePoint Foundation web application, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs SharePoint web applications and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, User Profile service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service application and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Visio Graphics service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs Visio Services in SharePoint Server 2016 and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Word Automation Services, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run Word Automation Services and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Hourly, distributed cache, all servers) | Runs SharePoint Health Analyzer jobs on all servers that run the Distributed Cache service. | Hourly |
| Health Analysis (Hourly, Microsoft SharePoint Foundation Timer, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Hourly, Microsoft SharePoint Foundation Timer, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Hourly, Security Token Service, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Security Token Service (STS) and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Hourly, User Profile service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Hourly, Word Automation Services, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs Word Automation Services and the Usage and Health Data Collection service application. | Hourly |
| Health Analysis (Monthly, Microsoft SharePoint Foundation Timer, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application. | Monthly |
| Health Analysis (Monthly, User Profile Service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile Service and the Usage and Health Data Collection service application. | Monthly |
| Health Analysis (Weekly, Central Administration, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Central Administration website and the Usage and Health Data Collection service application. | Weekly |
| Health Analysis (Weekly, Microsoft SharePoint Foundation Timer, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application. | Weekly |
| Health Analysis (Weekly, Microsoft SharePoint Foundation Timer, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application. | Weekly |
| Health Analysis (Weekly, Microsoft SharePoint Foundation web application, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run SharePoint web applications and the Usage and Health Data Collection service application. | Weekly |
| Health Analysis (Weekly, User Profile service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service and the Usage and Health Data Collection service application. | Weekly |
| Hold processing and reporting | Generates a hold report by enumerating items in a hold and updating them to remove them from hold, as appropriate. | Daily |
| Immediate Alerts | Sends out immediate and scheduled alerts. | 5 minutes |
| InfoPath Forms Services maintenance | Performs maintenance operations on administrator-approved InfoPath Forms Services form templates across all front-end Web servers. | Daily |
| Information management policy | Performs background processing for information policies, such as calculating updated expiration dates for items with a new retention policy. | Weekly |
| Internal app state update | Retrieves and applies updated information on apps from App Catalogs. | Hourly |
| Large list automatic column index management | Automatically manage list column indices for large lists. | Daily |
| License renewal | Renews all licenses of the apps from the SharePoint Store. | Hourly |
| Licensing synchronizer | Synchronizes trial expiration time licensing information to the configuration database. | Hourly |
| Machine Translation Service - Language Support | Updates the languages available to the Machine Translation Service. | Weekly |
| Machine Translation Service - Machine Translation Service | Initiates translation of documents that were submitted to the Machine Translation Service for asynchronous translation. | 15 minutes |
| Machine Translation Service - Remove Job History | Removes the history for expired jobs from the Machine Translation Service queue database. | Weekly |
| Microsoft SharePoint Foundation Usage Data Import | Imports usage log files into the event store. | 5 minutes |
| Microsoft SharePoint Foundation Usage Data Maintenance | Performs maintenance in the logging database. | Hourly |
| Microsoft SharePoint Foundation Usage Data Processing | Checks for expired usage data at the farm level and deletes the data. Expired usage data consists of records in the central usage data collection database that are older than 30 days. | Daily |
| Migration | Background migration task. | 1 minute |
| My Site cleanup | Starts a workflow on a deleted user's My Site. The default behavior is to send an email message to the manager with a link to the deleted user's site. The email message contains a request to the manager to move any documents or data that the manager wants to preserve, because the site might be deleted in the future. | Daily |
| My Site host automatic upgrade | Automatically upgrading for the My Site host. | Daily |
| My Site instantiation interactive request queue | A timer job queue for interactive (web initiated) My Site instantiation requests. | 1 minute |
| My Site instantiation non-interactive request queue | A timer job queue for non-interactive (Office-client initiated) My Site instantiation requests. | 1 minute |
| My Site second instantiation interactive request queue | A second timer job queue for interactive (web initiated) My Site instantiation requests. | 1 minute |
| My Sites automatic upgrade | Automatically upgrading for the My Sites. | Daily |
| Notification | Queries and updates the notification list and sends out pending scheduling notifications. | Daily |
| Over quota notification requests queue | Queue for site over quota email notification requests. | Hourly |
| Password management | Sends email and logs events for expiring passwords and password changes. This timer job helps ensure that managed passwords are changed before they expire. | Daily |
| Performance Metric Provider | This diagnostic data provider collects the per metrics data. | 1 minute |
| Persisted navigation term set synchronization | Synchronizes the persisted copy of navigation term sets. | Hourly |
| Product version | Checks the installation status of the computer and adds that data to the database. | Daily |
| Project Server: Active Directory Sync for Project Server service application | Synchronizes Active Directory with Project Web App enterprise resource pools and security groups. | Daily |
| Project Server: alerts and reminders for Project Server service application | Sends the alerts and reminders that were set up by Project Web App users. | Daily |
| Project Server: backup and restore for Project Server service application | Backs up and restores Project Web App data to and from the archive store, using the schedule set by the Project Server administrator. | Daily |
| Project Server: database maintenance job for Project Server service application | Performs routine maintenance on the Project Server database including defragmenting the indexes and updating the database usage. | Daily |
| Project Server: language installation for Project Server service application | Completes installation of Project Web App language packs in the database, and ensures deployment of localized Report Center reports. | Daily |
| Project Server: monitor scheduled cube jobs for Project Server service applicatio | Updates data analysis cubes that are scheduled in Project Web App. | Hourly |
| Project Server: product feedback job for Project Server service application | Collects statistical data on the usage, reliability and performance of Project Server features and sends this information to Microsoft to be used to improve the product in future releases. | Daily |
| Project Server: Queue auto heal job for Project Server service application | Attempts to automatically heal stuck Project Server queue jobs when the queue job is stuck at Waiting for Processing or Processing state due to internal errors. | 30 minutes |
| Project Server: Queue maintenance job for Project Server service application | Purges older Project Server queue jobs to maintain the performance of the Project Server queue. | Daily |
| Project Server: resource capacity refresh job for Project Server service application | Refreshes the resource capacity information in Project Web App reporting. | Daily |
| Project Server: synchronization of Project Web App permissions to SharePoint Server permissions job for Project Server service application | Synchronizes Project permissions to the SharePoint Server project sites. Users who can view or change projects in Project Web App are granted permissions to the SharePoint Server sites for those projects. You can change these permissions from the PWA Settings page. | Daily |
| Project Server: synchronization of SharePoint Server permissions to Project Web App permissions job for Project Server service application | Synchronizes SharePoint Server permissions to Project Web App. | 1 minute |
| Project Server: synchronize Exchange OOF calendar job for Project Server service application | Synchronizes out-of-office time for users who select this option. Each user's Microsoft Exchange calendar synchronizes with their Project Web App resource calendar. | Daily |
| Project Server: task list synchronizer for SharePoint Tasks List Projects job for Project Server service application | Updates Project Server with the latest changes from connected SharePoint Server Project Task Lists. | 5 minutes |
| Project Server: workflow maintenance job for Project Server service application | Maintains the health of Project Server workflows. It resolves issues between Enterprise Project Templates and workflows, updates the status of workflows, and closes completed workflows. | Daily |
| Recycle Bin | Looks for content in the Recycle Bins and moves it to the next stage or deletes it. | Weekly |
| Repair orphan site collections | Attempts to repair orphaned site collections | Daily |
| Request more quota | Queues up requests for additional quota by the site collection admin and sends the request to the tenant admin. | 30 minutes |
| Scheduled Approval | Looks for content that is scheduled for approval and moves it to the next stage in the process. | 1 minute |
| Scheduled Unpublish | Looks for content that is scheduled to be unpublished and removes it. | 1 minute |
| Search and process | Processes a search result that is scoped to a site collection and puts search results on hold. | Daily |
| Search change log generator | Generates appropriate change logs when SharePoint items change. This is required for search to function correctly. | 5 minutes |
| Search engine sitemap | Generates search engine sitemaps and updates robots.txt. | Daily |
| SharePoint BI maintenance | Deletes temporary dashboard objects and user-persistent filter values from the database. The longevity of these values can be set on the PerformancePoint Services Settings page. | Hourly |
| SharePoint Server CEIP data collection | Collects the Customer Experience Improvement Program data. | Daily |
| Site lookup refresh | Checks the site map data for site lookup changes. | 1 minute |
| Site master invalidation | Checks the site masters in content DB for any feature or site definitions changes. If required, it recreates the site master. | Hourly |
| Site policy and Exchange site mailbox policy update | Updates Exchange site mailboxes with the site policy of the associated SharePoint site. | Daily |
| Solution daily resource usage update | Marks the daily boundary for sandboxed solution resource quota monitoring. | Daily |
| Solution resource usage log processing | Aggregates resource usage data from sandboxed solution execution. | 5 minutes |
| Solution resource usage update | Records resource usage data from sandboxed solution execution, and sends email to owners of site collections that are exceeding their allocated resource quota. | 15 minutes |
| State Service delete expired sessions | Deletes expired data that is stored in the state service databases. | Hourly |
| Storage metrics processing | Processes storage metrics changes for site collections. | 5 minutes |
| Taxonomy groups replication | A timer job for hybrid connected servers that updates the local SharePoint Server term store with the latest term changes made to the Enterprise Metadata service in the hybrid connected SharePoint tenant. | Daily |
| Taxonomy update scheduler | Updates site collections with the latest term changes that were made to the Enterprise Metadata service. | Hourly |
| Timer service recycle | Recycles the Timer service to free resources. | Daily |
| Translation Export Job Definition | Exports page and list content to XLIFF for human translation or machine translation via the Machine Translation Service. | 15 minutes |
| Translation Import Job Definition | Imports translated page and list content from XLIFF to correct location in a site collection. | 15 minutes |
| Unified policy onprem sync | Synchronizes the unified policy from the master policy store for SharePoint Server. | Hourly |
| Unified policy sync status update | Uploads the workoad policy synchronize status to the master policy store. | 5 minutes |
| Upgrade site collections | Upgrades site collections in a content database. | 10 minutes |
| Upgrade site collections | Upgrades site collections in a content database. | Daily |
| Upgrade site collections | Upgrades site collections in a content database. | Hourly |
| Upgrade work item | Processes deferred upgrade work items which were generated during an upgrade. For example, generating thumbnails for upgraded image libraries. | Daily |
| Upload App Analytics | Uploads aggregated app usage data to Microsoft. Microsoft uses this data to improve the quality of apps in the marketplace. If you have multiple content farms connecting to the same search server, activate this feature only on one farm. | Daily |
| User Profile service application - activity feed | Pre-computes activities to be shown in users' activity feeds. | 10 minutes |
| User Profile service application - activity feed cleanup | Cleans up pre-computed activities that are used in activity feeds that are older than 14 days. This job does not affect the User Profile change log. | Daily |
| User Profile service application - audience compilation | Computes memberships of defined audiences. | Weekly |
| User Profile service application - background operations processing | Runs background operations for the User Profile service application. | 5 minutes |
| User Profile service application - feed cache full repopulation | Handles the full repopulation of feed cache. | 5 minutes |
| User Profile service application - feed cache repopulation | Handles the repopulation of feed cache. | 5 minutes |
| User Profile service application - My Site suggestions email | Sends email messages that contain colleague and keyword suggestions to people who do not update their profiles often. | Monthly |
| User Profile service application - Per database User Profile to SharePoint full synchronization | Synchronizes user information from the User Profile application to SharePoint users and from SharePoint site memberships to the User Profile application for a database. | 5 minutes |
| User Profile service application - profile attribute sync | Synchronizes Active Directory attributes to Profile database. | 10 minutes |
| User Profile service application - social data maintenance | Aggregates social tags and ratings and cleans the social data change log. | Hourly |
| User Profile service application - social rating synchronization | Use to synchronize rating values between Social database and Content database. | Hourly |
| User Profile service application - Unified group processing high performance | Runs the Unified Group site collection operations. | 1 minute |
| User Profile service application - Unified group processing | Runs the Unified Group site collection operations. | 1 minute |
| User Profile service application - User change import | Imports user property changes to the User Profile database. | 15 minutes |
| User Profile service application - User PointPublishing processing | Runs the User PointPublishing personal site collection operations. | 1 minute |
| User Profile service application - User Profile Active Directory import | Imports objects from Active Directory to the Profile database. | 5 minutes |
| User Profile service application - user profile change cleanup | Cleans up data that is 14 days old from User Profile change log. | Daily |
| User Profile service application - user profile change | Processes changes to user profiles. | Hourly |
| User Profile service application - user profile language synchronization | Looks for new language pack installations and makes sure that strings that relate to the user profile service are localized correctly. | Hourly |
| User Profile service application - User Profile to SharePoint full synchronization | Synchronizes user information from the User Profile service application to SharePoint users and synchronizes site memberships from SharePoint to the User Profile service application. | Hourly |
| User Profile service application - User Profile to SharePoint language and region synchronization | Synchronizes language and region information from the User Profile service application to SharePoint users. | 1 minute |
| User Profile service application - User Profile to SharePoint quick synchronization | Synchronizes user information from the User Profile service application to SharePoint users who were recently added to a site. | 5 minutes |
| User Profile service application - User Profile to SharePoint synchronization alert | Checks to see if the synchronization of user information from the User Profile application to SharePoint users is out of date. | Hourly |
| Variations create hierarchies job definition | Creates a complete variations hierarchy by spawning all sites and pages from the source site hierarchy for all variation labels. | Hourly |
| Variations propagate list items job definition | Propagates list items to variant sites. | 15 minutes |
| Variations propagate page job definition | Creates or updates peer pages of the source page that was approved or published in all target labels. The resulting peer pages are in an unpublished state. | 15 minute |
| Variations propagate sites and lists | Creates variant sites when the Variations Automatic Creation setting is enabled. | 30 minute |
| Video query rule provisioner | Provisions video query rule for a site when the Search service application becomes available. | Daily |
| Word Automation Services | Processes and distributes queued conversion job items to application servers. | 15 minutes |
| Word Automation Services - Remove Job History | Removes the history for expired jobs from Word Automation Services. | Weekly |
| Workflow | Processes workflow events that are in the scheduled items table, such as delays. | 5 minute |
| Workflow auto cleanup | Deletes tasks and instances in the workflow instance table for workflows that were marked completed more than  *n* days in the past, where  *n* is specified in the workflow association. Crawls through tasks and the workflow instance table. | Daily |
| Workflow failover | Processes events for workflows that have failed and are marked to be retried. | 15 minute |

See also

## See also

Other Resources

#### Other Resources

Default timer jobs in SharePoint Server 2019

Default timer jobs in SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
