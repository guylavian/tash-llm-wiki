---
title: "Core infrastructure documentation — pages 2241-2280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2241-2280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2241-2280
family: sccm
documentKind: "doc"
abstract: "When the device downloads client installation files over an HTTP connection, use this parameter to specify the download priority. Specify one of the following possible values: FOREGROUND HIGH NORMAL (default) LOW Example: ccmsetup.exe /BITSPriority:HIGH /config This parameter sp"
---

# Core infrastructure documentation — pages 2241-2280

<!-- p.2241 -->

When the device downloads client installation files over an HTTP connection, use this
parameter to specify the download priority. Specify one of the following possible values:

      FOREGROUND

      HIGH

      NORMAL (default)

      LOW

Example: ccmsetup.exe /BITSPriority:HIGH

/config

This parameter specifies a text file that lists client installation properties.

     If CCMSetup runs as a service, place this file in the CCMSetup system folder:
      %Windir%\Ccmsetup .

     If you specify the /noservice parameter, place this file in the same folder as
     CCMSetup.exe.

Example: CCMSetup.exe /config:"configuration file name.txt"

To provide the correct file format, use the mobileclienttemplate.tcf file in the \bin\
<platform> folder in the Configuration Manager installation directory on the site server.

This file has comments about the sections and how to use them. Specify the client
installation properties in the [Client Install] section, after the following text:
Install=INSTALL=ALL .

Example [Client Install] section entry: Install=INSTALL=ALL SMSSITECODE=ABC
SMSCACHESIZE=100

/downloadtimeout

If CCMSetup fails to download the client installation files, this parameter specifies the
maximum timeout in minutes. After this timeout, CCMSetup stops trying to download
the installation files. The default value is 1440 minutes (one day).

Use the /retry parameter to specify the interval between retry attempts.

Example: ccmsetup.exe /downloadtimeout:100

<!-- p.2242 -->

/ExcludeFeatures

This parameter specifies that CCMSetup.exe doesn't install the specified feature.

Example: CCMSetup.exe /ExcludeFeatures:ClientUI doesn't install Software Center on
the client.

  ７ Note

   ClientUI is the only value that the /ExcludeFeatures parameter supports.

/forceinstall

Specify that CCMSetup.exe uninstalls any existing client, and installs a new client.

/forcereboot

Use this parameter to force the computer to restart if necessary to complete the
installation. If you don't specify this parameter, CCMSetup exits when a restart is
necessary. It then continues after the next manual restart.

Example: CCMSetup.exe /forcereboot

/logon

If any version of the client is already installed, this parameter specifies that the client
installation should stop.

Example: ccmsetup.exe /logon

/mp

Specifies a management point for clients to use to find the nearest distribution point for
the client installation files. If there are no distribution points, or computers can't
download the files from the distribution points after four hours, they download the files
from the specified management point.

For more information on how ccmsetup downloads content, see Boundary groups -
client installation. That article also includes details of ccmsetup behavior if you use both
/mp and /source parameters.

<!-- p.2243 -->

  ） Important

  This parameter specifies an initial management point for computers to find a
  download source, and can be any management point in any site. It doesn't assign
  the client to the specified management point.

Computers download the files over an HTTP or HTTPS connection, depending on the
site system role configuration for client connections. The download can also use BITS
throttling if you configure it. If you configure all distribution points and management
points for HTTPS client connections only, verify that the client computer has a valid
client certificate.

You can use the /mp command-line parameter to specify more than one management
point. If the computer fails to connect to the first one, it tries the next in the specified
list. When you specify multiple management points, separate the values by semicolons.

If the client connects to a management point using HTTPS, specify the FQDN not the
computer name. The value must match the management point PKI certificate's Subject
or Subject Alternative Name. Although Configuration Manager supports using a
computer name in the certificate for connections on the intranet, using an FQDN is
recommended.

Example with the computer name: ccmsetup.exe /mp:SMSMP01

Example with the FQDN: ccmsetup.exe /mp:smsmp01.contoso.com

This parameter can also specify the URL of a cloud management gateway (CMG). Use
this URL to install the client on an internet-based device. To get the value for this
parameter, use the following steps:

      Create a CMG. For more information, see Set up a CMG.

      On an active client, open a Windows PowerShell command prompt as an
      administrator.

      Run the following command:

         PowerShell

         (Get-WmiObject -Namespace Root\Ccm\LocationServices -Class
         SMS_ActiveMPCandidate | Where-Object {$_.Type -eq "Internet"}).MP

      Append the https:// prefix to use with the /mp parameter.

<!-- p.2244 -->

Example for when you use the cloud management gateway URL: ccmsetup.exe
/mp:https://CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72057598037248100

  ） Important

  When specifying the URL of a cloud management gateway for the /mp parameter,
  it must start with https:// .

  ７ Note

  The /mp command-line parameter doesn't specify the management point used by
  the Configuration Manager client once it is installed. To specify the initial
  management point used by the Configuration Manager client once it is installed,
  use the SMSMP client.msi property. To specify a list of management points for the
  Configuration Manager client to use once it is installed, use the SMSMPLIST
  client.msi property.

/NoCRLCheck

Specifies that a client shouldn't check the certificate revocation list (CRL) when it
communicates over HTTPS with a PKI certificate. When you don't specify this parameter,
the client checks the CRL before it establishes an HTTPS connection. For more
information about client CRL checking, see Planning for PKI certificate revocation.

Example: CCMSetup.exe /UsePKICert /NoCRLCheck

/noservice

This parameter prevents CCMSetup from running as a service, which it does by default.
When CCMSetup runs as a service, it runs in the context of the Local System account of
the computer. This account might not have sufficient rights to access required network
resources for the installation. With /noservice , CCMSetup.exe runs in the context of the
user account that you use to start the installation.

Example: ccmsetup.exe /noservice

/regtoken

<!-- p.2245 -->

Use this parameter to provide a bulk registration token. An internet-based device uses
this token in the registration process through a cloud management gateway (CMG). For
more information, see Token-based authentication for CMG.

When you use this parameter, also include the following parameters and properties:

     /mp
     CCMHOSTNAME
     SMSSITECODE
     SMSMP

The following example command line includes the other required setup parameters and
properties:

ccmsetup.exe
/mp:https://CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72186325152220500

CCMHOSTNAME=CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72186325152220500
SMSSITECODE=ABC SMSMP=https://mp1.contoso.com

/regtoken:eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik9Tbzh2Tmd5VldRUjlDYVh5T2lac

HFlMDlXNCJ9.eyJTQ0NNVG9rZW5DYXRlZ29yeSI6IlN7Q01QcmVBdXRoVG9rZW4iLCJBdXRob3JpdHkiOiJ
TQ0NNIiwiTGljZW5zZSI6IlNDQ00iLCJUeXBlIjoiQnVsa1JlZ2lzdHJhdGlvbiIsIlRlbmFudElkIjoiQ0

RDQzVFOTEtMEFERi00QTI0LTgyRDAtMTk2NjY3RjFDMDgxIiwiVW5pcXVlSWQiOiJkYjU5MWUzMy1wNmZkL
TRjNWItODJmMy1iZjY3M2U1YmQwYTIiLCJpc3MiOiJ1cm46c2NjbTpvYXV0aDI6Y2RjYzVlOTEtMGFkZi00

YTI0LTgyZDAtMTk2NjY3ZjFjMDgxIiwiYXVkIjoidXJuOnNjY206c2VydmljZSIsImV4cCI6MTU4MDQxNbU

wNSwibmJmIjoxNTgwMTU2MzA1fQ.ZUJkxCX6lxHUZhMH_WhYXFm_tbXenEdpgnbIqI1h8hYIJw7xDk3wv62
5SCfNfsqxhAwRwJByfkXdVGgIpAcFshzArXUVPPvmiUGaxlbB83etUTQjrLIk-

gvQQZiE5NSgJ63LCp5KtqFCZe8vlZxnOloErFIrebjFikxqAgwOO4i5ukJdl3KQ07YPRhwpuXmwxRf1vsia
wXBvTMhy40SOeZ3mAyCRypQpQNa7NM3adCBwUtYKwHqiX3r1jQU0y57LvU_brBfLUL6JUpk3ri-

LSpwPFarRXzZPJUu4-mQFIgrMmKCYbFk3AaEvvrJienfWSvFYLpIYA7lg-6EVYRcCAA

   Tip

  If CCMSetup returns error 0x87d0027e, try removing the /mp parameter from the
  command line.

/retry

If CCMSetup.exe fails to download installation files, use this parameter to specify the
retry interval in minutes. CCMSetup continues to retry until it reaches the limit specified
in the /downloadtimeout parameter.

<!-- p.2246 -->

Example: ccmsetup.exe /retry:20

/service

Specifies that CCMSetup should run as a service that uses the Local System account.

   Tip

  If you're using a script to run CCMSetup.exe with the /service parameter,
  CCMSetup.exe exits after the service starts. It might not correctly report installation
  details to the script.

Example: ccmsetup.exe /service

/skipprereq

This parameter specifies that CCMSetup.exe doesn't install the specified prerequisite.
You can enter more than one value. Use the semicolon character ( ; ) to separate each
value.

Examples:

         CCMSetup.exe /skipprereq:filename.exe

         CCMSetup.exe /skipprereq:filename1.exe;filename2.exe

For more information on client prerequisites, see Windows client prerequisites.

/source

Specifies the file download location. Use a local or UNC path. The device downloads files
using the server message block (SMB) protocol. To use /source , the Windows user
account for client installation needs Read permissions to the location.

For more information on how ccmsetup downloads content, see Boundary groups -
client installation. That article also includes details of ccmsetup behavior if you use both
/mp and /source parameters.

   Tip

<!-- p.2247 -->

  You can use the /source parameter more than once in a command line to specify
  alternative download locations.

Example: ccmsetup.exe /source:"\\server\share"

/uninstall

Use this parameter to uninstall the Configuration Manager client. For more information,
see Uninstall the client.

Example: ccmsetup.exe /uninstall

  ７ Note

  Starting in version 2111, when you uninstall the client it also removes the client
  bootstrap, ccmsetup.msi, if it exists.

/UsePKICert

Specify this parameter for the client to use a PKI client authentication certificate. If you
don't include this parameter, or if the client can't find a valid certificate, it filters out all
HTTPS management points, including cloud management gateways (CMG). The client
uses an HTTP connection with a self-signed certificate.

Example: CCMSetup.exe /UsePKICert

If a device uses Microsoft Entra ID for client authentication and also has a PKI-based
client authentication certificate, if you use include this parameter the client won't be
able to get Microsoft Entra onboarding information from a cloud management gateway
(CMG). For a client that uses Microsoft Entra authentication, don't specify this
parameter, but include the AADRESOURCEURI and AADCLIENTAPPID properties.

  ７ Note

  In some scenarios, you don't have to specify this parameter, but still use a client
  certificate. For example, client push and software update-based client installation.
  Use this parameter when you manually install a client and use the /mp parameter
  with an HTTPS-enabled management point.

  Also specify this parameter when you install a client for internet-only
  communication. Use CCMALWAYSINF=1 together with the properties for the internet-

<!-- p.2248 -->

     based management point ( CCMHOSTNAME ) and the site code ( SMSSITECODE ). For more
     information about internet-based client management, see Considerations for client
     communications from the internet or an untrusted forest.

/IgnoreSkipUpgrade

Specify this parameter to manually upgrade an excluded client. For more information,
see How to exclude clients from upgrade.

CCMSetup.exe return codes
The CCMSetup.exe command provides the following return codes. To troubleshoot,
review %WinDir%\ccmsetup\Logs\ccmsetup.log on the client for context and additional
detail about return codes.

                                                                         ﾉ   Expand table

 Return code                 Meaning

 0                           Success

 6                           Error

 7                           Reboot required

 8                           Setup already running

 9                           Prerequisite evaluation failure

 10                          Setup manifest hash validation failure

Ccmsetup.msi properties
The following properties can modify the installation behavior of ccmsetup.msi.

CCMSETUPCMD

Use this ccmsetup.msi property to pass additional command-line parameters and
properties to ccmsetup.exe. Include other parameters and properties inside quotation
marks ( " ). Use this property when you bootstrap the Configuration Manager client with
the Intune MDM installation method.

<!-- p.2249 -->

Example: ccmsetup.msi CCMSETUPCMD="/mp:https://mp.contoso.com
CCMHOSTNAME=mp.contoso.com"

   Tip

  Microsoft Intune limits the command line to 1024 characters.

Client.msi properties
The following properties can modify the installation behavior of client.msi, which
ccmsetup.exe installs.

AADCLIENTAPPID

Specifies the Microsoft Entra client app identifier. You create or import the client app
when you configure Azure services for Cloud Management. An Azure administrator can
get the value for this property from the Azure portal. For more information, see get
application ID. For the AADCLIENTAPPID property, this application ID is for the Native
application type.

Example: ccmsetup.exe AADCLIENTAPPID=aa28e7f1-b88a-43cd-a2e3-f88b257c863b

AADRESOURCEURI

Specifies the Microsoft Entra server app identifier. You create or import the server app
when you configure Azure services for Cloud Management. When you create the server
app, in the Create Server Application window, this property is the App ID URI.

An Azure administrator can get the value for this property from the Azure portal. In
Microsoft Entra ID, find the server app under App registrations. Look for application
type Web app / API. Open the app, select Settings, and then select Properties. Use the
App ID URI value for this AADRESOURCEURI client installation property.

Example: ccmsetup.exe AADRESOURCEURI=https://contososerver

AADTENANTID

Specifies the Microsoft Entra tenant identifier. Configuration Manager links to this
tenant when you configure Azure services for Cloud Management. To get the value for
this property, use the following steps:

<!-- p.2250 -->

     On a device that runs Windows 10 or later and is joined to the same Microsoft
     Entra tenant, open a command prompt.

     Run the following command: dsregcmd.exe /status

     In the Device State section, find the TenantId value. For example, TenantId :
     607b7853-6f6f-4d5d-b3d4-811c33fdd49a

        ７ Note

        An Azure administrator can also obtain this value in the Azure portal. For
        more information, see get tenant ID.

Example: ccmsetup.exe AADTENANTID=607b7853-6f6f-4d5d-b3d4-811c33fdd49a

CCMADMINS

Specifies one or more Windows user accounts or groups to be given access to client
settings and policies. This property is useful when you don't have local administrative
credentials on the client computer. Specify a list of accounts that are separated by
semicolons ( ; ).

Example: CCMSetup.exe CCMADMINS="domain\account1;domain\group1"

CCMALLOWSILENTREBOOT

If necessary, allow the computer to silently restart after the client installation.

  ） Important

  When you use this property, the computer restarts without warning. This behavior
  occurs even if a user is signed in to Windows.

Example: CCMSetup.exe CCMALLOWSILENTREBOOT

CCMALWAYSINF

To specify that the client is always internet-based and never connects to the intranet, set
this property value to 1 . The client's connection type displays Always Internet.

<!-- p.2251 -->

Use this property with CCMHOSTNAME to specify the FQDN of the internet-based
management point. Also use it with the CCMSetup parameter UsePKICert and the
SMSSITECODE property.

For more information about internet-based client management, see Considerations for
client communications from the internet or an untrusted forest.

Example: CCMSetup.exe /UsePKICert CCMALWAYSINF=1 CCMHOSTNAME=SERVER3.CONTOSO.COM
SMSSITECODE=ABC

CCMCERTISSUERS

Use this property to specify the certificate issuers list. This list includes certificate
information for the trusted root certification authorities (CA) that the Configuration
Manager site trusts.

This value is a case-sensitive match for subject attributes that are in the root CA
certificate. Separate attributes by a comma ( , ) or a semicolon ( ; ). Specify more than
one root CA certificate by using a separator bar ( | ).

Example: CCMCERTISSUERS="CN=Contoso Root CA; OU=Servers; O=Contoso, Ltd; C=US |
CN=Litware Corporate Root CA; O=Litware, Inc."

   Tip

  Use the value of the CertificateIssuers attribute in the mobileclient.tcf file for the
  site. This file is in the \bin\<platform> subfolder of the Configuration Manager
  installation directory on the site server.

For more information about the certificate issuers list and how clients use it during the
certificate selection process, see Planning for PKI client certificate selection.

CCMCERTNAMECHECK

Starting in version 2207, this property can be used to skip checking the subject name for
the certificate. CCMCERTNAMECHECK=0 skips checking the subject name of the certificate.

CCMCERTSEL

If the client has more than one certificate for HTTPS communication, this property
specifies the criteria for it to select a valid client authentication certificate.

<!-- p.2252 -->

Use the following keywords to search the certificate Subject Name or Subject Alternative
Name:

      Subject : Find an exact match
      SubjectStr : Find a partial match

Examples:

      CCMCERTSEL="Subject:computer1.contoso.com" : Search for a certificate with an exact

     match to the computer name computer1.contoso.com in the Subject Name or the
     Subject Alternative Name.

      CCMCERTSEL="SubjectStr:contoso.com" : Search for a certificate that contains

      contoso.com in the Subject Name or the Subject Alternative Name.

Use the SubjectAttr keyword to search for the Object Identifier (OID) or distinguished
name attributes in the Subject Name or Subject Alternative Name.

Examples:

      CCMCERTSEL="SubjectAttr:2.5.4.11 = Computers" : Search for the organizational unit

     attribute expressed as an object identifier and named Computers .

      CCMCERTSEL="SubjectAttr:OU = Computers" : Search for the organizational unit

     attribute expressed as a distinguished name, and named Computers .

  ） Important

  If you use the Subject Name, the Subject keyword is case-sensitive, and the
   SubjectStr keyword is case-insensitive.

  If you use the Subject Alternative Name, both the Subject and the SubjectStr
  keywords are case-insensitive.

For the complete list of attributes that you can use for certificate selection, see
Supported attribute values for PKI certificate selection criteria.

If more than one certificate matches the search, and you set CCMFIRSTCERT to 1 , then
the client installer selects the certificate with the longest validity period.

CCMCERTSTORE

<!-- p.2253 -->

If the client installer can't locate a valid certificate in the default Personal certificate store
for the computer, use this property to specify an alternate certificate store name.

Example: CCMSetup.exe /UsePKICert CCMCERTSTORE="ConfigMgr"

CCMDEBUGLOGGING

This property enables debug logging when the client installs. This property causes the
client to log low-level information for troubleshooting. Avoid using this property in
production sites. Excessive logging can occur, which might make it difficult to find
relevant information in the log files. Also enable CCMENABLELOGGING.

Supported values:

      0 : Turn off debug logging (default)
      1 : Turn on debug logging

Example: CCMSetup.exe CCMDEBUGLOGGING=1

For more information, see About log files.

CCMENABLELOGGING

Configuration Manager enables logging by default.

Supported values:

      TRUE : Turn on logging (default)

      FALSE : Turn off logging

Example: CCMSetup.exe CCMENABLELOGGING=TRUE

For more information, see About log files.

CCMEVALINTERVAL

The frequency in minutes at which the client health evaluation tool (ccmeval.exe) runs.
Specify an integer value from 1 to 1440 . By default, ccmeval runs once a day (1440
minutes).

Example: CCMSetup.exe CCMEVALINTERVAL=1440

For more information on client health evaluation, see Monitor clients.

<!-- p.2254 -->

CCMEVALHOUR

The hour during the day when the client health evaluation tool (ccmeval.exe) runs.
Specify an integer value from 0 (midnight) to 23 (11:00 PM). By default, ccmeval runs at
midnight.

For more information on client health evaluation, see Monitor clients.

CCMFIRSTCERT

If you set this property to 1 , the client selects the PKI certificate with the longest validity
period.

Example: CCMSetup.exe /UsePKICert CCMFIRSTCERT=1

CCMHOSTNAME

If the client is managed over the internet, this property specifies the FQDN of the
internet-based management point.

Don't specify this option with the installation property of SMSSITECODE=AUTO . Directly
assign internet-based clients to an internet-based site.

Example: CCMSetup.exe /UsePKICert CCMHOSTNAME="SMSMP01.corp.contoso.com"

This property can specify the address of a cloud management gateway (CMG). To get
the value for this property, use the following steps:

     Create a CMG. For more information, see Set up a CMG.

     On an active client, open a Windows PowerShell command prompt as an
     administrator.

     Run the following command:

          PowerShell

          (Get-WmiObject -Namespace Root\Ccm\LocationServices -Class
          SMS_ActiveMPCandidate | Where-Object {$_.Type -eq "Internet"}).MP

     Use the returned value as-is with the CCMHOSTNAME property.

For example: ccmsetup.exe
CCMHOSTNAME=CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72057598037248100

<!-- p.2255 -->

   ） Important

   When you specify the address of a CMG for the CCMHOSTNAME property, don't
   append a prefix such as https:// . Only use this prefix with the /mp URL of a CMG.

CCMHTTPPORT

Specifies the port for the client to use when it communicates over HTTP to site system
servers. By default, this value is 80 .

Example: CCMSetup.exe CCMHTTPPORT=80

CCMHTTPSPORT

Specifies the port for the client to use when it communicates over HTTPS to site system
servers. By default, this value is 443 .

Example: CCMSetup.exe /UsePKICert CCMHTTPSPORT=443

CCMINSTALLDIR

Use this property to set the folder to install the Configuration Manager client files. By
default, it uses %WinDir%\CCM .

    Tip

   Regardless of where you install the client files, it always installs the ccmcore.dll file
   in the %WinDir%\System32 folder. On a 64-bit OS, it installs a copy of ccmcore.dll in
   the %WinDir%\SysWOW64 folder. This file supports 32-bit applications that use the 32-
   bit version of the client APIs from the Configuration Manager SDK.

Example: CCMSetup.exe CCMINSTALLDIR="C:\ConfigMgr"

CCMLOGLEVEL

Use this property to specify the level of detail to write to Configuration Manager log
files.

Supported values:

<!-- p.2256 -->

      0 : Verbose
      1 : Default

      2 : Warnings and errors
      3 : Errors only

Example: CCMSetup.exe CCMLOGLEVEL=0

For more information, see About log files.

CCMLOGMAXHISTORY

When a Configuration Manager log file reaches the maximum size, the client renames it
as a backup and creates a new log file. This property specifies how many previous
versions of the log file to keep. The default value is 1 . If you set the value to 0 , the
client doesn't keep any log file history.

Example: CCMSetup.exe CCMLOGMAXHISTORY=5

For more information, see About log files.

CCMLOGMAXSIZE

This property specifies the maximum log file size in bytes. When a log grows to the
specified size, the client renames it as a history file, and creates a new one. The default
size is 250,000 bytes, and the minimum size is 10,000 bytes.

Example: CCMSetup.exe CCMLOGMAXSIZE=300000 (300,000 bytes)

DISABLESITEOPT

Set this property to TRUE to block administrators from changing the assigned site in the
Configuration Manager control panel.

Example: CCMSetup.exe DISABLESITEOPT=TRUE

DISABLECACHEOPT

If set to TRUE, this property disables the ability of administrative users from changing
the client cache folder settings in the Configuration Manager control panel.

Example: CCMSetup.exe DISABLECACHEOPT=TRUE

<!-- p.2257 -->

DNSSUFFIX

Specify a DNS domain for clients to locate management points that you publish in DNS.
When the client locates a management point, it tells the client about other management
points in the hierarchy. This behavior means that the management point that the client
finds from DNS can be any one in the hierarchy.

  ７ Note

  You don't have to specify this property if the client is in the same domain as a
  published management point. In that case, the client's domain is automatically
  used to search DNS for management points.

For more information about DNS publishing as a service location method for
Configuration Manager clients, see Service location and how clients determine their
assigned management point.

  ７ Note

  By default, Configuration Manager doesn't enable DNS publishing.

Example: CCMSetup.exe SMSSITECODE=ABC DNSSUFFIX=contoso.com

FSP

Specify the fallback status point that receives and processes state messages sent by
Configuration Manager clients.

For more information, see Determine if you need a fallback status point.

Example: CCMSetup.exe FSP=SMSFP01

IGNOREAPPVVERSIONCHECK

If you set this property to TRUE , the client installer doesn't check the minimum required
version of Microsoft Application Virtualization (App-V).

  ） Important

<!-- p.2258 -->

  If you install the Configuration Manager client without installing App-V, you can't
  deploy virtual applications.

Example: CCMSetup.exe IGNOREAPPVVERSIONCHECK=TRUE

MANAGEDINSTALLER

If you set this property to 1 then ccmsetup.exe and client.msi are set as managed
installers. For more information, see Automatically allow apps deployed by a managed
installer with Windows Defender Application Control.

Example: CCMSetup.exe MANAGEDINSTALLER=1

NOTIFYONLY

When you enable this property, the client reports status, but doesn't remediate
problems that it finds.

Example: CCMSetup.exe NOTIFYONLY=TRUE

For more information, see How to configure client status.

PROVISIONTS

Use this property to start a task sequence on a client after it successfully registers with
the site.

  ７ Note

  If the task sequence installs software updates or applications, clients need a valid
  client authentication certificate. Token authentication alone doesn't work.

For example, you provision a new Windows device with Windows Autopilot, auto-enroll
it to Microsoft Intune, and then install the Configuration Manager client for co-
management. If you specify this new option, the newly provisioned client then runs a
task sequence. This process gives you additional flexibility to install applications and
software updates, or configure settings.

Use the following process:

<!-- p.2259 -->

   1. Create a non-OS deployment task sequence to install apps, install software
     updates, and configure settings.

   2. Deploy this task sequence to the new built-in collection, All Provisioning Devices.
     Note the task sequence deployment ID, for example PRI20001 .

         Tip

        The deployment's purpose can be either available or required. Since you
        specify the deployment ID as the property value, the purpose doesn't matter.

   3. Install the Configuration Manager client on a device using ccmsetup.msi, and
     include the following property: PROVISIONTS=PRI20001 . Set the value of this
     property as the task sequence deployment ID.

           If you're installing the client from Intune during co-management enrollment,
           see How to prepare internet-based devices for co-management.

              ７ Note

              This method may have additional prerequisites. For example, enrolling
              the site to Microsoft Entra ID, or creating a content-enabled cloud
              management gateway.

              Regardless the method, only use this property with ccmsetup.msi.

After the client installs and properly registers with the site, it starts the referenced task
sequence. If client registration fails, the task sequence won't start.

  ７ Note

  The task sequence launched by PROVISIONTS uses the Default Client Settings. This
  task sequence starts immediately after the client registers, so it won't be part of any
  collection to which you've deployed custom client settings. The client doesn't
  process or apply custom client settings before this task sequence runs.

  For the task sequence to work properly, you may need to change certain settings in
  the Default Client Settings. For example:

        Cloud Services group: Enable clients to use a cloud management gateway
        and Allow access to cloud distribution point

<!-- p.2260 -->

        Computer Agent group: PowerShell execution policy

  If devices don't need these client settings after the task sequence completes,
  deploy new custom client settings to reverse the default settings.

  For more information, see About client settings.

RESETKEYINFORMATION

If a client has the wrong Configuration Manager trusted root key, it can't contact a
trusted management point to receive the new trusted root key. Use this property to
remove the old trusted root key. This situation may occur when you move a client from
one site hierarchy to another. This property applies to clients that use HTTP and HTTPS
client communication. For more information, see Planning for the trusted root key.

Example: CCMSetup.exe RESETKEYINFORMATION=TRUE

SITEREASSIGN

Enables automatic site reassignment for client upgrades when used with
SMSSITECODE=AUTO.

Example: CCMSetup.exe SMSSITECODE=AUTO SITEREASSIGN=TRUE

SMSCACHEDIR

Specifies the location of the client cache folder on the client computer. By default, the
cache location is %WinDir%\ccmcache .

Example: CCMSetup.exe SMSCACHEDIR="C:\Temp"

Use this property with the SMSCACHEFLAGS property to control the client cache folder
location. For example, to install the client cache folder on the largest available client disk
drive: CCMSetup.exe SMSCACHEDIR=Cache SMSCACHEFLAGS=MAXDRIVE

SMSCACHEFLAGS

Use this property to specify further installation details for the client cache folder. You
can use SMSCACHEFLAGS properties individually or in combination separated by
semicolons ( ; ).

<!-- p.2261 -->

If you don't include this property:

     The client installs the cache folder according to the SMSCACHEDIR property
     The folder isn't compressed
     The client uses the SMSCACHESIZE property as the size limit in MB of the cache

When you upgrade an existing client, the client installer ignores this property.

Values for the SMSCACHEFLAGS property
      PERCENTDISKSPACE : Set the cache size as a percentage of the total disk space. If you

     specify this property, also set SMSCACHESIZE to a percentage value.

      PERCENTFREEDISKSPACE : Set the cache size as a percentage of the free disk space. If

     you specify this property, also set SMSCACHESIZE as a percentage value. For
     example, the disk has 10 MB free, and you specify SMSCACHESIZE=50 . The client
     installer sets the cache size to 5 MB. You can't use this property with the
      PERCENTDISKSPACE property.

      MAXDRIVE : Install the cache on the largest available disk. If you specify a path with

     the SMSCACHEDIR property, the client installer ignores this value.

      MAXDRIVESPACE : Install the cache on the disk drive with the most free space. If you

     specify a path with the SMSCACHEDIR property, the client installer ignores this
     value.

      NTFSONLY : Only install the cache on an NTFS-formatted disk drive. If you specify a

     path with the SMSCACHEDIR property, the client installer ignores this value.

      COMPRESS : Store the cache in a compressed form.

      FAILIFNOSPACE : If there's insufficient space to install the cache, remove the

     Configuration Manager client.

Example: CCMSetup.exe SMSCACHEFLAGS=NTFSONLY;COMPRESS

SMSCACHESIZE

  ） Important

  Client settings are available for specifying the client cache folder size. The addition
  of those client settings effectively replaces using SMSCACHESIZE as a client.msi

<!-- p.2262 -->

  property to specify the size of the client cache. For more information, see the client
  settings for cache size.

When you upgrade an existing client, the client installer ignores this setting. The client
also ignores the cache size when it downloads software updates.

Example: CCMSetup.exe SMSCACHESIZE=100

  ７ Note

  If you reinstall a client, you can't use SMSCACHESIZE or SMSCACHEFLAGS to set the
  cache size to be smaller than it was previously. The previous size is the minimum
  value.

SMSCONFIGSOURCE

Use this property to specify the location and order that the client installer checks for
configuration settings. It's a string of one or more characters, each defining a specific
configuration source:

      R : Check for configuration settings in the registry.

      For more information, see Provision client installation properties.

      P : Check for configuration settings in the installation properties from the

      command line.

      M : Check for existing settings when you upgrade an older client.

      U : Upgrade the installed client to a newer version and use the assigned site code.

By default, the client installer uses PU . It first checks the installation properties ( P ) and
then the existing settings ( U ).

Example: CCMSetup.exe SMSCONFIGSOURCE=RP

SMSMP

Specifies an initial management point for the Configuration Manager client to use.

  ） Important

<!-- p.2263 -->

  If the management point only accepts client connections over HTTPS, prefix the
  management point name with https:// .

Examples:

     CCMSetup.exe SMSMP=smsmp01.contoso.com

     CCMSetup.exe SMSMP=https://smsmp01.contoso.com

SMSMPLIST

Specifies a list of management points for the Configuration Manager client to use. Use a
semicolon ( ; ) as the delimiter when specifying multiple management points.

  ） Important

  If the management point only accepts client connections over HTTPS, prefix the
  management point name with https:// .

Examples:

     CCMSetup.exe

     SMSMPLIST=https://smsmp01.contoso.com;https://smsmp02.contoso.com;smsmp03.cont

     oso.com

     CCMSetup.exe

     SMSMPLIST=https://smsmp01.contoso.com;smsmp02.contoso.com;smsmp03.contoso.com

SMSPUBLICROOTKEY

If the client can't get the Configuration Manager trusted root key from Active Directory
Domain Services, use this property to specify the key. This property applies to clients
that use HTTP and HTTPS communication. For more information, see Planning for the
trusted root key.

Example: CCMSetup.exe SMSPUBLICROOTKEY=<keyvalue>

   Tip

  Get the value for the site's trusted root key from the mobileclient.tcf file on the site
  server. For more information, see Pre-provision a client with the trusted root key

<!-- p.2264 -->

  by using a file.

SMSROOTKEYPATH

Use this property to reinstall the Configuration Manager trusted root key. It specifies the
full path and name of a file that contains the trusted root key. This property applies to
clients that use HTTP and HTTPS client communication. For more information, see
Planning for the trusted root key.

Example: CCMSetup.exe SMSROOTKEYPATH=C:\folder\trk

SMSSIGNCERT

Specifies the full path and name of the exported self-signed certificate on the site server.
The site server stores this certificate in the SMS certificate store. It has the Subject name
Site Server and the friendly name Site Server Signing Certificate.

Export the certificate without the private key, store the file securely, and access it only
from a secured channel.

Example: CCMSetup.exe /UsePKICert SMSSIGNCERT=C:\folder\smssign.cer

SMSSITECODE

This property specifies a Configuration Manager site to which you assign the client. This
value can either be a three-character site code or the word AUTO . If you specify AUTO , or
don't specify this property, the client attempts to determine its site assignment from
Active Directory Domain Services or from a specified management point. To enable
AUTO for client upgrades, also set SITEREASSIGN=TRUE.

  ７ Note

  If you also specify an internet-based management point with the CCMHOSTNAME
  property, don't use AUTO with SMSSITECODE . Directly assign the client to its site by
  specifying the site code.

Example: CCMSetup.exe SMSSITECODE=XZY

UPGRADETOLATEST

<!-- p.2265 -->

This property forces CCMSetup to send a location request to the management point to
get the latest version of the Configuration Manager client installation source. There are
several scenarios where this property is especially useful:

      Pre-production clients. A newly installed client uses the production baseline
      because it can't evaluate the pre-production collection until the client is installed.
      In that scenario, after the client is installed and it evaluates policy, it will later
      upgrade to the pre-production client version. Use this property so that the device
      immediately installs the latest version of the client.

      This scenario also includes when using Autopilot into co-management. Use this
      property to make sure the newly provisioned Autopilot device uses the pre-
      production client version right away.

      Pull distribution points. Allow pull distribution points to install the latest client
      version even if it's not in the pre-production collection. This action makes sure that
      the client version on the pull distribution point is the same as the distribution point
      binaries. If these versions aren't the same, it may cause issues.

Attribute values for certificate selection criteria
Configuration Manager supports the following attribute values for the PKI certificate
selection criteria:

                                                                                 ﾉ     Expand table

 OID attribute                   Distinguished Name attribute         Attribute definition

 0.9.2342.19200300.100.1.25      DC                                   Domain component

 1.2.840.113549.1.9.1            E or E-mail                          Email address

 2.5.4.3                         CN                                   Common name

 2.5.4.4                         SN                                   Subject name

 2.5.4.5                         SERIALNUMBER                         Serial number

 2.5.4.6                         C                                    Country code

 2.5.4.7                         L                                    Locality

 2.5.4.8                         S or ST                              State or province name

 2.5.4.9                         STREET                               Street address

<!-- p.2266 -->

 OID attribute                   Distinguished Name attribute   Attribute definition

 2.5.4.10                        O                              Organization name

 2.5.4.11                        OU                             Organizational unit

 2.5.4.12                        T or Title                     Title

 2.5.4.42                        G or GN or GivenName           Given name

 2.5.4.43                        I or Initials                  Initials

 2.5.29.17                       (no value)                     Subject Alternative Name

Client push installation
If you use the client push installation method, use the following options on the Client
tab of the Client Push Installation Properties in the Configuration Manager console:

     Any of the Client.msi properties

     The following subset of CCMSetup.exe command-line parameters are allowed for
     client push:

            /AllowMetered (starting in version 2103)

            /AlwaysExcludeUpgrade

            /BITSPriority

            /downloadtimeout

            /ExcludeFeatures

            /forcereboot

            /logon

            /skipprereq

            /UsePKICert

Feedback

<!-- p.2267 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2268 -->

About client installation properties
published to Active Directory Domain
Services
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you extend the Active Directory schema for Configuration Manager, and the site
is published to Active Directory Domain Services, many client installation properties are
published to Active Directory Domain Services. If a computer can locate these client
installation properties, it can use them during Configuration Manager client deployment.

The advantages of using Active Directory Domain Services to publish client installation
properties include the following:

      Software update point-based client installations and Group Policy client
      installations do not require setup parameters to be set up on each computer.

      Because this information is automatically generated, the risk of human error
      associated with manually entering installation properties is eliminated.

  ７ Note

  For more information about how to extend the Active Directory schema for
  Configuration Manager, and how to publish a site, see Schema extensions for
  Configuration Manager.

Client installation properties published to
Active Directory Domain Services
The following is a list of client installation properties. For more information about each
item listed below, see About client installation properties.

      The Configuration Manager site code.

      The site server signing certificate.

      The trusted root key.

      The client communication ports for HTTP and HTTPS.

<!-- p.2269 -->

     The fallback status point. If the site has multiple fallback status points, only the first
     one that was installed is published to Active Directory Domain Services.

     A setting to indicate that the client must communicate by using HTTPS only.

     Settings related to PKI certificates:

        Whether to use a client PKI certificate.

        The selection criteria for certificate selection. This may be required because the
        client has more than one valid PKI certificate that can be used for Configuration
        Manager.

        A setting to determine which certificate to use if the client has multiple valid
        certificates after the certificate selection process.

        The certificate issuers list that contains a list of trusted root CA certificates.

     Client.msi installation properties that are specified in the Client tab of the Client
     Push Installation Properties dialog box.

Client installation (CCMSetup) uses the properties that are published to Active Directory
Domain Services only if no other properties are specified by using either of the
following:

     The manual installation method (described later in this article)

     The Group Policy installation method (described later in this article)

  ７ Note

  The client installation properties are used to install the client. These properties
  might be overwritten with new settings from its assigned site after the client is
  installed and has successfully been assigned to a Configuration Manager site.

Use the details in the following sections to determine which Configuration Manager
client installation methods use Active Directory Domain Services to obtain client
installation properties.

Client push installation
Client push installation does not use Active Directory Domain Services to obtain
installation properties.

<!-- p.2270 -->

Instead, you can specify client installation properties in the Installation Properties tab of
the Client Push Installation Properties dialog box. These options and client-related site
settings are stored in a file that the client reads during client installation.

  ７ Note

  You do not have to specify any CCMSetup properties for client push installation, or
  the fallback status point, or the trusted root key in the Installation Properties tab.
  These settings are automatically supplied to clients when they are installed by using
  client push installation. In addition to Client.msi properties, CCMSetup supports the
  following parameters: /forcereboot, /skipprereq, /logon, /BITSPriority,
  /downloadtimeout, /forceinstall

Any properties that you specify in the Installation Properties tab are published to Active
Directory Domain Services if the site is published to Active Directory Domain Services.
These settings are read by client installations where CCMSetup is run with no installation
properties.

Software update point-based installation
The software update point-based installation method does not support the addition of
installation properties to the CCMSetup command line.

If no command line properties have been provisioned on the client computer by using
Group Policy, CCMSetup searches Active Directory Domain Services for installation
properties.

Group Policy installation
The Group Policy installation method does not support the addition of installation
properties to the CCMSetup command line.

If no command line properties have been provisioned on the client computer,
CCMSetup searches Active Directory Domain Services for installation properties.

Manual installation
CCMSetup searches Active Directory Domain Services for installation properties under
the following circumstances:

<!-- p.2271 -->

     No command line properties are specified after the CCMSetup.exe command.

     The computer has not been provisioned with installation properties by using
     Group Policy.

Logon script installation
CCMSetup searches Active Directory Domain Services for installation properties under
the following circumstances:

     No command line properties are specified after the CCMSetup.exe command.

     The computer has not been provisioned with installation properties by using
     Group Policy.

Software distribution installation
CCMSetup searches Active Directory Domain Services for installation properties under
the following circumstances:

     No command line properties are specified after the CCMSetup.exe command.

     The computer has not been provisioned with installation properties by using
     Group Policy.

Installations for clients that cannot access
Active Directory Domain Services
These client computers cannot read or access the published installation properties from
Active Directory Domain Services.

These clients include:

     Workgroup computers.

     Clients that are assigned to a Configuration Manager site that is not published to
     Active Directory Domain Services.

     Clients that are installed when they are on the Internet.

Feedback

<!-- p.2272 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2273 -->

Prepare to deploy client software to
Macs
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

Follow these steps to make sure that you're ready to deploy the Configuration Manager
client to Mac computers.

For the list of supported versions, see Supported operating systems for clients and
devices.

Certificate requirements
Client installation and management for Mac computers requires public key
infrastructure (PKI) certificates. PKI certificates secure the communication between the
Mac computers and the Configuration Manager site by using mutual authentication and
encrypted data transfers. Configuration Manager can request and install a user client
certificate. It uses Certificate Services with an enterprise certification authority, and the
Configuration Manager enrollment point and enrollment proxy point. You can also
request and install a computer certificate independently from Configuration Manager.
This certificate must meet the Configuration Manager certificate requirements.

Configuration Manager Mac clients always check for certificate revocation. You can't
disable this function.

If Mac clients can't locate the certificate revocation list (CRL), they can't connect to
Configuration Manager site systems. Especially for Mac clients in a different forest to the
issuing certification authority, check your CRL design. Make sure that Mac clients can
locate and download a CRL.

Before you install the Configuration Manager client on a Mac computer, decide how to
install the client certificate:

<!-- p.2274 -->

     Use Configuration Manager enrollment by using the CMEnroll tool. The enrollment
     process doesn't support automatic certificate renewal. Re-enroll Mac computers
     before the certificate expires.

     Use a certificate request and installation method that's independent from
     Configuration Manager.

For more information about Mac client certificate requirements, see PKI certificate
requirements for Configuration Manager.

Mac clients are automatically assigned to the Configuration Manager site that manages
them. Mac clients install as internet-only clients, even if communication is restricted to
the intranet. This configuration means that they communicate with internet-enabled
management points and distribution points in their assigned site. Mac computers don't
communicate with site systems outside their assigned site.

  ） Important

  The Configuration Manager client for macOS can't be used to connect to a
  management point that's configured to use a database replica.

Deploy a web server certificate to site system
servers
If these site systems don't have it, deploy a web server certificate to the computers that
have these site system roles:

     Management point

     Distribution point

     Enrollment point

     Enrollment proxy point

The web server certificate must include the internet FQDN that's specified in the site
system properties. The server doesn't have to be accessible from the internet to support
Mac computers. If you don't require internet-based client management, you can specify
the intranet FQDN value for the internet FQDN.

Specify the site system's internet FQDN value in the web server certificate for the
management point, the distribution point, and the enrollment proxy point.

<!-- p.2275 -->

For more information of an example deployment, see Deploying the web server
certificate for site systems that run IIS.

Deploy a client authentication certificate to site
system servers
If these site systems don't have it, deploy a client authentication certificate to the
computers that host these site system roles:

     Management point

     Distribution point

For an example deployment that creates and installs the client certificate for
management points, see the Deploying the client certificate for Windows computers.

For an example deployment that creates and installs the client certificate for distribution
points, see the Deploying the client certificate for distribution points.

  ） Important

  To deploy the client to devices running macOS Sierra, the subject name of the
  management point certificate must be configured correctly. For example, use the
  FQDN of the management point server.

Prepare the client certificate template for Macs
The certificate template must have Read and Enroll permissions for the user account
that enrolls the certificate on the Mac computer.

For more information, see Deploying the client certificate for Mac computers.

Configure the management point and
distribution point
Configure management points for the following options:

     HTTPS

     Allow client connections from the internet. This configuration value is required to
     manage Mac computers. However, it doesn't mean that site system servers must

<!-- p.2276 -->

     be accessible from the internet.

     Allow mobile devices and Mac computers to use this management point

Distribution points aren't required to install the client for Mac. If you want to deploy
software to these computers after you install the client, configure distribution points to
allow client connections from the internet.

To configure management points and distribution points
to support Macs
Before you start this procedure, make sure to configure the management point and
distribution point with an internet FQDN. If these servers don't support internet-based
client management, specify the intranet FQDN as the internet FQDN value.

The site system roles must be in a primary site.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Servers and Site System Roles node.
     Then select the server that has the right site system roles.

   2. In the details pane, select the Management point role, and select Properties in the
     ribbon. In the Management point Properties window, configure these options:

      a. Choose HTTPS.

      b. Choose Allow internet-only client connections or Allow intranet and internet
        client connections. These options require an internet or intranet FQDN.

      c. Choose Allow mobile devices and Mac computers to use this management
        point.

      d. Select OK to save this configuration.

   3. In the details pane of the Server and Site System Roles node, select the
     Distribution point role, and select Properties in the ribbon. In the Distribution
     point Properties window, configure these options:

           Choose HTTPS.

           Choose Allow internet-only client connections or Allow intranet and
           internet client connections. These options require an internet or intranet
           FQDN.

<!-- p.2277 -->

           Choose Import certificate, browse to the exported client distribution point
           certificate file, and then specify the password.

   4. Repeat this procedure for all management points and distribution points in
     primary sites that manage Mac computers.

Configure the enrollment proxy point and the
enrollment point
Install both roles in the same site. You don't have to install them on the same site
system server, or in the same Active Directory forest.

For more information about site system role placement and considerations, see Site
system roles.

To add the site system roles to support Mac computers, see Install site system roles.

On the System Role Selection page, select Enrollment proxy point and Enrollment
point from the list of available roles.

Install the reporting services point
For more information, see Install the reporting services point.

Next steps
Deploy the Configuration Manager client to Mac computers

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2278 -->

How to deploy clients to Macs
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. For
  more information, see Mac computers.

This article describes how to deploy and maintain the Configuration Manager client on
Mac computers. To learn about what you have to configure before deploying clients to
Mac computers, see Prepare to deploy client software to Macs.

When you install a new client for Mac computers, you might have to also install
Configuration Manager updates to reflect the new client information in the
Configuration Manager console.

In these procedures, you have two options for installing client certificates. Read more
about client certificates for Macs in Prepare to deploy client software to Macs.

      Use Configuration Manager enrollment by using the CMEnroll tool. The enrollment
      process doesn't support automatic certificate renewal. Re-enroll the Mac computer
      before the installed certificate expires.

      Use a certificate request and installation method that is independent from
      Configuration Manager.

  ） Important

  To deploy the client to devices running macOS Sierra, correctly configure the
  Subject name of the management point certificate. For example, use the FQDN of
  the management point server.

Configure client settings
Use the default client settings to configure enrollment for Mac computers. You can't use
custom client settings. To request and install the certificate, the Configuration Manager
client for Mac requires the default client settings.

<!-- p.2279 -->

   1. In the Configuration Manager console, go to the Administration workspace. Select
      the Client Settings node, and then select Default Client Settings.

   2. On the Home tab of the ribbon, in the Properties group, choose Properties.

   3. Select the Enrollment section, and then configure the following settings:

      a. Allow users to enroll mobile devices and Mac computers: Yes

      b. Enrollment profile: Choose Set Profile.

   4. In the Mobile Device Enrollment Profile dialog box, choose Create.

   5. In the Create Enrollment Profile dialog box, enter a name for this enrollment
      profile. Then configure the Management site code. Select the Configuration
      Manager primary site that contains the management points for these Mac
      computers.

        ７ Note

        If you can't select the site, make sure that you configure at least one
        management point in the site to support mobile devices.

   6. Choose Add.

   7. In the Add Certification Authority for Mobile Devices window, select the
      certification authority server that issues certificates to Mac computers.

   8. In the Create Enrollment Profile dialog box, select the Mac computer certificate
      template that you previously created.

   9. Select OK to close the Enrollment Profile dialog box, and then the Default Client
      Settings dialog box.

         Tip

        If you want to change the client policy interval, use Client policy polling
        interval in the Client Policy client setting group.

The next time the devices download client policy, Configuration Manager applies these
settings for all users. To initiate policy retrieval for a single client, see Initiate policy
retrieval for a Configuration Manager client.

<!-- p.2280 -->

In addition to the enrollment client settings, make sure that you have configured the
following client device settings:

     Hardware inventory: Enable and configure this feature if you want to collect
     hardware inventory from Mac and Windows client computers. For more
     information, see How to extend hardware inventory.

     Compliance settings: Enable and configure this feature if you want to evaluate and
     remediate settings on Mac and Windows client computers. For more information,
     see Plan for and configure compliance settings.

For more information, see How to configure client settings.

Download the client for macOS

  ７ Note

  The macOS client installation package isn't available for new deployments, but
  existing deployments are supported until December 31, 2022.

   1. Save ConfigmgrMacClient.msi to a computer that runs Windows. This file isn't on
     the Configuration Manager installation media.

   2. Run the installer on the Windows computer. Extract the Mac client package,
     Macclient.dmg, to a folder on the local disk. The default path is C:\Program
     Files\Microsoft\System Center Configuration Manager for Mac client .

   3. Copy the Macclient.dmg file to a folder on the Mac computer.

   4. On the Mac computer, run Macclient.dmg to extract the files to a folder on the
     local disk.

   5. In the folder, make sure that it contains the following files:

           Ccmsetup: Installs the Configuration Manager client on your Mac computers
           using CMClient.pkg

           CMDiagnostics: Collects diagnostic information related to the Configuration
           Manager client on your Mac computers

           CMUninstall: Uninstalls the client from your Mac computers

           CMAppUtil: Converts Apple application packages into a format that you can
           deploy as a Configuration Manager application
