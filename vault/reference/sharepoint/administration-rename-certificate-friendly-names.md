---
title: "Rename certificate friendly names - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-rename-certificate-friendly-names
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/rename-certificate-friendly-names
family: administration
documentKind: "how-to"
abstract: "Learn how SharePoint supports changing the friendly name of certificates."
---

# Rename certificate friendly names - SharePoint Server

Note

Rename certificate friendly names

# Rename certificate friendly names

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports changing the friendly name of certificates using the Rename-SPCertificate PowerShell cmdlet.

```
Rename-SPCertificate [-Identity] <SPServerCertificatePipeBind> -NewFriendlyName <string>
```

The cmdlet parameters are:

| Parameter | Description |
| --- | --- |
| Identity | The certificate to be renamed. |
| NewFriendlyName | The new friendly name for the certificate. |

Example cmdlet syntax:

```
Rename-SPCertificate -Identity "Contoso SharePoint" -NewFriendlyName "Contoso SharePoint (2020)"
```

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
