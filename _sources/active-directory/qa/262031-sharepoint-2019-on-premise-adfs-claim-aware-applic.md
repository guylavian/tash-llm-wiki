---
title: "SharePoint 2019 on-Premise ADFS claim aware application is not sync with AD profile."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/262031/sharepoint-2019-on-premise-adfs-claim-aware-applic
question_id: 262031
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SharePoint 2019 on-Premise ADFS claim aware application is not sync with AD profile.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/262031/sharepoint-2019-on-premise-adfs-claim-aware-applic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a setup with ADFS claim aware application. It working as expected.  

Am able to login through domain credentials But SharePoint login profile is not synchronize with my AD profile means in SharePoint my site profile is not get synchronize with my AD profile.  

Some blogs suggest to use ldapcp add-on. Here am able to deploy the ldapcp add-on.  

But after deployed people picker is not working. It not searching a user in AD.   

Am getting error “Multiple entries matched, please click to resolve.”  

Please suggest how to resolve the SharePoint ADFS claim aware application profile sync issue with or without using ldapcp?  

Thanks   

Sivasubramanian.G

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-08*

@siva subramanian       

You could refer following article to know how to configure User Profile Service Application to use newly created Trusted Claims Provider for importing users from Active Directory.    

Configure User Profile Service For ADFS Provider    

If an Answer is helpful, please click "Accept Answer" and upvote it.	    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
