---
title: "Certificate prompt after installing a new Exchange 2013 Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/186857/certificate-prompt-after-installing-a-new-exchange
question_id: 186857
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Certificate prompt after installing a new Exchange 2013 Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/186857/certificate-prompt-after-installing-a-new-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have already Exchange 2013 environment. We are doing a DC to DC migrate. SO we built new Exchange 2013 servers in the new DC.   

-  Public Certificate is imported to the new server.   

-  Get-clientaccessserver , autodiscoverserviceinternaluri published with the load balanced name as well.  

-  Now new servers have not been added to the existing load balancer, no firewall ports opened yet too.  

We are getting outlook certificate prompts stating, name on security cert not matching with name of the site.   

Also, just to test a mailbox email, created a test mailbox on new server database. Trying to send email to self and it is failing stating you don't permission to do the action.   

Exchange installation was all successful. What are we missing?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-12-07*

Hi @GoodResource  ,    

We are getting outlook certificate prompts stating, name on security cert not matching with name of the site.    

At which point did this issue started to occur? As regards to the "autodiscoverserviceinternaluri" mentioned in your description, do you mean you modified it right before the issue began?     

As far as I know, this error usually occurs when the URL that you are trying to access is not listed in either the Subject or the Subject Alternative Name (SAN) of the certificate for the website. Please note the URL displayed at the upper left corner of the prompt, then click View Certificate > Details, check if the URL is included in the SAN list of the certificate:    

     

If the URL doesn't match, you may consider replacing the existing A record  for Autodiscover by using an SRV record that points to a namespace that is already in the SAN of the SSL certificate. For more information, hopefully you can find the article below useful:    

https://support.microsoft.com/en-us/help/2772058/the-name-on-the-security-certificate-is-invalid-or-does-not-match-the    

Then normally we only focus on one issue in one thread, as based on my understanding your second question about the permission error when sending from the test mailbox seems different from the certificate prompt issue we are discussing,  so it would be best if you try to open up a new thread for it. In this way, it will make answer searching in the forum easier and be beneficial to other community members as well. Thanks!     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
