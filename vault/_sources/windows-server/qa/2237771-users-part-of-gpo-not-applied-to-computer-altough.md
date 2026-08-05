---
title: "User's Part of GPO not applied to Computer altough loopback GPO processing is configured"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237771/users-part-of-gpo-not-applied-to-computer-altough
question_id: 2237771
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# User's Part of GPO not applied to Computer altough loopback GPO processing is configured

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237771/users-part-of-gpo-not-applied-to-computer-altough (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Environment is with two forests and one-way trust. 

Goal is to apply some user's settings for users from "domain A" loging in computers in "Domain B".

In "Domain B" GPO with "loopback processing configured" (GPO#1) is applied to "Computers_B" OU as well as GPO with needed user's settings (GPO#2). gpresult/r in run in case (User A logged in Computer B) and result is "The user 'domain\user' does not have RSoP data."  

As a test, user from "Domain B", who is not in same OU as Computer B is logged to Computer B. gpresult/r show expected result, but only "Computer Settings" part of GPO#2 is applied, not "User Settings".

Configuration is very simple, no WMI filter, no Security Filtering, only "Authenticated Users" (default) is used in GPO permissions.   

What is missing?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-24*

Hello Haris Brkanic,

Thank you for posting in Q&A forum. 

Based on the description "In "Domain B" GPO with "loopback processing configured" (GPO#1) is applied to "Computers_B" OU as well as GPO with needed user's settings (GPO#2)", I understand Computers_B OU has computer objects in domain B, you configure loopback processing ("Merge" or "Replace")  (GPO#1) and link (GPO#1) to Computers_B OU, and you configure some needed user's settings (GPO#2) and link (GPO#2) to Computers_B OU.  

Now as a test, you signed one domain user (such as U1) from "Domain B" (different OU as Computer B) on one machine in Computer_B OU (such as PC1), you can check this domain B user settings as below:

1.Logon PC1 using domain B user account U1 (that applies this gpo). 

2.Create a folder named F1 in C drive. 

3.Open CMD (do not run as Administrator). 

4.Type gpresult /h C:\F1\gpo.html and click Enter. 

5.Open gpo.html and check if there are needed user's settings (GPO#2) under "User Details" if it is "Replace" mode.  

Or

Open gpo.html and check if there are needed user's settings (GPO#2) and U1 user settings under "User Details" if it is "Merge" mode.

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/loopback-processing-of-group-policy

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-03-22*

You need to enable Computer Configuration\Administrative Templates\System\Group Policy\Allow cross-forest user policy and roaming user profiles 

For an example, refer to 

https://medium.com/@todddeland/cross-domain-group-policy-objects-ddaa96041a52

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
