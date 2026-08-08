---
title: "Estimate capacity and performance for compliance and eDiscovery for SharePoint Server 2013 - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-compliance-and-ediscovery-capacity-and-performance
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/compliance-and-ediscovery-capacity-and-performance
family: administration
documentKind: "article"
abstract: "Learn about how compliance, eDiscovery, and large-scale document repositories can effect capacity and performance in SharePoint Server 2013."
---

# Estimate capacity and performance for compliance and eDiscovery for SharePoint Server 2013 - SharePoint Server

Note

Estimate capacity and performance for compliance and eDiscovery for SharePoint Server 2013

# Estimate capacity and performance for compliance and eDiscovery for SharePoint Server 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Compliance feature sets, such as in-place holds and querying and exporting data under preservation, effect the processing, and storage requirements in SharePoint Server 2013 when used.

Storage requirements for in-place holds

## Storage requirements for in-place holds

An in-place hold preserves edited and deleted content to make the original version available for legal actions. In-place holds apply to a complete site. For example, if the root site of a site collection is put on hold, the complete site collection is also on hold. An in-place hold applies to documents, pages, and lists. After a site is put on hold, all items that are edited for the first time or deleted, are put in the Preservation Hold Library for the SharePoint site. This location is where the content was originally located on the site. The size of the site increases at a rate that correlates with how much of the content existed when the hold was enabled and is changed when new content is added. In practice, most content on legal hold is not new. The effect on storage for in-place holds is expected to be low because users are not actively changing content. For more information, see eDiscovery and in-place holds in SharePoint Server.

Effect of eDiscovery queries and export on other Search queries

## Effect of eDiscovery queries and export on other Search queries

SharePoint Server 2013 has a site collection type called Case Manager that allows you to execute eDiscovery queries across your organization's SharePoint content and Exchange Server 2013 mailboxes. eDiscovery queries are complex and wide in scope. These queries require more processing time on the Search system and potentially affect the search response time that other users experience.

The following guidelines can help you understand how these queries affect Search experiences for other users:

As you add more sources to an eDiscovery query, you increase the number of executed queries.

As you add more terms to an eDiscovery query, you increase the effect of your eDiscovery queries.

As you add more operators (such as AND, OR, NEAR) to an eDiscovery query, you increase the effect of your eDiscovery queries.

In our lab tests, we used an eDiscovery query of 350 terms that ran against 10 sources. The query returned a total of 150,000 items. We then exported those items. To perform this test, we executed five simulated loads on the Search service system, which represented other types of search queries that are expected to run on the system.

Our tests show that eDiscovery queries can increase query latencies that users observe by as much as 100 percent. If you run close to capacity for your user search queries, you might consider running eDiscovery queries and exports during non-peak hours to have a smaller effect on user search queries.

Effect of Export

## Effect of Export

After you run eDiscovery queries, a common operation is to export the data. During the export action, content that the eDiscovery query returned is downloaded one file at a time. We ran a set of tests where we downloaded files and updated SharePoint items. Export did not add a significant load on the SharePoint deployment. We ran the export action in our tests while the farm served about 100 requests per second. Out of the 100 requests only about five requests per second were made by the export action.

Note that the effect of export on Exchange Server 2013 may be different. Exchange Server 2013 queries are variable, particularly eDiscovery queries that are often long and complex.

Large-scale document repositories with SharePoint Server 2013

## Large-scale document repositories with SharePoint Server 2013

Aside from the compliance and eDiscovery features, the SharePoint Server 2013 large scale document repositories feature has not changed significantly from SharePoint Server 2010. In this section, we refer to Scale test report for very large scale document repositories (SharePoint Server 2010), and point out differences for scenarios that involve SharePoint Server 2013 document repositories. The following sections summarize the main differences.

Guidance for putting interactive service applications on front-end web servers

### Guidance for putting interactive service applications on front-end web servers

Guidance for SharePoint Server 2010 advised you to put service applications on a separate tier. In SharePoint Server 2013, we recommend that you put the interactive service applications on computers that run as front-end web servers. For more information, see Capacity planning for SharePoint Server 2013.

Search in SharePoint Server 2013

### Search in SharePoint Server 2013

The SharePoint Server 2013 Search Service application merges the SharePoint Server 2010 Search and FAST Search Server 2010 for SharePoint into a unified search platform with additional functionality. For more information, see Scale search for Internet sites in SharePoint Server and Overview of search architecture in SharePoint Server.

Efficient File I/O and SQL Server improvements

### Efficient File I/O and SQL Server improvements

Efficient File I/O in SharePoint Server 2013 is a storage method in which a file is split into pieces that are stored and updated separately, and streamed together when a user requests the file. This results in more efficient file updates as only the updated pieces are written to SQL Server. Efficient File I/O is very effective when you use it with large files. Small files can see a small increase in the disk storage that is required. A direct result of using Efficient File I/O is that the throughput to update documents is improved.

Other improvements use SQL Server 2008 R2 with SP1 features and throughput to find documents for link fix-up and alert handling.

Column limits

### Column limits

Column limits are updated in SharePoint Server 2013. For more information, see Software boundaries and limits for SharePoint Server 2016.

See also

## See also

Concepts

#### Concepts

Estimate capacity and performance for compliance and eDiscovery for SharePoint Server 2013

Configure eDiscovery in SharePoint Server

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
