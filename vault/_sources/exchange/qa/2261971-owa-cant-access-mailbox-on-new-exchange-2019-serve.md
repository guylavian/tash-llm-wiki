---
title: "OWA can't access mailbox on new Exchange 2019 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261971/owa-cant-access-mailbox-on-new-exchange-2019-serve
question_id: 2261971
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OWA can't access mailbox on new Exchange 2019 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261971/owa-cant-access-mailbox-on-new-exchange-2019-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Deployed new 2019 exchange mailbox server. But Exchange OWA can't access the mailboxes. 

We currently running a mix 2016 and 2019 on-perm exchange environment and just deployed a new 2019 mailbox server. New mailbox database was created along with new mailboxes. The Outlook desktop client can access the mailbox on the new server. However, when using Oulook web OWA, it keep looping back to the login screen. It took the credential but just go back to the OWA login without any error.

This behavior is the same when trying to login to OWA from internal netowrk or from the internet.

I checked the AutoDiscoverService URLs and all servers are different but using the same format: "serverhostname".domain.com/owa

The Exchange Server Auth Certificate is present on the server and valid.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-30*

I figured out the issue. Extended Protection was enabled on the 2019_02 server. Once I disabled it, both the 2016 OWA can access the 2019_02 mailbox.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-29*

Hi @Wang Lee (Admin)  ,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, here are some suggestions for you:

-  When we login OWA, Autodiscover will not be used. So, we have to check OWA virtual directory configuration:   Get-OwaVirtualDirectory | Format-List Identity,InternalUrl, ExternalUrl   Also, the AutoDiscoverServiceInternalUri should be set to use the format https://autodiscover.domain.com/Autodiscover/Autodiscover.xml instead of “/owa”

-  Does the issue only occur with mailboxes on Exchange 2019? Do mailboxes on Exchange 2016 login OWA successfully?   If so, please login OWA with the following url on Exchange 2019 to see if the issue persists:   https://localhost/owa   https://server_ip/owa

-  When you reproduce the issue on specific Exchange server, please check application logs from event viewer. We can check if any error events generated at that time. Those error information may be helpful for further investigation.

-  There could be several suth certificates on Exchange server. Please use the following command on each Exchange server, we need to double-confirm if the specific auth certificate that set for AuthConfig exists on each Exchange server:   (Get-AuthConfig).CurrentCertificateThumbprint | Get-ExchangeCertificate | Format-List

 If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
