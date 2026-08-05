---
title: "Query on LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5828405/query-on-ldap
question_id: 5828405
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Query on LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5828405/query-on-ldap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I am facing an issue with LDAP queries on macOS when retrieving Active Directory group memberships.

I have both a Windows and a macOS device. On Windows, when I query a user’s group memberships against a domain controller using PowerShell (Get-ADPrincipalGroupMembership), I get the expected count. To my knowledge, this cmdlet does not rely solely on a basic LDAP query and is able to resolve nested group memberships.

However, when I perform an LDAP search from macOS for the same user, I receive fewer group memberships. For example, Windows returns around 150 groups, whereas macOS returns only about 100. I suspect that macOS is not retrieving all nested group memberships, but I am not entirely sure.

Is there any limitation or default restriction in LDAP queries from macOS (such as size limits, lack of paging, or attribute constraints) that could cause this discrepancy?Any guidance would be appreciated.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-25*

Hello Glenn Maxwell,

I’m following up to check whether the issue has been resolved. Feel free to reply if you need further information. If the information provided was helpful, please click "Accept Answer" to help others in the community. Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-19*

The discrepancy is most likely caused by server‑side LDAP limits on how many values of a multivalued attribute (such as `memberOf`) a domain controller will return in a single response, not by a macOS‑specific client limit.

On modern Windows Server domain controllers, LDAP behavior is governed by LDAP policy settings such as:

-  `MaxPageSize` – limits the number of objects returned in a search result page.

-  `MaxValRange` – limits how many values of a multivalued attribute are returned.

For large groups or users with many group memberships, `MaxValRange` is particularly important. If the number of group memberships exceeds this limit, the domain controller returns only up to that many values for the attribute, and the rest are effectively truncated in the LDAP response.

The article on LDAP responses from Windows Server 2008 and newer domain controllers shows an example LDAP policy configuration:

```
MaxPageSize 50000
MaxValRange 25000
```

If these values are lower (or if other LDAP policy limits are in effect), an LDAP client such as the one on macOS that simply reads `memberOf` (or does a straightforward LDAP search) will only see the subset of memberships that the DC returns.

By contrast, `Get-ADPrincipalGroupMembership` on Windows does not just read the raw `memberOf` attribute. It uses Active Directory logic to resolve nested group memberships and can perform multiple queries and server‑side expansion, so it often returns more complete results than a single basic LDAP query.

Key points for the behavior observed:

-  Windows PowerShell cmdlets (like `Get-ADPrincipalGroupMembership`) use AD Web Services and directory APIs that:

-  Resolve nested group memberships.

-  Are not limited to a single `memberOf` read.

-  A basic LDAP search from macOS:

-  Reads only what the DC returns in the LDAP response.

-  Is subject to LDAP policy limits such as `MaxValRange` and `MaxPageSize`.

-  Does not automatically expand nested groups unless explicitly implemented in the client logic.

To investigate and mitigate:

-  Check LDAP policy on a domain controller using `ntdsutil` (as described in the referenced article) and verify values for `MaxPageSize` and `MaxValRange`.

-  If necessary and appropriate for the environment, adjust these LDAP policy values so that the DC can return all group memberships for heavily nested or highly populated accounts.

-  Ensure the macOS LDAP query logic accounts for nested groups if the goal is to match `Get-ADPrincipalGroupMembership` behavior; this typically requires additional queries or server‑side controls beyond a single attribute read.

References:

-  Windows Server 2008 and newer domain controller returns only 5000 values in an LDAP response

-  When you run an LDAP query against a domain controller, you obtain a partial attribute list

-  Performing an Attribute Scope Query
