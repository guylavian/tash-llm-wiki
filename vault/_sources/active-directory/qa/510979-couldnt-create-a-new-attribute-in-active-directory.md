---
title: "Couldn't create a new attribute in Active Directory Schema"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/510979/couldnt-create-a-new-attribute-in-active-directory
question_id: 510979
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Couldn't create a new attribute in Active Directory Schema

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/510979/couldnt-create-a-new-attribute-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

Firstly, I created a new attribute it was OK. Then I defunced and removed from classes. Restarted Active Directory Domain Services. Then I wanted recreate the same attribute but I couldn't do it. It tells me:  

An attemp was made to add an object to the directory with a name that is already in use.  

Please help me.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-18*

Hello Emile,   

I will suggest to clean the AD Recycle Bin. Seens that after deleting the attritbute the name will be still "locked" due to remain in the bin and deleted after certain time.  

This can help you:  

From a elevated Powershell prompt, run:   

Get-ADObject -Filter {isDeleted -eq $true -and Name -like "DEL:"} -IncludeDeletedObjects | Remove-ADObject -Confirm:$false  

Best regards,  

Luis P
