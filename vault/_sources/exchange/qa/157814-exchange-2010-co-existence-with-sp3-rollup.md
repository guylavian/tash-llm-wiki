---
title: "Exchange 2010 Co-Existence with SP3 & Rollup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/157814/exchange-2010-co-existence-with-sp3-rollup
question_id: 157814
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2010 Co-Existence with SP3 & Rollup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/157814/exchange-2010-co-existence-with-sp3-rollup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Friends,  

we have Exchange 2010 SP3 with 2 DAG members & 2 Cas-Hub Server in our environment recently we got an update that TLS 1.0 & 1.1 will not be supported anymore in a few weeks now we have two choices and either to update the existing CAS-HUB server which can support TLS 1.2 or more.  

I plan to co-exist with another  CAS-HUB server with Windows 2012 R2 along with Exchange 2010 SP3 7 Rollup 20 or more but will keep the existing environment the same, please advise.  

Can someone please also advise me which is the easiest way to co-exist the new CAS_HUB server or to update the existing which supports TLS 1.2 or more?  

 Please advise  

Thanks   

Ehsan

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-16*

Hi @Ehsan Shakeeb   ,    

For the solution you proposed, it is acceptable that each server in Exchange 2010 is in a different RU, but the requirement to enable TLS 1.2 should also be considered. So I suggest that you first grab the network packets between CAS/HUB and Mailbox server separately to check whether the communication between these two servers and Mailbox server needs TLS 1.2 encryption.    

In addition, for security reasons, we recommend that all your servers enable TLS 1.2 encryption, because even if the communication between CAS/HUB and Mailbox server does not require TLS 1.2 encryption, the communication between Mailbox server and other servers is also requires TLS 1.2 encryption.     

As stated in the previous reply, Exchange 2010 has been end of support, so for the security of your Exchange organization, it is recommended that you upgrade to a higher version of Exchange as soon as possible.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

Dear Friends,  

Thanks for the above replies, yes, of course, we will be moving to exchange online very soon I will be looking for some temporary solution as our Antispam vendor is forced to stop TLS 1.0 & 1.1 however they gave a workaround to turn off the TLS if can't upgrade.  

Also, I was thinking if I can install a new CAS-HUB server in my environment with windows 2012 R2 with Exchange 2010 SP3 RU latest because windows 2012 by default support TLS 1.2.  

but I don't want to touch my DAG servers can the exchange 2010 environment accept that some server is with RU latest and some without.   

Kindly I need guidance on it.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

Hi @Ehsan Shakeeb   ,  

We could enable the TLS 1.2 for Exchange 2010, but before setting, please meet the following conditions:  

1.For Exchange server version, Exchange 2010 must be at least RU19 or higher to support TLS 1.2. If you also need to prohibit TLS 1.0 and 1.1, at least RU20 or higher. So it’s recommend upgrade your Exchange server 2010 to the last version. Install the latest version of .NET 3.5.1 and patches.  

In addition, I agree with what AshokM-8240 said, Exchange 2010 will end support on October 13, 2020, so it is recommended that you upgrade Exchange to a higher version as soon as possible.  

For more information: Exchange 2010 end of support roadmap

2.For Windows server versions, your version is at least Windows server 2008 R2 SP1 to support TLS 1.2, but it is disabled by default. And please make sure your server is the latest version.  

For the conditions required to enable TLS 1.2 in Exchange server, please refer to: Exchange Server TLS guidance, part 1: Getting Ready for TLS 1.2

3.Then please following the steps to enable the TLS 1.2 for .NET 3.5:  

-  From Notepad.exe, create a text file named NET35-UseSchannelDefaults.reg.  

-  Copy, and then paste the following text.    Windows Registry Editor Version 5.00  

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft.NETFramework\v2.0.50727]  

    "SystemDefaultTlsVersions"=dword:00000001  

    [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft.NETFramework\v2.0.50727]  

    "SystemDefaultTlsVersions"=dword:00000001  

3) Save the NET35-UseSchannelDefaults.reg file.  

4) Double-click the NET35-UseSchannelDefaults.reg file.  

5) Click Yes to update your Windows Registry with these changes.  

6) Restart your computer for the change to take effect.  

For more specific steps you could refer to the first link provide by AshokM-8240.  

In addition, please note that incorrectly modifying the registry may cause errors, so please back up your registry file before operating. For specific methods, you can refer to: How to back up and restore the registry in Windows

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-10*

Hi,    

First of all, Exchange 2010 support has been ended and you should plan to upgrade Exchange to the latest supported environment.    

For TLS 1.2, you have to fully patch the OS and the Exchange 2010 to the latest RU and then enable the TLS 1.2.    

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-2-enabling-tls-1-2-and/ba-p/607761    

https://www.microsoft.com/security/blog/2017/07/20/tls-1-2-support-added-to-windows-server-2008/    

https://learn.microsoft.com/en-us/lifecycle/products/exchange-server-2010    

https://jaapwesselius.com/2018/10/05/exchange-2010-and-tls-1-2/comment-page-1/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
