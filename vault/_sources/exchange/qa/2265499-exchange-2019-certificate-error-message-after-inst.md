---
title: "Exchange 2019 Certificate Error Message after install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2265499/exchange-2019-certificate-error-message-after-inst
question_id: 2265499
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Certificate Error Message after install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2265499/exchange-2019-certificate-error-message-after-inst (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am the Exchange organization administrator. I installed a new Exchange 2019.  Everything works. I can do everything as expected. I can make a new mailbox database, change policies, migrate users, everything.... except check server certs. When I go to Servers, Certificates and select our old Exchange 2016, it works fine. But pick our new Exchange 2019 and I get error The Exchange certificate operation has failed with an exception on server Exch19. The error message is Access is: A security package specific error occurred.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-14*

Hi Martin, Craig,

Thank you for posting your question in the Microsoft Q&A forum.

Based on the error information, this issue could be related to connection issue between your Exchange and Exchange servers.

-  Please make sure that no network or port limitation between Exchange server and Exchange server, or between Exchange server and DCs.   You can check this article for more details:   Network ports for clients and mail flow in Exchange | Microsoft Learn

-  If you have any third-party scan tool or antivirus software is installed on Exchange servers, please perform Exchange related folder, file and process exclusion according to the following document. This could avoid any file lock or service interference when Exchange function:   Running Windows antivirus software on Exchange servers | Microsoft Learn

-  Please go to "Computer Management> Local Users and Groups>Groups>Administrators" on each of your Exchange servers.   Make sure that "Domain\Exchange Trusted Subsystem" is a member of this group.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
