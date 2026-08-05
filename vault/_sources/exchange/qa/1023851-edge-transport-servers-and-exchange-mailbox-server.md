---
title: "Edge Transport servers and Exchange mailbox server in maintenance mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1023851/edge-transport-servers-and-exchange-mailbox-server
question_id: 1023851
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Edge Transport servers and Exchange mailbox server in maintenance mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1023851/edge-transport-servers-and-exchange-mailbox-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I we have Exchange 2019 Mailbox servers and an Exchange 2019 edge transport server.    

I have been testing mail flow since running the Exchange Hybrid Configuration Wizard.    

I didn't realise at the time that one of the Exchange mailbox servers was in maintenance mode but I think the edge server was still trying to send email to it.    

Should the Edge server know the Exchange mailbox server is in maintenance mode and not send mail to it?    

If not is there anyway to prevent the edge server attempting to use the Exchange mailbox server in maintenance mode?    

The Edge server has the default  send and receive connectors created after running the HCW and there are no smart hosts in the connector configuration just the Exchange default routing group is used.    

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-27*

@Matthew Ridley       

When put Exchange in maintenance mode, you could use "Redirect-Message" command to redirect mail flow to another Exchange server.     

If there only exist one Exchange server, email will try to deliver to this server and get failed.    

If there only exist one Exchange server and you don't want mail flow between this Exchange server and Edge, you could disable the connector that created by Edge Subscription.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-26*

If the mailbox server is in maint mode, then it should not accept connections and the Edge server should fail then try another mailbox server. Did that not happen?
