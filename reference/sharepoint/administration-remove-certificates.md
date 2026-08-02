---
title: "Remove certificates - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-remove-certificates
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/remove-certificates
family: administration
documentKind: "how-to"
abstract: "Learn how SharePoint supports removing certificates."
---

# Remove certificates - SharePoint Server

Note

Remove certificates

# Remove certificates

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports removing certificates via Remove-SPCertificate PowerShell cmdlet.

- By default, SharePoint won't allow you to remove a certificate if it's currently assigned to a SharePoint object. You must override the default behavior if you want to force the removal of a certificate. If you override the default behavior, existing assignments of the certificate are cleared.

- The certificate and any private key associated with that certificate is removed from the Windows certificate store on every server in the SharePoint farm.

- The certificate and any private key associated with it's removed from the SharePoint configuration database.

- Any previous exports from the certificate through the SharePoint administration interface won't be removed. Those exported files will still exist.

Use the `Remove-SPCertificate` cmdlet to remove a certificate from SharePoint.

For example:

```
Remove-SPCertificate [-Identity] <SPServerCertificatePipeBind> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

The cmdlet parameters are:

| Parameter | Description |
| --- | --- |
| Identity | The certificate to remove from SharePoint. |
| Force | Specifies that the certificate should be removed from SharePoint, even if the certificate is currently assigned to SharePoint objects. If this parameter is specified, any existing assignments of the certificate are also cleared. If this parameter isn't specified and the certificate is assigned to a SharePoint object, the operation will fail. |

For example:

```
Remove-SPCertificate -Identity "Contoso SharePoint (2020)"
```

Additional resources

## Additional resources

- Last updated on 
		2024-05-30
