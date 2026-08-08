---
title: "Why does a weird news thing pop up when i hover on the \"type here to search\" area on my Windows 10?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4136549/why-does-a-weird-news-thing-pop-up-when-i-hover-on
question_id: 4136549
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Why does a weird news thing pop up when i hover on the "type here to search" area on my Windows 10?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4136549/why-does-a-weird-news-thing-pop-up-when-i-hover-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When i want to search for an app on my computer, this weird news thing appears on my screen. I tried to turn off news and intrests, but that only gets rid of the weather thing on the taskbar that also shows stocks stuff sometimes. I went in settings and was able to get the actually hover over to make it pop up and it dissapeared, but it still shows this on my screen even though its not there. This only appeared like a week or 2 ago but now its getting annoying as i cant search up anything in the search bar. PLEASE HELP![](https://learn-attachment.microsoft.com/api/attachments/004277d3-d53d-4430-a390-81d7a00cee58?platform=QnA

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-06-06*

Hi, and thanks for reaching out. My name is Bernard a Windows fan like you. I'll be happy to help you out today.

I understand the issue you have, there is nothing to worry I am here to help, may I know how did you turn off news and interest? because once you turn it off it should remove all icons and text of news and interest, try to:

Right-click on the blank space in the taskbar> Select News and Interests > Click Turn Off

Note: If that is the step you have done and still the same kindly do the steps below:

Open Registry by pressing Windows key + R then type in: 

regedit

Then hit OK

Navigate: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Feeds

On the right side look for "ShellFeedsTaskbarViewMode"

Double-click it and set the value data to 2

Then hit OK and restart the PC.

You may also refer to this link: https://www.prajwaldesai.com/disable-news-and-i....

Note: This is a non-Microsoft website. The page appears to be providing accurate, safe information. Watch out for ads on the site that may advertise products frequently classified as a PUP (Potentially Unwanted Products). Thoroughly research any product advertised on the site before you decide to download and install it.

Let me know how it goes and I hope that helps.

Bernard
