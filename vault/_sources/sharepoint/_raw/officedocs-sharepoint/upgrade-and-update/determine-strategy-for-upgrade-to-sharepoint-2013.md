---
title: "Determine strategy for upgrade to SharePoint 2013 - SharePoint Server"
description: "Understand how to minimize downtime and plan for special cases during an upgrade to SharePoint."
ms.topic: upgrade-and-migration-article
---
Note

Determine strategy for upgrade to SharePoint 2013

# Determine strategy for upgrade to SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When you upgrade your environment to SharePoint 2013, you want to limit how much downtime that users experience. You might also have a special case that you must address during upgrade. This article describes how to minimize downtime and work with these special cases.

In addition to the information in this article, make sure that you read Review supported editions and products for upgrading to SharePoint 2013 to understand exactly which upgrade situations are valid and lead to successful upgrades.

How to minimize downtime during upgrade

## How to minimize downtime during upgrade

The following table lists the techniques that you can use during upgrade to reduce the time that users can't access their content or to potentially increase upgrade performance.

**Read-only databases** You can use read-only databases to continue to provide read-only access to content during the upgrade process. For this approach, you set the databases to read-only on the original farm while the upgrade is in progress on another farm. This method reduces perceived downtime for users. Also, if you encounter a problem with upgrade, you can restore the read-only farm to read-write and restore access to users while you rework your plans before you try upgrade again.

**Parallel database upgrades** You can attach and upgrade multiple databases at a time to speed up the upgrade process overall. The maximum number of parallel upgrades depends on your hardware. This results in faster overall upgrade times for your environment. However, you must monitor the progress and your servers to make sure that the performance is acceptable, and for large databases, parallel upgrades can be slower than single upgrades.

For more information about upgrade performance, see Plan for performance during upgrade to SharePoint 2013 and Use a trial upgrade to SharePoint 2013 to find potential issues.

The instructions for using these techniques are included in Upgrade content databases from SharePoint 2010 to SharePoint 2013.

Special cases

## Special cases

You might have other requirements or additional goals that you want to achieve when you perform an upgrade. The following table lists special cases and describes how to approach upgrade for each case.

| Case | Upgrade approach |
| --- | --- |
| Upgrading an environment that uses forms-based authentication? | Additional steps are required to upgrade when you're using forms-based authentication. For more information, see Configure forms-based authentication for a claims-based web application in SharePoint Server. |
| Upgrading very large databases? | In general, very large databases—especially databases that have a large number or large size of document versions inside them—take longer to upgrade than smaller databases. However, the complexity of the data determines how long it takes to upgrade, not the size of the database itself. If the upgrade process times out, it's usually because of connection issues. For more information about how long upgrade might take for your environment, see Plan for performance during upgrade to SharePoint 2013. |
| Upgrading from the server products in the Office 2007 release? | Use a database attach upgrade method to upgrade to SharePoint 2010 Products, and then upgrade to SharePoint 2013. |
| Upgrading from SharePoint Foundation 2010 to SharePoint 2013? | Attach and upgrade the content databases from SharePoint Foundation 2010 to SharePoint 2013. |
| Changing languages? | You have two choices, depending on whether a single site or your whole environment is changing languages:  
  To change the multiple user interface (MUI) language for a specific site, upgrade in the same language, and then install the new language pack and change to that language. 

 **CAUTION** 
 **You must have the appropriate language packs installed to upgrade any sites based on a localized site definition.** If you don't have the new language pack, the sites won't be available. Wait for the new language packs to be released before you try to upgrade those sites. 

 To change the installation language for your environment, set up your new environment in the new language, and then attach and upgrade your databases in the new language. |

See also

## See also

Other Resources

#### Other Resources

Plan for performance during upgrade to SharePoint 2013

Review supported editions and products for upgrading to SharePoint 2013

Use a trial upgrade to SharePoint 2013 to find potential issues

Overview of the upgrade process from SharePoint 2010 to SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-26
