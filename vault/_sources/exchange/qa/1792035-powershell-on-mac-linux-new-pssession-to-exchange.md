---
title: "Powershell on Mac/Linux - New-PSSession to Exchange Server -> MI_RESULT_FAILED Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1792035/powershell-on-mac-linux-new-pssession-to-exchange
question_id: 1792035
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Powershell on Mac/Linux - New-PSSession to Exchange Server -> MI_RESULT_FAILED Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1792035/powershell-on-mac-linux-new-pssession-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How can the following error be resolved when trying to connect to an Exchange server via PowerShell from a Mac/Linux machine?  (working fine from windows machine though)

"New-PSSession: [<exchangeserver.domain>] Connecting to remote server <exchangeserve.domain> failed with the following error message: MI_RESULT_FAILED. For more information, see the about_Remote_Troubleshooting Help topic."

Additionally, I am unable to locate the troubleshooting document or any information on the MI_RESULT_FAILED error.  

Could you provide guidance on this issue?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-05*

There were multiple reports of problems using WSMAN on non-Microsoft machines years ago, and support for WSMAN on those machines was dropped (refer to the last post in this thread): https://github.com/PowerShell/PowerShell/issues/5130

There's a replacement for the WSMAN here: https://www.powershellgallery.com/packages/PSWSMan/2.3.1
