---
title: "GPO to always keep on this device for One Drive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5157613/gpo-to-always-keep-on-this-device-for-one-drive
question_id: 5157613
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 4
qa_tags: []
---
# GPO to always keep on this device for One Drive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5157613/gpo-to-always-keep-on-this-device-for-one-drive (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, 

Quick question regarding One Drive. 

We have an issue where downloading over cellular is causing some problems and I'd like to know if there is a way for us to keep the 

"Always keep on this device" option enabled via a GPO or Registry hack on our PCs

We don't want to do this manually for every user so I'd like to know if this is possible.

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-29*

Dear Audi911KQ,

Good day! Thanks for posting in the community. We are happy to help you.

For your questions, yes, the admin can disable the File On-Demand and make OneDrive download all files to the device by default.

Please try to set the following registry key value to 0:

[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"FilesOnDemandEnabled"="dword:00000000"

For your reference:

Use OneDrive policies to control sync settings

We look forward to your response. Thanks for your cooperation.

Sincerely,

George | Microsoft Community Moderator

***Note: In the event that you're unable to reply to this thread, please ensure that your Email address is verified in the Community Website by clicking on Your Account Name > "My Profile" > "Edit Profile" > Add your Email Address > tick "Receive email notifications" checkbox > click on "Save".***
