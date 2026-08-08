---
title: "Using Transport Rules to add a disclaimer to only the first email in a conversation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/159453/using-transport-rules-to-add-a-disclaimer-to-only
question_id: 159453
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Using Transport Rules to add a disclaimer to only the first email in a conversation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/159453/using-transport-rules-to-add-a-disclaimer-to-only (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created a Transport Rule to add an HTML text disclaimer to the end of an outbound email but how do I stop it from adding it to ever email in an ongoing conversation between two people?  

I have tried using the exception "If the subject or body matches these text patterns" and copied part or all of the disclaimer but that has not worked.  

Could I add another rule to add a header and then set an exception in my disclaimer rule to check for the header?  

Can anybody suggest a solution to this problem?  

Many thanks  

David

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Most strange!    

I changed the text in the Exception to use the same text @Joyce Shen - MSFT   used and it resolved the problem. Thank you all for your assistance, very much appreciated.    

Kind regards    

David

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

Hi @David Ewer   ,    

I copied your disclaimer in my environment, and set the rule like below which can work properly.    

    

And the disclaimer only add once    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

Thanks for all your replies. I am attaching several screenshots which show the entire rule. I am also attaching a screenshot of the HTML code for the disclaimer. I have altered the company name but the rest is the same.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

Hi @David Ewer  ,     

I tried in my environment, it seems work properly.    

Not adding exception, get multiple disclaimer times:    

    

After adding exception:    

    

Get only once:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
