---
title: "how to fix exchange error Exchange: An unknown error has occurred. Refer to correlation ID: e0b95974-ccea-499a-80fc-a1a9b0a68fcb.;"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1792287/how-to-fix-exchange-error-exchange-an-unknown-erro
question_id: 1792287
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# how to fix exchange error Exchange: An unknown error has occurred. Refer to correlation ID: e0b95974-ccea-499a-80fc-a1a9b0a68fcb.;

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1792287/how-to-fix-exchange-error-exchange-an-unknown-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

had to recreate a user multiple times and now it cant find a mailbox for a specific user

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-07-04*

Hi, @Lexi Ours

Based on your description, I understand that you encountered an error and need to create a user multiple times, and you can not find the mailbox of a specific user.

Error message "Exchange Online: An unknown error has occurred. Refer to correlation ID" usually occurs due to a configuration setting failure for the user's mailbox.

So, we should find the real cause of the error firstly. You can get the actual error message from PowerShell, either via the Exchange cmdlets or via MSOL:

Get-MsolUser -HasErrorsOnly | fl DisplayName,UserPrincipalName,@{Name="Error";Expression={($_.errors[0].ErrorDetail.objecterrors.errorrecord.ErrorDescription)}}.

More information can be found Troubleshooting Exchange Online Mailbox Provisioning Errors - Faris Malaeb (powershellcenter.com)

In addition, could you provide more information so that I can proceed to the next step of troubleshooting?

1.What is your work environment?

2.Did you encounter an error when creating or deleting a user, or was it anything else?

3.What is the status of the affected users now? Has it been created successfully? Will he be able to log in to his email?

4.Did you do anything else before you encountered the error?

You can still provide additional information that is not included in the above questions.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
