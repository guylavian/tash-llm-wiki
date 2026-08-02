---
title: "GPO to Run a specific application in the domin as administrator for a standard user account."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1569432/gpo-to-run-a-specific-application-in-the-domin-as
question_id: 1569432
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO to Run a specific application in the domin as administrator for a standard user account.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1569432/gpo-to-run-a-specific-application-in-the-domin-as (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, We a have an application in our environment. it's been used by few users in different machines. The application needs administrator privileges to run. Temporarily I have created a service account and added it to the local administrator group. As the service account has elevated permission and due to security concerns company has decided to provide administrator access only to the specific application. I have been searching all these times to create GPO and apply it to the specific computers but nothing worked. Unfortunately I did not find one in the internet. I created GPO's and tested but nothing worked. Any suggestion ?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2024-02-22*

Hi @Zaharan Safwan  

Unfortunately, it is not possible via GPO to give local administration rights to an application. 

On the other hand, you can give a user or a domain group administrative rights on a list of machines through Group Policy Preference. For more information please read this article : Using Group Policy Preferences to Manage the Local Administrator Group

Please don't forget to accept helpful answer
