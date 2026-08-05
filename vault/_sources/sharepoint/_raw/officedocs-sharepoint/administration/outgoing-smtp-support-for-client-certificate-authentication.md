---
title: "Outgoing SMTP support for client certificate authentication - SharePoint Server"
description: "Learn how some SMTP servers may require the use of client certificates for authentication before accepting email messages."
ms.topic: article
---
Note

Outgoing SMTP support for client certificate authentication

# Outgoing SMTP support for client certificate authentication

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Some SMTP servers may require the use of client certificates for authentication before accepting email messages. SharePoint now supports client certificate authentication when sending emails to an SMTP server. The outbound SMTP settings in SharePoint must be configured to use TLS connection encryption and a certificate must be assigned to use this capability. The certificate must be in SharePoint's End Entity certificate store, the certificate's private key must be imported, and the certificate's enhanced key usage extension must specify the certificate is valid for client authentication if that extension is present.

A `-Certificate <SPServerCertificatePipeBind>` parameter has been added to the following cmdlet parameter set:

```
Set-SPWebApplication [-Identity] <SPWebApplicationPipeBind> -SMTPServer <String> [-Certificate <SPServerCertificatePipeBind>] [-DisableSMTPEncryption] [-Force] [-NotProvisionGlobally] [-OutgoingEmailAddress <String>] [-ReplyToEmailAddress <String>] [-SMTPServerPort <Int32>] [-SMTPCredentials <PSCredential>]
```

To assign a certificate to the outbound SMTP settings through Central Administration, set Use TLS connection encryption and Use client certificate authentication to **Yes**, and then select the client certificate from the **Client certificate** drop-down list.

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
