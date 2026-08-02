---
title: "Cannot access OWA after re-create the Exchange virtual directories"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/185149/cannot-access-owa-after-re-create-the-exchange-vir
question_id: 185149
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Cannot access OWA after re-create the Exchange virtual directories

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/185149/cannot-access-owa-after-re-create-the-exchange-vir (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi together,  

I recreated Exchange 2013 virtual directories. After this change the cannot login on OWA externally. The users get login window. But if they use the correct credentials, they get the following error:  

Login Failed - Please make sure that your Username and Password are correct, and then try again.  

The users can access without any problem internally on OWA.  

There is a KEMP load balancer between external users and Exchange Server. But we made no changes on Load Balancer.  

External and internal URLs are correct. I found following article from Microsoft which describes the exactly this issue and offers a workaround.   

[https://support.microsoft.com/en-us/help/2778897/cannot-access-outlook-on-the-web-or-the-eac-after-you-re-create-the-ow][1]  

I applied but did not help.  

I need help very urgently.  

Best regards  

Birdal

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Hi @Birdal  ,    

I'm here to narrow down your problem:    

-  Could you login on OWA externally with a new user?    

-  Did you encounter the same issue when using these mailboxes to access ECP externally?    

-  Is there any error in the test result if you use Microsoft Remote Connectivity Analyzer to test the external connectivity?    

Could you please provide your current configurations of the OWA virtual directory? I will copy/paste your settings in my server and see if i encountered the same issue (You could run the following command to see that, please don't forget to replace your server FQDN and URLs with false ones):    

```
Get-OwaVirtualDirectory | fl Identity, *Url*, *Auth*
```

Based on the error "Login Failed - Please make sure that your Username and Password are correct, and then try again.", I guess that the browser cache could be one reason to cause the incorrect credential issue, please try to clear the browser cache or access OWA in incognito mode, and see if there is any difference.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
