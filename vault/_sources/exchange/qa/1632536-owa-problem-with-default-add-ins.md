---
title: "OWA - problem with default add-ins"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1632536/owa-problem-with-default-add-ins
question_id: 1632536
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# OWA - problem with default add-ins

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1632536/owa-problem-with-default-add-ins (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have MS Exchange 2019 on-prem. It is likely that after the installation of CU14 or CU14 Mar24SU, the add-ins installed by default (like My Templates) stopped working.

I have displayed the application configuration

```
Get-App -OrganizationApp | fl
```

and I see incorrect URLs in the ManifestXML and IconURL attribute.

The IconURL contains the address:

https://Exchange_FQDN/owa/MailboxGUID@Mailbox_email_domain/prem/15.2.1544.9/ext/def/a216ceed-7791-4635-a752-5a4ac0a5eb93/images/app_icon.png

It seems to me that the URL should be:

https://Exchange_FQDN/owa/prem/15.2.1544.9/ext/def/a216ceed-7791-4635-a752-5a4ac0a5eb93/images/app_icon.png.

The same applies to the SourceLocation attribute in the FormSettings section of the ManifestXML.

The entry looks like this:

```

```

and it should look like this:

```

```

Has anyone had this problem and solved it?

Best regards,

Rafal

## Answers

_No answers on this thread._
