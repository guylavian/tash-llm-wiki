---
title: "Nessus Says 'Microsoft Exchange Server Unsupported Version Detection' in Exchange 2016 (CU17) Critical Vulnerability"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/262886/nessus-says-microsoft-exchange-server-unsupported
question_id: 262886
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Nessus Says 'Microsoft Exchange Server Unsupported Version Detection' in Exchange 2016 (CU17) Critical Vulnerability

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/262886/nessus-says-microsoft-exchange-server-unsupported (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

When we run this Nessus scan tool "Microsoft Exchange Server Unsupported Version Detection"  

https://www.tenable.com/plugins/nessus/22313  

We have Upgraded CUs from Exchange 2016 (CU3) to Exchange (CU17).  

Still the same report says "Microsoft Exchange Server Unsupported Version Detection"  

How to fix this issue? without any impact.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-11*

Hello Ashok,  

After installed CU19 in Exchange 2016 .Now its all good now. Thanks for your support.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

Hello @Sathishkumar Singh   ,    

Thank you for sharing the logs.     

Error: Out of date Cumulative Update. Please upgrade to one of the two most recently released Cumulative Updates. Currently running on a build that is 260 days old.    

This indicates that the Exchange CU17 is 9 months old and the support is ended. So, this states that it has to be upgraded to CU18 or CU19.     

    

https://practical365.com/exchange-server/fixing-outdate-cumulative-updates-net-framework/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-03*

Hello Ashok,    

When i run HealthCheck Latest Script.    

below i found few details. What is the fix to be done?    

    

Build Version Shows CU17     

But Exchange IU or Security Hotfix Detected.    

Security Update for Exchange Server 2016 Cumulative Update 3 (KB4012178)    

below whole report    

Exchange Health Checker version 3.3.1    

Virtual Machine detected.  Certain settings about the host hardware cannot be detected from the virtual machine.  Verify on the VM Host that:    

```
- There is no more than a 1:1 Physical Core to Virtual CPU ratio (no oversubscribing)  
- If Hyper-Threading is enabled do NOT count Hyper-Threaded cores as physical cores  
- Do not oversubscribe memory or use dynamic memory allocation
```

Although Exchange technically supports up to a 2:1 physical core to vCPU ratio, a 1:1 ratio is strongly recommended for performance reasons.  Certain third party Hyper-Visors such as VMWare have their own guidance.    

VMWare recommends a 1:1 ratio.  Their guidance can be found at https://www.vmware.com/files/pdf/Exchange_2013_on_VMware_Best_Practices_Guide.pdf.    

Related specifically to VMWare, if you notice you are experiencing packet loss on your VMXNET3 adapter, you may want to review the following article from VMWare:  http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=2039495.    

For further details, please review the virtualization recommendations on Microsoft Learn at the following locations:    

Exchange 2013: https://learn.microsoft.com/en-us/exchange/exchange-2013-virtualization-exchange-2013-help#requirements-for-hardware-virtualization.    

Exchange 2016/2019: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/virtualization?view=exchserver-2019.    

Exchange Information    

--------------------    

Name: EXC01    

Version: Exchange 2016 CU17    

Build Number: 15.1.2044.4    

Error: Out of date Cumulative Update. Please upgrade to one of the two most recently released Cumulative Updates. Currently running on a build that is 260 days old.    

Exchange IU or Security Hotfix Detected.    

Security Update for Exchange Server 2016 Cumulative Update 3 (KB4012178)    

Server Role: Mailbox    

DAG Name:     

AD Site: UK    

MAPI/HTTP Enabled: True    

Exchange Server Maintenance: Server is not in Maintenance Mode    

Operating System Information    

----------------------------    

Version: Microsoft Windows Server 2012 R2 Standard    

System Up Time: 25 day(s) 17 hour(s) 28 minute(s) 2 second(s)    

Time Zone: W. Europe Standard Time    

Dynamic Daylight Time Enabled: True    

.NET Framework: 4.8    

Page File Size: 20000MB     

Warning: Page File is not set to Total System Memory plus 10MB which should be 20490MB    

Power Plan: Balanced --- Error    

Http Proxy Setting: <None>    

Visual C++ 2012: Redistributable is outdated    

Visual C++ 2013: Redistributable is outdated    

Note: For more information about the latest C++ Redistributeable please visit: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads    

This is not a requirement to upgrade, only a notification to bring to your attention.    

Server Pending Reboot: True --- Warning a reboot is pending and can cause issues on the server.    

Processor/Hardware Information    

------------------------------    

Type: VMWare    

Processor: Intel(R) Xeon(R) Gold 6240R CPU @ 2.40GHz    

Number of Processors: 2    

Note: Please make sure you are following VMware's performance recommendation to get the most out of your guest machine. VMware blog 'Does corespersocket Affect Performance?' https://blogs.vmware.com/vsphere/2013/10/does-corespersocket-affect-performance.html    

Number of Physical Cores: 4    

Number of Logical Cores: 4    

Hyper-Threading: Disabled    

All Processor Cores Visible: Passed    

Max Processor Speed: 2400    

Physical Memory: 20 GB    

NIC Settings Per Active Adapter    

-------------------------------    

Interface Description: vmxnet3 Ethernet Adapter [Ethernet0]    

Driver Date: 2020-12-01    

Driver Version: 1.8.17.0    

MTU Size: 1500    

Max Processors:     

Max Processor Number:     

Number of Receive Queues:     

RSS Enabled: False --- Warning: Enabling RSS is recommended.    

Link Speed: 10000 Mbps --- This may not be accurate due to virtualized hardware    

IPv6 Enabled: True    

IPv4 Address:     

Address: 10.XXXX\24 Gateway: 10.XXXX    

IPv6 Address:     

DNS Server: 10.XXXXXX 192.168.XXXX    

Registered In DNS: True    

Sleepy NIC Disabled: False --- Warning: It's recommended to disable NIC power saving options    

More Information: http://support.microsoft.com/kb/2740020    

Packets Received Discarded: 0    

Frequent Configuration Issues    

-----------------------------    

TCP/IP Settings: Not Set     

Error: Without this value the KeepAliveTime defaults to two hours, which can cause connectivity and performance issues between network devices such as firewalls and load balancers depending on their configuration.     

More details: https://techcommunity.microsoft.com/t5/Exchange-Team-Blog/Checklist-for-troubleshooting-Outlook-connectivity-in-Exchange/ba-p/604792    

RPC Min Connection Timeout: 0     

More Information: https://blogs.technet.microsoft.com/messaging_with_communications/2012/06/06/outlook-anywhere-network-timeout-issue/    

FIPS Algorithm Policy Enabled: 0    

CTS Processor Affinity Percentage: 0    

Credential Guard Enabled: False    

EdgeTransport.exe.config Present: True    

Security Settings    

-----------------    

LmCompatibilityLevel Settings: 3    

Description: Clients use only NTLMv2 authentication, and they use NTLMv2 session security if the server supports it. Domain controllers accept LM, NTLM, and NTLMv2 authentication.    

TLS 1.0    

Server Enabled: True    

Server Disabled By Default: False    

Client Enabled: True    

Client Disabled By Default: False    

TLS 1.1    

Server Enabled: True    

Server Disabled By Default: False    

Client Enabled: True    

Client Disabled By Default: False    

TLS 1.2    

Server Enabled: True    

Server Disabled By Default: False    

Client Enabled: True    

Client Disabled By Default: False    

SystemDefaultTlsVersions: True    

SystemDefaultTlsVersions - Wow6432Node: True    

SchUseStrongCrypto: False    

SchUseStrongCrypto - Wow6432Node: False    

SecurityProtocol: SystemDefault    

Certificate:     

FriendlyName: *.pm.com    

Thumbprint: 07963183428948BE8410D043406B51932C161D92    

Lifetime in days: 257    

Key size: 2048    

Bound to services: None    

Current Auth Certificate: False    

SAN Certificate: True    

Namespaces:     

*.pm.com    

pm.com    

Certificate:     

FriendlyName: Exchange Delegation Federation    

Thumbprint: 9571E40A906FC2BADB643B73BAF631AD7F2F73D2    

Lifetime in days: 288    

Key size: 2048    

Bound to services: SMTP, Federation    

Current Auth Certificate: False    

SAN Certificate: False    

Namespaces:     

Federation    

Certificate:     

FriendlyName: pm.com    

Thumbprint: ACC8BDF5DCD7FFFE524A7767GFHJNBGHJV789532    

Lifetime in days: 278    

Key size: 2048    

Bound to services: IMAP, POP, IIS, SMTP    

Current Auth Certificate: False    

SAN Certificate: True    

Namespaces:     

webmail.pm.com    

exc01.pm.local    

AutoDiscover.PM.local    

AutoDiscover.pm.com    

EXC01    

PM.LOCAL    

pm.com    

Certificate:     

FriendlyName: Microsoft Exchange Server Auth Certificate    

Thumbprint: 6178C9EDF4B2366FB675DECAC547I6876778798    

Lifetime in days: 243    

Key size: 2048    

Bound to services: SMTP    

Current Auth Certificate: True    

SAN Certificate: False    

Namespaces:     

Microsoft Exchange Server Auth Certificate    

Certificate:     

FriendlyName: Microsoft Exchange    

Thumbprint: FB0732CCA78544571A6B6467T866B7H8BFDS658    

Lifetime in days: 269    

Key size: 2048    

Bound to services: IIS, SMTP    

Current Auth Certificate: False    

SAN Certificate: True    

Namespaces:     

EXC01    

EXC01.PM.LOCAL    

Certificate:     

FriendlyName: WMSVC    

Thumbprint: 298776VD,9607C55160474555EA6DD0A1B17974    

Lifetime in days: 2090    

Key size: 2048    

Bound to services: None    

Current Auth Certificate: False    

SAN Certificate: False    

Namespaces:     

WMSvc-EXC01    

Valid Auth Certificate Found On Server: True    

SMB1 Installed: True    

SMB1 Blocked: False    

SMB1 should be uninstalled SMB1 should be blocked    

More Information: https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-and-smbv1/ba-p/1165615    

Security Vulnerability: CVE-2020-16875    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16875 for more information.    

Security Vulnerability: CVE-2020-16969    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16969 for more information.    

Security Vulnerability: CVE-2020-17083    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17083 for more information.    

Security Vulnerability: CVE-2020-17084    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17084 for more information.    

Security Vulnerability: CVE-2020-17085    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17085 for more information.    

Security Vulnerability: CVE-2020-17117    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17117 for more information.    

Security Vulnerability: CVE-2020-17132    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17132 for more information.    

Security Vulnerability: CVE-2020-17141    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17141 for more information.    

Security Vulnerability: CVE-2020-17142    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17142 for more information.    

Security Vulnerability: CVE-2020-17143    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17143 for more information.    

Security Vulnerability: CVE-2021-24085    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-24085 for more information.    

Security Vulnerability: CVE-2021-26412    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-26412 for more information.    

Security Vulnerability: CVE-2021-27078    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-27078 for more information.    

Security Vulnerability: CVE-2021-26854    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-26854 for more information.    

Security Vulnerability: CVE-2021-26855    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-26855 for more information.    

Security Vulnerability: CVE-2021-26857    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-26857 for more information.    

Security Vulnerability: CVE-2021-26858    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-26858 for more information.    

Security Vulnerability: CVE-2021-27065    

See: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2021-27065 for more information.    

Exchange Web App Pools    

----------------------    

Web App Pool: GC Server Mode Enabled | Status    

MSExchangeMapiFrontEndAppPool: False | Started    

MSExchangeOWAAppPool: False | Started    

MSExchangeECPAppPool: False | Started    

MSExchangeRestAppPool: False | Started    

MSExchangeMapiAddressBookAppPool: False | Started    

MSExchangeRpcProxyFrontEndAppPool: False | Started    

MSExchangePowerShellAppPool: False | Started    

MSExchangePowerShellFrontEndAppPool: False | Started    

MSExchangeRestFrontEndAppPool: False | Started    

MSExchangeMapiMailboxAppPool: False | Started    

MSExchangeOABAppPool: False | Started    

MSExchangePushNotificationsAppPool: False | Started    

MSExchangeOWACalendarAppPool: False | Started    

MSExchangeAutodiscoverAppPool: False | Started    

MSExchangeServicesAppPool: False | Started    

MSExchangeSyncAppPool: False | Started    

MSExchangeRpcProxyAppPool: False | Started    

Output file written to .\HealthCheck-EXC01-20210303144456.txt    

Exported Data Object Written to .\HealthCheck-EXC01-20210303144456.xml     

 Please advise
