---
title: "Remove an app from gpo."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1143015/remove-an-app-from-gpo
question_id: 1143015
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Remove an app from gpo.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1143015/remove-an-app-from-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I create a gpo from dc which try to remove a specific app.    

If i run the commands from client ,directly, it works but from gpo to client,no.    

GPO:    

i created as a scheduled task om specific time.    

Action: run the follow command     

wmic product where name="openvpn connect" call uninstall /nointeractive     

which is located  \dc\sysvol\local domain\scripts\Files.    

I believe that i have this error  beacause clients connected with file server, so i dont catche correctly the file server  from these commands, and furthermore     

the start up script doesnt work correctly too by it's own.

## Answers

_No answers on this thread._
