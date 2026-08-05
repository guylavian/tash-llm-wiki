---
title: "ADFS Logout problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194358/adfs-logout-problem
question_id: 2194358
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS Logout problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194358/adfs-logout-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is a duplicate of ADFS Logout problem on our testing platform - Microsoft Community, however i can't access the link for where the discussion continued  

https://[Domain name]/adfs/ls/?wa=wsignout1.0  

-  When user perform login, the below two cookies appear

-  MSISAuth

-  MSISAuth1

-  When user perform the logout, the below two cookies delete

-  MSISAuth

-  MSISAuth1

The below cookies created

-  MSISSignoutProtocol (10 mins expiry time)

-  When user perform login in same browser again, the below two cookies will appear again

-  MSISAuth

-  MSISAuth1

-  When user perform logout in same browser again, the below two cookies may not be deleted. It depends on if MSISSignoutProtocol has been deleted or expired.

-  MSISAuth

-  MSISAuth1

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-18*

Hello Eleazar Nathan,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to Active Directory Federation Services.   

Since there are no engineers dedicated to Active Directory Federation Services in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and type "Active Directory Federation Services" tag and select any tags related to your productions.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
