---
title: "Internet access on the Exchange Servers # Need Information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182951/internet-access-on-the-exchange-servers-need-infor
question_id: 182951
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Internet access on the Exchange Servers # Need Information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182951/internet-access-on-the-exchange-servers-need-infor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Internet access on the Exchange Servers # Need Information  

Hello Folks,  

I would like to know whether we need internet on Exchange Servers.  

As far as i understand we need to internet access on the application.  

Please help me with more clarification.  

thanks !!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

Hi Andy,anonymous userDavid   

Thanks for your reply !!  

So if i just allow the URL for CRL check that should be fine or i need full internet access only.  

I am purchasing certificate from digicert can you let me know which specific url will be used by exchange server to do the check?  

Regards,  

Arif

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-06*

anonymous userDavid   

Thank you David !!  

So if we disable the CRL check hope it will not have any issue on the mail flow internal and external.  

Regards,  

Arif

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-03*

anonymous user     

Hi,    

In order to receive messages from the internet, you need to configure the external URLs of the virtual directories on your exchange server.    

And you also need to set the following records in the public DNS.    

    

Here is a document on this topic for your reference: Configure mail flow and client access on Exchange servers    

To send messages to the internet,you need to create a send connector and configure it to send to the internet.    

For more detailed steps,please refer to this document: Create a Send connector in Exchange Server to send mail to the internet    

In addition,for security and to prevent your outbound messages from being recognized as spam,you may also need to set SPF, DKIM or DMARC records for your domain in the public DNS.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
