---
title: "New and improved features in SharePoint Server Subscription Edition Version 23H1 - SharePoint Server"
type: reference
domain: sharepoint
slug: what-s-new-new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release
family: what-s-new
documentKind: "overview"
abstract: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 23H1."
---

# New and improved features in SharePoint Server Subscription Edition Version 23H1 - SharePoint Server

Note

New and improved features in SharePoint Server Subscription Edition Version 23H1

# New and improved features in SharePoint Server Subscription Edition Version 23H1

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 23H1 feature update.

Summary of the features

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 23H1 feature update.

| **Feature** | **Release ring** | **More information** |
| --- | --- | --- |
| **Copy and move improvement in modern document library** | Standard release | For more information, see Copy and move improvement in modern document library.
 
This was part of *Early release* in the Version 22H2 feature update. |
| **Bulk editing in modern lists** | Standard release | For more information, see Bulk editing in modern lists. 
 
 This was part of *Early release* in the Version 22H2 feature update. |
| **Column formatting enhancement** | Standard release | For more information, see Column formatting enhancement. 
 
 This was part of *Early release* in the Version 22H2 feature update. |
| **Button web part** | Standard release | For more information, see Button web part.  
 
 This was part of *Early release* in the Version 22H2 feature update. |
| **Choose the default site language in the modern self-service site creation pane** | Standard release | For more information, see Choose the default site language in the modern self-service site creation pane. 
 
 This was part of *Early release* in the Version 22H2 feature update. |
| **New SharePoint RESTful ListData.svc implementation** | Standard release | For more information, see New SharePoint RESTful ListData.svc implementation. 
 
 This was part of *Early release* in the Version 22H2 feature update. |
| **Unified "uber" patches** | Standard release | For more information, see Unified "uber" patches. |
| **Support for SharePoint Framework (SPFx) version 1.5.1** | Standard release | For more information, see Support for SharePoint Framework (SPFx) version 1.5.1. |
| **New PowerShell cmdlets for variations feature** | Standard release | For more information, see New PowerShell cmdlets for variations feature. |
| **SharePoint Server recompiled with Visual C++ 2022** | Standard release | For more information, see SharePoint Server recompiled with Visual C++ 2022. |
| **Private key management in certificate management** | Early release | For more information, see Private key management in certificate management. |
| **Support for wildcard host header bindings** | Early release | For more information, see Support for wildcard host header bindings. |
| **Expanded usage of modern sharing dialog** | Early release | For more information, see Expanded usage of modern sharing dialog. |
| **Column totals in modern list views** | Early release | For more information, see Column totals in modern list views. |
| **Enhanced Quick Chart web part** | Early release | For more information, see Enhanced Quick Chart web part. |
| **Improved file picker** | Early release | For more information, see Improved file picker. |

Detailed description of features

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 23H1.

Note

Features previously introduced in the SharePoint Server Subscription Edition Version 22H2 feature update will not be described here. See New and improved features in SharePoint Server Subscription Edition Version 22H2 for descriptions of those features.

Unified "uber" patches

### Unified "uber" patches

Up until now, Microsoft would release two separate public updates each month for SharePoint Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition. The first public update was called the **STS** or **core** update and contained all of the language-independent file updates. The second public update was called the **WSSLOC** or **language pack** update and contained all of the language-dependent file updates. Both public updates were required to be installed to fully update a SharePoint farm, although a new language-dependent WSSLOC public update may not have been released every month.

Some SharePoint customers were confused by the need to download and install two separate updates to fully update their SharePoint farm each month. They may mistakenly only download and install one of those updates, which could lead to unexpected behavior in their SharePoint farms due to mismatched updates.

To simplify the process of updating your SharePoint Server farm, Microsoft will now only release a single update each month for SharePoint Server Subscription Edition, starting with the March 2023 public update. This single "uber" update combines all of the fixes that would have previously been released in separate STS and WSSLOC updates.

The single uber updates are cumulative, so you only need to install the latest uber update to be fully up to date with all of the latest fixes for SharePoint Server Subscription Edition. It isn’t necessary to install any of the previous STS or WSSLOC updates before installing the uber update. No additional STS or WSSLOC updates will be released after the February 2023 public updates.

Customers should remember to run the SharePoint upgrade actions in their farm after installing a new update to complete the patching and upgrade process. For more information, see Upgrade to SharePoint Server Subscription Edition.

For more information, see Software updates overview for SharePoint Server 2016, 2019, and Subscription Edition, and Install a software update for SharePoint Server.

Support for SharePoint Framework (SPFx) version 1.5.1

### Support for SharePoint Framework (SPFx) version 1.5.1

Previous versions of SharePoint Server Subscription Edition supported SharePoint Framework (SPFx) version 1.4.1. To expand the customization scenarios that SharePoint Server Subscription Edition supports, the 23H1 feature update adds support for SharePoint Framework (SPFx) version 1.5.1.

This is one step on our long-term journey to improve and expand the capabilities of SharePoint Framework in SharePoint Server Subscription Edition.
For more information about SharePoint Framework version 1.5.1, see SharePoint Framework v1.5.1 release notes.

New PowerShell cmdlets for variations feature

### New PowerShell cmdlets for variations feature

Previous versions of SharePoint Server included an `stsadm.exe -o variationsfixuptool` command to configure the variations feature of SharePoint. However, the `stsadm.exe` command line tool was removed in SharePoint Server Subscription Edition with no PowerShell cmdlets provided to replace this variations functionality.
SharePoint Server Subscription Edition Version 23H1 introduces four new PowerShell cmdlets that replaces the functionality of the `stsadm.exe -o variationsfixuptool` command.

Those cmdlets are:

- `Deploy-SPVariation -Identity <SPWebPipeBind> [-Recurse] [-Label <String>]`

- `Repair-SPVariation -Identity <SPWebPipeBind> [-Recurse] [-Label <String>]`

- `Test-SPVariation -Identity <SPWebPipeBind> [-Recurse] [-Label <String>]`

- `Get-SPVariationJob -Identity <SPWebPipeBind>`

For more information, see Cmdlet reference for SharePoint Server.

SharePoint Server recompiled with Visual C++ 2022

### SharePoint Server recompiled with Visual C++ 2022

Previous versions of SharePoint Server Subscription Edition were compiled with the Visual C++ 2019 compiler for unmanaged code. The SharePoint Prerequisite Installer that comes with the SharePoint Server Subscription Edition installed the Visual C++ Redistributable Package for Visual Studio 2015-2019 to support the binaries compiled with that compiler.

To ensure SharePoint Server can take advantage of the latest capabilities and fixes in the Visual C++ libraries, Microsoft has recompiled SharePoint Server Subscription Edition Version 23H1 with the Visual C++ 2022 compiler. The Version 23H1 feature update will automatically install the Visual C++ Redistributable Package for Visual Studio 2015-2022 to support the binaries recompiled with this compiler.

Private key management in certificate management

### Private key management in certificate management

SharePoint Server Subscription Edition introduced a new certificate management feature that allows SharePoint farm administrators to directly manage the deployment and lifecycle of SSL/TLS certificates in their SharePoint Server farms. The certificate management feature would apply a standard set of permissions to the private keys of these certificates regardless of their use cases.

To better support least privileges scenarios and minimize the permissions given to these private keys, SharePoint Server Subscription Edition Version 23H1 applies more granular and sophisticated permission management for these private keys. The permissions are based on the certificate assignments and will be dynamically updated when the certificate assignments change.

For example, if a certificate is assigned to perform client certificate authentication to an SMTP server, SharePoint ensures the process that’s connecting to the SMTP server has the necessary permissions to use the private key of that certificate. If a certificate is no longer assigned to perform client certificate authentication to an SMTP server, SharePoint removes permissions for that process so it no longer has access to the private key of that certificate.

APIs have been added to the *Microsoft.SharePoint.Administration.CertificateManagement.SPServerCertificate* class to allow third party integration with this functionality.

Support for wildcard host header bindings

### Support for wildcard host header bindings

Previous versions of SharePoint Server Subscription Edition support host header bindings that would allow multiple SharePoint web applications to share the same TCP port. However, SharePoint Server only supported explicit host header bindings such as "sharepoint.example.com". Sometimes customers may want to support multiple host-named site collections across multiple web applications, all using the same TCP port.

SharePoint Server Subscription Edition Version 23H1 adds support for specifying a wildcard host header binding for a web application. This allows you to specify different wildcard bindings across multiple web applications that can share the same TCP port such as `*.external.example.com` and `*.internal.example.com`. You can then provision host-named site collections in the first web application using the `*.external.example.com` DNS naming scheme (such as `site1.external.example.com`, `site2.external.example.com`, etc.) and other host-named site collections in the second web application using the `*.internal.example.com` DNS naming scheme (such as `site1.internal.example.com`, `site2.internal.example.com`, etc.).

Expanded usage of modern sharing dialog

### Expanded usage of modern sharing dialog

In previous releases of SharePoint Server Subscription Edition, using sharing functionality in lists, document libraries, pages, or site contents would trigger the classic sharing dialog, even when using the modern view in a modern Team site or Communication site.

To provide a more intuitive sharing experience, these sharing entry points have been updated to use SharePoint’s modern sharing dialog. The modern sharing dialog is also a more accessible experience.

Column totals in modern list views

### Column totals in modern list views

SharePoint Server Subscription Edition Version 23H1 adds support for displaying column totals in modern list views just like in classic list views. This option can be enabled in the **save view** feature.

Enhanced Quick Chart web part

### Enhanced Quick Chart web part

Previous versions of SharePoint Server Subscription Edition allowed users to manually enter data in the Quick Chart modern web part to render charts on modern pages. However, users were unable to connect the Quick Chart web part to a list or library within the site to consume its data.

SharePoint Server Subscription Edition Version 23H1 enhances the Quick Chart modern web part by adding a **Get data from a list or library on this site** option. Users can now configure the Quick Chart web part to consume data from a list or library within the site.

For more information, see Use the Quick Chart web part.

Improved file picker

### Improved file picker

SharePoint Server Subscription Edition Version 23H1 improves the modern file picker used by the Quick Links and File Viewer web parts. The Quick Links web part file picker can now support more file types such as PDF, TXT, MP4, M4V, MP3, OGG, and WAV. The File Viewer web part file picker can now support PDF files.

Additional resources

## Additional resources

- Last updated on 
		2023-09-06
