---
title: "How to run Get-GPO with alternate credentials"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/146413/how-to-run-get-gpo-with-alternate-credentials
question_id: 146413
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# How to run Get-GPO with alternate credentials

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/146413/how-to-run-get-gpo-with-alternate-credentials (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a need to run Get-GPO from a non-domain machine and return a list of all GPOs on a domain along with their basic information.  The majority of AD related powershell commands can be run with a credential parameter but Get-GPO doesn't offer that option.  

I have been testing with invoke-command, new-pssession, etc but I cannot get it to work.  When I try it as a session, it's essentially trying to setup a local session with credentials that the local machine knows nothing about.  

Help!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Either what andreas said:

```
#Fillout your credentials

$Credential = Get-Credential

#Andreas command above

Invoke-Command -ComputerName . -Credential $Credential -ScriptBlock {Get-GPO -All}
```

Or you could export a list by running the following on the task scheduler under an authorized user (or if local; try system)

```
#checking the directory exists and creating one where necessary
$path = "C:\Temp\"
If(!(test-path $path)){
    New-Item -ItemType Directory -Force -Path $path
}
#Set export Date
$date = get-date -Format yyyyMMdd-HHmmss

#Set exportpath

$gpolist = Get-GPO -All

$gpolist | Export-csv -Path $exportpath -NoClobber -NoTypeInformation -Force
```
