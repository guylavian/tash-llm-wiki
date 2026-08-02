---
title: "Query views"
type: reference
domain: sccm
slug: develop-query-views-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/query-views-configuration-manager
family: develop
documentKind: "reference"
abstract: "Information about all the queries in the Configuration Manager hierarchy."
---

# Query views

# Query views in Configuration Manager

Configuration Manager has only one query view, **v_Query**. It contains information about all the queries in the Configuration Manager hierarchy. The query ID, query name, comment, target class name, and the collection ID to which the query is limited, if applicable, are all listed.

The **v_Query** view can be joined to the **v_CollectionRuleQuery** collection view by using the **QueryID** column and to collection views by using the **LimitToCollectionID** column, which contains the same information as the **CollectionID** column in other views. It's also possible to join the query view to a security view so that the query name can be displayed when listing the class or instance permissions on the specific query object. An example is available in the section [Sample queries for queries in Configuration Manager](sample-queries-for-queries-configuration-manager.md).

## See also

[SQL Server views in Configuration Manager](sql-server-views-configuration-manager.md)
