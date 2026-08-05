---
title: "Assign certificates to web applications - SharePoint Server"
description: "Learn how to assign SharePoint-managed certificates.."
ms.topic: article
---
Note

Assign certificates to web applications

# Assign certificates to web applications

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports assigning SharePoint-managed certificates, which are imported by using the Import-SPCertificate PowerShell cmdlet, to web applications with an SSL binding. The certificate must be in SharePoint's End Entity certificate store and the certificate's private key must also be imported. You can assign a certificate when the web application is first created or after it's created.

A `-Certificate <SPServerCertificatePipeBind>` parameter has been added to the following cmdlets and commands:

- New-SPWebApplication

- New-SPWebApplicationExtension

- Set-SPWebApplication

- New-SPCentralAdministration

- Set-SPCentralAdministration

- PSConfig.exe -cmd adminvs

The `SPServerCertificatePipeBind` accepts the following values:

- **String:** Friendly name of the certificate.

- **String:** Thumbprint of the certificate.

- **String:** Serial number of the certificate.

- **GUID:** ID property of the SPServerCertificate object.

To assign a certificate to a web application, while creating that web application or extending a web application to another zone through Central Administration, then set "Use Server Sockets Layer (SSL)" to **Yes**.

Select the **server certificate** from the **Server Certificate** drop-down list.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
