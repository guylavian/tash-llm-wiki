---
title: "Issue with Exchange 2019 on premise management shell after server 2025 \"upgrade\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2156044/issue-with-exchange-2019-on-premise-management-she
question_id: 2156044
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue with Exchange 2019 on premise management shell after server 2025 "upgrade"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2156044/issue-with-exchange-2019-on-premise-management-she (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is occurring on 2 sites that we are trying to migrate from on premise exchange and since the "auto" upgrade of server 2025 happened we are unable to access the management console  

The Exchange Admin Centre appears to be working fine and the SSL certificate is up to date  

Any help is appreciated

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-03*

Remote Management Enablement for EXCHANGESE (contoso.com)

It’s been a challenging process, but we identified the specific Group Policy Object (GPO) settings that were preventing the Exchange Health Check and Management Tools from functioning correctly when accessed remotely from a new server—other than the original EXCH1. The configuration below now enables remote management from the SCOM server, allowing it to check health status, report accurately, and run both the Exchange Management Shell and Exchange Toolbox to manage the EXCHANGESE server as needed.

With remote monitoring and management now operational, I’m shifting focus to getting the tools to work locally. I suspect the issue is related to Credential Passing and may require a similar solution. Meanwhile, I’ve begun the decommissioning process for the EXCH2016 server.

Understanding the Kerberos Double-Hop Issue in EMS

When accessing the Exchange Management Shell (EMS), the Kerberos double-hop issue becomes a critical factor—especially when launching EMS remotely or even locally if it attempts to authenticate to itself or another service.

What Happens During EMS Launch:

-  EMS uses remote PowerShell to connect to the Exchange server—even for local launches.

-  Authentication is attempted via Kerberos, which is secure but strict.

-  If EMS needs to access another service (e.g., Active Directory), it must delegate your credentials.

-  Without proper delegation, Kerberos blocks the second hop—causing EMS to hang or fail.

Configuration Changes for Secure Remote Management of EXCHANGESE

To overcome the Kerberos double-hop limitation and enable secure remote management, the following GPO and Active Directory configurations were applied:

-  Enable Credential Delegation via Group Policy

On the client machine or via domain-level GPO:

Navigate to: `Computer Configuration → Administrative Templates → System → Credentials Delegation`

Enable these policies:

-  Allow Delegating Fresh Credentials

-  Allow Delegating Fresh Credentials with NTLM-only Server Authentication

      Configure with the following SPNs:

```
WSMAN/exchangese.contoso.com
```

HTTP/exchangese.contoso.com
RPC/exchangese.contoso.com
HOST/exchangese.contoso.com
WSMAN/exchangese
HTTP/exchangese
RPC/exchangese
HOST/exchangese
      ```

These SPNs cover WinRM, HTTP endpoints, RPC services, and host-level authentication for both the FQDN and short hostname of the Exchange server.

-  Configure Constrained Delegation in Active Directory

On the computer or user account initiating the remote session:

-  Open Active Directory Users and Computers

-  Locate the account, open Properties

-  Go to the Delegation tab

-  Select:

-  “Trust this computer/user for delegation to specified services only”

-  “Use Kerberos only”

-  Add the following services:

```
WSMAN/exchangese.contoso.com
```

HTTP/exchangese.contoso.com
RPC/exchangese.contoso.com
HOST/exchangese.contoso.com
WSMAN/exchangese
HTTP/exchangese
RPC/exchangese
HOST/exchangese
      ```

-  Verify SPN Registration

Ensure the EXCHANGESE server’s computer account in Active Directory has these SPNs registered:

```
WSMAN/exchangese.contoso.com
HTTP/exchangese.contoso.com
RPC/exchangese.contoso.com
HOST/exchangese.contoso.com
WSMAN/exchangese
HTTP/exchangese
RPC/exchangese
HOST/exchangese
```

Missing SPNs can result in failed authentication or session hangs during remote PowerShell sessions.

-  Configure WinRM for HTTPS (Optional)

If Kerberos trust cannot be established or constrained delegation isn’t feasible, configure WinRM to use HTTPS with a valid SSL certificate:

```
PS E:\Program Files\Microsoft\Exchange Server\V15\bin> winrm get winrm/config/client
Client
    NetworkDelayms = 5000
    URLPrefix = wsman
    AllowUnencrypted = false
    Auth
        Basic = true [Source="GPO"]
        Digest = true
        Kerberos = true
        Negotiate = true
        Certificate = true
        CredSSP = false
    DefaultPorts
        HTTP = 5985
        HTTPS = 5986
    TrustedHosts = *.contoso.com [Source="GPO"]
    spn_prefix = HOST
```

✅ Outcome

With these configurations in place:

-  Remote PowerShell sessions to EXCHANGESE authenticate successfully

-  EMS launches without delays or credential errors

-  Credential delegation is secure, compliant, and scalable for enterprise use

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-03*

Same here. Upgraded our Jump Host from Server 2019 to 2025 and the Exchange Mgmt Shell stopped working showing this WinRM error.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-02*

We are currently running into the same problem using ECP in Exchange Server 2019 CU15 running on Windows Server 2025. Due to the EOL on October the 14th it is a delicate issue in my opinion.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-11*

Hi, @Darren Woolley

Welcome to the Microsoft Q&A platform! 

Today Exchange Server 2019 releases CU15. with the release of CU15, CU13 is now no longer supported due to the “N-1” policy. If you are using an older version, please update it and try again.

Released: 2025 H1 Cumulative Update for Exchange Server | Microsoft Community Hub

If you are a supportable version. Depending on the error message, this could be that WinRM is not enabled or the listener is not configured. Run the following command as administrator:

```
winrm quickconfig
winrm enumerate winrm/config/listener
```

This will start the WinRM service, set it to start automatically, and configure a listener for WS-Management protocol messages.

Installation and configuration for Windows Remote Management - Win32 apps | Microsoft Learn

If you are using a non-domain member, you must use Basic Authentication, and you must also set Basic Authentication on the virtual directory, as shown below:

```
Get-PowerShellVirtualDirectory -Server ServerName | Set-PowerShellVirtualDirectory -BasicAuthentication:$TRUE
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
