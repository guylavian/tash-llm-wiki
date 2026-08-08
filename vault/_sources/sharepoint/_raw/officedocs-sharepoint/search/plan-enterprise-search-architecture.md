---
title: "Plan enterprise search architecture in SharePoint Server - SharePoint Server"
description: "Learn how to plan an enterprise search architecture."
ms.topic: how-to
---
Note

Plan enterprise search architecture in SharePoint Server

# Plan enterprise search architecture in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Before you set up your enterprise search architecture, there are quite a few things that require careful planning. Step by step, we'll help you to plan a small, a medium, large, or an extra large-size enterprise search architecture.

Are you familiar with the components of the search system in SharePoint Server, and how they interact? By reading Overview of search architecture in SharePoint Server and Search architectures for SharePoint Server 2016 (or Search architectures for SharePoint Server 2013) before you get going, you'll become familiar with search architecture, search components, search databases, and the search topology. When planning a search architecture, here are some suggestions about what to consider:

Step 1: How much content do I have?

Step 2: What size search architecture for how much content?

Step 3: Which hardware requirements should I be aware of?

Choose to run the servers physically or virtually

Choose hardware resources for the host servers

Plan storage performance

Choose how your search architecture supports high availability

Step 4: How to check that my search architecture performs well?

Test the storage I/O subsystem

Test the search performance

Step 1: How much content do I have?

## Step 1: How much content do I have?

The volume of content that you have in your search index affects what resources you need to host the farm. Work out approximately the number of items that you plan on making searchable. Here are some examples of items: documents, web pages, SharePoint list entries, and images. Remember that each entry in a SharePoint list counts as one item.

When you have established a figure, multiply it by what you think the expected growth of that content will be over the next 12 months.

For example, if you're starting out with 12,000 indexed items, and you expect the volume of that content to triple over the next 12 months. You should plan for 36,000 searchable items.

Step 2: What size search architecture for how much content?

## Step 2: What size search architecture for how much content?

It's not always easy to assess how big or small to make your search architecture. The size of your search architecture depends on the volume of your content, the crawl rate, the query throughput, and the level of high availability that you require. There are sample search architectures that we advise using as a basis to plan your own farm. The sample search architecture that you choose depends on how much content has to be searchable:

| Volume of content (SharePoint 2016) | Sample search architecture | Volume of content (SharePoint 2013) |
| --- | --- | --- |
| 0-20 million items | Small search farm | 0-10 million items |
| 0-80 million items | Medium search farm | 0-40 million items |
| 0-200 million items | Large search farm | 0-100 million items |
| 0-500 million items | Extra large search farm | Not supported |

Although these sample search architectures use virtual machines, you can use both physical servers and virtual machines according to the strategy of the overall SharePoint Server solution of your search architecture.

Small search farm

### Small search farm

We've estimated that this search architecture can crawl 50 documents per second, and serve in the order of 10 queries per second. If you have up to 20 million items in a SharePoint Server 2016 farm, the small search farm will probably be the most suitable farm for you. With a crawl rate of 50 documents per second, it takes search 110 hours to crawl 20 million items in the first full crawl.

Medium search farm

### Medium search farm

We've estimated that this search architecture can crawl 100 documents per second, and serve in the order of 10 queries per second. If you have between 20 and 80 million items in a SharePoint Server 2016 farm, the medium search farm will probably be the most suitable farm for you. With a crawl rate of 200 documents per second, it takes search 280 hours to crawl 80 million items in the first full crawl.

Large search farm

### Large search farm

We've estimated that this search architecture can crawl 200 documents per second, and serve in the order of 10 queries per second. If you have between 80 and 200 million items in a SharePoint Server 2016 farm, the large search farm will probably be the most suitable farm for you. With a crawl rate of 200 documents per second, it takes search 280 hours to crawl 200 million items in the first full crawl.

Extra large search farm

### Extra large search farm

Microsoft tested this search architecture and measured that it can crawl 300-500 documents per second, and serve in the order of 10 queries per second. Only SharePoint Server 2016 supports this size search architecture. If you have up to 500 million items, a farm similar to the extra large search farm is a good starting point. With a crawl rate of 500 documents per second, it takes search about 300 hours to crawl 500 million items in the first full crawl.

Creating a search farm of this size requires you to carefully plan and tune the farm to get the performance you want. You might find it advantageous to seek expert guidance. It's also important to plan how to back up and restore a search farm of this size, and how to recover the farm if your data center has a major outage. We recommend that you practice backup, restore and recovery.

Step 3: Which hardware requirements should I be aware of?

## Step 3: Which hardware requirements should I be aware of?

Now that you've determined the volume of your content and chosen a sample search architecture, the next step is to plan the hardware you'll need, as described in this section:

Choose to run the servers physically or virtually

Choose hardware resources for the host servers

General storage

Minimum hardware resources for the small search farm

Minimum hardware resources for the medium search farm

Minimum hardware resources for the large search farm

Minimum hardware resources for the extra large search farm

Plan storage performance

Choose storage

Search component IOPS requirements

Search database IOPS requirements

Choose how your search architecture supports high availability

Choose to run the servers physically or virtually

### Choose to run the servers physically or virtually

If you're using one of the architectures that we've estimated for you, then you'll be running your search architecture on virtual machines. Note also that although a virtual environment is easier to manage, its performance level can sometimes be slightly lower than that of a physical environment. A physical server can host more search components on the same server than a virtual server. You'll find useful guidance in Overview of farm virtualization and architectures for SharePoint 2013.

It's also possible to run your search architecture on physical servers. In the sample farm architectures, just move the search components from the virtual machines to the host server and take away the virtual machines. Each physical server can host up to four index components, but only one of each type of the other search components. If you for example change the medium sample search architecture to use physical servers, you'll find that you have two content processing components on Host E. The solution is to take away one of the content processing components. This works because crawling, processing of content, and processing of analytics depend on the amount of resources that are available, not the number of content processing components.

Choose hardware resources for the host servers

### Choose hardware resources for the host servers

Each search component and search database requires a minimum amount of hardware resources from the host server to perform well. But, the more hardware resources you have, the better the performance of your search architecture will be. So it's a good idea to have more than the minimum amount of hardware resources. The resources each search component requires depends on the workload, mostly determined by the crawl rate, the query rate, and the number of indexed items.

For example, when hosting virtual machines on Windows Server 2008 R2 Service Pack 1 (SP1), you can't use more than four CPU cores per virtual machine. With Windows Server 2012 or newer, you use eight or more CPU cores per virtual machine. Then you can scale out with more CPU cores for each virtual machine instead of scaling up with more virtual machines. Set up servers or virtual machines that host the same search components, with the same hardware resources. Let's use the index component as an example. When you host index partitions on virtual machines, the virtual machine with the weakest performance determines the performance of the overall search architecture.

General storage

#### General storage

Make sure that each host server has enough disk space for the base installation of the Windows Server operating system and for the SharePoint Server program files. The host server also needs free hard disk space for diagnostics such as logging, debugging, and creating memory dumps, for daily operations, and for the page file. Normally, 80 GB of disk space is enough for the Windows Server operating system and for the SharePoint Server program files.

Add storage for the SQL log space for each database server. If you don't set the database server to back up the databases often, the SQL log space uses lots of storage. For more information about how to plan SQL databases, see Storage and SQL Server capacity planning and configuration (SharePoint Server) .

The minimum storage that the analytics reporting database requires can vary. This is because the amount of storage depends on how users interact with SharePoint Server. When users interact frequently, there usually are more events to store. Check the amount of storage your current search architecture uses for the analytics database, and assign at least this amount for your redesigned topology.

Minimum hardware resources for the small search farm

#### Minimum hardware resources for the small search farm

This table shows the minimum amount of hardware resources that each application server or database server needs.

| Server | On host | Storage | RAM | Processor1 | Network bandwidth |
| --- | --- | --- | --- | --- | --- |
| Application server that has query processing and index components. | A, B | 500 GB2,3 | 32 GB2,3 | 1.8 GHz 8x CPU cores2,3 | 1 Gbps |
| Application server that has crawl, search administration, analytics and content processing components. | A, B | 200 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Database server that has all search databases. | C, D | 100 GB | 16 GB | 1.8 GHz 4x CPU cores | 1 Gbps |

1The number of CPU cores is specified here, not the number of CPU threads.

2With SharePoint Server 2013 the minimum amount of resources needed are 500 GB storage, 16 GB RAM, and four CPU cores.

3With SharePoint Server 2016 you can also use 250 GB storage, 16 GB RAM, and four CPU cores, but then each index component can only hold 10 million items and the search farm only supports the same volume of content as a SharePoint Server 2013 search farm.

Minimum hardware resources for the medium search farm

#### Minimum hardware resources for the medium search farm

This table shows the minimum amount of hardware resources that each application server or database server needs.

| Server | On host | Storage | RAM | Processor1 | Network bandwidth |
| --- | --- | --- | --- | --- | --- |
| Application server that has query processing and index components. | A, B, C, D | 500 GB2,3 | 32 GB2,3 | 1.8 GHz 8x CPU cores2,3 | 1 Gbps |
| Application server that has an index component. | A, B, C, D | 500 GB2,3 | 32 GB2,3 | 1.8 GHz 8x CPU cores2,3 | 1 Gbps |
| Application server that has analytics and content processing components. | E, F | 300 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Application server that has crawl, search administration, and content processing components. | E, F | 100 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Database server that has all search databases. | G, H | 400 GB | 16 GB | 1.8 GHz 4x CPU cores | 1 Gbps |

1The number of CPU cores is specified here, not the number of CPU threads.

2With SharePoint Server 2013 the minimum amount of resources needed are 500 GB storage, 16 GB RAM, and four CPU cores.

3With SharePoint Server 2016 you can also use 250 GB storage, 16 GB RAM, and four CPU cores, but then each index component can only hold 10 million items and the search farm only supports the same volume of content as a SharePoint Server 2013 search farm.

Minimum hardware resources for the large search farm

#### Minimum hardware resources for the large search farm

This table shows the minimum amount of hardware resources that each application server or database server needs.

| Server | On host | Storage | RAM | Processor1 | Network bandwidth |
| --- | --- | --- | --- | --- | --- |
| Application server that has query processing and index components. | A, B, C, D, E, G, H | 500 GB2, 3 | 32 GB2, 3 | 1.8 GHz 8x CPU cores2, 3 | 1 Gbps |
| Application server that has an index component. | A, B, C, D, E, F, G, H, I, J | 500 GB2, 3 | 32 GB2, 3 | 1.8 GHz 8x CPU cores2, 3 | 1 Gbps |
| Application servers that have analytics and content processing components | K, L, M, N | 300 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Application servers that have crawl and search administration components | K, L | 100 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Database server that have search databases | O, P, Q, R | 500 GB | 16 GB | 1.8 GHz 4x CPU cores | 1 Gbps |

1The number of CPU cores is specified here, not the number of CPU threads.

2With SharePoint Server 2013 the minimum amount of resources needed are 500 GB storage, 16 GB RAM, and four CPU cores.

3With SharePoint Server 2016 you can also use 250 GB storage, 16 GB RAM, and four CPU cores, but then each index component can only hold 10 million items and the search farm only supports the same volume of content as a SharePoint Server 2013 search farm.

Minimum hardware resources for the extra large search farm

#### Minimum hardware resources for the extra large search farm

This table shows the minimum amount of hardware resources that each application server or database server needs. You can only build this sample farm with SharePoint Server 2016.

| Server | On host | Storage | RAM | Processor1 | Network bandwidth |
| --- | --- | --- | --- | --- | --- |
| Application server that has index components. | A-X | 500 GB | 32 GB | 1.8 GHz 8x CPU cores | 1 Gbps |
| Application server that has query processing and index components. | Y, Z | 500 GB | 32 GB | 1.8 GHz 8x CPU cores | 1 Gbps |
| Application servers that have crawl, search administration, or content processing components | AA-AF | 100 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Application servers that have analytics processing components | AG, AH | 800 GB | 8 GB | 1.8 GHz 4x CPU cores | 1 Gbps |
| Database servers that have search databases | AI-AL | 500 GB | 16 GB | 1.8 GHz 4x CPU cores | 1 Gbps |

1The number of CPU cores is specified here, not the number of CPU threads.

Plan storage performance

### Plan storage performance

The speed of the storage affects the search performance. Make sure that the storage you have is fast enough to handle the traffic from the search components and databases. Disk speed is measured in I/O operations per second (IOPS).

The way you decide to distribute data from the search components and from the operating system across your storage, has an impact on search performance. It's a good idea to:

Split the Windows Server operating system files, the SharePoint Server program files, and diagnostics logs across three separate storage volumes or partitions with normal performance.

Store the search component data on a separate storage volume or partition with high performance.

Note

You can set a custom location for search component data when you install SharePoint Server on a host. Any search component on the host that needs to store data, stores it in this location. To change this location later, you have to reinstall SharePoint Server on that host.

Choose storage

#### Choose storage

For an overview of storage architectures and disk types, see Storage and SQL Server capacity planning and configuration (SharePoint Server). The servers that host the index or analytics processing components, or search databases, require storage that can maintain low latency, while providing sufficient I/O operations per second (IOPS). The following tables show how many IOPS each of these search components and databases require.

If you deploy shared storage like SAN/NAS, the peak disk load of one search component typically coincides with the peak disk load of another search component. To get the number of IOPS search requires from the shared storage, you need to add up the IOPS requirement of each of these components.

Search component IOPS requirements

#### Search component IOPS requirements

| Component name | Component details | IOPS requirements | Use of separate storage volume/partition |
| --- | --- | --- | --- |
| Index component | Uses storage when merging the index and when handling and responding to queries. | 300 IOPS for 64 KB random reads.  
  100 IOPS for 256 KB random writes.  
  200 MB/s for sequential reads.  
  200 MB/s for sequential writes. | Yes |
| Analytics component | Analyzes data locally, in bulk processing. | No | Yes |
| Crawl component | Stores downloaded content locally, before it sends it to a content processing component. Storage is limited by network bandwidth. | No | Yes |

Search database IOPS requirements

#### Search database IOPS requirements

| Database name | IOPS requirements | Typical load on I/O subsystem. |
| --- | --- | --- |
| Crawl database | Medium to high IOPS | 10 IOPS per 1 document per second (DPS) crawl rate. |
| Link database | Medium IOPS | 10 IOPS per 1 million items in the search index. |
| Search administration database | Low IOPS | Not applicable. |
| Analytics reporting database | Medium IOPS | Not applicable. |

Choose how your search architecture supports high availability

### Choose how your search architecture supports high availability

If you aren't familiar with high availability strategies, here's an article that will get you started: Create a high availability architecture and strategy for SharePoint Server. Your search architecture supports high availability when you host redundant search components and databases on separate fault domains. All of the sample search architectures host redundant search components on independent servers.

For each redundant host server in your search architecture, you should plan to install:

Redundant networking

Redundant power supplies with independent wiring or an uninterruptable power supply (UPS).

Step 4: How to check that my search architecture performs well?

## Step 4: How to check that my search architecture performs well?

Before you deploy your search architecture to a production environment, you'll need to check that it performs well. Here's a checklist of what to do:

Test that the index components use a storage I/O subsystem that has enough IOPS. See Test the storage I/O subsystem.

Deploy the search architecture to a pilot environment. Make sure that the pilot environment is representative of the production environment.

Test the search performance of the pilot environment. See Test the search performance

For an overview of testing in general in SharePoint , see Performance testing for SharePoint Server 2013.

Test the storage I/O subsystem

### Test the storage I/O subsystem

To test the storage I/O subsystem, run the most important disk operations and measure the IOPS. You can use the DiskSpd tool to run these tests. See DiskSpd: A Robust Storage Performance Tool.

Set up the test environment

#### Set up the test environment

You don't need to set up the whole search architecture, or install SharePoint Server. It's enough to set up a test environment that produces a realistic workload for the storage I/O subsystem.

Let's consider the case for local storage. For example, if host A in the medium search farm uses a local disk, you need to install the two virtual machines and run the disk operation tests on both virtual machines at the same time.

You need a different set-up for shared storage. If for example the workload from all the index components in the medium search farm plus other unrelated workloads share the same storage, you need to:

Install the eight virtual machines in host A, B, C, and D, and set up the sources of the unrelated workloads.

Make sure that the unrelated workload is applied to the shared storage at the same time as you run simultaneous disk operation tests on all the virtual machines in host A, B, D, and D.

Create a test file

#### Create a test file

Create a 256 GiBytes test file by using the command  `diskspd -c256G testfile`. This command creates a 256 GiBytes size file named "testfile". You can also create a file with another size by following the syntax: `diskspd -c<size>[K|M|G|b] <filename>`

Save the test file on the storage device that you want to test. For example: on the hard disk of Host A in the medium farm.

Restart the server. This will ensure that caching does not skew the test results.

Run tests

#### Run tests

It's a good idea to measure:

The performance of medium sized random accesses (see test number one and two below).

Read and write throughput for large transfers (see test number three and four below).

The table below shows the DiskSpd commands that you should use to run each test. All the commands assume that the "testfile" exists in the current directory. Each test runs for 300 seconds.

| Test number | Scope | Command |
| --- | --- | --- |
| 1 | 64 KB read [IOPS] | `diskspd -t4 -b64K -o25 -r -d300 testfile` |
| 2 | 256 KB write [IOPS] | `diskspd -t4 -b256K -o25 -r -w100 -d300 testfile` |
| 3 | 100 MB read [MB/s] | `diskspd -t1 -o1 -b100M -r -d300 testfile` |
| 4 | 100 MB write [MB/s] | `diskspd -t1 -o1 -b100M -r -w100 -d300 testfile` |

Example results for local disk storage

#### Example results for local disk storage

The sample results in the table below show a deployment where at least 50 percent of the disk subsystem capacity was in use before adding the test file.

The disk controller and the spindles of the disk strongly influence these results.

If you test on empty disks, you'll get elevated results because the test file will be in the most optimal tracks across all spindles (short stroking). This can increase performance by up to two or three times. You'll get unrealistically high results if you test a hard disk that optimizes away accesses on uninitialized storage space, or storage containing all zeros, for example dynamic VHD/VHDX files. In this case, use a very large test file that contains real data, rather than generating a synthetic test file using DiskSpd commands.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Disk layout | Test 1 | Test 2 | Test 3 | Test 4 |  |
| Recommended minimum IOPS during ordinary operations | 300 | 100 | 200 | 200 |  |
| 4x 1 TB 7200 RPM NLSAS in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size) | 1181 | 206 | 284 | 296 |  |
| 8x 1TB 7200 RPM NLSAS in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size) | 2082 | 337 | 610 | 645 |  |
| 16x 1TB 7200 RPM NLSAS in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size) | 3763 | 595 | 1173 | 1181 |  |
| 16x 1TB 7200 RPM NLSAS in RAID50 (2x8) on Dell H710 RAID controller (64kB stripe size, 64kB block size) | 3613 | 545 | 1139 | 1164 |  |
| 16x 1TB 7200 RPM NLSAS in RAID10 on Dell H710 RAID controller (256kB stripe size, 64kB block size) | 4030 | 1146 | 970 | 775 |  |
| 4x SmartStorage Optimus 800GB SSDs in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size) | 32385 | 3781 | 1714 | 1319 |  |
| 4x SmartStorage Optimus 800GB SSDs in RAID0 on Dell H710 RAID controller (256kB stripe size, 64kB block size) | 31747 | 7149 | 1643 | 1798 |  |

Test the search performance

### Test the search performance

Here's a checklist of what to do to test your search architecture:

Choose content to run tests on

Choose terms and phrases to test query performance

Measure search performance

Choose content to run tests on

#### Choose content to run tests on

Choose content that represents your production content well. If you choose content that's only there for test purposes, make sure you've got different types of items, not just one item that you've duplicated many times. The reason for this is that the query processor will spend time detecting duplicated items, which will affect search performance, and your results won't be representative of a production environment.

Set up one or more content sources to crawl the content. Verify that you have the required user account and network access.

Choose terms and phrases to test query performance

#### Choose terms and phrases to test query performance

The number of results you get for a query is called the recall.

To test query performance, you'll first need to create a set of terms and phrases to use as queries. Alternatively, collect queries from an existing installation. Make sure that the set contains terms and phrases that have low recall and high recall, and that the terms and phrases are relevant to your environment.

Examples

#### Examples

If you search for a product number in a product catalog, it's likely that there's only one number for one product. Therefore, you'll get your search results fast. This is low recall.

If you search for a common term like "presentation" on a company intranet, it's likely that you'll get many results, and it may take longer to get them. This is high recall.

If, for example, your content is related to human resources, use search terms that relate to this area.

Measure search performance

#### Measure search performance

SharePoint Server collects search performance measurements in the Crawl Health Reports and Query Health Reports. You can find these reports in Central Administration, under Search Administration.

It's a good idea to measure search performance first with a synthetic load, and then with a small set of live users, and live content. When you use live users and live content, you can observe how the search architecture is performing. If your content increases faster than you intended, it might be worth considering using the next size search architecture. Or, if your users are more active than anticipated, then we suggest that you increase the amount of storage space of the analytics database.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
