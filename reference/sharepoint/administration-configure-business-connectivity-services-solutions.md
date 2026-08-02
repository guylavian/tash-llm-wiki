---
title: "Configure Business Connectivity Services solutions for SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-business-connectivity-services-solutions
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-business-connectivity-services-solutions
family: administration
documentKind: "install-set-up-deploy"
abstract: "Find links to steps that will help you install and configure SharePoint Server Business Connectivity Services (BCS). Choose from on-premises, cloud-only, and hybrid BCS solutions."
---

# Configure Business Connectivity Services solutions for SharePoint Server - SharePoint Server

Note

Configure Business Connectivity Services solutions for SharePoint Server

# Configure Business Connectivity Services solutions for SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article is your starting place for the procedures to install common Microsoft Business Connectivity Services scenarios for SharePoint Server 2016. The Business Connectivity Services solution that you deploy will most likely look different from the solutions presented here, but you can model your installation on these examples. Also, you can select the individual procedures from here to build your own procedural documents for your Business Connectivity Services solution scenario.

Choose the Business Connectivity Services scenario that meets your needs

## Choose the Business Connectivity Services scenario that meets your needs

Every Business Connectivity Services solution is unique because each business has unique data integration problems that it solves with Business Connectivity Services. The solutions can range from something simple and straightforward that a power user or IT professional (who has the appropriate permissions) can perform by themselves, to complex solutions that require developer, IT professional, and end-user solution development involvement.

This guide presents the configuration choices for the common scenarios.

**On-premises deployment** All the Business Connectivity Services components are under your organizations control behind your firewall.

**Cloud-only deployment** All the Business Connectivity Services components are in SharePoint in Microsoft 365.

**Hybrid deployment** SharePoint in Microsoft 365 uses Business Connectivity Services to connect to data that lives in the cloud.

Prerequisites

## Prerequisites

Before you begin with any Business Connectivity Services scenario configuration, make sure that you have read Overview of Business Connectivity Services in SharePoint Server and completed the steps in Plan a Business Connectivity Services solution in SharePoint Server.

On-premises deployment

## On-premises deployment

The procedures in Deploy a Business Connectivity Services on-premises solution in SharePoint Server show you how to deploy a solution that involves the following:

A Business Connectivity Services infrastructure that is on your corporate network.

Information workers who access the Business Connectivity Services solution are on your corporate network.

External content that is surfaced in SharePoint as an external list.

External content that is synchronized into Microsoft Outlook for offline use.

Accessing external data that is in SQL Server database on your corporate network.

SharePoint Designer 2013 to create the external content type for the SQL Server data source.

The Secure Store Service to manage mapping of user credentials to group credentials for accessing the external systems.

Cloud-only deployment

## Cloud-only deployment

The procedures in Make an External List from a SQL Azure table with Business Connectivity Services and Secure StoreDeploy a Business Connectivity Services cloud-only solution in SharePoint 2013 show you how to deploy a solution that involves a Business Connectivity Services infrastructure that is in SharePoint in Microsoft 365.

Hybrid deployment

## Hybrid deployment

The procedures in Deploy a Business Connectivity Services hybrid solution in SharePoint shows you how to publish on-premises data to an external list or app for SharePoint in Microsoft 365.

Note

Business Connectivity Services (BCS) has retired in Microsoft 365. Its features are no longer available and can't be enabled. This applies to all environments including Government Clouds and Department of Defense. For more information, see BCS retirement in Microsoft 365.

See also

## See also

Additional resources

## Additional resources

- Last updated on 
		2025-02-24
