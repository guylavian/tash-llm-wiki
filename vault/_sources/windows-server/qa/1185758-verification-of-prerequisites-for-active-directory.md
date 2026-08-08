---
title: "Verification of prerequisites for Active Directory preparation failed. Unable to perform Exchange schema conflict check for domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185758/verification-of-prerequisites-for-active-directory
question_id: 1185758
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Verification of prerequisites for Active Directory preparation failed. Unable to perform Exchange schema conflict check for domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185758/verification-of-prerequisites-for-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Verification of prerequisites for Active Directory preparation failed. Unable to perform Exchange schema conflict check for domain X.local.

Exception: Access is denied.

Adprep could not retrieve data from the server X.local through Windows Managment Instrumentation (WMI).

[User Action]

Check the log file ADPrep.log in the C:\Windows\debug\adprep\logs\20230302100618-test directory for possible cause of failure.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-09*

Hi Khaled,

This message is likely due to DCOM hardening.  You might see an error message on an existing AD regarding RPC_C_AUTHN_LEVEL_PKT_INTEGRITY.  If this error exists install all Windows updates on the server to you are attempting to promote to DC.  There was a security update to DCOM in 2021/2022 that affected DCOM communications. The updates will make DCOM communications on your new server compatible with your existing DCs.

https://techcommunity.microsoft.com/t5/windows-it-pro-blog/dcom-authentication-hardening-what-you-need-to-know/ba-p/3657154

I hope this helps.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-02*

Hello there,

Make sure that No firewall is blocking the connection.Check if the account you are using is member of local administrators group of the server where you want launch the adprep.

The below thread discusses the same issue and you can try out some troubleshooting steps from this and see if that helps you to sort the Issue.

https://social.technet.microsoft.com/Forums/en-US/8b5c84ed-baa0-46ad-ac12-f6b648023b67/verification-of-prerequisites-for-active-directory-preparation-failed?forum=winserver8gen

https://social.technet.microsoft.com/Forums/windowsserver/en-US/19bb5ef9-2903-4cf8-9d6f-4f7e6f3a6011/verification-of-prerequisites-for-active-directory-preparation-failed?forum=winserverDS

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
