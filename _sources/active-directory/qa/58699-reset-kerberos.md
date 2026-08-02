---
title: "Reset Kerberos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/58699/reset-kerberos
question_id: 58699
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Reset Kerberos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/58699/reset-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Folks,  

I would like to know if exist some impact when execute reset Kerberos to VPN?  

I need to perform this task, but I don't know how my VPN will behave.  

Any Suggestions? Something that I need to know before and after this task?  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-13*

What do you mean by reset kerberos?  

You can clear cached kerberos ticket by using the following command   

```
klist purge
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-05*

Hi,    

When you said reset Kerberos ,you mean reset the password for the krbtgt account,right?If i misunderstand you ,please let me know.    

I haven't experienced VPN impacted by resetting the kerberos .    

Following infromation for your reference when you reset the krbtgt.    

    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn745899(v=ws.11)?redirectedfrom=MSDN#Anchor_5
