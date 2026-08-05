---
title: "Exchange Hybrid - OAuth - unable to create or enable Federation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105373/exchange-hybrid-oauth-unable-to-create-or-enable-f
question_id: 2105373
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid - OAuth - unable to create or enable Federation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105373/exchange-hybrid-oauth-unable-to-create-or-enable-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Run and Deploy the Hybrid Configuration between our Exchange server and Exchange online.

After Run the Wizard we encounter Auth error and as per suggestion from Microsoft We try to do manually but in that we encounter strange error at the time of new-federationtrust command, we have also tried the Graphically as well.

Error: Unable to access the Federation Metadata document from the federation partner. Detailed information: "The underlying connection was closed: An unexpected error occurred on a send.".

We have check all the steps TLS 1.2 is enable, Outbound and internet connection is okay, all the required XML and links are open over the exchange server, still though we are not able to enable the federation trust.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-18*

Hi, @Khushi Joshi

There are many reasons for the problem, and here are some common solutions you can try:

-  Check that the prerequisites for hybrid deployments are met.Hybrid deployment prerequisites | Microsoft Learn

-  Restart the Exchange hybrid server and rerun the HCW.

-  Run the following command on the local hybrid server:

```
Get-ExchangeCertificate | where {($_.CertificateDomains -eq 'Federation') -and ($_.Status -eq 'Valid')} | Select-Object -Expand Thumbprint
New-FederationTrust -Name “Microsoft Federation Gateway” -Thumbprint 
```

-  Ensure that only one AAD is deployed per tenant.

-  Collect HCW logs and make a request to the Microsoft support team. Customer service phone numbers - Microsoft Support

Your question is mentioned in this post How to address Federation Trust issues in Hybrid Configuration Wizard (HCW) - Microsoft Community Hub

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
