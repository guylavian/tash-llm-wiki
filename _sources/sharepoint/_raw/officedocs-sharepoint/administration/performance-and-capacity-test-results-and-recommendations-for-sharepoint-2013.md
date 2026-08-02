---
title: "Performance and capacity test results and recommendations (SharePoint Server 2013) - SharePoint Server"
description: "Learn about performance characteristics of features in SharePoint Server 2013."
ms.topic: article
---
Note

Performance and capacity test results and recommendations (SharePoint Server 2013)

# Performance and capacity test results and recommendations (SharePoint Server 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The following articles describe the tested performance and capacity characteristics and effect of specific scenarios and feature sets in SharePoint Server 2013. These articles include information about the characteristics of the scenario or feature and how it was tested by Microsoft, including:

**Test farm characteristics**, including:

Specifications for hardware, topology, and configuration

The workload and dataset used to generate test loads

**Test results and analysis** that demonstrate throughput, latency and hardware demand under load at specific scale points, and discuss important trends and considerations

**Recommendations** for how to optimize performance characteristics, scale your environment, and manage bottlenecks

**Troubleshooting performance and scalability** when specific conditions are observed

You can use the information in these articles to understand the performance and capacity characteristics of a specific scenario or feature under both normal and peak loads, and how performance trends for a scenario or feature change when farm servers are scaled out or hardware resources are added to existing servers. The articles can also help you estimate an appropriate starting point for your planned architecture, and to determine what factors are important to consider when you are planning for the resources your farm will have to maintain acceptable levels of performance under peak load.

It is important to realize that the test results that appear in these articles were produced in test labs that use workloads, datasets and architectures that are designed to emulate a production environment under highly controlled conditions. While great care is exercised in designing these tests, the performance characteristics of a test lab are never equivalent to the behavior of a production environment. These test results are not intended to represent the performance and capacity characteristics of a production farm, but instead to demonstrate observed trends in throughput, latency and hardware demand, and to provide an analysis of the observed data that can help you make capacity planning and management decisions in your own farm.

Before reading these articles, make sure that you understand the key concepts behind capacity management in SharePoint Server 2013. For more information, see Capacity management and sizing for SharePoint Server 2013.

The following table describes the available articles. This list will be updated as new articles become available.

| **Subject** | **Description** |
| --- | --- |
| Enterprise intranet collaboration scenario | This scenario-specific article describes guidance on performance and capacity planning for an enterprise intranet collaboration solution.  
 This article contains performance test results, analysis and recommendations based on testing of a SharePoint Server 2013 environment that was scaled out using virtual web servers that run on Hyper-V hosts. The article also includes comparison testing of SharePoint Server 2013 and SharePoint Server 2010 on both physical and virtual web servers.  
 View the article at Estimate performance and capacity requirements for enterprise intranet collaboration environments (SharePoint Server 2013). |
| Web Content Management | This article contains capacity and performance data to help plan the number of computers to use and the types of computers that are required to publish content and manage web content in SharePoint Server 2013.  
 View the article at Estimate capacity and performance for Web Content Management (SharePoint Server 2013). |
| Managed Metadata Service | This article discusses information and recommendations related to sizing and performance optimization of the Managed Metadata Service in SharePoint Server 2013. It also gives best practices for how to configure this service application and how to structure the service application databases for optimal performance.  
 View the article at Estimate capacity and performance for Managed Metadata Service (SharePoint Server 2013). |
| Video content | This article explains how to plan video content types and video player pages using the Rich Media Web Part to provide better user experiences when you play videos in SharePoint Server 2013.  
 View the article at Estimate capacity and performance for video content management in SharePoint Server 2013. |
| Compliance and eDiscovery | This article explains how compliance, eDiscovery, and large-scale document repositories can affect capacity and performance in SharePoint Server 2013.  
 View the article at Estimate capacity and performance for compliance and eDiscovery for SharePoint Server 2013. |
| Social content | This article explains how to determine the number and types of computers that you need for a capacity plan for a My Site and social computing portal based on SharePoint Server 2013.  
 View the article at Estimate performance and capacity requirements for social environments (SharePoint Server 2013). |
| Divisional collaboration | This article explains how to use test results and recommendations to estimate performance and capacity requirements for a divisional collaboration environment for SharePoint Server 2013.  
 View the article at Estimate performance and capacity requirements for divisional collaboration environments (SharePoint Server 2013). |

See also

## See also

Concepts

#### Concepts

Capacity management and sizing for SharePoint Server 2013

Software boundaries and limits for SharePoint Server 2016

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
