---
title: "Exchange (Multirole + Edge) and certificate from local CA."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/322705/exchange-multirole-edge-and-certificate-from-local
question_id: 322705
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange (Multirole + Edge) and certificate from local CA.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/322705/exchange-multirole-edge-and-certificate-from-local (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,  

I am setting up certificates in really simple on-prem environment  - 2 servers: 1st - multirole (no mailboxes, just for simple relay and O365 management), 2nd - edge role.  

Everything works when I generate certificate directly in Exchange, however when trying to use the certificate from the local CA emails are stuck in the queue on multirole server. The root certificate is added to the trusted root store on the edge server. I do not really have any more ideas on what can be done, what I've done was:  

-  Generate new subscription file on edge  

-  Enabled local CA certificate on multirole server for all the services (IIS,SMTP,POP,IMAP)  

-  Imported build new subscription on multirole server based on the subscription file  

-  Started the synchronization  

-  Rebooted the servers  

Synchronization seems to be ok - got susscesss state, however messages sit in the queue on multirole server with no willingness to go to the edge server, any ideas what step do I miss?  

Cheers,  

J

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-22*

Hi @PawelJarosz-0356 ,    

Please first check the OWA and EAC(ECP), if they are good then we could bypass the cert.     

And what does the multirole means? Mailbox + ClientAccess? What's your Exchange server, is it 2013? And have you added the CA certificate to the trusted root store on Multirole server?    

Sorry I don't know how you sent the emails without mailboxes. Please share more info so we can know this issue better.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
