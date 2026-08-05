---
title: "Databases used by SharePoint have fragmented indices (SharePoint Server) - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-databases-used-by-sharepoint-have-fragmented-indices
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/databases-used-by-sharepoint-have-fragmented-indices
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to resolve the SharePoint Health Analyzer rule: Databases used by SharePoint have fragmented indices, for SharePoint Server."
---

# Databases used by SharePoint have fragmented indices (SharePoint Server) - SharePoint Server

Note

Databases used by SharePoint have fragmented indices (SharePoint Server)

# Databases used by SharePoint have fragmented indices (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Databases used by SharePoint have fragmented indices.

**Summary:** SharePoint Server uses SQL Server to store most of the content for the Web site and configuration settings. One or more of the databases used by SharePoint Server have fragmented indexes. A fragmented index can cause a degrade in performance.

**Cause:** Database indexes can fragment over time as a result of insert and update operations performed by SharePoint Server. We recommend that you periodically delete and rebuild these indexes to improve system performance.

**Resolution: Reorganize and rebuild indexes**

- To correct index fragmentation, you can reorganize an index or rebuild an index. For more information, see Reorganize and Rebuild Indexes.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
