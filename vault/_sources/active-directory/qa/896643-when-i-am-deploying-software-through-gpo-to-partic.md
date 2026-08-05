---
title: "When i am deploying software through GPO to particular group or user it is deploying to every user can anyone solve this for me?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/896643/when-i-am-deploying-software-through-gpo-to-partic
question_id: 896643
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# When i am deploying software through GPO to particular group or user it is deploying to every user can anyone solve this for me?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/896643/when-i-am-deploying-software-through-gpo-to-partic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So when i am deploying mozila msi file to a specific security group of three people on first log on its deployment automatically to the other user in other ou's and groups

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-21*

Hi GaganpreetSingh-6107,    

Please check the ‘OU’ that you have applied the GPO to whether it has only computer systems or does it include users also. If it includes users also, then this group policy will be applied to the systems on which these users will be logged on to. This is the publishing method of installing a package in AD environment wherein the software package will be installed in those systems where the users in selected OUs have logged on to. This software package will be available in ‘Add or Remove Programs’ section of the control panel.    

Similarly, if the OU has computer systems only, and you have applied the GPO as specified in the question, then no computer system or user will be able to install that software package. And if the following GPO setting has been applied with users as well as computer systems in the OU, then when the user logs on to the computer, the software package gets installed and when the computer system starts, the software package gets installed. This is known as assigning method of software package deployment in AD environment.    

Group policy Management --> Select the GPO --> Edit --> Computer Configuration --> Software settings --> Software Installation --> New --> Package --> Type the UNC path of the share where the software package is placed --> Open --> Ok --> Save ’    

Please find the below link for more information on the above topics: -    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software    

-------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
