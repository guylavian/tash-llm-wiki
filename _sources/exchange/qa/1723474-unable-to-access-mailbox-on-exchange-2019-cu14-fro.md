---
title: "Unable to access mailbox on exchange 2019 cu14 from exchange 2016 owa"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1723474/unable-to-access-mailbox-on-exchange-2019-cu14-fro
question_id: 1723474
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to access mailbox on exchange 2019 cu14 from exchange 2016 owa

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1723474/unable-to-access-mailbox-on-exchange-2019-cu14-fro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After introducing 2019 CU14 to Exchange 2016(cu23) environment users cannot access migrated mailboxes from 2016 owa, authentication prompt loops. MAPI clients receive Server unreachable error. OWA through 2019 works as expected.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-24*

Hi @Roman Gelfand，

Welcome to the Microsoft Technical Support Forum.

 

According to your description, you cannot access the mailbox migrated from 2016 after you introduced 2019 CU14 into the Exchange 2016 (cu23) environment.

I suggest that you can follow the following methods to troubleshoot and solve the problem:

-  Make sure that the Exchange 2016 and Exchange 2019 environments have consistent authentication settings (for example, Integrated Windows Authentication or Basic Authentication). Mismatched settings may cause problems.

-  Verify that the internal and external URLs for OWA, ECP, Autodiscover, etc. are correctly configured in both environments. Incorrectly configured URLs may cause traffic routing issues. You can use the following PowerShell commands to check and set these URLs:

  Get-OWAVirtualDirectory | FL Identity,ExternalURL,InternalURL

  Get-ECPVirtualDirectory | FL Identity,ExternalURL,InternalURL

  Get-AutodiscoverVirtualDirectory | FL Identity,ExternalURL,InternalURL

To set the URLs if they are incorrect:

  Set-OWAVirtualDirectory -Identity "YourServer\owa (Default Web Site)" -InternalURL "https://yourserver.domain.com/owa" -ExternalURL "https://yourserver.domain.com/owa"

  Set-ECPVirtualDirectory -Identity "YourServer\ecp (Default Web Site)" -InternalURL "https://yourserver.domain.com/ecp" -ExternalURL "https://yourserver.domain.com/ecp"

  Set-AutodiscoverVirtualDirectory -Identity "YourServer\Autodiscover (Default Web Site)" -InternalURL "https://yourserver.domain.com/autodiscover/autodiscover.xml" -ExternalURL "https://yourserver.domain.com/autodiscover/autodiscover.xml"

-  Verify that the service connection point (SCP) used for Autodiscover is correctly configured and points to the correct server. Incorrect SCP settings may cause client connection problems. You can check the SCP settings in the following ways:

  Get-ClientAccessService | FL AutoDiscoverServiceInternalURI

-  If a load balancer or firewall is used between the client and the Exchange server, make sure it is correctly configured to handle communication between the Exchange 2016 and 2019 servers.

 

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
