---
title: "14 character password limit in GPO for server 2019 1809 LTSC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664332/14-character-password-limit-in-gpo-for-server-2019
question_id: 1664332
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# 14 character password limit in GPO for server 2019 1809 LTSC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664332/14-character-password-limit-in-gpo-for-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I have identified a issue when i try to increase the default length of passwords in a domain to more than 14 characters. The settings in GPO currently allows a mimimum of 14 characters but no more, even though its fully possible to actually set more than 14 characters in a password. That though leaves no possibility to enforce passwords to contain a higher number of characters. Current configuration is Server 2019 (1809), with DF/FL 2016. 

I dont have the option 'Relax minimum password lenght limits' in my GPO, and references to this also mentions build 2004 for the OS. I have found several posts about this topic, but i dont find any of them conclusive for my case.

What i am trying to find out is how i can overcome this problem and enforce paswords with a longer mimimum length requirement. Looking at different posts i can see that some have solved it with a fine grained password policy, but i would like it to be a domain default. 

So what is my best option to be able to enforce longer passwords? I have seen it is possible in server 2022 from some posts, but i would like to get this verified, and if going from server 2019 (1809) --> 2022 is my only option?

Any input is highly appreciated :-)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-09*

Hi brandsen,

Thank you for posting in the Q&A Forums.

This is because the 2019 version of Windows Server does not directly support this feature. The character limit for passwords can only be set indirectly through other settings.

As you said, this can be done by using a fine-grained password policy. This allows you to set different password policies for specific user groups or users, including longer minimum password length requirements. In this way, you can set a shorter default password minimum length in the domain and then force certain users or user groups to use longer passwords through a fine-grained password policy.

As far as I know, there doesn't seem to be any other way to set password character limits in Windows Server 2019. So you either need to set up a Departmental Granularity Password Policy or upgrade your server.

Best regards

Neuvi Jiang
