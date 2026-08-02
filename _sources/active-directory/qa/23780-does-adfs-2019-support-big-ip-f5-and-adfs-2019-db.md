---
title: "Does adfs 2019 support big ip F5 and ADFS 2019 DB requirments"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/23780/does-adfs-2019-support-big-ip-f5-and-adfs-2019-db
question_id: 23780
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Does adfs 2019 support big ip F5 and ADFS 2019 DB requirments

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/23780/does-adfs-2019-support-big-ip-f5-and-adfs-2019-db (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Does adfs 2019 support big ip F5 also i am unable to find anything on SQL DB requirements on ADFS 2019, Can you also confirm if ADFS supports Netscaler.  

Thanks,  

Anil

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-27*

Thanks all for your response, could you also confirm if when upgrading from ADFS server 2012 to 2019 via Add to farm with a SQL DB, in addition to Service communication certificate do i also have to export token signing, claims provider trust certificate and the encryption certificate over to new 2019 servers .  

Thanks,  

Anil

## Answer (community) — community member

*upvotes: 0 · updated: 2020-04-24*

Hi,  

As both F5 and Citrix (NetScaler) are third party vendors, you should check with them if they support ADFS 2019 or not.  

F5 forum    

https://devcentral.f5.com/s/    

As far as I know ADFS does support NetScaler, but better ask Citrix if they support the latest version of ADFS 2019.  

Citrix forum    

https://discussions.citrix.com/  

Best regards,    

Leon
