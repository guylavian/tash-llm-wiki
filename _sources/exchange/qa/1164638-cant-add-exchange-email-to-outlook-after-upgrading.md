---
title: "Can't add exchange email to Outlook after upgrading server license from 2013 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164638/cant-add-exchange-email-to-outlook-after-upgrading
question_id: 1164638
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Can't add exchange email to Outlook after upgrading server license from 2013 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164638/cant-add-exchange-email-to-outlook-after-upgrading (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Yesterday, I updated my server email license from MS Exchange 2013 to 2019. Prior to the update, I exported the files from Outlook (MSO365) and removed the email address from Outlook (per instructions from my hosting co). Now I can't add the email back into Outlook (desktop). Through "advanced" setup [autodiscover does not work], I've tried IMAP and Exchange. I even had a tech from my hosting company spend an hour trying to troubleshoot. No success. Most times it is just prompting me to re-enter the password.

I CAN access the email address through the web so p/w is not the problem, Outlook/my computer is.

I'm thinking it's trying to use data from the old (2013) exchange setup but I'm not finding anything about fixing that/clearing it out, if that is the problem.

For reference:

Windows 10 Pro on PC

MS Office365

Bitlocker enabled

everything up to date

non-MS email address (my bz email)

The email address is no longer showing in

Settings -> Accounts -> Email & accounts

nor in

Settings -> Accounts -> Email & accounts -> Access work or school

But it does show up when I'm adding the email to Outlook and entering the email address itself b/f the p/w. It appears in the dropdown as an option.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-27*

This turned out to be a known scenario, where Exchange 2019 does not install all necessary certificates when it noted an existing Exchange 2013 has a compatible certificate that it can piggy-back off of. When Exchange 2013 was retired from the domain, that certificate was no longer available, and caused "quirky" behavior with Outlook clients.

The following simple commands regenerated the certificate and put it in place:

`New-ExchangeCertificate -KeySize 2048 -PrivateKeyExportable $true -SubjectName "cn=Microsoft Exchange Server Auth Certificate" -FriendlyName "Microsoft Exchange Server Auth Certificate" -DomainName "OURDOMAIN"`

`$Thumbprint = (Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object {$_.Subject -match "Microsoft Exchange Server Auth Certificate"}).Thumbprint;`

`Set-AuthConfig -NewCertificateThumbprint $Thumbprint -NewCertificateEffectiveDate (Get-Date)`

`Set-AuthConfig -PublishCertificate`

`Set-AuthConfig -ClearPreviousCertificate`
