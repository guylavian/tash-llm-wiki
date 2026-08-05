---
title: "Configure Web Application Proxy for a hybrid environment - SharePoint Server"
type: reference
domain: sharepoint
slug: hybrid-configure-web-application-proxy-for-a-hybrid-environment
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/hybrid/configure-web-application-proxy-for-a-hybrid-environment
family: hybrid
documentKind: "how-to"
abstract: "Learn how to configure Windows Server 2012 R2 with Web Application Proxy (WA-P) as a reverse proxy device in a SharePoint hybrid environment."
---

# Configure Web Application Proxy for a hybrid environment - SharePoint Server

Note

Configure Web Application Proxy for a hybrid environment

# Configure Web Application Proxy for a hybrid environment

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article describes Web Application Proxy and helps you set it up to use as a reverse proxy for a hybrid SharePoint Server environment.

Before you begin

## Before you begin

**Accessibility note:** SharePoint Server supports the accessibility features of common browsers to help you administer deployments and access sites. For more information, see Accessibility for SharePoint 2013.

About Web Application Proxy in a hybrid environment

## About Web Application Proxy in a hybrid environment

Web Application Proxy is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices. It also includes proxy functionality for Active Directory Federation Services (AD FS). This helps system administrators provide secure access to an AD FS server. By using Web Application Proxy, system administrators choose how users authenticate themselves to a web application and can determine who is authorized to use one.

In hybrid SharePoint Server environments in which SharePoint in Microsoft 365 requests data from SharePoint Server, you can use Windows Server 2012 R2 with Web Application Proxy as a reverse proxy device to securely relay requests from the Internet to your on-premises SharePoint Server farm.

Important

To use Web Application Proxy as a reverse proxy device in a hybrid SharePoint Server environment, you must also deploy AD FS in Windows Server 2012 R2.

Note

To install and configure the Web Application Proxy feature, you must be a local administrator on the computer where Windows Server 2012 R2 is installed. The Windows Server 2012 R2 server running the Web Application Proxy feature can be a member of a domain or a workgroup.

Step 1: Install AD FS and the Web Application Proxy feature

## Step 1: Install AD FS and the Web Application Proxy feature

For info about installing AD FS in Windows Server 2012 R2, see Active Directory Federation Services Overview.

For info about installing the Web Application Proxy feature in Windows Server 2012 R2, see Install Server Roles and Features on a Server Core Server.

Step 2: Configure the Web Application Proxy

## Step 2: Configure the Web Application Proxy

This section describes how to configure the Web Application Proxy feature after it is installed:

Web Application Proxy matches the thumbprint against the secure channel certificate, which must be imported and installed in the local computer's Personal certificate store on the Web Application Proxy server.

Configure Web Application Proxy with a published application that can accept inbound requests from your SharePoint in Microsoft 365 tenant.

Import the Secure Channel SSL certificate

### Import the Secure Channel SSL certificate

You must import the Secure Channel SSL certificate into the Personal store of the local computer account and then set permissions on the certificate's private key to allow the service account of the Web Application Proxy Service (appproxysvc) Full Control.

Note

The default service account of the Web Application Proxy Service is the local computer **Network Service**.

|  |  |
| --- | --- |
|  | The location of the **Secure Channel SSL certificate** is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**.  
 If the certificate contains a private key, you will need to provide the certificate password, which is recorded in **Row 4** (Secure Channel SSL Certificate password) of **Table 4b: Secure Channel SSL Certificate**. |

For information about how to import an SSL certificate, see Import a Certificate.

Configure the published application

### Configure the published application

Note

The steps in this section can be performed only by using Windows PowerShell.

To configure a published application to accept and relay requests from your SharePoint in Microsoft 365 tenant, type the following Microsoft PowerShell command.

```
Add-WebApplicationProxyApplication -ExternalPreauthentication ClientCertificate -ExternalUrl <external URL> -BackendServerUrl <bridging URL> -name <friendly name of the published application> -ExternalCertificateThumbprint <certificate thumbprint> -ClientCertificatePreauthenticationThumbprint <certificate thumbprint> -DisableTranslateUrlInRequestHeaders:$False -DisableTranslateUrlInResponseHeaders:$False
```

Where:

- *<externalUrl>* is the external URL for the web application. This is the public URL to which SharePoint in Microsoft 365 will send inbound requests for SharePoint Server content and resources.

|  |  |
| --- | --- |
|  | The external URL is recorded in **Row 3** (External URL) of **Table 3: Public Domain Info** in the SharePoint Hybrid worksheet. |

- *<bridging URL>* is the internal URL you configured for the primary web application in your on-premises SharePoint Server farm. This is the URL to which Web Application Proxy will relay inbound requests from SharePoint in Microsoft 365.

|  |  |
| --- | --- |
|  | The bridging URL is recorded in one the following locations in the SharePoint Hybrid worksheet:  
  If your primary web application is configured with a *host-named site collection*, use the value in **Row 1** (Primary web application URL) of **Table 5a: Primary web application (host-named site collection)**.  
  If your primary web application is configured with a  *path-based site collection*  , use the value in **Row 1** (Primary web application URL) of **Table 5b: Primary web application (path-based site collection without AAM)**.  
  If your primary web application is configured with a  *path-based site collection with AAM*  , use the value in **Row 5** (Primary web application URL) of **Table 5c: Primary web application (path-based site collection with AAM)**. |

*<friendly name of the published application>* is a name you choose to identify the published application in Web Application Proxy.

*<certificate thumbprint>* is the certificate thumbprint, as a string with no spaces, of the certificate to use for the address specified by the  *ExternalUrl* parameter. This value should be entered twice, once for the *ExternalCertificateThumbprint* parameter and again for the *ClientCertificatePreauthenticationThumbprint* parameter.

|  |  |
| --- | --- |
|  | This is the thumbprint of the **Secure Channel SSL certificate**. The location of this certificate file is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**. |

For additional info about the **Add-WebApplicationProxyApplication** cmdlet, see Add-WebApplicationProxyApplication.

Validate the published application

## Validate the published application

To validate the published application, use the **Get-WebApplicationProxyApplication** cmdlet. Enter the following Microsoft PowerShell command:

```
Get-WebApplicationProxyApplication |fl
```

The output should resemble the content in the following table.

|  |  |
| --- | --- |
| ADFSRelyingPartyID | :<populated at run time> |
| ADFSRelyingPartyName | :<relying party name> |
| BackendServerAuthenticationMode | :ADFS |
| BackendServerAuthenticationSPN | : None |
| BackendServerCertificateValidation | : None |
| BackendServerUrl | : https://<bridging URL>/ |
| ClientCertificateAuthenticationBindingMode | : None |
| ClientCertificatePreauthenticationThumbprint : | : <certificate thumbprint> |
| DisableTranslateUrlInRequestHeaders | : False |
| DisableTranslateUrlInResponseHeaders | : False |
| ExternalCertificateThumbprint | : <certificate thumbprint> |
| ExternalPreauthentication | : PassThrough |
| ExternalUrl | : https://<external URL>/ |
| ID | : 91CFE805-44FB-A8A6-41E9-6197448BEA72 |
| InactiveTransactionsTimeoutSec | : 300 |
| Name | : <friendly name of the published application> |
| UseOAuthAuthentication | : False |
| PSComputerName | : |

Troubleshooting

## Troubleshooting

Web Application Proxy logs events and errors to the Application and Remote Access Windows Server event logs. Logging plays an important role in troubleshooting issues with connectivity and authentication between SharePoint Server and SharePoint in Microsoft 365. Identifying the component that is causing a connection failure can be challenging, and reverse proxy logs are the first place you should look for clues. Troubleshooting can involve comparing log events from Web Application Proxy event logs, SharePoint Server ULS logs, Windows Server event logs, and Internet Information Services (IIS) logs on multiple servers.

For more info about troubleshooting techniques and tools for SharePoint Server hybrid environments, see Troubleshooting hybrid environments.

See also

## See also

Concepts

#### Concepts

Hybrid for SharePoint Server

Configure a reverse proxy device for SharePoint Server hybrid

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
