---
title: "Exchange Server migration problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2286453/exchange-server-migration-problem
question_id: 2286453
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server migration problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2286453/exchange-server-migration-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are approaching for Exchange server migration from EX2016 to EX2019. Both environment applied for the latest CU. One question is when user are migrate from EX2016, once migration complete, their desktop will continuously prompt the login windows.

EX2016 user

Stay at Ex2016: no login windows prompt out

Migrate to Ex2019: continuously prompt out login window

New create user on Ex2019: no login windows prompt out.

I have also follow all the virtual directory settings from Ex2016, and have correctly place the cert .

Any suggestions?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-24*

Hi Hin, 

Thanks for you reply. 

One update: I have test again.. The account created on Ex2019 are still face the same issue.

And we use the same URL for the both ex2016  and ex2019 env. 

Here's the authentication  for both Ex2016 and Ex2019 for your further investigation.

Ex2016

Name                            : Autodiscover (Default Web Site)

InternalAuthenticationMethods   : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}

ExternalAuthenticationMethods   : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}

Ex2019

Name                            : Autodiscover (Default Web Site)

InternalAuthenticationMethods   : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}

ExternalAuthenticationMethods   : {Basic, Ntlm, WindowsIntegrated, WSSecurity, OAuth}

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-24*

Dear @Tang, Ken 

Thank you for posting your question in the Microsoft Q&A forum.   

According to your issue, I understand you're experiencing a frustrating situation with continuous login prompts for users after their mailboxes are moved from Exchange 2016 to Exchange 2019. Here are a few steps you can try to resolve this: 

-  Check Autodiscover Settings: Ensure that the Autodiscover service is correctly configured and that the Service Connection Point (SCP) is pointing to the correct URL. You can verify this by running the Test Email AutoConfiguration tool in Outlook (hold down the CTRL key and right-click the Outlook icon). 

-  Check Authentication Settings: Ensure that the authentication settings on your Exchange server are correctly configured. Sometimes, mismatched authentication settings can cause repeated credential prompts. 

-  DNS Configuration: Verify that your DNS settings are correctly configured and that the Autodiscover DNS records are pointing to the correct IP address of your Exchange server. 

To troubleshoot this more effectively, could you please provide details on the authentication methods enabled for the AutoDiscover Virtual Directory on both your Exchange 2016 and Exchange 2019 servers?

If you need further assistance, please let us know.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
