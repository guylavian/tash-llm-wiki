---
title: "Security issue on Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/254058/security-issue-on-active-directory
question_id: 254058
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Security issue on Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/254058/security-issue-on-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I got surprised when I found that every users (not admin) can get some information about password expiration, group membership, ecc. about every other users.    

I tried ADExplorer or "net user n.surname /domain" command.    

Is it normal? thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-02*

Hello,    

Thank you so much for posting here.    

Here is the discussion about this. We could kindly have a check.    

http://techgenix.com/active-directory-information-exposed-users/    

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Is because the enumeration is allowed. Try by configuring the security policies as shown:    

Network Access: Allow anonymous SID/Name Translation set to Disabled    

Network Access: Do not allow anonymous enumeration of SAM accounts set to Enabled    

Network Access: Do not allow anonymous enumeration of SAM accounts and shares set to Enabled    

Network Access: Let Everyone permissions apply to anonymous users set to Disabled    

Network Access: Restrict anonymous access to named pipes and shares set to Enabled    

Network access: Allows all permissions to apply to anonymous users set to Disabled    

Network Access: Shares that can be accessed anonymously set as Empty:
