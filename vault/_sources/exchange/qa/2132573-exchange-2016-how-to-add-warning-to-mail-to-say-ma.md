---
title: "Exchange 2016 : How to add warning to mail to say mail send is outside the organisation on outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2132573/exchange-2016-how-to-add-warning-to-mail-to-say-ma
question_id: 2132573
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2016 : How to add warning to mail to say mail send is outside the organisation on outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2132573/exchange-2016-how-to-add-warning-to-mail-to-say-ma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to configure a warning when sending mail outside to be displayed on outlook.

I ran the command: Set-OrganizationConfig -MailTipsExternalRecipientsTipsEnabled $true on the exchange management shell

However, the warning only appears on webmail.

I run the command Get-ExternalInOutlook to check and proceed with Set-ExternalInOutlook -Enabled $true but I get an error.

[PS] C:\Windows\system32>Get-ExternalInOutlook

Get-ExternalInOutlook : The term 'Get-ExternalInOutlook' is not recognized as the name of a cmdlet, function, script

file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct

and try again.

At line:1 char:1

-  Get-ExternalInOutlook

- 

```
+ CategoryInfo          : ObjectNotFound: (Get-ExternalInOutlook:String) [], CommandNotFoundException

    + FullyQualifiedErrorId : CommandNotFoundException
```

please help me.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-18*

Hi @ Pham Tien Dung，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you configured a warning when sending mail outside the organization, and you found that the warning only appears on webmail. You can check whether the mail tips are enabled in the outlook client:

-  Open Outlook, go to "File" > "Options" > "Mail".

-  In the "Mail Tips" section, check whether the relevant option is enabled.

In addition, you can use the command to check whether it is configured. 

```
Get-OrganizationConfig | Format-List MailTipsExternalRecipientsTipsEnabled
```

For the mail tips settings between organizations, you can refer to the Manage MailTips for organization relationships in Exchange Online | Microsoft Learn.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-17*

Mail tips can take a day to kick in with Outlook with caching so I would give it a day.

Make sure you meet all the requriements:

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/mailtips/mailtips

The other command isnt relevant to this:

https://learn.microsoft.com/en-us/powershell/module/exchange/get-externalinoutlook?view=exchange-ps

-  Get-ExternalInOutlook
