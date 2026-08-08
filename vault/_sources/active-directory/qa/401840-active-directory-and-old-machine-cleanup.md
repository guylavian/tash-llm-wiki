---
title: "Active Directory and old machine cleanup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401840/active-directory-and-old-machine-cleanup
question_id: 401840
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory and old machine cleanup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401840/active-directory-and-old-machine-cleanup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

In our Active Directory environment (Server 2012 R2) we have many machines (Windows 7\Windows 8\Windows 10) that no longer exists. Because if this we have no way to properly disjoin them from the domain. Is there a "clean up" process for removing these machines from AD other than just manually deleting them?   

Thank you,  

Steve

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-20*

Hi,  

I am glad to hear that your issue was successfully resolved\I am pleased to know that the information is helpful to you. If there is anything else we can do for you, please feel free to post in the forum.  

Best Regards,  

Vicky

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-19*

Sounds good, thank you!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-19*

Thank you for the response DSPatrick. I guess i could have been a little bit clearer in my initial post.   

Is manually deleting old computer accounts the only proper or clean way to remove them when they no longer exist and are unable to properly disjoin them from the domain? I just want to make sure that there isn't any residual "stuff" left in AD when manually deleting versus disjoining.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-19*

Some options here via PowerShell.  

https://gist.github.com/9to5IT/ce47adee89e9611050d89e2ae210eb74  

--please don't forget to Accept as answer if the reply is helpful--
