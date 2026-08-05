---
title: "Prerequisites for reporting"
type: reference
domain: sccm
slug: core-prerequisites-for-reporting
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/prerequisites-for-reporting
family: core
documentKind: "article"
abstract: "Understand various dependencies that impact your use of reporting in Configuration Manager."
---

# Prerequisites for reporting

# Prerequisites for reporting in Configuration Manager

*Applies to: Configuration Manager (current branch)*

Reporting in Configuration Manager has the following dependencies:

- SQL Server Reporting Services
- Reporting services point
- Power BI Report Server (optional, starting in version 2002)

## SQL Server Reporting Services

Before you can use reporting in Configuration Manager, install and configure SQL Server Reporting Services.

For more information about planning and deploying Reporting Services, see the [Install SQL Server Reporting Services](/sql/reporting-services/install-windows/install-reporting-services).

Install the Reporting Services database on either the default instance or a named instance of a 64-bit SQL Server installation. Colocate the SQL Server instance with the site system server, or configure it on a remote computer.

Configuration Manager supports the same versions of SQL Server for reporting as it does for the site database. For more information, see [Supported SQL Server versions](../../plan-design/configs/support-for-sql-server-versions.md#bkmk_SQLVersions).

## Reporting services point

Before you can use reporting in Configuration Manager, configure the reporting services point site system role.

For more information, see [Site and site system prerequisites](../../plan-design/configs/site-and-site-system-prerequisites.md#reporting-services-point).

## Power BI Report Server

Starting in version 2002, you can integrate reporting with Power BI Report Server. For more information including prerequisites, see [Integrate with Power BI Report Server](powerbi-report-server.md).

## Next steps

[Configure reporting](configuring-reporting.md)
