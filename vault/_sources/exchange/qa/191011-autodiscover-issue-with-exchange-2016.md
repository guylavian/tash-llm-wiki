---
title: "Autodiscover issue with Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/191011/autodiscover-issue-with-exchange-2016
question_id: 191011
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Autodiscover issue with Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/191011/autodiscover-issue-with-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We upgarded our Exchange server to 2016 version 2 years ago. Since version upgraded, we have mailbox autodiscover issue. We have 7 different domains that are using for our Exchange client email address. When we create a new shared mailbox and choose one domain as the mailbox reply address,  then the mailbox that is using other domains as their email address can't access or see the shared mailbox even though they have full access. However, if the reply address changes to another domain's address, then it disappears from previous client's outlook and appears on same domain's mailbox outlook. I also tested on regular mailbox and there is same issue if I assign full access of the mailbox to other domain's mailbox.  

We created a lot of shared mailboxes on Exchange 2010. They are all working until their reply address changed or Outlook upgrades to Outlook 2019 from Outlook 2010.  (this is only we tested outlook version).  After the reply address was changed, the same result as described before happened. In additional, some our clients have upgraded their Outlook to 2019 from 2010 and they lost the shared mailbox from their outlook mailbox list even though no any change of the shared mailbox.   

If you need more information, please let me know.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

@Yuki Sun-MSFT   .    

-  Exchange 2010 still exists and has not been decommissioned. I also guess this might be the issue but can't prove.    

-  The shared mailbox I mentioned as example was created on Exchange 2010 but already migrated to Exchange 2016 database. All other users who are still using Outlook 2010 have no any problem to access that shared mailbox only one user who upgraded her Outlook to 2019 has issue to access it. Anything hasn't change when the issue happened but only her Outlook upgraded.    

-  For all our shared mailbox, we can't access them through OWA. Event though we only have Exchange 2010 and no any issue before.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

@Yuki Sun-MSFT   . Thank you for replying. Yes, for some shared mailboxes, I used the way as you mentioned to add it. It worked when we were in Exchange 2010 but didn't work after upgraded and migrated to Exchange 2016. Moreover, as creator I granted Full Access to my account and I need to access the shared mailboxes in order to give permission to other user or manage those mailboxes. However, I even am unable to access them if their email address is different than mine.    

All 7 domains are in same forest. And again, it worked on Exchange 2010. After upgraded to Exchange 2016, the issue happened. For shared mailbox created in Exchange 2010, I can see the mailboxes in my list but I'm unable to see any new coming emails after migration to Exchange 2016. It disappered from my outlook list when I changed its reply address to my domain address and changed it back.     

There is an example. One our shared mailbox created in Exchange 2010, I grant permission to a distribution group and added it into all users as the way you mentioned before. The users on the distribution group have same domain as the reply address of the shared mailbox. One user upgraded her outlook version to outlook 2019 from 2010 and reported that she is unable to access the shared mailbox anymore. I asked all other users who are still using outlook 2010 and all have no any issue to access the shared mailbox. I didn't see any new emails since it migrated to Exchange 2010. When I changed its reply address to my domain, I can see testing email coming. It disappered from my outlook after I changed its reply address back to original.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-09*

Hi @Zack Tu  ,    

When we create a new shared mailbox and choose one domain as the mailbox reply address, then the mailbox that is using other domains as their email address can't access or see the shared mailbox even though they have full access.    

What if the users in other domains try manually opening the shared mailbox via OWA or adding it in Outlook via File > Account Settings > Account Settings, double click the account, click More Settings > Advanced > Add. Is there any error messages?    

    

Are the 7 domains in different forests? If this is the case, as far as I know, you may need to create linked mailbox with relevant permissions instead.     

Update:    

Hi @Zack Tu  ,    

Thanks for getting back with the additional information. To help better understand your situation, would you please clarify a few more things below?    

-  Has Exchange 2010 been totally decommissioned from your environment?    

-  Was the new shared mailbox mentioned earlier created in Exchange 2016? And do you mean the issue can be reproduced in both Outlook 2010 and Outlook 2019? Or only Outlook 2019 users are affected?    

-  Have you tried checking in OWA and see if the shared mailbox can be accessed as expected?    

Furthermore, I tried to search around on this and found the following article which describes a similar known issue in Exchange 2013:    

Shared mailbox cannot be opened in Outlook in an Exchange Server 2013 environment that has multiple domains    

Although no relevant document was found for Exchange 2016, I'd suggest considering to apply the most recent Exchange Server 2016 CU18 if you are still running an earlier CU, this helps ensure we are not troubleshooting an issue that has already been solved.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
