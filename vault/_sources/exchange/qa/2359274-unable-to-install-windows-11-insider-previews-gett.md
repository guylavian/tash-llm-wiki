---
title: "Unable to install Windows 11 insider previews. Getting error code 0x80070002"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2359274/unable-to-install-windows-11-insider-previews-gett
question_id: 2359274
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Unable to install Windows 11 insider previews. Getting error code 0x80070002

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2359274/unable-to-install-windows-11-insider-previews-gett (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to upgrade to windows 11. I am getting windows insider previews. The update is getting downloaded but it isn't getting installed. There are two versions of insider previews which are available for installing. The older version i.e. 10.0.22622.601, is getting installed till 88% then i am getting an error, the error code is 0x80070002. And the new version i.e. 10.0.22623.891, is getting installed till 85% and all of sudden the installation process is getting disappeared. The support team performed the basic trouble shooting but the problem still persists. So, they recommended me to contact the insider team. Please help me out with this.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-29*

Suggest you try an in-place repair using the official 22621 ISO

You don't lose apps or personal files by selecting "keep everything" but make a full system backup just in case.

The in-place repair will take you back a few builds, then check for updates and it should work.

Download the image, mount it in Explorer and run setup.exe

https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewiso
