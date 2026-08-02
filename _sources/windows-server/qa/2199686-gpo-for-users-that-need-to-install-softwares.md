---
title: "GPO for users that need to install softwares"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199686/gpo-for-users-that-need-to-install-softwares
question_id: 2199686
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# GPO for users that need to install softwares

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199686/gpo-for-users-that-need-to-install-softwares (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello everyone,

so i'm working for a company and my boss ask me to make a user in AD that only can install softwares and also don't be able to login to its account and also don't have any other permission to do anything else but can install softwares when UAC ask for domain admin username and password but the problem is i really don't know how to do that, could you help me please ??

i kind of know what should i do but i'm not sure about it, so i made a user and put it on seperate OU and add it to a group and connect that group to administrator group and then i created a GPO and set Deny login locally for that and also i set so restrictions for it but it think this is not right.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-20*

Hello iman mohammadi1  

Thank you for posting in Microsoft Community forum.  

You can create on GPO and link it to domain, edit it as below:

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny log on locally==>add this user account

Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny logon through Remote Desktop Services==>add this user account

It will block the account to sign in any domain machine. But I am not sure in such case, whether this account can be able to install software, please do some tests in your lab, if everything is OK, you can set it in production environment.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-18*

i kind of know what should i do but i'm not sure about it, so i made a user and put it on seperate OU and add it to a group and connect that group to administrator group and then i created a GPO and set Deny login locally for that and also i set so restrictions for it but it think this is not right.

Hi Iman, it's what I would try first.

Did you test the behavior from a client computer?

You can eventually test the Deny login locally on the Local Group Policy to not affect other computer during testing.
