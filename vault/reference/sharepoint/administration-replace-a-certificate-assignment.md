---
title: "Replace a certificate assignment - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-replace-a-certificate-assignment
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/replace-a-certificate-assignment
family: administration
documentKind: "how-to"
abstract: "Learn how SharePoint supports replacing all usage of an existing certificate within SharePoint with a different certificate."
---

# Replace a certificate assignment - SharePoint Server

Note

Replace a certificate assignment

# Replace a certificate assignment

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports replacing all usage of an existing certificate within SharePoint with a different certificate. For example, if an existing certificate is approaching its expiration and you can replace this existing certificate with a new certificate. Use the Switch-SPCertificate Powershell cmdlet to replace the assignments of the existing certificate with the new certificate. All usage of the existing certificate within SharePoint will then be replaced with the new certificate.

For example:

```
Switch-SPCertificate [-Identity] <SPServerCertificatePipeBind> [-NewCertificate] <SPServerCertificatePipeBind> [-WhatIf] [-Confirm] [<CommonParameters>]
```

The cmdlet parameters are:

| Parameter | Description |
| --- | --- |
| Identity | The certificate whose assignments you want to replace. |
| NewCertificate | The certificate that should replace all of the assignments of the certificate specified by the Identity parameter. |

For example:

```
Switch-SPCertificate -Identity "Contoso SharePoint (2020)" -NewCertificate "Contoso SharePoint (2021)"
```

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
