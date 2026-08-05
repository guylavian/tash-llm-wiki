---
title: "Facing issue while installing Microsoft Exchange server 2019 in production environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2150568/facing-issue-while-installing-microsoft-exchange-s
question_id: 2150568
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Facing issue while installing Microsoft Exchange server 2019 in production environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2150568/facing-issue-while-installing-microsoft-exchange-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have created an additional account for the Exchange deployment and granted Enterprise Admin, Domain Admin, and Schema Admin rights.

The Exchange and AD servers are located in the same site, and the Exchange server subnet is associated with this site.

Previously, we deployed the Exchange server, but it crashed due to a hardware issue. As a result, we removed the Microsoft Exchange organization from ADSI Edit in the configuration partition. This is a new deployment.

Failed [Rule:GlobalUpdateRequired] [Message:Global updates need to be made to Active Directory, and this user account isn't a member of the 'Enterprise Admins' group.]

Failed [Rule:GlobalServerInstall] [Message:You must be a member of the 'Organization Management' role group or a member of the 'Enterprise Admins' group to continue.]

Failed [Rule:DelegatedBridgeheadFirstInstall] [Message:You must use an account that's a member of the Organization Management role group to install or upgrade the first Mailbox server role in the topology.]

Failed [Rule:DelegatedCafeFirstInstall] [Message:You must use an account that's a member of the Organization Management role group to install the first Client Access server role in the topology.]

Failed [Rule:DelegatedFrontendTransportFirstInstall] [Message:You must use an account that's a member of the Organization Management role group to install the first Client Access server role in the topology.]

Failed [Rule:DelegatedMailboxFirstInstall] [Message:You must use an account that's a member of the Organization Management role group to install or upgrade the first Mailbox server role in the topology.]

Failed [Rule:DelegatedClientAccessFirstInstall] [Message:You must use an account that's a member of the Organization Management role group to install or upgrade the first Client Access server role in the topology.]

Failed [Rule:AdInitErrorRule] [Message:Setup encountered a problem while validating the state of Active Directory: Couldn't find the Enterprise Organization container.  See the Exchange setup log for more information on this error.]

## Answers

_No answers on this thread._
