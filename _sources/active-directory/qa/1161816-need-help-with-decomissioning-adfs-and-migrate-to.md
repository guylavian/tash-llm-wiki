---
title: "Need help with decomissioning ADFS and migrate to Azure cloud authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161816/need-help-with-decomissioning-adfs-and-migrate-to
question_id: 1161816
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Need help with decomissioning ADFS and migrate to Azure cloud authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161816/need-help-with-decomissioning-adfs-and-migrate-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi There,

I m looking for some assistance as we are in the process of migrating authentication from adfs to azure cloud using password sync. I have setup the stage roll out and it is working fine. Now I want to do final cut over, how do I go about it. Also how can i backup existing ADFS so that in case of roll over i should be able to do it. The existing system is not setup as ADFS farm.

Existing setup: ADFS 2.0, running on Win Server 2008R2

Azure AD connect sync is configured already.

Thanks,

Any help will be appreciated.

Rish

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-02-10*

The video is now live. https://www.youtube.com/watch?v=D0M-N-RQw0I

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-18*

So to flip the domain from federated to managed, you can follow this guide. [https://learn.microsoft.com/en-us/azure/active-directory/hybrid/migrate-from-federation-to-cloud-authentication#option-a. We have a video coming up soon that will show you this but it's basically following the steps here. To remove ADFS you can follow this doc [https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/decommission/adfs-decommission-guide which shows the backup commands as well.
