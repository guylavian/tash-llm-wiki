---
title: "Phishing email goes through because of an Exchange Transport Rule that cannot be found"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1293773/phishing-email-goes-through-because-of-an-exchange
question_id: 1293773
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Phishing email goes through because of an Exchange Transport Rule that cannot be found

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1293773/phishing-email-goes-through-because-of-an-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, 

I have got a Phishing email go through to the user's inbox. 

When going to the phishing email Explorer page on Security Center to get more details on why the email was let through, I found the following: 

-  Exchange Transport Rule has been applied to this email. I can see the GUID of the rule. 

I have checked the following so far: 

-  Get-TransportRule, nothing found using the GUID or by listing all the rules. 

-  Safe senders, mail flow rules, or block and allow organizational settings.

-  Anti-Spam, Anti-Phishing and other policies that might have a whitelist. 

We couldn't find any setting that would allow the email to pass through. 

Is there a way to find where and what is this rule by it's GUID only? Or, what policy and configuration allowed this email to pass to the user although it was detected as a phishing email? 

Thank you! 

Regards,

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-30*

Hello @Said A !

DId you run the hidden revealing command ?

Please see my answer and let us know!

I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-05-30*

Did you check the safe sender list of the user who received the message? Not sure which you checked

```
Get-MailboxJunkEmailConfiguration -Identity ""
```
