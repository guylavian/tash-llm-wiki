---
title: "Update user shell folders registry keys with GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/703269/update-user-shell-folders-registry-keys-with-gpo
question_id: 703269
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Update user shell folders registry keys with GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/703269/update-user-shell-folders-registry-keys-with-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello people,  

My goal is to change the location of two user Shell Folders located under %USERPROFILE%\AppData with a GPO.  

The keys in question are named Local AppData and AppData, which are located under HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders.  

I defined a create-GPO and a replace-GPO by selecting the specific registry keys inside the GPO management console, which is pretty straightforward.  

Desired values for those keys would be the following.  

Local AppData  

%USERPROFILE%\Documents\AppData\Local  

AppData  

%USERPROFILE%\Documents\AppData\Roaming  

After user login, the values are not being updated nor do the folders redirect to the desired location.  

Server OS: Windows Server 2016 Standard  

Client OS: Windows 10  

I appreciate any efforts.  

Thanks in advance.  

Have a nice one,  

Andreas

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-27*

Redirection of %USERPROFILE%\AppData\Local is not possible that way.  

Thanks for your input.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-27*

Hello @Andreas - IT Operator       

Why not to apply the next policy:    

user configuration>Windows settings>folder Redirection>Documents     

(You can specify other folders like downloads and music here too (same idea)    

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--
