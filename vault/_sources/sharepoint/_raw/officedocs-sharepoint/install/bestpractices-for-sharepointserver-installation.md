---
title: "Best Practices for SharePoint Server Installation - SharePoint Server"
description: "Learn the best practices for SharePoint Server installation and how it gets your servers ready for easy transition to the cloud."
ms.topic: best-practice
---
Note

Best practices for installation for SharePoint Servers 2016 and 2019

# Best practices for installation for SharePoint Servers 2016 and 2019

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Introduction

## Introduction

Installing a new version gives the opportunity to review what you have done in the past, currently and envision your goals going forward.

As you prepare for your installation, consider the following:

Are you staying on Server (on-premises) for the foreseeable future?

Do you currently have existing pieces of your system in the cloud?

What customizations or features do you no longer use?

Are you ready for a modern approach?

What is working well now, and what isn't?

Evaluating what features or services are no longer supported

## Evaluating what features or services are no longer supported

As you install a new version of SharePoint Server, take time to evaluate any service applications or features that you currently rely on that are no longer supported or listed as "deprecated."

If you have a reliance on any of the following, plan what you intend to replace that functionality with or if it's no longer being used actively by your company and it's time to phase it out.

Use supported service applications and consider phasing out the use of these deprecated service applications. For any of the SharePoint BI tools, you can use Power BI as a replacement:

| Deprecated feature or service |
| --- |
| Access Services and Access Services 2010 |
| Document Conversions services |
| Lotus Notes Connector |
| Machine Translation Services |
| PerformancePoint Service |
| PowerPoint Conversion Service |
| Visio Graphics Service |
| Word Automation Services |
| InfoPath |
| Workflow Manager |

Customizations

## Customizations

If you currently have SharePoint Server installed, chances are you have made some customizations to suit your business needs.

If you already have a portion of your company in the cloud or plan to do so in the future, know that certain customizations won't transfer to SharePoint. Here's a list of few of those:

Workflows, User Alerts, and custom master pages won't transfer to SharePoint. We recommend you use Power Automate for workflows, reconfigure alerts once migrated, and use the out of the box customization for site look and feel changes.

Custom Search schema won't transfer to SharePoint. When content is migrated to SharePoint, you may want to reimplement any custom Search schema configuration necessary.

Use SharePoint Add-ins with the Low Trust model. To learn more, see Creating SharePoint add in that use low trust authorization.

Use SharePoint Framework solutions for custom business solutions. To get started, see SharePoint Framework Overview.

Connect your data the modern way

## Connect your data the modern way

Do you use Business Data Connectivity Services (BCS) for any of your data connections? Are your data sources available by using a web service? Verify all data sources are available via other means, such as a web service.

- Where is your data? Where will it reside?

Instead of using BCS to display your data, you could use Power BI and a Data Management Gateway.

Adopt the modern features

## Adopt the modern features

If a portion of your sites is already in the cloud, or if you intend on moving online in the future, adopting the modern features now will help "futureproof" your installation.

Use Microsoft 365 Groups and Power Automate.   Retire the use of email, Site mailboxes, or Mobile Accounts (SMS/Text Messaging)

Solutions that intercept and/or modify the HTTP pipeline you could use Azure Conditional Access Policies by fronting the farm by using the Microsoft Entra application proxy. For more information on how to use AD FS, see Access Control Policies in Windows Server 2016 AD FS.

Implement only the necessary Web Application Policies, such as self-service site creation, Object Cache, and Search Crawler accounts, but try to avoid further usage of Web Application Policies as they aren't available in SharePoint.

For security purposes, phase out the use of anonymous SharePoint Server sites. Also note that anonymous site access isn't available in SharePoint in Microsoft 365.

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
