---
title: "How to check who logged in Active directory, at what time and what they did?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1858368/how-to-check-who-logged-in-active-directory-at-wha
question_id: 1858368
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to check who logged in Active directory, at what time and what they did?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1858368/how-to-check-who-logged-in-active-directory-at-wha (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I was working on Active Directory and 3 users have domain admin privileges. I want to know who signed into the AD server, at what time, what they did (history) and what time they logged off.

I have tried commands and I couldn't get the results i want.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-12*

Hello,

 

Thank you for posting in Q&A forum.

To achieve this purpose, please kindly follow below steps:

1.Open GPO Management Console and navigate to the Default Domain Policy GPO settings: Computer Configuration -> Policies -> Windows Settings -> Security Settings -> Advanced Audit Policy Configuration -> Audit Policies -> Logon/Logoff

2.Enable the following audit policies:

Audit Logon

Audit Other Logon/Logoff Events

3.Record successful and failed logons in both policies and sync the policy in DCs by CMD command:

gpupdate /force.

4.After the configuration you will be able to see records in Event Logs.

 

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
