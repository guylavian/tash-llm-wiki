---
title: "ADFS Logout problem MSISignOutProtocol preventing logout attempts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2168777/adfs-logout-problem-msisignoutprotocol-preventing
question_id: 2168777
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Logout problem MSISignOutProtocol preventing logout attempts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2168777/adfs-logout-problem-msisignoutprotocol-preventing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is a duplicate of ADFS Logout problem on our testing platform - Microsoft Community, however I can't access the link for where the discussion continued.  

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

## Answers

_No answers on this thread._
