---
title: "Exchange  Server Send Connector"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334583/exchange-server-send-connector
question_id: 334583
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange  Server Send Connector

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334583/exchange-server-send-connector (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,  

We've multiple exchange 2010 and exchange 2016 and running on coexistence mode.  

A send connector with domain * and source server 2010.  

B Send connector with domain gmail.com and source server 2016.  

Mailbox on exchange 2010 will go to exchange 2010 A Send Connector.  

Mailbox on exchange 2016 except gmail.com go to exchange 2010 A Send Connector.  

After disable A Send Connector, Mailbox on exchange 2010 will receive bounce back.#554 5.4.12 SMTP; Hop count exceeded - possible mail loop detected , it can't route to exchange 2016 B Send connector.  

Can we route all the mail traffic to Exchange 2016 B Send connector?  

Thanks.

## Answer (community) — community member

*upvotes: 2 · updated: 2021-03-30*

anonymous userDavid @Anonymous   The environment too complex , let me take more time to study.    

Thanks for your help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-29*

Hi @Mark TT   ,    

I think this is because of a setting error of your send connector or Exchange server.    

Is the domain of your recipient configured as an authoritative accepted domain?     

See this thread: https://social.technet.microsoft.com/Forums/office/en-US/8eb458ae-42e9-4aba-a181-4ffaf627c3e8/last-error-a-local-loop-was-detected-exchange-2010-linux-postfix?forum=exchangesvrsecuremessaging    

About the error: Hop count exceeded - possible mail loop detected, please check this:    

    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-28*

anonymous userDavid It say 2016 server reject the message with 554 5.4.12 SMTP; Hop count exceeded - possible mail loop detected on message id .  

If i put   

A Connector with * domain Exchange 2010  

B Connector with * domain Exchange 2016  

It will use Exchange 2010 first and never go to Exchange 2016.  

Thanks.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-28*

anonymous userDavid Yes, I've try to config B connector with * and disable send connect A, it can't route correctly, so  I'm confuse with the connector.  

Any exchange site configuration need to take care?  

Thanks.
