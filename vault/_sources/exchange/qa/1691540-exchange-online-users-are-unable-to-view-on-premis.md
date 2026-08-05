---
title: "Exchange Online users are unable to view on-premises calendar information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1691540/exchange-online-users-are-unable-to-view-on-premis
question_id: 1691540
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Online users are unable to view on-premises calendar information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1691540/exchange-online-users-are-unable-to-view-on-premis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

I have a problem with Outlook and need help. 

I have moved some users to Exchaneg online. Now when an exchange online user wants to access on premise users calendar, he gets the message above Calendar information cannot be updated. 

This does not happen for all on premise users, but only for some of them. I do not understand this. What can this be?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-06-05*

Have you walked through the troubleshooter?

https://learn.microsoft.com/en-us/exchange/troubleshoot/calendars/troubleshoot-freebusy-issues-in-exchange-hybrid

The error message you describe is not clear to me however. 

https://learn.microsoft.com/en-us/exchange/troubleshoot/calendars/users-can-see-only-basic-freebusy-mailbox-information

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-05*

I get this error message when I execute the command 

I get this error message when I execute the command

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-05*

Hi，@Son2020

Thanks for posting your question in the Microsoft Q&A forum.

Your email system is a hybrid environment, but some Online users cannot view local calendar information.

This problem may be caused by a configuration problem in a hybrid deployment. Here are my suggestions:

Step 1: Run the Get-PartnerApplication cmdlet to check if the Exchange Online-ApplicationAccount is present or missing from on-premises.

In our example, there is no output after we enter the below command.

Step 2: Run the Set-ADServerSettings cmdlet, including -ViewEntireForest parameter, to view and manage all the objects in the forest.

Step 3: Run the Get-User cmdlet to get the Exchange Online-ApplicationAccount user account.

Step 4: Run the Set-PartnerApplication cmdlet to link the Exchange Online-ApplicationAccount on the PartnerApplication.

[PS] C:>Set-PartnerApplication "Exchange Online" -LinkedAccount "exoip.local/users/Exchange Online-ApplicationAccount"

Step 5: Run the Get-PartnerApplication cmdlet to verify that the Exchange Online-ApplicationAccount is set to LinkedAccount.

Step 6: Run the IISReset command to restart IIS (Internet Information Services)

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
