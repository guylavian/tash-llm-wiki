---
title: "Active Directory Password Policy: Changing the [Mast Change] Attribute"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2116815/active-directory-password-policy-changing-the-mast
question_id: 2116815
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration", "microsoft-security-intune-enrollment", "microsoft-security-intune-other-l1", "microsoft-security-intune-security", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Password Policy: Changing the [Mast Change] Attribute

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2116815/active-directory-password-policy-changing-the-mast (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

Is there an article that specifies how to change the [Mast Change] attribute in Active Directory? I need to modify this parameter for some users to enforce a password change (bypassing the Default Policy - GPO).

Are there any certified articles or scripts available to change this parameter?  

Following this article is not enough for me: https://learn.microsoft.com/en-us/windows/win32/adsi/user-must-change-password-at-next-logon

Thanks in advance,

Alessio.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-03*

Not sure exactly what you are trying to do.. 

If you want different password policies for users, you can use something like fine grained password policies to manage them across your org. 

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/fine-grained-password-policies?tabs=adac

If you just want to set must change at next logon for a list of user you can use a script to modify the accounts you need to.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-03*

Hello,

I'm not 100% sure if I understood you correctly, but for changing the parameter "User must change password password at next logon", you can use Powershell or edit it in the account tab of the user in ADUC console manually. 

For PowerShell, you can use Set-ADAccount command with parameter -ChangePasswordAtLogon

More info about the syntax on:

https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2025-ps

Kind regards,

Domagoj
