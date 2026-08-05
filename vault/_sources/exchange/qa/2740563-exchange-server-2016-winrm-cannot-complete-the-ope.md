---
title: "Exchange server 2016 Winrm Cannot Complete the Operation."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2740563/exchange-server-2016-winrm-cannot-complete-the-ope
question_id: 2740563
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 26
qa_tags: []
---
# Exchange server 2016 Winrm Cannot Complete the Operation.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2740563/exchange-server-2016-winrm-cannot-complete-the-ope (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

While Starting Exchange Server Management Shell. I get the following error, I can ping my Active Directory Server & I can login with new domain name also on the server 2012 r2, I dont know how to solve the same, Kindly help.

New-PSSession : [ex01.systems.in] Connecting to remote server ex01.systems.in failed with the  

following error message : WinRM cannot complete the operation. Verify that the specified computer name is valid, that  

the computer is accessible over the network, and that a firewall exception for the WinRM service is enabled and allows  

access from this computer. By default, the WinRM firewall exception for public profiles limits access to remote  

computers within the same local subnet. For more information, see the about_Remote_Troubleshooting Help topic.  

At line:1 char:1  

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Microsoft.Excha ...  

- 

```

```

    + CategoryInfo          : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  

   gTransportException  

    + FullyQualifiedErrorId : WinRMOperationTimeout,PSSessionOpenFailed  

Exception calling "FindAll" with "0" argument(s): "Unknown error (0x80005000)"  

At C:\Program Files\Microsoft\Exchange Server\V15\bin\ConnectFunctions.ps1:253 char:2  

-      $search.FindAll()  

-      ~~~~~~~~~~~~~~~~~  

    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException  

    + FullyQualifiedErrorId : COMException

WARNING: No Exchange servers are available in the Active Directory site Default-First-Site-Name. Connecting to an  

Exchange server in another Active Directory site.

## Answer (community) — community member

*upvotes: 0 · updated: 2017-06-07*

Hi,

Your question is outside the scope of this Community.

I suggest that you repost your Question in the TechNet Exchange Forums.

https://social.technet.microsoft.com/Forums/exchange/en-us/home?category=exchangeserver

And/or here:

https://social.technet.microsoft.com/Forums/exchange/en-US/home?forum=exchangesvrgeneral

TechNet Server Forums. 

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

Or MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
