---
title: "Exchange 2013 CU update 22 seems to have uninstalled Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297969/exchange-2013-cu-update-22-seems-to-have-uninstall
question_id: 297969
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 CU update 22 seems to have uninstalled Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297969/exchange-2013-cu-update-22-seems-to-have-uninstall (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I was looking to run CU22 for my Exchange Server 2013 (running on Server 2012 R2). The update stalled, and now it seems that Exchange has been uninstalled. WTF? Any ideas? Please help

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-05*

Hi @BJ Henderson   ,    

Do you mean you manually stopped the setup after the update stalled? Or it gave an error then closed itself?    

Also please check the Control Panel, Installed Programs to check if the Exchange was uninstalled or not.    

And you could check your setup logs as AshokM has said, there will be the details of these errors during the installation.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-04*

Hi @BJ Henderson   ,    

Have you made a note of the error message when it failed?    

Try running the setup again with elevated privileges.     

Please share the logs/error message from <system drive>:\ExchangeSetupLogs\ExchangeSetup.log by covering your personal information.
