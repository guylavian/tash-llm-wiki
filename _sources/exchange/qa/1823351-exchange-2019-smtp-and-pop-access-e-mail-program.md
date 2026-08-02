---
title: "exchange 2019 smtp and pop access e-mail program"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1823351/exchange-2019-smtp-and-pop-access-e-mail-program
question_id: 1823351
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2019 smtp and pop access e-mail program

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1823351/exchange-2019-smtp-and-pop-access-e-mail-program (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning, I would like to use the Exchange 2019 server that we also have for sending mail with a non-domain PC with Outlook or another mail program, configuring it with a classic mail account, as if I have to configure an Aruba mail address or another provider , setting the pop and smpt.

How do I enable pop and smtp services on exchange for a user outside the domain or even with domain credentials?

I tried to look for some configuration solution on search engines but the configuration both via ECP and from commands is not clear.

Thanks so much for any info,

Raf

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-19*

Hi,

Welcome to the Microsoft Q&A forum.

Did you refer to these links：https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-pop3?view=exchserver-2019&source=recommendations，https://learn.microsoft.com/en-us/exchange/clients/pop3-and-imap4/configure-authenticated-smtp?view=exchserver-2019&source=recommendations

And based on my personal experience, the steps might be:

 Enabling POP and IMAP Services:

-  Open the Exchange Admin Center (EAC):

-  Navigate to `https://<YourExchangeServer>/ecp` and log in with your admin credentials.

2.Enable POP and IMAP services:

-  Go to Servers > Servers.

-  Select the server you want to enable POP on and click Edit (the pencil icon).

-  In the server properties window, go to POP3 and IMAP and enable the services. Make sure both services are started.

-  Repeat the same for IMAP if you need it.

-  Configure Authentication Settings for POP and IMAP:

-  Go to Servers > Virtual directories.

-  Select POP3 (or IMAP4) and click Edit.

-  Under Authentication, choose the authentication method you prefer (e.g., Plain text login, SPA).

-  Ensure that the settings match the requirements for your clients.

 Enabling SMTP Access:

-  Open Exchange Management Shell (EMS):

-  Run `Get-ReceiveConnector` to list all receive connectors.

-  Create a New Receive Connector for SMTP:

```
New-ReceiveConnector -Name "External SMTP" -Usage Custom -Bindings 0.0.0.0:587 -RemoteIPRanges 0.0.0.0-255.255.255.255
```

-  Configure Authentication and Permissions:

-  Set permission groups for the new connector:

```
Set-ReceiveConnector "External SMTP" -PermissionGroups AnonymousUsers,ExchangeUsers,ExchangeServers,Partners
```

-  Enable basic authentication:

```
Set-ReceiveConnector "External SMTP" -AuthMechanism BasicAuth
```

-  Restart Services:

-  To apply changes, restart the Microsoft Exchange POP3, Microsoft Exchange IMAP4, and Microsoft Exchange Transport services:

```
Restart-Service MSExchangeTransport
   Restart-Service MSExchangePOP3
   Restart-Service MSExchangeIMAP4
```

Configuring User Settings:

-  Ensure the user has the appropriate mailbox settings:

-  In the EAC, go to Recipients > Mailboxes, select the mailbox, and click Edit.

-  Go to Mailbox features and ensure that POP3 and IMAP4 are enabled for the mailbox.

 Client Configuration:

-  Outlook or other mail programs:

-  Use the following settings in the email client:

-  Incoming mail server (POP3): `mail.yourdomain.com`

-  Outgoing mail server (SMTP): `mail.yourdomain.com`

-  Authentication: Your username (usually the email address) and password.

-  Encryption: Choose SSL/TLS if your server requires it.

-  Port settings:

-  POP3: Typically port 995 (SSL) or 110 (non-SSL).

-  SMTP: Port 587 (TLS/STARTTLS) or 25.

Please feel free to contact me for any updates.And if this helps,don't forget to mark it as an answer.
