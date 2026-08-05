---
title: "Set up OIDC authentication in SharePoint Server using RSA public keys - SharePoint Server"
description: "Learn how to set up OIDC authentication in SharePoint Server using RSA public keys with Microsoft Entra ID."
ms.topic: install-set-up-deploy
---
Note

Set up OIDC authentication in SharePoint Server using RSA public keys

# Set up OIDC authentication in SharePoint Server using RSA public keys

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

OIDC is an authentication protocol that uses JSON Web Tokens (JWTs) to verify the identity of users, and grant them access to protected resources. JWTs are digitally signed using either symmetric keys (shared between the issuer and the consumer) or asymmetric keys (public/private key pairs).

SharePoint Server currently supports OIDC auth flow with x5c keys, which are certificates that contain the public key and other metadata. However, some OIDC providers may not use x5c keys, but instead use RSA public keys that are directly represented with RSA modulus and RSA public exponent. To support these providers, SharePoint Server added the ability to parse and validate RSA public keys in JWTs.

This article explains the new improvements from Version 24H2 that will help you set up OIDC authentication in SharePoint Server using RSA public keys.

OIDC configuration with RSA public keys overview

## OIDC configuration with RSA public keys overview

- Set up OIDC with Microsoft Entra ID using Global Administrator credentials by performing the steps mentioned here.

- Modify the SharePoint Server farm properties based on the version of your SharePoint Server farm. For more information, see change SharePoint farm properties.

- Configure SharePoint to trust the identity provider by creating `SPTrustedIdentityTokenIssuer` with RSA public keys using the steps mentioned in this article.

- Configure a web application in SharePoint to be federated with the Microsoft Entra OIDC, using the `SPTrustedIdentityTokenIssuer` created in the previous step. For more information, see create a new web application.

- Ensure the web application is configured with SSL certificate. To configure the web application, perform the steps to set the certificate.

- Create a team site collection as both Windows administrator and federated (Microsoft Entra ID) administrator. For more information, see create the site collection.

- Set up a People Picker by using a Custom Claims Provider, or the new UPA-backed claim provider included in SharePoint Server Subscription Edition. See set up People Picker.

Step 3: Configure SharePoint to trust the identity provider with RSA public keys

## Step 3: Configure SharePoint to trust the identity provider with RSA public keys

For RSA public keys, you create or set up a `SPTrustedTokenIssuer` to store the configuration that SharePoint needs to trust as the OIDC provider. You can configure SharePoint to trust the identity provider either manually or by using the metadata endpoint.

Configure SharePoint OIDC with RSA public keys by using metadata endpoint

### Configure SharePoint OIDC with RSA public keys by using metadata endpoint

An admin can follow the same PowerShell command that is used for x5c keys when using a metadata endpoint for RSA public keys. SharePoint figures out which kind of key is used from the metadata endpoint response and creates the `SPTrustedIdentityTokenIssuer` appropriately. For more information, see configure SharePoint to trust Microsoft Entra ID by using metadata endpoint for an example.

Configure SharePoint OIDC with RSA public keys manually

### Configure SharePoint OIDC with RSA public keys manually

When manually creating or setting up the `SPTrustedIdentityTokenIssuer` for RSA public keys, you must specify a new `-PublicKey` parameter while running the `New-SPTrustedIdentityTokenIssuer` or `Set-SPTrustedIdentityTokenIssuer` cmdlets to define the RSA public key modulus and exponent.

New-SPTrustedIdentityTokenIssuer

#### New-SPTrustedIdentityTokenIssuer

You can run the following PowerShell cmdlet with `-PublicKey` parameter:

```
New-SPTrustedIdentityTokenIssuer -Name "RSA-Manual" -Description "RSA Manually Created" -PublicKey $publicKeyXML -ClaimsMappings $emailClaimMap -IdentifierClaim $emailClaimMap.InputClaimType -DefaultClientIdentifier $clientIdentifier -RegisteredIssuerName $registeredissuernameurl -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -Scope "openid profile" 
```

The `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet uses the following parameters:

`<RSAKeyValue><Modulus>modulus</Modulus><Exponent>exponent</Exponent></RSAKeyValue>`

| Parameter | Description |
| --- | --- |
| Name | Gives a name to the new token issuer. |
| Description | Gives a description to the new token issuer. |
| PublicKey |  |
| ClaimsMappings | A `SPClaimTypeMapping` object, which is used to identify which claim in the `id_token` is regarded as identifier in SharePoint. |
| IdentifierClaim | Specifies the type of identifier. |
| DefaultClientIdentifier | Specifies the `client_id` of SharePoint server, which is assigned by OIDC identity provider. This is validated against aud claim in `id_token`. |
| RegisteredIssuerName | Specifies the issuer identifier, which issues the `id_token`. It's used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifies the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifies the sign out endpoint of the OIDC identity provider. |

To extract the correct `$publicKeyXML` value from an x509 certificate, you can run the following PowerShell command:

```
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 

$cert.Import("c:\certs\YourSigningCertificateHere.cer") 

$publicKeyXml = $cert.PublicKey.Key.ToXmlString($false) 
```

Set-SPTrustedIdentityTokenIssuer

#### Set-SPTrustedIdentityTokenIssuer

The `Set-SPTrustedIdentityTokenIssuer` cmdlet supports the new `-PublicKey` parameter for RSA public keys and takes the same `<RSAKeyValue><Modulus>modulus</Modulus><Exponent>exponent</Exponent></RSAKeyValue>` XML string that `New-SPTrustedIdentityTokenIssuer` uses. Example:

```
Set-SPTrustedIdentityTokenIssuer -Identity "RSA-Manual" -PublicKey $publicKeyXml -IsOpenIDConnect 
```

Improvements for OIDC configuration

## Improvements for OIDC configuration

With Version 24H2, admins can expect the following improvements when configuring the SharePoint Server to trust the identity provider.

Allow to configure multiple client identifiers in OIDC

### Allow to configure multiple client identifiers in OIDC

Configuring of multiple client identifiers is now allowed using -ScopedClientIdentifier switch in an OIDC `SPTrustedIdentityTokenIssuer`. Run the following command:

```
Set-SPTrustedIdentityTokenIssuer -Identity <name> -ScopedClientIdentifier Dictionary<Uri,string> -IsOpenIDConnect 
```

Enable ClaimsMappings editing capability in Set-SPTrustedIdentityTokenIssuer

### Enable ClaimsMappings editing capability in Set-SPTrustedIdentityTokenIssuer

​​In previous releases of SharePoint Server, when creating `SPTrustedIdentityTokenIssuer`, you need to provide the claims mappings list, which is used to map the claim from IdP token to SharePoint issued token. After `SPTrustedIdentityTokenIssuer` is created, you can only remove the existing claim mapping, or add the removed claim mapping back, which is identically the same as you removed. But, you can't add new claim mapping, which isn't originally in the list or change an existing claim mapping in place.

The new update from Version 24H2 build allows users to add a new parameter to `Set-SPTrustedIdentityTokenIssuer` so they can change the claims mappings list. With this new following parameter, you can even modify the claim mappings list of the token issuer.

New parameter: `-ClaimsMappings <SPClaimMappingPipeBind[]>`

Support OIDC IdPs that can't work with wildcard characters in redirection URL

### Support OIDC IdPs that can't work with wildcard characters in redirection URL

Some OIDC IdPs, such as Azure Active Directory B2C, can’t work with wildcard characters in the redirect URL. This causes SharePoint to be unable to redirect back to the original resource that is being asked after the authentication. In this release, we added a state property in the response header to preserve the redirect URL so that SharePoint will be able to know which URL to redirect to.

You can use the following PowerShell cmdlet to enable it on the tokenissuer you've created:

```
Set-SPTrustedIdentityTokenIssuer -Identity <name> -UseStateToRedirect:$True -IsOpenIDConnect
```

Refresh certificate by timer job

### Refresh certificate by timer job

A new timer job (RefreshMetadataFeed) is created to automatically fetch the latest configuration settings from configured OIDC metadata endpoint on daily basis and update OIDC trusted token issuer accordingly. It includes the certificates used for token encryption and signing, token issuer, authorization endpoint and SignoutUrl. You can change the frequency of refresh by changing the timer job schedule. For example, you can change the schedule of timer job to “5:00 every Saturday” by using PowerShell:

```
Get-SPTimerJob refreshmetadafeed | Set-SPTimerJob -Schedule "weekly at sat 5:00" 
```

This timer job is enabled when you set up a OIDC trusted token issuer with metadata endpoint. If you have a OIDC trusted token issuer setup before applying this update, you need to reset this token issuer again so that timer job can be enabled for this token issuer. You can reset the token issuer by using PowerShell

```
Set-SPTrustedIdentityTokenIssuer -Identity <OIDCtokenissuer> -MetadataEndPoint <URL> 
```

Additional resources

## Additional resources

- Last updated on 
		2024-09-10
