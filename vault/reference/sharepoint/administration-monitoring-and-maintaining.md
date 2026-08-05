---
title: "Monitoring and maintaining SharePoint Server 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-monitoring-and-maintaining
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/monitoring-and-maintaining
family: administration
documentKind: "article"
abstract: "Learn about how to monitor and maintain SharePoint Server."
---

# Monitoring and maintaining SharePoint Server 2013 - SharePoint Server

Note

Monitoring and maintaining SharePoint Server 2013

# Monitoring and maintaining SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article discusses monitoring and performance counters for SharePoint Server 2013 farms. To maintain SharePoint Server 2013 system performance, you must monitor your server to identify potential bottlenecks. Before you can monitor effectively, you must understand the key indicators that will tell you if a specific part of your farm requires attention, and know how to interpret these indicators. If you find that your farm is operating outside the targets you have defined, you can adjust your farm by adding or removing hardware resources, changing your topology, or changing how data is stored.

The information in this section is intended to help administrators manually configure performance counters and other settings. For more information about health monitoring and troubleshooting using the health monitoring tools built into the SharePoint Central Administration website interface, read the following articles:

Plan for monitoring in SharePoint Server

Monitoring and Reporting in SharePoint Server

Solving problems and troubleshooting in SharePoint Server

Before you read this article, you should read Capacity management and sizing overview for SharePoint Server 2013.

Configuring monitoring

## Configuring monitoring

Below is a list of the settings that you can change to monitor your environment in its early stages, which will help you determine whether any changes are needed. Increasing your monitoring capabilities will affect how much disk space that your usage database will require. Once the environment is stable and this detailed monitoring is no longer required, you may want to reverse the settings below to their default settings.

| **Setting** | **Value** | **Notes** |
| --- | --- | --- |
| Event Log Flooding Protection | Disabled | The default value is **Enabled**. It can be disabled to collect as much monitoring data as possible. For normal operations, it should be enabled. |
| **Timer Job Schedule** |  |  |
| Microsoft SharePoint Foundation Usage Data Import | 5 minutes | The default value is **30 minutes**. Lowering this setting imports the data into the usage database more frequently, and is especially useful when troubleshooting. For normal operations, it should be 30 minutes. |
| **Diagnostic Providers** |  |  |
| Enable all diagnostic providers | Enabled | The default value is **Disabled** except for the "Search Health Monitoring - Trace Events" provider. These providers collect health data for various features and components. For normal operations, you may want to revert to the default. |
| Set "job-diagnostics-performance-counter-wfe-provider" and "job-diagnostics-performance-counter-sql-provider" Schedule Intervals | 1 minute | The default value is **5 minutes**. Lowering this setting can poll data more frequently, and is especially useful when troubleshooting. For normal operations, it should be 5 minutes. |
| **Miscellaneous** |  |  |
| Enable stack tracing for content requests | Enabled | The default value is **Disabled**. Enabling this setting allows diagnosis of content requests failures using the process stack trace. For normal operations, it should be disabled. |
| Enable the Developer Dashboard | Enabled | The default value is **Disabled**. Enabling this setting allows diagnosis of slow pages, or other problems by using the Developer Dashboard. For normal operations, and as soon as troubleshooting is no longer necessary, it should be disabled. |
| **Usage Data Collection** |  |  |
| Content Import Usage  
 Content Export Usage  
 Page Requests  
 Feature Use  
 Search Query Use  
 Site Inventory Usage  
 Timer Jobs  
 Rating Usage | Enabled | Enabling the logging of this set of counters allows you to collect more usage data across the environment and to better understand the traffic patterns in the environment. |

Performance counters

### Performance counters

If you are using the usage database, then you can add the performance counters that assist you in monitoring and evaluating your farm's performance to the usage database, in such a way that they are logged automatically at a specific interval (by default, 30 minutes). Given that, you can query the usage database to retrieve these counters and graph the results over time. Here's an how to use the **Add-SPDiagnosticsPerformanceCounter** PowerShell cmdlet to add the % Processor Time counter to the usage database. This only has to be run on one of the web servers:

```
Add-SPDiagnosticsPerformanceCounter -Category "Processor" -Counter "% Processor Time" -Instance "_Total" -WebFrontEnd
```

There are several generic performance counters that you should monitor for any server system. The following table outlines these performance counters.

| **Performance Counter** | **Description** |
| --- | --- |
| Processor | You should monitor processor performance to ensure that all processor usage does not remain consistently high (over 80 percent) as this indicates that the system would not be able to handle any sudden surges of activity. And that in the common state, you will not see a domino effect if one component failure will bring the remaining components to a malfunctioning state. For example, if you have three web servers, you should make sure that the average CPU across all servers is under 60% so that if one fails, there is still room for the other two to absorb the additional load. |
| Network Interface | Monitor the rate at which data is sent and received via the network interface card. This should remain below 50 percent of network capacity. |
| Disks and Cache | There are several logical disk options that you should monitor regularly. The available disk space is important in any capacity study, but you should also review the time that the disk is idle. Dependent on the types of applications or services that you are running on your servers, you may review disk read and write times. Extended queuing for write or read function will affect performance. The cache has a major effect on read and write operations. You must monitor for increased cache failures. |
| Memory and Paging File | Monitor how much physical memory is available for allocation. Insufficient memory will lead to excessive use of the page file and an increase in the number of page faults per second. |

System counters

#### System counters

The following table provides information on system objects and counters that you could add to the set of counters monitored in the usage database using the **SPDiagnosticPerformanceCounter** on a web server.

| **Objects and Counters** | **Description** |
| --- | --- |
| **Processor** |  |
| % Processor Time | This shows processor usage over time. If this is consistently too high, you may find performance is adversely affected. Remember to count "Total" in multiprocessor systems. You can measure the utilization on each processor also, to ensure balanced performance between cores. |
| **Disk** |  |
| - Avg. Disk Queue Length | This shows the average number of both read and write requests that were queued for the selected disk during the sample interval. A bigger disk queue length may not be a problem as long as disk reads/writes are not suffering and the system is working in a steady state without expanding queuing. |
| Avg. Disk Read Queue Length | The average number of read requests that are queued. |
| Avg. Disk Write Queue Length | The average number of write requests that are queued. |
| Disk Reads/sec | The number of reads to disk per second. |
| Disk Writes/sec | The number of writes to disk per second. |
| **Memory** |  |
| - Available Mbytes | This shows how much physical memory is available for allocation. Insufficient memory leads to excessive use of the page file and an increase in the number of page faults per second. |
| - Cache Faults/sec | This counter shows the rate at which faults occur when a page is sought in the file system cache and is not found. This may be a soft fault, when the page is found in memory, or a hard fault, when the page is on disk.  
 The effective use of the cache for read and write operations can have a significant effect on server performance. You must monitor for increased cache failures, indicated by a reduction in the **Async Fast Reads/sec** or **Read Aheads/sec**. |
| - Pages/sec | This counter shows the rate at which pages are read from or written to disk to resolve hard page faults. If this increases, it indicates system-wide performance problems. |
| **Paging File** |  |
| - % Used and % Used Peak | The server paging file, also known as the swap file, holds "virtual" memory addresses on disk. Page faults occur when a process has to stop and wait while required "virtual" resources are retrieved from disk into memory. These will be more frequent if the physical memory is insufficient. |
| **NIC** |  |
| - Total Bytes/sec | This is the rate at which data is sent and received via the network interface card. You may have to investigate further if this rate is over 40-50 percent network capacity. To fine-tune your investigation, monitor **Bytes received/sec** and **Bytes Sent/sec**. |
| **Process** |  |
| - Working Set | This counter indicates the current size (in bytes) of the working set for a given process. This memory is reserved for the process, even if it is not being used. |
| - % Processor Time | This counter indicates the percentage of processor time that is used by a given process. |
| Thread Count (_Total) | The current number of threads. |
| **ASP.NET** |  |
| Requests Total | The total number of requests since the service was started. |
| Requests Queued | SharePoint Server 2013 provides the building blocks for HTML pages that are rendered in the user browser over HTTP. This counter shows the number of requests waiting to be processed. |
| Request Wait Time | The number of milliseconds that the most recent request waited in the queue for processing. As the number of wait events increases, users will experience decreased page-rendering performance. |
| Requests Rejected | The total number of requests not executed because of insufficient server resources to process them. This counter represents the number of requests that return a 503 HTTP status code, which indicates that the server is too busy. |
| Requests Executing (_Total) | The number of requests currently executing. |
| Requests/Sec (_Total) | The number of requests executed per second. This represents the current throughput of the application. Under constant load, this number should remain in a certain range, barring other server work (such as garbage collection, cache cleanup thread, external server tools, and so on). |
| **.NET CLR Memory** |  |
| # Gen 0 Collections | Displays the number of times the generation 0 objects (that is, the youngest, most recently allocated objects) are reclaimed by garbage collection since the application started. This number is useful as a ratio of #Gen 0: #Gen 1: #Gen 2 to make sure that the number of Gen 2 collections does not greatly exceed Gen 0 collections, optimally by a factor of 2. |
| # Gen 1 Collections | Displays the number of times the generation 1 objects are reclaimed by garbage collection since the application started. |
| # Gen 2 Collections | Displays the number of times the generation 2 objects are reclaimed by garbage collection since the application started. The counter is incremented at the end of a generation 2 garbage collection (also known as a full garbage collection). |
| % Time in GC | Displays the percentage of elapsed time that was spent performing a garbage collection since the last garbage collection cycle. This counter usually indicates the work done by the garbage collector to collect and compact memory on behalf of the application. This counter is updated only at the end of every garbage collection. This counter is not an average. Its value reflects the last observed value. This counter should be under 5% in normal operation. |

SQL Server counters

#### SQL Server counters

The following table provides information on SQL Server objects and counters.

| **Objects and Counters** | **Description** |
| --- | --- |
| General Statistics | This object provides counters to monitor general server-wide activity, such as the number of current connections and the number of users connecting and disconnecting per second from computers that are running an instance of SQL Server. |
| User Connections | This counter shows the number of user connections on your instance of SQL Server. If you see this number increase by 500 percent from your baseline, you may see a performance reduction. |
| Databases | This object provides counters to monitor bulk copy operations, backup and restore throughput, and transaction log activities. Monitor transactions and the transaction log to determine how much user activity is occurring in the database and how full the transaction log is becoming. The amount of user activity can determine the performance of the database and affect log size, locking, and replication. Monitoring low-level log activity to gauge user activity and resource usage can help you identify performance bottlenecks. |
| Transactions/sec | This counter shows the number of transactions on a given database or on the whole SQL Server instance per second. This number is to help you create a baseline and to help you troubleshoot issues. |
| Locks | This object provides information about SQL Server locks on individual resource types. |
| Number of Deadlocks/sec | This counter shows the number of deadlocks on the SQL Server per second. This should typically be 0. |
| Average Wait Time (ms) | This counter shows the average amount of wait time for each lock request that resulted in a wait. |
| Lock Wait Time (ms) | This counter shows the total wait time for locks in the last second. |
| Lock Waits/sec | This counter shows the number of locks per second that could not be satisfied immediately and had to wait for resources. |
| Latches | This object provides counters to monitor internal SQL Server resource locks called latches. Monitoring the latches to determine user activity and resource usage can help you identify performance bottlenecks. |
| Average Latch Wait Time (ms) | This counter shows the average latch wait time for latch requests that had to wait. |
| Latch Waits/sec | This counter shows the number of latch requests per second that could not be granted immediately. |
| SQL Statistics | This object provides counters to monitor compilation and the type of requests sent to an instance of SQL Server. Monitoring the number of query compilations and recompilations and the number of batches received by an instance of SQL Server gives you an indication of how quickly SQL Server is processing user queries and how effectively the query optimizer is processing the queries. |
| SQL Compilations/sec | This counter indicates the number of times the compile code path is entered per second. |
| SQL Re-Compilations/sec | This counter indicates the number of times statement recompiles are triggered per second. |
| Plan Cache | This object provides counters to monitor how SQL Server uses memory to store objects such as stored procedures, impromptu and prepared Transact-SQL statements, and triggers. |
| Cache Hit Ratio | This counter indicates the ratio between cache hits and lookups for plans. |
| Buffer Cache | This object provides counters to monitor how SQL Server uses memory to store data pages, internal data structures, and the procedure cache and counters to monitor the physical I/O as SQL Server reads and writes database pages. |
| Buffer Cache Hit Ratio | This counter shows the percentage of pages found in the buffer cache without having to read from disk. The ratio is the total number of cache hits divided by the total number of cache lookups since an instance of SQL Server was started. |

Removing bottlenecks

## Removing bottlenecks

System bottlenecks represent a point of contention where there are insufficient resources to service user transaction requests. These may be physical hardware, operating environment, or application-based. Often, the reason for the bottleneck will be inefficient custom code or third-party solutions, and a review of those could yield better results than adding hardware. Another common cause of bottlenecks is a misconfiguration of the farm, or an inefficient solution implementation that structures data in a way that requires more resources than necessary. For a system administrator, you should manage bottlenecks by constantly monitoring performance. When you identify a performance issue, you must assess the best resolution for removing the bottleneck. The performance counters and other performance monitoring applications, such as SCOM, are the key tools in tracking and analyzing problems, so that you can develop a solution.

Physical bottleneck resolution

### Physical bottleneck resolution

Physical bottlenecks are based on processor, disk, memory, and network contention: too many requests are contending for too few physical resources. The objects and counters described in the Monitoring Performance topic indicate where the performance problem is located, for example, hardware processor or ASP.NET. Bottleneck resolution requires that you identify the issue and then make a change or changes that mitigate the performance problem.

Problems seldom happen instantaneously; there is usually a gradual performance degradation that you can track if you monitor regularly, using your performance monitor tool or a more sophisticated system, such as SCOM. For both of these options, to varying degrees, you can embed solutions within an alert, in the form of advisory text or scripted commands.

You may have to resolve bottleneck issues by making changes to hardware or system configurations, once you have determined that they are not caused by a mis-configuration, inefficient custom code or third party solutions, or inefficient solution implementation. The following tables identify problem threshold and possible resolution options. Some of the options suggest hardware upgrades or modifications.

| **Objects and Counters** | **Problem** | **Resolution Options** |
| --- | --- | --- |
| **Processor** |  |  |
| Processor - % Processor Time | Over 75-85% | Upgrade processor  
 Increase number of processors  
 Add additional server(s) |
| **Disk** |  |  |
| Avg. Disk Queue Length | Gradually increasing, system not in a steady state and queue is backing up | Increase number or speed of disks  
 Change array configuration to stripe  
 Move some data to an alternative server |
| % Idle Time | Less than 90% | Increase number of disks  
 Move data to an alternative disk or server |
| % Free Space | Less than 30% | Increase number of disks  
 Move data to an alternative disk or server |
| **Memory** |  |  |
| Available Mbytes | Less than 2GB on a Web server. | Add memory.  
 > [!NOTE]> SQL Server available memory will be low, by design, and does not always indicate a problem. |
| Cache Faults/sec | Greater than 1 | Add memory  
 Increase cache speed or size if possible  
 Move data to an alternative disk or server |
| Pages/sec | Greater than 10 | Add memory |
| **Paging File** |  |  |
| % Used and % Used Peak | The server paging file, sometimes called the swap file, holds "virtual" memory addresses on disk. Page faults occur when a process has to stop and wait while required "virtual" resources are retrieved from disk into memory. These will be more frequent if the physical memory is inadequate. | Add memory |
| **NIC** |  |  |
| Total Bytes/sec | Over 40-50% of network capacity. This is the rate at which data is sent and received via the network interface card. | Investigate further by monitoring Bytes received/sec and Bytes Sent/sec.  
 Reassess network interface card speed  
 Check number, size, and usage of memory buffers |
| **Process** |  |  |
| Working Set | Greater than 80% of total memory | Add memory |
| % Processor Time | Over 75-85%. | Increase number of processors  
 Redistribute workload to additional servers |
| **ASP.NET** |  |  |
| Application Pool Recycles | Several per day, causing intermittent slowness. | Make sure that you have not implemented settings that automatically recycle the application pool unnecessarily throughout the day. |
| Requests Queued | Hundreds or thousands of requests queued. | Implement additional Web servers  
 The default maximum for this counter is 5,000, and you can change this setting in the Machine.config file |
| Request Wait Time | As the number of wait events increases, users will experience degraded page rendering performance. | Implement additional Web servers |
| Requests Rejected | Greater than 0 | Implement additional Web servers |

See also

## See also

Concepts

#### Concepts

Performance testing for SharePoint Server 2013

Capacity planning for SharePoint Server 2013

Other Resources

#### Other Resources

Capacity management and sizing overview for SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
