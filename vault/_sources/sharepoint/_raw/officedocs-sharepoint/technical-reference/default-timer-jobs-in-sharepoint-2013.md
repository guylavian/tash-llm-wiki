---
title: "Default timer jobs in SharePoint 2013 - SharePoint Server"
description: "Learn about the timer jobs in SharePoint."
ms.topic: reference
---
Note

Default timer jobs in SharePoint 2013

# Default timer jobs in SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Default timer jobs

## Default timer jobs

The following table lists the default timer jobs for SharePoint 2013.

| **Timer job** | **Description** | **Default schedule** |
| --- | --- | --- |
| Access Services monitor | Monitors the connectivity of Access Services on SharePoint and SQL Azure. | 5 minutes |
| Analytics Event Store Retention | Periodically cleans up the Event Store and the Reporting Database. All data older than 14 days is removed from the Event Store whereas all data older than 3 years is removed from the Reporting Database. | Weekly |
| Analytics for Search service application | Periodically schedules analytics for the Search service application. | 10 minutes |
| App installation service | Installs and uninstalls apps. | 5 minutes |
| App state update | Retrieves and applies updated information on apps from the SharePoint Store. It includes the availability of updates and information about disabled apps. | Hourly |
| Application addresses refresh | Synchronizes connection information for remote service applications. | 15 minutes |
| Application server | Manages shared service instances that do not perform highly privileged operations. The Search service instance is managed by this job on stand-alone server deployments. | 1 minute |
| Application server administration service | Manages shared service instances that may perform highly privileged operations. Requires that the SharePoint Administration service is running. The Search service instance is managed by this job on deployments other than stand-alone server deployments. | 1 minute |
| Audit log trimming | Trims audit trail entries from site collections. | Monthly |
| Bulk workflow task processing | Processes bulk workflow task completion. | Daily |
| CEIP data collection | Collects farm data for the Customer Experience Improvement Program. | Daily |
| Cell storage data cleanup | Deletes temporary cell storage data and frees SQL Server disk space. | Daily |
| Change log | Records many types of changes that you make to SharePoint sites. Removes expired entries from the change log of the web application. | Weekly |
| Content organizer processing | Processes documents in the drop-off library that match organizing rules. | Daily |
| Content type hub | Tracks content type log maintenance and manages unpublished content types. | Daily |
| Content type subscriber | Retrieves content type packages from the hub and applies them to the local content type gallery. For more information about content types, see Plan to share term sets and content types in SharePoint Server 2013. | Hourly |
| Crawl log cleanup for Search service application | Performs crawl log cleanup for Search service applications. | Daily |
| Create upgrade evaluation site collections | Creates upgrade evaluation site collections. | Daily |
| Dead site delete | When auto site cleanup is enabled, sites that are not used in a certain period of time are deleted. | Weekly |
| Delete job history | Deletes old entries from the timer job history. | Weekly |
| Delete upgrade evaluation site collections | Deletes upgrade evaluation site collections that are past their expiry date and sends notifications to those that are near expiry date. | Daily |
| Diagnostic data provider: app usage | Periodically collects App statistics. | Daily |
| Diagnostic data provider: event log | Collects Windows Event Log entries and stores the data in the logging database. | 10 minutes |
| Diagnostic data provider: IO intensive SQL queries | Collects a SQL trace of I/O intensive SQL queries. | 1 minute |
| Diagnostic data provider: per-database IO | Collects I/O statistics for each database file. | 2 minutes |
| Diagnostic data provider: performance counters - database servers | Collects Performance Monitor Counters data on database servers and stores the data in the logging database.  
 **Important:** 
 The timer service account must have sufficient permission to collect counters on the database server. The account should be a member of the Performance Monitor Users (PMU) group. | 1 minute |
| Diagnostic data provider: performance counters - web front ends | Collects performance monitor counters data on front-end Web servers and stores the data in the logging database. | 1 minute |
| Diagnostic data provider: site size | Collects size data for each site collection. | Daily |
| Diagnostic data provider: SQL blocking queries | Collects data associated with blocked SQL queries and stores the data in the logging database. | 15 seconds |
| Diagnostic data provider: SQL blocking reports | Captures the text of any queries that cause SQL blocking. | 1 minute |
| Diagnostic data provider: SQL deadlocks | Captures the call graphs of SQL deadlocks. | 1 minute |
| Diagnostic data provider: SQL DMV | Collects SQL Dynamic Management Views (DMV) data and stores the data in the logging database. | 30 minutes |
| Diagnostic data provider: SQL memory DMV | Collects SQL Dynamic Management Views (DMV) data and stores the data in the logging database. | 15 seconds |
| Diagnostic data provider: trace log | Collects trace log entries and stores the usage data in the logging database. | 10 minutes |
| Disk quota warning | Looks for sites that have exceeded the storage quota, and sends out disk quota warning email notifications. | Weekly |
| Document ID assignment | Work item that assigns document ID to all items in the site collection. | Daily |
| Document ID enable/disable | Work item that propagates content type changes across all sites when the Document ID feature is reconfigured. | Daily |
| Document Set fields synchronization | Synchronizes metadata from the document set to the items inside the document library. | 15 minutes |
| Document Set template update | Propagates changes that are made to the document set template to the existing items. | Hourly |
| eDiscovery in-place hold processing | The in-place hold timer job starts and releases the holds of SharePoint websites. | Hourly |
| Education bulk operation | Carries out the education bulk operations. | Hourly |
| Enterprise Metadata site data update | Updates all site collections after a language pack addition or an Enterprise Metadata service application restore. | Hourly |
| Expiration policy | Enumerates list items and looks for those with an expiration date that has already occurred. For those items, runs disposition processing. Disposition processing most often results in deleting items. But it can perform other actions, such as processing disposition workflows. | Weekly |
| Gradual site delete | Deletes all the data from the host content database for all deleted site collections. | Daily |
| Health analysis (Daily, Central Administration, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Central Administration web application and the Usage and Health Data Collection service application. | Daily |
| Health analysis (Daily, Central Administration, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the Central Administration web application and the Usage and Health Data Collection service application. | Daily |
| Health analysis (Daily, Machine Translation service, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Machine Translation service application and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Machine Translation service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the Machine Translation service application and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Microsoft SharePoint Foundation Timer, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Microsoft SharePoint Foundation Timer, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Microsoft SharePoint Foundation web application, all servers) | Runs SharePoint Health Analyzer jobs on all servers in the farm that run SharePoint web applications and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Microsoft SharePoint Foundation web application, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs SharePoint web applications and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, User Profile service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service application and the Usage and Health Data Collection service application. | Daily |
| Health Analysis (Daily, Visio Graphics service, any server) | Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs Visio Services in SharePoint Server 2013 and the Usage and Health Data Collection service application. | Daily |
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
| Health statistics updating | Updates the statistics for the Usage and Health Data Collection service application. | 1 minute |
| Hold processing and reporting | Generates a hold report by enumerating items in a hold and updating them to remove them from hold, as appropriate. | Daily |
| Immediate Alerts | Sends out immediate and scheduled alerts. | 5 minutes |
| Indexing schedule manager on SQL Server | Starts scheduled crawls. | 5 minutes |
| InfoPath Forms Services maintenance | Performs maintenance operations on administrator-approved InfoPath Forms Services form templates across all front-end Web servers. | Daily |
| Information management policy | Performs background processing for information policies, such as calculating updated expiration dates for items with a new retention policy. | Weekly |
| Internal app state update | Retrieves and applies updated information on apps from App Catalogs. | Hourly |
| License renewal | Renews all licenses of the apps from the SharePoint Store. | Hourly |
| Licensing synchronizer | Synchronizes trial expiration time licensing information to the configuration database. | Hourly |
| Machine Translation Service - Language Support | Updates the languages available to the Machine Translation Service. | Weekly |
| Machine Translation Service - Machine Translation Service | Initiates translation of documents that were submitted to the Machine Translation Service for asynchronous translation. | 15 minutes |
| Machine Translation Service - Remove Job History | Removes the history for expired jobs from the Machine Translation Service queue database. | Weekly |
| Microsoft SharePoint Foundation Usage Data Import | Imports usage log files into the event store. | 5 minutes |
| Microsoft SharePoint Foundation Usage Data Processing | Checks for expired usage data at the farm level and deletes the data. Expired usage data consists of records in the central usage data collection database that are older than 30 days. | Daily |
| My Site cleanup | Starts a workflow on a deleted user's My Site. The default behavior is to send an email message to the manager with a link to the deleted user's site. The email message contains a request to the manager to move any documents or data that the manager wants to preserve, because the site might be deleted in the future. | Daily |
| My Site instantiation interactive request queue | A timer job queue for interactive (web initiated) My Site instantiation requests. | 1 minute |
| My Site instantiation non-interactive request queue | A timer job queue for non-interactive (Office-client initiated) My Site instantiation requests. | 1 minute |
| My Site second instantiation interactive request queue | A second timer job queue for interactive (web initiated) My Site instantiation requests. | 1 minute |
| Notification | Queries and updates the notification list and sends out pending scheduling notifications. | Daily |
| Password management | Sends email and logs events for expiring passwords and password changes. This timer job helps ensure that managed passwords are changed before they expire. | Daily |
| Performance metric provider | Collects the performance metrics data. | 1 minute |
| Persisted navigation term set synchronization | Synchronizes the persisted copy of navigation term sets. | Hourly |
| Prepare query suggestions | Prepares candidate queries for query suggestion and performs pre-computations for result block ranking. | Daily |
| Product version | Checks the installation status of the computer and adds that data to the database. | Daily |
| Project Server: database maintenance job for Project Service Application | Performs routine maintenance on the Project Server database including defragmenting the indexes and updating the database usage. | Daily |
| Project Server: product feedback job for Project Service Application | Collects statistical data on the usage, reliability and performance of Project Server features and sends this information to Microsoft to be used to improve the product in future releases. | Daily |
| Project Server: Project Web App provisioning job for Project Service Application | Provisions new instances of Project Server. | Monthly |
| Project Server: Queue maintenance job for Project Service Application | Purges older Project Server queue jobs to maintain the performance of the Project Server queue. | Daily |
| Project Server: queue service health job for Project Service Application | Monitors the health of Queue service instances and takes corrective action when it is required. | 5 minutes |
| Project Server: resource capacity refresh job for Project Service Application | Refreshes the resource capacity information in Project Web App reporting. | Daily |
| Project Server: synchronization of SharePoint Server permissions to Project Web App permissions job for Project Service Application | Synchronizes SharePoint Server permissions to Project Web App. | 1 minute |
| Project Server: task list synchronizer for SharePoint Tasks List Projects job for Project Service Application | Updates Project Server with the latest changes from connected SharePoint Server Project Task Lists. | 5 minutes |
| Project Server: workflow maintenance job for Project Service Application | Maintains the health of Project Server workflows. It resolves issues between Enterprise Project Templates and workflows, updates the status of workflows, and closes completed workflows. | Daily |
| Project Web App: Shared Service | Enables per-instance Project Web App jobs to be managed. | 1 minute |
| Query classification dictionary update for Search service application. | Periodically updates dictionary that is used for query classification. | 30 minutes |
| Query logging | Updates query and click logs by inserting new entries and deleting old entries. | 15 minutes |
| Recycle Bin | Looks for content in the Recycle Bins and moves it to the next stage or deletes it. | Weekly |
| Scheduled Approval | Looks for content that is scheduled for approval and moves it to the next stage in the process. | 1 minute |
| Scheduled Unpublish | Looks for content that is scheduled to be unpublished and removes it. | 1 minute |
| Search and process | Processes a search result that is scoped to a site collection and puts search results on hold. | Daily |
| Search change log generator | Generates appropriate change logs when SharePoint items change. This is required for search to function correctly. | 5 minutes |
| Search custom dictionaries update | Updates the custom dictionaries used for search. These include custom dictionaries for company extraction and for query spelling correction. | 10 minutes |
| Search engine sitemap | Generates search engine sitemaps and updates robots.txt. | Daily |
| Search health monitoring - trace events | Runs to check the events that are being traced for search health monitoring. | 1 minute |
| SharePoint BI maintenance | Deletes temporary dashboard objects and user-persistent filter values from the database. The longevity of these values can be set on the PerformancePoint Services Settings page. | Hourly |
| Site policy and Exchange site mailbox policy update | Updates Exchange site mailboxes with the site policy of the associated SharePoint site. | Daily |
| Solution daily resource usage update | Marks the daily boundary for sandboxed solution resource quota monitoring. | Daily |
| Solution resource usage log processing | Aggregates resource usage data from sandboxed solution execution. | 5 minutes |
| Solution resource usage update | Records resource usage data from sandboxed solution execution, and sends email to owners of site collections that are exceeding their allocated resource quota. | 15 minutes |
| Spelling customizations upgrade | Upgrades user spelling customizations from the previous SharePoint version to this version. This job will run on schedule until it succeeds with the upgrade and then be set to disabled. If there are no spelling customizations to upgrade, it will be set to disabled after the first run. | Hourly |
| Spelling dictionary update | Updates the dynamic dictionary that is used to correct the spelling of queries with changes in the indexed content.  
 **Note:** 
 This is a time-consuming operation. Do not schedule it to run more frequently than one time per day. | Daily |
| State Service delete expired sessions | Deletes expired data that is stored in the state service databases. | Hourly |
| Storage metrics processing | Processes storage metrics changes for site collections. | 5 minutes |
| Taxonomy groups replication | A timer job for hybrid connected servers that updates the local SharePoint Server term store with the latest term changes made to the Enterprise Metadata service in the hybrid connected SharePoint tenant. | Daily |
| Taxonomy update scheduler | Updates site collections with the latest term changes that were made to the Enterprise Metadata service. | Hourly |
| Timer service recycle | Recycles the Timer service to free resources. | Daily |
| Translation Export Job Definition | Exports page and list content to XLIFF for human translation or machine translation via the Machine Translation Service. | 15 minutes |
| Translation Import Job Definition | Imports translated page and list content from XLIFF to correct location in a site collection. | 15 minutes |
| Upgrade site collections | Upgrades site collections in a content database. | 1 minute |
| Upgrade work item | Processes deferred upgrade work items which were generated during an upgrade. For example, generating thumbnails for upgraded image libraries. | Daily |
| Usage Analytics for Search service application | Periodically schedules processing of the Usage Analytics analysis. | 10 minutes |
| User Profile service application - activity feed | Pre-computes activities to be shown in users' activity feeds. | 10 minutes |
| User Profile service application - activity feed cleanup | Cleans up pre-computed activities that are used in activity feeds that are older than 14 days. This job does not affect the User Profile change log. | Daily |
| User Profile service application - audience compilation | Computes memberships of defined audiences. | Weekly |
| User Profile service application - My Site suggestions email | Sends email messages that contain colleague and keyword suggestions to people who do not update their profiles often. | Monthly |
| User Profile service application - social data maintenance | Aggregates social tags and ratings and cleans the social data change log. | Hourly |
| User Profile service application - system job to manage user profile synchronization | Manages provisioning and runs additional tasks that are related to User Profile Synchronization.  
 **Note:** 
 Do not change the information or frequency of this job. If you have to change how often incremental synchronization is performed, in Central Administration, go to the **Manage User Profile Service Application** page, and then in the **Synchronization** category, click **Schedule Incremental User Profile Synchronization**. | 1 minute |
| User Profile service application - user profile change | Processes changes to user profiles. Changes the user profile. User rights can be migrated from one user to another user. This timer job is used when a user has to be migrated. But the previous user profile remains in AD DS. | Hourly |
| User Profile service application - user profile change cleanup | Cleans up data that is 14 days old from User Profile change log. Migrates user rights from one user to another user, and migrates the user rights and removes that user from Active Directory Domain Services (AD DS). This is mainly used when the name of a user is changed in AD DS. The older user name is replaced by a new user name, and the older one is removed from AD DS.  
 If you want to change retention settings, see the Profilechangelog: Stsadm operation in Stsadm to Microsoft PowerShell mapping in SharePoint Server. | Daily |
| User Profile service application - user profile incremental synchronization | Runs at the specified interval to synchronize user, group and group membership changes between the User Profile service application and specified directory source (such as AD DS or Lightweight Directory Access Protocol (LDAP)). Synchronization will look for changes since the last time this job was run and only perform these changes for AD DS and LDAP sources.  
 **Note:** 
 Do not change the settings or frequency of this timer job.  
 Schedule profile synchronization provides two sections: To learn how to change the schedule for incremental synchronization, see the first section; to learn how to check the status of User Profile Synchronization timer jobs, see the second section. | Daily |
| User Profile service application - user profile language synchronization | Looks for new language pack installations and makes sure that strings that relate to the user profile service are localized correctly. | Hourly |
| User Profile service application proxy - feed cache repopulation | Handles the repopulation of feed cache. | 5 minutes |
| User Profile service application proxy - social rating synchronization | Synchronizes rating values between the social database and content database. | Hourly |
| User Profile service application proxy - User Profile to SharePoint full synchronization | Synchronizes user information from the User Profile service application to SharePoint users and synchronizes site memberships from SharePoint to the User Profile service application. | Hourly |
| User Profile service application proxy - User Profile to SharePoint language and region synchronization | Synchronizes language and region information from the User Profile service application to SharePoint users. | 1 minute |
| User Profile service application proxy - User Profile to SharePoint quick synchronization | Synchronizes user information from the User Profile service application to SharePoint users who were recently added to a site. | 5 minutes |
| Variations create hierarchies job definition | Creates a complete variations hierarchy by spawning all sites and pages from the source site hierarchy for all variation labels. | Hourly |
| Variations propagate list items job definition | Propagates list items to variant sites. | 15 minutes |
| Variations propagate page job definition | Creates or updates peer pages of the source page that was approved or published in all target labels. The resulting peer pages are in an unpublished state. | 15 minute |
| Variations propagate sites and lists | Creates variant sites when the Variations Automatic Creation setting is enabled. | 30 minute |
| Video query rule provisioner | Provisions video query rule for a site when the Search service application becomes available. | Daily |
| Word Automation Services | Processes and distributes queued conversion job items to application servers. | 15 minutes |
| Word Automation Services - Remove Job History | Removes the history for expired jobs from Word Automation Services. | Weekly |
| Work Management synchronize with Exchange | Triggers Exchange Sync operations for the Work Management service. | 1 minute |
| Workflow | Processes workflow events that are in the scheduled items table, such as delays. | 5 minute |
| Workflow auto cleanup | Deletes tasks and instances in the workflow instance table for workflows that were marked completed more than  *n* days in the past, where  *n* is specified in the workflow association. Crawls through tasks and the workflow instance table. | Daily |
| Workflow failover | Processes events for workflows that have failed and are marked to be retried. | 15 minute |

See also

## See also

Concepts

#### Concepts

Default timer jobs in SharePoint Server 2016

Default timer jobs in SharePoint Server 2019

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
