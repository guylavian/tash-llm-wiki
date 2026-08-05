---
title: "I am running exchange 2019 on prem, I want to delete spam email received by over 65 thousand users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2284855/i-am-running-exchange-2019-on-prem-i-want-to-delet
question_id: 2284855
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# I am running exchange 2019 on prem, I want to delete spam email received by over 65 thousand users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2284855/i-am-running-exchange-2019-on-prem-i-want-to-delet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

"We're operating on Exchange Server 2019 with over 65,000 mailboxes. I'm looking to remove spam emails received across all users in the environment. However, the Search-Mailbox cmdlet has limitations. Could you please advise on how to retrieve and delete these spam messages?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-17*

Hi @lletsweletse,

Thank you for posting your question in the Microsoft Q&A forum.   

Based on your inquiry, we understand that you have considered to delete junk mail from over 65 thousands user on exchange 2019 on prem. We will be glad to assist you in this part.     

According to your issue,  using ComplianceSearch is likely the most optimal method for handling such a large number of mailboxes. The reason you are  encountering issues with the ComplianceSearch command might be due to the Discovery Management role not being properly assigned, which is required to authorize the use of this command. If possible, please review the role settings on your server to ensure the necessary permissions are in place. 

You can refer to this link: Search for and delete messages in Exchange Server | Microsoft Learn 

Note: The "New-ComlianceSearch" cmdlet recommended that you add the user into the "Compliance Administrator" and "eDiscovery Manager" role groups. That is to say, you can re-confirm if you have added your account (the global admin) into the 2 role groups. 

If possible, could you double check which module you using and syntax within your script? The error indicating that the command is not recognized could be cautioned from them. I understand how frustrating this can be, and I will effort to troubleshoot this for you. 

You can refer via: Exchange cmdlet syntax | Microsoft Learn 

 

Please let me know if you need further assistance, please let us know.   

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".      

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
