---
title: "Hi I am looking for best steps for Exchange online tenant to tenant migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1134128/hi-i-am-looking-for-best-steps-for-exchange-online
question_id: 1134128
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Hi I am looking for best steps for Exchange online tenant to tenant migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1134128/hi-i-am-looking-for-best-steps-for-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we have acquired a company who's on O365. We are in Hybrid O365 exchange state where identities are syncing from on prem to Azure. the partner organization domain is subset of a parent company. So from parent company tenant we are going to migrate the sub domain of users. We want to do it as a phased wise. What could be the best approach and steps,     

-  should we verify the partner domain to source tenant first? What will happen to the mailboxes on source tenant?    

-  Should we switch MX to our domain as first step.     

-  Which one should be mailbox users for which domain should be part of accepted domain and verified. at present partner company has it as accepted domain.     

Please suggest.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-20*

Hi @GoodResource   ,    

Issue Symptom:    

Migrate mailboxes from a hybrid environment to a new tenant in a subdomain.    

Domains in the source tenant also need to be migrated to the new tenant so that the migrated mailboxes continue to use.    

The Solution:    

-  keep the mailboxes in source with primary smtp as is: ******@sourcedomain.com (Sourcedomain.com still registered in source O365 tenant, MX still points to source organization).    

-  Please note: Sourcedomain.com has to be switched too in target tenant.    

-  In target create remote mailboxes with same email address but with target domain. So it will be ******@targetdomain.com. Targetdomain.com is registered to target O365 tenant.    

-  once the mailbox content is migrated. Post migration no recipient type should change. A forwarder will be set on every mailboxes on source tenant to forward emails to targetdomain.com.    

-  Once cutover date is determined, detach the sourcedomain.com from source tenant and attach it to target tenant.    

-  Remove directory sync of those objects on source tenant.    

-  Now that sourcedomain.com is registered in target tenant, stamp the primary smtp accordingly. So now ******@targetdomain.com will be switched to ******@sourcedomain.com.    

-  change the mx record to target domain DNS.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-20*

Hi @GoodResource   ,    

In my opinion, if it's a batch migration, the remaining mailboxes that haven't migrated still need to be used, so the first step in migrating mailboxes isn't to switch MX records.    

You could refer to the detailed steps in this link to migrate mailboxes across tenants:    

Cross-tenant mailbox migration - Microsoft 365 Enterprise | Microsoft Learn    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
