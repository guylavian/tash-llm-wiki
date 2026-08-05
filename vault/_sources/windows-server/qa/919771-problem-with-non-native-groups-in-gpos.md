---
title: "Problem with non-native groups in GPOs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/919771/problem-with-non-native-groups-in-gpos
question_id: 919771
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Problem with non-native groups in GPOs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/919771/problem-with-non-native-groups-in-gpos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon everyone.    

the problem noticed happens on our Windows server 2008 R2, when we create GPOs and bind non-native users and groups in the GPO, the configuration is not applied on user terminals.    

We have already updated the group guidelines both on the user terminals and also on the server, with this we realized that the only GPOs that were being applied on the terminals are the ones that use the native group "Authenticated Users" all other groups and users linked in the GPO by Security Filtering do not receive the guidelines of GPOs.    

I wonder if this could be a bug in Windows server 2008 R2 Standard Version 6.1.7601 or a misconfiguration?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-11*

Hi there,    

I guess this is not a Bug. The first place to check is the Scope Tab on the Group Policy Object (GPO). If you are configuring a computer side setting, make sure the GPO is linked to the Organization Unit (OU) that contains the computer.     

Check the Security Filtering settings in your policy. By default, all new GPO objects in the domain have the permissions for the Authenticated Users group enabled. This group includes all users and computers in the domain. It means the policy will be applied to all users and computers within its scope.    

10 Common Problems Causing Group Policy To Not Apply     

https://social.technet.microsoft.com/wiki/contents/articles/22457.10-common-problems-causing-group-policy-to-not-apply.aspx    

Hope this resolves your Query !!    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
