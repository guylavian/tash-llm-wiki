---
title: "Set Desktop Wallpaper using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1053594/set-desktop-wallpaper-using-gpo
question_id: 1053594
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Set Desktop Wallpaper using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1053594/set-desktop-wallpaper-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

We have configured a GPO that set the specific desktop wallpaper for our 200 domain users. Our problem here is when they are connected to a different network the background turns black.    

Is there a way to configure the desktop wallpaper to be persistent via GPO even users are in different network?    

Any suggestion will be appreciated.     

Thank you,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-19*

You may want to use a method to copy the wallpaper image file local and then use the registry method to push the policy.    

http://woshub.com/setting-desktop-wallpapers-background-using-group-policy/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
