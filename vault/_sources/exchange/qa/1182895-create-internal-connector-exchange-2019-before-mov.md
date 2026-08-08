---
title: "Create internal connector Exchange 2019 before moving mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182895/create-internal-connector-exchange-2019-before-mov
question_id: 1182895
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Create internal connector Exchange 2019 before moving mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182895/create-internal-connector-exchange-2019-before-mov (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, i got this job to migrate my Exchange server 2019 mailboxes in DAG to another Exchange server mailbox in DAG hosted on a cloud platform.   

I was able to create my 2 other servers and create a second DAG with recplicated DB.  

Since my new infrastructure will have a different ip addres, before moving my mailboxes from sv1/sv2 to sv3 and sv4 i would like to create a connector so that migrated mailboxed will redirected to the first DAG. Once all the mailboxes are migrated i plan to change MX records and DNS records to the new public IP Address.  

Would you guide me in the creation of this internal connector?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-02-21*

Sounds like you need a shared SMTP space and continue to point the mx record at the existing Exch Servers

[http://clintboessen.blogspot.com/2020/07/smtp-namespace-sharing-how-it-differs.html]

To configure SMTP Namespace Sharing, you would change the Accepted Domain to an "Internal Relay Domain" and then create a send connector.  An example config would look like this:

Set-AcceptedDomain contoso.com -DomainType InternalRelay

New-SendConnector -Name "SMTP Namespace Sharing for Consoto.com" -Custom -AddressSpaces contoso.com -SmartHosts 10.1.1.54 -SourceTransportServers ExchangeServerFQDN

Once migrated, then you can change the MX record to point to the new infrastructure and set the accepted domain to Authoritative
