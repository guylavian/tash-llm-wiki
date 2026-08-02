---
title: "Use PerformancePoint Services with Secure Store Service in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-use-performancepoint-services-with-secure-store
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/use-performancepoint-services-with-secure-store
family: administration
documentKind: "article"
abstract: "Learn about the options available for using the Secure Store Service with PerformancePoint Services to connect to and refresh data from external data sources."
---

# Use PerformancePoint Services with Secure Store Service in SharePoint Server - SharePoint Server

Note

Use PerformancePoint Services with Secure Store Service in SharePoint Server

# Use PerformancePoint Services with Secure Store Service in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This series of articles describes how to configure data access in PerformancePoint Services by using the Secure Store Service to map user and group credentials to the credentials of external data sources.

In Secure Store you specify a group of users to whom you want to grant access to a data source and a set of credentials that has access to that data source. The user information is stored in a Secure Store target application and the associated credentials are stored, encrypted, in the Secure Store database. You can then specify the target application in PerformancePoint Dashboard Designer, and PerformancePoint Services will use the stored credentials on behalf of the specified users to access data in Dashboard Designer and in the browser.

Note

PerformancePoint Services has been removed from SharePoint Server Subscription Edition. We recommend to explore Microsoft Power BI as an alternative to PerformancePoint Services.

Note

These articles assume that you have already deployed a Secure Store Service Application. If you have not deployed Secure Store, see Plan the Secure Store Service in SharePoint Server and Configure the Secure Store Service in SharePoint Server.

PerformancePoint Services can be used with Secure Store in two primary scenarios:

**Unattended Service Account**: The unattended service account is an account that is used by PerformancePoint Services to provide broad database access to all users in the farm. Use the unattended service account for accessing data that is not considered sensitive or where you do not want to restrict access to a certain group of users. For information about how to configure this scenario, see Configure the unattended service account for PerformancePoint Services.

**Specified target application**: You can specify a Secure Store target application in Dashboard Designer and Dashboard Designer will use the credential stored in Secure Store to access the selected data source. When you publish your dashboard, PerformancePoint Services will use these credentials to provide data refresh for authorized users. For information about how to configure this scenario, see Configure Secure Store for use with PerformancePoint Services.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
