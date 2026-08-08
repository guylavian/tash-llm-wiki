---
title: "Exchange 2016 Forward aCopy os all Incoming mail to 1 Mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/221573/exchange-2016-forward-acopy-os-all-incoming-mail-t
question_id: 221573
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Forward aCopy os all Incoming mail to 1 Mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/221573/exchange-2016-forward-acopy-os-all-incoming-mail-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019  

Customer needs a copy (BCC) of all incoming e-mails sent to 1 mailbox  

Looks like there might be something in Mail Flow / Rules but I differentiate incoming mail  

Is there a way to do this ?  

Thanks,  

Steve

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-07*

You should be able to achieve that by setting up the following mail flow rule:  

-  Apply this rule if > The sender is located > Outside the organization  

-  Do the following> Bcc the message to > select the mailbox  

This way, all external emails should go to the mailbox you specify in the second step.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

I need all external incoming e-mail sent to all mailboxes forwarded to 1 e-mail account

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Hi @Steve Babcock      

According to your requirement above, you want to use transport rule to forward the messages sent to one mailbox by adding user(s) in BCC.    

When you choose 'The recipient is' it will prompt a page which list all users in GAL. This is the expected behavior, we can choose the user from the list or using the search option, then click the add buttoon.    

    

Search:    

    

After setting the rule, it should be like below    

    

Please correct me if I have any misunderstanding about your question.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-06*

Thanks for you reply,  

Ye - I did see that post  

Unfortunately, "the Recipient is " prompt then brings up a list of all the users in the GAL  

Am looking for a copy of everything that I can process without having to maintain the rule. GMail has this in their setup

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-06*

Maybe this is helpful for you:  

https://www.codetwo.com/admins-blog/forward-emails-exchange-server/  

In step 3. it should be "The recipient is..." instead of the "Sender is ..." (not tested by myself)  

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)  

Regards  

 Andreas Baumgarten
