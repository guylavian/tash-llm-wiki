---
title: "PerformancePoint Services application settings - SharePoint Server"
description: "Learn how to customize PerformancePoint Services application settings to meet your business needs."
ms.topic: article
---
Note

PerformancePoint Services application settings

# PerformancePoint Services application settings

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

PerformancePoint Services has settings such as cache durations, filter behavior, and query time-out that affect performance, security, and connections to external data. These settings affect anyone who uses the same service application. The settings can be managed by using the SharePoint Central Administration website.

Note

PerformancePoint Services has been removed from SharePoint Server Subscription Edition. We recommend to explore Microsoft Power BI as an alternative to PerformancePoint Services.

PerformancePoint Services application settings

## PerformancePoint Services application settings

| **Setting** | **Description** |
| --- | --- |
| Secure Store and Unattended Service Account | A single shared user account is used to access all data sources. This is a low-privileged domain account stored in the Secure Store Service. An application ID is automatically mapped in the Secure Store Service that specifies the default secure store target application, PerformancePoint Services, and it looks up credential mapping when it connects to external data sources.  
 > [!IMPORTANT]> When you establish an unattended service account, first determine whether this account should have access to the data sources that will be retrieved in Dashboard Designer. |
| Comments | Users who have appropriate permissions can annotate scorecard cells in Dashboard Designer and on a deployed SharePoint site.  
 > [!NOTE]> If a Dashboard Designer author attempts to add cell comments that are disabled, the author will receive a message that states, "An unexpected system error has occurred. Additional details have been logged for your administrator." If you want the author to be able to insert comments in a cell, select the check box, **Enable comments**.           You can also remove comments by clicking **Delete Comments by Date**. This command opens a dialog. Select the date by which you want comments removed from the PerformancePoint Services database, and then click **Delete**. |
| Analysis Services EffectiveUserName | The Analysis Services EffectiveUserName capability is an alternative to Windows delegation for allowing individual users to securely access Analysis Services data. When this setting is enable, all connections to Analysis Services data for individual users will be made using the EffectiveUserName connection string property instead of Windows delegation. |
| Cache | Temporarily storing (or "caching") frequently-accessed items decreases load times for future requests. Specify the duration for items to remain in the cache. |
| Data Sources | Set the duration of no response before a data source query is canceled. |
| Filters | Specify how long to remember user-selected filter values and how often to clear expired values. Set the maximum number of members to retrieve and insert into a filter of type "tree". |
| Select Measure Control | Set the maximum number of measures to retrieve and insert into a dashboard Select Measure control. |
| Show Details | Set the limit for the number of rows returned when a user clicks "Show Details." |
| Decomposition Tree | Set the maximum number of individual items (per level) returned to the decomposition tree visualization. The minimum value is 0. The maximum is 1,000,000. |

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
