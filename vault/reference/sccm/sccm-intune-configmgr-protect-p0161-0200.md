---
title: "Protect data and infrastructure documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-protect-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-protect-p0161-0200
family: sccm
documentKind: "doc"
abstract: "７ Note For version 2010, the message processing engine channel only escrows keys for OS and fixed drive volumes. It doesn't support recovery keys for removable drives or the TPM password hash. Starting in version 2103, BitLocker management policies over a CMG support the followi"
---

# Protect data and infrastructure documentation — pages 161-200

<!-- p.161 -->

  ７ Note

  For version 2010, the message processing engine channel only escrows keys for OS
  and fixed drive volumes. It doesn't support recovery keys for removable drives or
  the TPM password hash.

  Starting in version 2103, BitLocker management policies over a CMG support the
  following capabilities:

        Recovery keys for removable drives
        TPM password hash, otherwise known as TPM owner authorization

Rotate keys
When you recover a key with the self-service or helpdesk portals, since it's disclosed,
Configuration Manager requires the client to rotate the key. Rotating the key means that
the client generates a new key for BitLocker recovery. It then escrows the new key to the
recovery service.

  ７ Note

  When you migrate from MBAM, when the device receives a BitLocker management
  policy from Configuration Manager, it first rotates its key. It then sends the new key
  to the Configuration Manager recovery service.

Next steps
Migrate from MBAM

Set up BitLocker reports and portals

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.162 -->

Migrate from MBAM
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you currently use Microsoft BitLocker Administration and Monitoring (MBAM), you can
seamlessly migrate management to Configuration Manager. When you deploy BitLocker
management policies in Configuration Manager, clients automatically rotate their keys
and upload them to the Configuration Manager recovery service.

  ） Important

  When you migrate from stand-alone MBAM to Configuration Manager BitLocker
  management, if you require existing functionality of stand-alone MBAM, don't
  reuse stand-alone MBAM servers or components with Configuration Manager
  BitLocker management. If you reuse these servers, stand-alone MBAM will stop
  working when Configuration Manager BitLocker management installs its
  components on those servers. Don't run the MBAMWebSiteInstaller.ps1 script to
  set up the BitLocker portals on stand-alone MBAM servers. When you set up
  Configuration Manager BitLocker management, use separate servers.

Group policy
If a group policy setting exists for standalone MBAM, it will override the equivalent
setting attempted by Configuration Manager. Standalone MBAM uses domain group
policy, while Configuration Manager sets local policies for BitLocker management.
Domain policies will override the local Configuration Manager BitLocker management
policies. If the standalone MBAM domain group policy doesn't match the Configuration
Manager policy, Configuration Manager BitLocker management will fail. For example, if
a domain group policy sets the standalone MBAM server for key recovery services,
Configuration Manager BitLocker management can't set the same setting for its
recovery service. This behavior causes clients to not report their recovery keys to the
Configuration Manager BitLocker management recovery service.

Don't set a group policy for a setting that Configuration Manager BitLocker
management already specifies. Only set group policies for settings that don't currently
exist in Configuration Manager BitLocker management. Configuration Manager has
feature parity with standalone MBAM. In most instances there should be no reason to
set domain group policies to configure BitLocker policies. To prevent conflicts and

<!-- p.163 -->

problems, avoid use of group policies for BitLocker. Configure all settings through
Configuration Manager BitLocker management policies.

TPM password hash
     Previous MBAM clients don't upload the TPM password hash to Configuration
     Manager. The client only uploads the TPM password hash once.

     If you need to migrate this information to the Configuration Manager recovery
     service, clear the TPM on the device. After it restarts, it uploads the new TPM
     password hash to the recovery service.

  ７ Note

  Uploading of the TPM password hash mainly pertains to versions of Windows
  before Windows 10. Windows 10 or later by default doesn't save the TPM password
  hash, so these devices don't normally upload it. For more information, see About
  the TPM owner password.

Re-encryption
Configuration Manager doesn't re-encrypt drives that are already protected with
BitLocker Drive Encryption. If you deploy a BitLocker management policy that doesn't
match the drive's current protection, it reports as non-compliant. The drive is still
protected.

For example, you used MBAM to encrypt the drive with the AES-XTS 128 encryption
algorithm, but the Configuration Manager policy requires AES-XTS 256. The drive is
non-compliant with the policy, even though the drive is encrypted.

To work around this behavior, first disable BitLocker on the device. Then deploy a new
policy with the new settings.

Next steps
About the BitLocker recovery service

Set up BitLocker reports and portals

<!-- p.164 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.165 -->

Set up BitLocker portals
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To use the following BitLocker management components in Configuration Manager, you
first need to install them:

      User self-service portal
      Administration and monitoring website (helpdesk portal)

You can install the portals on an existing site server or site system server with IIS
installed, or use a standalone web server to host them.

  ７ Note

  Starting in version 2006, you can install the BitLocker self-service portal and the
  administration and monitoring website at the central administration site.

  In version 2002 and earlier, only install the self-service portal and the
  administration and monitoring website with a primary site database. In a hierarchy,
  install these websites for each primary site.

Before you start, confirm the prerequisites for these components.

Run the script
On the target web server, do the following actions:

  ７ Note

  Depending upon your site design, you may need to run the script multiple times.
  For example, run the script on the management point to install the administration
  and monitoring website. Then run it again on a standalone web server to install the
  self-service portal.

   1. Copy the following files from SMSSETUP\BIN\X64 in the Configuration Manager
      installation folder on the site server to a local folder on the target server:

            MBAMWebSite.cab

<!-- p.166 -->

           MBAMWebSiteInstaller.ps1

   2. Run PowerShell as an administrator, and then run the script similar to the following
     command line:

        PowerShell

        .\MBAMWebSiteInstaller.ps1 -SqlServerName <ServerName> -SqlInstanceName
        <InstanceName> -SqlDatabaseName <DatabaseName> -ReportWebServiceUrl
        <ReportWebServiceUrl> -HelpdeskUsersGroupName <DomainUserGroup> -
        HelpdeskAdminsGroupName <DomainUserGroup> -MbamReportUsersGroupName
        <DomainUserGroup> -SiteInstall Both

     For example,

        PowerShell

        .\MBAMWebSiteInstaller.ps1 -SqlServerName sql.contoso.com -
        SqlInstanceName instance1 -SqlDatabaseName CM_ABC -ReportWebServiceUrl
        https://rsp.contoso.com/ReportServer -HelpdeskUsersGroupName
        "contoso\BitLocker help desk users" -HelpdeskAdminsGroupName
        "contoso\BitLocker help desk admins" -MbamReportUsersGroupName
        "contoso\BitLocker report users" -SiteInstall Both

        ） Important

        This example command line uses all of the possible parameters to show their
        usage. Adjust your use according to your requirements in your environment.

After installation, access the portals via the following URLs:

     Self-service portal: https://webserver.contoso.com/SelfService
     Administration and monitoring website: https://webserver.contoso.com/HelpDesk

  ７ Note

  Microsoft recommends but doesn't require the use of HTTPS. For more
  information, see How to set up SSL on IIS.

Script usage
This process uses a PowerShell script, MBAMWebSiteInstaller.ps1, to install these
components on the web server. It accepts the following parameters:

<!-- p.167 -->

-SqlServerName <ServerName> (required): The fully qualified domain name of the

primary site database server.

-SqlInstanceName <InstanceName> : The SQL Server instance name for the primary

site database. If SQL Server uses the default instance, don't include this parameter.

-SqlDatabaseName <DatabaseName> (required): The name of the primary site

database, for example CM_ABC .

-ReportWebServiceUrl <ReportWebServiceUrl> : The web service URL of the primary

site's reporting service point. It's the Web Service URL value in Reporting Services
Configuration Manager.

  ７ Note

  This parameter is to install the Recovery Audit Report that's linked from the
  administration and monitoring website. By default Configuration Manager
  includes the other BitLocker management reports.

-HelpdeskUsersGroupName <DomainUserGroup> : For example, contoso\BitLocker help

desk users . A domain user group whose members have access to the Manage

TPM and Drive Recovery areas of the administration and monitoring website.
When using these options, this role needs to fill in all fields, including the user's
domain and account name.

-HelpdeskAdminsGroupName <DomainUserGroup> : For example, contoso\BitLocker

help desk admins . A domain user group whose members have access to all

recovery areas of the administration and monitoring website. When helping users
recover their drives, this role only has to enter the recovery key.

-MbamReportUsersGroupName <DomainUserGroup> : For example, contoso\BitLocker
report users . A domain user group whose members have read-only access to the

Reports area of the administration and monitoring website.

  ７ Note

  The installer script doesn't create the domain user groups that you specify in
  the -HelpdeskUsersGroupName, -HelpdeskAdminsGroupName, and -
  MbamReportUsersGroupName parameters. Before you run the script, make
  sure to create these groups.

<!-- p.168 -->

       When you specify the -HelpdeskUsersGroupName, -
       HelpdeskAdminsGroupName, and -MbamReportUsersGroupName
       parameters, make sure to specify both the domain name and the group name.
       Use the format "domain\user_group" . Don't exclude the domain name. If the
       domain name or group name contains spaces or special characters, enclose
       the parameter in quotation marks ( " ).

     -SiteInstall Both : Specify which of the components to install. Valid options

     include:
        Both : Install both components

        HelpDesk : Install only the administration and monitoring website

        SSP : Install only the self-service portal

     -IISWebSite : The website where the script installs the MBAM web applications. By

     default, it uses the IIS default website. Create the custom website before using this
     parameter.

     -InstallDirectory : The path where the script installs the web application files. By

     default, this path is C:\inetpub . Create the custom directory before using this
     parameter.

     -DomainName applies to version 2002 and later: Specify the NetBIOS domain name

     of the server with the help desk or self-service web portal role. Only necessary if
     the NetBIOS domain name doesn't match the DNS domain name. This
     configuration is also known as a disjointed domain namespace. For example, -
     DomainName fabrikham where the DNS domain name is contoso.com .

     -Uninstall : Uninstalls the BitLocker Management Help Desk/Self-Service web

     portal sites on a web server where they have been previously installed.

Verify
Monitor and troubleshoot using the following logs:

     Windows Event logs under Microsoft-Windows-MBAM-Web. For more
     information, see About BitLocker event logs and Server event logs.

     Trace logs for each component are in the following default locations:

        Self-service portal: C:\inetpub\Microsoft BitLocker Management
        Solution\Logs\Self Service Website

<!-- p.169 -->

            Administration and monitoring website: C:\inetpub\Microsoft BitLocker
            Management Solution\Logs\Help Desk Website

For more troubleshooting information, see Troubleshoot BitLocker.

Next steps
Customize the self-service portal

For more information on using the components that you installed, see the following
articles:

      BitLocker administration and monitoring website
      BitLocker self-service portal

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.170 -->

Customize the self-service portal
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install the BitLocker self-service portal, you can customize it for your
organization. Add a custom notice, your organization name, and other organization-
specific information.

Branding
Brand the self-service portal with your organization's name, help desk URL, and notice
text.

   1. On the web server that hosts the self-service portal, sign in as an administrator.

   2. Start the Internet Information Services (IIS) Manager (run inetmgr.exe).

   3. Expand Sites, expand Default Web Site, and select the SelfService node. In the
        details pane, ASP.NET group, open Application Settings.

                                                                                       

   4. Select the item that you want to change, and in the Actions pane, select Edit.
        Change the Value to the new name that you want to use.

          Ｕ Caution

<!-- p.171 -->

        Don't change the Name values. For example, don't change CompanyName ,
        change Contoso IT . If you change the Name values, the self-service portal will
        stop working.

The changes take effect immediately.

Supported branding values
For the values that you can set, see the following table:

                                                                                    ﾉ   Expand table

 Name             Description                                                       Default value

 CompanyName      The organization name that the self-service portal displays       Contoso IT
                  as a header at the top of every page.

 DisplayNotice    Display an initial notice that the user has to acknowledge.       true

 HelpdeskText     The string in the right pane below "For all other related         Contact
                  issues"                                                           Helpdesk or IT
                                                                                    Department

 HelpdeskUrl      The link for the HelpdeskText string.                             (empty)

 NoticeTextPath   The text of the initial notice that the user has to               Notice.txt
                  acknowledge. By default, the full file path on the web server
                  is C:\inetpub\Microsoft BitLocker Management
                  Solution\Self Service Website\Notice.txt . Edit and save
                  the file in a plain text editor. This path value is relative to
                  the SelfService application.

For a screenshot of the default self-service portal, see BitLocker self-service portal.

   Tip

  If necessary, you can localize some of these strings to display in different
  languages. For more information, see Localization.

Session time-out
To make the user's session expire after a specified period of inactivity, you can change
the session time-out setting for the self-service portal.

<!-- p.172 -->

   1. On the web server that hosts the self-service portal, sign in as an administrator.

   2. Start the Internet Information Services (IIS) Manager (run inetmgr.exe).

   3. Expand Sites, expand Default Web Site, and select the SelfService node. In the
     details pane, ASP.NET group, open Session State.

   4. In the Cookie Settings group, change the Time-out (in minutes) value. It's the
     number of minutes after which the user's session expires. The default value is 5 . To
     disable the setting, so that there's no time-out, set the value to 0 .

   5. In the Actions pane, select Apply.

Localize helpdesk text and URL
You can configure localized versions of the self-service portal HelpdeskText statement
and HelpdeskUrl link. This string informs users how to get additional help when they
use the portal. If you configure localized text, the portal displays the localized version for
web browsers in that language. If it doesn't find a localized version, it displays the
default value in the HelpdeskText and HelpdeskUrl settings.

   1. On the web server that hosts the self-service portal, sign in as an administrator.

   2. Start the Internet Information Services (IIS) Manager (run inetmgr.exe).

   3. Expand Sites, expand Default Web Site, and select the SelfService node. In the
     details pane, ASP.NET group, open Application Settings.

   4. In the Actions pane, select Add.

   5. In the Add Application Setting window, configure the following values:

           Name: enter HelpdeskText_<language> , where <language> is the language
           code for the text.

           For example, to create a localized HelpdeskText statement in Spanish (Spain),
           the name is HelpdeskText_es-es .

           Value: the localized string to display in the right pane of the self-service
           portal below "For all other related issues"

   6. Select OK to save the new setting.

   7. Repeat this process to add a new application setting for HelpdeskUrl_<language>
     that matches the associated HelpdeskText_<language> setting.

<!-- p.173 -->

Repeat this process to add a pair of settings for all languages that you support in your
organization.

Localize the notice file
You can configure localized versions of the initial notice that the user has to
acknowledge in the self-service portal. By default, the full file path on the web server is
C:\inetpub\Microsoft BitLocker Management Solution\Self Service Website\Notice.txt .

To display localized notice text, create a localized notice.txt file. Then save it under a
specific language folder. For example: Self Service Website\es-es\Notice.txt for
Spanish (Spain).

The self-service portal displays the notice text based on the following rules:

     If the default notice file is missing, the portal displays a message that the default
     file is missing.

     If you create a localized notice file in the appropriate language folder, it displays
     the localized notice text.

     If the web server doesn't find a localized version of the notice file, it displays the
     default notice.

     If the user sets their browser to a language that doesn't have a localized notice, the
     portal displays the default notice.

Create a localized notice file
   1. On the web server that hosts the self-service portal, sign in as an administrator.

   2. Create a <language> folder for each supported language in the Self Service
     Website application path. For example, es-es for Spanish (Spain). By default, the

     full path is C:\inetpub\Microsoft BitLocker Management Solution\Self Service
     Website\es-es .

     For a list of the valid language codes you can use, see National Language Support
     (NLS) API Reference.

         Tip

        The name of the language folder can also be the language neutral name. For
        example, es for Spanish, instead of es-es for Spanish (Spain) and es-ar for

<!-- p.174 -->

        Spanish (Argentina). If the user sets their browser to es-es, and that language
        folder doesn't exist, the web server recursively checks the parent locale folder
        (es). (The parent locales are defined in .NET.) For example, Self Service
        Website\es\Notice.txt . This recursive fallback mimics the .NET resource

        loading rules.

   3. Create a copy of your default notice file with the localized text. Save it in the folder
     for the language code. For example, for Spanish (Spain), by default the full path is
      C:\inetpub\Microsoft BitLocker Management Solution\Self Service Website\es-
     es\Notice.txt .

Repeat this process to a localized notice file for all languages that you support in your
organization.

Next steps
Now that you've installed and customized the self-service portal, try it out! For more
information, see BitLocker self-service portal.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.175 -->

View BitLocker reports
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install the reports on the reporting services point, you can view the reports.
The reports show BitLocker compliance for the enterprise and for individual devices.
They provide tabular information and charts, and have filters that let you view data from
different perspectives.

In the Configuration Manager console, go to the Monitoring workspace, expand
Reporting, and select the Reports node. The following reports are in the BitLocker
Management category:

      BitLocker Computer Compliance

      BitLocker Enterprise Compliance Dashboard

      BitLocker Enterprise Compliance Details

      BitLocker Enterprise Compliance Summary

      Recovery Audit Report

You can access all of these reports directly from the reporting services point website.

  ７ Note

  For these reports to display complete data:

        Create and deploy a BitLocker management policy to a device collection
        Clients in the target collection need to send hardware inventory

BitLocker computer compliance
Use this report to collect information that's specific to a computer. It provides detailed
encryption information about the OS drive and any fixed data drives. To view the details
of each drive, expand the Computer Name entry. It also indicates the policy that's
applied to each drive type on the computer.

<!-- p.176 -->

                                                                                           

You can also use this report to determine the last known BitLocker encryption status of
lost or stolen computers. Configuration Manager determines compliance of the device
based on the BitLocker policies that you deploy. Before you try to determine the
BitLocker encryption state of a device, verify the policies that you've deployed to it.

  ７ Note

  This report doesn't show the Removable Data Volume encryption status.

Computer details

                                                                              ﾉ     Expand table

 Column name         Description

 Computer name       User-specified DNS computer name.

 Domain name         Fully qualified domain name for the computer.

 Computer Type       Type of computer, valid types are Non-Portable and Portable.

 Operating system    OS type of the computer.

<!-- p.177 -->

Column name             Description

Overall                 Overall BitLocker compliance status of the computer. Valid states are
compliance              Compliant and Non-compliant. The compliance status per drive may
                        indicate different compliance states. However, this field represents that
                        compliance state from the specified policy.

Operating system        Compliance status of the OS on the computer. Valid states are Compliant
compliance              and Non-compliant.

Fixed data drive        Compliance status of a fixed data drive on the computer. Valid states are
compliance              Compliant and Non-compliant.

Last update date        Date and time that the computer last contacted the server to report
                        compliance status.

Exemption               Indicates whether the user is exempt or non-exempt from the BitLocker
                        policy.

Exempted user           The user who's exempt from the BitLocker policy.

Exemption date          Date on which the exemption was granted.

Compliance status       Error and status messages about the compliance state of the computer from
details                 the specified policy.

Policy cipher           Cipher strength that you selected in the BitLocker management policy.
strength

Policy: Operating       Indicates if encryption is required for the OS drive and the appropriate
system drive            protector type.

Policy: Fixed data      Indicates if encryption is required for the fixed data drive.
drive

Manufacturer            Computer manufacturer name as it appears in the computer BIOS.

Model                   Computer manufacturer model name as it appears in the computer BIOS.

Device users            Known users on the computer.

Computer volume

                                                                                        ﾉ   Expand table

Column name          Description

Drive letter         The drive letter on the computer.

<!-- p.178 -->

 Column name       Description

 Drive type        Type of drive. Valid values are Operating System Drive and Fixed Data Drive.
                   These entries are physical drives rather than logical volumes.

 Cipher            Cipher strength that you selected during in the BitLocker management policy.
 strength

 Protector types   Type of protector that you selected in the policy to encrypt the drive. The valid
                   protector types for an OS drive are TPM or TPM+PIN. The valid protector type
                   for a fixed data drive is Password.

 Protector state   Indicates that the computer enabled the protector type specified in the policy.
                   The valid states are ON or OFF.

 Encryption        Encryption state of the drive. Valid states are Encrypted, Not Encrypted, or
 state             Encrypting.

BitLocker enterprise compliance dashboard
This report provides the following graphs, which show BitLocker compliance status
across your organization:

     Compliance status distribution

     Non-compliant - Errors distribution

     Compliance status distribution by drive type

<!-- p.179 -->

                                                                                  

Compliance status distribution
This pie chart shows compliance status for computers in the organization. It also shows
the percentage of computers with that compliance status, compared to the total
number of computers in the selected collection. The actual number of computers with
each status is also shown.

The pie chart shows the following compliance statuses:

     Compliant

     Non-compliant

     User exempt

     Temporary user exempt

     Policy not enforced

       ７ Note

<!-- p.180 -->

       This state may be caused by a device that's encrypted and previously
       escrowed its key, but can't currently escrow its key. Because it can't escrow its
       key it doesn't enforce policy anymore.

     Unknown. These computers reported a status error, or they're part of the collection
     but have never reported their compliance status. The lack of a compliance status
     could occur if the computer is disconnected from the organization.

Non-compliant - Errors distribution
This pie chart shows the categories of computers in your organization that aren't
compliant with the BitLocker Drive Encryption policy. It also shows the number of
computers in each category. The report calculates each percentage from the total
number of non-compliant computers in the collection.

     User postponed encryption

     Unable to find compatible TPM

     System partition not available or large enough

     TPM visible but not initialized

     Policy conflict

     Waiting for TPM auto provisioning

     An unknown error has occurred

     No information. These computers don't have the BitLocker management agent
     installed, or it's installed but not activated. For example, the service isn't working.

Compliance status distribution by drive type
This bar chart shows the current BitLocker compliance status by drive type. The statuses
are Compliant and Non-compliant. Bars are shown for fixed data drives and OS drives.
The report includes computers without a fixed data drive, and only shows a value in the
Operating System Drive bar. The chart doesn't include users who have been granted an
exemption from the BitLocker Drive Encryption policy or the No Policy category.

BitLocker enterprise compliance details

<!-- p.181 -->

This report shows information about the overall BitLocker compliance across your
organization for the collection of computers to which you deployed the BitLocker
management policy.

                                                                                          

                                                                              ﾉ   Expand table

 Column name          Description

 Managed computers    Number of computers to which you deployed a BitLocker management
                      policy.

 % Compliant          Percentage of compliant computers in the organization.

 % Non-compliant      Percentage of non-compliant computers in the organization.

 % Unknown            Percentage of computers with a compliance state that's not known.
 compliance

 % Exempt             Percentage of computers exempt from the BitLocker encryption
                      requirement.

 % Non-exempt         Percentage of computers not exempt from the BitLocker encryption
                      requirement.

 Compliant            Count of compliant computers in the organization.

 Non-Compliant        Count of non-compliant computers in the organization.

 Unknown Compliance   Count of computers with a compliance state that's not known.

 Exempt               Count of computers that are exempt from the BitLocker encryption
                      requirement.

 Non-exempt           Count of computers that aren't exempt from the BitLocker encryption
                      requirement.

<!-- p.182 -->

Computer details

                                                                             ﾉ   Expand table

 Column name          Description

 Computer name        DNS computer name of the managed device.

 Domain name          Fully qualified domain name for the computer.

 Compliance status    Overall compliance status of the computer. Valid states are Compliant
                      and Non-compliant.

 Exemption            Indicates whether the user is exempt or non-exempt from the BitLocker
                      policy.

 Device users         Users of the device.

 Compliance status    Error and status messages about the compliance state of the computer
 details              from the specified policy.

 Last contact         Date and time that the computer last contacted the server to report
                      compliance status.

BitLocker enterprise compliance summary
Use this report to show the overall BitLocker compliance across your organization. It
also shows the compliance for individual computers to which you deployed the
BitLocker management policy.

                                                                                            

<!-- p.183 -->

                                                                              ﾉ    Expand table

 Column name             Description

 Managed computers       Number of computers that you manage with BitLocker policy.

 % Compliant             Percentage of compliant computers in your organization.

 % Non-compliant         Percentage of non-compliant computers in your organization.

 % Unknown               Percentage of computers with a compliance state that's not known.
 compliance

 % Exempt                Percentage of computers exempt from the BitLocker encryption
                         requirement.

 % Non-exempt            Percentage of computers not exempt from the BitLocker encryption
                         requirement.

 Compliant               Count of compliant computers in your organization.

 Non-compliant           Count of non-compliant computers in your organization.

 Unknown compliance      Count of computers with a compliance state that's not known.

 Exempt                  Count of computers that are exempt from the BitLocker encryption
                         requirement.

 Non-exempt              Count of computers that aren't exempt from the BitLocker encryption
                         requirement.

Recovery audit report

  ７ Note

  This report is only available from the BitLocker administration and monitoring
  website.

Use this report to audit users who have requested access to BitLocker recovery keys. You
can filter on the following criteria:

     A specific type of user, for example, a help desk user or an end user
     If the request failed or was successful
     The specific type of key requested: Recovery Key Password, Recovery Key ID, or
     TPM Password Hash
     A date range during which the retrieval occurred

<!-- p.184 -->

                                                                                               

                                                                                 ﾉ    Expand table

Column name      Description

Request date     Date and time that an end user or help desk user requested a key.
and time

Audit request    The site from where the request came. Valid values are Self-Service Portal or
source           Helpdesk.

Request result   Status of the request. Valid values are Successful or Failed.

Helpdesk user    The administrative user who requested the key. If a helpdesk admin recovers
                 the key without specifying the user name, the End User field is blank. A
                 standard helpdesk user must specify the user name, which appears in this field.
                 For recovery via the self-service portal, this field and the End User field display
                 the name of the user making the request.

End user         Name of the user who requested key retrieval.

Computer         Name of the computer that was recovered.

Key type         Type of key that the user requested. The three types of keys are:

                 - Recovery key password: used to recover a computer in recovery mode
                 - Recovery key ID: used to recover a computer in recovery mode for another
                 user
                 - TPM password hash: used to recover a computer with a locked TPM

Reason           Why the user requested the specified key type, based upon the option they
description      selected in the form.

<!-- p.185 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.186 -->

BitLocker administration and
monitoring website
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

The BitLocker administration and monitoring website is an administrative interface for
BitLocker Drive Encryption. It's also referred to as the help desk portal. Use this website
to review reports, recover users' drives, and manage device TPMs.

                                                                                      

Before you can use it, install this component on a web server. For more information, see
Set up BitLocker reports and portals.

Access the administration and monitoring website via the following URL:
https://webserver.contoso.com/HelpDesk

  ７ Note

  You can view the Recovery Audit Report in the administration and monitoring
  website. You add other BitLocker management reports to the reporting services
  point. For more information, see View BitLocker reports.

<!-- p.187 -->

Groups
To access specific areas of the administration and monitoring website, your user account
needs to be in one of the following groups. Create these groups in Active Directory
using any name you want. When you install this website, you specify these group names.
For more information, see Set up BitLocker reports and portals.

                                                                                  ﾉ   Expand table

 Group          Description

 BitLocker      Provides access to all areas of the administration and monitoring website. When
 help desk      you help a user recover their drives, you enter only the recovery key, and not the
 admins         domain and user name. If a user is a member of both this group and the BitLocker
                help desk users group, the admin group permissions override the user group
                permissions.

 BitLocker      Provides access to the Manage TPM and Drive Recovery areas of the
 help desk      administration and monitoring website. When you use either area, you need to fill
 users          in all fields including the user's domain and account name. If a user is a member of
                both this group and the BitLocker help desk admins group, the admin group
                permissions override the user group permissions.

 BitLocker      Provides access to the Reports area of the administration and monitoring website.
 report users

Manage TPM
If a user enters the incorrect PIN too many times, they can lockout the TPM. The number
of times that a user can enter an incorrect PIN before the TPM locks varies from
manufacturer to manufacturer. From the Manage TPM area of the administration and
monitoring website, access the centralized key recovery data system.

For more information about TPM ownership, see Configure MBAM to escrow the TPM
and store OwnerAuth passwords.

  ７ Note

  Starting with Windows 10, version 1607, Windows doesn't keep the TPM owner
  password when provisioning the TPM.

   1. Go to the administration and monitoring website in the web browser, for example
      https://webserver.contoso.com/HelpDesk .

<!-- p.188 -->

2. In the left pane, select the Manage TPM area.

3. Enter the fully qualified domain name for the computer and the computer name.

4. If necessary, enter the user's domain and user name to retrieve the TPM owner
  password file.

5. Choose one of the following options for the Reason for requesting TPM owner
  password file:

        Reset PIN lockout
        Turn on TPM
        Turn off TPM
        Change TPM password
        Clear TPM
        Other

  After you Submit the form, the website returns one of the following responses:

        If it can't find a matching TPM owner password file, it returns an error
        message.

        The TPM owner password file for the submitted computer

  After you retrieve the TPM owner password file, the website displays the owner
  password.

6. To save the password to a file, select Save.

<!-- p.189 -->

   7. In the Manage TPM area, select the Reset TPM lockout option, and provide the
     TPM owner password file.

     The TPM lockout is reset. BitLocker restores the user's access to the device.

       ） Important

       Don't share the TPM hash value or TPM owner password file.

Drive recovery

   Tip

  Starting in version 2107, you can also get BitLocker recovery keys for a tenant-
  attached device from the Microsoft Intune admin center. For more information, see
  Tenant attach: BitLocker recovery keys.

Recover a drive in recovery mode
Drives go into recovery mode in the following scenarios:

     The user loses or forgets their PIN or password
     The Trusted Module Platform (TPM) detects changes to the BIOS or startup files of
     the computer

To get a recovery password, use the Drive recovery area of the administration and
monitoring website.

  ） Important

  Recovery passwords expire after a single use. On OS drives and fixed data drives,
  the single-use rule automatically applies. On removable drives, it applies when you
  remove and reinsert the drive.

   1. Go to the administration and monitoring website in the web browser, for example
     https://webserver.contoso.com/HelpDesk .

   2. In the left pane, select the Drive Recovery area.

<!-- p.190 -->

3. If necessary, enter the user's domain and user name to view recovery information.

4. To see a list of possible matching recovery keys, enter the first eight digits of the
  recovery key ID. To get the exact recovery key, enter the entire recovery key ID.

5. Choose one of the following options as the Reason for Drive Unlock:

        Operating system boot order changed
        BIOS changed
        Operating system files modified
        Lost startup key
        Lost PIN
        TPM reset
        Lost passphrase
        Lost smartcard
        Other

  After you Submit the form, the website returns one of the following responses:

        If the user has multiple matching recovery passwords, it returns multiple
        possible matches.

        The recovery password and recovery package for the submitted user.

          ７ Note

          If you're recovering a damaged drive, the recovery package option
          provides BitLocker with critical information that it needs to recover the
          drive.

<!-- p.191 -->

          If it can't find a matching recovery password, it returns an error message.

     After you retrieve the recovery password and recovery package, the website
     displays the recovery password.

   6. To copy the password, select Copy Key. To save the recovery password to a file,
     select Save.

To unlock the drive, enter the recovery password or use the recovery package.

Recover a moved drive
When you move a drive to a new computer, because the TPM is different, BitLocker
doesn't accept the previous PIN. To recover the moved drive, get the recovery key ID to
retrieve the recovery password.

To recover a moved drive, use the Drive recovery area of the administration and
monitoring website.

   1. On the computer with the moved drive, start the computer in Windows Recovery
     Environment (WinRE) mode.

   2. In WinRE, BitLocker treats the moved OS drive as a fixed data drive. BitLocker
     displays the drive's recovery password ID and prompts for the recovery password.

       ７ Note

       In some situations, during the startup process select I forgot the PIN if the
       option is available. Then enter recovery mode to display the recovery key ID.

   3. Use the recovery key ID to get the recovery password from the administration and
     monitoring website. For more information, see Recover a drive in recovery mode.

If you configured the moved drive to use a TPM chip on the original computer,
complete the following steps. Otherwise, the recovery process is complete.

   1. After you unlock the drive, start the computer in WinRE mode. Open a command
     prompt in WinRE, and use the manage-bde command to decrypt the drive. This tool
     is the only way to remove the TPM + PIN protector without the original TPM chip.
     For more information about this command, see Manage-bde.

   2. When it's complete, start the computer normally. Configuration Manager will
     enforce the BitLocker policy to encrypt the drive with the new computer's TPM
     plus PIN.

<!-- p.192 -->

Recover a corrupted drive
Use the recovery key ID to get a recovery key package from the administration and
monitoring website. For more information, see Recover a drive in recovery mode.

   1. Save the Recovery Key Package on your computer, then copy it to the computer
     with the corrupted drive.

   2. Open a command prompt as an administrator, and type the following command:

     repair-bde <corrupted drive> <fixed drive> -kp <key package> -rp <recovery
     password>

     Replace the following values:

           <corrupted drive> : The drive letter of the corrupted drive, for example D:

           <fixed drive> : The drive letter of an available hard disk drive of similar or

           larger size than the corrupted drive. BitLocker recovers and moves data on
           the corrupted drive to the specified drive. All data on this drive is overwritten.
           <key package> : The location of the recovery key package
           <recovery password> : The associated recovery password

     For example:

     repair-bde C: D: -kp F:\RecoveryKeyPackage -rp 111111-222222-333333-444444-

     555555-666666-777777-888888

For more information about this command, see Repair-bde.

Reports
The administration and monitoring website includes the Recovery Audit Report. Other
reports are available from the Configuration Manager reporting services point. For more
information, see View BitLocker reports.

   1. Go to the administration and monitoring website in the web browser, for example
     https://webserver.contoso.com/HelpDesk .

   2. In the left pane, select the Reports area.

   3. From the top menu bar, select the Recovery Audit Report.

For more information on this report, see Recovery Audit Report

<!-- p.193 -->

   Tip

  To save report results, select Export on the Reports menu bar.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.194 -->

BitLocker self-service portal
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you install the BitLocker self-service portal, if BitLocker locks a user's device, they
can independently get access to their computers. The self-service portal requires no
assistance from help desk staff.

                                                                                         

  ） Important

  To get a recovery key from the self-service portal, a user must have successfully
  signed in to the computer at least once. This sign-in must be local to the device,
  not in a remote session. Otherwise, they need to contact the help desk for key

<!-- p.195 -->

  recovery. A help desk administrator can use the administration and monitoring
  website to request the recovery key.

BitLocker can lock the device in the following situations:

     The user forgets their BitLocker password or PIN

     There's a change to the device's OS files, BIOS, or Trusted Platform Module (TPM)

To request the BitLocker recovery key from the self-service portal:

   1. When BitLocker locks a device, it displays the BitLocker recovery screen during
     startup. Write down the 32-digit BitLocker recovery key ID.

   2. On another computer, go to the self-service portal in the web browser, for example
      https://webserver.contoso.com/SelfService .

   3. Read and accept the notice.

   4. In the Recovery Key ID field, enter the first eight digits of the BitLocker recovery
     key ID. If it matches multiple keys, then enter all 32 digits.

   5. Choose one of the following options for the Reason for this request:

             BIOS/TPM changed
             OS filed modified
             Lost PIN/passphrase

   6. Select Get Key. The self-service portal displays the 48-digit BitLocker recovery key.

   7. Enter this 48-digit code into the BitLocker recovery screen on your computer.

  ７ Note

  The BitLocker self-service portal may timeout after a period of inactivity. For
  example, after five minutes you may see a timeout warning with a 60 second
  counter.

<!-- p.196 -->

  If you don't respond to the countdown, the session will expire.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.197 -->

SQL Always On when BitLocker recovery
data is encrypted in the database
06/12/2025

For SQL Always On, additional steps are required when the BitLocker information is encrypted
using the instructions at Encrypt recovery data in the database. The additional steps ensure
that all Always On nodes can automatically open the Database Master Key (DMK) when a
failover event occurs. Following steps allows seamless retrieval of BitLocker keys without
manual intervention.

Overview of SQL Always On when BitLocker
recovery data is encrypted in the database
SQL Server encrypts data using a hierarchical infrastructure and is described in depth at
Encryption Hierarchy.

      Site Master Key (SMK) - This key is a per instance key that is unique to each SQL Server
      Always On node and isn't replicated. It's used to encrypt the database master key.
      Database Master Key (DMK) - This key is stored in the database and is replicated. It's
      used to encrypt the BitLockerManagement_CERT.
      BitLockerManagement_CERT - This certificate is stored in the database and is replicated.
      It's used to encrypt some BitLocker-related data like recovery keys.

The SMK encrypts the DMK password. SMKs are node-specific. When a failover event occurs,
the new primary node can't decrypt the DMK password since it was encrypted with a different
SMK. Setting the DMK password on each node allows the node to decrypt the password on
failover.

  ７ Note

  The BitLockerManagement_CERT performs the encryption of the columns. If this certificate
  is lost or deleted, or the DMK that encrypted it's lost or deleted, BitLocker keys have to be
  escrowed and re-encrypted again.

If the Database Master Key (DMK) password is
known

<!-- p.198 -->

Execute the following command on each node in the Availability Group that hosts the
Configuration Manager database:

  ） Important

  In the following command:

        Replace password everywhere with a strong password of your choosing. Make sure
        to securely store the password for future reference.
        Replace CM_XXX with the name of the Configuration Manager (CM) database.

  SQL

  EXEC sp_control_dbmasterkey_password
      @db_name = N'CM_XXX',
      @password = N'password',
      @action = N'add';

This command registers the DMK password with the local Service Master Key (SMK) allowing
SQL Server to automatically open the DMK when a failover event occurs. This process ensures
the DMK can be decrypted automatically on that node after a failover or a restart.

To verify that all nodes can automatically open the Database Master Key (DMK) and decrypt the
data, see the section Verify all nodes can automatically open the Database Master Key (DMK)
and decrypt the data in this article.

If the existing Database Master Key (DMK)
password is unknown
If the existing DMK password is unknown, the existing DMK must be dropped and a new one
created with a known password. These steps document how to perform this procedure.

Find a valid DMK
If it's unknown which node has a valid DMK, follow these steps to determine where the existing
DMK is open:

  ） Important

  In the following queries and commands:

<!-- p.199 -->

        Replace password everywhere with a strong password of your choosing. Make sure
        to securely store the password in a known location for future reference.
        Replace CM_XXX with the name of the Configuration Manager (CM) database.

   1. Run the following query on the primary node:

        SQL

        SELECT TOP 5 RecoveryAndHardwareCore.DecryptString(RecoveryKey, DEFAULT)
        FROM RecoveryAndHardwareCore_Keys
        ORDER BY LastUpdateTime DESC

   2. In the resultant query:

           If the DMK is open, the query returns plaintext values for any rows that have a valid
           key in them. This node is the node to start on and the next step can be skipped.
           If the DMK isn't open, the query returns NULL values for all rows. The current node
           isn't the node where the DMK is open. Follow the next step to find the node where
           the DMK is open.

   3. If the query returns all NULL values, then failover to each secondary node and repeat the
     previous steps until the node that can successfully decrypt
     RecoveryAndHardwareCore_Keys is found. This node is the node to start on.

Create a new Database Master Key (DMK)
Once the proper node with the open DMK is identified, follow these steps:

   1. On the node that was identified in the previous steps, run the following query to export
     the BitLockerManagement_CERT certificate with its private key. Make sure to use a strong
     password:

        SQL

        BACKUP CERTIFICATE BitLockerManagement_CERT
        TO FILE = 'C:\Windows\Temp\BitLockerManagement_CERT'
        WITH PRIVATE KEY
        (
            FILE = 'C:\Windows\Temp\BitLockerManagement_CERT_KEY',
            ENCRYPTION BY PASSWORD = 'password'
        );

   2. Back up the existing Database Master Key (DMK) by running the following query to
     export the existing DMK:

<!-- p.200 -->

    SQL

    BACKUP MASTER KEY
    TO FILE = 'C:\Windows\Temp\DMK'
    ENCRYPTION BY PASSWORD = 'password';

    ７ Note

    This step is optional but recommended. Make sure to keep the backup in a secure
    known location.

3. Run the following query to drop the existing certificate and DMK:

    SQL

    DROP CERTIFICATE BitLockerManagement_CERT;
    DROP MASTER KEY;

  This step removes the old keys.

4. Run the following query to create a new DMK. Make sure to use a strong password:

    SQL

    CREATE MASTER KEY
    ENCRYPTION BY PASSWORD = 'password';

5. Run the following query to register the new DMK password with the local SMK:

    SQL

    EXEC sp_control_dbmasterkey_password
        @db_name = N'CM_XXX',
        @password = N'password',
        @action = N'add';

6. Run the following query to import the previously exported BitLockerManagement_CERT
  certificate:

    SQL

    CREATE CERTIFICATE BitLockerManagement_CERT AUTHORIZATION
    RecoveryAndHardwareCore
    FROM FILE = 'C:\Windows\Temp\BitLockerManagement_CERT'
    WITH PRIVATE KEY
