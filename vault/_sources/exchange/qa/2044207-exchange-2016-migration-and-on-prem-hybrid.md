---
title: "Exchange 2016 Migration and On Prem Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2044207/exchange-2016-migration-and-on-prem-hybrid
question_id: 2044207
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Migration and On Prem Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2044207/exchange-2016-migration-and-on-prem-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an exchange 2016 sitting on server 2016 on site deployed with Server Essentials 2016. Right now I am in the planning phase of moving the Exchange to the cloud.

I would like to deploy a hybrid configuration but don't want to continue using exchange 2016. We also do not have the budget to purchase another server. I would like to keep Exchange Hybrid though using exchange 2019. No mailboxes will remain on site, and once the mailboxes are gone, the cloud spam service will be removed and all mail pointed to Exchange Online.

My current (high level) plan is to install a temp server on a spare workstation with Entra Connect sync the directory. Run the HCW with full Hybrid with Modern Hybrid since we need to maintain email send/receive through the current exchange due to cloud spam smarthost. Even though I have less than 50 mailboxes to move, I would like to space the moves over a few weeks so I can resolve problems, or move things back if there is an issue.

Once everything is confirmed to be moved to the cloud, I would like to remove Exchange 2016 and the exchange 2016 server from AD on prem, wipe the 2016 server, then install Exchange 2019 and Entra connect on server 2019, then remove the temp server.

I am not sure how this will work. I am hoping that removing Entra  and installing it on a new server would be OK. I just need to clean up the old installation before putting in the new installation. Would there be in danger in duplicating accounts with a removal and reinstall?

Exchange on prem is where I am getting stuck on. I am not sure if I can remove the exchange server without removing the exchange objects in AD on prem, then install the exchange 2019 server and put them back in.

I saw some references in my research that once Exchange is removed from on prem, you cannot reconnect it in a hybrid configuration. I can't think this would necessarily be true.

Do I need to have a minimal exchange 2019 install on the temp server? Or can I just wipe exchange from on prem, install the 2019 server, exchange 2019, then configure the hybrid deployment? I see references that there is an Exchange 2022 hybrid exchange download somewhere, would I be better off using this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-09*

As I gone through your query and plan, let me give the best solution for you.

Yes, you can remove the Exchange 2016 server, once you’ve moved all mailboxes to Exchange Online. Also don’t delete Exchange objects from AD. After removal of Exchange 2016, you can install Exchange 2019 for hybrid setup.

You can reinstall Entra Connect on a new server. Verify that it continues syncing your on-prem AD with Microsoft 365.

To maintain hybrid functionality, you’ll need to install Exchange 2019 before removing Exchange 2016.

Right now, there is no update regarding Exchange 2022. You can check this thread for Exchange 2016 to 2019 Migration

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please ask.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-09*

Hi, @BP-7667  

It sounds like you have a well-thought-out plan to move Exchange 2016 to the cloud and set up a hybrid configuration with Exchange 2019.

Here are some considerations:

1.It's a good idea to use a staging server with Entra Connect to sync directories and run the Hybrid Configuration Wizard (HCW), you can opt for Modern Hybrid, which maintains a seamless mail flow without downtime, and can keep emails send/receive. Migrating mailboxes in phases is a wise decision that allows you to address any issues that arise and ensures a smoother transition.

2.Once all mailboxes have been migrated to the cloud, you can remove Exchange 2016 from your on-premises environment. However, be careful when removing Exchange objects from Active Directory (AD). Ensure that all necessary objects are properly cleaned up to avoid any conflicts when installing Exchange 2019.

3.After you remove Exchange 2016, you can continue to install Exchange 2019 on the new server. Rather than simply deleting the Exchange server, follow the proper procedure to deactivate Exchange to ensure that all Exchange-related objects are properly cleaned up from your on-premises Active Directory. Ensure that you follow the correct steps to extend your AD schema to support Exchange 2019 and configure the necessary connectors and certificates.

More information can be found How and when to decommission your on-premises Exchange servers in a hybrid deployment | Microsoft Learn

4.Removing Entra Connect and installing it on a new server should have no problem, it doesn't remove user accounts from Azure AD, just make sure to thoroughly clean up the old installation before setting up a new server to avoid duplicate accounts.

5.Microsoft allows you to run Exchange 2019 servers for hybrid purposes only, without additional licensing, and you can use Exchange 2019 for hybrid setups.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
