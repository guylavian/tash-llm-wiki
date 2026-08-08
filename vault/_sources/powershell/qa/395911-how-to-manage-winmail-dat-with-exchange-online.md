---
title: "How to manage winmail.dat with Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/395911/how-to-manage-winmail-dat-with-exchange-online
question_id: 395911
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to manage winmail.dat with Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/395911/how-to-manage-winmail-dat-with-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have recently migrated one customer of mine to Microsoft 365 Business Standard subscription with Outlook 365 installed on Windows 10 20H2 PCs.  

After about three weeks just one user complains that two contacts receives wimail.dat attachments instead of originally PDF documents sent.  

Microsoft support has been replied with the link below  

https://support.microsoft.com/en-us/topic/how-to-specify-the-email-message-format-that-s-used-for-external-recipients-to-prevent-winmail-dat-attachments-4a379475-1557-9554-ab72-91c5867afc11  

With instructions within the link above (Scenario 1) I should be able to set just for the user experiencing the problem to disable TNEF, but I have not been able to use cmdlet Get-MailContact on the Exchange Online PowerShell environment. I have setup my environment to Connect to Exchange Online using Remote PowerShell and I can connect succesfully and query mailboxes but cmdlet in Get-MailConnect isn't recognized.  

I could set up Scenario 2 but why I cannot use that cmdlet?  

Thank you in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-17*

Hi Ian Xue,  

thanks for your reply and support.  

I'm working with Exchange Online (as part of Microsoft 365 subscription) but the link to install Exchange Management Shell is intended for Exchange Server 2016/2019.  

As I have written, actually I'm able to connect to Exchange Online PowerShell environment through EXO V2 module, but unable to use the Get-MailContact cmdlet.  

Can I use it in Exchange Online?  

If yes, how?  

Thank you in advance.  

Best regards,  

RS

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-17*

Hi,    

Did you run the cmdlets in the Exchange Management Shell? The Get-MailContact cmdlet is part of the module ExchangePowerShell.    

https://learn.microsoft.com/en-us/powershell/module/exchange/get-mailcontact    

To install the Exchange Management Shell you may refer to this link    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/install-management-tools    

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
