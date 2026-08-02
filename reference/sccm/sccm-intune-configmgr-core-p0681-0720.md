---
title: "Core infrastructure documentation — pages 681-720"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0681-0720
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0681-0720
family: sccm
documentKind: "doc"
abstract: "A PXE-enabled distribution point sends this certificate to computers. If the task sequence includes client actions like client policy retrieval or sending inventory information, the computer can connect to an HTTPS-enabled management point during the OS deployment process. ７ Not"
---

# Core infrastructure documentation — pages 681-720

<!-- p.681 -->

     A PXE-enabled distribution point sends this certificate to computers. If the task
     sequence includes client actions like client policy retrieval or sending inventory
     information, the computer can connect to an HTTPS-enabled management point
     during the OS deployment process.

        ７ Note

        For this PXE scenario, this certificate is only used during the OS deployment
        process. It isn't installed on the client. Because of this temporary use, you can
        use the same certificate for every OS deployment if you don't want to use
        multiple client certificates.

        The requirements for this certificate are the same as the client certificate for
        task sequence media. Because the requirements are the same, you can use the
        same certificate file.

        The certificate that you specify to HTTPS-enable a distribution point applies to
        all content distribution operations, not just OS deployment.

Certificate requirements:

     Certificate purpose: Client authentication

     Microsoft certificate template: Workstation Authentication

     The Enhanced Key Usage value must contain Client Authentication
     (1.3.6.1.5.5.7.3.2)

     There are no specific requirements for the certificate Subject Name or Subject
     Alternative Name (SAN). It's recommended to use a different certificate for each
     distribution point, but you can use the same certificate.

     The private key must be exportable.

     Maximum supported key length is 2,048 bits.

Export this certificate in a Public Key Certificate Standard (PKCS #12) format. You need to
know the password, so that you can import the certificate to the distribution point
properties.

Proxy web servers for internet-based client management

<!-- p.682 -->

If the site supports internet-based client management, and you use a proxy web server
by using SSL termination (bridging) for incoming internet connections, the proxy web
server has the following certificate requirements:

  ７ Note

  If you use a proxy web server without SSL termination (tunneling), no additional
  certificates are required on the proxy web server.

Certificate requirements:

     Certificate purpose: Server authentication and Client authentication

     Microsoft certificate template: Web Server and Workstation Authentication

     Internet FQDN in the Subject Name or Subject Alternative Name field. If you use
     Microsoft certificate templates, the Subject Alternative Name is only available with
     the workstation template.

This certificate is used to authenticate the following servers to internet clients and to
encrypt all data transferred between the client and this server with TLS:

     Internet-based management point
     Internet-based distribution point
     Internet-based software update point

The client authentication is used to bridge client connections between the Configuration
Manager clients and the internet-based site systems.

PKI certificates for clients

Windows client computers
Except for the software update point, this certificate authenticates the client to site
systems that run IIS and support HTTPS client connections.

Certificate requirements:

     Certificate purpose: Client authentication

     Microsoft certificate template: Workstation Authentication

<!-- p.683 -->

     The Enhanced Key Usage value must contain Client Authentication
     (1.3.6.1.5.5.7.3.2)

     The Key Usage value must contain Digital Signature, Key Encipherment (a0)

     Client computers must have a unique value in the Subject Name or Subject
     Alternative Name field. If used, the Subject Name field must contain the local
     computer name unless an alternative certificate selection criteria is specified. For
     more information, see Plan for PKI client certificate selection.

        ７ Note

        If you use multiple values for the Subject Alternative Name, it only uses the
        first value.

     There's no maximum supported key length.

By default, Configuration Manager looks for computer certificates in the Personal store
in the Computer certificate store.

Task sequence media for deploying operating systems
This certificate is used by an OSD task sequence and allows the computer to connect to
an HTTPS-enabled management point and distribution point during the OS deployment
process. Connections to the management point and to the distribution point may
include such actions such as client policy retrieval from the management point and
downloading of content from the distribution point.

This certificate is only used during the OS deployment process. It isn't used as part of
the client installation properties when the the client is installed during the Setup
Windows and ConfigMgr task nor is it installed on the device. Because of this
temporary use, you can use the same certificate for every OS deployment if you don't
want to use multiple client certificates.

When you have an environment that's HTTPS-only, the task sequence media must have
a valid certificate. This certificate allows the device to communicate with the site and for
the deployment to continue. After the task sequence completes, when the device is
joined to Active Directory, the client can automatically generate a PKI certificate via a
GPO, or you can install a PKI certificate by using another method.

  ７ Note

<!-- p.684 -->

  The requirements for this certificate are the same as the server certificate for site
  systems with the distribution point role. Because the requirements are the same,
  you can use the same certificate file.

Certificate requirements:

     Certificate purpose: Client authentication

     Microsoft certificate template: Workstation Authentication

     The Enhanced Key Usage value must contain Client Authentication
     (1.3.6.1.5.5.7.3.2)

     There are no specific requirements for the certificate Subject Name or Subject
     Alternative Name (SAN) fields. You can use the same certificate for all task
     sequence media.

     The private key must be exportable.

     Maximum supported key length is 2,048 bits.

Export this certificate in a Public Key Certificate Standard (PKCS #12) format. You need to
know the password, so that you can import the certificate when creating the task
sequence media.

  ） Important

  Boot images don't contain PKI certificates to communicate with the site. Instead,
  boot images use the PKI certificate added to the task sequence media to
  communicate with the site.

For more information on adding a PKI certificate to task sequence media, see Create
bootable media and Create prestaged media.

macOS client computers
This certificate authenticates the macOS client computer to the site system servers that
it communicates with. For example, management points and distribution points.

Certificate requirements:

     Certificate purpose: Client authentication

     Microsoft certificate template:

<!-- p.685 -->

        For Configuration Manager enrollment: Authenticated Session
        For certificate installation independent from Configuration Manager:
        Workstation Authentication

     The Enhanced Key Usage value must contain Client Authentication
     (1.3.6.1.5.5.7.3.2)

     Subject Name:
        For Configuration Manager that creates a User certificate, the certificate Subject
        value is automatically populated with the user name of the person who enrolls
        the macOS computer.
        For certificate installation that doesn't use Configuration Manager enrollment,
        but deploys a Computer certificate independently from Configuration Manager,
        the certificate Subject value must be unique. For example, specify the FQDN of
        the computer.
        The Subject Alternative Name field isn't supported.

     Maximum supported key length is 2,048 bits.

Mobile device clients
This certificate authenticates the mobile device client to the site system servers that it
communicates with. For example, management points and distribution points.

Certificate requirements:

     Certificate purpose: Client authentication

     Microsoft certificate template: Authenticated Session

     The Enhanced Key Usage value must contain Client Authentication
     (1.3.6.1.5.5.7.3.2)

     Maximum supported key length is 2,048 bits.

These certificates must be in Distinguished Encoding Rules (DER) encoded binary X.509
format. Base64 encoded X.509 format isn't supported.

Root certification authority (CA) certificates
This certificate is a standard root CA certificate.

Applies to:

<!-- p.686 -->

     OS deployment
     Client certificate authentication
     Mobile device enrollment

Certificate purpose: Certificate chain to a trusted source

The root CA certificate must be provided when clients have to chain the certificates of
the communicating server to a trusted source. The root CA certificate for clients must be
provided if the client certificates are issued by a different CA hierarchy than the CA
hierarchy that issued the management point certificate.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.687 -->

Step-by-step example deployment of
the PKI certificates for Configuration
Manager: Windows Server 2008
certification authority
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This step-by-step example deployment, which uses a Windows Server 2008 certification
authority (CA), has procedures that show you how to create and deploy the public key
infrastructure (PKI) certificates that Configuration Manager uses. These procedures use
an enterprise certification authority (CA) and certificate templates. The steps are
appropriate for a test network only, as a proof of concept.

Because there's no single method of deployment for the required certificates, consult
your particular PKI deployment documentation for the required procedures and best
practices to deploy the required certificates for a production environment. For more
about the certificate requirements, see PKI certificate requirements for Configuration
Manager.

   Tip

  You can adapt the instructions in this topic for operating systems that aren't
  documented in the Test Network Requirements section. However, if you are
  running the issuing CA on Windows Server 2012, you're not prompted for the
  certificate template version. Instead, specify this on the Compatibility tab of the
  template properties:

        Certification Authority: Windows Server 2003
           Certificate recipient: Windows XP / Server 2003

Test network requirements
The step-by-step instructions have the following requirements:

      The test network is running Active Directory Domain Services with Windows Server
      2008, and it is installed as a single domain, single forest.

<!-- p.688 -->

       You have a member server running Windows Server 2008 Enterprise Edition, which
       has the Active Directory Certificate Services role installed on it, and it is set up as
       an enterprise root certification authority (CA).

       You have one computer that has Windows Server 2008 (Standard Edition or
       Enterprise Edition, R2 or later) installed on it, that computer is designated as a
       member server, and Internet Information Services (IIS) is installed on it. This
       computer will be the Configuration Manager site system server that you will
       configure with an intranet fully qualified domain name (FQDN) to support client
       connections on the intranet and an internet FQDN if you must support mobile
       devices that are enrolled by Configuration Manager and clients on the internet.

       You have one Windows Vista client that has the latest service pack installed, and
       this computer is set up with a computer name that comprises ASCII characters and
       is joined to the domain. This computer will be a Configuration Manager client
       computer.

       You can sign in with a root domain administrator account or an enterprise domain
       administrator account and use this account for all procedures in this example
       deployment.

Overview of the certificates
The following table lists the types of PKI certificates that might be required for
Configuration Manager and describes how they are used.

                                                                                        ﾉ      Expand table

 Certificate                 Certificate Description
 Requirement

 Web server certificate      This certificate is used to encrypt data and authenticate the server to
 for site systems that run   clients. It must be installed externally from Configuration Manager on
 IIS                         site systems servers that run Internet Information Services (IIS) and that
                             are set up in Configuration Manager to use HTTPS.

                             For the steps to set up and install this certificate, see Deploy the web
                             server certificate for site systems that run IIS in this topic.

 Service certificate for     For the steps to configure and install this certificate, see Deploy the
 clients to connect to       service certificate for cloud-based distribution points in this topic.
 cloud-based
 distribution points         Important: This certificate is used in conjunction with the Windows
                             Azure management certificate. For more about the management

<!-- p.689 -->

Certificate              Certificate Description
Requirement

                         certificate, see How to Create a Management Certificate and How to
                         Add a Management Certificate to a Windows Azure Subscription.

Client certificate for   This certificate is used to authenticate Configuration Manager client
Windows computers        computers to site systems that are set up to use HTTPS. It can also be
                         used for management points and state migration points to monitor
                         their operational status when they are set up to use HTTPS. It must be
                         installed externally from Configuration Manager on computers.

                         For the steps to set up and install this certificate, see Deploy the client
                         certificate for Windows computers in this topic.

Client certificate for   This certificate has two purposes:
distribution points
                         The certificate is used to authenticate the distribution point to an
                         HTTPS-enabled management point before the distribution point sends
                         status messages.

                         When the Enable PXE support for clients distribution point option is
                         selected, the certificate is sent to computers that PXE boot so that they
                         can connect to a HTTPS-enabled management point during the
                         deployment of the operating system.

                         For the steps to set up and install this certificate, see Deploy the client
                         certificate for distribution points in this topic.

Enrollment certificate   This certificate is used to authenticate Configuration Manager mobile
for mobile devices       device clients to site systems that are set up to use HTTPS. It must be
                         installed as part of mobile device enrollment in Configuration
                         Manager, and you choose the configured certificate template as a
                         mobile device client setting.

                         For the steps to set up this certificate, see Deploy the enrollment
                         certificate for mobile devices in this topic.

Client certificate for   You can request and install this certificate from a Mac computer when
Mac computers            you use Configuration Manager enrollment and choose the configured
                         certificate template as a mobile device client setting.

                         For the steps to set up this certificate, see Deploy the client certificate
                         for Mac computers in this topic.

Deploy the web server certificate for site
systems that run IIS

<!-- p.690 -->

This certificate deployment has the following procedures:

     Create and issue the web server certificate template on the certification authority

     Request the web server certificate

     Configure IIS to use the web server certificate

Create and issue the web server certificate template on
the certification authority
This procedure creates a certificate template for Configuration Manager site systems
and adds it to the certification authority.

To create and issue the web server certificate template on the
certification authority

   1. Create a security group named ConfigMgr IIS Servers that has the member servers
     to install Configuration Manager site systems that will run IIS.

   2. On the member server that has Certificate Services installed, in the Certification
     Authority console, right-click Certificate Templates and then choose Manage to
     load the Certificate Templates console.

   3. In the results pane, right-click the entry that has Web Server in the Template
     Display Name column, and then choose Duplicate Template.

   4. In the Duplicate Template dialog box, ensure that Windows 2003 Server,
     Enterprise Edition is selected, and then choose OK.

        ） Important

        Do not select Windows 2008 Server, Enterprise Edition.

   5. In the Properties of New Template dialog box, on the General tab, enter a
     template name, like ConfigMgr Web Server Certificate, to generate the web
     certificates that will be used on Configuration Manager site systems.

   6. Choose the Subject Name tab, and make sure that Supply in the request is
     selected.

   7. Choose the Security tab, and then remove the Enroll permission from the Domain
     Admins and Enterprise Admins security groups.

<!-- p.691 -->

   8. Choose Add, enter ConfigMgr IIS Servers in the text box, and then choose OK.

   9. Choose the Enroll permission for this group, and do not clear the Read permission.

 10. Choose OK, and then close the Certificate Templates Console.

 11. In the Certification Authority console, right-click Certificate Templates, choose
     New, and then choose Certificate Template to Issue.

 12. In the Enable Certificate Templates dialog box, choose the new template that you
     just created, ConfigMgr Web Server Certificate, and then choose OK.

 13. If you do not need to create and issue more certificates, close Certification
     Authority.

Request the web server certificate
This procedure lets you specify the intranet and internet FQDN values that will be set up
in the site system server properties and then installs the web server certificate on to the
member server that runs IIS.

To request the web server certificate

   1. Restart the member server that runs IIS to ensure that the computer can access the
     certificate template that you created by using the Read and Enroll permissions that
     you configured.

   2. Choose Start, choose Run, and then type mmc.exe. In the empty console, choose
     File, and then choose Add/Remove Snap-in.

   3. In the Add or Remove Snap-ins dialog box, choose Certificates from the list of
     Available snap-ins, and then choose Add.

   4. In the Certificate snap-in dialog box, choose Computer account, and then choose
     Next.

   5. In the Select Computer dialog box, ensure that Local computer: (the computer
     this console is running on) is selected, and then choose Finish.

   6. In the Add or Remove Snap-ins dialog box, choose OK.

   7. In the console, expand Certificates (Local Computer), and then choose Personal.

   8. Right-click Certificates, choose All Tasks, and then choose Request New
     Certificate.

<!-- p.692 -->

 9. On the Before You Begin page, choose Next.

10. If you see the Select Certificate Enrollment Policy page, choose Next.

11. On the Request Certificates page, identify the ConfigMgr Web Server Certificate
   from the list of available certificates, and then choose More information is
   required to enroll for this certificate. Click here to configure settings.

12. In the Certificate Properties dialog box, in the Subject tab, do not make any
   changes to Subject name. This means that the Value box for the Subject name
   section remains blank. Instead, from the Alternative name section, choose the
   Type drop-down list, and then choose DNS.

13. In the Value box, specify the FQDN values that you will specify in the Configuration
   Manager site system properties, and then choose OK to close the Certificate
   Properties dialog box.

   Examples:

         If the site system will only accept client connections from the intranet, and
         the intranet FQDN of the site system server is server1.internal.contoso.com,
         enter server1.internal.contoso.com, and then choose Add.

         If the site system will accept client connections from the intranet and the
         internet, and the intranet FQDN of the site system server is
         server1.internal.contoso.com and the internet FQDN of the site system server
         is server.contoso.com:

         a. Enter server1.internal.contoso.com, and then choose Add.

         b. Enter server.contoso.com, and then choose Add.

           ７ Note

           You can specify the FQDNs for Configuration Manager in any order.
           However, check that all devices that will use the certificate, such as
           mobile devices and proxy web servers, can use a certificate subject
           alternative name (SAN) and multiple values in the SAN. If devices have
           limited support for SAN values in certificates, you might have to change
           the order of the FQDNs or use the Subject value instead.

14. On the Request Certificates page, choose ConfigMgr Web Server Certificate from
   the list of available certificates, and then choose Enroll.

<!-- p.693 -->

 15. On the Certificates Installation Results page, wait until the certificate is installed,
     and then choose Finish.

 16. Close Certificates (Local Computer).

Configure IIS to use the web server certificate
This procedure binds the installed certificate to the IIS Default Web Site.

To set up IIS to use the web server certificate

   1. On the member server that has IIS installed, choose Start, choose Programs,
     choose Administrative Tools, and then choose Internet Information Services (IIS)
     Manager.

   2. Expand Sites, right-click Default Web Site, and then choose Edit Bindings.

   3. Choose the https entry, and then choose Edit.

   4. In the Edit Site Binding dialog box, select the certificate that you requested by
     using the ConfigMgr Web Server Certificates template, and then choose OK.

        ７ Note

        If you are not sure which is the correct certificate, choose one, and then
        choose View. This lets you compare the selected certificate details to the
        certificates in the Certificates snap-in. For example, the Certificates snap-in
        shows the certificate template that was used to request the certificate. You
        can then compare the certificate thumbprint of the certificate that was
        requested by using the ConfigMgr Web Server Certificates template to the
        certificate thumbprint of the certificate currently selected in the Edit Site
        Binding dialog box.

   5. Choose OK in the Edit Site Binding dialog box, and then choose Close.

   6. Close Internet Information Services (IIS) Manager.

     The member server is now set up with a Configuration Manager web server
     certificate.

  ） Important

<!-- p.694 -->

  When you install the Configuration Manager site system server on this computer,
  make sure that you specify the same FQDNs in the site system properties as you
  specified when you requested the certificate.

Deploy the service certificate for cloud-based
distribution points
This certificate deployment has the following procedures:

     Create and issue a custom web server certificate template on the certification
     authority

     Request the custom web server certificate

     Export the custom web server certificate for cloud-based distribution points

Create and issue a custom web server certificate template
on the certification authority
This procedure creates a custom certificate template that is based on the web server
certificate template. The certificate is for Configuration Manager cloud-based
distribution points and the private key must be exportable. After the certificate template
is created, it is added to the certification authority.

  ７ Note

  This procedure uses a different certificate template from the web server certificate
  template that you created for site systems that run IIS. Although both certificates
  require server authentication capability, the certificate for cloud-based distribution
  points requires you to enter a custom-defined value for the Subject Name and the
  private key must be exported. As a security best practice, do not set up certificate
  templates so that the private key can be exported unless this configuration is
  required. The cloud-based distribution point requires this configuration because
  you must import the certificate as a file, rather than choose it from the certificate
  store.

  When you create a new certificate template for this certificate, you can restrict the
  computers that can request a certificate whose private key can be exported. On a
  production network, you might also consider adding the following changes for this
  certificate:

<!-- p.695 -->

      Require approval to install the certificate for additional security.
         Increase the certificate validity period. Because you must export and import
         the certificate each time before it expires, an increase of the validity period
         reduces how often you must repeat this procedure. However, an increase
         of the validity period also decreases the security of the certificate because
         it provides more time for an attacker to decrypt the private key and steal
         the certificate.
         Use a custom value in the certificate Subject Alternative Name (SAN) to
         help identify this certificate from standard web server certificates that you
         use with IIS.

To create and issue the custom web server certificate template on
the certification authority

  1. Create a security group named ConfigMgr Site Servers that has the member
    servers to install Configuration Manager primary site servers that will manage
    cloud-based distribution points.

  2. On the member server that is running the Certification Authority console, right-
    click Certificate Templates, and then choose Manage to load the Certificate
    Templates management console.

  3. In the results pane, right-click the entry that has Web Server in the Template
    Display Name column, and then choose Duplicate Template.

  4. In the Duplicate Template dialog box, ensure that Windows 2003 Server,
    Enterprise Edition is selected, and then choose OK.

      ） Important

      Do not select Windows 2008 Server, Enterprise Edition.

  5. In the Properties of New Template dialog box, on the General tab, enter a
    template name, like ConfigMgr Cloud-Based Distribution Point Certificate, to
    generate the web server certificate for cloud-based distribution points.

  6. Choose the Request Handling tab, and then choose Allow private key to be
    exported.

<!-- p.696 -->

   7. Choose the Security tab, and then remove the Enroll permission from the
     Enterprise Admins security group.

   8. Choose Add, enter ConfigMgr Site Servers in the text box, and then choose OK.

   9. Select the Enroll permission for this group, and do not clear the Read permission.

 10. Choose the Cryptography tab and ensure that Minimum key size has been set to
     2048.

 11. Choose OK, and then close Certificate Templates Console.

 12. In the Certification Authority console, right-click Certificate Templates, choose
     New, and then choose Certificate Template to Issue.

 13. In the Enable Certificate Templates dialog box, choose the new template that you
     just created, ConfigMgr Cloud-Based Distribution Point Certificate, and then
     choose OK.

 14. If you do not have to create and issue more certificates, close Certification
     Authority.

Request the custom web server certificate
This procedure requests and then installs the custom web server certificate on the
member server that will run the site server.

To request the custom web server certificate

   1. Restart the member server after you create and configure the ConfigMgr Site
     Servers security group to ensure that the computer can access the certificate
     template that you created by using the Read and Enroll permissions that you
     configured.

   2. Choose Start, choose Run, and then enter mmc.exe. In the empty console, choose
     File, and then choose Add/Remove Snap-in.

   3. In the Add or Remove Snap-ins dialog box, choose Certificates from the list of
     Available snap-ins, and then choose Add.

   4. In the Certificate snap-in dialog box, choose Computer account, and then choose
     Next.

   5. In the Select Computer dialog box, ensure that Local computer: (the computer
     this console is running on) is selected, and then choose Finish.

<!-- p.697 -->

   6. In the Add or Remove Snap-ins dialog box, choose OK.

   7. In the console, expand Certificates (Local Computer), and then choose Personal.

   8. Right-click Certificates, choose All Tasks, and then choose Request New
     Certificate.

   9. On the Before You Begin page, choose Next.

 10. If you see the Select Certificate Enrollment Policy page, choose Next.

 11. On the Request Certificates page, identify the ConfigMgr Cloud-Based
     Distribution Point Certificate from the list of available certificates, and then
     choose More information is required to enroll for this certificate. choose here to
     configure settings.

 12. In the Certificate Properties dialog box, in the Subject tab, for the Subject name,
     choose Common name as the Type.

 13. In the Value box, specify your choice of service name and your domain name by
     using an FQDN format. For example: clouddp1.contoso.com.

        ７ Note

        Make the service name unique in your namespace. You will use DNS to create
        an alias (CNAME record) to map this service name to an automatically
        generated identifier (GUID) and an IP address from Windows Azure.

 14. Choose Add, and then choose OK to close the Certificate Properties dialog box.

 15. On the Request Certificates page, choose ConfigMgr Cloud-Based Distribution
     Point Certificate from the list of available certificates, and then choose Enroll.

 16. On the Certificates Installation Results page, wait until the certificate is installed,
     and then choose Finish.

 17. Close Certificates (Local Computer).

Export the custom web server certificate for cloud-based
distribution points
This procedure exports the custom web server certificate to a file, so that it can be
imported when you create the cloud-based distribution point.

<!-- p.698 -->

To export the custom web server certificate for cloud-based
distribution points

   1. In the Certificates (Local Computer) console, right-click the certificate that you just
     installed, choose All Tasks, and then choose Export.

   2. In the Certificates Export Wizard, choose Next.

   3. On the Export Private Key page, choose Yes, export the private key, and then
     choose Next.

        ７ Note

        If this option is not available, the certificate has been created without the
        option to export the private key. In this scenario, you cannot export the
        certificate in the required format. You must set up the certificate template so
        that the private key can be exported, and then request the certificate again.

   4. On the Export File Format page, ensure that the Personal Information Exchange -
     PKCS #12 (.PFX) option is selected.

   5. On the Password page, specify a strong password to protect the exported
     certificate with its private key, and then choose Next.

   6. On the File to Export page, specify the name of the file that you want to export,
     and then choose Next.

   7. To close the wizard, choose Finish in the Certificate Export Wizard page, and then
     choose OK in the confirmation dialog box.

   8. Close Certificates (Local Computer).

   9. Store the file securely and ensure that you can access it from the Configuration
     Manager console.

     The certificate is now ready to be imported when you create a cloud-based
     distribution point.

Deploy the client certificate for Windows
computers
This certificate deployment has the following procedures:

<!-- p.699 -->

     Create and issue the Workstation Authentication certificate template on the
     certification authority

     Configure autoenrollment of the Workstation Authentication template by using
     Group Policy

     Automatically enroll the Workstation Authentication certificate and verify its
     installation on computers

Create and issue the Workstation Authentication
certificate template on the certification authority
This procedure creates a certificate template for Configuration Manager client
computers and adds it to the certification authority.

To create and issue the Workstation Authentication certificate
template on the certification authority

   1. On the member server that is running the Certification Authority console, right-
     click Certificate Templates, and then choose Manage to load the Certificate
     Templates management console.

   2. In the results pane, right-click the entry that has Workstation Authentication in
     the Template Display Name column, and then choose Duplicate Template.

   3. In the Duplicate Template dialog box, ensure that Windows 2003 Server,
     Enterprise Edition is selected, and then choose OK.

        ） Important

        Do not select Windows 2008 Server, Enterprise Edition.

   4. In the Properties of New Template dialog box, on the General tab, enter a
     template name, like ConfigMgr Client Certificate, to generate the client certificates
     that will be used on Configuration Manager client computers.

   5. Choose the Security tab, select the Domain Computers group, and then select the
     additional permissions of Read and Autoenroll. Do not clear Enroll.

   6. Choose OK, and then close Certificate Templates Console.

   7. In the Certification Authority console, right-click Certificate Templates, choose
     New, and then choose Certificate Template to Issue.

<!-- p.700 -->

   8. In the Enable Certificate Templates dialog box, choose the new template that you
     just created, ConfigMgr Client Certificate, and then choose OK.

   9. If you do not need to create and issue more certificates, close Certification
     Authority.

Configure autoenrollment of the Workstation
Authentication template by using Group Policy
This procedure sets up Group Policy to autoenroll the client certificate on computers.

To set up autoenrollment of the Workstation Authentication
template by using Group Policy

   1. On the domain controller, choose Start, choose Administrative Tools, and then
     choose Group Policy Management.

   2. Go to your domain, right-click the domain, and then choose Create a GPO in this
     domain, and Link it here.

       ７ Note

       This step uses the best practice of creating a new Group Policy for custom
       settings rather than editing the Default Domain Policy that is installed with
       Active Directory Domain Services. When you assign this Group Policy at the
       domain level, you will apply it to all computers in the domain. In a production
       environment, you can restrict the autoenrollment so that it enrolls on only
       selected computers. You can assign the Group Policy at an organizational unit
       level, or you can filter the domain Group Policy with a security group so that it
       applies only to the computers in the group. If you restrict autoenrollment,
       remember to include the server that is set up as the management point.

   3. In the New GPO dialog box, enter a name, like Autoenroll Certificates, for the new
     Group Policy, and then choose OK.

   4. In the results pane, on the Linked Group Policy Objects tab, right-click the new
     Group Policy, and then choose Edit.

   5. In the Group Policy Management Editor, expand Policies under Computer
     Configuration, and then go to Windows Settings / Security Settings / Public Key
     Policies.

<!-- p.701 -->

   6. Right-click the object type named Certificate Services Client - Auto-enrollment,
     and then choose Properties.

   7. From the Configuration Model drop-down list, choose Enabled, choose Renew
     expired certificates, update pending certificates, remove revoked certificates,
     choose Update certificates that use certificate templates, and then choose OK.

   8. Close Group Policy Management.

Automatically enroll the Workstation Authentication
certificate and verify its installation on computers
This procedure installs the client certificate on computers and verifies the installation.

To automatically enroll the Workstation Authentication certificate
and verify its installation on the client computer

   1. Restart the workstation computer, and wait a few minutes before you sign in.

        ７ Note

        Restarting a computer is the most reliable method of ensuring success with
        certificate autoenrollment.

   2. Sign in with an account that has administrative privileges.

   3. In the search box, enter mmc.exe., and then press Enter.

   4. In the empty management console, choose File, and then choose Add/Remove
     Snap-in.

   5. In the Add or Remove Snap-ins dialog box, choose Certificates from the list of
     Available snap-ins, and then choose Add.

   6. In the Certificate snap-in dialog box, choose Computer account, and then choose
     Next.

   7. In the Select Computer dialog box, ensure that Local computer: (the computer
     this console is running on) is selected, and then choose Finish.

   8. In the Add or Remove Snap-ins dialog box, choose OK.

<!-- p.702 -->

   9. In the console, expand Certificates (Local Computer), expand Personal, and then
     choose Certificates.

 10. In the results pane, confirm that a certificate has Client Authentication in the
     Intended Purpose column, and that ConfigMgr Client Certificate is in the
     Certificate Template column.

 11. Close Certificates (Local Computer).

 12. Repeat steps 1 through 11 for the member server to verify that the server that will
     be set up as the management point also has a client certificate.

     The computer is now set up with a Configuration Manager client certificate.

Deploy the client certificate for distribution
points

  ７ Note

  This certificate can also be used for media images that do not use PXE boot,
  because the certificate requirements are the same.

This certificate deployment has the following procedures:

     Create and issue a custom Workstation Authentication certificate template on the
     certification authority

     Request the custom Workstation Authentication certificate

     Export the client certificate for distribution points

Create and issue a custom Workstation Authentication
certificate template on the certification authority
This procedure creates a custom certificate template for Configuration Manager
distribution points so that the private key can be exported and adds the certificate
template to the certification authority.

  ７ Note

  This procedure uses a different certificate template from the certificate template
  that you created for client computers. Although both certificates require client

<!-- p.703 -->

 authentication capability, the certificate for distribution points requires that the
 private key is exported. As a security best practice, do not set up certificate
 templates so the private key can be exported unless this configuration is required.
 The distribution point requires this configuration because you must import the
 certificate as a file rather than choose it from the certificate store.

 When you create a new certificate template for this certificate, you can restrict the
 computers that can request a certificate whose private key can be exported. In our
 example deployment, this will be the security group that you previously created for
 Configuration Manager site system servers that run IIS. On a production network
 that distributes the IIS site system roles, consider creating a new security group for
 the servers that run distribution points so that you can restrict the certificate to just
 these site system servers. You might also consider adding the following
 modifications for this certificate:

      Require approval to install the certificate for additional security.
         Increase the certificate validity period. Because you must export and import
         the certificate each time before it expires, an increase of the validity period
         reduces how often you must repeat this procedure. However, an increase
         of the validity period also decreases the security of the certificate because
         it provides more time for an attacker to decrypt the private key and steal
         the certificate.
         Use a custom value in the certificate Subject field or Subject Alternative
         Name (SAN) to help identify this certificate from standard client certificates.
         This can be particularly helpful if you will use the same certificate for
         multiple distribution points.

To create and issue the custom Workstation Authentication
certificate template on the certification authority

  1. On the member server that is running the Certification Authority console, right-
    click Certificate Templates, and then choose Manage to load the Certificate
    Templates management console.

  2. In the results pane, right-click the entry that has Workstation Authentication in
    the Template Display Name column, and then choose Duplicate Template.

  3. In the Duplicate Template dialog box, ensure that Windows 2003 Server,
    Enterprise Edition is selected, and then choose OK.

<!-- p.704 -->

        ） Important

        Do not select Windows 2008 Server, Enterprise Edition.

   4. In the Properties of New Template dialog box, on the General tab, enter a
     template name, like ConfigMgr Client Distribution Point Certificate, to generate
     the client authentication certificate for distribution points.

   5. Choose the Request Handling tab, and then choose Allow private key to be
     exported.

   6. Choose the Security tab, and then remove the Enroll permission from the
     Enterprise Admins security group.

   7. Choose Add, enter ConfigMgr IIS Servers in the text box, and then choose OK.

   8. Select the Enroll permission for this group, and do not clear the Read permission.

   9. Choose OK, and then close Certificate Templates Console.

 10. In the Certification Authority console, right-click Certificate Templates, choose
     New, and then choose Certificate Template to Issue.

 11. In the Enable Certificate Templates dialog box, choose the new template that you
     just created, ConfigMgr Client Distribution Point Certificate, and then choose OK.

 12. If you do not have to create and issue more certificates, close Certification
     Authority.

Request the custom Workstation Authentication
certificate
This procedure requests and then installs the custom client certificate on to the member
server that runs IIS and that will be set up as a distribution point.

To request the custom Workstation Authentication certificate

   1. Choose Start, choose Run, and then enter mmc.exe. In the empty console, choose
     File, and then choose Add/Remove Snap-in.

   2. In the Add or Remove Snap-ins dialog box, choose Certificates from the list of
     Available snap-ins, and then choose Add.

<!-- p.705 -->

   3. In the Certificate snap-in dialog box, choose Computer account, and then choose
     Next.

   4. In the Select Computer dialog box, ensure that Local computer: (the computer
     this console is running on) is selected, and then choose Finish.

   5. In the Add or Remove Snap-ins dialog box, choose OK.

   6. In the console, expand Certificates (Local Computer), and then choose Personal.

   7. Right-click Certificates, choose All Tasks, and then choose Request New
     Certificate.

   8. On the Before You Begin page, choose Next.

   9. If you see the Select Certificate Enrollment Policy page, choose Next.

 10. On the Request Certificates page, choose ConfigMgr Client Distribution Point
     Certificate from the list of available certificates, and then choose Enroll.

 11. On the Certificates Installation Results page, wait until the certificate is installed,
     and then choose Finish.

 12. In the results pane, confirm that a certificate has Client Authentication in the
     Intended Purpose column and that ConfigMgr Client Distribution Point
     Certificate is in the Certificate Template column.

 13. Do not close Certificates (Local Computer).

Export the client certificate for distribution points
This procedure exports the custom Workstation Authentication certificate to a file so
that it can be imported in the distribution point properties.

To export the client certificate for distribution points

   1. In the Certificates (Local Computer) console, right-click the certificate that you just
     installed, choose All Tasks, and then choose Export.

   2. In the Certificates Export Wizard, choose Next.

   3. On the Export Private Key page, choose Yes, export the private key, and then
     choose Next.

        ７ Note

<!-- p.706 -->

        If this option is not available, the certificate has been created without the
        option to export the private key. In this scenario, you cannot export the
        certificate in the required format. You must set up the certificate template so
        that the private key can be exported and then request the certificate again.

   4. On the Export File Format page, ensure that the Personal Information Exchange -
     PKCS #12 (.PFX) option is selected.

   5. On the Password page, specify a strong password to protect the exported
     certificate with its private key, and then choose Next.

   6. On the File to Export page, specify the name of the file that you want to export,
     and then choose Next.

   7. To close the wizard, choose Finish on the Certificate Export Wizard page, and
     choose OK in the confirmation dialog box.

   8. Close Certificates (Local Computer).

   9. Store the file securely and ensure that you can access it from the Configuration
     Manager console.

     The certificate is now ready to be imported when you set up the distribution point.

   Tip

  You can use the same certificate file when you set up media images for an
  operating system deployment that does not use PXE boot, and the task sequence
  to install the image must contact a management point that requires HTTPS client
  connections.

Deploy the enrollment certificate for mobile
devices
This certificate deployment has a single procedure to create and issue the enrollment
certificate template on the certification authority.

Create and issue the enrollment certificate template on
the certification authority

<!-- p.707 -->

This procedure creates an enrollment certificate template for Configuration Manager
mobile devices and adds it to the certification authority.

To create and issue the enrollment certificate template on the
certification authority

   1. Create a security group that has users who will enroll mobile devices in
     Configuration Manager.

   2. On the member server that has Certificate Services installed, in the Certification
     Authority console, right-click Certificate Templates, and then choose Manage to
     load the Certificate Templates management console.

   3. In the results pane, right-click the entry that has Authenticated Session in the
     Template Display Name column, and then choose Duplicate Template.

   4. In the Duplicate Template dialog box, ensure that Windows 2003 Server,
     Enterprise Edition is selected, and then choose OK.

        ） Important

        Do not select Windows 2008 Server, Enterprise Edition.

   5. In the Properties of New Template dialog box, on the General tab, enter a
     template name, like ConfigMgr Mobile Device Enrollment Certificate, to generate
     the enrollment certificates for the mobile devices to be managed by Configuration
     Manager.

   6. Choose the Subject Name tab, make sure that Build from this Active Directory
     information is selected, select Common name for the Subject name format:, and
     then clear User principal name (UPN) from Include this information in alternate
     subject name.

   7. Choose the Security tab, choose the security group that has users who have
     mobile devices to enroll, and then choose the additional permission of Enroll. Do
     not clear Read.

   8. Choose OK, and then close Certificate Templates Console.

   9. In the Certification Authority console, right-click Certificate Templates, choose
     New, and then choose Certificate Template to Issue.

<!-- p.708 -->

 10. In the Enable Certificate Templates dialog box, choose the new template that you
     just created, ConfigMgr Mobile Device Enrollment Certificate, and then choose
     OK.

 11. If you do not need to create and issue more certificates, close the Certification
     Authority console.

     The mobile device enrollment certificate template is now ready to be selected
     when you set up a mobile device enrollment profile in the client settings.

Deploy the client certificate for Mac computers
This certificate deployment has a single procedure to create and issue the enrollment
certificate template on the certification authority.

Create and issue a Mac client certificate template on the
certification authority
This procedure creates a custom certificate template for Configuration Manager Mac
computers and adds the certificate template to the certification authority.

  ７ Note

  This procedure uses a different certificate template from the certificate template
  that you might have created for Windows client computers or for distribution
  points.

  When you create a new certificate template for this certificate, you can restrict the
  certificate request to authorized users.

To create and issue the Mac client certificate template on the
certification authority

   1. Create a security group that has user accounts for administrative users who will
     enroll the certificate on the Mac computer by using Configuration Manager.

   2. On the member server that is running the Certification Authority console, right-
     click Certificate Templates, and then choose Manage to load the Certificate
     Templates management console.

<!-- p.709 -->

 3. In the results pane, right-click the entry that displays Authenticated Session in the
   Template Display Name column, and then choose Duplicate Template.

 4. In the Duplicate Template dialog box, ensure that Windows 2003 Server,
   Enterprise Edition is selected, and then choose OK.

      ） Important

      Do not select Windows 2008 Server, Enterprise Edition.

 5. In the Properties of New Template dialog box, on the General tab, enter a
   template name, like ConfigMgr Mac Client Certificate, to generate the Mac client
   certificate.

 6. Choose the Subject Name tab, make sure that Build from this Active Directory
   information is selected, choose Common name for the Subject name format:, and
   then clear User principal name (UPN) from Include this information in alternate
   subject name.

 7. Choose the Security tab, and then remove the Enroll permission from the Domain
   Admins and Enterprise Admins security groups.

 8. Choose Add, specify the security group that you created in step one, and then
   choose OK.

 9. Choose the Enroll permission for this group, and do not clear the Read permission.

10. Choose OK, and then close Certificate Templates Console.

11. In the Certification Authority console, right-click Certificate Templates, choose
   New, and then choose Certificate Template to Issue.

12. In the Enable Certificate Templates dialog box, choose the new template that you
   just created, ConfigMgr Mac Client Certificate, and then choose OK.

13. If you do not have to create and issue more certificates, close Certification
   Authority.

   The Mac client certificate template is now ready to be selected when you set up
   client settings for enrollment.

Feedback

<!-- p.710 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.711 -->

Additional information about privacy for
Configuration Manager
07/17/2025

Applies to: Configuration Manager (current branch)

Updates and servicing
Configuration Manager uses an update model that helps keep your environment current with
the latest updates and features. This feature uses a site system role called the service
connection point. You choose the server where to install this role.

For more information about collected information and how it's used, see Usage data.

Usage data
Configuration Manager collects diagnostics and usage data about itself, which Microsoft uses
to improve the installation experience, quality, and security of future releases. Diagnostics and
usage data is enabled for each Configuration Manager hierarchy. It consists of SQL Server
queries that run on a weekly basis on each primary site and at the central administration site.
When the hierarchy uses a central administration site, the data from primary sites is then
replicated to that site. At the top-level site of your hierarchy, the service connection point
submits this information when it checks for updates. If the service connection point is in offline
mode, the information is transferred by using the service connection tool.

Configuration Manager collects data only from the site's SQL Server database, and it doesn't
collect data directly from clients or site servers.

Administrators can change the level of data that's collected by going to the Usage Data
section of the Configuration Manager console.

For more information about usage data levels and settings, see Diagnostics and usage data.

Endpoint Protection
Microsoft Cloud Protection Service was formerly known as Microsoft Active Protection Service
or MAPS.

The applicable products are System Center Endpoint Protection and the Endpoint Protection
feature of Configuration Manager (to manage System Center Endpoint Protection and

<!-- p.712 -->

Windows Defender for Windows 10 or later).

The Microsoft Cloud Protection Service antimalware community is a voluntary worldwide
online community that includes System Center Endpoint Protection users. When you join
Microsoft Cloud Protection Service, System Center Endpoint Protection automatically sends
information to Microsoft. Microsoft uses the information to determine software to investigate
for potential threats and to help improve the effectiveness of System Center Endpoint
Protection. This community helps stop the spread of new malicious software infections. If a
Microsoft Cloud Protection Service report includes details about malware or potentially
unwanted software that the Endpoint Protection client may be able to remove, Microsoft Cloud
Protection Service downloads the latest signature to address it. Microsoft Cloud Protection
Service can also find "false positives" and fix them. (False positives are where something
originally identified as malware turns out not to be.)

Microsoft Cloud Protection Service reports include information about potential malware files,
like file names, cryptographic hash, vendor, size, and date stamps. In addition, Microsoft Cloud
Protection Service might collect full URLs to indicate the origin of the file. These URLs might
occasionally have personal information like search terms or data that was entered in forms.
Reports might also include actions that you took when Endpoint Protection notified you about
unwanted software. Microsoft Cloud Protection Service reports include this information to help
Microsoft gauge how effectively Endpoint Protection can detect and remove malware and
potentially unwanted software and to attempt to identify new malware.

You can join Microsoft Cloud Protection Service if you have a basic or advanced membership.
Basic member reports have the information described previously. Advanced member reports
are more comprehensive and may include additional details about the software that Endpoint
Protection detects, like the location of such software, file names, how the software operates,
and how it has affected your computer. These reports and reports from other Endpoint
Protection users who participate in Microsoft Cloud Protection Service help Microsoft
researchers discover new threats more rapidly. Malware definitions are then created for
programs that meet the analysis criteria, and the updated definitions are made available to all
users through Microsoft Update.

To help detect and fix certain kinds of malware infections, the product regularly sends
Microsoft Cloud Protection Service information about the security state of your PC. This
information includes information about your PC's security settings and log files that describe
the drivers and other software that load while your PC boots.

A number that uniquely identifies your PC is also sent. Also, Microsoft Cloud Protection Service
may collect the IP addresses that the potential malware files connect to.

Microsoft Cloud Protection Service reports are used to improve Microsoft software and
services. The reports might also be used for statistical or other testing or analytical purposes

<!-- p.713 -->

and to generate definitions. Only Microsoft employees, contractors, partners, and vendors who
have a business need to use the reports can access them.

Microsoft Cloud Protection Service does not intentionally collect personal information. To the
extent that Microsoft Cloud Protection Service collects any personal information, Microsoft
does not use the information to identify you or contact you.

For more information, see Endpoint Protection.

<!-- p.714 -->

How to enable TLS 1.2
Article • 10/18/2024

Applies to: Configuration Manager (Current Branch)

Transport Layer Security (TLS), like Secure Sockets Layer (SSL), is an encryption protocol
intended to keep data secure when being transferred over a network. These articles
describe steps required to ensure that Configuration Manager secure communication
uses the TLS 1.2 protocol. These articles also describe update requirements for
commonly used components and troubleshooting common problems.

Enabling TLS 1.2
Configuration Manager relies on many different components for secure communication.
The protocol that's used for a given connection depends on the capabilities of the
relevant components on both the client and server side. If any component is out-of-date
or not properly configured, the communication might use an older, less secure protocol.
To correctly enable Configuration Manager to support TLS 1.2 for all secure
communications, you must enable TLS 1.2 for all required components. The required
components depend on your environment and the Configuration Manager features that
you use.

  ） Important

  Start this process with the clients, especially previous versions of Windows. Before
  enabling TLS 1.2 and disabling the older protocols on the Configuration Manager
  servers, make sure that all clients support TLS 1.2. Otherwise, the clients can't
  communicate with the servers and can be orphaned.

Tasks for Configuration Manager clients, site
servers, and remote site systems
To enable TLS 1.2 for components that Configuration Manager depends on for secure
communication, you'll need to do multiple tasks on both the clients and the site servers.

Enable TLS 1.2 for Configuration Manager clients

<!-- p.715 -->

      Update Windows and WinHTTP on Windows 8.0, Windows Server 2012 (non-R2)
      and earlier
      Ensure that TLS 1.2 is enabled as a protocol for SChannel at the OS level
      Update and configure the .NET Framework to support TLS 1.2

Enable TLS 1.2 for Configuration Manager site servers and
remote site systems
      Ensure that TLS 1.2 is enabled as a protocol for SChannel at the OS level
      Update and configure the .NET Framework to support TLS 1.2
      Update SQL Server and the SQL Server Native Client
      Update Windows Server Update Services (WSUS)

Features and scenario dependencies
This section describes the dependencies for specific Configuration Manager features
and scenarios. To determine the next steps, locate the items that apply to your
environment.

                                                                                  ﾉ   Expand table

 Feature or scenario        Update tasks

 Site servers (central,     - Update .NET Framework
 primary, or secondary)     - Verify strong cryptography settings

 Site database server       Update SQL Server and its client components

 Secondary site servers     Update SQL Server and its client components to a compliant version
                            of SQL Server Express

 Site system roles          - Update .NET Framework and verify strong cryptography settings
                            - Update SQL Server and its client components on roles that require it,
                            including the SQL Server Native Client

 Reporting services point   - Update .NET Framework on the site server, the SQL Server Reporting
                            Services servers, and any computer with the console
                            - Restart the SMS_Executive service as necessary

 Software update point      Update WSUS

 Cloud management           Enforce TLS 1.2
 gateway

 Configuration Manager      - Update .NET Framework

<!-- p.716 -->

 Feature or scenario      Update tasks

 console                  - Verify strong cryptography settings

 Configuration Manager    Update Windows to support TLS 1.2 for client-server communications
 client with HTTPS site   by using WinHTTP
 system roles

 Software Center          - Update .NET Framework
                          - Verify strong cryptography settings

 Windows 7 clients        Before you enable TLS 1.2 on any server components, update Windows
                          to support TLS 1.2 for client-server communications by using
                          WinHTTP. If you enable TLS 1.2 on server components first, you can
                          orphan earlier versions of clients.

Frequently asked questions

Why use TLS 1.2 with Configuration Manager?
TLS 1.2 is more secure than the previous cryptographic protocols such as SSL 2.0, SSL
3.0, TLS 1.0, and TLS 1.1. Essentially, TLS 1.2 keeps data being transferred across the
network more secure.

Where does Configuration Manager use encryption
protocols like TLS 1.2?
There are basically five areas that Configuration Manager uses encryption protocols like
TLS 1.2:

     Client communications to IIS-based site server roles when the role is configured to
     use HTTPS. Examples of these roles include distribution points, software update
     points, and management points.
     Management point, SMS Executive, and SMS Provider communications with SQL.
     Configuration Manager always encrypts SQL Server communications.
     Site Server to WSUS communications if WSUS is configured to use HTTPS.
     The Configuration Manager console to SQL Server Reporting Services (SSRS) if
     SSRS is configured to use HTTPS.
     Any connections to internet-based services. Examples include the cloud
     management gateway (CMG), the service connection point sync, and sync of
     update metadata from Microsoft Update.

<!-- p.717 -->

What determines which encryption protocol is used?
HTTPS will always negotiate the highest protocol version that is supported by both the
client and server in an encrypted conversation. On establishing a connection, the client
sends a message to the server with its highest available protocol. If the server supports
the same version, it sends a message using that version. This negotiated version is the
one that is used for the connection. If the server doesn't support the version presented
by the client, the server message will specify the highest version it can use. For more
information about the TLS Handshake protocol, see Establishing a Secure Session by
using TLS.

What determines which protocol version the client and
server can use?
Generally, the following items can determine which protocol version is used:

     The application can dictate which specific protocol versions to negotiate.
        Best practice dictates to avoid hard coding specific protocol versions at the
        application level and to follow the configuration defined at the component and
        OS protocol level.
        Configuration Manager follows this best practice.
     For applications written using the .NET Framework, the default protocol versions
     depend on the version of the framework they were compiled upon.
        .NET versions before 4.6.3 did not include TLS 1.1 and 1.2 in the list of protocols
        for negotiation, by default.
     Applications that use WinHTTP for HTTPS communications, like the Configuration
     Manager client, depend on the OS version, patch level, and configuration for
     protocol version support.

Additional resources
     Cryptographic controls technical reference
     Transport layer security (TLS) best practices with the .NET Framework
     KB 3135244: TLS 1.2 support for Microsoft SQL Server

Next steps
     Enable TLS 1.2 on clients
     Enable TLS 1.2 on the site servers

<!-- p.718 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.719 -->

How to enable TLS 1.2 on clients
Article • 10/18/2024

Applies to: Configuration Manager (Current Branch)

When enabling TLS 1.2 for your Configuration Manager environment, start by ensuring
the clients are capable and properly configured to use TLS 1.2 before enabling TLS 1.2
and disabling the older protocols on the site servers and remote site systems. There are
three tasks for enabling TLS 1.2 on clients:

      Update Windows and WinHTTP
      Ensure that TLS 1.2 is enabled as a protocol for SChannel at the operating system
      level
      Update and configure the .NET Framework to support TLS 1.2

For more information about dependencies for specific Configuration Manager features
and scenarios, see About enabling TLS 1.2.

Update Windows and WinHTTP
Windows 8.1, Windows Server 2012 R2, Windows 10, Windows Server 2016, and later
versions of Windows natively support TLS 1.2 for client-server communications over
WinHTTP.

Earlier versions of Windows, such as Windows 7 or Windows Server 2012, don't enable
TLS 1.1 or TLS 1.2 by default for secure communications using WinHTTP. For these
earlier versions of Windows, install Update 3140245    to enable the registry value
below, which can be set to add TLS 1.1 and TLS 1.2 to the default secure protocols list
for WinHTTP. With the patch installed, create the following registry values:

  ） Important

  Enable these settings on all clients running earlier versions of Windows before
  enabling TLS 1.2 and disabling the older protocols on the Configuration Manager
  servers. Otherwise, you can inadvertently orphan them.

Verify the value of the DefaultSecureProtocols registry setting, for example:

  Registry

<!-- p.720 -->

  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet
  Settings\WinHttp\
        DefaultSecureProtocols = (DWORD): 0xAA0
  HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Int
  ernet Settings\WinHttp\
        DefaultSecureProtocols = (DWORD): 0xAA0

If you change this value, restart the computer.

The example above shows the value of 0xAA0 for the WinHTTP DefaultSecureProtocols
setting. Update to enable TLS 1.1 and TLS 1.2 as default secure protocols in WinHTTP in
Windows     lists the hexadecimal value for each protocol. By default in Windows, this
value is 0x0A0 to enable SSL 3.0 and TLS 1.0 for WinHTTP. The above example keeps
these defaults, and also enables TLS 1.1 and TLS 1.2 for WinHTTP. This configuration
ensures that the change doesn't break any other application that might still rely on SSL
3.0 or TLS 1.0. You can use the value of 0xA00 to only enable TLS 1.1 and TLS 1.2.
Configuration Manager supports the most secure protocol that Windows negotiates
between both devices.

If you want to completely disable SSL 3.0 and TLS 1.0, use the SChannel disabled
protocols setting in Windows. For more information, see Restrict the use of certain
cryptographic algorithms and protocols in Schannel.dll.

Ensure that TLS 1.2 is enabled as a protocol for
SChannel at the operating system level
For the most part, protocol usage is controlled at three levels, the operating system
level, the framework or platform level, and the application level. TLS 1.2 is enabled by
default at the operating system level. Once you ensure that the .NET registry values are
set to enable TLS 1.2 and verify the environment is properly utilizing TLS 1.2 on the
network, you may want to edit the SChannel\Protocols registry key to disable the older,
less secure protocols. For more information on disabling TLS 1.0 and 1.1, see
Configuring Schannel protocols in the Windows Registry.

Update and configure the .NET Framework to
support TLS 1.2

Determine .NET version
