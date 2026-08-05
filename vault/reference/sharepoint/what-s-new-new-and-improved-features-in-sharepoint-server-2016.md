---
title: "New and improved features in SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: what-s-new-new-and-improved-features-in-sharepoint-server-2016
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-2016
family: what-s-new
documentKind: "overview"
abstract: "Learn about the new features and updates to existing features in SharePoint Server 2016."
---

# New and improved features in SharePoint Server 2016 - SharePoint Server

Note

New and improved features in SharePoint Server 2016

# New and improved features in SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the new features and updates to existing features in SharePoint Server 2016.

For a comparison of SharePoint on-premises features between SharePoint 2013 and SharePoint Server 2016 editions, see SharePoint feature availability across on-premises solutions. For new features in SharePoint Server 2016 for end users, see What's new in SharePoint Server 2016.

Summary of features

## Summary of features

The following table provides a summary of the new features that you can try out in this SharePoint Server 2016 release.

| **Feature** | **Description** | **More info** |
| --- | --- | --- |
| **Access Services** | New Access features are available when you deploy Access Services in SharePoint Server 2016. | For more info, see Access Services plus Access client and server. |
| **Compliance features** | New compliance features for SharePoint Server 2016 include the document deletion and in-place hold policies. | For more info, see Compliance features. |
| **Customized web parts** | The compile time for customized XSLT files used for Content Query, Summary Links, and Table of Contents Web Parts is improved. | NA |
| **Document Library accessibility** | SharePoint Server 2016 includes new document library accessibility features. | For more info, see Document Library accessibility. |
| **Durable links** | Resource-based URLs now retain links when documents are renamed or moved in SharePoint. | NA |
| **Encrypted Connections** | SharePoint Server 2016 supports TLS 1.2 connection encryption by default. | For more info, see Encrypted connections. |
| **Fast Site Collection Creation** | The Fast Site Collection Creation feature is a rapid method to create site collections and sites in SharePoint. | For more info, see Fast Site Collection Creation. |
| **Filenames - expanded support for special characters** | SharePoint Server 2016 now supports using some special characters in file names that were blocked in previous versions. | For more info, see File names - expanded support for special characters. |
| **Hybrid in SharePoint 2016** | Hybrid in SharePoint Server 2016 enables you to integrate your on-premises farm with Microsoft 365 productivity experiences, allowing you to adopt the cloud at your own pace. | For more info, see Hybrid in SharePoint Server 2016. |
| **Identify and search for sensitive content** | SharePoint Server 2016 now provides the same data loss prevention capabilities as Office 365. | For more info, see Identify and search for sensitive content in both SharePoint Server 2016 and OneDrive documents. |
| **Image and video previews** | You can now preview images and videos in SharePoint Server 2016 document libraries. | For more info, see Image and video previews. |
| **Information Rights Management** | SharePoint Server 2016 provides Information Rights Management (IRM) capabilities to secure info by encrypting and securing info about SharePoint libraries with OneDrive. | For more info, see Information Rights Management. |
| **Large file support** | SharePoint Server 2016 now supports uploading and downloading files larger than 2,047 MB. | For more info, see Large file support. |
| **MinRole** | MinRole is a new feature in SharePoint Server 2016 that allows a SharePoint farm administrator to define each server's role in a farm topology. | For more info, see MinRole farm topology. |
| **Mobile experience** | SharePoint Server 2016 offers an improved mobile navigation experience. | For more info, see Mobile experience. |
| **New features in November 2016 PU for SharePoint Server 2016 (Feature Pack 1)** | The November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1) offers seven new features for SharePoint Server 2016. | For more info, see New features in November 2016 PU for SharePoint Server 2016 (Feature Pack 1). |
| **New controls for working with OneDrive** | SharePoint Server 2016 provides controls at the top of your personal document folders that make common tasks in OneDrive more accessible. | For more info, see New controls for working with OneDrive. |
| **New Recycle Bin in OneDrive and Team sites** | SharePoint Server 2016 adds a link for the Recycle Bin in the left navigation area of the OneDrive and Team sites. | NA |
| **Open Document Format (ODF)** | SharePoint Server 2016 adds support for Open Document Format (ODF) files to use in document library templates. | For more info, see Open Document Format (ODF) available for document libraries. |
| **Project Server** | New Project Server features are available in SharePoint Server 2016. | For more info, see Project Server 2016 . |
| **ReFS file system support** | SharePoint Server 2016 now supports drives that are formatted with the ReFS file system. | For more info about the ReFS file system, see Resilient File System Overview and Resilient file system. |
| **SharePoint business intelligence** | SharePoint Server 2016 now supports SQL Server 2016 CTP 3.1 and the Power Pivot add-in and Power View. | For more info about SharePoint business intelligence, see Power Pivot add-in and Power View are now available to use with SharePoint Server 2016. |
| **SharePoint Search** | SharePoint Search Server Application has significant changes to its deployment. | For more info, see SharePoint Search Service application. |
| **Sharing improvements** | SharePoint Server 2016 has many new sharing improvements available. | For more info, see Sharing. |
| **Site Folders view** | SharePoint Server 2016 provides a new Site Folders view that lets you access the document libraries in sites that you're following. | For more info, see Site folders view. |
| **Sites page pinning** | This new feature helps you see and follow sites. | For more info, see Sites page pinning. |
| **SMTP Connection Encryption** | SharePoint Server 2016 supports sending email to SMTP servers that use **STARTTLS** connection encryption. | For more info, see SMTP connection encryption. |
| **SMTP ports (non-default)** | SharePoint Server 2016 adds support for SMTP servers that use TCP ports other than the default port (25). | For more info, see Use SMTP ports other than the default (25). |
| **Web Application Open Platform Interface Protocol (WOPI)** | You can now rename files, create new files, and share files from within the WOPI iframe on the browser page. | NA |

Detailed description of features

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server 2016.

Access Services plus Access client and server

### Access Services plus Access client and server

The following new Access features are available when you deploy Access Services in SharePoint Server 2016:

Support apps for Office. For more info, see Spice up your Access app with add-ins for Office.

Access App Upgrade. For more info, see Upgrade an Access app.

Download in Excel feature available for users to pivot Access tables. For more info, see Introducing a new feature in Access 2013 web apps-Download in Excel.

With the improved Related Item Control, you can do the following:

On the Related Item Control, select from any existing view for the dialog.

Add a new item on the Related Item Control when the parent record isn't saved.

At the bottom of the Related Item Control, turn off the **Add link**.

The **Cascading Combo** box is now available in Access. For more info, see Introducing a new user experience feature in Access web apps: Cascading Controls.

Central Administration is no longer provisioned on all servers by default

### Central Administration is no longer provisioned on all servers by default

SharePoint Server 2016 Central Administration is now provisioned on the first server in a farm by default when using the SharePoint Products Configuration Wizard. Central Administration isn't provisioned on other servers in a farm by default.

You can provision or unprovision Central Administration on individual servers in a farm, no matter what the server role is by using the following methods:

The **Services on Server** page on **Central Administration > System Settings**

Microsoft PowerShell cmdlets:

New-SPCentralAdministration

Remove-SPCentralAdministration

The  `psconfig.exe -cmd adminvs` operation

The **SharePoint Products Configuration Wizard**

Note

The state of Central Administration does not affect whether a server is considered compliant with MinRole. The MinRole health rule will not attempt to provision or unprovision Central Administration.

Compliance features

### Compliance features

The document deletion policy lets you delete documents in users' OneDrive sites after specific periods of time. The In-Place Hold policy allows administrators to preserve documents, email, and other files.

For more info, see Overview of document deletion policies.

Document Library accessibility

### Document Library accessibility

The following features are now available for working in SharePoint Server 2016 document libraries:

Landmarks to a page make it easier to navigate, and there are alt text improvements for all major navigation links.

Keyboard shortcuts are provided for the following document tasks:

Alt + **N** - **N** ew

Alt + **E** - **E** dit

Alt + **U** - **U** pload

Alt + **M** - **M** anage

Alt + **S** - **S** hare

Alt + **Y** - S **y** nchronization

Focus improvements, such as keeping focus on prior elements and focus trapping.

Announcements for upload progress.

Announcements for file name and file types when browsing folder and file lists.

Improved callout reading.

Fixed use of color issues for views switcher.

Updates to the Help documentation.

Encrypted connections

### Encrypted connections

When you set up an SSL binding in Internet Information Services (IIS) Manager to host your web application, SharePoint uses TLS 1.2 connection encryption if your client application supports it. SharePoint also supports TLS 1.2 connection encryption when connecting to other systems, for example when crawling websites.

Note

A security vulnerability was identified in the SSL 3.0 protocol that can allow an attacker to decrypt data. For enhanced security, some SharePoint features now disable SSL 3.0 connection encryption by default, as well as certain encryption algorithms (for example RC4) with known weaknesses. SharePoint disables SSL 3.0 connection encryption by default for some, but not all features. To ensure that SSL 3.0 is disabled for all features, you should disable it in Windows by editing the Windows Registry. For more info, see the "Disable SSL 3.0 in Windows For Server Software", and "For Client Software", workarounds in Microsoft Security Advisory 3009008.

Fast Site Collection Creation

### Fast Site Collection Creation

This new feature provides templates that work at same level as SQL Server, which reduces the round trips required between the SharePoint and SQL servers. Use the **SPSiteMaster** Microsoft PowerShell cmdlets to create sites and site collections quickly.

File names - expanded support for special characters

### File names - expanded support for special characters

SharePoint has historically blocked file names that included the **&**, **~**, **{**, and **}** characters, file names that contained a **GUID**, file names with leading dots, and file names longer than 128 characters. These restrictions are removed in SharePoint Server 2016 and are now available to use.

Important

Restricted characters such as **%** and **#** are still not allowed in file names. Page file names, such as wiki pages, may not contain the following characters: " # % * : < > ? \ / | nor can they begin with a leading dot (period) character.

Hybrid in SharePoint Server 2016

### Hybrid in SharePoint Server 2016

In SharePoint Server 2016, new hybrid features are available to enable hybrid solutions.

**Hybrid sites**

**Hybrid sites features** allows your users to have an integrated experience while using SharePoint Server and SharePoint in Microsoft 365 sites:

Users can follow SharePoint Server and SharePoint in Microsoft 365 sites, and see them consolidated in a single list.

Users have a single profile in Office 365, where all of their profile info is stored.

For more info, see SharePoint hybrid sites and search.

**Hybrid OneDrive**

Hybrid sites features are used in concert with **Hybrid OneDrive** (introduced in SharePoint Server 2013 with Service Pack 1 (SP1)):

Users can sync files with Office 365 and share them with others.

Users can access their files directly through Office 365 from any device.

**Cloud hybrid search**

Cloud hybrid search is a new hybrid search solution alternative. With cloud hybrid search:

You index all of your crawled content, including on-premises content, to your search index in Office 365. You can set up the crawler in SharePoint Server 2016 to crawl the same content sources and use the same search connectors in Office SharePoint Server 2007, SharePoint Server 2010, and SharePoint Server 2013.

When users query your search index in Office 365, they get unified search results from both on-premises and Office 365 content.

For more info about cloud hybrid search, see the public Microsoft cloud hybrid search program on Microsoft Office connection.

For more info, see Plan for hybrid OneDrive.

For more info about the hybrid solutions available today, visit the SharePoint Hybrid Solutions Center.

Identify and search for sensitive content in both SharePoint Server 2016 and OneDrive documents

### Identify and search for sensitive content in both SharePoint Server 2016 and OneDrive documents

With this new capability, you can:

**Search for sensitive content** across SharePoint Server 2016, SharePoint in Microsoft 365, and OneDrive.

**Leverage 51 built-in sensitive information types** (credit cards, passport numbers, Social Security numbers, and more).

To discover sensitive content relating to common industry regulations from the SharePoint eDiscovery Center, from the eDiscovery site collection, select **DLP Queries**, identify offending documents, and export a report.

Turn on **DLP Policies** from the Compliance Policy Center site collection to notify end users and administrators when documents with sensitive info are stored in SharePoint and automatically protect the documents from improper sharing.

Info about configuring and using this feature is documented in SharePoint and Microsoft 365. For more info, see:

- Search for sensitive content in SharePoint and OneDrive documents

Image and video previews

### Image and video previews

In SharePoint Server 2016, when you post images and videos to a document library, you can see a preview by hovering the mouse over the image or video, or by selecting them.

Information Rights Management

### Information Rights Management

For more info, see Secure and sync with Information Rights Management on OneDrive and Apply Information Rights Management to a list or library.

Large file support

### Large file support

Previous versions of SharePoint didn't support uploading or downloading files larger than 2,047 MB. SharePoint Server 2016 now allows you to upload or download larger files. You can configure the desired maximum file-size limit on a per-web application basis in your SharePoint farm.

MinRole farm topology

### MinRole farm topology

The role of a server is specified when you create a new farm or join a server to an existing farm. SharePoint automatically configures the services on each server based on the server role, optimizing the performance of the farm based on that topology. There are eight predefined server roles that are available, as shown in the following table.

| **Server role** | **Description** |
| --- | --- |
| **Front-end** | Service applications, services, and components that serve user requests belong on front-end web servers. These servers are optimized for low latency. |
| **Application** | Service applications, services, and components that serve back-end requests, such as background jobs or search crawl requests, belong on Application servers. These servers are optimized for high throughput. |
| **Distributed Cache** | Service applications, services, and components that are required for a distributed cache belong on Distributed Cache servers. |
| **Search** | Service applications, services, and components that are required for search belong on Search servers. |
| **Custom** | Custom service applications, services, and components that don't integrate with MinRole belong on Custom servers. The farm administrator has full control over which service instances can run on servers assigned to the Custom role. MinRole doesn't control which service instances are provisioned on this role. |
| **Single-Server Farm** | Service applications, services, and components required for a single-machine farm belong on a Single-Server Farm. A Single-Server Farm is meant for development, testing, and very limited production use. A SharePoint farm with the Single-Server Farm role can't have more than one SharePoint server in the farm.  
 **Important:** 
 The Standalone Install mode is no longer available in SharePoint Server 2016. The Single-Server Farm role replaces the Standalone Install mode available in previous SharePoint Server releases. Unlike Standalone Install, the SharePoint admin must separately install and prepare Microsoft SQL Server for SharePoint. The SharePoint admin must also configure the SharePoint farm services and web applications, either manually or by running the Farm Configuration Wizard. |
| **Front-end with Distributed Cache** | Shared role that combines the Front-end and Distributed Cache roles on the same server.  
 **Note:** 
 This shared role was introduced in the November Public Update for SharePoint Server 2016 (Feature Pack 1). |
| **Application with Search** | Shared role that combines the Application and Search roles on the same server.  
 **Note:** 
 This shared role was introduced in the November Public Update for SharePoint Server 2016 (Feature Pack 1). |

For more info about the MinRole feature, see Overview of MinRole Server Roles in SharePoint Server 2016 and Planning for a MinRole server deployment in SharePoint Server 2016.

Mobile experience

### Mobile experience

When you use a mobile device to access the home page for a SharePoint Server 2016 team site, you can tap tiles or links on the screen to navigate the site. You can also switch from the mobile view to PC view, which displays site pages as they're seen on a client computer. This view is also touch enabled.

New controls for working with OneDrive

### New controls for working with OneDrive

You can select a control to create new Office documents, upload files, synchronize your files for offline use, and share your files. For more info, see Get started creating, managing, and sharing files in OneDrive and SharePoint.

Open Document Format (ODF) available for document libraries

### Open Document Format (ODF) available for document libraries

The Open Document Format (ODF) lets you create new files in a document library and save as ODF files so that users can edit the new file with a program they choose. For more info, see Set Open Document Format (ODF) as the default file template for a library.

Project Server 2016

### Project Server 2016

Project Server 2016 for SharePoint Server 2016 has many new capabilities and features, including:

**Resource Engagements**: Now project managers can request needed resources from resource managers to complete their projects. Also, resource managers can use the new heat map functionality to see where resources are spending their time.

**Multiple Timelines**: Project and Portfolio managers can now create richer timelines that display multiple timelines in a single view.

**Simpler administration**: Project Server now has multitenant storage capabilities and has combined data storage with SharePoint. This greatly reduces IT overhead by eliminating the dedicated Project Server database and improves backup and restore capabilities.

**Cloud grade performance and scale**: Many performance and scalability improvements that have been added to Project Online have also been added to Project Server 2016.

For more info, see What's new for IT pros in Project Server 2016 Preview.

Important

Project Server 2016 is installed with SharePoint Server 2016 Enterprise, though is licensed separately. For more info about Project Server licensing, see Licensing Project.

Power Pivot add-in and Power View are now available to use with SharePoint Server 2016

### Power Pivot add-in and Power View are now available to use with SharePoint Server 2016

SQL Server 2016 CTP 3.1 is now available. You can now download SQL Server 2016 CTP 3.1 to use the Power Pivot for SharePoint add-in. You can also use Power View by installing SQL Server Reporting Services (SSRS) in SharePoint-integrated mode and the SSRS front-end add-in from the SQL Server installation media.

Download SQL Server 2016 CTP 3.1 from Microsoft Download Center.

The following SharePoint Server 2016 business intelligence features are available when you upgrade to SQL Server 2016 CTP 3.1:

Power Pivot Gallery

Scheduled Data Refresh

Workbooks as a Data Source

Power Pivot Management Dashboard

Power View reports

Power View Subscriptions

Report Alerting

For more info, download the new Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016 white paper. For details about configuring and deploying business intelligence in a multiple server SharePoint Server 2016 farm, download Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm.

Request Manager service improvements

### Request Manager service improvements

SharePoint Request Manager now provisions on the server roles shown in the following list, to support both throttling and routing scenarios:

Application

Distributed Cache

Front-End

Additionally, the Request Manager service will no longer prevent sites from rendering when the service is enabled while you have no routing rules defined.

Sharing

### Sharing

The following list shows the sharing improvements that are available for SharePoint Server 2016:

Create and Share folder

Sharing Hint

See who the folder is shared with when viewing a folder

Members can share

Improved invitation mail

One-click email to approve or deny a request for access

Recently Shared Items cache, see Enable the Recently Shared Items (RSI) cache to quickly populate the Shared with Me view.

SharePoint Search Service application

### SharePoint Search Service application

SharePoint Search supports indexing of up to 500 million items per Search Server application. For more info, see Overview of search architecture in SharePoint Server. For info about SharePoint cloud hybrid search, see Learn about cloud hybrid search for SharePoint.

Simplified SSL configuration for Central Administration site

### Simplified SSL configuration for Central Administration site

We've simplified the process for configuring Central Administration to use SSL bindings. The following command parameters are now available to use:

`New-SPCentralAdministration -Port <number> -SecureSocketsLayer`

`Set-SPCentralAdministration -Port <number> -SecureSocketsLayer`

`Psconfig.exe -cmd adminvs -port <number> -ssl`

You must assign a server certificate to the Central Administration IIS web site by using the IIS administration tools. The Central Administration web application won't be accessible until you do this.

If you specify port 443, it will automatically create an SSL binding instead of an HTTP binding even if you don't include the **SecureSocketsLayer** or **SSL** parameters.

The Central Administration public AAM URL is automatically updated to use the appropriate protocol scheme, server name, and port number.

Site collection upgrades

### Site collection upgrades

There are three options available for upgrading site collections. For more info, see Upgrade a site collection to SharePoint Server 2016.

SMTP connection encryption

### SMTP connection encryption

The following list shows the SharePoint 2016 requirements that are needed to negotiate connection encryption with an SMTP server:

STARTTLS must be enabled on the SMTP server.

The SMTP server must support the TLS 1.0, TLS 1.1, or TLS 1.2 protocol.

Important

SSL 2.0 and SSL 3.0 protocols are not supported.

The SMTP server must have a server certificate installed.

The server certificate must be valid. Typically, this means that the name of the server certificate must match the name of the SMTP server provided to SharePoint. The server certificate must also be issued by a certificate authority that is trusted by the SharePoint server.

SharePoint must be configured to use SMTP connection encryption.

To configure SharePoint to always use SMTP connection encryption, open the SharePoint Central Administration website and browse to **System Settings** > **Configure outgoing e-mail settings** and set the **Use TLS connection encryption** drop-down menu to **Yes**. To configure SharePoint to always use SMTP connection encryption in Microsoft PowerShell, use the  `Set-SPWebApplication` cmdlet without the **DisableSMTPEncryption** parameter. For example:

```
$WebApp = Get-SPWebApplication -IncludeCentralAdministration | ? { $_.IsAdministrationWebApplication -eq $true }
Set-SPWebApplication -Identity $WebApp -SMTPServer smtp.internal.contoso.com -OutgoingEmailAddress sharepoint@contoso.com -ReplyToEmailAddress sharepoint@contoso.com
```

To configure SharePoint to never use SMTP connection encryption in SharePoint Central Administration, browse to **System Settings** > **Configure outgoing email settings** and set the **Use TLS connection encryption** drop-down menu to **No**. To configure SharePoint to never use SMTP connection encryption in PowerShell, use the  `Set-SPWebApplication` cmdlet with the **DisableSMTPEncryption** parameter. For example:

```
$WebApp = Get-SPWebApplication -IncludeCentralAdministration | ? { $_.IsAdministrationWebApplication -eq $true }
Set-SPWebApplication -Identity $WebApp -SMTPServer smtp.internal.contoso.com -DisableSMTPEncryption -OutgoingEmailAddress sharepoint@contoso.com -ReplyToEmailAddress 
sharepoint@contoso.com
```

Note

If SharePoint is configured to use SMTP connection encryption, it will only send email messages if it successfully negotiates connection encryption with the SMTP server. It will not fall back and send email messages unencrypted if connection encryption negotiation fails. If SharePoint is not configured to use SMTP connection encryption, it will always send email messages unencrypted, even if the SMTP server supports connection encryption. > Using SMTP connection encryption does not enable SMTP authentication. SMTP requests are always sent anonymously.

Site folders view

### Site folders view

For more info, see Change views on the OneDrive website.

Sites page pinning

### Sites page pinning

You can now pin sites that you see on the sites page. A pinned site shows at the top of the list of sites that you're following.

Apply themes to your Suite Navigation

### Apply themes to your Suite Navigation

You can now apply themes to your Suite Navigation.

Use SMTP ports other than the default (25)

### Use SMTP ports other than the default (25)

To configure SharePoint to use a nondefault SMTP port open SharePoint Central Administration, browse to **System Settings** > **Configure outgoing email settings**, and set the **SMTP server port** to the port number of your SMTP server. To configure SharePoint to use a nondefault SMTP port in PowerShell, use the  `Set-SPWebApplication` cmdlet with the **SMTPServerPort** <port number> parameter. For example:

```
$WebApp = Get-SPWebApplication -IncludeCentralAdministration | ? { $_.IsAdministrationWebApplication -eq $true }
Set-SPWebApplication -Identity $WebApp -SMTPServer smtp.internal.contoso.com -SMTPServerPort 587 -OutgoingEmailAddress sharepoint@contoso.com -ReplyToEmailAddress 
sh  arepoint@contoso.com
```

Related articles

## Related articles

What is SharePoint?

Additional resources

## Additional resources

- Last updated on 
		2024-12-02
