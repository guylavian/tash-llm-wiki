---
title: "GPO add link in file explorer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/94864/gpo-add-link-in-file-explorer
question_id: 94864
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO add link in file explorer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/94864/gpo-add-link-in-file-explorer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,     

I would deploy some paths to many computer using Group Policy inside Windows 10 File Explorer.    

Servers has got Windows 2016 OS.    

Is it possible to add link to "Quick access" or in "This PC" section using GPO?    

    

I have searched online but I did not find anything.    

Thanks so much    

Federico

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-22*

Yes there is a way using Shortcuts in user Group Policy Preferences.  

Create a user shortcut as such:  

Name: %USERPROFILE%\Links\YourLinkNameHere  

Target Type: File System Object  

Target Path: \blah\blah\blah  

On the Common tab check to run in logged-on user's security context.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-15*

Hi I would link share SMB to "Quick Access" section of laptop users file explorer.    

I have already created a GPO with link in "Network Location" section with success, due to this customer doesn't want use disk mapping    

(here there is my other discussion and solution: https://learn.microsoft.com/en-us/answers/questions/94432/gpo-network-location.html    

Thanks so much!
