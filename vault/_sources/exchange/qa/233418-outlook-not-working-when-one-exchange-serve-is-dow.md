---
title: "Outlook not working when one Exchange serve is down"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/233418/outlook-not-working-when-one-exchange-serve-is-dow
question_id: 233418
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Outlook not working when one Exchange serve is down

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/233418/outlook-not-working-when-one-exchange-serve-is-dow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have 2 Exchange 2019 servers, one of them was recently rebuilt due to a crash.  

Since the rebuild, whenever this node goes down, Outlook doesn't work anymore.  

OWA keeps working.  

The rebuild server can hold the active databases.  

I already checked the "Autodiscover" parameter on the rebuild server and it's set exactly as on the other server.  

What am I missing ?  

Thank you for your help.  

Regards,  

J.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-29*

I ran the auto config check multiple times and I get different results.    

Sometimes, all the urls' are set to LB name.    

But regularly, I see the server's name.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-28*

Hello, Unfortuantely, we haven't come around a new test.    

I noticed the following, when checking the connection status of my Outlook.    

I see 8 connections (I have several shared mailboxes). Some of them are connected with the LB name, some are connected directly to the server.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Have you tried rebooting the LB after rebuilding the server?    

You should follow Andy's suggestion that bypassing the LB and connecting the other Exchange server directly by editing the host file on client's pc, if it's connecting, then you can focus on LB or network issues.    

Do you have mobile devices using Activesync? Does it behave correctly like OWA?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Remove the account:  

Control Panel > Mail > Email Accounts > View/Change > Remove  

Then add it back in.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-17*

and the other node shows its handling the sessions?   

Is the FQDN that Outlook clients the same as OWA? In other words, since OWA is working, Outlook should be using that same pool I would assume.  

If so, then you should take a fiddler trace on one of the Outlook clients when that node is down and see what its trying to connect to.   

Another test is attempting to bypass the F5 and set the hosts file on an Outlook client of the load balanced FQDN to the other servers IP rather then the F5, then disable the one that was rebuilt in the F5 and see if the client can connect.  

Does it fail for all Outlook clients when that one server is down?  

The network team should be able to tell if the clients are using the remaining node once the other goes down as the sessions should increase.
