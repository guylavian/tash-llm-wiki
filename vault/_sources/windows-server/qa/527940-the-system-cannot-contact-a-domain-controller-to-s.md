---
title: "The System cannot contact a domain controller to service the authentication reqeust.  Please try again later."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/527940/the-system-cannot-contact-a-domain-controller-to-s
question_id: 527940
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# The System cannot contact a domain controller to service the authentication reqeust.  Please try again later.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/527940/the-system-cannot-contact-a-domain-controller-to-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Environment: Windows 2012 Standard Server | Windows 10 clients.

Recently, customer's ISP installed a modem/router on the network that was running DHCP. This caused their equipment to begin dishing out IP addresses. I eventually found this; disabled DHCP Service on the router, and re-enabled DHCP on the Domain Controller/DHCP/DNS server. Verified that client workstations were now correctly obtaining IP from the server.

We found however, that multiple client workstations are unable to correctly authenticate to the server. They first receive this message:  

  

During the process of troubleshooting, I found that the time on the workstation differed from that on the server by 2 minutes. Matching it addressed the issue on a few workstations, but issue remains on a few.

I see that a possible resolution is to remove and rejoin to the domain.

I've also flushed DNS from the server. DNS server Service restarted. Event Logs are clean.

Any other suggestions would be welcome.

Thanks in advance.

Regards,  

Rudy

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-04*

I had this issue on one computer that did not want to connect to a NAS.

I had to set Restrict NTLM to Disable on the local machine accessing the resouce.

Powershell -> secpol -> Local Policies -> Security Options -> Network security: Restrict NTLM... -> Set to Disable

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-26*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-26*

Hello RudolfAmarlapudi,  

In this case, if the ammount of remaining affected machines if not very big, the fastest solution would be to re-join them in the domain since everything else seems to work fine now. There might be a number of causes why that machines remain not able to authenticate, but I suspect something related with AD token expiration during the time that were not able to authenticate.   

Best regards,  

Luis P

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-25*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
