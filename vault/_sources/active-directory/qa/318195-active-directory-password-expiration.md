---
title: "Active Directory - Password Expiration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/318195/active-directory-password-expiration
question_id: 318195
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory - Password Expiration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/318195/active-directory-password-expiration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have a problem with the password expiration of the users, in AD the "Password never expirer" is unchecked but the users do not receive the message to change the password after 60 days. I have executed the command "net user nameoftheuser" and it shows that the password never expire. So I have tried to execute the command "WMIC USERACCOUNT WHERE Name='nameoftheuser' SET PasswordExpires=FALSE but I receive the follow error: Updating proprierties of '\SERVDC01\ROOT\CIMV2:Win32_UserAccount.Domain="domain",Name="nameoftheuser"' ERROR: Description = generic error Can someone help me. Best regards.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-18*

Hi,  

I would suggest you confirm the password policy from the default domain policy and if any FGPP set for the user.  

Run the following command to  

Get default domain policy PowerShell Command: Get-ADDefaultDomainPasswordPolicy  

Get FGPP PowerShell Command: Get-ADFineGrainedPasswordPolicy -Filter "name -like 'admin'"  

If possible, please let me know the result.  

Best Regards,
