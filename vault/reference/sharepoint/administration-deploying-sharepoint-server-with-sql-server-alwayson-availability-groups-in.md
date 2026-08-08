---
title: "Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-deploying-sharepoint-server-with-sql-server-alwayson-availability-groups-in
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/deploying-sharepoint-server-with-sql-server-alwayson-availability-groups-in
family: administration
documentKind: "install-set-up-deploy"
abstract: "Get an overview of deploying SharePoint Server in Microsoft Azure with links to each phase of the deployment."
---

# Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure - SharePoint Server

Note

Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure

# Deploying SharePoint Server with SQL Server Always On Availability Groups in Azure

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Step through the deployment an intranet-only, high availability SharePoint Server farm in Azure with these virtual machines:

Two SharePoint front end and distributed cache servers

Two SharePoint application and search servers

One cluster majority node server

Two domain controllers

Here is the configuration, with placeholder names for each server.

**An intranet-only, high availability SharePoint Server farm in Azure**

Two virtual machines for each role ensure high availability. All of the virtual machines are in a single cross-premises Azure virtual network. Each group of virtual machines for a specific role is in its own subnet and availability set.

Note

Because this VNet is connected to the on-premises network, this configuration does not include jumpbox or monitoring virtual machines on a management subnet. For more information, see Running Windows VMs for an N-tier architecture.

Bill of materials

## Bill of materials

This baseline configuration requires the following set of Azure services and components:

Nine virtual machines.

Four availability sets.

One cross-premises virtual network with five subnets.

One Azure subscription.

Here are the virtual machines and their default sizes for this configuration.

| **Item** | **Virtual machine description** | **Gallery image** | **Default size** |
| --- | --- | --- | --- |
| 1. | First domain controller | Windows Server 2016 Datacenter | D2 |
| 2. | Second domain controller | Windows Server 2016 Datacenter | D2 |
| 3. | First database server | Microsoft SQL Server 2016 Enterprise - Windows Server 2016 | DS4 |
| 4. | Second database server | Microsoft SQL Server 2016 Enterprise - Windows Server 2016 | DS4 |
| 5. | Majority node for the cluster | Windows Server 2016 Datacenter | D2 |
| 6. | First SharePoint application and search server | Microsoft SharePoint Server 2016 Trial - Windows Server 2012 R2 | DS4 |
| 7. | Second SharePoint application and search server | Microsoft SharePoint Server 2016 Trial - Windows Server 2012 R2 | DS4 |
| 8. | First SharePoint front end and distributed cache server | Microsoft SharePoint Server 2016 Trial - Windows Server 2012 R2 | DS4 |
| 9. | Second SharePoint front end and distributed cache server | Microsoft SharePoint Server 2016 Trial - Windows Server 2012 R2 | DS4 |

To compute the estimated costs for this configuration, see the Azure pricing calculator.

Note

The Azure Pricing Calculator does not include the additional costs for the SQL Server license for the two virtual machines running SQL Server 2016 Enterprise. See Virtual Machines Pricing-SQL for more information.

Phases of deployment

## Phases of deployment

You deploy this SharePoint Server farm with the following phases:

SharePoint Intranet Farm in Azure Phase 1: Configure Azure

Create resource groups, availability sets, and a cross-premises virtual network.

SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers

Create and configure replica Windows Server Active Directory (AD) domain controllers

Note

SharePoint Server also supports the use of Microsoft Entra Domain Services as a substitute for virtual machines running as domain replicas. However, at this time, this deployment guide only describes the use of virtual machine-based replica domain controllers.

SharePoint Intranet Farm in Azure Phase 3: Configure SQL Server Infrastructure

Create and configure the SQL Server virtual machines, prepare them for use with SharePoint, and create the cluster.

SharePoint Intranet Farm in Azure Phase 4: Configure SharePoint servers

Create and configure the four SharePoint server virtual machines.

SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases

Prepare databases and create a SQL Server Always On availability group.

This configuration is a prescriptive, phase-by-phase guide for a predefined architecture to create a highly available intranet SharePoint Server farm in Azure infrastructure services. Keep the following in mind:

If you are an experienced SharePoint implementer, feel free to adapt the instructions in phases 3 through 5 and build the farm that best suits your needs.

If you already have an existing Azure hybrid cloud deployment, feel free to adapt or skip the instructions in phases 1 and 2 and host the new SharePoint farm on the appropriate set of subnets.

To build a dev/test environment or a proof-of-concept of this configuration, see Intranet SharePoint Server in Azure dev/test environment.

Next step

## Next step

Start the configuration with SharePoint Intranet Farm in Azure Phase 1: Configure Azure.

See also

## See also

Concepts

#### Concepts

Install SharePoint Server

Other Resources

#### Other Resources

SharePoint Server in Microsoft Azure

Designing a SharePoint Server farm in Azure

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
