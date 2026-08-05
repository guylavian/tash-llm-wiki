---
title: "[Migrated from MSDN Exchange Dev] throthling anyonymous messeage sending smtp error 4.7.500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/152099/migrated-from-msdn-exchange-dev-throthling-anyonym
question_id: 152099
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] throthling anyonymous messeage sending smtp error 4.7.500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/152099/migrated-from-msdn-exchange-dev-throthling-anyonym (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/96ec8dab-c59e-4282-82e2-b14d4e6cd190/throthling-anyonymous-messeage-sending-smtp-error-47500?forum=exchangesvrdevelopment   

Dear all!  

We have an application server which is sending out e-mails to our domain only, no external messeages (at least 90% of the messeages sent internal, but i am not 100% sure). We do not use authenication. We have set up a connector sender: our e-mail server recipient: office365. I am unsure if this settings is left from migration or not. We are checking the IP address of the sender. The sending works, but the application server is working like this:  

1 . start sending out e-mails daily at a time like 13:00 for the nex day's work details  

The e-mail count is less then 50, so this is not a very big ammount. The e-mails are sent with 5 sec delay. Still after 14-20 e-mails the application server getting SMTP error 4.7.500 Access deniend.  

How could i avoid this?  

thanks  

peter  

edit: i supposed to post this in exchange online topic, i do not know how it ended up here

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-12*

@petersonal       

Does this issue occurs every day that the emails are delayed after 14-20 e-mails?    

Are there any messages sent from the application without knowing?    

According to the document, reasonable limits are imposed for SMTP relay: Compare the options - Limitations. All outbound messages from Microsoft 365 datacenter servers that's determined to be spam or that exceeds the sending limits of the service or outbound spam policies are sent through the high-risk delivery pool. You can check this for more details: High-risk delivery pool.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-05*

Did the connector work before? Were messages from your application ever sent successfully?    

Please check these steps again to make sure everything is configured well: Option 3: Configure a connector to send mail using Microsoft 365 or Office 365 SMTP relay.     

You can check the message tracing for messages from the application, to see is more error information is provided. You can post the screenshot here, and don't forget to cover your personal information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
