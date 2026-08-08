---
title: "New and improved features in SharePoint Server Subscription Edition - SharePoint Server"
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition."
ms.topic: overview
---
Note

New and improved features in SharePoint Server Subscription Edition

# New and improved features in SharePoint Server Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Learn about the new features and updates to existing features that were introduced during the initial release of SharePoint Server Subscription Edition.

For information on new and updated features that were introduced after the initial release of SharePoint Server Subscription Edition, see SharePoint Server Subscription Edition Version 22H2 and SharePoint Server Subscription Edition Version 23H1.

List of new features and updates to existing features

## List of new features and updates to existing features

The following table provides the list of new features and updates to existing features, introduced during the initial release of SharePoint Server Subscription Edition.

- Support for OpenID Connect (OIDC) 1.0

- Enhanced People Picker for modern authentication

- Improved Integrated Windows authentication over TLS

- For more information, see OpenID Connect (OIDC) 1.0 authentication.

- For more information, see Enhanced People Picker for modern authentication.

- For more information, see Reduced Integrated Windows authentication latency over TLS.

- Support for Windows Server 2022

- Support for Windows Server Core

- Support for "N - 2" upgrade from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)

- AppFabric Cache integration

- For more information, see Windows Server 2022.

- For more information, see Windows Server Core.

- For more information, see Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019).

- For more information, see AppFabric Cache integration.

- Support for host header bindings on Central Administration web application

- Support for Server Name Indication (SNI) for host header bindings

- Support for changing web application bindings

- Easier AAM configuration for Central Administration

- Federated service applications support "N - 2" consuming farms (SharePoint 2016, 2019, and Subscription Edition)

- Support for client certificate authentication to SMTP servers

- For more information, see Central Administration now supports host header bindings.

- For more information, see Server Name Indication.

- For more information, see Change web application IIS bindings.

- For more information, see Easier AAM configuration for Central Administration.

- For more information, see Federated service applications support "N - 2" consuming farms (SharePoint 2016, 2019, and Subscription Edition).

- For more information, see Client certificate authentication to SMTP servers.

- Certificate notification contacts haven't been configured

- Upcoming SSL certificate expirations

- SSL certificates are about to expire

- SSL certificates have expired

- For more information, see Certificate notification contacts haven't been configured.

- For more information, see Upcoming SSL certificate expirations.

- For more information, see SSL certificates are about to expire.

- For more information, see SSL certificates have expired.

- Better integration with Power Apps and Power Automate

- Improved hybrid search troubleshooting

- For more information, see Power Apps and Power Automate integration.

- For more information, see Improved hybrid search troubleshooting.

- SharePoint PowerShell cmdlets converted from snap-in to module

- SharePoint Management Shell warns when not running as an elevated administrator

- Distributed Cache cmdlets

- New-SPWebApplication creates web applications in Windows claims mode by default

- New People Picker cmdlets

- Remove-SPConfigurationObject cmdlet

- SharePoint Volume Shadow Copy Service writer cmdlets

- For more information, see SharePoint PowerShell cmdlets converted from snap-in to module.

- For more information, see SharePoint Management Shell warns when not running as an elevated administrator.

- For more information, see Distributed Cache cmdlets.

- For more information, see New-SPWebApplication PowerShell cmdlet.

- For more information, see New People Picker cmdlets

- For more information, see Introducing Remove-SPConfigurationObject PowerShell cmdlet.

- For more information, see SharePoint Volume Shadow Copy Service writer cmdlets.

- Search result page modernization

- Support for returning list content in modern results page

- Thumbnails in modern search result page

- For more information, see Search result page modernization.

- For more information, see Support for returning list content in modern results page.

- For more information, see Thumbnails in modern search result page.

- SSL certificate management

- Support for TLS 1.3

- Strong TLS encryption by default

- Improved ASP.NET view state security and key management

- For more information, see SSL certificate management.

- For more information, see TLS 1.3.

- For more information, see Strong TLS encryption by default.

- For more information, see Improved ASP.NET view state security and key management.

- Accessibility improvements

- Brick layout for document library thumbnails and image gallery web part

- Bulk check-in and check-out

- Bulk file download from document libraries and OneDrive personal sites

- Image and document thumbnails in document libraries and picture libraries

- Modern list and library web parts support adding, editing, and deleting content

- Modern document sets

- For more information, see Accessibility improvements across modern UX.

- For more information, see Brick layout for document library thumbnails and image gallery web part.

- For more information, see Bulk check-in/check-out in modern Document library experience.

- For more information, see Bulk file download from document libraries and OneDrive personal sites.

- For more information, see Image and document thumbnails in document libraries and picture libraries.

- For more information, see Modern list and library web parts support adding, editing, and deleting content.

- For more information, see Modern document sets.

- New BLOB storage provider: Remote Share Provider

- Remote Share Provider diagnostic tool

- For more information, see Remote Share Provider.

- For more information, see Remote Share Provider diagnostic tool.

| **Feature Group** | **Features** | **More info** |
| --- | --- | --- |
| Authentication and Identity Management |  |  |
| Deployment and Upgrade |  |  |
| Farm Administration |  |  |
| Health and Monitoring |  |  |
| Hybrid |  |  |
| PowerShell |  |  |
| Search |  |  |
| Security |  |  |
| Sites, Lists, and Libraries |  |  |
| Storage |  |  |

Detailed description of features

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition.

Authentication and Identity Management

## Authentication and Identity Management

OpenID Connect (OIDC) 1.0 authentication

### OpenID Connect (OIDC) 1.0 authentication

SharePoint Server Subscription Edition adds support for the OpenID Connect (OIDC) 1.0 authentication protocol. OIDC is a modern authentication protocol that makes it easy to integrate applications and devices with your organization's identity and authentication management solutions to better meet your evolving security and compliance needs. For example, organizations can enforce authentication policies such as multifactor authentication (MFA), conditional access policies based on device compliance, and more.

SharePoint Server Subscription Edition supports OIDC authentication with identity providers such as Microsoft Entra ID, Active Directory Federation Services (AD FS) 2016 or higher, and third-party identity providers that implement the OIDC 1.0 protocol.

To set up OIDC authentication in SharePoint Server, see OpenID Connect 1.0 authentication.

Enhanced People Picker for modern authentication

### Enhanced People Picker for modern authentication

When modern authentication (a trusted identity provider) such as SAML 1.1 or OIDC 1.0 is used, the People Picker control can't search, resolve, and validate users and groups without writing a custom claim provider through C#.

In SharePoint Server Subscription Edition, the People Picker has been enhanced to allow resolving users and groups based on their profiles in the User Profile Application (UPA). UPA must be configured to synchronize users and groups from the trusted identity provider membership store. This allows the People Picker to only resolve valid users and groups without requiring a custom claims provider.

To configure People Picker, see Enhanced People Picker for modern authentication.

Reduced Integrated Windows authentication latency over TLS

### Reduced Integrated Windows authentication latency over TLS

Internet Information Services (IIS) 10 advertises support for HTTP/2 during TLS negotiation, letting the client know that it can use HTTP/2 once the Transport Layer Security (TLS) connection is complete. However, HTTP/2 and above are not compatible with Integrated Windows authentication protocols such as Negotiate (Kerberos) and New Technology LAN Manager (NTLM).

If a server detects that a client is attempting to perform Kerberos or NTLM authentication over an HTTP/2 or HTTP/3 connection, it will notify the client to downgrade the connection to HTTP/1.1 and restart the attempt. This results in extra round trips between the client and the server during authentication, which increases latency.

SharePoint Server Subscription Edition reduces this authentication latency by disabling HTTP/2 and Quick UDP Internet Connections (QUIC) in SharePoint IIS web sites when Negotiate (Kerberos) or NTLM are enabled. HTTP/2 and QUIC will continue to be available on SharePoint IIS web sites that aren't configured to use Negotiate (Kerberos) or NTLM.

Deployment and Upgrade

## Deployment and Upgrade

Windows Server 2022

### Windows Server 2022

Windows Server 2022 includes multiple new features and improvements in security, virtualization, networking, and more, such as:

**Security**

Secured-core server provides advanced protection against increasingly sophisticated attacks through hardware root-of-trust, firmware protection, and virtualization-based security. Network security is strengthened through the support of TLS 1.3, DNS-over-HTTPS (DoH), and stronger SMB file share encryption.

**Networking**

Performance improvements in both TCP and UDP networking maximize bandwidth, minimize packet loss, and reduce CPU load. In addition, SMB compression allows files to be compressed as they're transferred over the network for faster file transfers.

**Virtualization**

Performance improvements in the Hyper-V virtual switch reduces the CPU load of virtual machine network communication. Nested virtualization support has also been added for AMD processors.

For more information about Windows Server 2022, see What's new in Windows Server 2022.

SharePoint Server Subscription Edition supports additional security features when deployed with Windows Server 2022 such as support for TLS 1.3 and strong TLS encryption by default.

Note

These security features are not available when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

Windows Server Core

### Windows Server Core

Windows Server Core is a leaner Windows Server deployment type compared to the classic Windows Server with Desktop Experience. Server Core minimizes the number of OS features and services that are installed and running to only those that are essential for a server. This reduces the demand on system resources (CPU, RAM, and disk space) and the potential attack surface for security vulnerabilities.

SharePoint Server Subscription Edition adds support for the Windows Server Core deployment type with both Windows Server 2019 and Windows Server 2022. The Windows Server Desktop Experience deployment type remains supported with both Windows Server 2019 and Windows Server 2022.

For more information about Windows Server Core, see What is the Server Core installation option in Windows Server. For guidance on installing SharePoint Server Subscription Edition on Windows Server Core, see Installing SharePoint Server Subscription Edition on Windows Server Core.

Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)

### Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)

SharePoint Server Subscription Edition supports both **N - 1** and **N - 2** version-to-version upgrade. You can upgrade directly from the following SharePoint products using the standard database attach upgrade procedure:

SharePoint Server 2019 (including Project Server 2019)

SharePoint Server 2016 (including Project Server 2016)

Note

Directly upgrading from versions of SharePoint earlier than SharePoint Server 2016 via database attach is not supported. SharePoint 2013, SharePoint 2010, and so on must first be upgraded to either SharePoint Server 2016 or SharePoint Server 2019 via database attach before upgrading to SharePoint Server Subscription Edition.

For more information:

To install SharePoint Server Subscription Edition, see Installation overview for SharePoint Server Subscription Edition.

To upgrade to SharePoint Server Subscription Edition, see Upgrade to SharePoint Server Subscription Edition.

AppFabric Cache integration

### AppFabric Cache integration

In previous versions of SharePoint Server, the Distributed Cache feature relied on Windows Server AppFabric, which was a separately installed component. Starting with SharePoint Server Subscription Edition, the AppFabric caching technology has been directly integrated into the Distributed Cache feature. Distributed Cache no longer relies on the external Windows Server AppFabric component and it will no longer be installed by the Microsoft SharePoint Products Preparation Tool.

Farm Administration

## Farm Administration

Central Administration now supports host header bindings

### Central Administration now supports host header bindings

You can now configure the SharePoint Central Administration website to use a host header binding, which will allow it to share the same TCP port number as other websites. This would typically be used to let the SharePoint Central Administration site and your content website to be hosted on the same TCP port, such as port 443 for SSL.

To configure this, specify the host header binding with the `-HostHeader` parameter of the `New-SPCentralAdministration` and `Set-SPCentralAdministration` cmdlets, or with the `-hostheader` parameter of the `psconfig.exe -cmd adminvs` command.

Server Name Indication (SNI)

### Server Name Indication (SNI)

Server Name Indication (SNI) allows multiple IIS websites with unique host headers and unique server certificates to share the same Secure Sockets Layer (SSL) port. The server examines the server name specified by the client during the SSL handshake to determine which server certificate should be used to complete the connection. Your IIS website must have a host header and must use SSL to use Server Name Indication. If Server Name Indication isn't used, all IIS websites sharing the same SSL port will share the same server certificate.

Server Name Indication can be configured by the **Use Server Name Indication** setting on the **Create New Web Application** and **Extend Web Application** pages in SharePoint Central Administration.

It can also be configured by the following commands:

`psconfig.exe -adminvs -port <port number> -hostheader <host header> -ssl -usesni`

`New-SPCentralAdministration -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`

`Set-SPCentralAdministration -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`

`New-SPWebApplication ... -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`

`Set-SPWebApplication ... -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`

`New-SPWebApplicationExtension ... -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`

Change web application IIS bindings

### Change web application IIS bindings

In previous versions of SharePoint, it was difficult to change the IIS bindings of your SharePoint web application once it was created. You could try to remove a web application from a zone and then re-extend it to the zone with updated bindings, but this was a time consuming operation and risked potentially losing customizations in that IIS web site. Or you could manually edit the bindings of the IIS web site itself, but SharePoint would be unaware of such manual changes, so you risked SharePoint overwriting those bindings at any time.

You can now easily change your web application IIS bindings through PowerShell or Central Administration without having to first delete and then recreate your web applications. This functionality is supported in all web application zones.

For more information, see Update a web application URL and IIS bindings for SharePoint Server Subscription Edition.

Easier AAM configuration for Central Administration

### Easier AAM configuration for Central Administration

You can now specify the public AAM URL directly in the Central Administration command-line tools, bringing them to parity with the content web application command-line tools.  This can be specified via the optional `-Url <String>` parameter in the following PowerShell cmdlets and `PSConfig.exe` command-line utility:

`New-SPCentralAdministration`

`Set-SPCentralAdministration`

`PSConfig.exe -cmd adminvs`

Federated service applications support "N - 2" consuming farms (SharePoint 2016, 2019, and Subscription Edition)

### Federated service applications support "N - 2" consuming farms (SharePoint 2016, 2019, and Subscription Edition)

In SharePoint Server, some service applications can be shared across server farms. Microsoft supports service applications published by a SharePoint Server Subscription Edition farm being consumed by the following versions of SharePoint Server:

SharePoint Server Subscription Edition (N)

SharePoint Server 2019 (N - 1)

SharePoint Server 2016 (N - 2)

For more information, see Share service applications across farms in SharePoint Server.

Client certificate authentication to SMTP servers

### Client certificate authentication to SMTP servers

You can now authenticate to Simple Mail Transfer Protocol (SMTP) servers using client certificates. This is typically used for more advanced security configurations where password-based authentication isn't sufficient.

For more information, see Plan outgoing email for a SharePoint Server farm.

Health and Monitoring

## Health and Monitoring

The following Health Analyzer rules have been added:

Certificate notification contacts haven't been configured

### Certificate notification contacts haven't been configured

This health rule runs weekly to provide notifications through Central Administration when certificates are in use and no certificate notification contacts have been configured.

Upcoming SSL certificate expirations

### Upcoming SSL certificate expirations

This health rule runs weekly to provide advanced notification through both Central Administration and email of upcoming certificate expirations.

SSL certificates are about to expire

### SSL certificates are about to expire

This health rule runs daily to provide advanced notification through both Central Administration and email when certificates are about to expire.

SSL certificates have expired

### SSL certificates have expired

This health rule runs daily to provide notification through both Central Administration and email when certificates have expired.

Hybrid

## Hybrid

Power Apps and Power Automate integration

### Power Apps and Power Automate integration

Two new commands will be available in the modern document library page and modern list page command bar when a SharePoint Server Subscription Edition farm is connected to a Microsoft 365 tenant through hybrid:

Power Apps

Power Automate

These commands will take you directly to the Power Apps and Power Automate service pages.

Improved hybrid search troubleshooting

### Improved hybrid search troubleshooting

There are two improvements added to Search Crawler Log in Center Admin user experience:

A new column called **online ID** is introduced to crawler log for all contents when SharePoint Farm is configured with cloud hybrid search (cloud SSA). This **online ID** is SharePoint online search index for On-Premises contents in SharePoint Server.

A new **Warning breakdown** pivot is added next to the **Error breakdown** pivot in the crawler log page. It provides the ability for administrators to examine search crawler warnings with the same user experience as the **Error breakdown** pivot by listing all of the warnings in the crawler log.

PowerShell

## PowerShell

SharePoint PowerShell cmdlets converted from snap-in to module

### SharePoint PowerShell cmdlets converted from snap-in to module

SharePoint Server PowerShell cmdlets are now installed via a PowerShell module instead of a PowerShell snap-in. This follows the recommended packaging approach from PowerShell and allows us to better support the PowerShell experience.

It includes the following benefits:

SharePoint Server cmdlets are now automatically available in all Windows PowerShell consoles.  You don't have to launch the SharePoint Management Shell or use the `Add-PSSnapin` cmdlet to access the SharePoint Server cmdlets.

PowerShell will be able to download updated SharePoint Server cmdlet help content over the Internet.

Note

The SharePoint Management Shell will continue to be included in the product to provide a familiar PowerShell UI for managing SharePoint Server. The SharePoint Server PowerShell cmdlets will continue to require Windows PowerShell. These cmdlets will not be compatible with PowerShell Core 6.x or PowerShell 7.x.

SharePoint Management Shell warns when not running as an elevated administrator

### SharePoint Management Shell warns when not running as an elevated administrator

Some SharePoint PowerShell cmdlets require the user to be an elevated administrator to run successfully. However, the Windows User Account Control feature can block a user's elevated administrator token unless PowerShell is launched with the "Run as Administrator" option. To prevent confusion about whether you're running as an elevated administrator, the SharePoint Management Shell will now notify users if they're not running as an elevated administrator when it's first launched.

Distributed Cache cmdlets

### Distributed Cache cmdlets

The following SharePoint cmdlets have been added to help manage Distributed Cache in SharePoint Server Subscription Edition. These cmdlets are equivalent to the direct Distributed Cache cmdlets that were available in the standalone AppFabric Distributed Cache product used with previous versions of SharePoint Server.

`New-SPCache`: Creates a new named cache.

`Get-SPCache`: Gets the cache information from the cache cluster.

`Get-SPCacheStatistics`: Gets the name cache state.

`Get-SPCacheHost`: Gets the cache host information from the cache cluster.

`Start-SPCacheCluster`: Starts the Caching Service on all cache hosts in the cluster.

`Stop-SPCacheCluster`: Stops the Caching Service on all cache hosts in the cluster.

`Import-SPCacheClusterConfig -Path <String>`: Imports the cache cluster configuration details from an XML file.

`Export-SPCacheClusterConfig -Path <String>`: Export cache cluster configuration details to an XML file.

`Get-SPCacheClusterHealth`: Returns statistics for all of the named caches in the cache cluster.

The `Stop-SPDistributedCacheServiceInstance` cmdlet is improved to better support graceful shutdowns. You can specify the `-Graceful` switch parameter with the cmdlet to ensure that the cached data in a Distributed Cache service instance is transferred to another Distributed Cache service instance before the first service instance shuts down.

You can specify the time limit for a graceful shutdown data transfer to complete via the `-Timeout` parameter.  If the `-Timeout` parameter isn't specified, the default is 900 seconds (5 minutes). You can also specify the `-Force` switch parameter to force a Distributed Cache service instance to shut down, even if it isn't able to complete a graceful shutdown before it times out.

New-SPWebApplication PowerShell cmdlet

### New-SPWebApplication PowerShell cmdlet

In previous versions of SharePoint, you had to specify the `AuthenticationProvider` parameter in the `New-SPWebApplication` and `New-SPWebApplicationExtension` PowerShell cmdlets to create web applications using Windows Claims authentication. If you didn't, the web application would have been created in the Windows Classic authentication mode and you would have received a warning.

As the Windows Classic authentication mode is no longer supported, the behaviors of these PowerShell cmdlets have changed when you don't specify the `AuthenticationProvider` parameter. In SharePoint Server Subscription Edition, the PowerShell cmdlet creates web applications in Windows claims mode by default and the warning message will no longer be displayed. The Central Administration web application will continue to use Windows Classic authentication.

New People Picker cmdlets

### New People Picker cmdlets

We've added the following PowerShell cmdlets to configure the People Picker and replace the `stsadm.exe` commands described in Configure People Picker (SharePoint Server 2010).

`Get-SPPeoplePickerConfig`: Gets People Picker settings of a specified Web application.

`Set-SPPeoplePickerConfig`: Configures People Picker settings of a specified Web application.

`Add-SPPeoplePickerSearchADDomain`: Adds a forest or domain to the list that the People Picker uses when searching for users.

`Clear-SPPeoplePickerSearchADDomain`: Clears the list of People Picker search forests and domains for a specified Web application.

`Get-SPPeoplePickerSearchADDomain`: Returns all Active Directory forests or domains that the People Picker uses when searching for users.

`Remove-SPPeoplePickerSearchADDomain`: Removes a forest of domain from the list that the People Picker uses when searching for users.

`Add-SPPeoplePickerDistributionListSearchDomain`: Adds a domain to the People Picker distribution list search domains.

`Clear-SPPeoplePickerDistributionListSearchDomain`: Clears the list of People Picker distribution list search domains.

`Get-SPPeoplePickerDistributionListSearchDomain`: Returns all domains in the People Picker distribution list search domains.

`Remove-SPPeoplePickerDistributionListSearchDomain`: Removes a domain from the People Picker distribution list search domains.

`Add-SPPeoplePickerServiceAccountDirectoryPath`: Adds an OU to People Picker service account directory path list.

`Clear-SPPeoplePickerServiceAccountDirectoryPath`: Clears the OUs of People Picker service account directory path list.

`Remove-SPPeoplePickerServiceAccountDirectoryPath`: Removes an OU from People Picker service account directory path list.

Introducing Remove-SPConfigurationObject PowerShell cmdlet

### Introducing Remove-SPConfigurationObject PowerShell cmdlet

The `Remove-SPConfigurationObject` PowerShell cmdlet replaces the `stsadm.exe -o deleteconfigurationobject` command.

Its parameters are:

`[-Identity] <guid>`: The GUID of the object in the SharePoint configuration database to delete.

`[-Force]`: Specifies that the object will be deleted without confirmation that you want to proceed. This can be used for scripts that don't support interactive confirmation prompts.

Warning

Improper usage of this cmdlet has the potential to destroy necessary data in a SharePoint configuration database, requiring a complete rebuild of the SharePoint farm. Use it only under guidance with Microsoft Support.

SharePoint Volume Shadow Copy Service writer cmdlets

### SharePoint Volume Shadow Copy Service writer cmdlets

To improve the management of the SharePoint Volume Shadow Copy Service (VSS) writer, the following new PowerShell cmdlets are introduced:

`Register-SPVssWriter`: Registers the SharePoint VSS Writer service on the local server.

`Unregister-SPVssWriter`: Unregisters the SharePoint VSS Writer service on the local server.

These cmdlets perform the same actions as the stsadm.exe -o registerwsswriter and stsadm.exe -o unregisterwsswriter commands.

Search

## Search

Search result page modernization

### Search result page modernization

We're bringing modern experiences from SharePoint in Microsoft 365 to the search result page in SharePoint Server Subscription Edition to make it more compelling, flexible, and easier to use. This will provide a closer look and feel to Microsoft 365.

The following features have been modernized and introduced into this release:

Centralized search bar.

Content type filters including **All**, **Files**, **Sites**, and **News**. **All** is introduced to have the results of **Files**, **Sites**, and **News**.

Duration filter to filter content by time scope.

Support for returning list content in modern results page

### Support for returning list content in modern results page

Lists and list items are now searchable in the modern UX. List item results will be included in the **All** category of the modern search result page.

Thumbnails in modern search result page

### Thumbnails in modern search result page

The modern search result page will now show thumbnails for popular document and image file types such as PDF, Word, PowerPoint, PNG, JPEG, GIF, and more.

Security

## Security

SSL certificate management

### SSL certificate management

SharePoint farm administrators can now directly manage the deployment and lifecycle of SSL/TLS certificates in their SharePoint Server farms.  SharePoint certificate management is built on top of Cryptography API: Next Generation, a modern and flexible infrastructure that supports both Elliptic Curve Cryptography (ECC) and classic RSA certificates.

Certificate management capabilities include:

Generating new and renewal certificate signing requests (CSRs) to submit to certificate authorities.

Importing and exporting certificates, with or without private keys.

Viewing certificate properties.

Automatically deploying and retracting certificates to each server in their SharePoint farm.

Assigning and unassigning certificates to web applications.

Automated scanning and notification of certificates that will soon expire or have already expired based on thresholds that can be configured by farm administrators.

Certificates can be fully managed through PowerShell cmdlets and Central Administration.

Administrative logging of all certificate management operations for auditing purposes.

Public APIs allow external tools to integrate with SharePoint certificate management.

TLS 1.3

### TLS 1.3

Transport Layer Security (TLS) is a cryptographic protocol that encrypts communication between two endpoints, such as between a web browser and an HTTPS web site. TLS 1.3 is the latest and most secure version of the TLS protocol.

SharePoint Server Subscription Edition supports TLS 1.3 by default when deployed with Windows Server 2022 or higher.

Note

TLS 1.3 is not available and is not supported when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

Note

Not all applications in your software ecosystem may support TLS 1.3. Check with your software vendors to determine if your other applications support TLS 1.3. SharePoint Server Subscription Edition can fall back to earlier TLS protocol versions when connecting with systems that don't support TLS 1.3 unless the customer has disabled earlier TLS protocol versions.

For more information, see TLS 1.3 Support.

Strong TLS encryption by default

### Strong TLS encryption by default

SharePoint Server Subscription Edition will use the advanced security capabilities of Windows Server 2022 to ensure that TLS connections made to your SharePoint sites only use the strongest encryption by default. SharePoint Server will configure itself to enforce the following minimum TLS version and cipher suite requirements on its SSL bindings:

The SSL/TLS protocol version negotiated must be TLS 1.2 or higher.

The TLS cipher suite negotiated must support forward secrecy and AEAD encryption modes such as GCM.

Customers can allow legacy encryption to be used if needed for backward compatibility with older software that doesn't support strong TLS protocol versions and cipher suites.

Note

Strong TLS encryption by default is not available when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

For more information, see Strong TLS Encryption.

Improved ASP.NET view state security and key management

### Improved ASP.NET view state security and key management

SharePoint now encrypts the `machineKey` section of its `web.config` files by default. This prevents attackers from reading your ASP.NET view state encryption and validation keys even if they gain access to those `web.config` files.

Farm administrators can also change the ASP.NET view state decryption and validation keys of a SharePoint web application through the new `Set-SPMachineKey` and `Update-SPMachineKey` PowerShell cmdlets. This allows you to rotate those keys in your farm.

Sites, Lists, and Libraries

## Sites, Lists, and Libraries

Accessibility improvements across modern UX

### Accessibility improvements across modern UX

SharePoint Server Subscription Edition includes numerous accessibility improvements across the modern UX to ensure that all users can be productive with SharePoint.

Brick layout for document library thumbnails and image gallery web part

### Brick layout for document library thumbnails and image gallery web part

SharePoint Server Subscription Edition introduces the Brick layout as a layout option in modern document libraries and the image gallery web part. The Brick layout displays several images of various sizes, automatically arranged in a pattern similar to a brick wall. The Brick layout respects the aspect ratio of all images shown, including 16:9, 4:3, 1:1, and so on.

Bulk check-in/check-out in modern document library experience

### Bulk check-in/check-out in modern document library experience

Checking out a file from a document library allows you to make changes to a file while preventing others from making changes to that file. Once you're done making changes to the file, checking it in to the document library will allow others to see your changes.

With bulk check-out and check-in, you can now select multiple files and perform the check-out and check-in operations on all of them at the same time. This saves you time by avoiding repetitive steps.

Bulk download files from document library and OneDrive personal sites

### Bulk download files from document library and OneDrive personal sites

SharePoint Server Subscription Edition now supports downloading multiple files at once from document libraries and OneDrive personal sites. Once you select multiple files and folders and then click **Download** in the command bar, SharePoint will compress the selected files and folders into a ZIP file and then download the ZIP file to the user.

The following limitations apply to  the bulk download feature:

Each single file can't exceed 10 GB.

Total size of all the selected files can't exceed 20 GB.

Maximum level of folders is limited to 100 levels.

No more than 10,000 files can be downloaded at once.

For more information about this feature, see Download files and folders from OneDrive or SharePoint.

Image and document thumbnails in document libraries and picture libraries

### Image and document thumbnails in document libraries and picture libraries

SharePoint Server Subscription Edition can render thumbnails of files in the Tiles view of document libraries, picture libraries, and OneDrive personal sites. SharePoint will render thumbnails of popular image file formats such as PNG, JPEG, GIF, and more. And if you've linked your SharePoint Server farm to an Office Online Server farm, SharePoint will also be able to render thumbnails of popular document formats such as PDFs, Word documents, PowerPoint documents, and Rich Text Files.

Modern list and library web parts support adding, editing, and deleting content

### Modern list and library web parts support adding, editing, and deleting content

In SharePoint Server 2019, modern document library web parts and modern list web parts provided a read-only experience to access documents and list items. Users couldn't add new content or edit existing content through these web parts and instead had to navigate to the document library or list to perform these actions.

SharePoint Server Subscription Edition adds the ability to perform the following actions directly in modern document library web parts and modern list web parts:

Document library web parts: create, upload, share, download, rename, delete, and edit documents and folders.

List web parts: create, edit, and delete list items.

Modern document sets

### Modern document sets

A Document Set is a group of related documents that you can manage as a single entity. In previous versions of SharePoint Server, document sets only supported the classic UX. Now in SharePoint Server Subscription Edition, Document Sets have been enhanced to support the modern experience in document libraries.

Storage

## Storage

Remote Share Provider

### Remote Share Provider

In SharePoint Server Subscription Edition, Remote Share Provider, a new RBS (Remote BLOB Storage) provider, is introduced to enable customer to offload BLOB storages from SQL server to low-cost remote Server Message Block (SMB) systems.

By using this new technology, customer can shift data storage from costly SQL server to low-cost SMB file storage. It can also increase the total size of the content in a content database by offloading BLOBs to a remote data storage system.

Remote Share Provider diagnostic tool

### Remote Share Provider diagnostic tool

To support the new Remote Share Provider, SharePoint Server Subscription Edition provides a new `Test-SPRemoteShareBlobStore` PowerShell cmdlet to validate the data consistency of content database that is remote share provider enabled. It provides an easy way for checking healthy of content database and remote storage, and for troubleshooting storage problem.

Related articles

## Related articles

Installation overview for SharePoint Server Subscription Edition

System requirements for SharePoint Server Subscription Edition

Upgrade to SharePoint Server Subscription Edition

Additional resources

## Additional resources

- Last updated on 
		2023-09-01
