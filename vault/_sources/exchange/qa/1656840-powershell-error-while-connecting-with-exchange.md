---
title: "Powershell error while connecting with exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1656840/powershell-error-while-connecting-with-exchange
question_id: 1656840
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Powershell error while connecting with exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1656840/powershell-error-while-connecting-with-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,

Good day.

Getting error "Content within this application coming from the website listed below is being blocked by Internet Explorer Enhanced Security Configuration."

while running (connect -exchangeonline) command in powershell.

Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-17*

Hi Marcin,

Thanks for your help, tried to go down your path as I am beginner in Powershell, couldn't get it. Maybe screenshot would be helpful.

Thanks again.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-17*

Disable Internet Explorer Enhanced Security Configuration (at least temporarily). There are different ways to accomplish this, for example,

https://learn.microsoft.com/en-us/troubleshoot/developer/browsers/security-privacy/enhanced-security-configuration-faq#how-to-disable-internet-explorer-esc-by-using-a-script

or 

https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Disable-IE-Enhanced-Security-on-Windows-Server.html

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
