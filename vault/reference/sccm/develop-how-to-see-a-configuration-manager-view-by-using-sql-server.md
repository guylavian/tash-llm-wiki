---
title: "See a View by Using SQL Server"
type: reference
domain: sccm
slug: develop-how-to-see-a-configuration-manager-view-by-using-sql-server
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/how-to-see-a-configuration-manager-view-by-using-sql-server
family: develop
documentKind: "how-to"
abstract: "The following examples demonstrate various Microsoft Configuration Manager SQL view queries."
---

# See a View by Using SQL Server

# How to See a Configuration Manager View by Using SQL Server
The following examples demonstrate various Microsoft Configuration Manager SQL view queries.

## Examples

#### To determine the display name of a resource type from the resource type number

-   In SQL Server, query the Configuration Manager database with the following SQL statement:

```
select DisplayName from v_ResourceMap where ResourceType=5
```

#### To determine discovery properties for a particular resource type

-   In SQL Server, query the Configuration Manager database with the following SQL statement:

```
select * from v_ResourceAttributeMap where ResourceType=5
```

#### To list the inventory groups for a particular resource type

-   In SQL Server, query the Configuration Manager database with the following SQL statement:

```
select InvClassName from v_GroupMap where ResourceType = 5
```
