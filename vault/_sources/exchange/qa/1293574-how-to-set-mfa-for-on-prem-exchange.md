---
title: "how to set MFA for on prem Exchange."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1293574/how-to-set-mfa-for-on-prem-exchange
question_id: 1293574
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# how to set MFA for on prem Exchange.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1293574/how-to-set-mfa-for-on-prem-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

how can I set MFA for Exchange on premise (I have hybrid so;ution), I created MFA for Owa using application proxy, but now I need to set MFA on Outlook application for in windows and on mobile, the users have Microsoft office 365 license,please help me

Thank you

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2023-05-29*

Hello @Waleed Waleed !

Welcome to Microsoft QnA!

First you must enable Modern Authentication

https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-exchange-server-for-hybrid-modern-authentication?view=o365-worldwide

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide

https://www.techtarget.com/searchwindowsserver/tip/Microsoft-modern-authentication-deadline-looms-over-Exchange

You can set up Conditional Access Policies or Per User MFA

You need Azure Premium P1 License , it is included in most plans

1.       Set up Azure AD Connect: Ensure that Azure AD Connect is installed and configured to synchronize user accounts from your on-premises Active Directory to Azure AD.

2.       Enable MFA for Azure AD users: Enable MFA for the user accounts that require MFA. You can enable MFA individually for each user through the Azure portal or in bulk using PowerShell.

3.       Configure Conditional Access policies: Create a Conditional Access policy in Azure AD to enforce MFA for Exchange on-premises. The policy should target the specific user group or users and require MFA when accessing Exchange resources.

4.       Enable Modern Authentication for Exchange: Ensure that Modern Authentication is enabled on your Exchange servers. Modern Authentication is required for MFA to work with Outlook applications.

5.       Configure MFA for Outlook clients: Depending on the Outlook client versions used by your users (e.g., Outlook for Windows, Outlook for Mac, Outlook mobile apps), you can configure the MFA settings accordingly. For Outlook for Windows, you can utilize the "Enable modern authentication" option in the Exchange Online PowerShell module. For Outlook for Mac and mobile apps, MFA is typically enforced by Azure AD, so the user will be prompted to complete the MFA process when accessing their mailbox.

6.       Test and monitor: Test the MFA setup by accessing Exchange on-premises resources using Outlook clients. Monitor the authentication logs in Azure AD to ensure that MFA is being enforced as expected.

If you need more assistance please let us know!

I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards
