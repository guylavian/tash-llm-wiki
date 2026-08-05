---
title: "What are the ingress IP addresses for the exchange hybrid configuration?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1700346/what-are-the-ingress-ip-addresses-for-the-exchange
question_id: 1700346
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# What are the ingress IP addresses for the exchange hybrid configuration?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1700346/what-are-the-ingress-ip-addresses-for-the-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are planning to set up a hybrid configuration to integrate the on-premises Exchange server calendar with the Teams application. We want to restrict connections to the auto-discover and EWS URLs only from the Microsoft 365 environment and not expose them to the internet. Therefore, we need to find the IP address details for the ingress traffic to Exchange Onprem. Where can we find this information?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-05*

Bruce Jing-MSFT obviously did not properly read your question.

I am also interested in the answer.

Did you ever work out what subset of IP Addresses from https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide#exchange-online was needed for this?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-19*

Hi，@Vimal K

Thanks for posting your question in the Microsoft Q&A forum.

You want to integrate your on-premises Exchange server calendar with the Teams application.

First, you need to meet the prerequisites, you can refer to this link for details: Resolve interaction issues between Teams and Exchange Server - Microsoft Teams | Microsoft Learn

Step1：The Teams service uses the Exchange Autodiscover service to locate the EWS URL that is published by the server that's running Exchange Server. To verify that the Autodiscover process is working correctly, use the following steps:

-  Ask the user to navigate to the Microsoft Remote Connectivity Analyzer. The Remote Connectivity Analyzer tool uses a specific set of IP addresses to locate the EWS URL. For a list of these IP addresses for Microsoft 365, see the information for ID 46 in Microsoft 365 URLs and IP address ranges.

-  Select the Use Autodiscover to detect server settings check box.

-  Input the requested information.

-  Select the Perform Test button to start the Autodiscover test.

If the test fails, you must first resolve the Autodiscover issue.

Step 2: Verify that the Autodiscover service can route the Autodiscover requests to on-premises

In Windows PowerShell, run the following command:

Invoke-RestMethod -Uri https://outlook.office365.com/autodiscover/autodiscover.json?Email=******@contoso.com&Protocol=EWS&RedirectCount=5 -UserAgent Teams

For a mailbox hosted on-premises, the EWS URL should point to the on-premises external EWS. The output should resemble the following:

If this test fails, or if the EWS URL is incorrect, review the Prerequisites section. This is because the problem is likely caused by an Exchange hybrid configuration issue, or a firewall or reverse proxy that is blocking external requests.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
