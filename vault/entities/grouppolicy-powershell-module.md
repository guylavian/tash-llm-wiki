---
title: GroupPolicy PowerShell Module (New-GPO / New-GPLink / Item-Level Targeting)
type: entity
domain: powershell
slug: grouppolicy-powershell-module
summary: The GroupPolicy module scripts GPO creation, linking, and even bulk item-level targeting cleanly — but several everyday GPO tasks (Group Policy Preference printer actions, ADMX multi-value list-boxes, DNS-client Administrative Template values) have no first-class cmdlet, and community answers consistently redirect to the GPMC GUI instead.
sources:
  - "web:https://learn.microsoft.com/en-us/answers/questions/1080500/gpo-printer-tcp-ip-change-from-create-to-replace (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1082671/how-to-script-gpo-multi-dns-ips-to-server-farm (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1234067/configure-gpo-item-level-targeting-in-powershell-i (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/110026/add-multiple-urls-on-gpo-configuration-box (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1371108/how-to-disable-and-enableusb-on-one-gpo (Microsoft Q&A, fetched 2026-07-25)"
  - "web:https://learn.microsoft.com/en-us/answers/questions/1181731/adding-and-showing-active-directory-sites-in-gp-ma (Microsoft Q&A, fetched 2026-07-25)"
provenance_extracted: 6
provenance_inferred: 2
provenance_ambiguous: 1
tags: [ps-modules, troubleshooting]
status: draft
updated: 2026-07-25
---

# GroupPolicy PowerShell Module (New-GPO / New-GPLink / Item-Level Targeting)

**`Import-Module GroupPolicy` scripts GPO creation and linking (`New-GPO`, `New-GPLink`, `Get-GPO`) and bulk item-level targeting (`New-GPItemLevelTargetingComputerItem` + `Add-GPItemLevelTargetingEntry`) — but several everyday GPO tasks (per-preference-item printer actions, ADMX multi-value list-boxes, DNS-client template values) have no first-class cmdlet, and community answers keep redirecting to the GPMC GUI.**

## Community Q&A (upstream)

### Creating and linking GPOs: New-GPO / New-GPLink
Thread 1181731's own script shows the idiomatic pattern: `New-GPO -Name "Home"` then `Get-GPO -Name "Home" | New-GPLink -Target "dc=home,dc=lab" -LinkEnabled Yes -Enforced Yes -ErrorAction Stop`, repeated per site/OU/domain target DN. The thread's actual question, though, was about a **GPMC UI toggle** — showing linked-GPO info against an AD site in the console tree — which a **Microsoft Moderator** (a stronger-weight answerer than an anonymous community reply) answered as GUI-only ("Click on show sites, then select target site"): scripting the link itself is fully cmdlet-covered, but surfacing that link under **Sites** in the GPMC snap-in tree is a view setting `New-GPLink` doesn't control or expose.

### Bulk item-level targeting IS cmdlet-covered — correcting the premise
Thread 1234067 shows item-level targeting for registry Group Policy Preference entries **does** have real cmdlets: `New-GPItemLevelTargetingComputerItem -ComputerName <list> -LogicalOperator Or` builds a targeting object, and `Add-GPItemLevelTargetingEntry -Name <GPOName> -Target <that object> -ItemLevelTarget "Registry" -RegistryKey <key>` attaches it to a specific GPP entry. The poster's script failed with `Index operation failed; the array index evaluated to null` from `$ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.IndexOf($RegistryKey)]]` *(inferred — this is a hashtable-indexing bug: positionally indexing a hashtable's `.Keys`/`.Values` collections isn't reliable the way the script assumes)*, not a cmdlet limitation. No working fix was posted in-thread (2 upvotes, no accepted answer).

### Printer GPP create→replace: no cmdlet path surfaced
Thread 1080500: changing ~400 printer-connection Group Policy Preference items from **Create** action to **Replace** (temporarily, then back) got no PowerShell/module answer across 3 replies. Community consensus (unaccepted, from Q&A Users) was that this is a GUI/GPP-console task — one reply explicitly pushes back on scripting it at all ("GPO's are centralized so making a change should be easy to accomplish using the GUI ... this is going to be a change in the Group Policy Preference"). No `GroupPolicy`-module action-flip primitive for printer GPP items is offered anywhere in the thread.

### DNS-client and ADMX list-box settings: the same GUI-only pattern
Thread 1082671 (pushing 4 DNS server IPs to a server farm) gets routed to **Computer Configuration > Policies > Administrative Templates > Network > DNS Client**, setting multiple space-separated IPs in that one box — no `GroupPolicy`-module cmdlet is offered for writing that Administrative Template value. Thread 110026 (importing 1,100+ URLs into an Edge cookie-exception ADMX list-box) gets the same answer twice: the list-box UI only accepts entries "one at a time," and a community reply states there's no ADDS-forum-sanctioned bulk/import script for it, redirecting to the general Windows Server PowerShell forum instead. No `GroupPolicy`-module cmdlet populates a multi-value ADMX list-box in bulk in either thread; doing that has to go through the underlying registry values directly via a startup/logon script *(inferred — both threads confirm the gap but neither states the registry-script workaround explicitly)*.

### USB policy precedence: unresolved in-thread
Thread 1371108: two GPOs (`DisableUSB` for "Authenticated Users", `EnableUSB` scoped to specific users) — the exception GPO isn't taking effect for the intended users. The single answer only links a Windows Server 2008 R2-era TechNet article (its title/content was never fetched into this corpus, so its subject is (inferred) from the URL), with no PowerShell content and no explanation of why the more specific GPO isn't winning (link order, OU precedence, and whether both GPOs even target the same OU are all unaddressed). This is an open gap in the corpus, not a resolved precedence rule.

## Contradictions / caveats
- **The premise this page started from — that bulk item-level targeting has "no clean cmdlet" — is wrong.** Thread 1234067 shows cmdlets exist (`New-GPItemLevelTargetingComputerItem`, `Add-GPItemLevelTargetingEntry`); the real problem there was a scripting bug in the poster's own hashtable-indexing logic, not a module gap. **(ambiguous → resolved against the original premise; recorded here so a future reader doesn't re-file the same wrong claim.)**
- Threads 1080500, 1082671, 110026, and 1371108 all end without an accepted answer or any PowerShell-module solution — treat "no cmdlet exists for this" as this corpus's current state, not a confirmed permanent product limitation.

## See also
- [[active-directory-powershell-cmdlets]]
- [[gpo-script-deployment-troubleshooting]]
- [[powershell-modules]]
