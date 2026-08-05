---
title: "Folder redirection GPO won't apply after installation of Win 10 Pro 21H1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/437292/folder-redirection-gpo-wont-apply-after-installati
question_id: 437292
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Folder redirection GPO won't apply after installation of Win 10 Pro 21H1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/437292/folder-redirection-gpo-wont-apply-after-installati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

I have a customer with a 2012 server; simple environment 1 DC, 10 Windows 10 Pro clients. One machine refused to do an upgrade from W7 to W10, so I did a clean install, which out up ver. 21H1. I have a server GPO for folder redirection, for one security group. This user is in that security group. Worked well when the machine was Win 7, works for every other W10 machine in the building, and for all the users in the security group. It refuses to apply on this one machine. When I run "gpresult /r", only the default domain controller GPO is applied. Gpupdate /force runs with no errors, but it doesn't help anything. On the server side, nothing has changed from the users' perspective.

I have seen posts about setting registry values for hardened UNC paths \*\NETLOGON and \*\SYSVOL, but that doesn't help.

On the server side, nothing has changed with regard to the user account.

I don't get this.

Please help ;-)

Tim

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-16*

Hi,    

Based on my understanding, all the computer GPOs and user GPOs don't apply on this specific computer (after installation of Win 10 Pro 21H1), right?    

If i misunderstand you, please feel free to let me know.    

Did you check the security filter, was the computer has the read permission on the folder redirection GPO?    

Are there any errors when you run  gpresult /h report.html.    

You may try to run the following PowerShell command and check the result:    

Test-ComputerSecureChannel    

Test-ComputerSecureChannel -Server "DCName.domain.com"    

If the command fails, run command:    

Test-ComputerSecureChannel -Repair    

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/test-computersecurechannel?view=powershell-5.1    

And then check if it repairs the issue.    

If not, it will be a quick way to remove and join it to the domain again.    

Best Regards,
