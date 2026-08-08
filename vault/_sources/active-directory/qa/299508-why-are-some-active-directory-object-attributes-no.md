---
title: "Why are some Active Directory object attributes not writeable with PowerShell?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299508/why-are-some-active-directory-object-attributes-no
question_id: 299508
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Why are some Active Directory object attributes not writeable with PowerShell?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299508/why-are-some-active-directory-object-attributes-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I want to use PowerShell to write to the `flags` attribute of a group object in my Active Directory.  

But PowerShell with the ActiveDirectory module won't even retrieve this attribute.  

Why is that?  

Is there any PowerShell module that allows one to write any attribute in AD?  

Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-05*

Hello @fubar  ,    

Thank you for posting here.    

Based on the descroption above, not sure what PS command you are using and what error message you are receiving.    

Here is PS command, I can add flags attribute value to one group (groups1 is the group name, I set the flags value as 2.).    

For example:    

Set the flags value:    

Get-ADGroup -Identity group1 -Properties * | Set-ADGroup -replace @{flags = 2}    

View the flags value:    

(Get-ADGroup -Identity group1 -Properties *)    

    

Set-ADGroup    

https://learn.microsoft.com/en-us/powershell/module/addsadministration/set-adgroup?view=win10-ps    

hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

You can always fall back to using ADSI in PowerShell.  

Not showing the script (or at least the portion of the script) you're having a problem with is never a good idea.  

It may be that the object returned by PowerShell has decoded the flag bits into named properties of that object, but who can tell exactly what you're trying to do?
