---
title: "exchange 2013 cannot connect to EMS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/185148/exchange-2013-cannot-connect-to-ems
question_id: 185148
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# exchange 2013 cannot connect to EMS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/185148/exchange-2013-cannot-connect-to-ems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have this problem since a lot of time and still not able to solve  

When I try to connect to exchange 2013 trow the consolle I get this error:

VERBOSE: Connecting to echange.mydomain.net.it.  

New-PSSession : [echange.mydomain.net.it] Connecting to remote server echange.mydomain.net.it failed with the  

following error message : WinRM cannot complete the operation. Verify that the specified computer name is valid, that  

the computer is accessible over the network, and that a firewall exception for the WinRM service is enabled and allows  

access from this computer. By default, the WinRM firewall exception for public profiles limits access to remote  

computers within the same local subnet. For more information, see the about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Microsoft.Excha ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

gTransportException  

-  FullyQualifiedErrorId : WinRMOperationTimeout,PSSessionOpenFailed  

VERBOSE: Connecting to echange.mydomain.net.it.

I follow some article, like

check the certificate on backend (changed between the public certificate and the exchange builtin one)  

and  

check then Winrm listener

Winrm enumerate winrm/config/listener  

Listener  

Address = *  

Transport = HTTP  

Port = 5985  

Hostname  

Enabled = true  

URLPrefix = wsman  

CertificateThumbprint  

ListeningOn = 10.0.0.250, 127.0.0.1, ::1, fe80::5efe:10.0.0.250%13, fe80::29  

8f:dd6a:b43d:a2cf%12

the only solution is to restart the server than it works for some days than stop again

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

still working.   

Thank you
