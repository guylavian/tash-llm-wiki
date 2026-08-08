---
title: "What's deprecated or removed from SharePoint Server Subscription Edition? - SharePoint Server"
description: "Learn about the features and functionalities that are deprecated or removed in SharePoint Server Subscription Edition."
ms.topic: overview
---
Note

What's deprecated or removed from SharePoint Server Subscription Edition

# What's deprecated or removed from SharePoint Server Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the features and functionalities that are deprecated or removed in SharePoint Server Subscription Edition.

Definitions

## Definitions

Different customers may have different interpretations of terms such as "deprecated." To ensure that customers fully understand what we mean by the terminology in this document, we're including this brief definition of each term. For more information on Microsoft's lifecycle terms and definitions, see Lifecycle Terms and Definitions.

**Deprecated**

A feature is deprecated when Microsoft decides to no longer invest in its enhancements or further development. Customers are discouraged from having a dependency on a deprecated feature if they haven't used it before. Deprecated features are still supported by Microsoft in SharePoint Server Subscription Edition for customers who are already using this feature in previous releases and need the feature for backward compatibility. Deprecated features may be removed in future updates to SharePoint Server Subscription Edition. Unless there are exceptional circumstances, Microsoft will provide advance notice before a deprecated feature is removed by a future update. Customers should begin to explore their options for migrating away from these features.

Deprecated features are included in SharePoint Server Subscription Edition for compatibility with previous product versions. For information about new features in SharePoint Server Subscription Edition, see New and improved features in SharePoint Server Subscription Edition.

**Removed**

A removed feature is no longer supported by Microsoft in SharePoint Server Subscription Edition. In many cases, the feature is removed from the product, but in some cases it may still be present. A feature labeled as "removed" is unsupported even if the feature is still present in the product.

Deprecated features

## Deprecated features

InfoPath Forms Services

Microsoft Workflow Manager

SharePoint 2010 workflows

SharePoint Designer 2013

Internet Explorer 11

Basic authentication

Removed features

## Removed features

Access Services 2010

Access Services 2013

Classic authentication mode for content web applications

Groove sync app support

Lists web service APIs for Groove sync app

PerformancePoint Services

Stsadm.exe command-line tool

Update-SPHelp PowerShell cmdlet

Claims to Windows Token Service (C2WTS)

Legacy Cloud Hybrid Search

Detailed description of features deprecated or removed in SharePoint Server Subscription Edition

## Detailed description of features deprecated or removed in SharePoint Server Subscription Edition

The following features and functionality have been deprecated or removed in SharePoint Server Subscription Edition.

InfoPath Forms Services

### InfoPath Forms Services

InfoPath Forms Services is deprecated but will remain supported for the SharePoint Server Subscription Edition release until July 14, 2026. After that date, InfoPath Forms Services will no longer be supported. Microsoft recommends exploring Power Apps as a potential alternative to InfoPath forms.

Microsoft Workflow Manager

### Microsoft Workflow Manager

Microsoft has released SharePoint Workflow Manager as the new workflow engine to power the SharePoint 2013 Workflow platform for SharePoint Server and replace Microsoft Workflow Manager. We recommend that all customers using SharePoint 2013 workflows upgrade to SharePoint Workflow Manager as soon as they're able to. Microsoft will focus all future investments and maintenance on SharePoint Workflow Manger rather than Microsoft Workflow Manager, including providing support beyond the year 2026. For more information, see Install and configure workflow for SharePoint Server.

SharePoint 2010 workflows

### SharePoint 2010 workflows

SharePoint 2010 workflows are deprecated but will remain supported for the SharePoint Server Subscription Edition release until July 14, 2026. After that date, SharePoint 2010 workflows will no longer be supported. Microsoft recommends exploring SharePoint 2013 workflows or Power Automate as potential alternatives to SharePoint 2010 workflows.

SharePoint Designer 2013

### SharePoint Designer 2013

SharePoint Designer 2013 is deprecated but will remain supported with SharePoint Server Subscription Edition until July 14, 2026. After that date, SharePoint Designer 2013 will no longer be supported. Customers will be able to continue using Visual Studio to create and edit their SharePoint 2013 workflows after that date.

Internet Explorer 11

### Internet Explorer 11

Internet Explorer 11 is only supported in the SharePoint Central Administration site. Internet Explorer 11 isn't supported in Team sites, OneDrive personal sites, or any other types of SharePoint content sites. Microsoft recommends exploring Microsoft Edge as the replacement for Internet Explorer 11.

Basic authentication

### Basic authentication

For many years, applications have used Basic authentication to connect to servers, services, and API endpoints. Basic authentication simply means the application sends a username and password with requests, making it easier for attackers to capture user credentials, which increases the risk of those stolen credentials being reused against other endpoints or services.

With these threats and risks in mind, Basic authentication is deprecated but will remain supported for the SharePoint Server Subscription Edition until July 14, 2026. After that date, Basic authentication will no longer be supported and will eventually be removed in SharePoint Server Subscription Edition for all scenarios. Microsoft recommends exploring Trusted Identity Provider as the replacement for authentication.

Note

Starting with the 24H2 update (September 2024) for SharePoint Server Subscription Edition, admins can no longer create new web applications or web app extensions using Basic authentication.  Existing web apps using Basic authentication should continue to function, but new ones cannot be created.

Access Services 2010

### Access Services 2010

Access Services 2010 was removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps and Power Automate as potential alternatives to Access Services 2010.

Access Services 2013

### Access Services 2013

Access Services 2013 was removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft Power Apps and Power Automate as potential alternatives to Access Services 2013.

Classic authentication mode for content web applications

### Classic authentication mode for content web applications

Classic authentication mode was removed and is no longer supported by Microsoft for content web applications in SharePoint Server Subscription Edition. Content web applications will now only support claims authentication mode. The Central Administration web application continues to use and support classic authentication mode.

Groove sync app support

### Groove sync app support

Groove sync app support was removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring the Microsoft OneDrive sync app as the replacement for the Groove sync app.

Lists web service APIs for Groove sync app

### Lists web service APIs for Groove sync app

The Lists web service APIs for Groove sync app were removed and are no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring the Microsoft OneDrive sync app as the replacement for the Groove sync app.

PerformancePoint Services

### PerformancePoint Services

PerformancePoint Services had a significant dependency on Microsoft Silverlight, which is a technology that is no longer be supported as of October 12, 2021. PerformancePoint Services was removed from SharePoint Server Subscription Edition. We recommend exploring Microsoft Power BI as an alternative to PerformancePoint Services as we're making many new business intelligence investments in Power BI.

Stsadm.exe command-line tool

### Stsadm.exe command-line tool

The stsadm.exe command-line administration tool was removed from SharePoint Server Subscription Edition. SharePoint PowerShell cmdlets can be used to administer SharePoint from the command line or through scripting.

Update-SPHelp PowerShell cmdlet

### Update-SPHelp PowerShell cmdlet

As SharePoint PowerShell cmdlets were converted from snap-ins to modules in SharePoint Server Subscription Edition, the Update-SPHelp cmdlet is no longer necessary to download the latest cmdlet help content. The Update-Help cmdlet will now be able to download the latest help content for SharePoint PowerShell cmdlets.

Claims to Windows Token Service

### Claims to Windows Token Service

The Claims to Windows Token Service (C2WTS) was removed from SharePoint Server Subscription Edition. The service still appears in the Central Administration site, but the backing Windows service isn't installed, so the SharePoint service won't start. Trying to start the service in Central Administration results in error: **SPWindowsTokenServiceInstance: could not find c2wtshost.exe.config. Please edit the configuration manually.**

SharePoint Server Subscription Edition replaced Windows Identity Foundation (WIF) 3.5 with WIF 4.5, in which the Claims to Windows Token Service and its associated classes are removed. If you have a custom solution that depends on the C2WTS, you may need to adjust it to work with WIF 4.5. See Guidelines for Migrating an Application Built Using WIF 3.5 to WIF 4.5 for more information.

Legacy Cloud Hybrid Search

### Legacy Cloud Hybrid Search

Search Content Service (SCS), an internal component of Cloud Hybrid Search in SharePoint in Microsoft 365 will be retired starting June 30, 2025. To continue using Cloud Hybrid Search by then, upgrade your SharePoint Server farm to SharePoint Server Subscription Edition (SPSE) Version 25H1 or later versions. Without this upgrade, previous versions of SPSE can only search for on-premises and Microsoft 365 content separately through Hybrid Federated Search after this retirement.

Additional resources

## Additional resources

- Last updated on 
		2025-03-11
