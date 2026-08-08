---
title: "Replacing Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185196/replacing-domain-controller
question_id: 2185196
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Replacing Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185196/replacing-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are replacing an old Windows Server 2008 domain/dns/dhcp/file server with a new Windows Server 2022. When adding the new 2022 server to the domain and promoting it to domain controller, should you do this after hours? Does it disrupt the entire domain when it replicates? Can users still login during this time?

dhcp and dns, how do you copy these over to the new server? i assume this is an after hours thing. 

Last thing, the AD connect / Entra connect sync for emails.. if you reinstall this or update it to the new version on a new server, will this sign out everyone's email where they have to log back in? Any idea how long the sync process is? 

Any links to this would be very appreciated.

Thank you in advance!

## Answer (community) — community member

*upvotes: 1 · updated: 2024-04-16*

Hi Matt Fraiol,

Thank you for posting in the Microsoft Community Forums.

We are replacing an old Windows Server 2008 domain/dns/dhcp/file server with a new Windows Server 2022. When adding the new 2022 server to the domain and promoting it to domain controller, should you do this after hours? Does it disrupt the entire domain when it replicates? Can users still login during this time?

You just need to join the 2022 server to the domain and elevate it to domain control.

Then the contents of the domain will be automatically copied to the new domain control, this does not destroy the entire domain, it is normal operation for the domain. Users will still be able to log on normally during this period.

Then transfer the FSMO from the 2008 server to the 2022 server.

dhcp and dns, how do you copy these over to the new server? i assume this is an after hours thing.

The DNS records will be automatically copied to the new server if your AD domain is a DNS integrated domain.

Since the tag you chose belongs to the AD service and this question is about networking, I'm not sure if the DNS records are replicated in the case of DHCP records vs. non-integrated domains. I don't understand the network part. You can ask this question under network tag.

Last thing, the AD connect / Entra connect sync for emails.. if you reinstall this or update it to the new version on a new server, will this sign out everyone's email where they have to log back in? Any idea how long the sync process is?

I don't understand this question either, as I said above, I only understand the AD part.

So the parts you need to ask elsewhere are DHCP & DNS (network)

AD connect / Entra connect for email this one I don't know which tag it belongs to either.

Very sorry about that.

Best regards

Neuvi Jiang
