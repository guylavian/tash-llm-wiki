---
title: Active Directory PowerShell Cmdlets (Get-AD* / Set-AD* / ADDSDeployment)
type: entity
domain: powershell
slug: active-directory-powershell-cmdlets
summary: Community Q&A threads on the ActiveDirectory module's everyday cmdlets — bulk export with Get-ADUser/Get-ADGroup/Get-ADGroupMember, Get-ADDefaultDomainPasswordPolicy — plus real edges the module has no clean answer for: a Set-ADUser attribute-write gap, no cmdlet for ACL-inheritance "restore defaults," and an ADDSDeployment backtick line-continuation parsing gotcha.
sources:
  - "web:https://learn.microsoft.com/en-us/answers/questions/1051244/set-attribute-in-active-directory (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1062825/active-directory-inheritence-disabled (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1091891/on-premises-active-directory (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1155936/import-active-directory-and-connect-aad (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1179551/the-term-sysvolpath-is-not-recognized (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1187539/ldap-query-in-powershell-to-check-all-windows-clie (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 6
provenance_inferred: 2
provenance_ambiguous: 1
tags: [ps-modules, troubleshooting]
status: draft
updated: 2026-07-25
---

# Active Directory PowerShell Cmdlets (Get-AD* / Set-AD* / ADDSDeployment)

**The `ActiveDirectory` module's `Get-ADUser`/`Get-ADGroup`/`Get-ADComputer`/`Get-ADGroupMember`/`Get-ADDefaultDomainPasswordPolicy` cover bulk read/export and membership queries well, but community Q&A surfaces real edges: `Set-ADUser` can't write every attribute, there's no cmdlet for resetting ACL inheritance to defaults, and `ADDSDeployment`'s cmdlets are unusually sensitive to backtick line-continuation formatting.**

## Community Q&A (upstream)

### Bulk export: Get-ADUser / Get-ADGroup / Get-ADGroupMember
Community answers to "export all AD users to CSV" converge on the same shape (threads 1091891, 1155936): `Get-ADUser -Filter * -SearchBase '<OU DN>' -Properties <list> | Select-Object <list> | Export-Csv <path> -Encoding unicode -NoTypeInformation`, scoped per-OU with a `$ouList` array piped through a `ForEach`. The same pattern enumerates groups (`Get-ADGroup -Filter * -SearchBase ...`), and group membership is pulled by piping each group through `Get-ADGroupMember` (`$groupmember = foreach ($group in $grouplist) { Get-ADGroup $group | Get-ADGroupMember }`). One answer in 1091891 links directly to the `Get-ADGroupMember` reference page as the authoritative doc.

### Get-ADDefaultDomainPasswordPolicy for expiry math
Thread 1155936's script calls `(Get-ADDefaultDomainPasswordPolicy).MaxPasswordAge.Days` once, then computes each user's expiration as `(Get-Date $_.PasswordLastSet).AddDays($maxPassAge)`. The cmdlet returns the **domain-wide default** password policy object only — it says nothing about whether a given user is instead covered by a [[fine-grained-password-policies]] PSO with a different max age, which would make the expiry math wrong for that user *(inferred — fine-grained policies aren't mentioned in this thread; this is the module's documented scope, not a claim the thread makes)*.

### Set-ADUser's attribute-write gap
Thread 1051244 (three answers, none accepted) is a community member reporting that a particular attribute — described only as "a Configuration Object from Domain Controller" — could not be set with `Set-ADUser`; the other answer just links the `Set-ADUser` docs page without addressing why that specific attribute failed. **(ambiguous)** — the thread never identifies which attribute, so whether this is a read-only/constructed attribute, a wrong-object-class attempt, or a genuine `Set-ADUser` limitation is not resolvable from this material. Treat "`Set-ADUser` can't write every attribute" as real but under-specified — not a confirmed list of exceptions.

### No cmdlet for restoring default ACL inheritance
Thread 1062825 (zero answers) asked for a scriptable way to re-enable ACL inheritance on an OU and have permissions actually reset — the poster found that, in the GUI (Advanced Security Settings), re-enabling inheritance additionally requires clicking **"Restore defaults"** before permissions actually reset, and turned up no cmdlet or module automating that step. No answer in the thread contradicts this, so it stands as a documented capability gap in this corpus — not a vendor-confirmed absence, since nobody authoritative weighed in.

### ADDSDeployment / Install-ADDSDomainController backtick gotcha
Thread 1179551 shows `Install-ADDSDomainController` called across many backtick (`` ` ``)-continued lines; the reported errors were `-SiteName` and then `-SysvolPath` "is not recognized as the name of a cmdlet." That is the classic symptom of a broken line continuation — a stray trailing character (usually whitespace) after a backtick ends the logical line early, so the next `-Param` token parses as a brand-new, unrecognized command. The one (unaccepted) community answer suggests reordering parameters to bisect the broken line and retyping the script in a different editor to strip invisible characters; no root cause was confirmed in-thread, but "trailing character after backtick" is the standard cause of this exact error shape *(inferred from the error pattern, not asserted as fact by the answerer)*.

### Get-ADComputer -LDAPFilter doesn't show live LDAP bind activity
Thread 1187539: `Get-ADComputer -LDAPFilter "(&(objectClass=computer)(lastLogonTimestamp>=1))"` was proposed to find which computers are currently authenticating via LDAP (ahead of an LDAP-to-LDAPS migration). A community answer states plainly: "The AD won't have the information you're looking for" — `Get-ADComputer`/LDAP filters query object *attributes*, not live bind/auth telemetry — and redirects to DC security-event-log auditing instead (the thread says only "the security log"; the Directory Service Access subcategory is (inferred)), warning that log fills up fast once LDAP-bind auditing is enabled.

## Contradictions / caveats
- Thread 1051244 never resolves which attribute `Set-ADUser` rejected — filed as **(ambiguous)**: a real gap exists, but its exact scope isn't corpus-confirmed.
- Thread 1062825 and other zero-answer/unaccepted-answer threads in this corpus skew this page toward unresolved "has anyone hit this" reports rather than confirmed fixes — weaker evidence than an accepted or Microsoft-affiliated answer. None of the answerers here carry a Microsoft/MVP affiliation tag.

## See also
- [[grouppolicy-powershell-module]]
- [[gpo-script-deployment-troubleshooting]]
- [[powershell-modules]]
- [[powershell-pipeline-and-objects]]
