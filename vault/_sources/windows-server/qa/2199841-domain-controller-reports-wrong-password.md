---
title: "Domain controller reports wrong password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199841/domain-controller-reports-wrong-password
question_id: 2199841
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Domain controller reports wrong password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199841/domain-controller-reports-wrong-password (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I have 2 domain controllers named  DC1 and DC2. DC1 is windows 2022 server and DC2 is windows 2016.  DC 2 was working for many years however last time when i perform Cumulative update september then all of a sudden domain admin password is no longer working. on DC1 it is all working fine

So now I cannot login to computer using RDP \

Any reason for that

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-25*

Hello cer113,  

Thank you for posting in Microsoft Community forum.  

1.Based on the description "when i perform Cumulative update September then all of a sudden domain admin password is no longer working. on DC1 it is all working fine", do you mean for the same domain Administrator, you can log into DC1 but you cannot log into DC2?  

2.If so, what error message do you receive when you log into DC2 using domain Administrator?  

3.Based on the description "So now I cannot login to computer using RDP", please check can you log into DC2 using domain Administrator locally?  

4.The last option is you can try to uninstall the KBs within Cumulative update September and then check if it helps.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
