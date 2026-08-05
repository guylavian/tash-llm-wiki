---
title: "Active Directory password expiration notification."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164544/active-directory-password-expiration-notification
question_id: 1164544
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
---
# Active Directory password expiration notification.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164544/active-directory-password-expiration-notification (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have many users who complain about not getting AD passwords expiration notification pop up on their PC, and they have to call the help desk to get their password resettled.

Further troubleshooting indicates that some of the users don't log off their pc at all.  They just lock their workstation when they leave, and as the result, they don't  see the password expiration notification.

Is there a way to have password expiration notification pops up on user pc everyday for 15 days regardless if they logoff the network or not?

Thanks for your help.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-01-26*

Hi @brichardi  

Did you try to set notification through GPO : 

How to Notify Active Directory Users When Their Password is About to Expire

You can also run one of the scripts mentioned in the links below through a scheduled task in order to send notification by mail regarding the date of password expiration:

Script to Automated Email Reminders when Users Passwords due to Expire.

How to configure password expiration notifications

Please don't forget to mark helpful answer as accepted

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-01-26*

Hi,

It seems User working practice is not correct, you will need to educate users also you can setup email notification via the steps in this article - [https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/how-to-setup-a-password-expiration-notification-email-solution/ba-p/257836

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
