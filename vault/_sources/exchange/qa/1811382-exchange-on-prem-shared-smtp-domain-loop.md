---
title: "Exchange On Prem shared smtp domain loop"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1811382/exchange-on-prem-shared-smtp-domain-loop
question_id: 1811382
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange On Prem shared smtp domain loop

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1811382/exchange-on-prem-shared-smtp-domain-loop (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 2 AD domains with 2 exchange 2016 organization which shares the domain.com smtp domain, we're migrating from domainA to domainB.

We set up the 2 exchange domains to share the domain.com by adding it as accepted domain on both the organization as "internal relay".

The we configured the send connector for the shared domain to forward the "unkown email" to the other Org.

To cope with the unknown recipient issue, which would create a loop, we followed the advice from this article  https://ibrahimnore.wordpress.com/2012/09/10/configuring-smtp-namespace-sharing-between-two-exchange-forests-part-3/ creating the transport rules on each organization.  

All seems to be running correctly, but we noticed that:

-  the user is not getting any NDR for non-existant recipient

-  In the server queue "submission" we noticed emails for "local loop" that should not exist because of the transport rules

can anyone help us on this ?

thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-15*

Hi @Stefano Colombo,

Welcome to the Microsoft Q&A platform!

Based on your description, it sounds like you have done a lot of the setup correctly, but you are running into some issues with non-delivery reports (NDRs) and local loop errors.

After my research, I suggest that you can follow the steps below to troubleshoot:

-  NDRs for non-existent recipients:

-  Make sure the transport rules you created are configured correctly to handle messages for non-existent recipients. This may involve setting up custom NDRs or making sure the rules cover all possible scenarios.

-  Double-check the internal relay configuration on both Exchange organizations to confirm that they are set up correctly.

-  Verify that all connectors and transport rules are scoped and ordered correctly to avoid conflicting rules or configurations that may suppress NDRs.

-  Local loop errors:

-  Transport rules: Review the transport rules for both organizations to ensure that they explicitly prevent email from looping back. Check the conditions and actions to ensure that they are defined correctly.

-  Accepted domains: Confirm that the accepted domain is still configured as "internal relay" rather than "authoritative". If the organization is authoritative for a domain, unknown recipients will not be forwarded, which may cause loops.

-  Connectors: Make sure both the Send connector and the Receive connector are configured correctly. The Send connector should point to the correct destination, and both organizations should know where to route email.

-  MX records: Confirm that the MX records in DNS are accurate and properly directing traffic to the correct Exchange organization without confusion or misrouting.

-  Mail flow logs: Check the mail flow logs for both organizations to see where the loop is occurring. This will help determine if the problem is with the transport rules, connector settings, or other configuration.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
