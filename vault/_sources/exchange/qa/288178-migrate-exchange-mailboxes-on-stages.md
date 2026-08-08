---
title: "migrate exchange mailboxes on stages"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/288178/migrate-exchange-mailboxes-on-stages
question_id: 288178
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# migrate exchange mailboxes on stages

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/288178/migrate-exchange-mailboxes-on-stages (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we need to migrate exchange mailboxes from exchange 2016 to 2019 on stages is migrate exchange mailboxes on stages applicable or not?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

Just to confirm, will Exchange 2019 be installed in same domain/organization with 2016?     

And do you want to migrate only the mailboxes or the Exchange server with customize configuration?    

Yes&only mailbox: Use the Exchange Management Shell to create a local move request for individual or multiple mailboxes    

Yes&server: Refer to Ashokm posts.    

No&only mailbox: An easy method is Mailbox imports and exports    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-25*

Hi @ramy ali   ,

Yes, you can install Exchange 2019 and upgrade from Exchange 2016.

1.Make sure to have Exchange 2016 CU11 or later  

2.Install & configure Exchange 2019  

3.Move the DNS, client connectivity, mail flow to Exchange 2019  

4.Migrate the mailboxes in batches

https://www.petenetlive.com/KB/Article/0001472  

https://assistants.microsoft.com/

If the above suggestion helps, please click on "Accept Answer" and upvote it.
