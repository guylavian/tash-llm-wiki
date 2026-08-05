---
title: "Active Directory Domain Join Error - SPN Value Not Unique"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2281112/active-directory-domain-join-error-spn-value-not-u
question_id: 2281112
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Domain Join Error - SPN Value Not Unique

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2281112/active-directory-domain-join-error-spn-value-not-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Assistance is needed to resolve an issue when attempting to join a Windows 11 laptop to an Active Directory domain. The following error message is encountered:    

 ***The following error occurred attempting to join the domain xxxx.com: the operation failed because SPN value provided for additional/modification is not unique forest wide.***The computer account has already been deleted from the Domain Controller. While renaming the hostname of the client machine allows successful domain joining, the goal is to keep the hostname unchanged. Guidance on resolving this issue would be appreciated.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-06*

Hello,

Thank you for posting question on Microsoft Windows forum!

Recommended Solutions：

-  On a Domain Controller, open PowerShell as Administrator 

-  Run the following command to find the conflicting SPN:   

powershell：   *setspn -Q /<your_computer_name>    Replace `<your_computer_name>` with your laptop's hostname

-  If found, delete the conflicting SPN with:

setspn -D HOST/<your_computer_name> <computer_account_name> 

setspn -D HOST/<your_computer_name>.<domain> 

Hope the above information is helpful!
