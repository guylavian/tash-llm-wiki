---
title: "Optimize performance for SharePoint Server 2013 - SharePoint Server"
description: "Learn about the techniques and tools available for optimizing SharePoint Server 2013 performance."
ms.topic: how-to
---
Note

Optimize performance for SharePoint Server 2013

# Optimize performance for SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the techniques and tools available for optimizing SharePoint Server 2013 performance.

This article provides information about techniques and tools for optimizing SharePoint Server 2013 performance.

Optimizing performance

## Optimizing performance

There are many technologies and techniques available to optimize SharePoint Server 2013 performance. In a given environment, some or all of these techniques may apply.

Using BranchCache to optimize WAN performance

### Using BranchCache to optimize WAN performance

BranchCache is a feature of the Windows 7, Windows 8, Windows Server 2008 R2 and Windows Server 2012 operating systems that caches content from file and web servers on a wide area network (WAN) on computers at a local branch office. In a geographically distributed SharePoint Server 2013 environment, BranchCache can optimize WAN performance by caching large files that users download from SharePoint Server 2013.

After you install and configure BranchCache, a computer on the branch office network caches files that branch office users download from SharePoint Server 2013. BranchCache also stores file version metadata when the following Office applications access files:

OneNote

Word

Excel

Visio

PowerPoint

Every time a branch office user requests a cached file from SharePoint Server 2013, BranchCache checks to see if a more recent file exists on the server. If not, BranchCache will serve the cached version of the file.

For more information about BranchCache, see the following resources:

BranchCache Overview for Windows 8 and Windows Server 2012

BranchCache Overview for Windows 7 and Windows Server 2008 R2

BranchCache Deployment Guide for Windows 8 and Windows Server 2012

BranchCache Deployment Guide for Windows 7 and Windows Server 2008 R2

Configuring BranchCache for use with SharePoint Server 2013

#### Configuring BranchCache for use with SharePoint Server 2013

This section describes how to install and configure BranchCache for use with SharePoint Server 2013.

- Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

You must be logged in as a farm administrator to enable BranchCache for SharePoint Server 2013.

You must be logged in as a domain administrator or local computer administrator to install and enable BranchCache on a Windows 7 or Windows Server computer.

- Deploy BranchCache on each web server in your SharePoint Server 2013 farm by following the instructions in the following topics:

For Windows Server 2012, see Install Content Servers that Use the BranchCache Feature.

For Windows Server 2008 R2, see Install content servers that use the BranchCache feature.

- Deploy BranchCache in your branch office network environment by following the instructions in the following topics:

For Windows 8 and Windows Server 2012, see the BranchCache Deployment Guide.

For Windows 7 and Windows Server 2008 R2, see the BranchCache Deployment Guide

- If you have deployed BranchCache in Distributed mode, and the AuthNoEncap policy is enabled in your environment, you must install the update described in Performance issue when you enable the AuthNoEncap policy to handle large payloads in a network environment in Windows 7 or in Windows Server 2008 R2 on all Windows 7 client computers.

After you have installed and configured BranchCache in the operating system of each web server in your SharePoint Server 2016 farm and each computer in your branch office, content in SharePoint Server 2013 will be cached automatically, and no further configuration is required.

See also

## See also

Concepts

#### Concepts

Performance planning in SharePoint Server 2013

Other Resources

#### Other Resources

Plan for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
