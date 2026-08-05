---
title: "Windows OpenSSH SFTP Server Support for Kerberos Protocol Transition"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/627787/windows-openssh-sftp-server-support-for-kerberos-p
question_id: 627787
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Windows OpenSSH SFTP Server Support for Kerberos Protocol Transition

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/627787/windows-openssh-sftp-server-support-for-kerberos-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I wish to setup an SFTP Server front-end for file shares (virtual roots) located on backend hosts.  Does the OpenSSH-based SFTP server available with the newer Windows Server OSes support the Kerberos Protocol Transition (KPT) feature?   In addition, what are the known security vulnerabilities or threats associated with KPT?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-16*

Thanks all for the feedback.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-16*

I can't speak about the SFTP/Open SSH part of your question.  

But regarding the second about the risks of Kerberos Protocol Transition, I can :) To allow protocol transition, you basically need to allow a system to impersonate an account without having to know any of the shared secrets usually necessary to authenticate. So you would have to highly trust the system allowed to perform protocol transition. This way to delegate authentication to a third party service (outside of the domain controllers) makes it a primary target for attackers wishing to perform credential thefts and other impersonation techniques. There are plenty of posts and videos available that described how protocol transition and delegation can be abused in general and other specific vulnerabilities found using Kerberos delegation (Sean Metcalf’s website is usually a good starting point). Note that delegation can be disabled on sensitive accounts to avoid those accounts from being abused from systems allowed to perform delegation. But mitigation is another conversation...
