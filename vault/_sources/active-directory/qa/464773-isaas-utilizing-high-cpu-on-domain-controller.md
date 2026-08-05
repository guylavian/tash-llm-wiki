---
title: "ISAAS utilizing high CPU on domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/464773/isaas-utilizing-high-cpu-on-domain-controller
question_id: 464773
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ISAAS utilizing high CPU on domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/464773/isaas-utilizing-high-cpu-on-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

ISAAS is consuming high CPU utilization how to troubleshoot,

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-28*

Hi Team

ISASS utilizing high CPU in Domain Controllers

Is this issue resolved?

If yes, Could you please update the solution here.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-12*

Hello @irfan  ,    

I am sorry for the late reply. Thank you for your confirmation.    

Local Security Authority Subsystem Service (LSASS) is a process in Microsoft Windows operating systems that is responsible for enforcing the security policy on the system. It verifies users logging on to a Windows computer or server, handles password changes, and creates access tokens.    

It (ISASS utilizing high CPU) means many users and machines launch authenticate to this DC during one period of time.    

For troubleshooting this issue, you can refer to link below.    

How to troubleshoot high Lsass.exe CPU utilization on Active Directory Domain Controllers    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/troubleshoot-high-lsass.exe-cpu-utilization    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-08*

Yes exactly your right ISAAS is Local Security Authority Subsystem Service  this service in one of my DC consuming high CPU.....
