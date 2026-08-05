---
title: "SMTP send to Exchange Online with Inbound Connector - strange issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2276469/smtp-send-to-exchange-online-with-inbound-connecto
question_id: 2276469
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor"]
---
# SMTP send to Exchange Online with Inbound Connector - strange issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2276469/smtp-send-to-exchange-online-with-inbound-connecto (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We switched to a dedicated Windows SMTP server and moved away from Exchange Hybrid server for SMTP. Was working fine until  we changed the certificate (same cert but renewed wildcard cert for one of our domains). We use a smarthost entry and the inbound connector in EOL is for that domain and its wildcard using TLS. We have that wildcard cert set in SMTP for TLS and it shows its configured for it in settings under the access tab. 

Once we have it set it works fine for a bit but then we start getting errors in the SMTP logs for

550+5.7.64+TenantAttribution;+Relay+Access+Denied+ localservername+is+untrustedroot. 

So it is trying to use the servers local cert for some odd reason instead of the wildcard when authing to 365 suddenly. We do have certs issued to our servers from domain. but this hasn't been a problem before. 

Can anyone shed light as to how to resolve this? If we delete the machine/server certs it starts working again for a bit. But then resumes the problem once again once those certs get on the server.  Very odd and annoying. We know its working as it works when not trying to use local cert to auth to 365 for our inbound connector.

Thoughts?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-23*

Dear Team,

This is my answer:

Since the issue stems from auto-enrolled certs taking precedence, this workaround is effective:

Block domain-based auto-enrollment via Group Policy.

Keep only the wildcard cert you want for TLS authentication.

This works, but you lose the ability to use the machine cert for other purposes.

Windows' built-in SMTP service doesn't support SNI (Server Name Indication) or reliable certificate binding.

Alternative: Use a modern SMTP server that supports:

Explicit certificate binding,

SNI (if applicable),

Reliable TLS authentication.

Examples:

-  hMailServer (free, but less maintained),

-  Postfix on Windows Subsystem for Linux (WSL),

-  3rd-party commercial SMTP relay apps.Windows' built-in SMTP service doesn't support SNI (Server Name Indication) or reliable certificate binding.  Alternative: Use a modern SMTP server that supports:

-  Explicit certificate binding,

-  SNI (if applicable),

-  Reliable TLS authentication.

  Examples:

-  hMailServer (free, but less maintained),

-  Postfix on Windows Subsystem for Linux (WSL),

-  3rd-party commercial SMTP relay apps.

You could try using PowerShell or `certutil` to manage which certificates are available in the Computer\Personal store.

Example (PowerShell):

```
# Export or backup the wildcard cert first
$cert = Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object { $_.Subject -like "*.yourdomain.com" }
$cert | Remove-Item
```

Then re-import only the desired cert.

This is manual and not permanent; cert renewal or domain policy updates will reset it.

Best Regards,
