---
title: "One User cannot open Outlook (on-prem Exchange 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163747/one-user-cannot-open-outlook-on-prem-exchange-2019
question_id: 1163747
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# One User cannot open Outlook (on-prem Exchange 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163747/one-user-cannot-open-outlook-on-prem-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am having an odd problem. We migrated from On-Prem Exchange 2010 to 2019 via 2016 and everything is working fine and as intended.

THe issue is that one Shared user account on our Domain cannot open the Outlook App (2021 version) stating that it cannot connect to the Exchange Server.

When creating a new Outlook profile, it is fine and can connect automatically to the account and signs in to the Exchange Server no problem and completes. Then when trying to open Outlook, it fails.

I have tried multiple PCs and the same things happens. It only started happening randomly a couple of weeks ago and doesnt always happen.

DNS / nslookup resolves correctly as does the autodiscover. I can provide screenshots and logs if anything is required.

Any help would be great.

Thanks,

Declan

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-26*

Hi @Declan Ridley  ,

Please refer to the following steps to create a registry entry that excludes your Outlook to detect Office365 and see if it changes:

1.Locate this location in Registry Editor：

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\AutoDiscover

2.Create a DWORD (30-bit) value for ExcludeExplicitO365Endpoint and change the value to "1" to enable it.

3.Restart the computer and log in to the Outlook client.

 

If you are still unable to connect to the exchange server after the above operations, please refer to this link to run Test Email AutoConfiguration .

Enable and collect logs for profile creation issues - Outlook | Microsoft Learn

If possible, please provide the screenshot about log page for our better research. (In order to avoid the disclosure of your privacy, please remember to hide your personal information).

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hi,

Thank you for posting your query.

Kindly follow the steps provided below to resolve your issue.

Check with your account administrator to see what version of Exchange Server is managing your account.

Outlook for Mac supports accounts managed by Microsoft Exchange Server 2007 Service Pack 1 with Update Rollup 4 (KB952580) and later versions

Go to this link for your reference and other troubleshooting procedures https://support.microsoft.com/en-us/office/i-can-t-connect-to-my-exchange-account-372b793f-e8d3-4aed-a3a9-dbfbfad97c6d

Do not hesitate to message us if you need further assistance.

If the answer is helpful kindly click "Accept as Answer" and up vote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

Hi,

Thank you for posting your query.

Kindly follow the steps provided below to resolve your issue.

Check with your account administrator to see what version of Exchange Server is managing your account.

Outlook for Mac supports accounts managed by Microsoft Exchange Server 2007 Service Pack 1 with Update Rollup 4 (KB952580) and later versions

Go to this link for your reference and other troubleshooting procedures https://support.microsoft.com/en-us/office/i-can-t-connect-to-my-exchange-account-372b793f-e8d3-4aed-a3a9-dbfbfad97c6d

Do not hesitate to message us if you need further assistance.

If the answer is helpful kindly click "Accept as Answer" and up vote it.
