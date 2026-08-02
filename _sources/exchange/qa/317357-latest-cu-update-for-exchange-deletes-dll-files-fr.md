---
title: "Latest CU update for exchange deletes dll files from bin and FIPS directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/317357/latest-cu-update-for-exchange-deletes-dll-files-fr
question_id: 317357
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Latest CU update for exchange deletes dll files from bin and FIPS directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/317357/latest-cu-update-for-exchange-deletes-dll-files-fr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I started to update client exchange servers to the latest CU (one client uses 2013 standard and another 2016 standard). Both updates deleted dll files from the directories. One server i was able to restore them from a backup to get the exchange services running. The other server however i am not so fortunate. no exchange services will start. They were left in a disabled state after the update failed. restoring a backup i took before the update ran into problems because the machine account lost its trust with the domain controller, removing and readding did not solve the problem - additionally, exchange doesn't show as being installed in add remove programs. I have been waiting over a week for Microsoft support to respond, all i get are notices that it is taking longer than normal to assign a tech. We have already been forced to route mail to an cloud provider just to get email but we still need our history. I am posting this as a warning to anyone who is looking to install the latest CU. Make sure you have a very good disaster recovery plan because this affected 2 out of 2 exchange server i tried it on (a 2013 and 2016). Shame on Microsoft for releasing such a horrible patch, there is no way something like this should ever happen with a failed update.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

no, it depends on the MS filtering management service.  If i could have repaired the MS filtering management service it probably would have been ok but at this point i have moved on.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

the problematic one is exchange 2016.  I restored a backup and tested the latest CU with the same result.  i will try the recover option...looks like that will take some time and planning to get a test environment setup.  for the time being it seems that there isn't a known solution to this problem.  I am having a hard time finding anyone else reporting this issue but it happened on two separate client servers in completely different environments so i have to image many other exchange environments are having this problem.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-17*

Hi @TheDude   ,    

Good day!    

As you said you installed the latest CU update for Ex 2013 and 2016, what's the version or do you mean you installed the security update? And I guess it's 2016 that's facing a service disabled issue right?    

Can you set the services to automatic start and then start the services? Will it work?    

For this issue, you could try https://www.reddit.com/r/exchangeserver/comments/lxfd8u/2013_kb5000871_killed_my_server_and_this_just/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
