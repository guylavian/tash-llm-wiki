---
title: "PowerShell to Find Where Your Active Directory Groups Are Used On servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/634272/powershell-to-find-where-your-active-directory-gro
question_id: 634272
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# PowerShell to Find Where Your Active Directory Groups Are Used On servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/634272/powershell-to-find-where-your-active-directory-gro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm looking for a script to scan all the serves in an OU for a specific AD group.  We get requests like this from time to time and we really have no way/tool to pull this information.  

I'm NOT looking for anything user related - I have scripts to get users in groups, add uses to groups, remove users from groups, etc.  Strictly looking to obtain a list of servers where a specific AD group is in the local admin group - again can either use a list or a (probably easier) scan an OU.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-03*

Thanks Rich.  I have a question though - I follow the script up until the "foreach-object" - but then lose it.  What does that part of the script do exactly?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-19*

Something like this should do it:  

```
$Accounts = 'ralph','george','melvin'
$computers = Get-ADComputer -Filter * -SearchBase YourOuDistinguishedNameGoesHere 
Get-WmiObject win32_groupuser -ComputerName $computers |
    Where-Object {$_.groupcomponent -like '*"Administrators"'} |
        ForEach-Object{
            $_.partcomponent -match ".+Domain\=(.+)\,Name\=(.+)$" > $nul
            $Name   = $matches[2].Trim('"')
            if ($Accounts -contains $Name){
                [PSCustomObject]@{
                    ComputerName = $_.PSComputerName
                    Domain = $matches[1].Trim('"')
                    Name   = $Name
                }
            }
        }
```
