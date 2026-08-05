---
title: "How to setup remote Exchange user in Outlook 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/132710/how-to-setup-remote-exchange-user-in-outlook-2013
question_id: 132710
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# How to setup remote Exchange user in Outlook 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/132710/how-to-setup-remote-exchange-user-in-outlook-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a remote worker and am trying to connect him to company exchange. He is connected on his comcast ISP; not local LAN.  

I had him add the Outlook profile with the appropriate Mail.mycompany.com server address and email account /password.  

It starts to create the profile but will not Logon. Says cannot find account.   

Is there another way to create the outlook profile to access the company exchange server.  

I checked the account on the LAN and could create the outlook profile on an inhouse system.  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-24*

I successfully setup remote exchange user. I usually  do a manual setup in the local network which did not work remotely. I just entered the email & eMail password. Of course, I had to enter the domain logon when challenged.  

All is good.  

 Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-21*

Hi @John Lenz  ,    

As suggested by Andy, with Autodiscover set up properly and a corresponding DNS record created in your external (public) DNS (see Autodiscover in DNS ), the external user should be able to add his account in Outlook with his email address and password only:    

    

Please have a go at your convenience and feel free to post back if you would like further assistance on this.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
