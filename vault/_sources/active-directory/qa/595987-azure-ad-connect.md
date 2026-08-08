---
title: "Azure AD Connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/595987/azure-ad-connect
question_id: 595987
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Azure AD Connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/595987/azure-ad-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am unable to disable the Azure AD connect even after deleting the VM.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-19*

@DineoM   ,     

In order to disable the sync for your tenant it is required to update the cloud side configuration for your azure AD instance as well . Just deleting the VM for Azure AD connect may not do the trick . You would need to follow the article Turn off directory synchronization for Microsoft 365 . The following powershell command needs to be run by logging in to Azure AD using Azure AD powershell module. You need to install the powershell module before you could run the following . Please follow the links in the article on how to install the powershell module for azure AD..      

`Set-MsolDirSyncEnabled -EnableDirSync $false`    

Once you have run the above command it can take upto 72 hours for the directory sync configuration to be updated on the Azure AD tenant side. if you have already run this cmdlet and 72 hours have elapsed then we will need to engage support team. Please let as know and we will help you further on this. You can check it by going to https://portal.azure.com > Azure Active Directory  > Azure AD connect > sync status and it would show up on the portal as disabled once the process is complete after running the powershell cmdlet . You can see the following screenshot . I have highlighted the part sync status which should show as disabled once done.     

    

Hope this is helpful .     

Thank you.     

----------------------------------------------------------------------------------------------------------------------------------------------------------    

-  Please don't forget to click on  or upvote  button whenever the information provided helps you. Original posters help the community find answers faster by identifying the correct answer. Here is how    

-  Want a reminder to come back and check responses? Here is how to subscribe to a notification    

-  If you are interested in joining the VM program and help shape the future of Q&A: Here is how you can be part of Q&A Volunteer Moderators
