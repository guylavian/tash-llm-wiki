---
title: "Autodiscover failed after upgrade Exchange 2013 to CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/363021/autodiscover-failed-after-upgrade-exchange-2013-to
question_id: 363021
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Autodiscover failed after upgrade Exchange 2013 to CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/363021/autodiscover-failed-after-upgrade-exchange-2013-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

 After upgrade Exchange Server to 2013, the autodiscover cannot access with error:    

     

     

 But the OWA/ECP are working fine.    

 Plz help me to fix this issue.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-20*

That's Incorrect. Not sure why thats allowing OWA and EAC are working and autodiscover is not with that cert, but that backend cert should be the self-signed Exchange Cert.  

See my blog on how to change it to the correct one:  

https://ehloergosum.com/2020/01/25/renewing-that-pesky-microsoft-exchange-certificate/  

From the article I first linked above. Do the following:  

Start IIS Manager on the Mailbox Server.  

Expand Site, highlight Exchange Back End, and select Bindings from the Actions pane in the right side column.  

Select Type https on Port 444.  

Click Edit and select the Microsoft Exchange certificate.  

From an administrator command prompt, run IISReset. ( Do this off-hours if this a standalone Exchange Server. If you are using a DAG, then move all the databases to other servers and have at it)

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-20*

Hi @NTD8685  ,    

Please also have a check to see if a proper certificate is bound to the Exchange Backend website on port 444:    

-  Start IIS Manager on the Mailbox Server.    

-  Expand Site, highlight Exchange Back End, and select Bindings from the Actions pane in the right side column.    

-  Select Type https on Port 444, click Edit and check if the certificate is bound properly:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-19*

ok, looks normal.    

So EAC/OWA work, just not autodiscovery?     

Nothing in the event logs?    

No errors?    

See if resetting it fixes it in EAC:    

    

If all else fails, consider recreating the AutoD Virtual D:    

https://theitbros.com/recreate-owa-ecp-virtual-directories-exchange-server-2016/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-19*

Hi AndyDavid,    

MSExchangeAutodisoverAppPool is started, I did to recycle it or restart server but no luck.    

    

I still get error.
