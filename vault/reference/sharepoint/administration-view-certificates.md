---
title: "View certificates - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-view-certificates
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/view-certificates
family: administration
documentKind: "how-to"
abstract: "Learn how SharePoint supports finding the certificates."
---

# View certificates - SharePoint Server

Note

View certificates

# View certificates

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports finding certificates via the Get-SPCertificate PowerShell cmdlet. Optional parameters are available to filter the results returned by this cmdlet.

```
Get-SPCertificate [-Identity] <SPServerCertificatePipeBind>
Get-SPCertificate [-DisplayName] <String> [-Thumbprint <String>] [-SerialNumber <String>] [-Store {EndEntity | Intermediate | Pending | Root}] [-InUse] [-DaysToExpiration <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

The cmdlet parameters are:

| Parameter | Description |
| --- | --- |
| Identity | Specifies the display name, thumbprint, serial number, or GUID of the certificate to find. If multiple certificates match the identity specified, no certificates are returned. Use the filtering criteria of the optional parameters when multiple certificates would match. |
| DisplayName | The display name of the certificate to find. Use this parameter instead of the Identity parameter if multiple certificates might match this criteria. The Identity parameter can only return a single certificate. |
| Thumbprint | The thumbprint of the certificate to find, in the form "1234567890ABCDEF1234567890ABCDEF12345678". |
| SerialNumber | The serial number of the certificate to find, in the form "1234567890ABCDEF1234567890ABCDEF" |
| Store (EndEntity / Intermediate / Pending / Root) | Specifies the certificate store to search. If this parameter isn't specified, all certificate stores are searched. |
| InUse | Specify to only return certificates that are directly assigned to SharePoint objects (that is, currently in use). |
| DaysToExpiration | If a positive number, only return certificates that will expire in the number of days from now specified by this parameter. Specify "-1" to only return certificates that have already expired. Specifying "0" results in no filtering based on expiration date. |

The following are the examples of cmdlet syntax:

```
- Get-SPCertificate -FriendlyName "Contoso SharePoint (2020)"
- Get-SPCertificate -InUse -DaysToExpiration 30
```

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
