---
title: "Configure the unattended service account for PerformancePoint Services - SharePoint Server"
description: "Learn how to configure the unattended service account for PerformancePoint Services."
ms.topic: how-to
---
Note

Configure the unattended service account for PerformancePoint Services

# Configure the unattended service account for PerformancePoint Services

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The unattended service account is an Active Directory account that is used for accessing PerformancePoint Services data sources. This account is used by PerformancePoint Services on behalf of authorized users to provide access to external data sources for the purposes of creating and using dashboards and other PerformancePoint Services content. To configure the unattended service account, see Configure the unattended service account for PerformancePoint Services in this article.

Note

PerformancePoint Services has been removed from SharePoint Server Subscription Edition. We recommend to explore Microsoft Power BI as an alternative to PerformancePoint Services.

Note

The unattended service account is a universal account that provides equal data access to all authorized users. If you need more fine-grained data access, see Configure Secure Store for use with PerformancePoint Services.

PerformancePoint Services uses Secure Store Service to store the unattended service account password. Before using the Unattended Service Account, make sure that Secure Store has been configured.

Configure the unattended service account for PerformancePoint Services

## Configure the unattended service account for PerformancePoint Services

Use the following procedure to configure the unattended service account for PerformancePoint Services.

**To configure the unattended service account for PerformancePoint Services**

On the SharePoint Central Administration Web site, in the **Application Management** section, click **Manage Service Applications**, and then click the PerformancePoint Services service application.

On the Manage PerformancePoint Services page, click **PerformancePoint Service Application Settings**.

In the **Secure Store and Unattended Service Account** section, enter the user name and password for the account that you want to use as the unattended service account.

Click **OK**.

You will see the Secure Store Service name and the user name that represents the unattended service account.

Once the unattended service account has been configured, you must grant that account access to your data sources:

For SQL Server data, the account must have a SQL logon with **db_datareader** permissions on each database that you want to access.

For SQL Server Analysis Services data, the account must have read access to the cube or an appropriate portion of the cube, depending on your needs.

For Excel Services data, the account must have access to the Excel workbook in a SharePoint document library.

For data in a SharePoint list, the account must have read access to the list.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
