---
title: "External adfs not working for office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5046370/external-adfs-not-working-for-office-365
question_id: 5046370
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# External adfs not working for office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5046370/external-adfs-not-working-for-office-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! I really need someone to help me out now since i spent days learning and doing labs and i finally made it but not completely. I have 3 VMs, 1 DC, ADFS server and ADFS proxy server with 2 NICs. Internally i can reach the ADFS login page with https://adfs.domain.com/adfs/ls/idpinitiatedsignon.aspx and
 its working. But i want to be able to reach the ADFS externally, so i created a public DNS record for adfs.domain.com and pointed it to my public ip and
 in my router i configured port forwarding so that when the request comes in, it should be sent to my ADFS proxy server which will pass it to the ADFS server and etc. But when i try to reach the ADFS https://adfs.domain.com/adfs/ls/idpinitiatedsignon.aspx externally
 i get error message this site cant be reached. adfs.domain.com took too long to respond.

So i need help to be able to reach the ADFS over the internet, can someone help me out with what to do and how ? Thanks thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-03-20*

Hello TuffGong1,

Based on your description when try to access the ADFS URL from externally, the connection failed. As far as I know the problem is more likely related to your ADFS proxy deployment, as your ADFS is working from internally. 

First please double check your firewall, it must allow the traffic for the protocol and port number used by published Proxy server, and you must also configure the firewall to allow HTTPS traffic on port 443 for clients to communicate with ADFS server.

Secondly, please check your DNS configurations, the DNS server configured internally and externally required by the proxy server.  ADFS Proxy requires internal name resolution to resolve the names of AD FS servers. And it also requres an external URL, and
 the public DNS server must be able to reslove each external URL you configured, and not the external URL must reslove to the same IP address as the Proxy server.  For more information above please refer to https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn383644(v=ws.11)?redirectedfrom=MSDN >
 Configure server network settings.    And  https://docs.microsoft.com/en-us/previous-versions/orphan-topics/ws.11/dn383648(v=ws.11)?redirectedfrom=MSDN.

On another hand, if your issue persists, since we are focusing on Office 365 for Business Exchange Online Support, we have limited resource regarinding to ADFS proxy deplyment. However, Microsoft has a dedicated TechNet
 Forum, the dedicated support engineers there are focusing on this kinds of problems, and please post a new thread there to get further professional assistance regarding your problem,thanks.  By the way, if you need any other help from our Office 365 Business
 Exchange Online side, please feel free to let me know, thanks.

Your understanding will be highly appreciated.

Best Regards,

Oliver
