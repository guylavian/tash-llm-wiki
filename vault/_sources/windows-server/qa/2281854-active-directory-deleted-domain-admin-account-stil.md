---
title: "Active Directory :: Deleted Domain Admin Account Still Usable on Client Systems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2281854/active-directory-deleted-domain-admin-account-stil
question_id: 2281854
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory :: Deleted Domain Admin Account Still Usable on Client Systems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2281854/active-directory-deleted-domain-admin-account-stil (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a local Active Directory environment on Windows Server 2022 with approximately 100 domain-joined client systems. For support and administrative tasks on client machines, I had created a dedicated user account with administrative privileges in the domain.

As part of our security hygiene, the credentials (either the username or password) of this account are rotated weekly. However, I’ve recently observed a critical issue: even after the support account was deleted from Active Directory, it can still be used on client machines to perform elevated operations.

This raises a significant security concern, as it indicates that deleted or disabled accounts may still retain local elevation capabilities on client systems. Despite the account no longer existing in AD, it appears to function locally on the clients.

I am unable to identify the root cause or resolve this issue. I would appreciate guidance or support in remediating this issue.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-06-07*

The behavior you're observing happens because:

-  Kerberos tickets are cached locally (in memory) on the client and are valid until they expire, regardless of whether the account still exists in AD.

-  If the ticket is still valid, it can be used for authentication and SSO-based elevation (e.g., for `runas`, scheduled tasks, services, etc.).

-  In certain configurations, cached credentials (for offline login) may also allow a deleted user to appear functional temporarily, but Kerberos is the main culprit for continued privilege.

Check these domain-wide Kerberos policy settings (via GPO or `Default Domain Policy`):

-  Maximum lifetime for user ticket (TGT):
  Default: `10 hours`

-  Maximum lifetime for service ticket:
  Default: `600 minutes (10 hours)`

-  Maximum tolerance for computer clock synchronization:
  Default: `5 minutes`

So even after deleting the user from AD:

-  If the Ticket-Granting Ticket (TGT) is still valid, it can be reused until expiration.

-  The client doesn't revalidate the account's AD status unless a new TGT is requested (e.g., after logoff/logon or ticket purge).

To confirm, run the following on the computer where you're seeing this issue:

```
klist
```

You'll likely see:

-  A valid TGT (krbtgt/DOMAIN)

-  A ticket for the local admin task (e.g., `cifs/machine`, `host/machine`)

To remediate, you would need to purge Kerberos tickets immediately by running (on the target computer)

```
klist purge
```

This clears the Kerberos ticket cache from memory, forcing a reauthentication — which will now fail if the account is deleted.

You could also consider setting shorter ticket lifetimes (note this will not prevent the behavior you're seeing - but lower its potential impact)

In GPO:

```
Computer Configuration → Policies → Windows Settings → Security Settings → Account Policies → Kerberos Policy
```

Recommendations for tighter security:

-  Maximum lifetime for user ticket (TGT): 4 hours or less

-  Maximum lifetime for service ticket: 2 hours

-  Enforce user logoff after logon hours expire: Enabled

Lower values reduce exposure if a privileged account is deleted or compromised.

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
