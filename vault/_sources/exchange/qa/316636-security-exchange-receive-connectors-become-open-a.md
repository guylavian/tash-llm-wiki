---
title: "Security! Exchange receive connectors become open after CU15 to CU19 and march 2021 security patch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316636/security-exchange-receive-connectors-become-open-a
question_id: 316636
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Security! Exchange receive connectors become open after CU15 to CU19 and march 2021 security patch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316636/security-exchange-receive-connectors-become-open-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

Our mail infrastructure is composed of two Exchange servers version 2016 in a DAG, that were in CU15.  

Where receive connectors did not accept anonymous connections without configuring per ip address permissions!  

Today, we discovered that after upgrading to CU19 and installing security patch KB5000871 , using any simple tool or any script, would permit sending emails using any identity from our network... which would cause a huge security breach if discovered..!  

I would like to know, if anyone had this problem? and if resolved, what was the solution for it?  

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

thank you for your help,    

for the receive connectors, i believe that those ip addresses are set...    

for the available connectors we have:    

    

for the configuration of the internal smtp relay ## :    

security:    

    

scope:    

    

for the default #SERVER security:    

    

and the scope:    

    

as you said, @Anonymous   for the send connectors:    

    

and the last one, has only the antispam device to send emails to internet.    

And i believe, that nothing was changed lately...    

Could anyone please, tell what should be done?    

Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-17*

Hi @LotfiBOUCHERIT-4930 ,

Have you tried to uncheck the Anonymous users of the Internal SMTP Relay connector?  

I would think it's expected if you allow the anonymous relay on that receive connector and the Senders & Recipients are internal guys.  

Also please check the permission of the other receive connectors.

As Andy said, you could try to change the scoping of IP addresses to allow specific users to access.

I'd like to know, too, if possible, for a received email, can we know which connector was used to deliver it?

Well if you have created a send connector, you can judge by the scoping Domain and Cost. But it could also use the default Send Connector to do that if you didn't create one.

Regards,  

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-16*

Thank you,  

The settings seem to be fine correct but it's not working... i don't know, if it's could be caused by the last upgrade and patch management?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-16*

Yes, you can tell that by enabling SMTP protocol logging on the Receive Connectors.     

The one used will be listed for that connection in the protocol logs    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/configure-protocol-logging?view=exchserver-2019
