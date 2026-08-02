---
title: "lockoutstatus.exe mismatch with Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181574/lockoutstatus-exe-mismatch-with-active-directory
question_id: 1181574
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# lockoutstatus.exe mismatch with Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181574/lockoutstatus-exe-mismatch-with-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I did quite a bit of research online about this issue and I can't seem to find a definitive answer so I'm asking over here in case someone might know the answer.

Basically, when I use the Microsoft lockoutstatus.exe tool, an account will say locked out even past the 30 minute lockout timer in our domain.

but when I run a command in PowerShell to check such as:

get-aduser MyUserName -server Server -Properties * | Select-Object LockedOut

it will say the account is not locked - even when I specify the specific server that is saying it's locked in the domain.

Thinking this is a glitch with LockoutStatus I kept testing - but yes in fact the account is still locked out for the end user even though the PowerShell tool will swear up and down it's not locked.

I even scripted something to check the lockout status on every server in our domain and every single server will say unlocked - but lockoutstatus.exe will still say locked - and the user will still be locked.

now this doesn't seem to occur for fresh lockouts - only lockouts where the account should have auto-unlocked due to our domain's policy.

I double checked our policy and it is set to 30 minutes and the account lockout time in both the script and the lockoutstatus.exe tool both say it's been over the 30 minute mark, but lockoutstatus.exe still says locked, while powershell and AD say unlocked.

to make matters even more confusing, the end user is in fact still locked.

I'm just wondering what in fact the lockoutstatus.exe tool is doing to come up with the correct information.

Any ideas are much appreciated :)

thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-17*

Double post
