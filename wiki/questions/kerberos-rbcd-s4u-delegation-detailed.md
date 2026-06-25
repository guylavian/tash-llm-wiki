---
title: Kerberos RBCD / S4U detailed — NTLM front-end, protocol transition, and the delegation authority shift
type: question
domain: active-directory
slug: kerberos-rbcd-s4u-delegation-detailed
summary: "Deep dive into Resource-Based Constrained Delegation (RBCD): how S4U2Self+S4U2Proxy overcome NTLM front-end auth without TRUSTED_TO_AUTH_FOR_DELEGATION, why RBCD's S4U2Proxy succeeds with a non-forwardable evidence ticket when classic constrained delegation fails, and the security implications of delegating authority to the resource owner."
sources:
  - ref:wiki/reference/active-directory/ad-ds-configure-kerberos-delegation-group-managed-service-accounts.md
  - ref:wiki/reference/active-directory/ad-ds-delegated-managed-service-accounts-overview.md
  - ref:wiki/reference/active-directory/ad-ds-schema-updates.md
  - ref:wiki/reference/keycloak/rhbk-26-4-configuring-authentication-server-administration-guide.md
  - web:https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/ (MS-SFU: Kerberos Protocol Extensions — Service for User and Constrained Delegation Protocol, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/ (MS-ADTS: Active Directory Technical Specification, fetched 2026-06-18)
  - web:https://datatracker.ietf.org/doc/rfc4120/ (RFC 4120 — The Kerberos Network Authentication Service V5, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview (Kerberos Authentication Overview, fetched 2026-06-18)
provenance_extracted: 8
provenance_inferred: 5
provenance_ambiguous: 0
tags: [federation]
status: reviewed
updated: 2026-06-18
---

# Kerberos RBCD / S4U detailed — NTLM front-end, protocol transition, and the delegation authority shift

**The scenario:** A web service running as gMSA `FE$` on Server A needs to access a SQL backend on Server B running as `BE$`, in the *caller's identity*. Resource-Based Constrained Delegation (RBCD) is configured: `BE$`'s `msDS-AllowedToActOnBehalfOfOtherIdentity` security descriptor grants `FE$` the right to act on behalf of others. The user authenticates to FE via NTLM (e.g. smart-card logon without Kerberos). FE has **no** `TRUSTED_TO_AUTH_FOR_DELEGATION` flag ("Use any authentication protocol").

## 1. Can FE obtain a service ticket to BE in the user's identity? Which S4U extensions and in what order?

**Yes.** FE can obtain a service ticket (TGS) to BE in the user's identity — this is precisely the scenario Resource-Based Constrained Delegation (RBCD) was designed to solve. The protocol extensions involved are:

### The S4U extensions — the order of operations

**S4U2Self (Service-for-User-to-Self)** — first call:

1. FE uses its own gMSA TGT to request a service ticket from the KDC *to itself* (FE's SPN), but **for the user's identity**.
2. The KDC issues a "service ticket to self" — a ticket that maps to FE but carries the user's authorization data. Despite NTLM on the front end, the KDC has enough information (FE supplies the user's name and realm) to look up the user and produce this ticket.
3. This is the **protocol transition** step: it bridges a non-Kerberos authentication mechanism into the Kerberos ticket world.
4. **Without `TRUSTED_TO_AUTH_FOR_DELEGATION`**, the S4U2Self response includes a `FORWARDABLE` flag set to **false** on the resulting ticket — the ticket is not marked forwardable. (inferred: per MS-SFU, the KDC sets forwardable=false on S4U2Self responses when the requesting account lacks `TRUSTED_TO_AUTH_FOR_DELEGATION`; the forwardable flag on the evidence ticket is what the classic constrained-delegation KDC logic uses to decide whether the user "consented" to delegation.)

**S4U2Proxy (Service-for-User-to-Proxy)** — second call:

1. FE presents the S4U2Self-obtained ticket (non-forwardable, the "evidence ticket") to the KDC and requests a service ticket to BE's SPN on behalf of the user.
2. The KDC checks the authorization: does FE have the right to request delegation to BE?
3. Under **RBCD**, the KDC checks **BE's `msDS-AllowedToActOnBehalfOfOtherIdentity`** security descriptor — a binary ACL stored on the target computer object.
4. If FE is listed in that SD with the `ACCESS_ALLOWED` ACE for the `CR_ACT_AS_USER` right (control access right 5e1b0535-c2bb-44b9-9c08-43fb7fed8a42), the KDC issues a service ticket to BE carrying the user's identity. (inferred: MS-ADTS §3.1.1.5.3 documents the KDC behavior — the `msDS-AllowedToActOnBehalfOfOtherIdentity` SD is consulted; additional 2012+ KDC behavior.)

### Key difference from classic constrained delegation

In **classic constrained delegation** (with protocol transition), FE would need `TRUSTED_TO_AUTH_FOR_DELEGATION` (UAC bit `0x1000000` / 16777216) set on its account — and the `msDS-AllowedToDelegateTo` attribute listing BE's SPNs. Without that flag, S4U2Self returns a non-forwardable ticket and S4U2Proxy refuses it. The vault's reference note on configuring Kerberos delegation for gMSA documents the flag precisely: `Set-ADAccountControl -TrustedToAuthForDelegation $true` enables "Kerberos-constrained delegation with protocol transition" and sets the `TRUSTED_TO_AUTH_FOR_DELEGATION` bit in `userAccountControl`. (extracted: ad-ds-configure-kerberos-delegation-group-managed-service-accounts.md, lines 58–64)

**Under RBCD, `TRUSTED_TO_AUTH_FOR_DELEGATION` is not required** because the delegation authorization lives on the **target** (BE), not on the requestor (FE).

---

## 2. Why does RBCD's S4U2Proxy succeed with a non-forwardable evidence ticket when classic constrained delegation fails?

The answer lies in the **different KDC code paths** for the two delegation models:

### Classic constrained delegation (pre-2012)

- The KDC looks at the **requesting account (FE)**:
  1. Does FE have `msDS-AllowedToDelegateTo` with BE's SPN?
  2. Is FE `TRUSTED_TO_AUTH_FOR_DELEGATION` (protocol transition) OR does the user's original TGS have the `TGT_FLG_FORWARDABLE` flag?
- The KDC enforces the Kerberos chain-of-forwards rule: a delegation operation must be traceable back to a user-authenticated, forwardable TGT. This protects the user by requiring their explicit Kerberos participation (or an admin-granted `TRUSTED_TO_AUTH_FOR_DELEGATION` exemption).
- If the evidence ticket is non-forwardable (as from S4U2Self without `TRUSTED_TO_AUTH_FOR_DELEGATION`) and no user TGS exists (NTLM auth), the KDC **rejects** the S4U2Proxy request.
- This is consistent with the Kerberos protocol definition: RFC 4120 §5.4 defines the `FORWARDABLE` flag; delegation (TGS-REQ with `KDC_OPT_FORWARDED`) requires a forwardable TGT. (web:RFC 4120)

### Resource-Based Constrained Delegation (Windows Server 2012+)

- The KDC looks at the **target account (BE)**:
  1. Does BE's `msDS-AllowedToActOnBehalfOfOtherIdentity` include FE (direct SID or group membership)?
  2. Does the requesting account have proof of possession of its own TGT? (FE presents its gMSA-authenticated TGT.)
- **The forwardable flag on the evidence ticket is NOT checked** — the authorization comes from the target's security descriptor, not from the forwardable chain.
- Per MS-SFU §3.2.5.2 (KDC processing of S4U2Proxy), under RBCD the forwardable check is replaced by the `msDS-AllowedToActOnBehalfOfOtherIdentity` access check. (inferred: MS-SFU documents this difference explicitly for the S4U2Proxy extended KDC reply.)

**Why this works securely:** The target resource's owner (the BE administrator) has explicitly delegated the right to FE. The KDC trusts this owner-side authorization more than the forwardable chain — the principle is that the resource owner controls who can authenticate *as someone else to its service*. The forwardable requirement was a surrogate for the user's consent; under RBCD, the resource owner's consent replaces it.

### Concrete illustration

| Factor | Classic constrained delegation | Resource-Based Constrained Delegation |
|--------|-------------------------------|--------------------------------------|
| Who configures | Domain admin (on FE via `msDS-AllowedToDelegateTo`) | Resource owner (on BE via `msDS-AllowedToActOnBehalfOfOtherIdentity`) |
| S4U2Self | Forwardable ticket only if `TRUSTED_TO_AUTH_FOR_DELEGATION` set | Non-forwardable ticket returned (always); forwardable not needed |
| S4U2Proxy evidence ticket | MUST be forwardable | Forwardable not required |
| If user auth'd via NTLM | Requires `TRUSTED_TO_AUTH_FOR_DELEGATION`, else fails | Works — S4U2Self bridges protocol gap, RBCD authorizes the target |

---

## 3. Who controls delegation — RBCD vs. classic — and why is it both more secure and an attack vector?

### Who controls the delegation permission

**Classic constrained delegation:**
- Configured on the **front-end service account** (FE) via:
  - `userAccountControl` — the `TRUSTED_TO_AUTH_FOR_DELEGATION` bit (for protocol transition)
  - `msDS-AllowedToDelegateTo` — the list of SPNs FE may delegate to
- Requires the **SeEnableDelegationPrivilege** user right — by default only Domain Admins and Enterprise Admins can set delegation on an account.
- Centralized model: the domain admin decides for all resources which front-ends they trust.

**Resource-Based Constrained Delegation:**
- Configured on the **backend resource account** (BE) via:
  - `msDS-AllowedToActOnBehalfOfOtherIdentity` — a security descriptor (SD) listing which accounts may act on behalf of others to this resource
- Requires only **`WriteProperty` on `msDS-AllowedToActOnBehalfOfOtherIdentity`** — a right that can be delegated to the BE administrator (e.g. the SQL server admin).
- Decentralized model: the resource owner decides who may delegate to *their* resource.

The vault notes confirm the attribute's purpose: the schema definition at `ad-ds-schema-updates.md:4772` states: *"This attribute is used for access checks to determine if a requester has permission to act on the behalf of other identities to services running as this account."* (extracted: ad-ds-schema-updates.md, line 4772)

The dMSA migration documentation also shows that `msDS-AllowedToActOnBehalfOfOtherIdentity` is a security-critical attribute that gets copied during service account migration — reinforcing its role as the delegation authorization anchor. (extracted: ad-ds-delegated-managed-service-accounts-overview.md, line 83)

### Why RBCD is considered **more secure**

1. **Least-privilege delegation:** The BE admin (who knows BE's security requirements best) decides which front-ends can delegate, without needing Domain Admin authority.
2. **Principle of resource autonomy:** A compromised FE can only delegate to resources whose owners explicitly authorized it. Under classic delegation, a compromised FE can delegate to every service listed in its `msDS-AllowedToDelegateTo` — but that list could be broad.
3. **Reduced attack surface for delegation misconfigurations:** Classic delegation requires an account to hold the `TRUSTED_TO_AUTH_FOR_DELEGATION` bit, which is a high-privilege/promiscuous setting (it enables protocol transition for ALL constrained delegation targets). RBCD eliminates this binary bypass — the authorization is per-resource.
4. **No global flag needed:** Since the authorization is at the target, the front-end service never needs `TRUSTED_TO_AUTH_FOR_DELEGATION`, which reduces the risk of a front-end being able to perform protocol transition to *any* backend if `msDS-AllowedToDelegateTo` is misconfigured.

### Why RBCD is a **known attack vector**

RBCD abuse is a well-documented Active Directory attack path:

1. **Attack pre-condition:** The attacker gains `GenericWrite`, `GenericAll`, `AllExtendedRights`, or `WriteProperty` on a target computer object (`BE$` in AD). This can happen through ACL misconfigurations, insecure delegation, vulnerable group memberships, or by exploiting the default `Add/Remove self as member` ACE that certain accounts inherit.

2. **Attack sequence:**
   - The attacker creates or controls a computer account (or uses an existing machine account they have the password/credentials for).
   - They write the controlled account's SID into `BE$`'s `msDS-AllowedToActOnBehalfOfOtherIdentity` security descriptor.
   - They call S4U2Self from the controlled machine to get a service ticket for any user (e.g. a Domain Admin) to themselves.
   - They call S4U2Proxy to get a service ticket to BE's SPN in the DA's identity.
   - They use that ticket to access BE with Domain Admin privileges.

3. **Why it's dangerous:** Because RBCD eliminates the `TRUSTED_TO_AUTH_FOR_DELEGATION` requirement, any attacker with write access to a computer's `msDS-AllowedToActOnBehalfOfOtherIdentity` can impersonate any user (including Domain Admins) to that computer. The attack is detectable by BloodHound (edge `AllowedToDelegate`) and by monitoring changes to `msDS-AllowedToActOnBehalfOfOtherIdentity` (Event ID 5136 on the attribute).

This dual nature — both a security improvement (decentralized resource authorization) and an attack surface — makes RBCD one of the most important delegation concepts to understand for AD security practitioners.

---

## Contradictions / caveats

- The vault's harvested reference notes contain the classic delegation configuration (userAccountControl flags, msDS-AllowedToDelegateTo) and the schema definition of msDS-AllowedToActOnBehalfOfOtherIdentity, but do **not** contain the detailed MS-SFU protocol specification for S4U2Self/S4U2Proxy KDC processing rules. The fine-grained protocol behavior (e.g., the exact KDC code-path separation between classic and resource-based delegation, the forwardable-skip rule for RBCD) is drawn from the MS-SFU and MS-ADTS Open Specifications and from RFC 4120. These `web:` sources are authoritative for the protocol mechanics.
- The RBCD attack vector described above is a well-known AD security finding documented in MITRE ATT&CK (T1558.003 — "Kerberoasting: Steal or Forge Tickets: Kerberos Delegation Abuse") and in the BloodHound attack-path catalog. The vault does not currently have a dedicated page on AD attack paths; this is flagged as a coverage gap.

## See also
- [[service-accounts-overview]] — gMSA, sMSA, dMSA, virtual accounts
- [[group-managed-service-accounts]] — gMSA lifecycle, KDS root key, SPN management
- [[delegated-managed-service-accounts]] — dMSA, Credential Guard binding, msDS-AllowedToActOnBehalfOfOtherIdentity
- [[active-directory-implementation-review]] — AD DS health evaluation lens
- [[securing-active-directory]] — AD defense model, reducing attack surface
- [[monitoring-ad-for-compromise]] — event log monitoring for AD compromise (RBCD abuse via 5136 monitoring)
- [[protected-accounts-and-groups]] — AdminSDHolder, Protected Users group
- [[credential-theft-and-attractive-accounts]] — Kerberoasting, pass-the-ticket, delegation abuse
- [[windows-server-identity-coverage-gaps]] — which AD topics are synthesized vs. raw-only

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)

- **ad-ds-configure-kerberos-delegation-group-managed-service-accounts.md** — Configuring Kerberos Delegation for Group Managed Service Accounts. Documents the `TRUSTED_TO_AUTH_FOR_DELEGATION` userAccountControl flag for protocol transition, classic delegation types (unconstrained, constrained, constrained+protocol transition), and the `msDS-AllowedToDelegateTo` attribute. Source: Microsoft Learn (Windows Server gMSA docs).
- **ad-ds-delegated-managed-service-accounts-overview.md** — Delegated Managed Service Accounts overview (Windows Server 2025). References `msDS-AllowedToActOnBehalfOfOtherIdentity` security descriptor being copied during dMSA migration. Source: Microsoft Learn.
- **ad-ds-schema-updates.md** — AD DS Schema Updates. Contains the full attributeSchema definition for `msDS-AllowedToActOnBehalfOfOtherIdentity`: attributeId `1.2.840.113556.1.4.2182`, description *"used for access checks to determine if a requester has permission to act on the behalf of other identities to services running as this account"*. Source: Microsoft Learn.
- **rhbk-26-4-configuring-authentication-server-administration-guide.md** — RHBK server administration guide section 8.5.4. Documents Keycloak's Kerberos credential delegation support, the `gss delegation credential` protocol mapper, and the requirement to "Configure forwardable Kerberos tickets in krb5.conf". Source: Red Hat RHBK 26.4 documentation.

### Wiki / upstream (`web:`)

- **MS-SFU** — *Kerberos Protocol Extensions: Service for User and Constrained Delegation Protocol*. Microsoft Open Specifications. Defines S4U2Self (sections 3.2.4, 3.2.5) and S4U2Proxy (sections 3.2.6, 3.2.7), the forwardable-ticket requirement for classic S4U2Proxy, and the alternative RBCD authorization path using `msDS-AllowedToActOnBehalfOfOtherIdentity`.
- **MS-ADTS** — *Active Directory Technical Specification*. Microsoft Open Specifications. Section 3.1.1.5.3 defines the KDC access check against the target computer's `msDS-AllowedToActOnBehalfOfOtherIdentity` security descriptor.
- **RFC 4120** — *The Kerberos Network Authentication Service V5*. IETF. Defines the `FORWARDABLE` flag (§5.4), TGT delegation semantics (§5.4.1), and the standard KDC processing rules.
- **Kerberos Authentication Overview** — Microsoft Learn. Overview of Windows Kerberos implementation, service tickets, delegation models, and gMSA support.
