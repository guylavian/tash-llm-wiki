---
title: "Export certificates - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-export-certificate
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/export-certificate
family: administration
documentKind: "article"
abstract: "Learn how SharePoint export the certificates."
---

# Export certificates - SharePoint Server

Note

Export certificates

# Export certificates

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports exporting certificates to PFX (PKCS #12) files, P7B (PKCS #7) files, and CER files. Both PFX files and P7B files can contain multiple certificates, which is useful for exporting a chain of certificates from the end entity (leaf) certificate to the root certificate. However, only PFX files can contain private keys for certificates, which are necessary for a server certificate to be assigned to an IIS website. CER files contain only a single certificate.

Use the `Export-SPCertificate` PowerShell cmdlet to import certificates from certificate files.

This cmdlet supports multiple parameter sets:

```
Export-SPCertificate [-Identity] <SPServerCertificatePipeBind> -Password <securestring> [-EncryptionType {AES256 | TripleDes}] [-IncludeAllCertificatesInCertificationPath] [-IncludeExtendedProperties] [-Path <string>] [-Force]
Export-SPCertificate [-Identity] <SPServerCertificatePipeBind> -Type {Cert | Pkcs7} [-IncludeAllCertificatesInCertificationPath] [-Path <string>] [-Force]
```

The cmdlet parameters are:

| Parameter | Description |
| --- | --- |
| Identity | The certificate to export. -Password The password to use to protect the exported PFX file. This parameter is only compatible with PFX files. |
| EncryptionType | Specifies the encryption algorithm to use to protect the exported PFX file. AES256 specifies that `AES-256` encryption with SHA256 hashing will be used. TripleDes specifies that 3DES encryption with SHA1 hashing will be used. `AES-256` encryption is stronger than 3DES encryption, but is only supported with PFX files on Windows Server 2019 and newer operating systems. Use 3DES encryption if the PFX file needs to be compatible with older operating systems. If this parameter is not specified, `AES-256` encryption is used by default. This parameter is only compatible with PFX files |
| Type | Specifies the type of file to generate. Cert will generate a CER file containing a single DER-encoded certificate. Pkcs7 will generate a P7B (PKCS #7) file containing one or more certificates. This parameter is only compatible with CER and P7B files |
| IncludeAllCertificatesInCertificationPath | Specifies whether to export additional certificates that are part of the certificate chain of the specified certificate. This will only add parent certificates of the specified certificate, not child certificates issued by the specified certificate. This parameter is only compatible with PFX and P7B files. |
| IncludeExtendedProperties | Specifies whether extended properties of the certificate should be exported, such as the friendly name of the certificate. This parameter is only compatible with PFX files. |
| Path | Specifies the path to the PFX, P7B, or CER file containing certificates. |
| Force | Specifies whether to overwrite a file if it already exists at the specified path. Example cmdlet syntax: `$password = ConvertTo-SecureString -AsPlainText -Force Export-SPCertificate -Identity "Contoso SharePoint (2020)" -Password $password -IncludeAllCertificatesInCertificationPath -IncludeExtendedProperties -Path "\server\fileshare\certificates.pfx`". |

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
