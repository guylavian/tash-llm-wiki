---
title: "[Migrated from MSDN Exchange Dev] Exchange Hybrid - All on-prem mail to route via EOP - SPF"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/142379/migrated-from-msdn-exchange-dev-exchange-hybrid-al
question_id: 142379
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Exchange Hybrid - All on-prem mail to route via EOP - SPF

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/142379/migrated-from-msdn-exchange-dev-exchange-hybrid-al (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/15f48032-8cf5-4c4f-a7e1-6370d44e29af/exchange-hybrid-all-onprem-mail-to-route-via-eop-spf?forum=exchangesvrdevelopment   

Hi all,  

If you have Exchange Hybrid configured, and the on-prem to Cloud send connector has been updated to route not just 'org' emails between the two - so in other words all on-prem email will go out of the 'hybrid' SMTP connector to the EOP Tenant and then onwards to the final MX destination. In that deployment type, would you need to add your on-prem Public IP into the SPF for the organisation? If the EOP receive connector was basically already restricting the flow of SMTP either by source IP (on-prem) and/or Certificate Authentication?  

Thank you for any input.  

Phil

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-28*

In the hybrid environment, HCW creates the send connector "Outbound to Office 365" for mail flow from on-premises to Exchange Online. Emails from on-premises should be treated as internal messages. In general, we don't have to modify other send connectors and this is the recommended configuration from Microsoft. If you don't want to use the default connectors, after adding public IP's into SPF, please monitor the mail flow from on-premises for several days to make sure everything works well. Otherwise, we have to use connectors created by HCW for mail flow between on-premises and Exchange Online.    

For your reference: Office 365 – Common Exchange Online Hybrid Mail Flow Issues.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
