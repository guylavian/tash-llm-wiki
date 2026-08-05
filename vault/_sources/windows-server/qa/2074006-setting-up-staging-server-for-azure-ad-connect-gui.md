---
title: "Setting up staging server for Azure AD Connect, Guide points to folder AdPrep that is missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2074006/setting-up-staging-server-for-azure-ad-connect-gui
question_id: 2074006
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Setting up staging server for Azure AD Connect, Guide points to folder AdPrep that is missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2074006/setting-up-staging-server-for-azure-ad-connect-gui (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In the middle of starting up a staging server for Azure AD Connect.  (2.3.20) on Windows Server 2022 Standard 21H2.

When confirming that the imported settings got right I saw that Device Write-back setting is not checked and even grayed out when customizing the setup.

Found what I believe a good guide to help me. https://learn.microsoft.com/en-us/troubleshoot/azure/entra/entra-id/user-prov-sync/cannot-enable-device-writeback#step-2-enable-the-organization-for-device-writeback

But in step 2.3 it points to a folder that doesn't exist for me neither in active server (2.2.1)  

%ProgramFiles%\Microsoft Azure Active Directory Connect\AdPrep  

I don't know how to continue, from all the different guides Ive been looking on points to something in that folder.

Any pointers given is much appreciated!  

Thanks in advance!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-20*

Hi Håkan Norman,

Thank you for posting in the Q&A Forums.

Check the version:

Verify that the version of Azure AD Connect you are using supports the Device Write-back feature. You can get the information by checking the official documentation or update logs.

Check permissions:

Ensure that the user performing the Azure AD Connect configuration is a global administrator of Azure AD and has sufficient permissions to modify Device Write-back settings.

Verify the environment configuration:

Ensure that the Azure AD Connect server meets all prerequisites for enabling Device Write-back, including network connectivity, firewall rules, DNS resolution, and so on.

Check that the trust relationship between Azure AD and the local Active Directory has been correctly established back. the associated

Synchronization

Rule 4...

** Check -Synchronization If the rule has a ** conflict: or

Incorrect Rule -, use Please Azure try AD modify Connect or of remove Synchronize them Rule, Editor and come to recheck the configuration for the presence of Device with WriteDevice- Writeback- settings.

Check the official documentation:

Visit the official Microsoft documentation for detailed information and configuration steps about Device Write-back.

https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-device-writeback

Official documentation usually provides the most up-to-date guidance, including any known limitations and issues.

Best regards

NeuviJ

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
