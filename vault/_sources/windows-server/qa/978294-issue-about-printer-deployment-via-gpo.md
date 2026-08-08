---
title: "Issue about printer deployment via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/978294/issue-about-printer-deployment-via-gpo
question_id: 978294
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue about printer deployment via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/978294/issue-about-printer-deployment-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Printer server is win server 2019. AD server is win server 2012 R2.    

I am trying to deploy printer but failure. GPO update not map new printer to existing user. But new user profile is ok.    

Otherwise manually add shared printer is ok.    

May I know 2012 AD server not available to deploy printer on 2019 server?    

I have to upgrade AD server from 2012 to 2019 to make deployment succeed ?    

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-08-30*

Hello @WwW  

May I know 2012 AD server not available to deploy printer on 2019 server?

To deploy printer connections using Group Policy, the Active Directory Domain Services (AD DS) schema version must be at least Windows Server 2008.

1.Do they get the update when you run gpupdate /force?  

2.Run gpresult /h report.html on the clients to check whether the GPO has been applied successfully  

3.Have you tried log them off and log back on the computer?  

4.Where did you configure this policy? Under user configuration or computer configuration?

I would highly recommend to check below 2 articles:

10 Common Problems Causing Group Policy To Not Apply - TechNet Articles - United States (English) - TechNet Wiki (microsoft.com)  

Troubleshooting: Group Policy (GPO) Not Being Applied to Clients | Windows OS Hub (woshub.com)  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

Best regards  

Karlie Weng
