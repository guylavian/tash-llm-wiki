---
title: "AD one-way trust GPO apply"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/415375/ad-one-way-trust-gpo-apply
question_id: 415375
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD one-way trust GPO apply

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/415375/ad-one-way-trust-gpo-apply (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello:  

I setup a AD one way trust  

A domain trust B domain  

then I use a user in B domain to login a computer in A domain  

But the GPO in B domain not apply,  

It still apply A domain GPO  

If it can apply B domain GPO ??  

I setup user configuration GPO in B domain.  

Thanks.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-31*

Hello @poling chen  ,    

Thank you for posting here.    

Q: If it can apply B domain GPO ??    

A: I set a similar scenario, that is:    

I setup a AD one way trust    

A domain trust B domain    

I setup user configuration GPO in B domain.    

then I use a user in B domain to login a computer in A domain.    

From the gpresult of the user, the user in domain B cannot apply B domain GPO, he/she only applies A domain GPO.    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
