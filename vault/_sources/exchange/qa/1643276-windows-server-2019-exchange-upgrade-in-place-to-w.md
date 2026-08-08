---
title: "Windows Server 2019 Exchange - Upgrade (In Place) to Windows Server 2022 Standard"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1643276/windows-server-2019-exchange-upgrade-in-place-to-w
question_id: 1643276
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows Server 2019 Exchange - Upgrade (In Place) to Windows Server 2022 Standard

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1643276/windows-server-2019-exchange-upgrade-in-place-to-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I want to upgrade a Windows Server 2019 that runs Exchange 365 to Windows Server 2022 Standard and keep the Exchange as is. Until last year Microsoft was officially supporting Windows Server 2019 for Exchange. (Technically you could run Exchange on Windows Server 2022 but since it is a production environment with many users I would rather be safe)

Any how now that Microsoft supports Server 2022 I thought I would upgrade the Exchange to Server 2022 Standard so every server would have the same OS.

My steps.

-  I have made a backup and a snapshot.

-  I have installed all the updates until now (time of writing). 

-  I have the Windows Server 2022 Standard ISO and an activation key.

-  Since I want to make an In Place Upgrade to also keep everything, I mount the ISO and run as admin the Setup.exe

-  Change how Setup downloads update; choose Not right now

-  Install Windows Server; Accept

-  Choose Windows Server 2022 Standard Evaluation (Desktop Experience)

-  Accept EULA

-  In this step I should expect to either have to enter the Server 2022 Key to activate it and/or continue with Evaluation, either Choose what to Keep files, settings and apps or Nothing. Here I get only the Choose Nothing.

Now I don't want to upgrade and install-setup the Exchange again if it is possible.

My questions are:

a. I can't upgrade and keep the files because the Server 2019 is an Evaluation copy? Do I have to use a key and activate it first?

b. Is it not possible at all? Do I have to setup the Exchange again?

c. Do I miss a step? Just mounting the ISO and running the setup is not enough for an in Place Upgrade?

## Answers

_No answers on this thread._
