---
title: "Exchange 2019 onprem \"route outgoing emails based rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2075418/exchange-2019-onprem-route-outgoing-emails-based-r
question_id: 2075418
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 onprem "route outgoing emails based rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2075418/exchange-2019-onprem-route-outgoing-emails-based-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Exchange expert,

how to route outgoing emails(selection of smart host) based sender domain or group membership to smart host without use of any third party software. 

Let say you want to route messages from members of a certain group to a smart host instead of using default connector or dns. just like we have option in office365 to forward that rule to specific connector. 

Regards,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-23*

Hi,

Welcome to Microsoft Q&A community.

It is suggested to use the EAC to create a Send connector.

-  In the EAC, navigate to Mail flow > Send connectors, and then click Add .

-  In the New send connector wizard, specify a name for the send connector and then select Custom for the Type. You typically choose this selection when you want to route messages to computers not running Microsoft Exchange Server 2013. Click Next.

-  Choose Route mail through smart hosts, and then click Add . In the Add smart host window, specify the IP address, such as 192.168.100.1, or the fully qualified domain name (FQDN), such as contoso.com. Click Save.   For Smart host authentication, choose the type of authentication required by the smart host. If you choose Basic authentication, you must provide a username and password.   Note   If you choose Basic authentication, we recommend that you use an encrypted connection because the username and password are sent in clear text.

-  Under Address space, click Add . In the Add domain window, make sure SMTP is listed as the Type. For Fully Qualified Domain Name (FQDN), enter * to specify that this send connector applies to messages sent to any domain. Click Save.

-  For Source server, click Add . In the Select a server window, choose a server and click Add . Click OK.

-  Click Finish.

Once you have created the send connector, it appears in the Send connector list.

More details you can refer to:https://learn.microsoft.com/en-us/exchange/create-a-send-connector-to-route-outbound-email-through-a-smart-host-exchange-2013-help?source=recommendations
