---
title: "Implement Active Directory in Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2045354/implement-active-directory-in-azure
question_id: 2045354
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Implement Active Directory in Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2045354/implement-active-directory-in-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are planning to migrate on-prem Active directory to Azure. as a finance company we have 527 active users and 2500+ inactive users. due to a government policy we can't remove profiles of resigned users. we have no clear plan if we want to go to azure what kind of license plans should we have and how can we manage servers and all other BYOD via Azure and enable SSO.  is anyone seems this is possible to do with azure? if so please explain me and guide me

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-10*

@Madushan Gunarathne, Thanks for posting in Q&A. In General, Intune can be used to manage device like deploy device configuration policy (similar like what GPO do).), conditional access policy, compliance or manage app and etc.

https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune

For example, you can use Group Policy analytics tool to analyze the GPO policies and find if the same setting existing in Intune existing.

https://techcommunity.microsoft.com/t5/intune-customer-success/the-group-policy-analytics-tool-is-now-generally-available/ba-p/3913190

Currently, Intune can support to manage windows client, like windows 10/11. other OS like iOS, Android and etc. But windows server is not supported yet. You can see more details in the following link:

https://learn.microsoft.com/en-us/mem/intune/fundamentals/supported-devices-browsers

To manage the devices, we need to choose one suitable method to enroll the device into Intune.

https://learn.microsoft.com/en-us/mem/intune/fundamentals/deployment-guide-enrollment-windows

Meanwhile, for the enrolled user, Microsoft Intune license is needed to be assigned.

https://learn.microsoft.com/en-us/mem/intune/fundamentals/licenses

Here are the suggestions from Intune side. If you have any more questions with Intune, you can let me know. And here is an article I find about migration you can refer:

https://learn.microsoft.com/en-us/entra/architecture/road-to-the-cloud-migrate

For other questions with Microsoft Entra ID, I notice the tag is added. You can wait to see if the related support can be involved to help answer.

Hope the above information can help.

If the answer is helpful, please click "Accept Answer"  and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-09*

If you are not clear on the requirements and design elements then I will suggest to partner with a vendor or implement via fast track. While not complicated, the setup is important and involves a lot of moving parts. Alternatively you can start here - https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect, https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune
