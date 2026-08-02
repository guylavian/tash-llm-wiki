---
title: "Console ResourceAssembly Element"
type: reference
domain: sccm
slug: develop-console-resourceassembly-element
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/core/servers/console/console-resourceassembly-element
family: develop
documentKind: "article"
abstract: "Learn how to define the resources that are used by the node with the ResourceAssembly element in Configuration Manager."
---

# Console ResourceAssembly Element

# Configuration Manager Console ResourceAssembly Element
In Configuration Manager, the `ResourceAssembly` element defines the resources that are used by the node. The following XML defines the assembly, `AdminUI.CollectionProperty.dll`, and the type of the resource within the assembly.

```
<ResourceAssembly>
    <Assembly>AdminUI.CollectionProperty.dll</Assembly>
    <Type>Microsoft.ConfigurationManagement.AdminConsole.CollectionProperty.Properties.Resources.resources</Type>
</ResourceAssembly>

```

## See Also
 [About Configuration Manager Administrator Console Nodes](../../../../develop/core/servers/console/about-configuration-manager-console-nodes.md)
 [How to Find a Configuration Manager Node GUID](../../../../develop/core/servers/console/how-to-find-a-configuration-manager-console-node-guid.md)
 [Configuration Manager Console Node XML](../../../../develop/core/servers/console/console-node-xml.md)
