---
title: Special Identity Groups
type: entity
domain: active-directory
slug: special-identity-groups
summary: Special identity groups are OS-managed, dynamic groups whose membership you cannot directly modify; they represent access contexts (Everyone, Authenticated Users, Interactive, Network, etc.) and carry well-known SIDs that remain constant across all Windows installations.
sources:
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-special-identities-groups (Microsoft Learn — Special Identity Groups, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-principals (Microsoft Learn — Security Principals, fetched 2026-06-18)
provenance_extracted: 16
provenance_inferred: 2
provenance_ambiguous: 1
tags: [directory-services, ad-authn, concept]
status: draft
updated: 2026-06-18
---

# Special Identity Groups

**Special identity groups are built-in, OS-controlled groups whose membership automatically reflects the current sign-in context of each user; you can assign permissions or user rights to them but you cannot directly view or modify their member lists.**

## Key Groups

| SID | Name | Who is in it |
|---|---|---|
| S-1-1-0 | **Everyone** | All interactive, network, dial-up, and authenticated users (see caveat re: Anonymous below) |
| S-1-5-11 | **Authenticated Users** | Any principal that authenticated through a sign-in process; excludes Guest even if Guest has a password |
| S-1-5-4 | **Interactive** | Users logged on locally to the system |
| S-1-5-2 | **Network** | Users accessing the system over the network; access tokens for interactive users do not contain this SID |
| S-1-5-14 | **Remote Interactive Logon** | Users connected via RDP; is a subset of Interactive (both SIDs appear in the token) |
| S-1-5-3 | **Batch** | Principals running as scheduled tasks / batch queue |
| S-1-5-6 | **Service** | All security principals signed in as a service |
| S-1-5-7 | **Anonymous Logon** | Users who connected without supplying credentials |
| S-1-5-9 | **Enterprise Domain Controllers** | All DCs in the forest; OS-controlled |
| S-1-5-18 | **SYSTEM (LocalSystem)** | OS and services running as LocalSystem; hidden Administrators member; uses computer domain account on the network |
| S-1-5-19 | **LocalService** | Services with no need for extensive local access; accesses network as anonymous |
| S-1-5-20 | **NetworkService** | Services needing authenticated network access; accesses network as the computer account |
| S-1-3-0 | **Creator Owner** | Placeholder SID in inheritable ACEs; replaced at inheritance time with the current owner's SID |
| S-1-3-1 | **Creator Group** | Placeholder SID; replaced at inheritance with the owner's primary group SID (POSIX subsystem) |
| S-1-5-10 | **Principal Self** | Placeholder in ACEs on AD user/group/computer objects; replaced during access check with the object's own SID — used to grant objects rights over themselves |
| S-1-5-12 | **Restricted** | Added to tokens of processes running in restricted security contexts (e.g. software restriction policies) |
| S-1-5-15 | **This Organization** | Users from the same AD organisation; added only by domain controllers |
| S-1-5-17 | **IUSR** | IIS anonymous authentication account (replaces legacy IUSR_MachineName since IIS 7) |

## Group Scope and Membership

Group scopes do not apply to special identity groups. The OS assigns users to these groups dynamically based on how they authenticate or what context they run in — you cannot manage membership via Active Directory Users and Computers. You can, however, place special identity groups in ACEs (DACLs/SACLs) or in user-rights assignments in Group Policy. (inferred — the source states that scopes do not apply and membership cannot be modified, but does not explicitly describe how GPO assignment works with them.)

## Service Account Identities

LocalSystem, LocalService, and NetworkService are not interactive user accounts — they are OS-managed identities for service processes:

- **LocalSystem** has full local privileges and uses the machine's domain identity on the network; do not run services as LocalSystem on domain controllers because it grants access to the entire domain.
- **LocalService** has Users-level local access; accesses network resources as an anonymous session.
- **NetworkService** has Users-level local access; accesses network resources using the computer account credentials (same network identity as LocalSystem, but reduced local privileges).

## Contradictions / caveats
- **Everyone vs. Anonymous Logon**: On Windows 2000 and earlier, Anonymous Logon was a default member of Everyone. Starting with Windows Server 2003, Anonymous Logon is excluded from Everyone by default. The old behaviour can be restored via the `everyoneincludesanonymous` DWORD (`HKLM\SYSTEM\CurrentControlSet\Control\Lsa`, value 1). This is an ambiguous area — policies written for pre-2003 that relied on Everyone to cover anonymous access will silently fail on modern systems.
- Anonymous Logon is different from the IIS IUSR account: IUSR is a real account with a password that IIS uses for "anonymous" web access; that user is therefore a member of Authenticated Users, not Anonymous Logon.

## Reference notes
- [[ad-ds-understand-special-identities-groups]]
- [[ad-ds-understand-security-principals]]

## See also
- [[security-principals]]
- [[security-identifiers-sid]]
- [[security-groups]]
- [[securing-active-directory]]
