---
title: "Multiple failed login request Kerberos pre-authentication failed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4172026/multiple-failed-login-request-kerberos-pre-authent
question_id: 4172026
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Multiple failed login request Kerberos pre-authentication failed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4172026/multiple-failed-login-request-kerberos-pre-authent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

* More recent, similar thread. 

https://answers.microsoft.com/en-us/windows/forum/all/kerberos-pre-authentication-failed/7e379cbb-990b-4952-9d68-48007958dc40 

 Event ID: 4771  Log Name:      SecuritySource:        Microsoft-Windows-Security-AuditingDate:          16-02-2023 14:37:05Event ID:      4771Task Category: Kerberos Authentication ServiceLevel:         InformationKeywords:      Audit FailureUser:          N/AComputer:      NIAMUMPDC1.NIACL.CO.INDescription:Kerberos pre-authentication failed. Account Information:                Security ID:                         NIACL\24290                Account Name:                 24290 Service Information:                Service Name:                   krbtgt/NIACL.CO.IN Network Information:                Client Address:                 ::ffff:10.115.44.52                Client Port:                         51947 Additional Information:                Ticket Options:                  0x40810010                Failure Code:                     0x12                Pre-Authentication Type:             0 Certificate Information:                Certificate Issuer Name:                               Certificate Serial Number:                           Certificate Thumbprint:                 Certificate information is only provided if a certificate was used for pre-authentication. Pre-authentication types, ticket options and failure codes are defined in RFC 4120. If the ticket was malformed or damaged during transit and could not be decrypted, then many fields in this event might not be present.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-20*

Hi, my name is Anderson Souza, I hope I can help you with your issue.

If your computer is part of a corporate network, I believe that your question will be better resolved if it is posted in a more suitable location such as the new Microsoft Q&A forum that is replacing the old TechNet. As it is a question aimed at infrastructure administrators that have more knowledge about Microsoft's enterprise technologies, I believe that you will get better results there, since this forum here is intended for home Windows users. Please, check the link below:

https://docs.microsoft.com/en-us/answers/products/
