---
title: "Expired Microsoft exchange server auth certificate in hybrid setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/195453/expired-microsoft-exchange-server-auth-certificate
question_id: 195453
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Expired Microsoft exchange server auth certificate in hybrid setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/195453/expired-microsoft-exchange-server-auth-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,   

I have a customer who's Microsoft Exchange Server Auth Certificate is expired.  

The procedure to renew is pretty straightforward : http://byronwright.blogspot.com/2018/05/expired-microsoft-exchange-server-auth.html   

But my question is : do i need to change something on Office365/Exchange Online ?   

i can read in the comments that you need to export this certificate and upload it to Azure.  

Or is running the hybrid wizard again an option ?   

Please advise ...   

thanks!   

Filip

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

what happens if mail flow is still going onprem and all mailboxes are in the cloud so all mails go through the connector to O365 and this certificate is expired ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

@Filip Soogen      

Here are the detailed information about the function of this certificate:    

    

So, the best practice is to re-run HCW after renewing this certificate.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-11*

I would re-run the Hybrid Wizard. Doing that should take care of things
