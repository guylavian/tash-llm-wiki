---
title: "What's deprecated or removed from SharePoint Server 2016 - SharePoint Server"
description: "Learn about the features and functionality that are deprecated or removed in SharePoint Server"
ms.topic: overview
---
Note

What's deprecated or removed from SharePoint Server 2016

# What's deprecated or removed from SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the features and functionality that are deprecated or removed in SharePoint Server 2016

Deprecated features are included in SharePoint Server 2016 for compatibility with previous product versions. For information about new features in SharePoint Server 2016, see New and improved features in SharePoint Server 2016.

Features deprecated in SharePoint Server 2016

## Features deprecated in SharePoint Server 2016

The following features and functionality are deprecated in SharePoint Server.

Duet Enterprise for Microsoft SharePoint

### Duet Enterprise for Microsoft SharePoint

Duet Enterprise for Microsoft SharePoint and SAP can't be deployed with SharePoint Server 2016. SharePoint Server 2016 doesn't have any Duet components, so it will not install.

If you want to deploy Duet Enterprise for Microsoft SharePoint, you must use SharePoint Server 2013 Enterprise Edition.

SharePoint Foundation

### SharePoint Foundation

SharePoint Foundation 2013 remains available for use. For more information, see SharePoint Foundation 2013.

Previous releases of SharePoint Server included SharePoint Foundation, a free edition of SharePoint that included most of the core functionality and architecture provided by the commercial editions of SharePoint. SharePoint Foundation is no longer available in the SharePoint Server 2016 release.

Standalone Install mode

### Standalone Install mode

SharePoint Server 2016 doesn't support the standalone install option, so it's no longer available in the setup program. Use the MinRole feature during installation and choose one of the available install options. The Single Server Farm option where everything is installed on the same computer is supported for dev/test/demo purposes. When you use this option, you must install SQL Server yourself and then run the SharePoint Server 2016 farm configuration wizard. For more information, see "MinRole farm topology" in New and improved features in SharePoint Server 2016.

ForeFront Identity Manager client (FIM)

### ForeFront Identity Manager client (FIM)

Earlier versions of SharePoint used ForeFront Identity Manager client (FIM) to synchronize between Active Directory and SharePoint. SharePoint Server 2016 no longer uses FIM as the synchronization client. The default process is Active Directory Import. You can also use any synchronization tool such as Microsoft Identity Manager 2016, or any third-party tool. We'll soon release tools to help you deploy and configure Microsoft Identity Manager 2016 to work with SharePoint Server 2016 for identity synchronization.

Excel Services in SharePoint

### Excel Services in SharePoint

Excel Services and its associated business intelligence capabilities are no longer hosted on SharePoint Server. Excel Services functionality is now part of Excel Online in Office Online Server (this is the next version of Office Web Apps Server), and SharePoint users can use the services from there. For more information, see Office Online Server now available, Office Online Server, and Configure Excel Online administrative settings.

If you currently use Excel Services in SharePoint 2013 and upgrade to SharePoint Server 2016, you must also deploy Office Online Server with Excel Online to ensure Excel Services functionality remains available.

The following Excel Services functionality is deprecated:

Trusted data providers

Trusted file locations

Trusted data connection libraries

Unattended service account

Excel Services PowerShell cmdlets

Opening of Excel workbooks from SharePoint Central Administration site

The following Excel Services functionality requires Excel Online in Office Online Server:

Viewing and editing Excel workbooks in a browser (with or without the Data Model)

Excel Web Access web part for SharePoint

ODC file support (no longer requires Data Connection Libraries)

Programmability features such as JavaScript OM, User Defined Function Assemblies, SOAP and REST protocol support

Tags and Notes

### Tags and Notes

The Tags and Notes feature is deprecated in SharePoint Server 2016. This means that users can still create new tags and notes and access any existing ones. However, we don't recommend using this feature because it will be removed in the next release.

Administrators can archive all existing tags and notes by using the **Export-SPTagsAndNotesData** cmdlet.

Verify that you meet all of the following minimum requirements.

You must have membership in the **securityadmin** fixed server role on the SQL Server instance

You must have membership in the **db_owner** fixed database role on all databases that are to be updated.

You must be a member of the Administrators group on the server on which you're running the Microsoft PowerShell cmdlet.

```
Export-SPTagsAndNotesData -Site <http://site.contoso.com> -FilePath <tagsandnotes.zip>
```

Where:

`<http://site.contoso.com>` is the URL to an existing SharePoint root site where you want to export the tags and notes from.

`<tagsandnotes.zip>` is the name you give to the .zip file that you want to export.

Stsadm.exe

### Stsadm.exe

We recommend that you use Microsoft PowerShell when you perform command-line administrative tasks. The Stsadm command-line tool is deprecated, but it's included to support compatibility with previous product versions.

Removed features in SharePoint Server 2016

## Removed features in SharePoint Server 2016

The following feature and functionality is removed in SharePoint Server 2016.

Work Management Service Application

### Work Management Service Application

The Work Management Service Application is removed from SharePoint Server 2016. The My Tasks and associated Exchange Task Sync features are also removed from SharePoint Server 2016. Both of these features required the Work Management Service Application.

Legacy Cloud Hybrid Search

### Legacy Cloud Hybrid Search

Search Content Service (SCS), an internal component of Cloud Hybrid Search in SharePoint in Microsoft 365 will be retired starting June 30, 2025. To continue using Cloud Hybrid Search by then, upgrade your SharePoint Server farm to SharePoint Server Subscription Edition (SPSE) Version 25H1 or later versions. Without this upgrade, all versions of SharePoint Server 2016 can only search for on-premises and Microsoft 365 content separately through Hybrid Federated Search after this retirement.

SharePoint BI capabilities

## SharePoint BI capabilities

If you want to use Microsoft SQL Server Power Pivot for SharePoint or Microsoft Power View for SharePoint for BI solutions with SharePoint Server 2016, you must install the Power Pivot or Power View add-ins for SQL Server 2016 RTM. The SQL Server 2014 (SP1) Power Pivot for SharePoint and Power View for SharePoint add-ins can't be deployed or used with SharePoint Server 2016. To deploy these add-ins, you need to upgrade to SQL Server 2016 RTM. For more information, see New and improved features in SharePoint Server 2016. The following business intelligence features are available with SharePoint Server 2016 when you download SQL Server 2016 RTM:

Power Pivot Gallery

Scheduled Data Refresh

Using another workbook's Data Model as a data source

Power View reports (standalone or embedded in Excel workbooks)

Power View Subscriptions and Report Alerting

Power Pivot Management Dashboard

BISM Link support

Additional resources

## Additional resources

- Last updated on 
		2025-03-11
