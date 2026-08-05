---
title: "Move certificates between certificate stores - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-move-certificates-between-certificate-stores
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/move-certificates-between-certificate-stores
family: administration
documentKind: "upgrade-and-migration-article"
abstract: "Learn how SharePoint supports moving certificates."
---

# Move certificates between certificate stores - SharePoint Server

Note

Move certificates between certificate stores

# Move certificates between certificate stores

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports moving certificates between certificate stores using the Move-SPCertificate PowerShell cmdlet.

```
Move-SPCertificate [-Identity] <SPServerCertificatePipeBind> -NewStore {Default | EndEntity | Intermediate | Root} [-Force]
```

The cmdlet parameters are:

| Parameter | Description |
| --- | --- |
| Identity | The certificate to move. |
| NewStore (Default / EndEntity / Intermediate / Root) | The certificate store to move the certificate to. If Default is specified, SharePoint will automatically select the appropriate certificate store for the certificate. |
| Force | Specifies that the certificate should be moved to a different certificate store, even if the certificate is currently assigned to SharePoint objects.
 If this parameter is specified, any existing assignments of the certificate are cleared. If this parameter isn't specified and the certificate is assigned to a SharePoint object, the operation will fail. |

Example cmdlet syntax:

```
Move-SPCertificate -Identity "Contoso SharePoint (2020)" -NewStore EndEntity
```

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
