---
title: "Exchange Server — pages 281-320"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0281-0320
family: exchange
documentKind: "doc"
abstract: "Property Microsoft Exchange Microsoft WMSVC Exchange Server Auth Certificate was installed. Manager service was installed. Expires on (NotAfter) 5 years after NotBefore . 5 years after 10 years after NotBefore . NotBefore . Public key size 2048 2048 2048 (PublicKeySize) RootCATy"
---

# Exchange Server — pages 281-320

<!-- p.281 -->

 Property                    Microsoft Exchange                    Microsoft           WMSVC
                                                                   Exchange Server
                                                                   Auth Certificate

                                                                   was installed.      Manager service
                                                                                       was installed.

 Expires on (NotAfter)       5 years after NotBefore .             5 years after       10 years after
                                                                   NotBefore .         NotBefore .

 Public key size             2048                                  2048                2048
 (PublicKeySize)

 RootCAType                  Registry                              None                Registry

 Services                    IMAP, POP, IIS, SMTP                  SMTP                None

* These properties aren't visible in the standard view in the Exchange Management Shell. To see

them, you need to specify the property name (exact name or wildcard match) with the Format-
Table or Format-List cmdlets. For example:

      Get-ExchangeCertificate -Thumbprint <Thumbprint> | Format-List *

      Get-ExchangeCertificate -Thumbprint <Thumbprint> | Format-Table -Auto

     FriendlyName,*PrivateKey*

For more information, see Get-ExchangeCertificate.

Further details about the default self-signed certificates that are visible in Windows Certificate
Manger are described in the following table.

                                                                                        ﾉ     Expand table

 Property          Microsoft Exchange         Microsoft Exchange          WMSVC
                                              Server Auth Certificate

 Signature         sha256RSA1                 sha256RSA1                  sha256RSA1
 algorithm

 Signature hash    sha2561                    sha2561                     sha2561
 algorithm

 Key usage         Digital Signature, Key     Digital Signature, Key      Digital Signature, Key
                   Encipherment (a0)          Encipherment (a0)           Encipherment (a0), Data
                                                                          Encipherment (b0 00 00 00)

 Basic             Subject Type=End            Subject Type=End Entity    n/a
 constraints       Entity

<!-- p.282 -->

 Property          Microsoft Exchange   Microsoft Exchange        WMSVC
                                        Server Auth Certificate

                   Path Length          Path Length
                   Constraint=None      Constraint=None

 Thumbprint        sha2561              sha2561                   sha2561
 algorithm

1 Applies to fresh installations of Exchange 2016 Cumulative Update 22 or later and Exchange

2019 Cumulative Update 11 or later. For more information, see Exchange Server 2019 and 2016
certificates created during setup use SHA-1 hash   .

Typically, you don't use Windows Certificate Manger to manage Exchange certificates (use the
Exchange admin center or the Exchange Management Shell). Note that the WMSVC certificate
isn't an Exchange certificate.

<!-- p.283 -->

Certificate procedures in Exchange Server
Article • 04/30/2025

APPLIES TO:         2016       2019        Subscription Edition

Ensuring that certificates are installed and configured correctly is key to delivering a secure
messaging infrastructure for the enterprise. In Exchange Server you can manage certificates in
the Exchange admin center (EAC), and in the Exchange Management Shell. Certificate
management in the EAC has been improved over certificate management in the Exchange
Management Console in Exchange Server 2010. Specifically, certificate management in the EAC
can help administrators by:

        Minimizing the number of certificates that are required.

        Minimizing the interaction that's required for certificates.

        Allowing the centralized installation and management of certificates on all Exchange
        servers in the organization.

For more information about certificates in Exchange, see Digital certificates and encryption in
Exchange Server.

The tasks that are associated with certificate management in Exchange are described in the
following table.

                                                                                         ﾉ    Expand table

 Task               EAC                Exchange              Topic           Comments
                                       Management Shell

 Create a new       Servers >          New-                  Create a new    You can create new self-
 self-signed        Certificates >     ExchangeCertificate   Exchange        signed certificates and
 certificate on     select the                               Server self-    configure the certificates for
 an Exchange        server > Add                             signed          Exchange services in one
 server.                > Create a                           certificate     step.
                    self-signed
                    certificate

 Create a new       Servers >          New-                  Create an       The procedures are the same
 certificate        Certificates >     ExchangeCertificate   Exchange        for an internal CA (for
 request (also      select the         with the              Server          example, Active Directory
 known as a         server > Add       GenerateRequest       certificate     Certificate Services) or a
 certificate           > Create a      switch.               request for a   commercial CA.
 signing            request for a                            certification
 request or         certificate                              authority
 CSR) for a         from a

<!-- p.284 -->

Task              EAC               Exchange              Topic             Comments
                                    Management Shell

certification     certification
authority (CA).   authority

Complete a        Servers >         Import-               Complete a        After you receive the
pending           Certificates >    ExchangeCertificate   pending           certificate file or files from
certificate       select the                              Exchange          the CA, you install them on
request on an     server > select                         Server            the Exchange server.
Exchange          the certificate                         certificate
server.           request > click                         request
                  the Complete
                  link in the
                  details pane.

Assign a          Servers >         Enable-               Assign            The procedures are the same
certificate to    Certificates >    ExchangeCertificate   certificates to   for self-signed certificates, or
Exchange          select the                              Exchange          certificates that were issued
services.         server > select                         Server            by a CA.
                  the certificate                         services          For certificates issued by a
                  > Edit      >                                             CA, you can only assign the
                  Services tab.                                             certificates to Exchange
                                                                            services after you complete
                                                                            the pending certificate
                                                                            request (install the certificate
                                                                            on the Exchange server).

Delete an         Servers >         Remove-               n/a               The procedures are the same
existing          Certificates >    ExchangeCertificate                     for self-signed certificates,
certificate or    select the                                                certificate requests, or
certificate       server > select                                           certificates issued by a CA.
request from      the certificate
an Exchange       > Delete
server.

Renew an          Servers >         Get-                  Renew an          For self-signed certificates,
existing          Certificates >    ExchangeCertificate   Exchange          you renew the certificate in
certificate on    select the        and New-              Server            one step.
an Exchange       server > select   ExchangeCertificate   certificate       For certificates that were
server.           the certificate                                           issued by a CA, you create a
                  > click Renew                                             request to renew the
                  in the details                                            certificate, and send the
                  pane.                                                     request to the CA.
                                                                            The notification viewer in the
                                                                            EAC displays a warning when
                                                                            a certificate on any Exchange
                                                                            server in your organization is
                                                                            about to expire.

<!-- p.285 -->

Task               EAC                Exchange              Topic            Comments
                                      Management Shell

Export an          Servers >          Export-               Export a         You can only export valid
existing           Certificates >     ExchangeCertificate   certificate      (unexpired) certificates where
certificate or     select the                               from an          the PrivateKeyExportable
certificate        server > select                          Exchange         property has the value True .
request from       the certificate                          server           You can only export pending
an Exchange        > More                                                    certificate requests in the
server.            options       >                                           Exchange Management Shell.
                   Export                                                    You can't import an exported
                   Exchange                                                  pending certificate request.
                   Certificate

Import (install)   Servers >          Import-               Import or        Import a certificate that was
a certificate on   Certificates >     ExchangeCertificate   install a        exported from another
an Exchange        select the                               certificate on   server.
server.            server > More                            an Exchange
                   options       >                          server
                   Import
                   Exchange
                   Certificate

View existing      Servers >          Get-                  n/a              Some certificate properties
certificates or    Certificates >     ExchangeCertificate                    are visible in the details pane
certificate        select the                                                in the EAC when you select
requests on an     server                                                    the certificate or certificate
Exchange           For details on a                                          request from the list.
server, or view    specific                                                  Some certificate properties
the details for    certificate or                                            aren't visible in the standard
a specific         certificate                                               view in the Exchange
certificate or     request, select                                           Management Shell. To see
certificate        the item from                                             them, you need to specify
request.           the list, and                                             the property name (exact
                   then click Edit                                           name or wildcard match)
                      .                                                      with the Format-Table or
                                                                             Format-List cmdlets. For
                                                                             more information, see Get-
                                                                             ExchangeCertificate.

<!-- p.286 -->

Create an Exchange Server certificate
request for a certification authority
Article • 04/30/2025

APPLIES TO:        2016       2019    Subscription Edition

Creating a certificate request is the first step in installing a new certificate on an Exchange
server to configure Transport Layer Security (TLS) encryption for one or more Exchange
services. You use a certificate request (also known as a certificate signing request or CSR) to
obtain a certificate from a certification authority (CA). The procedures are the same for
obtaining certificates from an internal CA (for example, Active Directory Certificate Services), or
from a commercial CA. After you create the certificate request, you send the results to the CA,
and the CA uses the information to issue the actual certificate, which you install later.

You can create certificate requests in the Exchange admin center (EAC) or in the Exchange
Management Shell. The New Exchange certificate wizard in the EAC can assist you in selecting
the host names that are required in the certificate.

What do you need to know before you begin?
      You need to be assigned permissions before you can perform this procedure or
      procedures. For more information on the permissions you need, see the "Client Access
      services security" entry in the Clients and mobile devices permissions article.

      Estimated time to complete: 5 minutes to complete the new certificate request. However,
      more time is required before the request leads to issuance of a certificate. For more
      information, see Next steps.

      You need to plan carefully to choose the type of certificate that you want, and the host
      names that are required in the certificate. For more information, see Digital certificates
      and encryption in Exchange Server.

      Verify the certificate request requirements of the CA. Exchange generates a PKCS #10
      request (.req) file that uses Base64 (default) or Distinguished Encoding Rules (DER)
      encoding, with an RSA public key that's 1024, 2048 (default), or 4096 bits. Encoding and
      public key options are only available in the Exchange Management Shell. For more
      information, see New-ExchangeCertificate.

      In the EAC, you need to store the certificate request file on a UNC path ( \\<Server>\
      <Share>\ or \\<LocalServerName>\c$\ ). In the Exchange Management Shell, you can

      specify a local path.

<!-- p.287 -->

   To learn how to open the Exchange Management Shell in your on-premises Exchange
   organization, see Open the Exchange Management Shell.

   For more information about keyboard shortcuts that may apply to the procedures in this
   article, see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Use the EAC to create a new certificate request

 ７ Note

 The Exchange Admin Center (EAC) can be used to manage certificates in Exchange Server
 2019 CU15 and later. For Exchange Server 2016 CU23 and Exchange Server 2019 CU12 to
 CU14, use the Exchange Management Shell (EMS) procedure.

 1. Open the EAC and navigate to Servers > Certificates.

 2. In the Select server drop-down list, select the Exchange server where you want to install
   the certificate, and then select Add    .

   The New Exchange certificate wizard opens.

 3. On the This wizard will create a new certificate or a certificate request file page, verify
   that Create a request for a certificate from a certification authority is selected, and then
   select Next.

      ７ Note

      To create a new self-signed certificate, see Create a new Exchange Server self-
      signed certificate.

 4. On the Friendly name for this certificate page, enter a descriptive name for the
   certificate, and then select Next.

 5. On the Request a wildcard certificate page, make one of the following choices:

<!-- p.288 -->

            If you want a wildcard certificate: Select Request a wildcard certificate, and enter
            the wildcard character (*) and the domain in the Root domain box, for example,
            *.contoso.com or *.eu.contoso.com. When you're finished, select Next.
            If you want a subject alternative name (SAN) certificate: Make no selections on this
            page, and select Next.
            If you want a certificate for a single host: Make no selections on this page, and
            select Next.

   6. In the Store certificate request on this server page, select Browse and select the
     Exchange server where you want to store the certificate request (where you want to install
     the certificate). Then, select OK and Next.

        ７ Note

        Steps 7 and 8 only apply to a request for a SAN certificate, or a certificate for a single
        host. If you selected Request a wildcard certificate, skip to Step 9.

The Specify the domains you want to be included in your certificate page appears. This page
is basically a worksheet that helps you to determine the internal and external host names that
are required in the certificate for the following Exchange services:

     Outlook on the web
     Offline address book generation (OAB)
     Exchange Web Services
     Exchange ActiveSync
     Autodiscover
     POP
     IMAP
     Outlook Anywhere

   7. Enter a value for each service based on the location (internal or external). Then, the wizard
     determines the host names that are required in the certificate, and the information is
     displayed on the next page.

   8. If you want to modify a value for a service, select Edit (   ) and enter the host name value
     that you want to use (or delete the value). When you're finished, select Next.

        ７ Note

<!-- p.289 -->

      If you've already determined the host name values that you need in the certificate,
      you don't need to fill out the information on this page. Instead, select Next to
      manually enter the host names on the next page.

   The Based on your selections, the following domains will be included in your certificate
   page appears. This page lists the host names that will be included in the certificate
   request. The host name that's used in the certificate's Subject box is bold, which can be
   hard to see if that host name is selected.

 9. Verify the host name entries that are required in the certificate by referring to the
   selections that you made on the previous page.

   If you don't want to consider this list of host names for inclusion in the certificate request,
   go to Step 10.

10. Ignore the values from the last page and add, edit, or remove host name values by
   performing the following steps: a. If you want a SAN certificate: To select the host name
   for the certificate's Subject field, select the value and select Set as common name (check
   mark). The value should now appear bold. b. If you want a certificate for a single host
   name: Select the other values one at a time and select Remove (       ).

      ７ Note

      You can't delete the bold host name value that will be used for the certificate's
      Subject box. First, you need to select or add a different host name, and then check
      the Set as common name box. The changes that you make on this page might be
      lost if you select the Back button.

11. On the Specify information about your organization page, enter the following values:

         Organization name
         Department name
         City/Locality
         State/Province
         Country/Region name

７ Note

These X.500 values are included in the certificate's Subject box. Although a value is
required in every field before you can proceed, the CA might not care about certain fields
(for example, Department name), while other fields are important (for example,

<!-- p.290 -->

  Country/Region name and Organization name). Check the Subject box requirements of
  your CA.

 12. When you're finished, select Next.

 13. On the Save the certificate request to the following file page, enter the UNC path and
     filename for the certificate request, for example,
      \\FileServer01\Data\ExchCertRequest.req . When you're finished, select Finish.

The certificate request appears in the list of Exchange certificates with a status value of
Pending. For more information on the next steps, see Next steps section.

Use the Exchange Management Shell to create a
new certificate request
To create a new request for a wildcard certificate, a SAN certificate, or a certificate for a single
host, use the following syntax:

     If you need to send the content of the certificate request file to the CA, use the following
     syntax to create a Base64 encoded request file:

        PowerShell

        $txtrequest = New-ExchangeCertificate -PrivateKeyExportable $True -
        GenerateRequest [-FriendlyName <DescriptiveName>] -SubjectName C=
        <CountryOrRegion>[,S=<StateOrProvince>,L=<LocalityOrCity>,O=
        <Organization>,OU=<Department>],CN=<HostNameOrFQDN> [-DomainName <Host1>,
        <Host2>...] [-KeySize <1024 | 2048 | 4096>] [-Server <ServerIdentity>]
        [System.IO.File]::WriteAllBytes('<FilePathOrUNCPath>\<FileName>.req',
        [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

     If you need to send the certificate request file to the CA, use the following syntax to create
     a DER encoded request file:

        PowerShell

        $binrequest = New-ExchangeCertificate -PrivateKeyExportable $True -
        GenerateRequest -BinaryEncoded [-FriendlyName <DescriptiveName>] -SubjectName
        C=<CountryOrRegion>[,S=<StateOrProvince>,L=<LocalityOrCity>,O=
        <Organization>,OU=<Department>],CN=<HostNameOrFQDN> [-DomainName <Host1>,
        <Host2>...] [-KeySize <1024 | 2048 | 4096>] [-Server <ServerIdentity>]
        [System.IO.File]::WriteAllBytes('<FilePathOrUNCPath>\<FileName>.pfx',
        $binrequest.FileData)

<!-- p.291 -->

  ７ Note

  The only required part of the X.500 SubjectName parameter value (the certificate's Subject
  box) to run the command is CN=<HostNameOrFQDN> . But, you should always include the C=
  <CountryOrRegion> value. Otherwise, you might not be able to renew the certificate. Check

  the Subject box requirements of your CA. If you don't use the KeySize parameter, the
  certificate request has a 2048-bit RSA public key. If you don't use the Server parameter,
  the command is run on the local Exchange server.

For detailed syntax and parameter information, see New-ExchangeCertificate.

Wildcard certificate request
These examples create certificate request files for wildcard certificates with the following
properties:

     SubjectName: *.contoso.com in the United States, which requires the value
      C=US,CN=*.contoso.com .

     RequestFile: \\FileServer01\Data\Contoso Wildcard Cert.<cer or pfx>
     FriendlyName: Contoso.com Wildcard Cert

To create a Base64 encoded request file for the wildcard certificate, run the following
command:

  PowerShell

  $txtrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest
  -FriendlyName "Contoso.com Wildcard Cert" -SubjectName "C=US,CN=*.contoso.com"
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Contoso Wildcard Cert.req',
  [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

To create a DER encoded request file for the wildcard certificate, run the following command:

  PowerShell

  $binrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest
  -BinaryEncoded -FriendlyName "Contoso.com Wildcard Cert" -SubjectName
  "C=US,CN=*.contoso.com"
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Contoso Wildcard Cert.pfx',
  $binrequest.FileData)

SAN certificate request

<!-- p.292 -->

These examples create certificate request files for SAN certificates with the following
properties:

     SubjectName: mail.contoso.com in the United States, which requires the value
      C=US,CN=mail.contoso.com . This CN value is automatically included in the DomainName

     parameter (the Subject Alternative Name field).
     Other Subject Alternative Name field values:
        autodiscover.contoso.com
        legacy.contoso.com
        mail.contoso.net
        autodiscover.contoso.net
        legacy.contoso.net
     RequestFile: \\FileServer01\Data\Contoso SAN Cert.<cer or pfx>
     FriendlyName: Contoso.com SAN Cert
     DomainName: Unquoted comma-separated list of domains

To create a Base64 encoded request file for the SAN certificate, run the following command:

  PowerShell

  $txtrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest
  -FriendlyName "Contoso.com SAN Cert" -SubjectName "C=US,CN=mail.contoso.com" -
  DomainName
  autodiscover.contoso.com,legacy.contoso.com,mail.contoso.net,autodiscover.contoso.
  net,legacy.contoso.net
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Contoso SAN Cert.req',
  [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

To create a DER encoded request file for the SAN certificate, run the following command:

  PowerShell

  $binrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest
  -BinaryEncoded -FriendlyName "Contoso.com SAN Cert" -SubjectName
  "C=US,CN=mail.contoso.com" -DomainName
  autodiscover.contoso.com,legacy.contoso.com,mail.contoso.net,autodiscover.contoso.
  net,legacy.contoso.net
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Contoso SAN Cert.pfx',
  $binrequest.FileData)

Single subject certificate request
These examples create certificate request files for single subject certificates with the following
properties:

<!-- p.293 -->

     SubjectName: mail.contoso.com in the United States, which requires the value
      C=US,CN=mail.contoso.com .

     RequestFile: \\FileServer01\Data\Mail.contoso.com Cert.<cer or pfx>
     FriendlyName: Mail.contoso.com Cert

To create a Base64 encoded request file for the single subject certificate, run the following
command:

  PowerShell

  $txtrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest
  -FriendlyName "Mail.contoso.com Cert" -SubjectName "C=US,CN=mail.contoso.com"
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Mail.contoso.com Cert.req',
  [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

To create a DER encoded request file for the single subject certificate, run the following
command:

  PowerShell

  $binrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest
  -BinaryEncoded -FriendlyName "Mail.contoso.com Cert" -SubjectName
  "C=US,CN=mail.contoso.com"
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Mail.contoso.com Cert.pfx',
  $binrequest.FileData)

How do you know these commands worked?
To verify that you've successfully created a new certificate request, perform either of the
following steps:

     In the EAC at Servers > Certificates, verify whether the server where you stored the
     certificate request is selected. The request should be in the list of certificates with the
     Status parameter's value set as Pending request.

     In the Exchange Management Shell on the server where you stored the certificate request,
     run the following command:

        PowerShell

        Get-ExchangeCertificate | where {$_.Status -eq "PendingRequest" -and
        $_.IsSelfSigned -eq $false} | Format-List
        FriendlyName,Subject,CertificateDomains,Thumbprint

<!-- p.294 -->

Next steps
The content of a Base64 encoded certificate request file looks like the example described
below:

  text

  -----BEGIN NEW CERTIFICATE REQUEST-----
  MIIEBjCCAu4CAQAwYzEWMBQGA1UEAwwNKi5jb250b3NvLmNvbTELMAkGA1UECwwC
  SVQxEDAOBgNVBAoMB0NvbnRvc28xEDAOBgNVBAcMB1NlYXR0bGUxCzAJBgNVBAgM
  AldBMQswCQYDVQQGEwJVUzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
  ANZFK6JxcQMEBitJcEC82vCvr6251o28CMmrpIkl7Z0MnkCrU+BMTLBuZnIgaLvb
  jlzORvH6DP/dbyR8gQEAHVrXVWdr3AJIRbqQXWwN++BM5b2O6lIrA8w41XwGNu6r
  dtddi+POf8UYwot7PXw6wDsbKaTs1ePVK/0XdemdJCFIXNfCT8LY4p/KryQAyquo
  XDa+Acbx7TRxG2kXNAxgPGve+mvyCyizbugXAJIz4nugJ2k/X1kGYDc7f/b80tCv
  bPTcGCr09ScsbKmsQcqJ7UxiX2tScpO5AQxNxJHGL+bA6+96FBjPnFZaqPbFgI74
  N6hmZdSEDgQlaGfLEGjZBGMCAwEAAaCCAVwwGgYKKwYBBAGCNw0CAzEMFgo2LjEu
  NzYwMS4yMEwGCSqGSIb3DQEJDjE/MD0wDgYDVR0PAQH/BAQDAgWgMAwGA1UdEwEB
  /wQCMAAwHQYDVR0OBBYEFNRw1o74zcuGyky33rl7WChgdQrlMHIGCisGAQQBgjcN
  AgIxZDBiAgEBHloATQBpAGMAcgBvAHMAbwBmAHQAIABSAFMAQQAgAFMAQwBoAGEA
  bgBuAGUAbAAgAEMAcgB5AHAAdABvAGcAcgBhAHAAaABpAGMAIABQAHIAbwB2AGkA
  ZABlAHIDAQAwfAYJKwYBBAGCNxUUMW8wbQIBBQwrRVhIUi0zMjQ4LkVYSFItMzI0
  OGRvbS5leHRlc3QubWljcm9zb2Z0LmNvbQwXRVhIUi0zMjQ4RE9NXEVYSFItMzI0
  OCQMIk1pY3Jvc29mdC5FeGNoYW5nZS5TZXJ2aWNlSG9zdC5leGUwDQYJKoZIhvcN
  AQEFBQADggEBAL63qVj1m2mBz53+nilnlFweOlcltXoxaF28+Kf0hrJVbH5a2Jme
  tS0iKU8YXU3mZ3NnWco+5ea024f9awMIzg4z/heE5yEUFf9UtwRGSOc84r2QexPa
  zT/rveTTcbliKU0EFhporl3C2uuBCdAewyLj+/k0hABH3djnmMONG6NyC5f+wMun
  kkH5naiSLdsTYbq8jkWYuSqL0qdhtmauqWeAPpA0hKDkQk5eDWpOGx3mgxiaQumo
  Rqw6dmQ+o8TC+lE3Tvgdfv47A84X8H7Y9h8liS4h0OfbsgEQb8LcM0YHD6yvPgcD
  JCmt8A7JFHF9u6mghjiKlXaZ/i+2l10Wsu8=
  -----END NEW CERTIFICATE REQUEST-----

You need to send this information to the CA. How you send it depends on the CA, but typically,
you send the contents of the file in an email message or in the certificate request form on the
CA's website.

If the CA requires a binary certificate request that's encoded by DER (you used the New-
ExchangeCertificate cmdlet with the BinaryEncoded switch), you typically send the whole
certificate request file to the CA.

After you receive the certificate from the CA, you need to complete the pending certificate
request. For more information, see Complete a pending Exchange Server certificate request.

<!-- p.295 -->

Complete a pending Exchange Server
certificate request
Article • 04/30/2025

APPLIES TO:         2016      2019      Subscription Edition

Completing a pending certificate request (also known as a certificate signing request or CSR) is
the next step in configuring Transport Layer Security (TLS) encryption in Exchange Server. After
you receive the certificate from the certification authority (CA), you install the certificate on the
Exchange server to complete the pending certificate request.

You can complete a pending certificate request in the Exchange admin center (EAC) or in the
Exchange Management Shell. The procedures are the same for completing new certificate
requests or certificate renewal requests. The procedures are also the same for certificates that
were issued by an internal CA (for example, Active Directory Certificate Services), or a
commercial CA.

You might receive one or more of the following types of certificate files CA:

      PKCS #12 certificate files: These are binary certificate files that have .cer, .crt, .der, .p12, or
      .pfx filename extensions, and require a password when the file contains the private key or
      chain of trust. The CA might issue you only one binary certificate file that you need to
      install (protected by a password), or multiple root or intermediate binary certificate files
      that you also need to install.

      PKCS #7 certificate files: These are text certificate files that have .p7b or .p7c filename
      extensions. These files contain the text: -----BEGIN CERTIFICATE----- and -----END
      CERTIFICATE----- or -----BEGIN PKCS7----- and -----END PKCS7----- . If the CA includes

      a chain of certificates file with your binary certificate file, you also need to install the chain
      of certificates file.

  ７ Note

  The Exchange Admin Center (EAC) can be used to manage certificates in Exchange Server
  2019 CU15 and later. For Exchange Server 2016 CU23 and Exchange Server 2019 CU12 to
  CU14, use the Exchange Management Shell (EMS) procedure.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

<!-- p.296 -->

   The procedures in this topic require you to have created a new certificate request on the
   Exchange server, sent the certificate request to the CA, and received the certificate from
   the CA. For more information, see Create an Exchange Server certificate request for a
   certification authority.

   In the EAC, you need to retrieve the certificate file from a UNC path ( \\<Server>\<Share>
   or \\<LocalServerName>\c$\ ). In the Exchange Management Shell, you can use a local file
   path.

   If you renew or replace a certificate that was issued by a CA on a subscribed Edge
   Transport server, you need to remove the old certificate, and then delete and recreate the
   Edge Subscription. For more information, see Edge Subscription process.

   To learn how to open the Exchange Management Shell in your on-premises Exchange
   organization, see Open the Exchange Management Shell.

   You need to be assigned permissions before you can perform this procedure or
   procedures. To see what permissions you need, see the "Client Access services security"
   entry in the Clients and mobile devices permissions topic.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online        , or Exchange Online Protection .

Use the EAC to create complete a pending
certificate request
 1. Open the EAC and navigate to Servers > Certificates.

 2. In the Select server list, select the Exchange server that holds the pending certificate
   request.

 3. A pending certificate request has the following properties:

           In the list of certificates, the value of the Status field is Pending request.

           When you select the certificate request from the list, there's a Complete link in the
           details pane.

<!-- p.297 -->

     Select the pending certificate request that you want to complete, and then click Complete
     in the details pane.

   4. On the Complete pending request page that opens, in the File to import from field,
     enter the UNC path and filename for the certificate file. For example,
      \\FileServer01\Data\ContosoCert.cer . When you're finished, click OK.

The certificate request becomes a certificate in the list of Exchange certificates with a Status
value of Valid. For next steps, see the Next steps section.

Use the Exchange Management Shell to complete
a pending certificate request
To complete a pending certificate request, use the following syntax:

  PowerShell

  Import-ExchangeCertificate -FileData
  ([System.IO.File]::ReadAllBytes('<FilePathOrUNCPath>')) [-Password (Read-Host
  "Enter password" -AsSecureString)] [-PrivateKeyExportable <$true | $false>] [-
  Server <ServerIdentity>]

You use this syntax with the following types of certificate files:

     Binary certificate files (PKCS #12 files that have .cer, .crt, .der, .p12, or .pfx filename
     extensions).
     Chain of certificates files (PKCS #7 text files that have .p7b or .p7c filename extensions).

This example imports the binary certificate file \\FileServer01\Data\Contoso Cert.cer that's
protected on the local Exchange server. You're prompted to enter the password.

  PowerShell

  Import-ExchangeCertificate -FileData
  ([System.IO.File]::ReadAllBytes('\\FileServer01\Data\Contoso Cert.cer')) -Password
  (Read-Host "Enter password" -AsSecureString)

This example imports the text certificate file \\FileServer01\Data\Chain of Certificates.p7b
on the local Exchange server.

  PowerShell

  Import-ExchangeCertificate -FileData

<!-- p.298 -->

  ([System.IO.File]::ReadAllBytes('\\FileServer01\Data\Chain of Certificates.p7b'))

Notes:

     The FileData parameter accepts local paths if the certificate file is located on the
     Exchange server where you're running the command, and this is the same server where
     you want to import the certificate. Otherwise, use a UNC path.
     If you want to be able to export the certificate from the server where you're importing it,
     you need to use the PrivateKeyExportable parameter with the value $true .
     For more information, see Import-ExchangeCertificate.

How do you know this worked?
To verify that you have successfully completed the certificate request and installed the
certificate on the Exchange server, use either of the following procedures:

     In the EAC at Servers > Certificates, verify the server where you installed the certificate is
     selected. In the list of certificates, verify that the certificate has Status property value
     Valid.

     In the Exchange Management Shell on the server where you installed the certificate, run
     the following command and verify that the certificate is listed:

         PowerShell

         Get-ExchangeCertificate | where {$_.Status -eq "Valid" -and $_.IsSelfSigned -
         eq $false} | Format-List FriendlyName,Subject,CertificateDomains,Thumbprint

Next steps
After you complete the pending certificate request by installing the certificate on the server,
you need to assign the certificate to one or more Exchange services before the Exchange server
is able to use the certificate for encryption. For more information, see Assign certificates to
Exchange services.

<!-- p.299 -->

Assign certificates to Exchange Server
services
Article • 04/30/2025

APPLIES TO:        2016       2019      Subscription Edition

After you install a certificate on an Exchange server, you need to assign the certificate to one or
more Exchange services before the Exchange server is able to use the certificate for encryption.
You can assign certificates to services in the Exchange admin center (EAC) or in the Exchange
Management Shell. Once you assign a certificate to a service, you can't remove the assignment.
If you no longer want to use a certificate for a specific service, you need to assign another
certificate to the service, and then remove the certificate that you don't want to use.

The available Exchange services are described in the following table.

                                                                                         ﾉ    Expand table

 Service               Uses

 IIS                   TLS encryption for internal and external client connections that use HTTP. This
                       includes:
                       Autodiscover
                       Exchange ActiveSync
                       Exchange admin center
                       Exchange Web Services
                       Offline address book (OAB) distribution
                       Outlook Anywhere (RPC over HTTP)
                       Outlook MAPI over HTTP
                       Outlook on the web

 IMAP                  TLS encryption for IMAP4 client connections.
                       Don't assign a wildcard certificate to the IMAP4 service. Instead, use the Set-
                       ImapSettings cmdlet to configure the fully qualified domain name (FQDN) that
                       clients use to connect to the IMAP4 service.

 POP                   TLS encryption for POP3 client connections.
                       Don't assign a wildcard certificate to the POP3 service. Instead, use the Set-
                       PopSettings cmdlet to configure the FQDN that clients use to connect to the
                       POP3 service.

 SMTP                  TLS encryption for external SMTP client and server connections.
                       Mutual TLS authentication between Exchange and other messaging servers.
                       When you assign a certificate to SMTP, you're prompted to replace the default
                       Exchange self-signed certificate that's used to encrypt SMTP communication
                       between internal Exchange servers. Typically, you don't need to replace the default
                       SMTP certificate.

<!-- p.300 -->

Service             Uses

Unified Messaging   TLS encryption for client connections to the backend UM service on Exchange
(UM)                2016 Mailbox servers.
                    You can only assign a certificate to the UM service when the UM startup mode
                    property of the service is set to TLS or Dual. If the UM startup mode is set to the
                    default value TCP, you can't assign the certificate to the UM service. (Note: UM is
                    not available in Exchange 2019). For more information, see Configure the Startup
                    Mode on a Mailbox Server.

Unified Messaging   TLS encryption for client connections to the UM Call Router service in the Client
Call Router         Access services on Exchange 2016 Mailbox servers.
(UMCallRouter)      You can only assign a certificate to the UM Call Router service when the UM
                    startup mode property of the service is set to TLS or Dual. If the UM startup mode
                    is set to the default value TCP, you can't assign the certificate to the UM Call
                    Router service. (Note: UM is not available in Exchange 2019). For more
                    information, see Configure the Startup Mode on a Client Access Server.

What do you need to know before you begin?
    Estimated time to complete: 5 minutes.

    After you do the procedures in this topic, you might need to restart Internet Information
    Services (IIS). In some scenarios, Exchange might continue to use the previous certificate
    for encrypting and decrypting the cookie that's used for Outlook on the web (formerly
    known as Outlook Web App) authentication. We recommend restarting IIS in
    environments that use Layer 4 load balancing.

    If you renew or replace a certificate that was issued by a CA on a subscribed Edge
    Transport server, you need to remove the old certificate, and then delete and recreate the
    Edge Subscription. For more information, see Edge Subscription process.

    To learn how to open the Exchange Management Shell in your on-premises Exchange
    organization, see Open the Exchange Management Shell.

    You need to be assigned permissions before you can perform this procedure or
    procedures. To see what permissions you need, see the "Client Access services security"
    entry in the Clients and mobile devices permissions topic.

    For information about keyboard shortcuts that may apply to the procedures in this topic,
    see Keyboard shortcuts in the Exchange admin center.

  Tip

<!-- p.301 -->

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

Use the EAC to assign a certificate to Exchange
services
   1. Open the EAC, and navigate to Servers > Certificates.

   2. In the Select server list, select the Exchange server that holds the certificate.

   3. Select the certificate that you want to configure, and then click Edit     . The certificate
     needs to have the Status value Valid.

   4. On the Services tab, in the Specify the services you want to assign this certificate to
     section, select the services. Remember, you can add services, but you can't remove them.
     When you're finished, click Save.

Use the Exchange Management Shell to assign a
certificate to Exchange services
To assign a certificate to Exchange services, use the following syntax:

  PowerShell

  Enable-ExchangeCertificate -Thumbprint <Thumbprint> -Services <Service1>,
  <Service2>... [-Server <ServerIdentity>]

This example assigns the certificate that has the thumbprint value
434AC224C8459924B26521298CE8834C514856AB to the POP, IMAP, IIS, and SMTP services.

  PowerShell

  Enable-ExchangeCertificate -Thumbprint 434AC224C8459924B26521298CE8834C514856AB -
  Services POP,IMAP,IIS,SMTP

You can find the certificate thumbprint value by using the Get-ExchangeCertificate cmdlet.

How do you know this worked?

<!-- p.302 -->

To verify that you have successfully assigned a certificate to one or more Exchange services, use
either of the following procedures:

     In the EAC at Servers > Certificates, verify the server where you installed the certificate is
     selected. Select the certificate, and in the details pane, verify that the Assigned to services
     property contains the services that you selected.

     In the Exchange Management Shell on the server where you installed the certificate, run
     the following command to verify the Exchange services for the certificate:

       PowerShell

        Get-ExchangeCertificate | Format-List
        FriendlyName,Subject,CertificateDomains,Thumbprint,Services

<!-- p.303 -->

Create a new Exchange Server self-signed
certificate
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

When you install Exchange Server, a self-signed certificate that's created and signed by the
Exchange server itself is automatically installed on the server. However, you can also create
additional self-signed certificates that you can use.

You can create self-signed certificates certificate in the Exchange admin center (EAC) or in the
Exchange Management Shell.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      Exchange self-signed certificates work well for encrypting communication between
      internal Exchange servers, but not so well for encrypting external connections, because
      clients, servers, and services don't automatically trust Exchange self-signed certificates. To
      create a certificate request (also known as a certificate signing request or CSR) for a
      commercial certification authority that's automatically trusted by all clients, servers, and
      services, see Create an Exchange Server certificate request for a certification authority.

      When you create a new self-signed certificate by using the New-ExchangeCertificate
      cmdlet, you can assign the certificate to Exchange services during the creation of the
      certificate. For more information about the Exchange services, see Assign certificates to
      Exchange Server services.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Client Access services security"
      entry in the Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

<!-- p.304 -->

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online, or Exchange Online Protection .

Use the EAC to create a new Exchange self-signed
certificate
 1. Open the EAC and navigate to Servers > Certificates.

 2. In the Select server list, select the Exchange server where you want to install the
   certificate, and then click Add     .

 3. The New Exchange certificate wizard opens. On the This wizard will create a new
   certificate or a certificate request file page, select Create a self-signed certificate, and
   then click Next.

   Note: To create a new certificate request for a certificate authority, see Create an
   Exchange Server certificate request for a certification authority.

 4. On the Friendly name for this certificate page, enter a friendly name for the certificate,
   and then click Next.

 5. In the Specify the servers you want to apply this certificate to page, click Add

   On the Select a server page that opens, select the Exchange server where you want to
   install the certificate, and click Add - >. Repeat this step as many times as necessary.
   When you're finished selecting servers, click OK.

   When you're finished, click Next.

 6. The Specify the domains you want to be included in your certificate page is basically a
   worksheet that helps you determine the internal and external host names that are
   required in the certificate for the following Exchange services:

         Outlook on the web

         Offline address book generation (OAB)

         Exchange Web Services

         Exchange ActiveSync

         Autodiscover

         POP

<!-- p.305 -->

           IMAP

           Outlook Anywhere

           If you enter a value for each service based on the location (internal or external), the
           wizard determines the host names that are required in the certificate, and the
           information is displayed on the next page. To modify a value for a service, click Edit (
               ) and enter the host name value that you want to use (or delete the value). When
           you're finished, click Next.

           If you've already determined the host name values that you need in the certificate,
           you don't need to fill out the information on this page. Instead, click Next to
           manually enter the host names on the next page.

   7. The Based on your selections, the following domains will be included in your certificate
     page lists the host names that will be included in the self-signed certificate. The host
     name that's used in the certificate's Subject field is bold, which can be hard to see if that
     host name is selected. You can verify the host name entries that are required in the
     certificate based on the selections that you made on the previous page. Or, you can
     ignore the values from the last page and add, edit, or remove host name values.

           If you want a SAN certificate, the Subject field still requires one common name (CN)
           value. To select the host name for the certificate's Subject field, select the value and
           click Set as common name (check mark). The value should now appear bold.

           If you want a certificate for a single host name, select the other values one at a time
           and click Remove (    ).

           When you're finished on this page, click Finish.

     Notes:

           You can't delete the bold host name value that will be used for the certificate's
           Subject field. First, you need to select or add a different host name, and then click
           Set as common name (check mark).
           The changes that you make on this page might be lost if you click the Back button.

Use the Exchange Management Shell to create a
new Exchange self-signed certificate
To create a new Exchange self-signed certificate, use the following syntax:

  PowerShell

<!-- p.306 -->

  New-ExchangeCertificate [-FriendlyName <DescriptiveName>] [-SubjectName [C=
  <CountryOrRegion>,S=<StateOrProvince>,L=<LocalityOrCity>,O=<Organization>,OU=
  <Department>],CN=<HostNameOrFQDN>]] [-DomainName <Host1>,<Host2>...] [-Services
  <None | IIS | IMAP | POP | SMTP | UM | UMCallRouter> [-PrivateKeyExportable <
  $true | $false>] [-Server <ServerIdentity>] -[Force]

This example creates a self-signed certificate on the local Exchange server with the following
properties:

     Subject: <ServerName>. For example, if you run the command on the server named
     Mailbox01, the value is Mailbox01 .
     Subject alternative names: <ServerName>, <Server FQDN>. For example, Mailbox01,
     Mailbox01.contoso.com .
     Friendly name: Microsoft Exchange
     Services: POP, IMAP, SMTP.

  PowerShell

  New-ExchangeCertificate

This example creates a creates a self-signed certificate on the local Exchange server with the
following properties:

     Subject: Exchange01, which requires the value CN=Exchange01 . Note that this value is
     automatically included in the DomainName parameter (the Subject Alternative Name
     field).
     Additional subject alternative names:
        mail.contoso.com
        autodiscover.contoso.com
        Exchange01.contoso.com
        Exchange02.contoso.com
     Services: SMTP, IIS
     Friendly name: Contoso Exchange Certificate
     The private key is exportable. This allows you to export the certificate from the server (and
     import it on other servers).

  PowerShell

  New-ExchangeCertificate -FriendlyName "Contoso Exchange Certificate" -SubjectName
  CN=Exchange01 -DomainName
  mail.contoso.com,autodiscover.contoso.com,Exchange01.contoso.com,Exchange02.contos
  o.com -Services SMTP,IIS -PrivateKeyExportable $true

<!-- p.307 -->

Notes:

     The only required part of the X.500 SubjectName parameter value (the certificate's
     Subject field) is CN=<HostNameOrFQDN> .
     Some Services parameter values generate warning or confirmation messages. For more
     information, see Assign certificates to Exchange Server services.
     For more information, see New-ExchangeCertificate.

How do you know this worked?
To verify that you have successfully created an Exchange self-signed certificate, perform either
of the following steps:

     In the EAC at Servers > Certificates, verify the server where you created the self-signed
     certificate is selected. The certificate should be in the list of certificates with the Status
     value Valid.

     In the Exchange Management Shell on the server where you created the self-signed
     certificate, run the following command and verify the properties:

         PowerShell

         Get-ExchangeCertificate | where {$_.Status -eq "Valid" -and $_.IsSelfSigned -
         eq $true} | Format-List
         FriendlyName,Subject,CertificateDomains,Thumbprint,NotBefore,NotAfter

<!-- p.308 -->

Renew an Exchange Server certificate
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Every certificate has a built-in expiration date. In Exchange Server, the default self-signed
certificate that's installed on the Exchange server expires 5 years after Exchange was installed
on the server. You can use the Exchange admin center (EAC) or the Exchange Management
Shell to renew Exchange certificates. This includes Exchange self-signed certificates, and
certificates that were issued by a certification authority (CA).

  ７ Note

  The Exchange Admin Center (EAC) can be used to manage certificates in Exchange Server
  2019 CU15 and later. For Exchange Server 2016 CU23 and Exchange Server 2019 CU12 to
  CU14, use the Exchange Management Shell (EMS) procedure.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      For certificates that were issued by a CA, verify the certificate request requirements of the
      CA. Exchange generates a PKCS #10 request (.req) file that uses Base64 encoding (default)
      or Distinguished Encoding Rules (DER), with an RSA public key that's 1024, 2048 (default),
      or 4096 bits. Note that encoding and public key options are only available in the
      Exchange Management Shell.

      To renew a certificate that was issued by a CA, you need to renew the certificate with the
      same CA that issued the certificate. If you're changing CAs, or if there's a problem with
      the original certificate when you try to renew it, you need to create a new certificate
      request (also known as a certificate signing request or CSR) for a new certificate. For more
      information, see Create an Exchange Server certificate request for a certification authority.

      If you renew or replace a certificate that was issued by a CA on a subscribed Edge
      Transport server, you need to remove the old certificate, and then delete and recreate the
      Edge Subscription. For more information, see Edge Subscription process.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Client Access services security"

<!-- p.309 -->

     entry in the Clients and mobile devices permissions topic.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online        , or Exchange Online Protection .

Renew a certificate that was issued by a
certification authority
The procedures are the same for certificates that were issued by an internal CA (for example,
Active Directory Certificate Services), or a commercial CA.

To renew a certificate that was issued by a CA, you create a certificate renewal request, and
then you send the request to the CA. The CA then sends you the actual certificate file that you
need to install on the Exchange server. The procedure is nearly identical to that of completing a
new certificate request by installing the certificate on the server. For instructions, see Complete
a pending Exchange Server certificate request.

Use the EAC to create a certificate renewal request for a
certification authority
   1. Open the EAC and navigate to Servers > Certificates.

   2. In the Select server list, select the Exchange server that holds the certificate that you want
     to renew.

   3. All valid certificates have a Renew link in the details pane that's visible when you select
     the certificate from the list. Select the certificate that you want to renew, and then click
     Renew in the details pane.

   4. On the Renew Exchange certificate page that opens, in the Save the certificate request
     to the following file field, enter the UNC path and filename for the new certificate
     renewal request file. For example, \\FileServer01\Data\ContosoCertRenewal.req . When
     you're finished, click OK.

The certificate request appears in the list of Exchange certificates with a status value of
Pending.

<!-- p.310 -->

Use the Exchange Management Shell to create a certificate
renewal request for a certification authority
To create a new certificate renewal request for a certification authority, use the following
syntax:

     If you need to send the content of the certificate renewal request file to the CA, use the
     following syntax to create a Base64 encoded request file:

          PowerShell

          $txtrequest = Get-ExchangeCertificate -Thumbprint <Thumbprint> | New-
          ExchangeCertificate -GenerateRequest [-KeySize <1024 | 2048 | 4096>] [-Server
          <ServerIdentity>]
          [System.IO.File]::WriteAllBytes('<FilePathOrUNCPath>\<FileName>.req',
          [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

     If you need to send the certificate renewal request file to the CA, use the following syntax
     to create a DER encoded request file:

          PowerShell

          $binrequest = Get-ExchangeCertificate -Thumbprint <Thumbprint> | New-
          ExchangeCertificate -GenerateRequest -BinaryEncoded [-KeySize <1024 | 2048 |
          4096>] [-Server <ServerIdentity>]
          [System.IO.File]::WriteAllBytes('<FilePathOrUNCPath>\<FileName>.pfx',
          $binrequest.FileData)

To find the thumbprint value of the certificate that you want to renew, run the following
command:

  PowerShell

  Get-ExchangeCertificate | where {$_.Status -eq "Valid" -and $_.IsSelfSigned -eq
  $false} | Format-List
  FriendlyName,Subject,CertificateDomains,Thumbprint,NotBefore,NotAfter

For detailed syntax and parameter information, see Get-ExchangeCertificate and New-
ExchangeCertificate.

Notes:

     If you don't use the KeySize parameter, the certificate request has a 2048 bit RSA public
     key.
     If you don't use the Server parameter, the command is run the local Exchange server.

<!-- p.311 -->

This example creates a Base64 encoded certificate renewal request for the existing certificate
with the Thumbprint value 5DB9879E38E36BCB60B761E29794392B23D1C054 :

  PowerShell

  $txtrequest = Get-ExchangeCertificate -Thumbprint
  5DB9879E38E36BCB60B761E29794392B23D1C054 | New-ExchangeCertificate -
  GenerateRequest
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\ContosoCertRenewal.req',
  [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

This example creates a DER (binary) encoded certificate renewal request for the same
certificate:

  PowerShell

  $binrequest = Get-ExchangeCertificate -Thumbprint <Thumbprint> | New-
  ExchangeCertificate -GenerateRequest -BinaryEncoded
  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\ContosoCertRenewal.pfx',
  $binrequest.FileData)

How do you know that you successfully created a certificate
renewal request?
To verify that you have successfully created a certificate renewal request for a certification
authority, perform either of the following steps:

      In the EAC at Servers > Certificates, verify the server where you stored the certificate
      request is selected. The request should be in the list of certificates with the Status value
      Pending request.

      In the Exchange Management Shell on the server where you stored the certificate request,
      run the following command:

         PowerShell

         Get-ExchangeCertificate | where {$_.Status -eq "PendingRequest" -and
         $_.IsSelfSigned -eq $false} | Format-List
         FriendlyName,Subject,CertificateDomains,Thumbprint

Renew an Exchange self-signed certificate
When you renew an Exchange self-signed certificate, you're basically making a new certificate.

<!-- p.312 -->

Use the EAC to renew an Exchange self-signed certificate
   1. Open the EAC and navigate to Servers > Certificates.

   2. In the Select server list, select the Exchange server that holds the certificate that you want
     to renew.

   3. All valid certificates have a Renew link in the details pane that's visible when you select
     the certificate from the list. Select the certificate that you want to renew, and then click
     Renew in the details pane.

   4. On the Renew Exchange certificate page that opens, verify the read-only list of Exchange
     services that the existing certificate is assigned to, and then click OK.

Use the Exchange Management Shell to renew an Exchange
self-signed certificate
To renew a self-signed certificate, use the following syntax:

  PowerShell

  Get-ExchangeCertificate -Thumbprint <Thumbprint> | New-ExchangeCertificate [-
  Force] [-PrivateKeyExportable <$true | $false>]

To find the thumbprint value of the certificate that you want to renew, run the following
command:

  PowerShell

  Get-ExchangeCertificate | where {$_.IsSelfSigned -eq $true} | Format-List
  FriendlyName,Subject,CertificateDomains,Thumbprint,NotBefore,NotAfter

This example renews a self-signed certificate on the local Exchange server, and uses the
following settings:

     The thumbprint value of the existing self-signed certificate to renew is
      BC37CBE2E59566BFF7D01FEAC9B6517841475F2D

     The Force switch replaces the original self-signed certificate without a confirmation
     prompt.
     The private key is exportable. This allows you to export the certificate and import it on
     other servers.

  PowerShell

<!-- p.313 -->

  Get-ExchangeCertificate -Thumbprint BC37CBE2E59566BFF7D01FEAC9B6517841475F2D |
  New-ExchangeCertificate -Force -PrivateKeyExportable $true

How do you know that you've successfully renewed an
Exchange self-signed certificate?
To verify that you have successfully renewed an Exchange self-signed certificate, use either of
the following procedures:

     In the EAC at Servers > Certificates, verify the server where you installed the certificate is
     selected. In the list of certificates, verify that the certificate has Status property value
     Valid.

     In the Exchange Management Shell on the server where you renewed the self-signed
     certificate, run the following command to verify the property values:

  PowerShell

  Get-ExchangeCertificate | where {$_.Status -eq "Valid" -and $_.IsSelfSigned -eq
  $true} | Format-List
  FriendlyName,Subject,CertificateDomains,Thumbprint,NotBefore,NotAfter

  ） Important

  Removing, renewing, or assigning services to the certificate can remove the certificate
  from Exchange Back End and Default Web Site. It's essential that you check the certificate
  bindings and apply the correct certificates.

Additional resources
Unable to open OWA, ECP, or EMS after a self-signed certificate is removed from the Exchange
Back End website

<!-- p.314 -->

Export a certificate from an Exchange
server
Article • 04/30/2025

APPLIES TO:        2016      2019     Subscription Edition

You can export a certificate from an Exchange server as a backup or to import the certificate on
other clients, devices or servers. You can export certificates in the Exchange admin center (EAC)
or in the Exchange Management Shell. The resulting certificate file is a password-protected
binary PKCS #12 file that contains the certificate's private key, and is suitable for importing
(installing) on other servers.

  ７ Note

  The Exchange Admin Center (EAC) can be used to manage certificates in Exchange Server
  2019 CU15 and later. For Exchange Server 2016 CU23 and Exchange Server 2019 CU12 to
  CU14, use the Exchange Management Shell (EMS) procedure.

What do you need to know before you begin?
      Estimated time to complete: 5 minutes.

      In the EAC, you need to export the certificate file to a UNC path ( \\<Server>\<Share>\ or
      \\<LocalServerName>\c$\ ). In the Exchange Management Shell, you can specify a local

      path.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Client Access services security"
      entry in the Clients and mobile devices permissions topic.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection .

<!-- p.315 -->

Use the EAC to export a certificate
   1. Open the EAC and navigate to Servers > Certificates.

   2. In the Select server list, select the Exchange server that contains the certificate, click More
     options     , and select Export Exchange certificate.

   3. On the Export Exchange certificate page that opens, enter the following information:

            File to export to: Enter the UNC path and file name of the certificate file. For
            example, \\FileServer01\Data\Fabrikam.pfx

            Password: When you export the certificate with its private key, you need to specify a
            password. Exporting the certificate with its private key allows you to import the
            certificate on other servers.

     When you're finished, click OK.

Use the Exchange Management Shell to export a
certificate
To export a binary certificate file that you can import on other clients or servers, use the
following syntax:

  PowerShell

  $cert = Export-ExchangeCertificate -Thumbprint <Thumbprint> -BinaryEncoded -
  Password (Read-Host "Enter password" -AsSecureString) [-Server <ServerIdentity>]

  [System.IO.File]::WriteAllBytes('<FilePathOrUNCPath>\<FileName>.pfx',
  $cert.FileData)

This example exports a certificate from the local Exchange server to a file with the following
settings:

     The certificate that has the thumbprint value 5113ae0233a72fccb75b1d0198628675333d010e
     is exported to the file C:\Data\Fabrikam.pfx on the same server where you're running the
     command.
     The exported certificate file is encoded by DER (not Base64).
     You're prompted to enter the password.

  PowerShell

<!-- p.316 -->

  $cert = Export-ExchangeCertificate -Thumbprint
  5113ae0233a72fccb75b1d0198628675333d010e -BinaryEncoded -Password (Read-Host
  "Enter password" -AsSecureString)

  [System.IO.File]::WriteAllBytes('C:\Data\Fabrikam.pfx', $cert.FileData)

To export a pending certificate request (also known as a certificate signing request or CSR), use
the following syntax:

  PowerShell

  $txtcert = Export-ExchangeCertificate -Thumbprint <Thumbprint> [-Server
  <ServerName>]

  [System.IO.File]::WriteAllBytes('<FilePathOrUNCPath>\<FileName>.req',
  [System.Text.Encoding]::Unicode.GetBytes($txtcert))

This example exports a pending certificate request from the local Exchange server to a file with
the following settings:

     The certificate that has the thumbprint value 72570529B260E556349F3403F5CF5819D19B3B58
     is exported to the file \\FileServer01\Data\Fabrikam.req .
     The exported certificate file is Base64 encoded.

  PowerShell

  $txtcert = Export-ExchangeCertificate -Thumbprint
  72570529B260E556349F3403F5CF5819D19B3B58

  [System.IO.File]::WriteAllBytes('\\FileServer01\Data\Fabrikam.req',
  [System.Text.Encoding]::Unicode.GetBytes($txtcert))

For detailed syntax and parameter information, see Export-ExchangeCertificate.

  ７ Note

        You can export a pending certificate request if you need to resubmit the certificate
        request to the certification authority and you can't find the original certificate
        request file.
        When you export a certificate request, you typically don't need to use the Password
        parameter or the BinaryEncoded switch, and you save the request to a .req file.
        You can't import an exported pending certificate request on another server.

<!-- p.317 -->

How do you know this worked?
To verify that you have successfully exported a certificate from an Exchange server, try
importing the certificate file on another server. For more information, see Import or install a
certificate on an Exchange server.

<!-- p.318 -->

Import or install a certificate on an
Exchange server
Article • 04/30/2025

APPLIES TO:         2016     2019       Subscription Edition

To enable encryption for one or more Exchange services, the Exchange server needs to use a
certificate. SMTP communication between internal Exchange servers is encrypted by the default
self-signed certificate that's installed on the Exchange server. To encrypt communication with
internal or external clients, servers, or services, you'll likely want to use a certificate that's
automatically trusted by all clients, services and servers that connect to your Exchange
organization. For more information, see Certificate requirements for Exchange services.

You can import (install) certificates on Exchange servers in the Exchange admin center (EAC) or
in the Exchange Management Shell.

These are the types of certificate files that you can import on an Exchange server:

      PKCS #12 certificate files: These are binary certificate files that have .cer, .crt, .der, .p12, or
      .pfx filename extensions, and require a password when the file contains the private key or
      chain of trust. Examples of these types of files include:

         Self-signed certificates that were exported from other Exchange servers by using the
         EAC or the Export-ExchangeCertificate with the PrivateKeyExportable parameter value
         $true . For more information, see Export a certificate from an Exchange server.

         Certificates that were issued by a certification authority (an internal CA like Active
         Directory Certificate Services, or a commercial CA).

         Certificates that were exported from other servers (for example, Skype for Business
         Server).

      PKCS #7 certificate files: These are text certificate files that have .p7b or .p7c filename
      extensions. These files contain the text: -----BEGIN CERTIFICATE----- and -----END
      CERTIFICATE----- or -----BEGIN PKCS7----- and -----END PKCS7----- . A certificate

      authority might include a chain of certificates file that also needs to be installed along
      with the actual binary certificate file.

  ７ Note

<!-- p.319 -->

 The Exchange Admin Center (EAC) can be used to manage certificates in Exchange Server
 2019 CU15 and later. For Exchange Server 2016 CU23 and Exchange Server 2019 CU12 to
 CU14, use the Exchange Management Shell (EMS) procedure.

What do you need to know before you begin?
   Estimated time to complete: 5 minutes.

   In the EAC, you need to import the certificate file from a UNC path ( \\<Server>\<Share>\
   or \\<LocalServerName>\c$\ ). In the Exchange Management Shell, you can specify a local
   path.

   In the EAC, you can import the certificate file on multiple Exchange servers at the same
   time (Step 4 in the procedure).

   To learn how to open the Exchange Management Shell in your on-premises Exchange
   organization, see Open the Exchange Management Shell.

   You need to be assigned permissions before you can perform this procedure or
   procedures. To see what permissions you need, see the "Client Access services security"
   entry in the Clients and mobile devices permissions topic.

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online      , or Exchange Online Protection .

Use the EAC to import a certificate on one or more
Exchange servers
 1. Open the EAC and navigate to Servers > Certificates.

 2. In the Select server list, select the Exchange server where you want to install the
   certificate, click More options   , and select Import Exchange certificate.

 3. The Import Exchange certificate wizard opens. On the This wizard will import a
   certificate from a file page, enter the following information:

<!-- p.320 -->

            File to import from: Enter the UNC path and filename of the certificate file. For
            example, \\FileServer01\Data\Fabrikam.cer

            Password: If the certificate file contains the private key or chain of trust, the file is
            protected by a password. Enter the password here.

     When you're finished, click Next.

   4. In the Specify the servers you want to apply this certificate to page, click Add

     On the Select a server page that opens, select the Exchange server where you want to
     install the certificate, and click Add - >. Repeat this step as many times as necessary.
     When you're finished selecting servers, click OK.

     When you're finished, click Finish. For next steps, see the Next steps section.

Use the Exchange Management Shell to import a
certificate on an Exchange server
To import a certificate file, use the following syntax:

  PowerShell

  Import-ExchangeCertificate -FileData
  ([System.IO.File]::ReadAllBytes('<FilePathOrUNCPath>')) [-Password (Read-Host
  "Enter password" -AsSecureString)] [-PrivateKeyExportable <$true | $false>] [-
  Server <ServerIdentity>]

You use this syntax with the following types of certificate files:

     Binary certificate files (PKCS #12 files that have .cer, .crt, .der, .p12, or .pfx filename
     extensions).
     Chain of certificates files (PKCS #7 text files that have .p7b or .p7c filename extensions).

This example imports the certificate file \\FileServer01\Data\Fabrikam.pfx that's protected by
the password P@ssw0rd1 on the local Exchange server. You're prompted to enter the
password.

  PowerShell

  Import-ExchangeCertificate -FileData
  ([System.IO.File]::ReadAllBytes('\\FileServer01\Data\Fabrikam.pfx')) -Password
  (Read-Host "Enter password" -AsSecureString)
