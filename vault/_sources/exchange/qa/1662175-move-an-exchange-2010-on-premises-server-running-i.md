---
title: "move an exchange 2010 on premises server running in a hybrid configuration to a new server running exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662175/move-an-exchange-2010-on-premises-server-running-i
question_id: 1662175
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# move an exchange 2010 on premises server running in a hybrid configuration to a new server running exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662175/move-an-exchange-2010-on-premises-server-running-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to move off exchange 2010 running in a hybrid configuration with exchange online to a new server running exchange 2016 as i believe this is the only supported configurationI installed exchnage 2016 on a new windows server but it fails

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-28*

Hi Bruce as previously noted the Exchange Deployment Assistant does not allow me to select Exchange 2010. I am slowly working through the docs you have linked to and I did try to reinstall Exchange 2016 but the installer insisted that it was already installed and stopped. I will see if there is a /force like cmd that i can use to over write existing installation.

Thanks for your help to date i will report back once I have finished just for completion

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-21*

Hi Bruce went through all the above, even went to the linked article when it didn't work to see if i had overlooked something. Same error

Thanks Robert

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-14*

Hi Bruce a new admin did not work, trying to give application permissions to folder as some suggest online.

Robert

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-02*

Hi，

Thanks for posting your question in the Microsoft Q&A forum.

Based on your description, I have a few questions to confirm with you.

Did you get errors when installing Exchange 2016? If so, could you please provide the screenshot of the error? If not, please provide more details.

 You could refer to the following document for migration.

Exchange On-Premises Best Practices for Migrations from 2010 to 2016 - Microsoft Community Hub

In order to better upgrade Exchange, we recommend that you use the Exchange Deployment Assistant.
