---
title: "[Active Directory] Export group members to CSV with their emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/837598/active-directory-export-group-members-to-csv-with
question_id: 837598
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# [Active Directory] Export group members to CSV with their emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/837598/active-directory-export-group-members-to-csv-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I work in a larger globally managed company. I need to export a list of users from a particular group to a CSV file. I am using a simple command in PowerShell:    

"Get-AdGroupMember -identity "group-name" | select name | Export-csv -path C:\members.csv -NoTypeInformation"     

This is where the problem starts because I need to list people by their first and last name and in PowerShell after a command:    

"Get-AdGroupMember -identity "group-name""    

is called these people are listed by their ID number (below is an example)    

name                         :  00022001    

object class                : user    

SamAccountName    : 00022001    

In Active Directory Users and Computers, the example above (that is, person 0022001) is shown like this:    

0022001    

first name: Jan    

Last name: Kowalski    

Display name: Jan Kowalski    

Discription:    

Office: xxx    

Email: jankowalski@X  .com    

My question is: How to export a list of users from a group including their email addresses or first and last name instead of an ID number?    

I am a beginner so please give me clear guidance on the problem.     

Thank you for your help.    

Regards,    

Jakub.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-05*

@Newbie Jones       

Your answer proved correct, thank you for your quick and complete instruction.    

I wish you the best of luck.
