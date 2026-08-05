---
title: "Inventory views"
type: reference
domain: sccm
slug: develop-inventory-views-configuration-manager
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/understand/sqlviews/inventory-views-configuration-manager
family: develop
documentKind: "reference"
abstract: "Hardware and software inventory information about the clients, files, and products, in the Configuration Manager hierarchy."
---

# Inventory views

# Inventory views in Configuration Manager

Inventory views contain hardware and software inventory information about the clients, files, products, and so forth, in the Configuration Manager hierarchy. Configuration Manager collects inventory data when you enable the Hardware Inventory Client Agent or Software Inventory Client Agent. Because you can configure which hardware inventory to collect during the hardware inventory scan cycle and which file types to scan for during the software inventory scan cycle, each site will have a unique set of inventory that is collected.

For each Configuration Manager site, it's possible to retrieve a list of the hardware and software inventory schema to determine exactly what is inventoried. The articles in this section provide examples of how to do get the hardware and software inventory lists, and detailed information about the typical Configuration Manager SQL views.

## In This Section

- [Hardware inventory views in Configuration Manager](hardware-inventory-views-configuration-manager.md)

- [Software inventory views in Configuration Manager](software-inventory-views-configuration-manager.md)

- [Asset intelligence views in Configuration Manager](asset-intelligence-views-configuration-manager.md)

## See also

[SQL Server views in Configuration Manager](sql-server-views-configuration-manager.md)
