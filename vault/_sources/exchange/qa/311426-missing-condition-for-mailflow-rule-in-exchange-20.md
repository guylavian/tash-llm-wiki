---
title: "Missing condition for mailflow rule in Exchange 2016 On Premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/311426/missing-condition-for-mailflow-rule-in-exchange-20
question_id: 311426
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Missing condition for mailflow rule in Exchange 2016 On Premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/311426/missing-condition-for-mailflow-rule-in-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I would like to get help on a mystical issue when I was trying to set up a mailflow rule on Exchange 2016 on-premise. My goal is to redirect the mail from a specific group of sender to a send connector.

I've successfully do this with Office365:

-   In the send connector we set that we want to use this connector only when I have a transport rule set up that redirects messages to this computer.    And then we set up how we want to route email messages - Route email through these smart host, and we input the smart host IP (public IP of Edge server).

-   In the Mail flow rule, we set up the condition to "Apply this rule if ..." the sender is inside the organization.    Next in the Do the following we set up Redirect the message to the following connector and we choose the send connector.

Then specify the exceptions . . .

However, it is impossible to do this job OnPremise:

-   In the send connector there isn't any option for use this connector only when I have a transport rule set up that redirects messages . . .

-   In the transport rule there isn't option for Redirect the message to the following connector.

Do you have any thoughts about this issue? What could possibly be done to achieve the same goal with on premise installation?

Thanks in advanced.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi @Hiếu Lâm      

Yes, that's the default behavior in Exchange server. We can check them in offcial documents    

1.Mail flow rule actions in Exchange Online    

Use the following connector    

Redirect the message to > the following connector    

RouteMessageOutboundConnector	OutboundConnector	Uses the specified outbound connector to deliver the message. For more information about connectors, see Configure mail flow using connectors.    

2.Mail flow rule actions in Exchange Server    

Redirect the message to these recipients    

Redirect the message to > these recipients	RedirectMessageTo	Addresses	Redirects the message to the specified recipients. The message isn't delivered to the original recipients, and no notification is sent to the sender or the original recipients.    

For the reason how Exchange server choose send connectors for outbound messages we can check the maiflow for on-premise Exchange server here: Mail flow and the transport pipeline    

    

The Mailbox Transport Submission service uses RPC to retrieve the outbound message from the local mailbox database.    

The Mailbox Transport Submission service uses SMTP to send the message to the Transport service on the local Mailbox server or on a different Mailbox server.    

In the Transport service, the default Receive connector named "Default <Mailbox server name>" accepts the message.    

What happens next depends on the configuration of the Send connector:    

Default: The Transport service uses the Send connector you created to send the message to the Internet.    

Outbound proxy: The Transport service uses the Send connector you created to send the message to the Front End Transport service on the local Mailbox server or on a remote Mailbox server. In the Front End Transport service, the default Receive connector named "Outbound Proxy Frontend <Mailbox server name>" accepts the message. The Front End Transport services sends the message to the Internet.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
