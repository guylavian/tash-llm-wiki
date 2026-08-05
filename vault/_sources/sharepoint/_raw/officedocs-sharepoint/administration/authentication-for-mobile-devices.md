---
title: "Authentication for mobile devices in SharePoint 2013 - SharePoint Server"
description: "This article contains information about the supported authentication types for select devices in SharePoint Server 2013."
ms.topic: article
---
Note

Authentication for mobile devices in SharePoint 2013

# Authentication for mobile devices in SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This article contains information about the supported authentication types for select devices in SharePoint Server 2013.

Plan for mobile device security

## Plan for mobile device security

Authentication is one aspect of security that you must consider to make sure that SharePoint Server 2013 is not compromised. We recommend that you consult the following articles to make sure that your corporate data is safe:

Mobile security and authentication in SharePoint 2013 (/SharePoint/administration/mobile-security-and-authentication)

The Importance of Smartphone Security

SharePoint Server 2013 supports multiple authentication methods and authentication modes. Not all mobile browsers and devices work with all the available authentication methods. When you plan for mobile device access, you must do the following:

Determine the mobile devices that you must support. Then, learn the authentication methods that are supported by the mobile devices. This information varies by manufacturer.

Determine the sites that you want to make available to your mobile device users.

Determine whether you want to make SharePoint sites available for mobile devices when the devices are used outside the corporate firewall. If you do, the method that you use to enable external access can also affect mobile device authentication.

Authentication for mobile devices

## Authentication for mobile devices

The following tables detail the authentication types for browsers and Office Hub Windows Phone experience in SharePoint Server 2013.

**Table: Mobile authentication support for SharePoint browsers**

| **SharePoint Infrastructure** | **Authentication mode** | **Authentication provider** | **Windows Phone 7.5 or later versions (Internet Explorer Mobile)** | **iOS 5.0 or later versions (iPad, iPhone using Safari)** |
| --- | --- | --- | --- | --- |
| SharePoint on-premises | NTLM | Active Directory | Supported | Supported |
| SharePoint on-premises | Basic authentication | Active Directory | Supported | Supported |
| SharePoint on-premises | SAML | WS-Federation 1.1 compatible Identity Provider | Supported | Supported |
| SharePoint in Microsoft 365 | Forms-based authentication | Org-ID | Supported | Supported |

**Table: Mobile authentication support for Office Hub**

| **SharePoint infrastructure** | **Authentication mode** | **Authentication provider** | **Windows Phone 7.5 or later versions** |
| --- | --- | --- | --- |
| SharePoint on-premises | NTLM | Active Directory | Supported |
| SharePoint on-premises | Basic authentication | Active Directory | Not supported |
| SharePoint on-premises | SAML | WS-Federation 1.1 compatible Identity Provider | Not supported |
| SharePoint in Microsoft 365 | Forms-based authentication | Org-ID | Supported |

Important

In order for mobile devices to communicate with SharePoint servers, Internet Protocol security (IPsec) must be disabled on the servers. This must be done because mobile devices are not domain-joined.

See also

## See also

Concepts

#### Concepts

Overview of mobile devices and SharePoint Server 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-20
