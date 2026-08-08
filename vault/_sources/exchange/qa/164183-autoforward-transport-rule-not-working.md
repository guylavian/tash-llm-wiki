---
title: "Autoforward Transport rule not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/164183/autoforward-transport-rule-not-working
question_id: 164183
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Autoforward Transport rule not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/164183/autoforward-transport-rule-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there    

I am trying to create a transport rule to auto forward emails with a specific subject line but I cant seem to get it to work and I can't figure out why.     

The settings are     

    

but the email still delivers to the inbox.    

Can anyone suggest why it might be doing this? The person to forward to is an external email address but I have the same problem if it is internal.    

Kind regards    

David

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-17*

Hi @David Ewer       

I think your condition is the issue    

If you are tying to look for a " specific subject line", then you need to use an "include" instead:    

The rule you have is looking for a pattern match in the subject. If you want the rule to look for specific subject text, then use the rule below as an example.    

    

so the final rule would look like:    

    

https://learn.microsoft.com/en-us/exchange/policy-and-compliance/mail-flow-rules/conditions-and-exceptions?view=exchserver-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

HI Andy  

I did as you suggested and removed the recipient and had the same issue of email just delivering.  

Hi Eric  

Im not sure what you mean by regular expressions? Could you elaborate so I can give you relevant information?  

Kind regards  

David

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

I have seen some similar threads that discussing regular expressions in transport rules but not all expressions would work, I'm not an expert in this area, would you share your regular expressions with us so that we can test for you?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
