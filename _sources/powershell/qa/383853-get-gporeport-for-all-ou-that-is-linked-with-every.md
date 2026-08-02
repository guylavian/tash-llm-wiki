---
title: "Get-gporeport for all ou that is linked with every gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/383853/get-gporeport-for-all-ou-that-is-linked-with-every
question_id: 383853
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Get-gporeport for all ou that is linked with every gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/383853/get-gporeport-for-all-ou-that-is-linked-with-every (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys, im stuck with this.  

I'm creating a folder for each of my OU then getting the GPO report for each gpo that is linked in my ou then storing that reports to my folder that i created that is named  

each ou.  

$OUs = Get-ADOrganizationalUnit -Filter 'Name -like "*"'  

$directory = foreach($ou in $ous){ new-item -name $ou.name -ItemType directory -path C:\temp\test}  

$like = foreach($ou in $ous){Get-GPInheritance -Target $ou}  

foreach($pol in $like){if ($pol.path -eq $ou.Name){foreach($link in $pol.GpoLinks){Get-GPOReport -Name $link -ReportType html -path }}}

## Answers

_No answers on this thread._
