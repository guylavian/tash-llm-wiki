---
title: "How do I create on WIndows Server 2019 a GPO that adds notepad to the taskbar on all clients?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/760198/how-do-i-create-on-windows-server-2019-a-gpo-that
question_id: 760198
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How do I create on WIndows Server 2019 a GPO that adds notepad to the taskbar on all clients?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/760198/how-do-i-create-on-windows-server-2019-a-gpo-that (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

How do I create a GPO that adds notepad to the taskbar on all clients?  

Do I create an XML-file like the following one:  

```

  

    

      

      

    

  

```

Or do I export registry entries?  

I tried to resolve this for hours and it is driving me crazy!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-04*

I've already tried this.  

I am able to add normal desktop shortcuts, but no taskbar icons.  

Moreover, on Windows Server 2019 there is no setting called "Start Layout" in the section User Configuration -> Policies -> Administrative Templates -> Start Menu and Taskbar  

Is there a workaround?  

Thank you!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-04*

You can follow along here.  

http://woshub.com/create-desktop-shortcuts-group-policy/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
