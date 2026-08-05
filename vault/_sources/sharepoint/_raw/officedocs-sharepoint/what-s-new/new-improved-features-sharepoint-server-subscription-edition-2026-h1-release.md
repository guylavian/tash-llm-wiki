---
title: "New and improved features in SharePoint Server Subscription Edition Version 26H1 - SharePoint Server"
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 26H1."
ms.topic: overview
---
Note

New and improved features in SharePoint Server Subscription Edition Version 26H1

# New and improved features in SharePoint Server Subscription Edition Version 26H1

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 26H1 feature update.

Summary of the features

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 26H1 feature update.

This was part of Early release in the Version 25H2 feature update.

This was part of Early release in the Version 25H2 feature update.

This was part of Early release in the Version 25H2 feature update.

This was part of Early release in the Version 25H2 feature update.

This was part of Early release in the Version 25H2 feature update.

| **Feature** | **Release ring** | **More information** |
| --- | --- | --- |
| **Modern People Card** | Standard release | For more information, see Modern People Card. |
| **Document Intelligence** | Standard release | For more information, see Document Intelligence. |
| **Support JWE encrypted tokens from Entra ID** | Early release |  |
| **Drag and drop functionality for web parts in publishing sites** | Early release |  |
| **AMSI Body Scan Defaults to “Full Mode”** | Early release |  |
| **Enhance Document Virus Check with AMSI Option** | Early release |  |
| **New enhancements for the Text web part** | Early release |  |
| **Config to exclude "Everyone" claim on People Picker** | Early release | For more information, see Config to exclude "Everyone" claim on People Picker. |

Detailed description of features

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 26H1.

Note

Features previously introduced in the Version 25H2 feature update won't be described here. For more information on Version 25H2, see New and improved features in SharePoint Server Subscription Edition Version 25H2.

Config to exclude "Everyone" claim on People Picker

### Config to exclude "Everyone" claim on People Picker

SharePoint Server introduces a configurable capability that allows administrators to exclude the "Everyone" claim from People Picker suggestions at the Web Application level. When enabled, the "Everyone" claim is no longer resolved or suggested during People Picker searches, reducing the risk of unintentionally granting broad access when assigning permissions. This configuration is centrally enforced and applies consistently across all site collections hosted by the Web Application. Existing permissions and content access are not modified.

**Key Benefits**

- Prevents accidental over‑sharing: Reduces the likelihood of site owners or administrators granting permissions to an overly broad audience by mistake.

- Improves security hygiene: Helps organizations align with least‑privilege and access‑governance requirements by removing implicit, high‑risk identities from permission assignment workflows.

- Centralized and consistent enforcement: Configuration is applied once at the Web Application scope and automatically enforced across all site collections.

- Low operational risk: Existing permissions, users, and content remain unchanged. Only People Picker resolution behavior is affected.

**Configuration**

Scope: Web Application

Default value: Disabled (False)

Persistence: The setting is stored as a persisted property on SPPeoplePickerSettings and saved in the SharePoint Configuration Database (SP_CONFIG). The configuration is farm‑wide, durable, and automatically replicated to all servers. No web.config edits are required.

Prerequisites

- SharePoint Server Subscription Edition

- Farm administrator permissions

- SharePoint Management Shell

**How to use the feature**

Enable this feature

```
    $wa = Get-SPWebApplication `https://contoso`
    $wa.PeoplePickerSettings.ExcludeEveryoneClaim = $true
    $wa.Update()
```

Disable this feature

```
    $wa = Get-SPWebApplication `https://contoso`  
    $wa.PeoplePickerSettings.ExcludeEveryoneClaim = $false  
    $wa.Update()
```

Additional resources

## Additional resources

- Last updated on 
		2026-06-11
