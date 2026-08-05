---
title: "Scale search for Internet sites in SharePoint Server - SharePoint Server"
description: "Determine hardware requirements and review considerations to scale out SharePoint Server search topologies for Internet sites for performance and availability."
ms.topic: article
---
Note

Scale search for Internet sites in SharePoint Server

# Scale search for Internet sites in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article lists the minimum hardware requirements for virtual machines and physical servers for search topologies for Internet sites.

This article also provides basic guidance on the scaling of search topologies to improve performance and availability.

Introduction

## Introduction

This article lists the minimum requirements and gives guidance about how and when to scale out search topologies for Internet sites.

For examples of topologies, see the technical diagram Internet sites search architectures for SharePoint Server 2016.

For an overview and a description of search components and the overall search architecture, see Overview of search architecture in SharePoint Server and the technical diagram Search architectures for SharePoint Server 2016.

Hardware requirements for search topologies for Internet sites

## Hardware requirements for search topologies for Internet sites

The following tables show the hardware requirements for servers that host a medium search topology for Internet sites. The hardware requirements apply to:

Application servers and Web servers that contain search components.

Database servers that contain search databases.

The minimum listed RAM requirements for a server that hosts a search component is the total required amount of RAM for that server. For example, if you are hosting a content processing component, a search administration component and a crawl component on one server, the total amount of minimum required RAM for that server is 24 GB.

Each server must have sufficient disk space for the base installation of the Windows Server operating system and sufficient disk space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, the server also needs additional free disk space for day-to-day operations and for the page file. Follow the guidance on free disk space and page file size corresponding to your Windows Server installation.

Note

The medium search topology example is optimized for physical hardware, but you can deploy it on virtual machines as well.

**Application servers and Web servers hosting search components**

| **Search component on the physical server** | **RAM** | **Hard disk** | **Processor** |
| --- | --- | --- | --- |
| Index component | 48 GB for each server in the farm that hosts an index component, a query processing component and the Web front end. | 500 GB additional disk space, preferably a separate disk volume/partition. | **All components:**64-bit, 4 cores minimum, 8 cores recommended. |
| Analytics processing component | 24 GB for each server in the farm that hosts an analytics processing component, a crawl component, a content processing component and/or a search administration component. | 300 GB additional disk space, preferably a separate disk volume/partition. |  |
| Crawl component Content processing component | See the requirements listed for the analytics processing component. | 80 GB for system drive. |  |
| Query processing component | See the requirements listed for the index component. |  |  |
| Search administration component | See the requirements listed for the analytics processing component. |  |  |

**Database servers hosting search databases**

| **Component** | **Minimum requirements** |
| --- | --- |
| Processor | 64-bit, 4 cores for small topologies.  
 64-bit, 8 cores for medium topologies. |
| RAM | 8 GB for small topologies.  
 16 GB for medium topologies. |
| Hard disk | 80 GB for system drive.  
 Hard disk space depends on the amount of content. |

Performance considerations for a medium Internet sites topology

## Performance considerations for a medium Internet sites topology

A medium Internet sites (FIS) topology is optimized for a corpus size of 3,400,000 items, processing approximately 100-200 documents per second, depending on language, and a usage pattern of 85 page views per second, which corresponds to 100 queries per second.

**Performance considerations**

| **What to consider** | **Why this is important** |
| --- | --- |
| Cache | The query and its results are cached with Windows Server AppFabric, in key-value pairs: the query being the key and the results being the value. For each query, there is an approximate 50% cache ratio. This means that if you have a usage pattern of 200 queries per second, about 100 queries are sent to the search index and the other 100 queries are cached. The results from the cache have lower query latency than those that you retrieve from the search index. For example, results for front-page queries that are often run are likely to be cached. |
| Continuous crawl | We recommend that you enable continuous crawl with an interval of one minute, instead of the default interval of 15 minutes. You can only enable continuous crawl on SharePoint content sources. |
| Anonymous access | With anonymous access, users do not have to use credentials to log on to a SharePoint Internet site. Anonymous queries are cached, so they are cheaper because of lower query latency. You must enable anonymous access in two locations: on the web front-end and on the site. |
| Query latency | Query latency is influenced by caching, anonymous access and by other factors such as the number and complexity of query rules that are applied and triggered. Also, consider the disks on which the search index is stored; a disk that has multiple spindles can improve the access speed of the disk and reduce query latency. |

See also

## See also

Manage the search topology in SharePoint Server

Change the default search topology in SharePoint Server

Manage search components in SharePoint Server

Manage the index component in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
