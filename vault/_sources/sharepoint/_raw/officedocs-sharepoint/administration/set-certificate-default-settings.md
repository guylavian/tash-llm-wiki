---
title: "Set certificate default settings - SharePoint Server"
description: "Learn how SharePoint supports farm-wide default settings for certificate management by creating, renewing certificates, and certificate health rule thresholds."
ms.topic: article
---
Note

Set certificate default settings

# Set certificate default settings

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint supports farm-wide default settings for certificate management. These include default properties for creating and renewing certificates and certificate health rule thresholds.

Use the Set-SPCertificateSettings PowerShell cmdlet to set the certificate management default settings.

```
Set-SPCertificateSettings [-OrganizationalUnit <String>] [-Organization <String>] [-Locality <String>] [-State <String>] [-Country <String>] [-KeyAlgorithm {ECC | RSA}] [-KeySize {0 | 2048 | 4096 | 8192 | 16384}] [-EllipticCurve {Default | nistP256 | nistP384 | nistP521}] [-HashAlgorithm {Default | SHA256 | SHA384 | SHA512}] [-RsaSignaturePadding {Default | Pkcs1 | Pss}] [-CertificateExpirationAttentionThreshold <Int32>] [-CertificateExpirationWarningThreshold <Int32>] [-CertificateExpirationErrorThreshold <Int32>] [<CommonParameters>]]
```

The cmdlet parameters are:

`RSA` is the most common and widely supported key algorithm for certificates. Select the RSA algorithm if you're unsure which type of key your certificate authority supports. `ECC` uses elliptic curve cryptography based on ECDSA keys with NIST P-256, P-384, or P-521 curves.

SSL/TLS connections are faster to complete with `ECC` certificates than `RSA` certificates at the equivalent security strength. Verify that your certificate authority supports `ECC` certificates before selecting it.

Select `2048` if you're unsure which key size to use. Key sizes larger than `4096` aren't recommended.

Select `nistP256` if you're unsure which elliptic curve to use. Elliptic curves larger than `nistP384` aren't recommended.

| Parameter | Description |
| --- | --- |
| OrganizationalUnit | The name of your department within your organization or company. |
| Organization | The legally registered name of your organization or company. |
| Locality | The name of the city or locality where your organization is legally located. Don't abbreviate the name. |
| State | The name of the state or province where your organization is legally located. Don't abbreviate the name. |
| Country | The two letter country code where your organization is legally located. This must be an ISO 3166-1 alpha-2 country code. |
| KeyAlgorithm (ECC / RSA) |  |
| KeySize (0 / 2048 / 4096 / 8192 / 16384) |  |
| EllipticCurve (Default / nistP256 / nistP384 / nistP521) |  |
| HashAlgorithm (Default / SHA256 / SHA384 / SHA512) | Specifies the hash algorithm of your certificate signature, which your certificate authority will use to verify that your certificate request hasn't been tampered with. Larger hash algorithms provide more cryptographic strength than smaller hash algorithms, but they're also more computationally expensive. Select `SHA256` if you're unsure which hash algorithm to use. Hash algorithms larger than `SHA384` aren't recommended. |
| RsaSignaturePadding | Specifies the RSA signature padding mode for creating and renewing certificates with RSA keys. `Pkcs1` represents the RSASSA-PKCS1-v1_5 padding mode. `Pss` represents the RSASSA-PSS padding mode. The default RSA signature padding mode is `Pkcs1`. |
| CertificateExpirationAttentionThreshold | Specify the number of days before a certificate expires to trigger a certificate expiration notification. This is a reminder of upcoming certificate expirations that can be handled with normal priority. A certificate will only trigger a notification when it's assigned to SharePoint objects. This alert is disabled when set to 0. |
| CertificateExpirationWarningThreshold | Specifies the number of days before a certificate expires to trigger a certificate expiration warning. This is a warning of imminent certificate expirations that should be handled with high priority. A certificate will only trigger a warning when it is assigned to SharePoint objects. This warning is disabled when set to 0. |
| CertificateExpirationErrorThreshold | Specifies the number of days after a certificate expired to trigger a certificate expiration alert. This is an alert about certificates that have already expired and should be handled with critical priority. A certificate will only trigger an alert when it is assigned to SharePoint objects. This alert is disabled when set to 0. |

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
