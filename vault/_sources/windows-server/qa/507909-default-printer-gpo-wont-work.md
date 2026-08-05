---
title: "Default printer GPO won't work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/507909/default-printer-gpo-wont-work
question_id: 507909
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Default printer GPO won't work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/507909/default-printer-gpo-wont-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to set up a GPO for setting the default printer for all users at logon to our terminal server (Windows Server 2019). The issue is that it won't work even though the GPO itself applies at logon. I've set it up from group policy management console (gpmc.msc) by creating a new GPO (enforcing it) then setting User Configuration/Preferences/Control Panel Settings/Printers and adding a share printer. The printer is selected from active directory since it's properly published and there are no user rights restrictions to it. I've applied the GPO, forced gpupdate and logged out/in with users but it won't set their default printer to the desired one. I've ran gpresult to see if the GPO applies and it does. But the default printer still won't be set to the desired one. Do you have any suggestions?

## Answers

_No answers on this thread._
