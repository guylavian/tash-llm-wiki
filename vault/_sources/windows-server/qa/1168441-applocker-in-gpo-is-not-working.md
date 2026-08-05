---
title: "Applocker in GPO is not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1168441/applocker-in-gpo-is-not-working
question_id: 1168441
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Applocker in GPO is not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1168441/applocker-in-gpo-is-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have configured Applocker in Windows Server 2019 using GPO and linked to a OU called "Workstations" which contains two Windows 10.

What I want to do its denied any app to the User "test", I am trying with the "notepad" but is not working

Also, I tried change the defaults rules to Everyone allows "windows folder" and "Program folders", in that example I change it to "Administrators".

Thanks very much!!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-07*

Hi Philippe Levesque

Thanks so much for your answer, its was easy to find the root of problem.

But if I dont disturb I could make 2 questions more.

My Applocker GPO its working correctly, I have configured the default rules and one deny rule for internet explorer, my question its, there is any problem if I deny the path C:\Windows\System32\cmd.exe but I have the default rule that allows everyone %WINDIR%*

What do u recommend me?

And my last question, how can I customize the applocker message?

Could be possible?

Best Regards!
