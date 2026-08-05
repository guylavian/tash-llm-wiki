---
title: "Exchange 2013 GALSYNC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297408/exchange-2013-galsync
question_id: 297408
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2013 GALSYNC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297408/exchange-2013-galsync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

we have two exchange installations in two forests , the AD trust is the domain level two way trust.  

i want to hav GAL synced between two exchanges so that i can get free/busy services.  

can anyone please help me?  

Thanks  

Prakash

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

Thank you for the Quick response :) ,    

Regarding GALsync , MIM i need to purchase a license and i'm looking for something free :)     

we have acquired a company and it came with a complex IT setup or i would say misconfigured setup.    

the complication with us is, both forests are using the same UPN suffix ( though Domain Name is different)     

Forest A (domain name qwe.local) , has 5 UPN suffix, one of which (abc.com) which used for user login(user1@jaswant  .com) .    

Forest B (domain name ABC.com) has by default user11@jaswant  .com id.    

now i'm stuck with free/busy not woking, as the trust is domainwide two way (not forest)  but no GALSYNC    

i tried creating mail contact manually to test but it's not working     

i've followed the Technet article for Free/busy configuration.    

https://social.technet.microsoft.com/wiki/contents/articles/28332.steps-to-configure-cross-forest-availability-between-two-exchange-forests-in-exchange-2013.aspx     

i'm sorry, i started my question with GALSYNC and now asking about free/busy....     

Thanks     

Prakash

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-04*

Hi, Prakash.    

You may use (MIM)Microsoft Identity Manager to perform a galsync between the forests.    

It needs a SQL server in your environment.    

About the detailed steps, you may refer to this article:     

Using Microsoft Identity Manager Synchronisation Server's Global Address List Synchronisation feature to create a shared global address book across three Exchange Forests    

(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information. )    

Once the galsync succeeded, you may see mailboxes in another forests synced in the specific OU and appear as "cross-forest mail contact" in EAC>contacts.    

    

About configuring the free/busy(availability) service, there is also a Microsoft document: Configure the Availability service for cross-forest topologies    

And since you are using Exchange 2013, there are some additional steps introduced in this KB: Cross forest free/busy lookup fails when target forest is Exchange Server 2013 or Exchange Server 2016    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
