---
title: "Pass windows credentials through ADFS for external site without being prompted??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/31276/pass-windows-credentials-through-adfs-for-external
question_id: 31276
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Pass windows credentials through ADFS for external site without being prompted??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/31276/pass-windows-credentials-through-adfs-for-external (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

im running into an issue with passing logged in user credentials through internal ADFS to external website without being prompted for credentials. I added the site into the trusted sites, set the "automatic logon with current username and pass", made sure the settings in "advanced" was correct. but no matter what i change, im still being promoted with the ADFS login page.  

any ideas??

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-06-03*

ADFS does not pass credentials.     

In order to achieved Sigle Sign On for an internal application you will need:    

-  Configure the application to use Federation and to point/redirect ADFS for authentication.    

-  Configure a Replying Party Trust for the application in ADFS.    

-  Confirm that Windows Integrated Authentication is configured on the primary authentication policy.    

-  Confirm that the ServicePrincipalName of the farm is set on the service account and only on the service account.    

-  Make sure the client is domain joined and have the URL of the ADFS server (not the application) in either the Trusted Site List or the Intranet Site List.    

-  Make sure the useragentstring of the browser is listed in the list of supported UAS for Windows Integrated Authentication (example for Chrome available here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia#configuring-wia-for-chrome).
