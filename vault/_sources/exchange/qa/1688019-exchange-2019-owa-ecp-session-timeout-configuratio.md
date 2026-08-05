---
title: "Exchange 2019 Owa/ecp session timeout configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688019/exchange-2019-owa-ecp-session-timeout-configuratio
question_id: 1688019
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "MicrosoftVendor"]
---
# Exchange 2019 Owa/ecp session timeout configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688019/exchange-2019-owa-ecp-session-timeout-configuratio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI ,

   May I ask why the Exchange 2019 session timeout configuration does not take effect?

Set-OrganizationConfig -ActivityBasedAuthenticationTimeoutInterval 00:15:00

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 1 · updated: 2026-06-02*

Now these values ​​are in  "HKLM:\SOFTWARE\Microsoft\ExchangeServer\v15\MSExchange OWA"

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-28*

Hi,邓超

Welcome to the Microsoft forum.

Based on your description, maybe you need to set the ActivityBasedAuthenticationTimeoutEnabled or ActivityBasedAuthenticationTimeoutWithSingleSignOnEnabled parameter value to $true.When the two parameter’s value are both $false,it will not work even if you had set the ActivityBasedAuthenticationTimeoutInterval value.

Please try to run the following command:

 Set-OrganizationConfig – ActivityBasedAuthenticationTimeoutEnabled $true.

More information about these parameters,you can refer to Set-OrganizationConfig (ExchangePowerShell) | Microsoft Learn.

If the value is already been set to $true ,but stll does not work,maybe you need to run: 

Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\MSExchange OWA" -Name PrivateTimeout -Value 15 -Type DWORD

Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\MSExchange OWA" -Name PublicTimeout -Value 15 -Type DWORD

More details refer to: Exchange admin tip: Configure timeout settings for Outlook on the Web (techgenix.com)

And it is mentioned that “in January 2024, Microsoft started retiring activity-based authentication timeout for Outlook on the web” in this link : Activity-based authentication timeout for Outlook on the web in Office 365 - Microsoft Support.

I hope this helps.Please feel free to contact me for any updates.
