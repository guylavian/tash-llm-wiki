---
title: "Can On-Prem Exchange 2019 service two Organisation Domains (Send/Rec emails)?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1053691/can-on-prem-exchange-2019-service-two-organisation
question_id: 1053691
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Can On-Prem Exchange 2019 service two Organisation Domains (Send/Rec emails)?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1053691/can-on-prem-exchange-2019-service-two-organisation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Exchange experts,    

Plan to implement new On-Prem AD and Exchange 2019. The objective is to deploy 1 AD and 1 Exchange (Mailbox) and another Exchange server (Edge) to service two organisation Domains. Both Domains (i.e. work.com and tuition.org) can use this single Exchange mailbox server to send/Receive emails.    

-  Is the above possible?    

-  What are the steps to implement the above?    

Hope the expert can share their experiences.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-19*

Hi! @Mohd Ali Abdullah    

You can config Exchange to accept mail for multiple authoritative domains to solve the issue. As long as the Public DNS record for both two domains points to your Exchange org and you have the two domains set as accepted domains, it will work.

You can reference the following steps to configure it :  

-  Create Public DNS records  

Add the following records in Public DNS. If you already do see records configured, have a closer look. If you have more than one record with the same type, mail flow will not work as expected.  

i. MX record points to Exchange Server domain.  

ii. SPF record to authorize the mail server to send with the domain.  

iii. A record point to the MX record IP-address to have autodiscover work on mobile devices (iOS/Android).  

iv. SRV record for autodiscover, so you don’t get a certificate error.  

By adding the SRV autodiscover record, you can add multiple domains and use the same SAN (Subject Alternative Name) certificate, also known as a multi-domain certificate. The changes will not be visible instantly after you create the records. It depends on the configured TTL. If you did enter the records the first time, you would see the records live within 5 to 10 min.

-   Create an authoritative domain  

    In the EAC, navigate to Mail flow > Accepted domains, and click Add+..  

    In the Name field, enter the display name for the accepted domain. Each accepted domain for your organization must have a unique display name. This may be different than the accepted domain. For example, the domain contoso.com could have a display name of Contoso Local Accepted Domain.  

    In the Accepted domain field, specify an SMTP namespace for which your organization accepts email messages. For example, contoso.com.  

    Select Authoritative domain.  

    Click Save.

-   Configure an email address policy for the authoritative domain  

    For your requirement, you may need to replace the existing primary email address for a filtered set of recipients which are in different department or company. You can use EAC to finish it.( For the filtered set of recipients, you can add them to different organization to solve it)  

    ]2

For more information about the multiple domain setting issue ,you can reference this Microsoft Document : configure-exchange-to-accept-mail-for-multiple-authoritative-domains-exchange-2013-help
