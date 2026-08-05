---
title: "Description of MinRole and associated services in SharePoint Servers 2016, 2019, and Subscription Edition - SharePoint Server"
description: "Learn about the MinRole feature in SharePoint Server and the services that are associated with each server role."
ms.topic: overview
---
Note

Description of MinRole and associated services in SharePoint Servers 2016, 2019, and Subscription Edition

# Description of MinRole and associated services in SharePoint Servers 2016, 2019, and Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The MinRole feature in SharePoint Servers 2016, 2019 and Subscription Edition lets SharePoint farm administrators assign each server's role in a farm topology. The role of a server is specified when you create a new farm or join a server to an existing farm.

This article describes the services associated with each server role. These services are listed in **Central Administration** > **System settings** > **Manage services in this farm**, or by running the Get-SPService cmdlet. The service instances for some services are hidden because they are internal to the operation of SharePoint and not meant to be directly controlled. To retrieve a list of services instances on a server, including hidden services, use this syntax,  `(Get-SPServer <server_name>).ServiceInstances`.

Note

The services listed are the list of what will be running on each server role if all of the services are enabled. Services associated with service applications will only be enabled if the farm administrator provisions that service application. Services that aren't associated with service applications will only be running if Auto Provision is enabled on that service.

For more information about the MinRole feature, see Overview of MinRole Server Roles in SharePoint Servers 2016, 2019 and Subscription Edition.

MinRole and associated services for each server role

## MinRole and associated services for each server role

The following table shows the services for each server role.

| Server role | Services |
| --- | --- |
| Front-end | Access Services  
  Access Services 2010  
  App Management Service  
  Business Data Connectivity Service  
  Claims to Windows Token Service  
  Machine Translation Service  
  Managed Metadata Web Service  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Sandboxed Code Service  
  Microsoft SharePoint Foundation Subscription Settings Service  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Foundation Web Application  
  Microsoft SharePoint Insights  
  PerformancePoint Service  
  Project Server Application Service  
  Request Management  
  Secure Store Service  
  User Profile Service  
  Visio Graphics Service  
 **Note**: Access Services, Access Service 2010, Claims to Windows Token Service, and PerformancePoint Service are not available in Subscription Edition. 
 **Note**: The list of **hidden services** are:  
  Information Management Policy Configuration Service  
  Microsoft Project Server Calculation Service  
  Microsoft Project Server Events Service  
  Microsoft Project Server Queuing Service  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service |
| Application | App Management Service  
  Application Discovery and Load Balancer Service  
  Business Data Connectivity Service  
  Claims to Windows Token Service  
  Machine Translation Service  
  Managed Metadata Web Service  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Incoming E-Mail  
  Microsoft SharePoint Foundation Subscription Settings Service  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Foundation Web Application  
  Microsoft SharePoint Foundation Workflow Timer Service  
  Microsoft SharePoint Insights  
  PowerPoint Conversion Service  
  Project Server Application Service  
  Request Management  
  Secure Store Service  
  User Profile Service  
  Word Automation Services  
 **Note**: Claims to Windows Token Service is not available in Subscription Edition. 
 **Note**: The list of **hidden services** are:  
  Information Management Policy Configuration Service  
  Microsoft Project Server Calculation Service  
  Microsoft Project Server Events Service  
  Microsoft Project Server Queuing Service  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service |
| Distributed cache | Distributed Cache  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Insights  
 **Note**: The list of **hidden services** are:  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service  
 **Note**: If the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1) or higher is not installed, the following services will also be assigned to this role:  
  Claims to Windows Token Service  
  Microsoft SharePoint Foundation Web Application  
  Request Management |
| Search | Application Discovery and Load Balancer Service  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Insights  
  Search Administration Web Service  
  Search Host Controller Service  
  Search Query and Site Settings Service  
  SharePoint Server Search  
 **Note**: The list of **hidden services** are:  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service  
 **Note**: If the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1) or higher is not installed, the following service will also be assigned to this role:  
  Claims to Windows Token Service |
| Custom | Distributed Cache  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Foundation Web Application |
| Single-server farm | Access Services  
  Access Services 2010  
  App Management Service  
  Application Discovery and Load Balancer Service  
  Business Data Connectivity Service  
  Claims to Windows Token Service  
  Distributed Cache  
  Lotus Notes Connector  
  Machine Translation Service  
  Managed Metadata Web Service  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Incoming E-Mail  
  Microsoft SharePoint Foundation Sandboxed Code Service  
  Microsoft SharePoint Foundation Subscription Settings Service  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Foundation Web Application  
  Microsoft SharePoint Foundation Workflow Timer Service  
  Microsoft SharePoint Insights  
  PerformancePoint Service  
  PowerPoint Conversion Service  
  Project Server Application Service  
  Request Management  
  Search Administration Web Service  
  Search Host Controller Service  
  Search Query and Site Settings Service  
  Secure Store Service  
  SharePoint Server Search  
  User Profile Service  
  Visio Graphics Service  
  Word Automation Services 
 **Note**: Access Services, Access Service 2010, Claims to Windows Token Service, and PerformancePoint Service are not available in Subscription Edition. 
 **Note**: The list of **hidden services** are:  
  Information Management Policy Configuration Service  
  Microsoft Project Server Calculation Service  
  Microsoft Project Server Events Service  
  Microsoft Project Server Queuing Service  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service |
| Front-end with Distributed Cache | Access Services  
  Access Services 2010  
  App Management Service  
  Business Data Connectivity Service  
  Claims to Windows Token Service  
  Distributed Cache  
  Machine Translation Service  
  Managed Metadata Web Service  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Sandboxed Code Service  
  Microsoft SharePoint Foundation Subscription Settings Service  
  Microsoft SharePoint Foundation Timer  
  Microsoft SharePoint Foundation Web Application  
  Microsoft SharePoint Insights  
  PerformancePoint Service  
  Project Server Application Service  
  Request Management  
  Secure Store Service  
  User Profile Service  
  Visio Graphics Service 
 **Note**: Access Services, Access Service 2010, Claims to Windows Token Service, and PerformancePoint Service are not available in Subscription Edition. 
 **Note**: The list of **hidden services** are:  
  Information Management Policy Configuration Service  
  Microsoft Project Server Calculation Service  
  Microsoft Project Server Events Service  
  Microsoft Project Server Queuing Service  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service |
| Application with Search | App Management Service  
  Application Discovery and Load Balancer Service  
  Business Data Connectivity Service  
  Claims to Windows Token Service  
  Machine Translation Service  
  Managed Metadata Web Service  
  Microsoft SharePoint Foundation Administration  
  Microsoft SharePoint Foundation Incoming E-Mail  
  Microsoft SharePoint Foundation Subscription Settings Service  
  Microsoft SharePoint Foundation Timer  
 Microsoft SharePoint Foundation Web Application  
  Microsoft SharePoint Foundation Workflow Timer Service  
  Microsoft SharePoint Insights  
  PowerPoint Conversion Service  
  Project Server Application Service  
  Request Management  
  Search Administration Web Service  
 Search Host Controller Service  
 Search Query and Site Settings Service  
  Secure Store Service  
  SharePoint Server Search  
  User Profile Service  
  Word Automation Services  
 **Note**: Claims to Windows Token Service is not available in Subscription Edition. 
 **Note**: The list of **hidden services** are:  
  Information Management Policy Configuration Service  
  Microsoft Project Server Calculation Service  
  Microsoft Project Server Events Service  
  Microsoft Project Server Queuing Service  
  Microsoft SharePoint Foundation Tracing  
  Microsoft SharePoint Foundation Usage  
  Portal Service  
  Security Token Service  
  SSP Job Control Service |

See also

## See also

Concepts

#### Concepts

Overview of MinRole Server Roles in SharePoint Servers 2016, 2019 and Subscription Edition

What's deprecated or removed from SharePoint Server Subscription Edition

Other Resources

#### Other Resources

Planning for a MinRole server deployment in SharePoint Servers 2016, 2019 and Subscription Edition

Managing a MinRole Server Farm in SharePoint Servers 2016, 2019, and Subscription Edition

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
