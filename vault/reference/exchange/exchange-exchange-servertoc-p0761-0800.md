---
title: "Exchange Server — pages 761-800"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p0761-0800
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p0761-0800
family: exchange
documentKind: "doc"
abstract: "There might be a delay between the release of an Exchange Server Security Update (SU) or Cumulative Update (CU) and an update to the Mitigation XML file, excluding the security fixed build numbers from the Mitigations being applied. This is expected and shouldn't cause any probl"
---

# Exchange Server — pages 761-800

<!-- p.761 -->

There might be a delay between the release of an Exchange Server Security Update (SU) or
Cumulative Update (CU) and an update to the Mitigation XML file, excluding the security fixed
build numbers from the Mitigations being applied. This is expected and shouldn't cause any
problems. If you want to remove and block a Mitigation being applied in the meantime, you can
follow the steps outlined in the Block or remove mitigations section.

We update the table under List of mitigations released section, along with the corresponding
steps in the Rollback procedures for released mitigations section, for the specific Mitigation as
soon as it's no longer applied to security fixed Exchange builds.

Rollback procedures for released mitigations
This section provides the detailed steps to manually remove specific released mitigations. Only
run these steps after you confirm that the mitigation is no longer needed (for example, after you
install the SU or CU that fixes the underlying vulnerability) and that the EM service won't reapply
it. To prevent the EM service from reapplying a mitigation, block it first as described in the Block
or remove mitigations section.

M1
Remove the rule EEMS M1.1 PowerShell - inbound manually from the IIS URL Rewrite module
inside the Default Web Site.

M2
Run the following commands to back up the affected web.config file and remove the M2 URL
Rewrite outbound rule and its precondition:

 PowerShell

 Copy-Item -Path "$env:ExchangeInstallPath\FrontEnd\HttpProxy\owa\web.config" -
 Destination "$env:ExchangeInstallPath\FrontEnd\HttpProxy\owa\web.config.$((Get-
 Date).ToString('yyyyMMdd-HHmmss')).bak"

 Remove-WebConfigurationProperty -PSPath "IIS:\Sites\Default Web Site\owa" -Filter
 "system.webServer/rewrite/outboundRules" -Name "." -AtElement @{name="EEMS M2.1 OWA
 CSP - outbound"}

 Remove-WebConfigurationProperty -PSPath "IIS:\Sites\Default Web Site\owa" -Filter
 "system.webServer/rewrite/outboundRules/preConditions" -Name "." -AtElement
 @{name="EEMS M2.1 OWA SPA HTML shell - precondition"}

<!-- p.762 -->

Audit and logging
Any mitigations blocked by an admin are logged in the Windows Application Event Log. In
addition to logging blocked mitigations, the EM service also logs details about service startup,
shutdown, and termination (like all services running on Windows) and details of its actions and
any errors encountered by the EM service. For example, Events 1005 and 1006 with a source of
"MSExchange Mitigation Service" are logged for successful actions such as when a mitigation is
applied. Event 1008 with the same source is logged for any encountered errors, such as when the
EM service can't reach the OCS.

You can use Search-AdminAuditLog to review actions taken by yourself or other admins,
including enabling and disabling automatic mitigations.

The EM service maintains a separate log file in the \V15\Logging\MitigationService folder in the
Exchange Server installation directory. This log details the tasks performed by the EM service,
including fetched, parsed, and applied mitigations and details about the information sent to the
OCS (if sending diagnostic data is enabled).

Diagnostic data
When data sharing is enabled, the EM service sends diagnostic data to the OCS. This data is used
to identify and mitigate threats. To learn more about what is collected and how to disable data
sharing, see Diagnostic Data collected for Exchange Server.

）Note: The author created this article with assistance from AI. Learn more

 Last updated on 07/14/2026

<!-- p.763 -->

Exchange Server update FAQ
Article • 05/09/2025

APPLIES TO:        2016      2019           Subscription Edition

Overview
It's very important to keep updating your on-premises Exchange Servers to a supported
state. Your on-premises environments should always be ready to take an emergency security
update (this applies to Exchange, Windows, and any other products you use on-premises). With
the threat landscape rapidly evolving, the importance of keeping your environment current
shouldn't be underestimated.

Keep your Exchange Servers up to date. We want to continue helping you keep your
environment secure, and this means your Exchange servers need to be up to date. This is a
continuous process.

Exchange Server update types and release
schedule
There are three types of updates that Microsoft might release for Exchange Server:

                                                                                           ﾉ   Expand table

 Update         Frequency of release             Exchange requirement                  Contains
 type

 Cumulative     Twice a year (no specific        Exchange must be in Mainstream        Cumulative. Contains
 Update (CU)    dates).                          support.                              fixes from all
                                                                                       previously released
                                                                                       updates.

 Security       When needed. Released            Exchange must be in at least          Cumulative. Contains
 Update (SU)    typically on Microsoft           Extended support. Released for last   all security updates
                'Patch Tuesday' - second         CU only (if Exchange is in Extended   since the CU it
                Tuesday of every month           support) or for last two CUs (if      applies to was
                (unless emergency release).      Exchange is in Mainstream             released.
                                                 support).

 Hotfix         Released only if feature         Exchange must be in Mainstream        The feature update
 Update (HU)    updates are needed faster        support.                              applies only to the
                than CU releases.                                                      CU it's released for.

<!-- p.764 -->

Update best practices
This process assumes that your Exchange Server is still supported:

     Install the latest CU. Use the Exchange Update Assistant     to choose your current CU and
     your target CU to get specific directions. Additional information can be found in Upgrade
     Exchange to the latest Cumulative Update.
     Inventory your Exchange Servers to determine which updates are needed using the
     Exchange Server Health Checker script . Running this script will tell you if any of your
     Exchange Servers are behind on updates (CUs, SUs, or manual actions).
     Install the Security Update (SU) as they're released.
     Re-run the Health Checker after you install an SU to see if any further actions are needed.
     At times, extra actions are required.
     If you encounter errors during or after installation of Exchange Server, run the SetupAssist
     script   . If something doesn't work properly after updates, see Repair failed installations
     of Exchange Cumulative and Security updates .

Q&A
We have prepared a set of questions and answers that cover what we hear most often about
Exchange updates.

We updated my Exchange Servers a few months ago! How
come they're 'not supported' today?
For versions of Exchange that are within mainstream support (see product lifecycle), Microsoft
supports (releases relevant security fixes for) the two latest CUs. Sometimes the latest two CUs
are referred to as "N and N-1". As a current example, if the latest released CU is CU12 ('N'), and
the server version is Exchange Server 2019, then Microsoft at this time supports two Exchange
Server 2019 CUs, N and N-1 (CU12 and CU11). When CU13 is released, the "supported CU
window" will slide toward the newly released CU13 (and what used to be the N-1 supported
CU, CU11, will become unsupported).

Why does Microsoft release updates so often?
It's good that updates are released when issues are found. Microsoft (and other software
publishers) release updates only when they're needed. CUs typically contain resolutions to
feature problems that were reported to us by our customers (and can contain security updates
from previous SUs) and are released twice a year (in H1 and H2). SUs are released only when
actual security issues are found and fixed, and are typically released on a 'patch Tuesday'. Let's

<!-- p.765 -->

take an example of how a typical release flow for two CUs and two SUs we might release would
look like:

      On a particular month (let's say March), we might release CU4; CU4 is cumulative and will
      include fixes and updates from before.
      A month later we release CU4 SU1, a security update for CU4.
      In July we then release CU4 SU2, an additional security update for CU4. CU4 SU2 includes
      updates released in CU4 SU1 also.
      In September we release CU5, which will contain all updates released up to that point.

                                                                                           

Our Exchange Servers are working as expected, why update
them?
Keeping Exchange Server current allows you to ensure that it keeps working without major
interruptions to functionality and will help ensure your company data is safer. Investing time
into Exchange Server maintenance (on your planned schedule) gives you a long-term benefit of
well running system, with code as protected from vulnerabilities as possible.

How can we update Exchange Server when (insert 3rd party
application name here) doesn't support the latest supported
Exchange Server CUs?
Work with your 3rd party vendor to bring their software current in a timely manner. Consider
that your Exchange environment contains many valuable company directory and messaging
information. Your priority should be to keep your environment as secure as possible.

How can we stay current when we're a 24x7 business and have
no time to take down our servers for maintenance?
Many customers require Exchange Server to work 24x7. In fact, our update process is designed
for these high-demand businesses. You should use Database Availability Groups (DAGs) and
put servers that you're updating in Maintenance mode to enable a graceful and non-disruptive
update process for your users. See Performing maintenance on DAG members for more
information.

<!-- p.766 -->

If we're in Hybrid mode and don't actively use our on-
premises Exchange Server, do we still need to stay current?
Even if you're only using Exchange Server on-premises to manage Exchange-related objects,
you need to keep the server current. The Hybrid Configuration Wizard (HCW) doesn't need to
be re-run after updates are installed.

We looked at recent security update releases and the
Common Vulnerabilities and Exposures (CVE) severity wasn't
high; why update?
Microsoft recommends that you apply all available security updates because it can be difficult
to understand how even lower severity vulnerabilities disclosed in one month might interact
with vulnerabilities disclosed and fixed a month later. An attack can trigger only specific low-
impact functionality on a remote target machine and nothing else, causing the scoring for the
CVE to be low one month. For example, in the following month an important issue with that
functionality could be discovered, but it might be only triggered locally and require significant
user interaction. That on its own might also not be scored highly. But if your software is behind
in updates, these two issues could combine into an attack chain, thereby scoring at critical
levels.

We applied mitigations for a recent security vulnerability. Why
should we install (later released) updates for those same
vulnerabilities?
Mitigations are a temporary form of protection that should be used until the actual code fix is
released. Because mitigations don't address the actual vulnerability that is present in the code,
they can (and sometimes do) get bypassed by threat actors attacking systems that are still
vulnerable. Microsoft recommends installing the code fix for any vulnerability as soon as it's
available. Mitigations shouldn't be considered a long-term solution to vulnerable code.

We find it difficult to update because Active Directory (AD)
schema extensions and Exchange installations require
different teams to take action.
In cases where different teams need to perform separate actions to prepare for installation of
Exchange Cumulative Updates (as those might require AD schema extension) - we recommend
you request schema changes when we release new CUs that require them. Even if you don't
need to update to the latest CU (because last two CUs are supported for Exchange versions

<!-- p.767 -->

that are still within support lifetime) - the fact that Active Directory schema will be up to date
means that if you do find that you need to install the latest CU, AD schema will already be
updated. We release CUs twice a year and not all of them require AD schema updates. You can
track this here for Exchange Server 2016 and here for Exchange Server 2019.

We installed a previous CU on our server and then applied
available SUs. We updated our server to the latest CU
available. Do we need to apply the already released SU for the
latest CU too?
After a new CU is installed on the server, you always need to install the latest SUs available for
that CU. Let us walk through a hypothetical Exchange Server 2019 scenario of this:

     In May, you installed CU9 (the latest available CU at the time) and all available SUs for
     CU9
     In June, we released CU10 for Exchange Server 2019
     In July, we released SUs that apply to both CU9 and CU10
     In July, you installed July SU to your Exchange 2019 CU9 server
     In August, you installed CU10 (the latest available CU in July)
     You now need to apply the latest SU that is available for Exchange Server 2019 CU10

We installed an SU for current CU last month. This month, a
new SU is available for the same CU. Do we need to uninstall
last month's SU before installing a newer one for the same
CU?
No, uninstallation of last month's SU isn't necessary. Install this month's SU as it becomes
available. Newer SU contains last month's SUs security fixes too.

SUs are always CU specific. In other words - installing a later CU requires that any SU available
for that CU be installed also, no matter if the SU for the latest and previous CU were released
on the same day. If there are SUs for the CU your server is running, then you should install it.
SUs will typically be 'rolled into the CU' at the next subsequent CU release.

We skipped a few SUs and want to bring Exchange fully up to
date to the latest SU. Do we need to install all the SUs in order
to get to the latest?

<!-- p.768 -->

Because SUs are cumulative "since the CU they're applicable to", you only need to install the
latest SU. This gives you all of the security fixes released since the CU was released.

Did Microsoft change how often Exchange CUs are released?
Yes, starting with 2022 H1 Cumulative Updates , we have moved to a release cadence of two
CUs per year - releasing in H1 and H2 of each calendar year, with general target release dates
of March and September. But our release dates are driven by quality, so we might release
updates in April or October, or some other month, depending on what we're delivering. With
these service model changes, being current still means to run the latest CU or the one
immediately preceding it (N or N-1), but the 'currency window' is now extended from 6 months
to 1 year.

Do we need to install SUs on all Exchange Servers within our
organization? What about 'Management Tools only'
machines?
Our recommendation is to install Security Updates on all Exchange Servers and servers or
workstations running Exchange Management Tools only, which will ensure that there's no
incompatibility between management tools clients and servers. If you're trying to update the
Exchange Management Tools in the environment with no running Exchange servers, see this.

We installed current CU and SU releases and are fully up to
date. Is there anything else that we should do?
Depending on the particular environment, addressing certain vulnerabilities might require extra
actions to be performed by the Exchange administrator. To make sure, that you have
performed all of the actions necessary after relevant Security Updates were installed, run the
Exchange Server Health Checker script . Ensure that you update the Windows operating
system that Exchange Server is running on, as vulnerabilities in the OS can be used as a part of
attack chain too.

<!-- p.769 -->

Exchange Server TLS configuration best
practices
Article • 04/25/2025

APPLIES TO:        2016    2019      Subscription Edition

This documentation outlines the necessary steps to correctly configure specific TLS versions on
Microsoft Exchange Server. It also details how to optimize the cipher suites and hashing
algorithms used by TLS. Incorrect TLS configuration can lead to various issues when interacting
with Microsoft 365 or other systems that require a certain minimum TLS standard.

You can find more information about the TLS protocols in the Transport Layer Security protocol
documentation.

   Tip

  You can use the Exchange HealthChecker script        to check the current TLS configuration
  of your Exchange server.

Read carefully, as some steps can only be performed on specific operating systems or
Exchange Server versions. Each section starts with a matrix showing whether a setting is
supported and if it has been pre-configured from a certain Exchange Server version, followed
by steps to enable or disable the specific TLS protocol or feature.

Things to consider before disabling a TLS version
Please make sure that every application supports the TLS versions, which remain enabled.
Considerations such as (but not limited to):

      Do your Domain Controllers and Global Catalog servers support, for example, a TLS 1.2 or
      TLS 1.3 only configuration?
      Do partner applications support, for example, a TLS 1.2 or TLS 1.3 only configuration?
      Do the Operating System (OS) support the latest TLS protocol version TLS 1.2 over
      WinHTTP     ?
      Do your load balancers support TLS 1.2 or TLS 1.3 being used?
      Do your desktop, mobile, and browser applications support TLS 1.2 or TLS 1.3?
      Do devices such as multi-function printers support TLS 1.2 or TLS 1.3?
      Do your third-party or custom in-house applications that integrate with Exchange Server
      or Microsoft 356 support a strong TLS implementation?

<!-- p.770 -->

As such we strongly recommend any steps you take to transition to TLS 1.2 or TLS 1.3 and away
from older security protocols are first performed in labs which simulate your production
environments before you slowly start rolling them out in production.

The steps used to disable a specific TLS version as outlined below apply to the following
Exchange Server functionalities:

     Simple Mail Transport Protocol (SMTP)
     Outlook Client Connectivity (Outlook Anywhere / MAPI/HTTP)
     Exchange Active Sync (EAS)
     Outlook on the Web (OWA)
     Exchange Admin Center (EAC) and Exchange Control Panel (ECP)
     AutoDiscover
     Exchange Web Services (EWS)
     REST (Exchange Server 2016/2019)
     Use of PowerShell by Exchange over HTTPS
     POP and IMAP

Prerequisites
TLS 1.3 support was introduced with Exchange Server 2019 Cumulative Update (CU) 15 on
Windows Server 2022 and Windows Server 2025, except for the SMTP protocol. Therefore,
disabling any TLS protocol except TLS 1.3 is not supported yet. Support for this protocol will be
added with a future update. TLS 1.2 support was introduced with Exchange Server 2013 CU19
and Exchange Server 2016 CU8. Exchange Server 2019 supports TLS 1.2 by default.

Exchange Server cannot run without Windows Server and therefore it is important to have the
latest operating system updates installed to run a stable and secure TLS implementation.

It's also required to have the latest version of .NET Framework and associated patches
supported by your CU in place.

Based on your operating system, make sure that the following updates are also in place (they
should be installed if your server is current on Windows Updates):

If your operating system is Windows Server 2012 or Windows Server 2012 R2, KB3161949
and KB2973337     must be installed before TLS 1.2 can be enabled.

  ２ Warning

<!-- p.771 -->

  Windows Server 2012 and Windows Server 2012 R2 extended support has ended on
  October 10, 2023. These servers no longer receive Windows Security Updates without an
  ESU. We strongly recommend migrating to a supported version as soon as possible!

Make sure to reboot the Exchange Server after the TLS configuration has been applied. It
becomes active after the server was restarted.

Preparing .NET Framework to inherit defaults from Schannel
The following table shows the Exchange Server/Windows Server combinations with the default
.NET Framework Schannel inheritance configuration:

                                                                                          ﾉ   Expand table

 Exchange Server             Windows         Supported     Configured by default
                             Server

 Exchange Server 2019        Any             Yes           Yes (new installations only)
 CU14 or later

 Exchange Server 2019        Any             Yes           Partially ( SchUseStrongCrypto must be
 CU13 or older                                             configured manually)

 Exchange Server 2016        Any             Yes           No (OS defaults are used)

 Exchange Server 2013        Any             Yes           No (OS defaults are used)

The SystemDefaultTlsVersions registry value defines which security protocol version defaults
are used by .NET Framework 4.x. If the value is set to 1 , then .NET Framework 4.x inherits its
defaults from the Windows Secure Channel (Schannel) DisabledByDefault registry values. If the
value is undefined, it behaves as if the value is set to 0 .

The strong cryptography (configured by the SchUseStrongCrypto registry value) uses more
secure network protocols (TLS 1.3, TLS 1.2 and TLS 1.1) and blocks protocols that are not
secure. SchUseStrongCrypto affects only client (outgoing) connections in your application. By
configuring .NET Framework 4.x to inherit its values from Schannel we gain the ability to use
the latest versions of TLS supported by the OS, including TLS 1.2 and TLS 1.3.

Enable .NET Framework 4.x Schannel inheritance
Run the following commands from an elevated PowerShell window to configure the .NET
Framework 4.x Schannel inheritance:

<!-- p.772 -->

  PowerShell

  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\.NETFramework\v4.0.30319" -Name
  "SystemDefaultTlsVersions" -Value 1 -Type DWord
  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\.NETFramework\v4.0.30319" -Name
  "SchUseStrongCrypto" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319" -Name
  "SystemDefaultTlsVersions" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319" -Name
  "SchUseStrongCrypto" -Value 1 -Type DWord

Enable .NET Framework 3.5 Schannel inheritance

Exchange Server 2013 and later do not need this setting. However, we recommend configuring
it identically to the .NET 4.x settings to ensure a consistent configuration.

Run the following commands from an elevated PowerShell window to configure the .NET
Framework 3.5 Schannel inheritance:

  PowerShell

  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\.NETFramework\v2.0.50727" -Name
  "SystemDefaultTlsVersions" -Value 1 -Type DWord
  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\.NETFramework\v2.0.50727" -Name
  "SchUseStrongCrypto" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727" -Name
  "SystemDefaultTlsVersions" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727" -Name
  "SchUseStrongCrypto" -Value 1 -Type DWord

Steps to configure TLS 1.3
The following table shows the Exchange Server/Windows Server combinations on which TLS 1.3
is supported. The table also shows the default configuration:

                                                                                      ﾉ   Expand table

 Exchange Server                     Windows Server              Supported      Configured by
                                                                                default

 Exchange Server 2019 CU15           Windows Server              Yes            Yes ( enabled )
                                     2022/2025

<!-- p.773 -->

 Exchange Server                    Windows Server            Supported    Configured by
                                                                           default

 Exchange Server 2019 CU15          Windows Server 2019       No           N/A

 Exchange Server 2019 CU14 or       Any                       No           N/A
 older

 Exchange Server 2016               Any                       No           N/A

 Exchange Server 2013               Any                       No           N/A

Enable TLS 1.3
Run the following command from an elevated PowerShell window to enable TLS 1.3 for client
and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.3" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Client" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Client" -Name "Enabled" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Server" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Server" -Name "Enabled" -Value 1 -Type DWord

As per RFC 8446    TLS 1.3 uses the same cipher suite space as previous versions of TLS.
However, TLS 1.3 cipher suites are defined differently, only specifying the symmetric ciphers,
and cannot be used for TLS 1.2. Similarly, cipher suites for TLS 1.2 and lower cannot be used
with TLS 1.3.

Run the following command from an elevated PowerShell window to configure the TLS 1.3
cipher suites:

<!-- p.774 -->

  PowerShell

  Enable-TlsCipherSuite -Name TLS_AES_256_GCM_SHA384 -Position 0
  Enable-TlsCipherSuite -Name TLS_AES_128_GCM_SHA256 -Position 1

Disable TLS 1.3
Run the following command from an elevated PowerShell window to explicitly disable TLS 1.3
for client and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.3" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Client" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Client" -Name "Enabled" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Server" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.3\Server" -Name "Enabled" -Value 0 -Type DWord

Run the following command from an elevated PowerShell window to remove the TLS 1.3 cipher
suites:

  PowerShell

  Disable-TlsCipherSuite -Name TLS_AES_256_GCM_SHA384
  Disable-TlsCipherSuite -Name TLS_AES_128_GCM_SHA256

Steps to configure TLS 1.2
The following table shows the Exchange Server/Windows Server combinations on which TLS 1.2
is supported. The table also shows the default configuration:

<!-- p.775 -->

                                                                              ﾉ   Expand table

 Exchange Server             Windows Server      Supported      Configured by default

 Exchange Server 2019        Any                 Yes            Yes ( enabled )

 Exchange Server 2016        Any                 Yes            No

 Exchange Server 2013        Any                 Yes            No

Enable TLS 1.2
Run the following command from an elevated PowerShell window to enable TLS 1.2 for client
and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.2" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Client" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Client" -Name "Enabled" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Server" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Server" -Name "Enabled" -Value 1 -Type DWord

Disable TLS 1.2
Run the following command from an elevated PowerShell window to explicitly disable TLS 1.2
for client and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -

<!-- p.776 -->

  Name "TLS 1.2" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Client" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Client" -Name "Enabled" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Server" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.2\Server" -Name "Enabled" -Value 0 -Type DWord

Steps to configure TLS 1.1
The following table shows the Exchange Server/Windows Server combinations on which TLS 1.1
is supported. The table also shows the default configuration:

                                                                                   ﾉ    Expand table

 Exchange Server             Windows Server           Supported      Configured by default

 Exchange Server 2019        Any                      Yes            Yes ( disabled )

 Exchange Server 2016        Any                      Yes            No

 Exchange Server 2013        Any                      Yes            No

Enable TLS 1.1

  ７ Note

  The Microsoft TLS 1.1 implementation       has no known security vulnerabilities. But
  because of the potential for future protocol downgrade attacks and other TLS
  vulnerabilities, it is recommended to carefully plan and disable TLS 1.1. Failure to plan
  carefully may cause clients to lose connectivity.

<!-- p.777 -->

Run the following command from an elevated PowerShell window to enable TLS 1.1 for client
and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.1" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Client" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Client" -Name "Enabled" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Server" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Server" -Name "Enabled" -Value 1 -Type DWord

Disable TLS 1.1
Run the following command from an elevated PowerShell window to explicitly disable TLS 1.1
for client and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.1" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Client" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Client" -Name "Enabled" -Value 0 -Type DWord
  Set-ItemProperty -Path

<!-- p.778 -->

  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Server" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.1\Server" -Name "Enabled" -Value 0 -Type DWord

Steps to configure TLS 1.0
The following table shows the Exchange Server/Windows Server combinations on which TLS 1.0
is supported. The table also shows the default configuration:

                                                                                   ﾉ    Expand table

 Exchange Server             Windows Server           Supported      Configured by default

 Exchange Server 2019        Any                      Yes            Yes ( disabled )

 Exchange Server 2016        Any                      Yes            No

 Exchange Server 2013        Any                      Yes            No

Enable TLS 1.0

  ７ Note

  The Microsoft TLS 1.0 implementation        has no known security vulnerabilities. But
  because of the potential for future protocol downgrade attacks and other TLS
  vulnerabilities, it is recommended to carefully plan and disable TLS 1.0. Failure to plan
  carefully may cause clients to lose connectivity.

Run the following command from an elevated PowerShell window to enable TLS 1.0 for client
and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.0" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path

<!-- p.779 -->

  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Client" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Client" -Name "Enabled" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Server" -Name "DisabledByDefault" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Server" -Name "Enabled" -Value 1 -Type DWord

Disable TLS 1.0
Run the following command from an elevated PowerShell window to explicitly disable TLS 1.0
for client and server connections:

  PowerShell

  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols" -
  Name "TLS 1.0" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0" -Name "Client" -ErrorAction SilentlyContinue
  New-Item -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0" -Name "Server" -ErrorAction SilentlyContinue
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Client" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Client" -Name "Enabled" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Server" -Name "DisabledByDefault" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
  1.0\Server" -Name "Enabled" -Value 0 -Type DWord

Steps to configure TLS renegotiation strict mode
TLS strict mode is a security feature that ensures only clients with the necessary security
updates can establish and renegotiate TLS sessions with the server.

The following table shows the Exchange Server/Windows Server combinations with the default
TLS renegotiation strict mode configuration:

<!-- p.780 -->

                                                                                  ﾉ   Expand table

 Exchange Server             Windows Server         Supported       Configured by default

 Exchange Server 2019        Any                    Yes             Yes ( enabled )

 Exchange Server 2016        Any                    Yes             No

 Exchange Server 2013        Any                    No              N/A

Enable TLS renegotiation strict mode
Run the following command from an elevated PowerShell window to enable renegotiation
strict mode:

  PowerShell

  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL" -Name
  "AllowInsecureRenegoClients" -Value 0 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL" -Name
  "AllowInsecureRenegoServers" -Value 0 -Type DWord

Disable TLS renegotiation strict mode
Run the following command from an elevated PowerShell window to explicitly disable
renegotiation strict mode:

  PowerShell

  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL" -Name
  "AllowInsecureRenegoClients" -Value 1 -Type DWord
  Set-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL" -Name
  "AllowInsecureRenegoServers" -Value 1 -Type DWord

Validate TLS 1.2 or TLS 1.3 usage
Once TLS 1.2 or TLS 1.3 has been enabled, it can be helpful to validate your work was
successful and the system is able to negotiate TLS 1.2 or TLS 1.3 for inbound (server)
connections and outbound (client) connections. There are a few methods available for
validating TLS usage, some of them are discussed in the following sections.

<!-- p.781 -->

Many protocols used in Exchange Server are HTTP based, and therefore traverse the IIS
processes on the Exchange server. MAPI/HTTP, Outlook Anywhere, Exchange Web Services,
Exchange ActiveSync, REST, OWA & EAC, Offline Address Book downloads, and AutoDiscover
are examples of HTTP based protocols used by Exchange Server.

IIS logging
The Internet Information Services (IIS) team has added capabilities to Windows Server 2012 R2
or later to log custom fields related to encryption protocol versions and ciphers. We
recommend reviewing the blog for documentation on how to enable these custom fields
and begin parsing logs for information on incoming connections in your environment related
to HTTP based protocols.

These IIS custom fields do not exist for Windows Server version prior Windows Server 2012 R2.
Your load balancer or firewall logs may be able to provide this information. Please request
guidance from your vendors to determine if their logs may provide this information.

Microsoft Edge Developer Tools
You can utilize the Developer Tools , which are available with Microsoft Edge   , to check the
TLS version that was used to establish a secure connection, when connecting to Outlook on the
Web (OWA) or the Exchange Admin Center (ECP). To do this, follow these steps:

   1. Open the Microsoft Edge browser and establish an HTTPS connection to OWA or ECP.

   2. Press CTRL + SHIFT + I to open the Developer Tools .

   3. Click on the + symbol in the upper right corner.

   4. Click on Security in the dropdown menu.

   5. Check the TLS version in the Connection - secure connection settings section.

<!-- p.782 -->

                                                                                             

Message headers
Message header data in Exchange Server 2016 or later provides the protocol negotiated and
used when the sending and receiving host exchanged a piece of mail. You can use the Message
Header Analyzer       to get a clear overview of each hop.

There is a known exception to the message headers example. When a client sends a message
by connecting to a server using authenticated SMTP (also known as the SMTP client
submission protocol), the TLS version in the messages headers does not show the correct TLS
version used by the client. Microsoft is investigating the possibility of adding this information
in a future update.

SMTP logging
SMTP logs in Exchange Server contain the encryption protocol and other encryption related
information used during the exchange of email between two systems.

When the server is the SMTP receiving system , search for the Server value in the log
depending on the version of TLS used. If the server is the SMTP sending system , search for the
Client value in the log depending on the version of TLS used.

                                                                                 ﾉ   Expand table

 TLS version            Server value                         Client value

 TLS 1.0                SP_PROT_TLS1_0_SERVER                SP_PROT-TLS1_0_CLIENT

<!-- p.783 -->

 TLS version         Server value                           Client value

 TLS 1.1             SP_PROT_TLS1_1_SERVER                  SP_PROT-TLS1_1_CLIENT

 TLS 1.2             SP_PROT_TLS1_2_SERVER                  SP_PROT-TLS1_2_CLIENT

  ７ Note

  Support for SMTP TLS 1.3 will be included in an upcoming Exchange 2019 CU15 update.

The following example searches the log files on an Exchange server, which runs the mailbox
role, for connections that were made using the TLS 1.0 protocol:

  PowerShell

  Select-String -Path (((Get-TransportService -Identity
  $env:COMPUTERNAME).ReceiveProtocolLogPath).PathName.Replace("Hub","FrontEnd")+"\*.
  log") "SP_PROT_TLS1_0"

Example of searching log files on an Exchange server, which runs the Edge Transport role, for
connections that were made using the TLS 1.1 protocol:

  PowerShell

  Select-String -Path (((Get-TransportService -Identity
  $env:COMPUTERNAME).ReceiveProtocolLogPath).PathName+"\*.log") "SP_PROT_TLS1_1"

POP and IMAP
No logging exists that exposes the encryption protocol version used for POP and IMAP clients.
To capture this information, you may need to capture a Netmon trace from your server or
inspect traffic as it flows through your load balancer or firewall where HTTPS bridging is taking
place.

Cipher and hashing algorithms best practices
The steps in this section can be used to configure Exchange Server 2016 with the same set of
cipher and hashing algorithms as Exchange Server 2019. These steps are not necessary for
Exchange Server 2019, as it already comes with a preconfigured cipher and hashing algorithm
setup.

<!-- p.784 -->

As a prerequisite, you must first configure TLS 1.2 and then disable TLS 1.0 and TLS 1.1.
Consider applying the following settings separately from disabling TLS 1.0 and TLS 1.1 to
isolate configuration issues with problematic clients.

Enable recommended cipher suites

Windows Server 2012 and Windows Server 2012 R2
Run the following commands from an elevated PowerShell window to configure the
recommended cipher suites:

  PowerShell

  New-ItemProperty -Path
  "HKLM:\SYSTEM\CurrentControlSet\Control\Cryptography\Configuration\Local\SSL\00010
  002" -Name "Functions" -PropertyType MultiString -Value
  "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_
  P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P384,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
  256_P256,TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384_P384,TLS_ECDHE_ECDSA_WITH_AES_256
  _GCM_SHA384_P256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256_P384,TLS_ECDHE_ECDSA_WITH
  _AES_128_GCM_SHA256_P256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384_P384,TLS_ECDHE_EC
  DSA_WITH_AES_256_CBC_SHA384_P256,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256_P384,TLS_
  ECDHE_ECDSA_WITH_AES_128_CBC_SHA256_P256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P384,T
  LS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P384,TLS
  _ECDHE_RSA_WITH_AES_128_CBC_SHA_P256,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA_P384,TLS
  _ECDHE_ECDSA_WITH_AES_256_CBC_SHA_P256,TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA_P384,T
  LS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA_P256,TLS_RSA_WITH_AES_256_GCM_SHA384,TLS_RSA_W
  ITH_AES_128_GCM_SHA256" -Force

Windows Server 2016

Run the following commands from an elevated PowerShell window to configure the
recommended cipher suites.

  ７ Note

  It is possible to configure the cipher suites by utilizing a Group Policy Object (GPO). You
  can't configure them manually by using the Enable-TlsCipherSuite or Disable-
  TLSCipherSuite cmdlets if they were already configured via GPO or if the Functions
  registry entry already exists under the
   HKLM:\SOFTWARE\Policies\Microsoft\Cryptography\Configuration\SSL\00010002 path.

First, disable all cipher suites:

<!-- p.785 -->

  PowerShell

  foreach ($suite in (Get-TLSCipherSuite).Name) {
      if (-not([string]::IsNullOrWhiteSpace($suite))) {
          Disable-TlsCipherSuite -Name $suite -ErrorAction SilentlyContinue
      }
  }

Next, re-enable only the recommended TLS 1.2 cipher suites:

  PowerShell

  $cipherSuites = @('TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384',
                  'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256',
                  'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384',
                  'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256',
                  'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384',
                  'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256',
                  'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384',
                  'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256')

  $suiteCount = 0
  foreach ($suite in $cipherSuites) {
      Enable-TlsCipherSuite -Name $suite -Position $suiteCount
      $suiteCount++
  }

Disable outdated ciphers and hashes
Run the following command from an elevated PowerShell window to explicitly disable
outdated ciphers and hashes:

  PowerShell

  New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL"
  -Name "Hashes" -ErrorAction SilentlyContinue
  New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL"
  -Name "Ciphers" -ErrorAction SilentlyContinue
  (Get-Item
  HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
  hers", $true).CreateSubKey("DES 56/56")
  (Get-Item
  HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
  hers", $true).CreateSubKey("NULL")
  (Get-Item
  HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
  hers", $true).CreateSubKey("RC2 40/128")
  (Get-Item
  HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
  hers", $true).CreateSubKey("RC2 56/128")

<!-- p.786 -->

(Get-Item
HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
hers", $true).CreateSubKey("RC2 56/56")
(Get-Item
HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
hers", $true).CreateSubKey("RC4 40/128")
(Get-Item
HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
hers", $true).CreateSubKey("RC4 56/128")
(Get-Item
HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
hers", $true).CreateSubKey("RC4 64/128")
(Get-Item
HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
hers", $true).CreateSubKey("RC4 128/128")
(Get-Item
HKLM:).OpenSubKey("SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Cip
hers", $true).CreateSubKey("Triple DES 168")
New-Item -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Hashes" -Name
"MD5" -ErrorAction SilentlyContinue
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\DES
56/56" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\NULL" -
Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC2
40/128" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC2
56/128" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC2
56/56" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC4
40/128" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC4
56/128" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC4
64/128" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\RC4
128/128" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Ciphers\Triple
DES 168" -Name "Enabled" -Value 0 -Type DWord
Set-ItemProperty -Path
"HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Hashes\MD5" -
Name "Enabled" -Value 0 -Type DWord

<!-- p.787 -->

Configure the elliptic curve preference
It's recommended to disable the curve25519 elliptic curve as it's not available in FIPS mode.
More information can be found in the TLS Elliptic Curves in Windows 10 version 1607 and later
documentation.

Run the following command from an elevated PowerShell window to configure the elliptic
curve preference:

  PowerShell

  Disable-TlsEccCurve -Name "curve25519"
  Enable-TlsEccCurve -Name "NistP384" -Position 0
  Enable-TlsEccCurve -Name "NistP256" -Position 1

<!-- p.788 -->

Change Server deployment reference
Article • 05/09/2025

APPLIES TO:        2016   2019      Subscription Edition

Exchange Server readiness checks

Exchange Server editions and versions

Exchange Server language support

Exchange Server storage configuration options

Network ports for clients and mail flow in Exchange

Overview of Exchange services on Exchange servers

Exchange 2019 preferred architecture

<!-- p.789 -->

Exchange Server readiness checks
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

The article provides details about the readiness checks that Exchange Server does when
Exchange is installed. Readiness checks ensure that your Active Directory forest and Exchange
servers are ready for the version of Exchange that you're installing. Each readiness check article
describes the actions that you can take to resolve issues that are found when the readiness
checks are run. You should only do the steps outlined in a readiness check article if that
readiness check was displayed during setup.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.790 -->

AD LDS directory exists in default location
[ADAMDataPathExists]
07/23/2025

Exchange Setup can't continue because the attempt to install Active Directory Lightweight
Directory Services (AD LDS) failed.

An older installation of AD LDS exists in the default location. Setup can't perform a new AD LDS
install in an existing AD LDS directory structure.

To resolve this issue, remove the existing AD LDS directory and then run Setup again.

For more information about AD LDS directory management, see Administering AD LDS
Directory Partitions.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.791 -->

Duplicate Microsoft Exchange System
Objects container exists in Active Directory
[AdInitErrorRule]
07/23/2025

Exchange Setup can't continue because it found a duplicate Microsoft Exchange System
Objects container in Active Directory Domain Naming context. When Setup finds a duplicate
Microsoft Exchange System Objects container, you need to delete the duplicate container
before Setup can continue. Note that running DomainPrep again won't fix the problem. You
need to find and delete the duplicate Microsoft Exchange System Objects container.

To resolve this issue, do the following steps:

   1. Open Active Directory Users and Computers. For example:

             Press Windows key + R, enter dsc.msc, and then click OK.

             In Administrative Tools > Active Directory Users and Computers.

   2. In the Active Directory Users and Computers, click View > Advanced Features.

   3. Locate the duplicate Microsoft Exchange System Objects container.

   4. Verify that the duplicate Microsoft Exchange System Objects container doesn't contain
     valid Active Directory objects.

   5. Right-click the duplicate Microsoft Exchange System Objects container, click Delete, and
     then click Yes in the confirmation dialog box.

  ７ Note

  To immediately replicate the change, you need to manually initiate replication between
  domain controllers.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.792 -->

Failover Cluster Command Interface
Windows feature not installed
[RsatClusteringCmdInterfaceInstalled]
07/23/2025

Microsoft Exchange Server 2016 Setup can't continue because the local computer is missing a
required Windows feature. You'll need to install this Windows feature before Exchange 2016
can continue.

Exchange 2016 Setup requires that the Failover Cluster Command Interface Windows feature
be installed on the computer before installation can continue.

Do the following to install the Windows feature on this computer. If the feature requires a
reboot to complete installation, you'll need to exit Exchange 2016 Setup, reboot, and then start
Setup again.

  ７ Note

  Additional Windows features or updates might need to be installed before Exchange 2016
  Setup can continue. For a complete list of required Windows features and updates, check
  out Exchange Server prerequisites.

   1. Open Windows PowerShell on the local computer.

   2. Run the following command to install the required Windows feature.

       PowerShell

        Install-WindowsFeature RSAT-Clustering-CmdInterface

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.793 -->

Active Directory doesn't exist or can't be
contacted [CannotAccessAD]
07/23/2025

Exchange Setup can't continue because it can't contact a valid Active Directory site. Setup
requires that the target server is able to locate the configuration naming context in Active
Directory.

To resolve this issue, verify that the account that you're using an Active Directory account to
run Setup, and then try running Setup again. If this doesn't resolve the issue, follow the
guidance about using the support tools in the following articles to further diagnose the
problem.

For more information about Active Directory troubleshooting and configuration for Exchange,
see the following articles:

     Prepare Active Directory and domains
     Troubleshooting Active Directory Domain Services
     Configuring a Computer for Troubleshooting
     Troubleshooting Active Directory Replication Problems

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.794 -->

The local computer isn't joined to an Active
Directory domain
[ComputerNotPartofDomain]
07/23/2025

Exchange Setup can't continue because it detected that the target server isn't a member of an
Active Directory domain. You need to join the target server to an Active Directory domain
before you can install the Mailbox server role. You might also see this message if you're using a
local computer account instead of a domain user account (with the required permissions) to
install Exchange.

For more information, see Exchange Server system requirements

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.795 -->

Installation of the first Exchange server in
the organization can't be delegated
[DelegatedBridgeheadFirstInstall]
07/23/2025

Exchange Setup can't continue because this is the first Exchange server in the organization, and
the first Exchange server needs to be installed by a member of the Enterprise Admins security
group (to create the Exchange Organization container and configure objects in it).

Note: If you haven't already extended the Active Directory schema for Exchange, you need to
do one of the following steps:

     A member of the Schema Admins group can extend the Active Directory schema using
     another computer in the domain before you install Exchange.

     Exchange Setup can extend the schema if your account is a member of the Schema
     Admins group.

To resolve this issue, run Exchange setup again using an account that's a member of the
Enterprise Admins security group (add the current account or use a different account).

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.796 -->

Installation of the first Exchange server in
the organization can't be delegated
[DelegatedCafeFirstInstall]
07/23/2025

Exchange Setup can't continue because this is the first Exchange server in the organization, and
the first Exchange server needs to be installed by a member of the Enterprise Admins security
group (to create the Exchange Organization container and configure objects in it).

Note: If you haven't already extended the Active Directory schema for Exchange, you need to
do one of the following steps:

     A member of the Schema Admins group can extend the Active Directory schema using
     another computer in the domain before you install Exchange.

     Exchange Setup can extend the schema if your account is a member of the Schema
     Admins group.

To resolve this issue, run Exchange setup again using an account that's a member of the
Enterprise Admins security group (add the current account or use a different account).

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.797 -->

Installation of the first Exchange server in
the organization can't be delegated
[DelegatedClientAccessFirstInstall]
07/23/2025

Exchange Setup can't continue because this is the first Exchange server in the organization, and
the first Exchange server needs to be installed by a member of the Enterprise Admins security
group (to create the Exchange Organization container and configure objects in it).

Note: If you haven't already extended the Active Directory schema for Exchange, you need to
do one of the following steps:

     A member of the Schema Admins group can extend the Active Directory schema using
     another computer in the domain before you install Exchange.

     Exchange Setup can extend the schema if your account is a member of the Schema
     Admins group.

To resolve this issue, run Exchange setup again using an account that's a member of the
Enterprise Admins security group (add the current account or use a different account).

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.798 -->

Installation of the first Exchange server in
the organization can't be delegated
[DelegatedMailboxFirstInstall]
07/23/2025

Exchange Setup can't continue because this is the first Exchange server in the organization, and
the first Exchange server needs to be installed by a member of the Enterprise Admins security
group (to create the Exchange Organization container and configure objects in it).

Note: If you haven't already extended the Active Directory schema for Exchange, you need to
do one of the following steps:

     A member of the Schema Admins group can extend the Active Directory schema using
     another computer in the domain before you install Exchange.

     Exchange Setup can extend the schema if your account is a member of the Schema
     Admins group.

To resolve this issue, run Exchange setup again using an account that's a member of the
Enterprise Admins security group (add the current account or use a different account).

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.799 -->

Installation of the first Exchange server in
the organization can't be delegated
[DelegatedUnifiedMessagingFirstInstall]
07/23/2025

Exchange 2016 Setup can't continue because this is the first Exchange server in the
organization, and the first Exchange server needs to be installed by a member of the Enterprise
Admins security group (to create the Exchange Organization container and configure objects in
it).

Note: If you haven't already extended the Active Directory schema for Exchange, you need to
do one of the following steps:

       A member of the Schema Admins group can extend the Active Directory schema using
       another computer in the domain before you install Exchange.

       Exchange Setup can extend the schema if your account is a member of the Schema
       Admins group.

To resolve this issue, run Exchange setup again using an account that's a member of the
Enterprise Admins security group (add the current account or use a different account).

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.

<!-- p.800 -->

The Active Directory must be modified with
'Setup /PrepareAD' before domains can be
prepared for Exchange
[DomainPrepWithoutADUpdate]
07/23/2025

Exchange Setup can't continue because it detected that the PrepareAD has not been run. Your
account needs to be a member of the Enterprise Admins security group. The computer needs
to be a member of the same Active Directory domain and site as the schema master, and must
be able to contact all of the domains in the forest on TCP port 389. For more information, see
Prepare Active Directory and domains for Exchange Server.

Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange Server |
Management.
