---
title: "Plan service deployment in SharePoint Server - SharePoint Server"
description: "Learn about the services on the Services on Server page in the SharePoint Central Administration website and deployment guidance for these services. Many of these services are associated with service applications."
ms.topic: install-set-up-deploy
---
Note

Plan service deployment in SharePoint Server

# Plan service deployment in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

About Services on Server

## About Services on Server

The **Services on Server** page in Central Administration lists services that are started or stopped on specific servers in the farm. Some of these services are associated with service applications. After deploying service applications to the farm, go to the Services on Server page and make sure that the associated services are started on the appropriate servers. Some of these services are not associated with service applications.

Note

Note: Search components are deployed by using PowerShell instead of the **Services on Server** page.

After planning the farm topology, use this article to make sure that the appropriate services on server are started for each server in the farm. This may not be necessary for small farms in which all of the service applications and services are run on one server or two redundant servers.

This article lists recommended configuration of services and service applications for two different architecture approaches:

**Streamlined topologies** — The distribution of services and other components in a farm is intended to maximize system resources of server hardware. Streamlined architectures include Front-end servers, Application servers, Search servers, Distributedand database servers.

**Traditional topologies** — Topologies are based on traditional approaches to building architectures with Web servers, application servers, and database servers.

For more information about these SharePoint 2013 topology approaches, see the following models:

Streamlined Topologies for SharePoint Server 2013

Traditional Topologies for SharePoint Server 2013

For information about SharePoint Server 2016 topology, see the following model:

- Planning for a MinRole server deployment in SharePoint Server

Services on server for streamlined topologies in SharePoint 2013

## Services on server for streamlined topologies in SharePoint 2013

Note

The following table only apply to SharePoint 2013.

**Table: Service applications and Services on Server for streamlined topologies**

| **Service application** | **Services on server** | **MinRole server role** | **Additional information** |
| --- | --- | --- | --- |
| Access Services | Access Services | Front-end or Application server | Enables users of the Access 2013 client to create new Access service applications. View, edit, and interact with Access Services databases in a browser. |
| Access Services 2010 | Access Services 2010 | Front-end server | Allows continued maintenance of SharePoint 2010 Access service applications by using Access 2010 clients and Access 2013 clients. Does not allow users to create new applications. |
| App Management Service | App Management Service | Front-end or Application server |  |
| Business Data Connectivity | Business Data Connectivity service | Front-end or Application server |  |
| Excel Services | Excel Calculation Services | Front-end server or specialized server |  |
| Machine Translation Service | Machine Translation Service | Front-end or Application server | The Machine Translation Service uses SharePoint OAuth for file management. The Machine Translation Service Application's app pool account needs permissions to the User Profile Application to function correctly. The Machine Translation Service connects to the Microsoft Translator online service. Microsoft Translator may collect some data to improve the quality of translations. |
| Managed Metadata Service | Managed Metadata Web Service | Front-end or Application server |  |
| Microsoft SharePoint Foundation Subscription Settings Service | Microsoft SharePoint Foundation Subscription Settings Service | Front-end server | You must use Microsoft PowerShell to deploy this service. Start this service if you have deployed service applications in multi-tenant mode or if the farm includes sites that use site subscriptions. This service stores settings and configuration data for tenants in a multi-tenant environment. After you start this service, web applications consume the service automatically. |
| PerformancePoint | PerformancePoint Service | Front-end server |  |
| PowerPoint Conversion | PowerPoint Conversion Service | Application server | This service converts PowerPoint presentations to other formats. It typically runs on one or more application servers. It starts one or more worker processes to perform conversions. When actively converting, a worker process may use up a complete processor core. Memory usage depends on the size and content of files being converted. You can use Microsoft PowerShell cmdlets to control the number of worker processes that are used. Several other configuration options are also available through Microsoft PowerShell cmdlets. |
| Search | Lotus Notes Connector | Search server | To learn how to configure Lotus Notes Connector which crawls data on a Lotus Domino server, see the documentation. |
| Search | Search Host Controller Service | Search servers | This service manages the search topology components. The service is automatically started on all servers that run search topology components. |
| Search | Search Query and Site Settings Service | Search servers | This service load balances queries within the search topology. It also detects farm-level changes to the search service and puts these in the Search Admin database. The service is automatically started on all servers that run the query processing component. |
| Search | SharePoint Server Search | Search servers | This service crawls content for the search index. This service is automatically started on all servers that run search topology components. The service cannot be stopped or started from the Services on Server page. |
| Secure Store Service | Secure Store Service | Front-end or Application server |  |
| Usage and Health Data Collection |  |  | This service application has no associated service on server. |
| User Profile | User Profile Service | Front-end or Application server |  |
| User Profile | User Profile Synchronization Service | Front-end server |  |
| Visio Graphics Service | Visio Graphics Service | Front-end server |  |
| Word Automation Service | Word Automation Services | Application server | Performs automated bulk document conversions. When actively converting, this service will fully use one CPU for each worker process (configured in Central Administration). If the service is started on multiple servers, a job will be shared across all the servers. |
| Work Management | Work Management Service | Batch-processing server |  |
|  | Central Administration | Front-end or Application server | This service runs the Central Administration site. It can be put on a batch-processing server if security policies of an organization mandate this. |
|  | Claims to Windows Token Service | Application server |  |
|  | Distributed Cache | Distributed Cache OR Custom servers | By default this service is started on all web servers and application servers in a farm. |
|  | Document Conversions Launcher Service | Batch-processing servers | Schedules and starts the document conversions on a server. |
|  | Document Conversions Load Balancer Service | Batch-processing servers | Balances document conversion requests from across the server farm. Each web application can have only one load balancer registered with it at a time. |
|  | Microsoft SharePoint Foundation Incoming E-Mail | Application servers | Typically, this service runs on a web server. If you have to isolate this service, you can start it on an application server. |
|  | Microsoft SharePoint Foundation Sandboxed Code Service | Front-end servers | Start this service on computers that run sandboxed code in the farm. This can include front-end servers and batch-processing servers. This service runs code that is deployed as part of a sandboxed solution in a remote, rights-restricted process and measures the server resources that are used during execution against a site collection-scoped, daily quota. |
|  | Microsoft SharePoint Foundation Web Application | Front-end servers, batch-processing servers, plus the Distributed Cache and Request Management servers if these servers are implemented | This service provides web server functionality. It is started by default on web servers. Custom features scoped to web applications may not display in Central Administration as intended if this service is not started on the server running Central Administration and if the feature cannot be deployed globally. |
|  | Microsoft SharePoint Foundation Workflow Timer Service | Application server | This service is automatically configured to run on all web servers in a farm. |
|  | Request Management | Distributed Cache and Request Management tier | In integrated mode, Request Management runs on all web servers in a farm. In dedicated mode servers in a separate Request Management farm are between the hardware load balancer and one or more SharePoint farms. |

Services on Server for traditional topologies in SharePoint 2013

## Services on Server for traditional topologies in SharePoint 2013

Note

The following table only apply to SharePoint 2013.

**Table: Service applications and Services on Server for traditional topologies**

| **Service Application** | **Services on Server** | **Server Recommendation** | **More information** |
| --- | --- | --- | --- |
| Access Services 2010 | Access Services 2010 | Front-end Server | Allows continued maintenance of SharePoint 2010 Access service applications by using Access 2010 clients and Access 2013 clients. Does not allow users to create new applications. |
| Access Services | Access Services | Front-end Server | Allows creation of new Access service applications by using the Access 2013 client. View, edit, and interact with Access Services databases in a browser. |
| App Management Service | App Management Service | Front-end or Application Server |  |
|  |  |  |  |
| Business Data Connectivity | Business Data Connectivity service | Front-end or Application Server |  |
| Excel Calculation Services | Excel Calculation Services | Application Server |  |
| Machine Translation Service | Machine Translation Service | Front-end or Application Server | The Machine Translation Service uses SharePoint OAuth for file management. The Machine Translation Service Application's app pool account needs permissions to the User Profile Application to function correctly. The Machine Translation Service connects to the Microsoft Translator online service. Microsoft Translator may collect some data to improve the quality of translations. |
| Managed Metadata Service | Managed Metadata Web Service | Application Server |  |
| Microsoft SharePoint Foundation Subscription Settings Service | Microsoft SharePoint Foundation Subscription Settings Service | Front-end server | This service application is deployed only by using PowerShell. In hosting environments, this service is typically started on one or more application servers. Start this service if you have deployed service applications in multi-tenant mode or if the farm includes sites that use site subscriptions. This service stores settings and configuration data for tenants in a multi-tenant environment. After it is started, web applications consume this service automatically. |
| PerformancePoint | PerformancePoint Service | Front-end server |  |
| PowerPoint Conversion | PowerPoint Conversion Service | Application Server | This service converts PowerPoint presentations to other formats. It typically runs on one or more application servers. It starts one or more worker processes to perform conversions. When actively converting, a worker process may use up a whole processor core. Memory usage depends on the size and content of files being converted. The number of worker processes that are used can be controlled through PowerShell cmdlets. Several other configuration options are also available through PowerShell cmdlets. |
| Search | Lotus Notes Connector | Search Server | To learn how to configure Lotus Notes Connector which crawls data on a Lotus Domino server, see the documentation. |
| Search | Search Host Controller Service | Search servers | This service manages the search topology components. The service is automatically started on all servers that run search topology components. |
| Search | Search Query and Site Settings Service | Search servers | This service load balances queries within the search topology. It also detects farm-level changes to the search service and puts these in the Search Admin database. The service is automatically started on all servers that run the query processing component. |
| Search | SharePoint Server Search | Search servers | This service crawls content for the search index. This service is automatically started on all servers that run search topology components. The service cannot be stopped or started from the Services on Server page. |
| Secure Store Service | Secure Store Service | Search or Application server |  |
| Usage and Health Data Collection | NA | NA | This service application has no associated service on server. |
| User Profile | User Profile Service | Front-end or Application server |  |
| User Profile | User Profile Synchronization Service | Front-end or Application Server |  |
| Visio Graphics Service | Visio Graphics Service | Front-end or server |  |
| Word Automation Service | Word Automation Services | Application server | Performs automated bulk document conversions. When actively converting, this service will fully use one CPU for each worker process (configured in Central Administration). If the service is started on multiple servers, a job will be shared across all the servers. |
| Work Management | Work Management Service | Application Server |  |
|  | Central Administration | Front-end or Application Server | This service runs the SharePoint Central Administration website. |
|  | Claims to Windows Token Service | Web and application servers | This service is automatically configured to run on applicable servers. |
|  | Distributed Cache | Web and application servers | By default this service is started on all web servers and application servers in a farm. |
|  | Document Conversions Launcher Service | Application Server | Schedules and starts the document conversions on a server. |
|  | Document Conversions Load Balancer Service | Application Server | Balances document conversion requests from across the server farm. Each web application can have only one load balancer registered with it at a time. |
|  | Microsoft SharePoint Foundation Incoming E-Mail | Web server or application server | Typically, this service runs on a web server. If you need to isolate this service, you can start it on an application server. |
|  | Microsoft SharePoint Foundation Sandboxed Code Service | Web server or application server | Start this service on computers in the farm that run sandboxed code. This can include web servers and application servers. This service runs code that is deployed as part of a sandboxed solution in a remote, rights-restricted process and measures the server resources that are used during execution against a site collection-scoped, daily quota. |
|  | Microsoft SharePoint Foundation Web Application | Web server | Ensure that this service is started on all web servers in a farm. Stop this service on application servers. This service provides web server functionality. It is started by default on web servers. Custom features scoped to web applications may not display in Central Administration as intended if this service is not started on the server that runs Central Administration and if the feature cannot be deployed globally. |
|  | Microsoft SharePoint Foundation Workflow Timer Service | Web server | This service is automatically configured to run on all web servers in a farm. |
|  | Request Management | Web server or dedicated servers | In integrated mode, Request Management runs on all web servers in a farm. In dedicated mode servers in a separate Request Management farm are between the hardware load balancer and one or more SharePoint farms. |

For a list of **Services on Server** in SharePoint Server 2016, see Description of MinRole and associated services in SharePoint Server 2016.

See also

## See also

Other Resources

#### Other Resources

Plan for SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
