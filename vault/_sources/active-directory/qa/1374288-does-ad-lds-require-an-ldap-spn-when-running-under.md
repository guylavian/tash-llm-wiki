---
title: "Does AD LDS require an LDAP SPN when running under a service account?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374288/does-ad-lds-require-an-ldap-spn-when-running-under
question_id: 1374288
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Does AD LDS require an LDAP SPN when running under a service account?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374288/does-ad-lds-require-an-ldap-spn-when-running-under (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Scenario:

There is an LDS instance hosted on a domain member server.  The LDS service is running under the context of a domain member service account.  There are SPN values (LDAP/hostname, etc.) registered on the service account.

I'm trying to understand why those values were registered.  In what scenario(s) would this be required?  When would Kerberos be used for authentication?

Note: The LDS instance contains/supports userProxy objects.

Thanks,

DaveC

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-29*

Thank you @Wesley Li  

Yes I stood up an LDS instance in lab, running under service account, and every hour I see it attempting to register SPNs and create a ServicePointConnection object.  I had intentionally not granted the svc account any privileges in the ADDS directory.

At the moment I'm a bit lost on the statement you made regarding "AD/LDAP Connector", but I'll research it later.

One interesting thing I notice about enabling Kerberos for LDS running as an ADDS svc account - it sort of mucks up using the AD PS module to target the LDS instance from a remote machine (even when the account being used has permission inside LDS).  This is because ADWS (on the LDS server) run as the local system.  Changing ADWS to run as that same service account is the solution.  My conclusions were:

-  If SPN registration is prevented, then authenticating to LDS can use NTLM (not necessarily desirable, but...whatever, this is just a test :) )

-  If SPN gets registered, then remote clients (running from ADDS domain members) can obtain a ticket for LDS, and this works fine for typical LDAP clients.  But PS module connects to ADWS on the LDS and will now present the ticket it obtained.  If ADWS is not running as the service account it has no means for decrypting that ticket and the client does not fall back to NTLM in this scenario.  Client throws an SSPI exception, which is expected since the ticket is not really valid in this context.

-DC
