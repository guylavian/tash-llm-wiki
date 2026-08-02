---
title: "Migrate from Exchange 2013 to Microsoft 365?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2130081/migrate-from-exchange-2013-to-microsoft-365
question_id: 2130081
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrate from Exchange 2013 to Microsoft 365?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2130081/migrate-from-exchange-2013-to-microsoft-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

currently we have exchange server 2013 with 7.5TB DB size. we have 800 users and I’m considering using CodeTwo to migrate from on-prem Exchange 2013 to O365.

Another way is setup hybrid environment.

CodeTwo seems pretty straightforward, but I can’t find much on whether you can schedule automatic Outlook configuration after cutover… of if I have to do this either manually or with a GPO. 

Also, I believe we need to setup password syncing (Entra ID) after cutover. or it’s not necessary?

Do we need to uninstall current office 2019/2021 (one-time payment)? 

 Can anyone comment on how the post-migration process works with Outlook and CodeTwo? 

or what would you suggest?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-16*

Hi @Amir-G，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you want to migrate from Exchange 2013 to Microsoft 365. You can refer to Microsoft's official hybrid options to complete the migration. You can use the minimal hybrid option in the Exchange Hybrid Configuration Wizard to migrate user mailbox content to Microsoft 365 or Office 365. First, your local domain must be a verified domain in the Microsoft 365 or Office 365 organization. Then start the Exchange Hybrid Configuration Wizard on the Data Migration page of the Microsoft 365 Admin Center. Follow the wizard's prompts and finally update the DNS record. Regarding the issue of migrating from Exchange 2013 to Microsoft 365 using CodeTwo, please understand that we only support Microsoft official products. You can try to contact the relevant technical support for consultation. Thank you for your understanding and cooperation.

Refer to: Use Minimal Hybrid to quickly migrate Exchange mailboxes to Microsoft 365 or Office 365 | Microsoft Learn

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
