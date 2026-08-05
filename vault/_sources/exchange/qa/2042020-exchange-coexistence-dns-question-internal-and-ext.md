---
title: "Exchange coexistence DNS question internal and external records"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2042020/exchange-coexistence-dns-question-internal-and-ext
question_id: 2042020
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange coexistence DNS question internal and external records

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2042020/exchange-coexistence-dns-question-internal-and-ext (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the final stages at a client of moving things over to a 2019 Exchange server that is currently setup in coexistence with an older Exchange 2013 server. Certificates and namespace is all prepared (mail.company.com)

My question specifically is this.

The internal DNS records (LAN) in the company points to Exchange 2013

The external DNS records (WAN) also point to Exchange 2013

I am currently testing a few pc's (LAN) by modifying the host file, to test connectivity with a pilot group.

What would happen if I start pointing the external DNS (WAN) to the Exchange 2019 server while briefly keeping the internal DNS pointed to Exchange 2013 for a few days until testing is done?

I want to know if for example a user that has mobile email configured on a phone/tablet would notice anything strange, meaning, if the user is outside the office the phone connects to Exchange 2019 but in the office WiFi still points to 2013 so on the LAN side the phone would connect to Exchange 2013.

Will this cause Outlook profile/connection issues the people working from both inside as outside the company? Not only for mobile devices but also for a non-domain joined laptop? I'm not sure how Outlook responds switching between servers inside and outside the company building..

I know best practice is point everything to the new server but I couldn't figure out the behavior to be expected when doing it this way.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-06*

Hi,Welcome to the Microsoft Q&A platform!

Let's break down the considerations and potential impacts:

-  Autodiscover Service: Outlook clients and mobile devices use the Autodiscover service to find the mailbox server and configure the connection settings. In a coexistence scenario, Autodiscover should ideally be updated to point to the Exchange 2019 server. By doing so, regardless of whether the client connects via LAN or WAN, it will receive configurations pointing to Exchange 2019.

-  Split DNS and Namespaces: In a split DNS configuration, internal and external DNS should resolve to the appropriate server. If external DNS is updated to Exchange 2019 but internal DNS still points to Exchange 2013, clients on the LAN using Wi-Fi could potentially see inconsistencies or errors, especially if their mailbox has already been moved to Exchange 2019.

-  Outlook Connectivity:

-  Inside the Office (LAN/Wi-Fi): If internal DNS points to Exchange 2013 but the mailbox resides on Exchange 2019, Outlook will initially contact the Exchange 2013 server, which will then proxy the request to Exchange 2019. This adds an extra hop and could introduce delays or inconsistencies.

-  Outside the Office (WAN): If external DNS points to Exchange 2019, users outside the office should connect directly to the new server without issues. They should receive the correct mailbox location via Autodiscover.

-  Mobile Devices: For mobile devices, especially those not using domain credentials (like many user-owned phones), there might be a noticeable delay as the device might interpret the change as a different server migration. This could lead to re-prompting for credentials or a slight disruption during the transition.

-  Non-Domain Joined Laptops: These devices will rely heavily on Autodiscover and DNS settings. If they are switching between LAN (pointing to Exchange 2013) and WAN (pointing to Exchange 2019), they might experience connection delays or be prompted to re-authenticate

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer!
