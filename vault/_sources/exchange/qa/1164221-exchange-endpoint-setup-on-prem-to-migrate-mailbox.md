---
title: "Exchange Endpoint setup on prem to migrate mailboxes to 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164221/exchange-endpoint-setup-on-prem-to-migrate-mailbox
question_id: 1164221
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange Endpoint setup on prem to migrate mailboxes to 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164221/exchange-endpoint-setup-on-prem-to-migrate-mailbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings everyone,

I am trying to setup a migration endpoint on exchange 2016 (from on prem into 365)

I've been following the guide here (Migrate email to Exchange Online using the Exchange cutover method in Exchange Online | Microsoft Learn)

I have tested my outlook anywhere using https://testconnectivity.microsoft.com/ and it has passed with some warnings: The Microsoft Connectivity Analyzer can only validate the certificate chain using the Root Certificate Update functionality from Windows Update. Your certificate may not be trusted on Windows if the "Update Root Certificates" feature isn't enabled.

This test did pass with those warning so I just moved onto the next step.

On Step 2: Connect Microsoft 365 or Office 365 to your email system

In the ECP of our on prem exchange i'm trying to create the endpoint. When I put in the credentials for the test email and forest admin it returns this error and tells me to manually put in the FQDN settings

 We couldn't detect your server settings. Please enter them. Method not found: ‎'Void Microsoft.Exchange.WebServices.Data.EwsHttpWebRequest..ctor‎(System.Uri, System.Net.Security.RemoteCertificateValidationCallback)‎‎'.

Remote MRS proxy server:  

The FQDN of the Exchange server that the Mailbox Replication Service (MRS) Proxy is on.

When I manually put in my FQDN it just says "error connection could not be completed."

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-26*

Hi @Isaac Percy ,

Do you enable TLS 1.2? Here is a similar case: Migration to Exchange Online - ERROR - Connection to the server .. could not be completed / MRS Proxy

Thanks for your feedback above which shared more information and glad to know that your issue is resolved now! Since our forum has the policy that The question author cannot accept their own answer. They can only accept answers by others, and according to the scenario introduced here: Answering your own questions on Microsoft Q&A

I would make a brief summary of this post so that other forum members could easily find useful information here:

[Exchange Endpoint setup on prem to migrate mailboxes to 365 - Summary]

Issue Symptom:  

When put in the credentials for the test email and forest admin it returns error and tells to manually put in the FQDN settings

Solution:  

Got around this issue by doing the minimal hybrid deployment

You could "Accept Answer" for this summary to close this thread, and your action would be helpful to other users who encounter the same issue and read this thread. Thanks for your understanding!

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-25*

I got around this issue by doing the minimal hybrid deployment option. Though I am still curious as to what that callback error is.
