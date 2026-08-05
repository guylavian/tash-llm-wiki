---
title: "Migrating exchange to Azure VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/240589/migrating-exchange-to-azure-vm
question_id: 240589
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migrating exchange to Azure VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/240589/migrating-exchange-to-azure-vm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

In the company we are thinking about migrating our on-premise exchange to an Azure VM.  

Could someone let me know if it is required to migrate our on-premise AD to Azure too?  

In the scenario I have our AD in Azure, how do I connect my on-premise network to Azure for authentication ?  

Best regards

## Answer (community) — community member

*upvotes: 3 · updated: 2021-01-22*

Hi @Carlos Cortez   ,    

In order to better solve your issue, I want to confirm with you that you want to migrate On-premises Exchange to Azure VM instead of Exchange online? If I understanding wrong, please correct me in time.    

Did you want to remove the physical domain and Exchange server after migration?    

If you still remain the physical domain, you just need to change DNS record to the new Exchange server which hosted on Azure VM.    

If you will remove the physical domain, you could following the steps:    

-  Create the second Domain controller and install the Exchange server on Azure VM.    

-  Please migrate the physical DC function to Azure VM DC, and migrate the on-premises to new Exchange server on Azure VM.    

-  Change the DSN record.    

In addition, Microsoft officially does not recommend that you install the Exchange server in Azure VM. And before you install the Exchange server on Azure VM, please make sure that you have met all the requirements for Exchange server virtualization: Exchange Server virtualization    

About specific steps on how to connect an on-premises network to a Microsoft Azure virtual network. you could refer to the Microsoft officially article: Connect an on-premises network to a Microsoft Azure virtual network    

There is an article on how to install the Exchange dev/test environments in Azure might be helpful to you: Exchange dev/test environments in Azure    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-12-01*

Hi @Carlos Cortez   ,    

Do you already have the Exchange server running in Azure? I am planning on migrating mine to Azure.    

If so, are you using a backup mechanism to Azure Backup Server?    

I'm very interested in that!    

Kind regards,    

Ronald

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-22*

Hi @Carlos Cortez       

Thank You for posting question!    

In your scenario, you should use Azure AD Connect sync    

    

You can refer Integrate on-premises AD with Azure    

Integrate on-premises AD domains with Azure AD    

Custom installation of Azure Active Directory Connect and Prerequisites for Azure AD Connect    

And Migrating your on-premise exchange server to Azure Office 365    

If a post helps to resolve your issue, please click the `Accept the answer` and Click Answered Vote as helpful . By marking a post as Answered and/or Helpful, you help others find the answer faster.
