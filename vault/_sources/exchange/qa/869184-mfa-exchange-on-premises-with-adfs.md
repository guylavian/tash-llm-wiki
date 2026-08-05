---
title: "MFA Exchange on premises with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/869184/mfa-exchange-on-premises-with-adfs
question_id: 869184
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# MFA Exchange on premises with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/869184/mfa-exchange-on-premises-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Guys,   

In our environment, We have Exchange Server 2016 On premises and we want to add Multi Factor Authentication / OTP on OWA and ECP. Users should receive OTP by SMS on their phone numbers.   

How can it be done by just ADFS without any third-party application or Azure MFA?  

Active Directory 2016 and Exchange 2016 both are on premises.  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-05-31*

Hi @Parisa Razavi       

To my knowledge it is possible to integrate Exchange ECP and OWA with ADFS on-premises.    

Here is a link about how to achieve this: Use AD FS claims-based authentication with Outlook on the web    

While to enable MFA on ADFS, I suppose the only supported method without third-party solutions or Azure is Certificate Authentication.    

Here is a link about this topic: Configure Additional Authentication Methods for AD FS    

Kindly note that: since we are not very familiar with ADFS, if you have further questions or need help with ADFS, please consider adding the tag "adfs" to your question to post in the ADFS forum.    

It would also help you get better support.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
