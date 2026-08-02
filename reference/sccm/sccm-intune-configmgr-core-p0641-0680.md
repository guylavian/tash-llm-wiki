---
title: "Core infrastructure documentation — pages 641-680"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0641-0680
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0641-0680
family: sccm
documentKind: "doc"
abstract: "1. On the site server, browse to the Configuration Manager installation directory. In the \\bin\\<platform> subfolder, open the following file in a text editor: mobileclient.tcf 2. Locate the entry, SMSPublicRootKey . Copy the value from that line, and close the file without savin"
---

# Core infrastructure documentation — pages 641-680

<!-- p.641 -->

  1. On the site server, browse to the Configuration Manager installation directory. In
    the \bin\<platform> subfolder, open the following file in a text editor:
    mobileclient.tcf

  2. Locate the entry, SMSPublicRootKey . Copy the value from that line, and close the
    file without saving any changes.

  3. Create a new text file, and paste the key value that you copied from the
    mobileclient.tcf file.

  4. Save the file in a location where all computers can access it, but where the file is
    safe from tampering.

  5. Install the client by using any installation method that accepts client.msi properties.
    Specify the following property: SMSROOTKEYPATH=<full path and file name>

       ） Important

       When you specify the trusted root key during client installation, also specify
       the site code. Use the following client.msi property: SMSSITECODE=<site code>

Pre-provision a client with the trusted root key without
using a file
  1. On the site server, browse to the Configuration Manager installation directory. In
    the \bin\<platform> subfolder, open the following file in a text editor:
    mobileclient.tcf

  2. Locate the entry, SMSPublicRootKey . Copy the value from that line, and close the
    file without saving any changes.

  3. Install the client by using any installation method that accepts client.msi properties.
    Specify the following client.msi property: SMSPublicRootKey=<key> where <key> is
    the string that you copied from mobileclient.tcf.

       ） Important

       When you specify the trusted root key during client installation, also specify
       the site code. Use the following client.msi property: SMSSITECODE=<site code>

<!-- p.642 -->

Verify the trusted root key on a client
   1. Open a Windows PowerShell console as an administrator.

   2. Run the following command:

        PowerShell

        (Get-WmiObject -Namespace root\ccm\locationservices -Class
        TrustedRootKey).TrustedRootKey

The returned string is the trusted root key. Verify that it matches the SMSPublicRootKey
value in the mobileclient.tcf file on the site server.

Remove or replace the trusted root key
Remove the trusted root key from a client by using the client.msi property,
RESETKEYINFORMATION = TRUE .

To replace the trusted root key, reinstall the client together with the new trusted root
key. For example, use client push, or specify the client.msi property SMSPublicRootKey.

For more information on these installation properties, see About client installation
parameters and properties.

Signing and encryption
Configure the most secure signing and encryption settings for site systems that all
clients in the site can support. These settings are especially important when you let
clients communicate with site systems by using self-signed certificates over HTTP.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node. Select the primary site to
     configure.

   2. In the ribbon, select Properties, and then switch to the Signing and Encryption
     tab.

     This tab is available on a primary site only. If you don't see the Signing and
     Encryption tab, make sure that you're not connected to a central administration
     site or a secondary site.

<!-- p.643 -->

   3. Configure the signing and encryption options for clients to communicate with the
     site.

             Require signing: Clients sign data before sending to the management point.

             Require SHA-256: Clients use the SHA-256 algorithm when signing data.

               ２ Warning

               Don't Require SHA-256 without first confirming that all clients support
               this hash algorithm. These clients include ones that might be assigned to
               the site in the future.

               If you choose this option, and clients with self-signed certificates can't
               support SHA-256, Configuration Manager rejects them. The
               SMS_MP_CONTROL_MANAGER component logs the message ID 5443.

             Use encryption: Clients encrypt client inventory data and status messages
             before sending to the management point.

Repeat this procedure for all primary sites in the hierarchy.

Role-based administration
Role-based administration combines security roles, security scopes, and assigned
collections to define the administrative scope for each administrative user. A scope
includes the objects that a user can view in the console, and the tasks related to those
objects that they have permission to do. Role-based administration configurations are
applied at each site in a hierarchy.

For more information, see Configure role-based administration. This article details the
following actions:

     Create custom security roles

     Configure security roles

     Configure security scopes for an object

     Configure collections to manage security

     Create a new administrative user

     Modify the administrative scope of an administrative user

<!-- p.644 -->

  ） Important

  Your own administrative scope defines the objects and settings that you can assign
  when you configure role-based administration for another administrative user. For
  information about planning for role-based administration, see Fundamentals of
  role-based administration.

Manage accounts
Configuration Manager supports Windows accounts for many different tasks and uses.
To view accounts that are configured for different tasks, and to manage the password
that Configuration Manager uses for each account, use the following procedure:

      1. In the Configuration Manager console, go to the Administration workspace,
        expand Security, and then choose the Accounts node.

      2. To change the password for an account, select the account in the list. Then choose
        Properties in the ribbon.

      3. Choose Set to open the Windows User Account dialog box. Specify the new
        password for Configuration Manager to use for this account.

          ７ Note

          The password that you specify must match this account's password in Active
          Directory.

For more information, see Accounts used in Configuration Manager.

Microsoft Entra ID
Integrate Configuration Manager with Microsoft Entra ID to simplify and cloud-enable
your environment. Enable the site and clients to authenticate by using Microsoft Entra
ID.

For more information, see the Cloud Management service in Configure Azure services.

SMS Provider authentication

<!-- p.645 -->

You can specify the minimum authentication level for administrators to access
Configuration Manager sites. This feature enforces administrators to sign in to Windows
with the required level before they can access Configuration Manager. For more
information, see Plan for SMS Provider authentication.

  ） Important

  This configuration is a hierarchy-wide setting. Before you change this setting, make
  sure that all Configuration Manager administrators can sign in to Windows with the
  required authentication level.

To configure this setting, use the following steps:

   1. First sign in to Windows with the intended authentication level.

   2. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   3. Select Hierarchy Settings in the ribbon.

   4. Switch to the Authentication tab. Select the desired authentication level, and then
     select OK.

           Only when necessary, select Add to exclude specific users or groups. For
           more information, see Exclusions.

Exclusions
From the Authentication tab of Hierarchy Settings, you can also exclude certain users or
groups. Use this option sparingly. For example, when specific users require access to the
Configuration Manager console, but can't authenticate to Windows at the required level.
It may also be necessary for automation or services that run under the context of a
system account.

Next steps
     How to enable TLS 1.2

     Cryptographic controls technical reference

     Communication between endpoints

<!-- p.646 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.647 -->

Cryptographic controls technical
reference
Article • 10/15/2024

Applies to: Configuration Manager (current branch)

Configuration Manager uses signing and encryption to help protect the management of
the devices in the Configuration Manager hierarchy. With signing, if data has been
altered in transit, it's discarded. Encryption helps prevent an attacker from reading the
data by using a network protocol analyzer.

The primary hashing algorithm that Configuration Manager uses for signing is SHA-256.
When two Configuration Manager sites communicate with each other, they sign their
communications with SHA-256.

Starting in version 2107, the primary encryption algorithm that Configuration Manager
uses is AES-256. Encryption mainly happens in the following two areas:

      If you enable the site to Use encryption, the client encrypts its inventory data and
      state messages that it sends to the management point.

      When the client downloads secret policies, the management point always encrypts
      these policies. For example, an OS deployment task sequence that includes
      passwords.

  ７ Note

  If you configure HTTPS communication, these messages are encrypted twice. The
  message is encrypted with AES, then the HTTPS transport is encrypted with AES-
  256.

When you use client communication over HTTPS, configure your public key
infrastructure (PKI) to use certificates with the maximum hashing algorithms and key
lengths. When using CNG v3 certificates, Configuration Manager clients only support
certificates that use the RSA cryptographic algorithm. For more information, see PKI
certificate requirements and CNG v3 certificates overview.

For transport security, anything that uses TLS supports AES-256. This support includes
when you configure the site for enhanced HTTP (E-HTTP) or HTTPS. For on-premises site
systems, you can control the TLS cipher suites. For cloud-based roles like the cloud

<!-- p.648 -->

management gateway (CMG), if you enable TLS 1.2, Configuration Manager configures
the cipher suites.

For most cryptographic operations with Windows-based operating systems,
Configuration Manager uses these algorithms from the Windows CryptoAPI library
rsaenh.dll.

For more information about specific functionality, see Site operations.

Site operations
Information in Configuration Manager can be signed and encrypted. It supports these
operations with or without PKI certificates.

Policy signing and encryption
The site signs client policy assignments with its self-signed certificate. This behavior
helps prevent the security risk of a compromised management point from sending
tampered policies. If you use internet-based client management, this behavior is
important because it requires an internet-facing management point.

When policy contains sensitive data, starting in version 2107, the management point
encrypts it with AES-256. Policy that contains sensitive data is only sent to authorized
clients. The site doesn't encrypt policy that doesn't have sensitive data.

When a client stores policy, it encrypts the policy using the Windows data protection
application programming interface (DPAPI).

Policy hashing
When a client requests policy, it first gets a policy assignment. Then it knows which
policies apply to it, and it can request only those policy bodies. Each policy assignment
contains the calculated hash for the corresponding policy body. The client downloads
the applicable policy bodies and then calculates the hash for each policy body. If the
hash on the policy body doesn't match the hash in the policy assignment, the client
discards the policy body.

The hashing algorithm for policy is SHA-256.

Content hashing

<!-- p.649 -->

The distribution manager service on the site server hashes the content files for all
packages. The policy provider includes the hash in the software distribution policy.
When the Configuration Manager client downloads the content, the client regenerates
the hash locally and compares it to the one supplied in the policy. If the hashes match,
the content isn't altered, and the client installs it. If a single byte of the content is
altered, the hashes won't match, and the client doesn't install the software. This check
helps to make sure that the correct software is installed because the actual content is
compared with the policy.

The default hashing algorithm for content is SHA-256.

Not all devices can support content hashing. The exceptions include:

     Windows clients when they stream App-V content.

Inventory signing and encryption
When a client sends hardware or software inventory to a management point, it always
signs the inventory. It doesn't matter if the client communicates with the management
point over E-HTTP or HTTPS. If they use E-HTTP, you can also choose to encrypt this
data, which is recommended.

State migration encryption
When a task sequence captures data from a client for OS deployment, it always encrypts
the data. In version 2103 and later, the task sequence runs the User State Migration Tool
(USMT) with the AES-256 encryption algorithm.

Encryption for multicast packages
For every OS deployment package, you can enable encryption when you use multicast.
This encryption uses the AES-256 algorithm. If you enable encryption, no other
certificate configuration is required. The multicast-enabled distribution point
automatically generates symmetric keys to encrypt the package. Each package has a
different encryption key. The key is stored on the multicast-enabled distribution point
by using standard Windows APIs.

When the client connects to the multicast session, the key exchange occurs over an
encrypted channel. If the client uses HTTPS, it uses the PKI-issued client authentication
certificate. If the client uses E-HTTP, it uses the self-signed certificate. The client only
stores the encryption key in memory during the multicast session.

<!-- p.650 -->

Encryption for OS deployment media
When you use media to deploy operating systems, you should always specify a
password to protect the media. With a password, the task sequence environment
variables are encrypted with AES-128. Other data on the media, including packages and
content for applications, isn't encrypted.

Encryption for cloud-based content
When you enable a cloud management gateway (CMG) to store content, the content is
encrypted with AES-256. The content is encrypted whenever you update it. When clients
download the content, it's encrypted and protected by the HTTPS connection.

Signing in software updates
All software updates must be signed by a trusted publisher to protect against
tampering. On client computers, the Windows Update Agent (WUA) scans for the
updates from the catalog. It won't install the update if it can't locate the digital
certificate in the Trusted Publishers store on the local computer.

When you publish software updates with System Center Updates Publisher, a digital
certificate signs the software updates. You can either specify a PKI certificate or
configure Updates Publisher to generate a self-signed certificate to sign the software
update. If you use a self-signed certificate to publish the updates catalog, such as WSUS
Publishers Self-signed, the certificate must also be in the Trusted Root Certification
Authorities certificate store on the local computer. WUA also checks whether the Allow
signed content from intranet Microsoft update service location group policy setting is
enabled on the local computer. This policy setting must be enabled for WUA to scan for
the updates that were created and published with System Center Updates Publisher.

Signed configuration data for compliance settings
When you import configuration data, Configuration Manager verifies the file's digital
signature. If the files aren't signed, or if the signature check fails, the console warns you
to continue with the import. Only import the configuration data if you explicitly trust the
publisher and the integrity of the files.

Encryption and hashing for client notification
If you use client notification, all communication uses TLS and the highest algorithms that
the server and client can negotiate. The same negotiation occurs for hashing the packets

<!-- p.651 -->

that are transferred during client notification, which uses SHA-2.

Certificates
For a list of the public key infrastructure (PKI) certificates that can be used by
Configuration Manager, any special requirements or limitations, and how the certificates
are used, see PKI certificate requirements. This list includes the supported hash
algorithms and key lengths. Most certificates support SHA-256 and 2048-bits key
length.

Most Configuration Manager operations that use certificates also support v3 certificates.
For more information, see CNG v3 certificates overview.

  ７ Note

  All certificates that Configuration Manager uses must contain only single-byte
  characters in the subject name or subject alternative name.

Configuration Manager requires PKI certificates for the following scenarios:

     When you manage Configuration Manager clients on the internet

     When you use a cloud management gateway (CMG)

For most other communication that requires certificates for authentication, signing, or
encryption, Configuration Manager automatically uses PKI certificates if available. If they
aren't available, Configuration Manager generates self-signed certificates.

Mobile device management and PKI certificates

  ７ Note

  Since Nov 2021 we have deprecated Mobile device management and we
  recommend customers to uninstall this role.

OS deployment and PKI certificates
When you use Configuration Manager to deploy operating systems, and a management
point requires HTTPS client connections, the client needs a certificate to communicate
with the management point. This requirement is even when the client is in a transitional

<!-- p.652 -->

phase such as booting from task sequence media or a PXE-enabled distribution point.
To support this scenario, create a PKI client authentication certificate, and export it with
the private key. Then import it to the site server properties and also add the
management point's trusted root CA certificate.

If you create bootable media, you import the client authentication certificate when you
create the bootable media. To help protect the private key and other sensitive data
configured in the task sequence, configure a password on the bootable media. Every
computer that boots from the bootable media uses the same certificate with the
management point as required for client functions such as requesting client policy.

If you use PXE, import the client authentication certificate to the PXE-enabled
distribution point. It uses the same certificate for every client that boots from that PXE-
enabled distribution point. To help protect the private key and other sensitive data in
the task sequences, require a password for PXE.

If either of these client authentication certificates is compromised, block the certificates
in the Certificates node in the Administration workspace, Security node. To manage
these certificates, you need the permission to Manage operating system deployment
certificate.

After Configuration Manager deploys the OS installs the client, the client requires its
own PKI client authentication certificate for HTTPS client communication.

ISV proxy solutions and PKI certificates
Independent Software Vendors (ISVs) can create applications that extend Configuration
Manager. For example, an ISV could create extensions to support non-Windows client
platforms. However, if the site systems require HTTPS client connections, these clients
must also use PKI certificates for communication with the site. Configuration Manager
includes the ability to assign a certificate to the ISV proxy that enables communications
between the ISV proxy clients and the management point. If you use extensions that
require ISV proxy certificates, consult the documentation for that product.

If the ISV certificate is compromised, block the certificate in the Certificates node in the
Administration workspace, Security node.

Copy GUID for ISV proxy certificate
Starting in version 2111, to simplify the management of these ISV proxy certificates, you
can now copy its GUID in the Configuration Manager console.

   1. In the Configuration Manager console, go to the Administration workspace.

<!-- p.653 -->

   2. Expand Security, and select the Certificates node.

   3. Sort the list of the certificates by the Type column.

   4. Select a certificate of type ISV Proxy.

   5. In the ribbon, select Copy Certificate GUID.

This action copies this certificate's GUID, for example: aa05bf38-5cd6-43ea-ac61-
ab101f943987

Asset Intelligence and certificates

  ７ Note

  Since Nov 2021 we have deprecated Asset Intelligence and we recommend
  customers to uninstall this role.

Azure services and certificates
The cloud management gateway (CMG) requires server authentication certificates. These
certificates allow the service to provide HTTPS communication to clients over the
internet. For more information, see CMG server authentication certificate.

Clients require another type of authentication to communicate with a CMG and the on-
premises management point. They can use Microsoft Entra ID, a PKI certificate, or a site
token. For more information, see Configure client authentication for cloud management
gateway.

Clients don't require a client PKI certificate to use cloud-based storage. After they
authenticate to the management point, the management point issues a Configuration
Manager access token to the client. The client presents this token to the CMG to access
the content. The token is valid for eight hours.

CRL checking for PKI certificates
A PKI certificate revocation list (CRL) increases overall security, but does require some
administrative and processing overhead. If you enable CRL checking, but clients can't
access the CRL, the PKI connection fails.

IIS enables CRL checking by default. If you use a CRL with your PKI deployment, you
don't need to configure most site systems that run IIS. The exception is for software

<!-- p.654 -->

updates, which requires a manual step to enable CRL checking to verify the signatures
on software update files.

When a client uses HTTPS, it enables CRL checking by default.

The following connections don't support CRL checking in Configuration Manager:

      Server-to-server connections

Server communication
Configuration Manager uses the following cryptographic controls for server
communication.

Server communication within a site
Each site system server uses a certificate to transfer data to other site systems in the
same Configuration Manager site. Some site system roles also use certificates for
authentication. For example, if you install the enrollment proxy point on one server, and
the enrollment point on another server, they can authenticate one another by using this
identity certificate.

When Configuration Manager uses a certificate for this communication, if there's a PKI
certificate available with server authentication capability, Configuration Manager
automatically uses it. If not, Configuration Manager generates a self-signed certificate.
This self-signed certificate has server authentication capability, uses SHA-256, and has a
key length of 2048 bits. Configuration Manager copies the certificate to the Trusted
People store on other site system servers that might need to trust the site system. Site
systems can then trust one another by using these certificates and PeerTrust.

In addition to this certificate for each site system server, Configuration Manager
generates a self-signed certificate for most site system roles. When there is more than
one instance of the site system role in the same site, they share the same certificate. For
example, you might have multiple management points in the same site. This self-signed
certificate uses SHA-256 and has a key length of 2048 bits. It's copied to the Trusted
People Store on site system servers that might need to trust it. The following site system
roles generate this certificate:

      Asset Intelligence synchronization point

      Endpoint Protection point

      Fallback status point

<!-- p.655 -->

     Management point

     Multicast-enabled distribution point

     Reporting services point

     Software update point

     State migration point

Configuration Manager automatically generates and manages these certificates.

To send status messages from the distribution point to the management point,
Configuration Manager uses a client authentication certificate. When you configure the
management point for HTTPS, it requires a PKI certificate. If the management point
accepts E-HTTP connections, you can use a PKI certificate. It can also use a self-signed
certificate with client authentication capability, uses SHA-256, and has a key length of
2048 bits.

Server communication between sites
Configuration Manager transfers data between sites by using database replication and
file-based replication. For more information, see Data transfers between sites and
Communications between endpoints.

Configuration Manager automatically configures the database replication between sites.
If available, it uses PKI certificates with server authentication capability. If not available,
Configuration Manager creates self-signed certificates for server authentication. In both
cases, it authenticates between sites by using certificates in the Trusted People store that
uses PeerTrust. It uses this certificate store to make sure that only the Configuration
Manager hierarchy SQL Servers participate in site-to-site replication.

Site servers establish site-to-site communication by using a secure key exchange that
happens automatically. The sending site server generates a hash and signs it with its
private key. The receiving site server checks the signature by using the public key and
compares the hash with a locally generated value. If they match, the receiving site
accepts the replicated data. If the values don't match, Configuration Manager rejects the
replication data.

Database replication in Configuration Manager uses the SQL Server Service Broker to
transfer data between sites. It uses the following mechanisms:

     SQL Server to SQL Server: This connection uses Windows credentials for server
     authentication and self-signed certificates with 1024 bits to sign and encrypt the

<!-- p.656 -->

     data with the AES algorithm. If available, it uses PKI certificates with server
     authentication capability. It only uses certificates in the computer's Personal
     certificate store.

     SQL Service Broker: This service uses self-signed certificates with 2048 bits for
     authentication and to sign and encrypt the data with the AES algorithm. It only
     uses certificates in the SQL Server master database.

File-based replication uses the server message block (SMB) protocol. It uses SHA-256 to
sign data that isn't encrypted and doesn't contain any sensitive data. To encrypt this
data, use IPsec, which you implement independently from Configuration Manager.

Clients that use HTTPS
When site system roles accept client connections, you can configure them to accept
HTTPS and HTTP connections, or only HTTPS connections. Site system roles that accept
connections from the internet only accept client connections over HTTPS.

Client connections over HTTPS offer a higher level of security by integrating with a
public key infrastructure (PKI) to help protect client-to-server communication. However,
configuring HTTPS client connections without a thorough understanding of PKI
planning, deployment, and operations could still leave you vulnerable. For example, if
you don't secure your root certificate authority (CA), attackers could compromise the
trust of your entire PKI infrastructure. Failing to deploy and manage the PKI certificates
by using controlled and secured processes might result in unmanaged clients that can't
receive critical software updates or packages.

  ） Important

  The PKI certificates that Configuration Manager uses for client communication
  protect the communication only between the client and some site systems. They
  don't protect the communication channel between the site server and site systems
  or between site servers.

Unencrypted communication when clients use HTTPS
When clients communicate with site systems over HTTPS, most traffic is encrypted. In
the following situations, clients communicate with site systems without using
encryption:

<!-- p.657 -->

     Client fails to make an HTTPS connection on the intranet and falls back to using
     HTTP when site systems allow this configuration.

     Communication to the following site system roles:

        Client sends state messages to the fallback status point.

        Client sends PXE requests to a PXE-enabled distribution point.

        Client sends notification data to a management point.

You configure reporting services points to use HTTP or HTTPS independently from the
client communication mode.

Clients that use E-HTTP
When clients use E-HTTP communication to site system roles, they can use PKI
certificates for client authentication, or self-signed certificates that Configuration
Manager generates. When Configuration Manager generates self-signed certificates,
they have a custom object identifier for signing and encryption. These certificates are
used to uniquely identify the client. These self-signed certificates use SHA-256, and
have a key length of 2048 bits.

OS deployment and self-signed certificates
When you use Configuration Manager to deploy operating systems with self-signed
certificates, the client must also have a certificate to communicate with the management
point. This requirement is even if the computer is in a transitional phase such as booting
from task sequence media or a PXE-enabled distribution point. To support this scenario
for E-HTTP client connections, Configuration Manager generates self-signed certificates
that have a custom object identifier for signing and encryption. These certificates are
used to uniquely identify the client. These self-signed certificates use SHA-256, and
have a key length of 2048 bits. If these self-signed certificates are compromised, prevent
attackers from using them to impersonate trusted clients. Block the certificates in the
Certificates node in the Administration workspace, Security node.

Client and server authentication
When clients connect over E-HTTP, they authenticate the management points by using
either Active Directory Domain Services or by using the Configuration Manager trusted
root key. Clients don't authenticate other site system roles, such as state migration
points or software update points.

<!-- p.658 -->

When a management point first authenticates a client by using the self-signed client
certificate, this mechanism provides minimal security because any computer can
generate a self-signed certificate. Use client approval to enhance this process. Only
approve trusted computers, either automatically by Configuration Manager, or manually
by an administrative user. For more information, see Manage clients.

About SSL vulnerabilities
To improve the security of your Configuration Manager clients and servers, do the
following actions:

     Enable TLS 1.2 across all devices and services. To enable TLS 1.2 for Configuration
     Manager, see How to enable TLS 1.2 for Configuration Manager.

     Disable SSL 3.0, TLS 1.0, and TLS 1.1.

     Reorder the TLS-related cipher suites.

For more information, see the following articles:

     Restrict the use of certain cryptographic algorithms and protocols in Schannel.dll
     Prioritizing Schannel cipher suites

These procedures don't affect Configuration Manager functionality.

  ７ Note

  Updates to Configuration Manager download from the Azure content delivery
  network (CDN), which has cipher suite requirements. For more information, see
  Azure Front Door: TLS configuration FAQ..

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.659 -->

Certificates in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager uses a combination of self-signed and public key infrastructure
(PKI) digital certificates.

Use PKI certificates whenever possible. For more information, see PKI certificate
requirements. When Configuration Manager requests PKI certificates during enrollment
for mobile devices, use Active Directory Domain Services and an enterprise certification
authority. For all other PKI certificates, deploy and manage them independently from
Configuration Manager.

PKI certificates are required when client computers connect to internet-based site
systems. The cloud management gateway also requires certificates. For more
information, see Manage clients on the internet.

When you use a PKI, you can also use IPsec to help secure the server-to-server
communication between site systems in a site, between sites, and for other data transfer
between computers. Implementation of IPsec is independent from Configuration
Manager.

When PKI certificates aren't available, Configuration Manager automatically generates
self-signed certificates. Some certificates in Configuration Manager are always self-
signed. In most cases, Configuration Manager automatically manages the self-signed
certificates, and you don't have to take another action. One example is the site server
signing certificate. This certificate is always self-signed. It makes sure that the policies
that clients download from the management point were sent from the site server and
weren't tampered with. As another example, when you enable the site for Enhanced
HTTP, the site issues self-signed certificates to site server roles.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

CNG v3 certificates

<!-- p.660 -->

Configuration Manager supports Cryptography: Next Generation (CNG) v3 certificates.
Configuration Manager clients can use a PKI client authentication certificate with private
key in a CNG Key Storage Provider (KSP). With KSP support, Configuration Manager
clients support hardware-based private keys, such as a TPM KSP for PKI client
authentication certificates.

For more information, see CNG v3 certificates overview.

Enhanced HTTP
Using HTTPS communication is recommended for all Configuration Manager
communication paths, but is challenging for some customers because of the overhead
of managing PKI certificates. The introduction of Microsoft Entra integration reduces
some but not all of the certificate requirements. You can instead enable the site to use
enhanced HTTP. This configuration supports HTTPS on site systems by using self-signed
certificates, along with Microsoft Entra ID for some scenarios. It doesn't require PKI.

For more information, see Enhanced HTTP.

Certificates for CMG
Managing clients on the internet via the cloud management gateway (CMG) requires the
use of certificates. The number and type of certificates varies depending upon your
specific scenarios.

For more information, see CMG set up checklist.

  ７ Note

  The cloud-based distribution point (CDP) is deprecated. Starting in version 2107,
  you can't create new CDP instances. To provide content to internet-based devices,
  enable the CMG to distribute content. For more information, see Deprecated
  features.

  For more information about certificates for a CDP, see Certificates for the cloud
  distribution point.

The site server signing certificate

<!-- p.661 -->

The site server always creates a self-signed certificate. It uses this certificate for several
purposes.

Clients can securely get a copy of the site server signing certificate from Active Directory
Domain Services and from client push installation. If clients can't get a copy of this
certificate by one of these mechanisms, install it when you install the client. This process
is especially important if the client's first communication with the site is with an internet-
based management point. Because this server is connected to an untrusted network, it's
more vulnerable to attack. If you don't take this other step, clients automatically
download a copy of the site server signing certificate from the management point.

Clients can't securely get a copy of the site server certificate in the following scenarios:

     You don't install the client by using client push, and:

        You haven't extended the Active Directory schema for Configuration Manager.

        You haven't published the client's site to Active Directory Domain Services.

        The client is from an untrusted forest or a workgroup.

     You're using internet-based client management and you install the client when it's
     on the internet.

For more information on how to install clients with a copy of the site server signing
certificate, use the SMSSIGNCERT command-line property. For more information, see
About client installation parameters and properties.

Hardware-bound key storage provider
Configuration Manager uses self-signed certificates for client identity and to help
protect communication between the client and site systems. When you update the site
and clients to version 2107 or later, the client stores its certificate from the site in a
hardware-bound key storage provider (KSP). This KSP is typically the trusted platform
module (TPM) at least version 2.0. The certificate is also marked non-exportable.

If the client also has a PKI-based certificate, it continues to use that certificate for TLS
HTTPS communication. It uses its self-signed certificate for signing messages with the
site. For more information, see PKI certificate requirements.

  ７ Note

  For clients that also have a PKI certificate, the Configuration Manager console
  displays the Client certificate property as Self-signed. The client control panel

<!-- p.662 -->

  Client certificate property shows PKI.

When you update to version 2107 or later, clients with PKI certificates will recreate self-
signed certificates, but don't reregister with the site. Clients without a PKI certificate will
reregister with the site, which can cause extra processing at the site. Make sure that your
process to update clients allows for randomization. If you simultaneously update lots of
clients, it may cause a backlog on the site server.

Configuration Manager doesn't use TPMs that are known vulnerable. For example, the
TPM version is earlier than 2.0. If a device has a vulnerable TPM, the client falls back to
using a software-based KSP. The certificate is still not exportable.

OS deployment media doesn't use hardware-bound certificates, it continues to use self-
signed certificates from the site. You create the media on a device that has the console,
but then it can run on any client.

To troubleshoot certificate behaviors, use the CertificateMaintenance.log on the client.

Next steps
     Plan for PKI certificates in Configuration Manager

     Configure security

     Cryptographic controls technical reference

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.663 -->

Plan for PKI certificates in Configuration
Manager
Article • 04/11/2023

Applies to: Configuration Manager (current branch)

Configuration Manager uses public key infrastructure (PKI)-based digital certificates
when available. Use of these certificates is recommended for greater security, but not
required for most scenarios. You need to deploy and manage these certificates
independently from Configuration Manager.

This article provides information about PKI certificates in Configuration Manager to help
you plan your implementation. For more general information about the use of
certificates in Configuration Manager, see Certificates in Configuration Manager.

PKI certificate revocation
When you use PKI certificates with Configuration Manager, plan for use of a certificate
revocation list (CRL). Devices use the CRL to verify the certificate on the connecting
computer. The CRL is a file that a certificate authority (CA) creates and signs. It has a list
of certificates that the CA has issued but revoked. When a certificate administrator
revokes certificates, its thumbprint is added to the CRL. For example, if an issued
certificate is known or suspected to be compromised.

  ） Important

  Because the location of the CRL is added to a certificate when a CA issues it, make
  sure that you plan for the CRL before you deploy any PKI certificates that
  Configuration Manager uses.

IIS always checks the CRL for client certificates, and you can't change this configuration
in Configuration Manager. By default, Configuration Manager clients always check the
CRL for site systems. Disable this setting by specifying a site property and by specifying
a CCMSetup property.

Computers that use certificate revocation checking but can't locate the CRL behave as if
all certificates in the certification chain are revoked. This behavior is because they can't
verify if the certificates are in the certificate revocation list. In this scenario, all
connections fail that require certificates and include CRL checking. When validating that

<!-- p.664 -->

your CRL is accessible by browsing to its HTTP location, it's important to note that the
Configuration Manager client runs as LOCAL SYSTEM. Testing CRL accessibility with a
web browser under a user context may succeed, but the computer account may be
blocked when attempting to make an HTTP connection to the same CRL URL. For
example, it can be blocked because of an internal web filtering solution like a proxy. Add
the CRL URL to the approved list for any web filtering solutions.

Checking the CRL every time that a certificate is used offers more security against using
a certificate that's revoked. It does introduce a connection delay and more processing
on the client. Your organization may require this security check for clients on the
internet or an untrusted network.

Consult your PKI administrators before you decide whether Configuration Manager
clients need to check the CRL. When both of the following conditions are true, consider
keeping this option enabled in Configuration Manager:

     Your PKI infrastructure supports a CRL, and it's published where all Configuration
     Manager clients can locate it. These clients might include devices on the internet,
     and ones in untrusted forests.

     The requirement to check the CRL for each connection to a site system that's
     configured to use a PKI certificate is greater than the following requirements:
        Faster connections
        Efficient processing on the client
        The risk of clients failing to connect to servers if they can't locate the CRL

PKI trusted root certificates
If your IIS site systems use PKI client certificates for client authentication over HTTP, or
for client authentication and encryption over HTTPS, you might have to import root CA
certificates as a site property. Here are the two scenarios:

     You deploy operating systems by using Configuration Manager, and the
     management points only accept HTTPS client connections.

     You use PKI client certificates that don't chain to a root certificate that the
     management points trust.

        ７ Note

        When you issue client PKI certificates from the same CA hierarchy that issues
        the server certificates that you use for management points, you don't have to
        specify this root CA certificate. However, if you use multiple CA hierarchies

<!-- p.665 -->

        and you aren't sure whether they trust each other, import the root CA for the
        clients' CA hierarchy.

If you need to import root CA certificates for Configuration Manager, export them from
the issuing CA or from the client computer. If you export the certificate from the issuing
CA that's also the root CA, don't export the private key. Store the exported certificate file
in a secure location to prevent tampering. You need access to the file when you set up
the site. If you access the file over the network, make sure the communication is
protected from tampering by using IPsec.

If any root CA certificate that you import are renewed, import the renewed certificate.

These imported root CA certificates and the root CA certificate of each management
point create the certificate issuers list. Configuration Manager computers use this list in
the following ways:

      When clients connect to management points, the management point verifies that
      the client certificate is chained to a trusted root certificate in the site's certificate
      issuers list. If it doesn't, the certificate is rejected, and the PKI connection fails.

      When clients select a PKI certificate and have a certificate issuers list, they select a
      certificate that chains to a trusted root certificate in the certificate issuers list. If
      there's no match, the client doesn't select a PKI certificate. For more information,
      see PKI client certificate selection.

PKI client certificate selection
If your IIS site systems use PKI client certificates for client authentication over HTTP or
for client authentication and encryption over HTTPS, plan for how Windows clients
select the certificate to use for Configuration Manager.

  ７ Note

  Some devices don't support a certificate selection method. Instead, they
  automatically select the first certificate that fulfills the certificate requirements. For
  example, clients on macOS computers and mobile devices don't support a
  certificate selection method.

In many cases, the default configuration and behavior are sufficient. The Configuration
Manager client on Windows computers filters multiple certificates by using these criteria
in this order:

<!-- p.666 -->

   1. The certificate issuers list: The certificate chains to a root CA that's trusted by the
      management point.

   2. The certificate is in the default certificate store of Personal.

   3. The certificate is valid, not revoked, and not expired. The validity check also verifies
      that the private key is accessible.

   4. The certificate has client authentication capability.

   5. The certificate Subject Name contains the local computer name as a substring.

   6. The certificate has the longest validity period.

Configure clients to use the certificate issuers list by using the following mechanisms:

      Publish it with Configuration Manager site information to Active Directory Domain
      Services.

      Install clients by using client push.

      Clients download it from the management point after they're successfully assigned
      to their site.

      Specify it during client installation as a CCMSetup client.msi property of
      CCMCERTISSUERS.

If clients don't have the certificate issuers list when they're first installed, and aren't yet
assigned to the site, they skip this check. When clients do have the certificate issuers list,
and don't have a PKI certificate that chains to a trusted root certificate in the certificate
issuers list, certificate selection fails. Clients don't continue with the other certificate
selection criteria.

In most cases, the Configuration Manager client correctly identifies a unique and
appropriate PKI certificate. When this behavior isn't the case, instead of selecting the
certificate based on the client authentication capability, you can set up two alternative
selection methods:

      A partial string match on the client certificate subject name. This method is a case-
      insensitive match. It's appropriate if you're using the fully qualified domain name
      (FQDN) of a computer in the subject field and want the certificate selection to be
      based on the domain suffix, for example contoso.com. You can use this selection
      method to identify any string of sequential characters in the certificate subject
      name that differentiates the certificate from others in the client certificate store.

<!-- p.667 -->

           ７ Note

           You can't use the partial string match with the subject alternative name (SAN)
           as a site setting. Although you can specify a partial string match for the SAN
           by using CCMSetup, it'll be overwritten by the site properties in the following
           scenarios:
             Clients retrieve site information that's published to Active Directory
             Domain Services.
             Clients are installed by using client push installation.

           Use a partial string match in the SAN only when you install clients manually
           and when they don't retrieve site information from Active Directory Domain
           Services. For example, these conditions apply to internet-only clients.

      A match on the client certificate subject name attribute values or the subject
      alternative name (SAN) attribute values. This method is a case-sensitive match. It's
      appropriate if you're using an X500 distinguished name or equivalent object
      identifiers (OIDs) in compliance with RFC 3280, and you want the certificate
      selection to be based on the attribute values. You can specify only the attributes
      and their values that you require to uniquely identify or validate the certificate and
      differentiate the certificate from others in the certificate store.

The following table shows the attribute values that Configuration Manager supports for
the client certificate selection criteria:

                                                                               ﾉ    Expand table

 OID Attribute                    Distinguished name attribute      Attribute definition

 0.9.2342.19200300.100.1.25       DC                                Domain component

 1.2.840.113549.1.9.1             E or E-mail                       Email address

 2.5.4.3                          CN                                Common name

 2.5.4.4                          SN                                Subject name

 2.5.4.5                          SERIALNUMBER                      Serial number

 2.5.4.6                          C                                 Country code

 2.5.4.7                          L                                 Locality

 2.5.4.8                          S or ST                           State or province name

<!-- p.668 -->

 OID Attribute                  Distinguished name attribute       Attribute definition

 2.5.4.9                        STREET                             Street address

 2.5.4.10                       O                                  Organization name

 2.5.4.11                       OU                                 Organizational unit

 2.5.4.12                       T or Title                         Title

 2.5.4.42                       G or GN or GivenName               Given name

 2.5.4.43                       I or Initials                      Initials

 2.5.29.17                      (no value)                         Subject Alternative Name

  ７ Note

  If you configure either of the above alternate certificate selection methods, the
  certificate Subject Name doesn't need to contain the local computer name.

If more than one appropriate certificate is located after the selection criteria are applied,
you can override the default configuration to select the certificate that has the longest
validity period. Instead, you can specify that no certificate is selected. In this scenario,
the client can't communicate with IIS site systems with a PKI certificate. The client sends
an error message to its assigned fallback status point to alert you to the certificate
selection failure. Then you can change or refine your certificate selection criteria.

The client behavior then depends on whether the failed connection was over HTTPS or
HTTP:

      If the failed connection was over HTTPS: The client tries to connect over HTTP and
      uses the client self-signed certificate.

      If the failed connection was over HTTP: The client tries to connect again over HTTP
      by using the self-signed client certificate.

To help identify a unique PKI client certificate, you can also specify a custom store other
than the default of Personal in the Computer store. Create a custom certificate store
outside of Configuration Manager. You need to be able to deploy certificates to this
custom store and renew them before the validity period expires.

For more information, see Configure settings for client PKI certificates.

Transition strategy for PKI certificates

<!-- p.669 -->

The flexible configuration options in Configuration Manager let you gradually transition
clients and the site to use PKI certificates to help secure client endpoints. PKI certificates
provide better security and enable you to manage internet clients.

This plan first introduces PKI certificates for authentication only over HTTP, and then for
authentication and encryption over HTTPS. When you follow this plan to gradually
introduce these certificates, you reduce the risk that clients become unmanaged. You'll
also benefit from the highest security that Configuration Manager supports.

Because of the number of configuration options and choices in Configuration Manager,
there's no single way to transition a site so that all clients use HTTPS connections. The
following steps provide general guidance:

   1. Install the Configuration Manager site and configure it so that site systems accept
     client connections over HTTPS and HTTP.

   2. Configure the Communication Security tab in the site properties. Set Site System
     Settings to HTTP or HTTPS and select Use PKI client certificate (client
     authentication capability) when available. For more information, see Configure
     settings for client PKI certificates.

   3. Pilot a PKI rollout for client certificates. For an example deployment, see Deploy
     the client certificate for Windows computers.

   4. Install clients by using the client push installation method. For more information,
     see the How to install Configuration Manager clients by using client push.

   5. Monitor client deployment and status by using the reports and information in the
     Configuration Manager console.

   6. Track how many clients are using a client PKI certificate by viewing the Client
     Certificate column in the Assets and Compliance workspace, Devices node.

        ７ Note

        For clients that also have a PKI certificate, the Configuration Manager console
        displays the Client certificate property as Self-signed. The client control panel
        Client certificate property shows PKI.

     You can also deploy the Configuration Manager HTTPS Readiness Assessment Tool
     (CMHttpsReadiness.exe) to computers. Then use the reports to view how many
     computers can use a client PKI certificate with Configuration Manager.

<!-- p.670 -->

    ７ Note

    When you install the Configuration Manager client, it installs the
    CMHttpsReadiness.exe tool in the %windir%\CCM folder. The following
    command-line options are available when you run this tool:

          /Store:<Certificate store name> : This option is the same as the

          CCMCERTSTORE client.msi property - /Issuers:<Case-sensitive issuer
          common name> : This option is the same as the CCMCERTISSUERS

          client.msi property
          /Criteria:<Selection criteria> : This option is the same as the

          CCMCERTSEL client.msi property
          /SelectFirstCert : This option is the same as the CCMFIRSTCERT

          client.msi property

  The tool outputs information to the CMHttpsReadiness.log in the CCM\Logs
  directory.

  For more information, see About client installation properties.

7. When you're confident that enough clients are successfully using their client PKI
  certificate for authentication over HTTP, follow these steps:

  a. Deploy a PKI web server certificate to a member server that runs another
     management point for the site, and configure that certificate in IIS. For more
     information, see Deploy the web server certificate for site systems that run IIS.

  b. Install the management point role on this server. Configure the Client
     connections option in the management point properties for HTTPS.

8. Monitor and verify that clients that have a PKI certificate use the new management
  point by using HTTPS. You can use IIS logging or performance counters to verify.

9. Reconfigure other site system roles to use HTTPS client connections. If you want to
  manage clients on the internet, make sure that site systems have an internet
  FQDN. Configure individual management points and distribution points to accept
  client connections from the internet.

    ） Important

<!-- p.671 -->

        Before you set up site system roles to accept connections from the internet,
        review the planning information and prerequisites for internet-based client
        management. For more information, see Communications between
        endpoints.

 10. Extend the PKI certificate rollout for clients and for site systems that run IIS. Set up
     the site system roles for HTTPS client connections and internet connections, as
     required.

 11. For the highest security: When you're confident that all clients are using a client
     PKI certificate for authentication and encryption, change the site properties to use
     HTTPS only.

Next steps
     Configure security

     Cryptographic controls technical reference

     PKI certificate requirements

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.672 -->

CNG v3 certificates overview
Article • 10/04/2022

Configuration Manager supports Cryptography: Next Generation (CNG) certificates.
Configuration Manager clients can use a PKI client authentication certificate with the
private key generated and stored in a CNG Key Storage Provider (KSP). With KSP
support, Configuration Manager clients support hardware-based private keys, such as a
TPM KSP for PKI client authentication certificates.

  ７ Note

  When using CNG certificates, Configuration Manager clients only support
  certificates that use the RSA cryptographic algorithm.

Supported scenarios
You can use Cryptography API: Next Generation (CNG) v3 certificate templates for the
following scenarios:

      Client registration and communication with an HTTPS management point
      Software distribution and application deployment with an HTTPS distribution point
      OS deployment
      Client messaging SDK (with latest update) and ISV Proxy
      Cloud management gateway (CMG) configuration
      User-targeted available applications in Software Center

Also use CNG v3 certificates for the following HTTPS-enabled server roles:

      Management point
      Distribution point
      Software update point
      State migration point
      Certificate registration point, including the NDES server with the Configuration
      Manager policy module

  ７ Note

  CNG is backward compatible with Crypto API (CAPI). CAPI certificates continue to
  be supported even when CNG support is enabled on the client.

<!-- p.673 -->

Unsupported scenarios
The following scenarios currently aren't supported:

     The following server roles aren't operational when installed in HTTPS mode with a
     CNG v3 certificate bound to the web site in Internet Information Services (IIS):
         Enrollment point
         Enrollment proxy point

To use CNG certificates
To use CNG v3 certificates, your certification authority (CA) needs to provide CNG
certificate templates for target machines. Template details vary according to the
scenario; however, the following properties are required:

     Compatibility tab

         Certificate Authority must be Windows Server 2008 or later. (Windows Server
         2012 is recommended.)

         Certificate recipient must be Windows Vista/Server 2008 or later. (Windows
         8/Windows Server 2012 is recommended.)

     Cryptography tab

         Provider Category must be Key Storage Provider. (required)

         Algorithm name must be RSA. (required)

         Request must use one of the following providers: must be Microsoft Software
         Key Storage Provider.

  ７ Note

  The requirements for your environment or organization may be different. Contact
  your PKI expert. The important point to consider is a certificate template must use a
  Key Storage Provider to take advantage of CNG.

For best results, we recommend building the Subject Name from Active Directory
information. Use the DNS Name for Subject name format and include the DNS name in
the alternate subject name. Otherwise, you must provide this information when the
device enrolls into the certificate profile.

<!-- p.674 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.675 -->

PKI certificate requirements for
Configuration Manager
Article • 03/22/2023

Applies to: Configuration Manager (current branch)

The public key infrastructure (PKI) certificates that you might require for Configuration
Manager are listed in the following tables. This information assumes basic knowledge of
PKI certificates.

You can use any PKI to create, deploy, and manage most certificates in Configuration
Manager. For client certificates that Configuration Manager enrolls on mobile devices
and Mac computers, they require use of Active Directory Certificate Services.

When you use Active Directory Certificate Services and certificate templates, this
Microsoft PKI solution can ease the management of certificates. Use the Microsoft
certificate template reference in the sections below to identify the certificate template
that most closely matches the certificate requirements. Only an enterprise certification
authority (CA) that runs on the Enterprise or Datacenter editions of Windows server can
use template-based certificates.

For more information, see the following articles:

      Step-by-step example deployment of the PKI certificates for Configuration
      Manager: Windows Server 2008 Certification Authority

      Active Directory Certificate Services Overview

      How to enable Transport Layer Security (TLS) 1.2

Supported certificate types

Secure Hash Algorithm 2 (SHA-2) certificates
Issue new server and client authentication certificates that are signed with SHA-2, which
includes SHA-256 and SHA-512. All internet-facing services should use an SHA-2
certificate. For example, if you purchase a public certificate for use with a cloud
management gateway, make sure that you purchase an SHA-2 certificate.

Windows doesn't trust certificates signed with SHA-1. For more information, see
Windows Enforcement of SHA1 certificates       .

<!-- p.676 -->

CNG v3 certificates
Configuration Manager supports Cryptography: Next Generation (CNG) v3 certificates.
Configuration Manager clients can use a PKI client authentication certificate with private
key in a CNG Key Storage Provider (KSP). With KSP support, Configuration Manager
clients support hardware-based private keys, such as a TPM KSP for PKI client
authentication certificates.

For more information, see CNG v3 certificates overview.

PKI certificates for servers

Site systems that run IIS and support HTTPS client
connections
This web server certificate is used to:

     Authenticate the servers to the client
     Encrypt all data that's transferred between the client and these servers with TLS.

Applies to:

     Management point
     Distribution point
     Software update point
     State migration point
     Enrollment point
     Enrollment proxy point
     Certificate registration point

Certificate requirements:

     Certificate purpose: Server authentication

     Microsoft certificate template: Web Server

     The Enhanced Key Usage value must contain Server Authentication
     (1.3.6.1.5.5.7.3.1)

     Subject Name:

        If the site system accepts connections from the internet, the Subject Name or
        Subject Alternative Name must contain the internet fully qualified domain

<!-- p.677 -->

         name (FQDN).

         If the site system accepts connections from the intranet, the Subject Name or
         Subject Alternative Name must contain either the intranet FQDN
         (recommended) or the computer's name, depending on how the site system is
         set up.

         If the site system accepts connections from both the internet and the intranet,
         both the internet FQDN and the intranet FQDN (or computer name) must be
         specified. Use the ampersand ( & ) symbol delimiter between the two names.

        ７ Note

        When the software update point accepts client connections from the internet
        only, the certificate must contain both the internet FQDN and the intranet
        FQDN.

     Key length: Configuration Manager doesn't specify a maximum supported key
     length for this certificate. Consult your PKI and IIS documentation for any key-size
     related issues for this certificate.

Most site system roles support key storage providers for certificate private keys (v3). For
more information, see CNG v3 certificates overview.

This certificate must be in the Personal store in the Computer certificate store.

Cloud management gateway (CMG)
This service certificate is used to:

     Authenticate the CMG service in Azure to Configuration Manager clients

     Encrypt all data transferred between them by using TLS.

Export this certificate in a Public Key Certificate Standard (PKCS #12) format. You need to
know the password, so that you can import the certificate when you create the CMG.

Certificate requirements:

     Certificate purpose: Server authentication

     Microsoft certificate template: Web Server

<!-- p.678 -->

     The Enhanced Key Usage value must contain Server Authentication
     (1.3.6.1.5.5.7.3.1)

     The Subject Name must contain a customer-defined service name as the Common
     Name for the specific instance of the cloud management gateway.

     The private key must be exportable.

     Supported key lengths: 2048-bit or 4096-bit

This certificate supports key storage providers for certificate private keys (v3).

For more information, see CMG server authentication certificate.

Site system servers that run Microsoft SQL Server
This certificate is used for server-to-server authentication.

Certificate requirements:

     Certificate purpose: Server authentication

     Microsoft certificate template: Web Server

     The Enhanced Key Usage value must contain Server Authentication
     (1.3.6.1.5.5.7.3.1)

     The Subject Name must contain the intranet fully qualified domain name (FQDN)

     Maximum supported key length is 2,048 bits.

This certificate must be in the Personal store in the Computer certificate store.
Configuration Manager automatically copies it to the Trusted People Store for servers in
the Configuration Manager hierarchy that might have to establish trust with the server.

SQL Server Always On failover cluster instance
This certificate is used for server-to-server authentication.

Certificate requirements:

     Certificate purpose: Server authentication

     Microsoft certificate template: Web Server

<!-- p.679 -->

     The Enhanced Key Usage value must contain Server Authentication
     (1.3.6.1.5.5.7.3.1)

     The Subject Name must contain the intranet fully qualified domain name (FQDN)
     of the cluster

     The private key must be exportable

     The certificate must have a validity period of at least two years when you configure
     Configuration Manager to use the failover cluster instance

     Maximum supported key length is 2,048 bits.

Request and install this certificate on one node in the cluster. Then export the certificate
and import it to the other nodes.

This certificate must be in the Personal store in the Computer certificate store.
Configuration Manager automatically copies it to the Trusted People Store for servers in
the Configuration Manager hierarchy that might have to establish trust with the server.

Site system monitoring
Applies to:

     Management point
     State migration point

Certificate requirements:

     Certificate purpose: Client authentication

     Microsoft certificate template: Workstation Authentication

     The Enhanced Key Usage value must contain Client Authentication
     (1.3.6.1.5.5.7.3.2)

     Computers must have a unique value in the Subject Name field or in the Subject
     Alternative Name field.

        ７ Note

        If you use multiple values for the Subject Alternative Name, it only uses the
        first value.

<!-- p.680 -->

      Maximum supported key length is 2,048 bits.

This certificate is required on the listed site system servers, even if the Configuration
Manager client isn't installed. This configuration allows the site to monitor and report on
the health of these site system roles.

The certificate for these site systems must be in the Personal store of the Computer
certificate store.

Servers running the Configuration Manager Policy
Module with the Network Device Enrollment Service
(NDES) role service
Certificate requirements:

      Certificate purpose: Client authentication

      Microsoft certificate template: Workstation Authentication

      The Enhanced Key Usage value must contain Client Authentication
      (1.3.6.1.5.5.7.3.2)

      There are no specific requirements for the certificate Subject Name or Subject
      Alternative Name (SAN). You can use the same certificate for multiple servers
      running the Network Device Enrollment Service.

      Supported key lengths: 1,024 bits and 2,048 bits.

Site systems that have a distribution point installed
This certificate has two purposes:

      It authenticates the distribution point to an HTTPS-enabled management point
      before the distribution point sends status messages.

        ７ Note

        When you configure all management points for HTTPS, then HTTPS-enabled
        distribution points must use a PKI-issued certificate. Don't use self-signed
        certificates on distribution points when management points use certificates.
        Issues may occur otherwise. For example, distribution points won't sent state
        messages.
