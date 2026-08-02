---
title: "F5 with MS-ADFSPIP Support Going to WAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/690266/f5-with-ms-adfspip-support-going-to-wap
question_id: 690266
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# F5 with MS-ADFSPIP Support Going to WAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/690266/f5-with-ms-adfspip-support-going-to-wap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  An organization configured designed AD FS to have external traffic flow to a MS-ADFSPIP Aware F5 Proxy than to an AD FS WAP then the internal AD FS farm.    

Is this supported by Microsoft? I could not find anything definitive in the documentation. All the examples in the docs are for F5 to send the traffic directly to the internal AD FS servers.    

Looking at logon audit logs I see that the "X-MS-Forwarded-Client-IP" value has of "<Real Client IP>, <F5 IP>". Will this cause issues with Extranet Smart Lockout thinking that the F5 IP is a client IP as well?    

Traffic Flow:    

[Client] -> [F5 Proxy] -> [WAP] -> [AD FS]    

Thanks! @Pierre Audonnet - MSFT

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-11*

Hello,     

A third party ADFS Proxy can supported as long as it stick the the following specifications:    

https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adfspip/76deccb1-1429-4c80-8349-d38e61da5cbb    

[MS-ADFSPIP]: Active Directory Federation Services and Proxy Integration Protocol    

As F5 is third party vendor, you should check with them (F5 forum) also if this is supported by them.    

Also here some compatibility information:    

Frequently asked questions (FAQ) about AD FS    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-faq#are-third-party-proxies-supported-with-ad-fs    

---------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
