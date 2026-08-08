---
title: "Choose a disaster recovery strategy for SharePoint Server - SharePoint Server"
description: "Understand the disaster recovery options and supported technologies for recovering a SharePoint Server farm if there is a disaster."
ms.topic: article
---
Note

Choose a disaster recovery strategy for SharePoint Server

# Choose a disaster recovery strategy for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

We define disaster recovery as the ability to recover from a situation in which the primary data center that hosts a SharePoint Server farm is unable to continue to operate. Regardless of the nature of event and its cause, the data center outage is significant enough to set into motion the actions defined in your organization's disaster recovery plan. This means putting a fully operational farm into production using computer resources that are located in a data center that is not affected by the event.

SharePoint Servers 2019, 2016, 2013, and the SQL Servers that support them provide configuration and content recovery options that can meet the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) that are required for your business if there is a disaster. For more information about these and other disaster recovery concepts, see High availability and disaster recovery concepts in SharePoint Server.

Introduction

## Introduction

An effective disaster recovery strategy for a SharePoint Server farm must be sufficient to meet your organization's business requirements, which are typically expressed by using two measures: Recovery Time Objective (RTO) and Recovery Point Objective (RPO). RTO and RPO requirements are derived by determining the downtime cost to the organization if a disaster happens.

Important

As a best practice we recommend that you clearly identify and quantify your organization's RTO and RPO before you develop a recovery strategy and implement a technical solution. Focus on what is required, not how to do it.

Downtime costs vary significantly between and within industries, especially due to the different effects of downtime. Business size is the most obvious factor. However, it is not the only one. Setting a measure means establishing the nature and implications of the failure. Reduced to the simplest level, a failure of a critical application could lead to the following types of losses:

Loss of the application service. The effect of downtime varies with the application and the business.

Loss of data. The potential loss of data due to a system outage can have significant legal and financial impact.

Most organizations will incur a downtime cost from both of the previous types of loss but the nature of the business will determine which type of loss has the biggest effect. The following article, written by Chris Preimesberger at eWEEK, highlights the financial effect of data center downtime. Unplanned IT Downtime Can Cost $5K Per Minute: Report.

In most scenarios, SharePoint products is one of several applications that must be recovered in the event of a data center shutdown that qualifies as a disaster. For this reason we have not included information about disaster recovery planning but focus on options for making sure that you can recover your SharePoint Server farm at another location.

Regardless of the type and scale of a disaster, recovery involves the use of a standby data center that you can recover the farm to.

Standby data center recovery options

## Standby data center recovery options

Standby data centers are required for scenarios where local redundant systems and backups cannot recover from the outage at the primary data center. The time and immediate effort to get a replacement farm up and running in a different location is often known as a hot, warm, or cold standby. Our definitions for these farm recovery data centers are as follows:

**Cold standby**. A secondary data center that can provide availability within hours or days.

**Warm standby**. A secondary data center that can provide availability within minutes or hours.

**Hot standby**. A secondary data center that can provide availability within seconds or minutes.

Each of these standby data centers has specific characteristics and requirements, and also an associated cost to operate and maintain.

Cold standby disaster recovery strategy: A business ships backups to support bare metal recovery to local and regional offsite storage regularly, and has contracts in place for emergency server rentals in another region.

**Pros:** Often the cheapest option to maintain, operationally. Often an expensive option to recover, because it requires that physical servers be configured correctly after a disaster has occurred.

**Cons:** The slowest option to recover.

Warm standby disaster recovery strategy with Azure Site Recovery.

**Pros:** Often fairly inexpensive to recover, because a virtual server farm can require little configuration upon recovery.

**Cons:** Can be very expensive and time-consuming to maintain.

Hot standby disaster recovery strategy: A business runs multiple data centers, but serves content and services through only one data center.

**Pros:** Often fairly fast to recover.

**Cons:** Can be very expensive to configure and maintain.

Important

No matter which of the previous disaster recovery solutions that you decide to apply, there is likely going to be some data loss.

Cold standby recovery

### Cold standby recovery

In a cold standby disaster recovery scenario, you recover by setting up a new farm in a new location (preferably by using a scripted deployment) and restoring backups. Or, you can recover by restoring the farm using a backup solution such as System Center - Data Protection Manager (DPM). DPM protects your data at the computer operating system level and lets you restore each server individually. This article does not contain detailed instructions for how to create and recover in cold standby scenarios. For more information, see:

Overview of backup and recovery in SharePoint Server

Plan for backup and recovery in SharePoint Server

Warm standby recovery

### Warm standby recovery

In a warm standby disaster recovery scenario, you create a warm standby environment by creating a duplicate farm at the alternate data center and ensure that it is updated regularly by using full and incremental backups of the primary farm.

**Virtual warm standby environments**

Virtualization provides a workable and cost effective option for a warm standby recovery solution. You can use Hyper-V as an in-house solution or Azure as a hosted solution to provide necessary infrastructure for recovery. For more information, see Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure

Hot standby recovery

### Hot standby recovery

In a hot standby disaster recovery scenario, you set up a failover farm in the standby data center so that it can assume production operations almost immediately after the primary farm goes offline. An environment that has a separate failover farm has the following characteristics:

A separate configuration database and the SharePoint Central Administration website content database must be maintained on the failover farm.

All customizations must be deployed on both farms.

Tip

There is consistency between the two farms and to reduce the possibility of error we recommend that you use scripted deployment to create the primary and failover farm by using the same configuration settings and customizations.

Operating system, SQL Server and SharePoint Server software updates must be applied to both farms, to maintain a consistent configuration across both farms.

You can copy SharePoint Server content databases to the failover farm by using asynchronous mirroring, asynchronous commit on an availability group replica, or log-shipping.

Note

SQL Server mirroring can only be used to copy databases to a single mirror server, but you can log-ship to multiple secondary servers.

The SQL Server database mirroring feature will be removed in future versions. We recommend that you avoid using this feature in new deployments. Plan to change applications that currently use this feature. Use Always On Availability Groups instead.

Service applications vary in whether they can be log-shipped to a farm. For more information, see Service application redundancy later in this article.

The hot standby farm topology can be repeated across more than one data center, as long as you configure SQL Server log shipping to one or more additional data centers.

Important

Available network bandwidth and latency are major considerations when you are using a failover approach for disaster recovery. We recommend that you consult with your SAN vendor to determine whether you can use SAN replication for SQL databases or another supported mechanism to provide the hot standby level of availability across data centers. Note that using SAN replication for SharePoint servers is not supported.

Service application redundancy

### Service application redundancy

To provide availability across data centers for service applications, we recommend that for the services that can be run cross-farm, you run a separate services farm that can be accessed from both the primary and the secondary data centers.

For services that cannot be run cross-farm, and to provide availability for the services farm itself, the strategy for providing redundancy across data centers for a service application varies. The strategy employed depends on whether:

There is business value in running the service application in the disaster recovery farm when it is not being used.

The databases associated with the service application can be log-shipped, asynchronously mirrored, or replicated using asynchronous commit.

The service application can run against read-only databases.

Review the Supported high availability and disaster recovery options for SharePoint databases article before designing a disaster recovery solution that uses a warm or hot standby data center.

System requirements for recovery

## System requirements for recovery

In an ideal scenario, the failover components and systems match the primary components and systems in all ways: platform, hardware, and number of servers. At a minimum, the failover environment must be able to handle the traffic that you expect during a failover. Keep in mind that only a subset of users may have to be served by the failover site. The systems must match in at least the following:

Operating system version and all updates

SQL Server versions and all updates

SharePoint Server versions and all updates

In addition to the previous requirements, farm recovery time will also be affected by availability of facilities and infrastructure components. Make sure that the following requirements are met:

Power, cooling, network, directory, and SMTP are fully redundant

Choose a switching mechanism; whether DNS or hardware load balancing, that meets your needs.

See also

## See also

Concepts

#### Concepts

High availability and disaster recovery concepts in SharePoint Server

Other Resources

#### Other Resources

What workloads can you protect with Azure Site Recovery?

Replicate a multi-tier SharePoint application for disaster recovery using Azure Site Recovery

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
