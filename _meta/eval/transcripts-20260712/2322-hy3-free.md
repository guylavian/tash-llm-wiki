# opencode session ses_0a800e588ffe1x6FSD5l0AbCIl — 2026-07-12 23:22
model: hy3-free

## USER
Answer this question from the wiki: **We're rolling out Windows LAPS on our domain-joined servers this quarter.
Where does LAPS store the managed local admin password in AD, which schema
attributes are involved, and what should we monitor to verify rotation is
actually happening? **

Run the mechanized QUERY pipeline first — it routes, retrieves, graph-expands,
gates, and synthesizes in one shot (orchestrated through the LangGraph StateGraph
by default; degrades to the same nodes linearly when langgraph is absent):

- Preferred: call the `wikikb` MCP tool `ask` with the question (add `domain`
  and `tier` when known).
- CLI equivalent: `PYTHONPATH=_meta _meta/.venv-online/bin/python -m wikikb ask
  "We're rolling out Windows LAPS on our domain-joined servers this quarter.
Where does LAPS store the managed local admin password in AD, which schema
attributes are involved, and what should we monitor to verify rotation is
actually happening? " --json` (plain `python3` also works — linear fallback; check the
  `orchestrator` field).

If the returned answer is thin or extractive, deepen it per "Operation: QUERY"
in `CLAUDE.md` (repo root = vault root): read `index.<domain>.md` + candidate
pages' `title:`/`summary:`, open page bodies only when needed, then grep the
in-vault raw tier (`reference/<domain>/` for corpus-backed domains,
`_sources/<domain>/` for notes-first ones).

Then **end the answer with the two-group References section (RH ground-truth +
Wiki/`web:`) mandated by "Operation: QUERY" in `CLAUDE.md`**, and file the answer
back as `questions/<slug>.md` (full frontmatter, `status: draft`, banner rules).

Never edit the immutable `reference/`, `_sources/`, or `references/`. Offline only.

## ASSISTANT-REASONING
Let me run the query pipeline. The question is about Windows LAPS, Active Directory. This is in the active-directory domain. Let me call the wikikb ask tool.

Let me start with the MCP ask

## ASSISTANT
I'll run the mechanized QUERY pipeline. Let me start by routing and asking the question.

## TOOL wikikb_ask({"question": "We're rolling out Windows LAPS on our domain-joined servers this quarter. Where does LAPS store the managed local admin password in AD, which schema attributes are involved, and what should we monitor to verify rotation is actually happening?", "domain": "active-directory", "tier": "su)
### OUTPUT
{"query": "We're rolling out Windows LAPS on our domain-joined servers this quarter. Where does LAPS store the managed local admin password in AD, which schema attributes are involved, and what should we monitor to verify rotation is actually happening?", "orchestrator": "langgraph", "domain": "active-directory", "confident": true, "thin": false, "banner": ["out-of-coverage: support-kb not in ['conceptual'] (H1)"], "guard": [], "answer": "⚠️ out-of-coverage: support-kb not in ['conceptual'] (H1)\n\n[extractive fallback — no model answer (gateway returned no answer: http://127.0.0.1:11434)] top sources: ad-ds-credential-guard-protected-machine-accounts, ad-ds-virtualized-domain-controllers-hyper-v, ad-ds-avenues-to-compromise, ad-ds-implementing-least-privilege-administrative-models, ad-ds-understand-default-user-accounts\n\n## References (canonical)\n\n### RH ground-truth\n- `ref:ad-ds-credential-guard-protected-machine-accounts` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts\n- `ref:ad-ds-virtualized-domain-controllers-hyper-v` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v\n- `ref:ad-ds-avenues-to-compromise` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Avenues-to-Compromise\n- `ref:ad-ds-implementing-least-privilege-administrative-models` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Implementing-Least-Privilege-Administrative-Models\n- `ref:ad-ds-understand-default-user-accounts` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-default-user-accounts\n- `ref:ad-ds-ad-forest-recovery-guide` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide\n- `ref:ad-ds-advanced-ad-ds-management-using-active-directory-administrative-center-level-200` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/Advanced-AD-DS-Management-Using-Active-Directory-Administrative-Center--Level-200-\n- `ref:ad-ds-advanced-audit-policy-configuration` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration\n- `ref:ad-ds-appendix-c-protected-accounts-and-groups-in-active-directory` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Appendix-C--Protected-Accounts-and-Groups-in-Active-Directory\n- `ref:ad-ds-appendix-l-events-to-monitor` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/Appendix-L--Events-to-Monitor\n- `ref:ad-ds-attractive-accounts-for-credential-theft` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Attractive-Accounts-for-Credential-Theft\n- `ref:ad-ds-best-practices-for-securing-active-directory` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Best-Practices-for-Securing-Active-Directory\n- `ref:ad-ds-configure-kerberos-delegation-group-managed-service-accounts` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/configure-kerberos-delegation-group-managed-service-accounts\n- `ref:ad-ds-group-managed-service-accounts-overview` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview\n- `ref:ad-ds-how-to-configure-spn` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/how-to-configure-spn\n- `ref:ad-ds-implementing-secure-administrative-hosts` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Implementing-Secure-Administrative-Hosts\n- `ref:ad-ds-ldap-signing` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing\n- `ref:ad-ds-maintaining-a-more-secure-environment` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Maintaining-a-More-Secure-Environment\n- `ref:ad-ds-manage-group-managed-service-accounts` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/manage-group-managed-service-accounts\n- `ref:ad-ds-monitoring-active-directory-for-signs-of-compromise` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Monitoring-Active-Directory-for-Signs-of-Compromise\n- `ref:ad-ds-planning-for-compromise` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Planning-for-Compromise\n- `ref:ad-ds-reducing-the-active-directory-attack-surface` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Reducing-the-Active-Directory-Attack-Surface\n- `ref:ad-ds-schema-updates` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/Schema-Updates\n- `ref:ad-ds-securing-domain-controllers-against-attack` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/Securing-Domain-Controllers-Against-Attack\n- `ref:ad-ds-understand-fsmo-roles` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-fsmo-roles\n- `ref:ad-ds-understand-service-accounts` — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-service-accounts\n\n### Wiki\n- [[active-directory-implementation-review]]\n- [[credential-theft-active-directory-techniques]]\n- [[kcd-rbcd-mutual-exclusivity]]\n- [[kerberos-preauth-4771-bruteforce]]\n- [[laps-password-encryption]]\n- [[microsoft-defensive-security-model-ad]]\n- [[service-accounts-overview]]\n- [[w32tm-resync-force-flag

## ASSISTANT-REASONING
The answer is thin/extractive and out-of-coverage (support-kb tier not in conceptual). The gateway returned no answer. I need to deepen it per Operation: QUERY in CLAUDE.md. Let me read the relevant pages: windows-laps, laps-password-encryption, and the index. Let me read the wiki pages.

Let me read the key pages: windows-laps and laps-password-encryption. Also let me check the raw reference tier for LAPS. Let me look at the index and these

## ASSISTANT
The gate returned an extractive fallback (no model answer). Per the QUERY protocol, I'll deepen by reading the candidate wiki pages and the raw tier. Let me pull them in parallel.

## TOOL wikikb_read_page({"slug": "windows-laps"})
### OUTPUT
{"slug": "windows-laps", "path": "topics/windows-laps.md", "frontmatter": {"title": "Windows LAPS (Local Administrator Password Solution)", "type": "topic", "domain": "active-directory", "slug": "windows-laps", "summary": "How Windows LAPS automatically rotates and backs up each device's local-admin (and DC DSRM) password to AD or Entra ID, the join-state rules that decide where, and the ACL + encryption security model for retrieval.", "sources": "", "provenance_extracted": "9", "provenance_inferred": "2", "provenance_ambiguous": "0", "symptoms": "", "tags": "[security, directory-services, concept]", "status": "draft", "updated": "2026-06-18"}, "body": "# Windows LAPS (Local Administrator Password Solution)\n\n**A built-in Windows feature that automatically generates, rotates, and backs up\nthe password of a local administrator account (and a DC's DSRM account) into a\ndirectory, so every machine has a unique, recoverable local-admin password.**\n\n## Body\n\nThe core security win is that a single shared local-admin password across a fleet is\nexactly what enables **pass-the-hash and lateral movement**; LAPS gives every device\na unique, rotated password instead. It is native to Windows (April 2023 update on\nWin 10/11, Server 2019/2022; built into Server 2025) and is a **separate\nimplementation** from the deprecated legacy MSI \"Microsoft LAPS\" — legacy emulation\nmode exists only to ease migration.\n\n**Where the password goes is decided by join state**, not preference:\n- AD-joined only → backs up only to **Windows Server Active Directory**.\n- Entra-joined only → backs up only to **Microsoft Entra ID**.\n- Hybrid-joined → either, but **never both at once**.\n- Workplace-joined clients are unsupported.\n\nA hard-coded **once-per-hour background task** (not the Group Policy refresh cycle —\nunlike legacy LAPS, which ran as a GPO client-side extension) checks expiry,\ngenerates a policy-compliant random password, and stores it with an expiration time\nin the directory. Policy is delivered via the **Intune CSP** (preferred for Entra)\nor **Group Policy** (preferred for AD). Admins can force rotation with\n`Reset-LapsPassword` or the CSP, and force a cycle with `Invoke-LapsPolicyProcessing`.\n\nRetrieval security differs by directory: Entra ID uses **RBAC** (Global Admin / Cloud\nDevice Admin / Intune Admin can read clear text); AD uses **ACLs plus optional\nencryption** — see [[laps-password-encryption]]. Storing local-admin passwords in AD\nwithout encryption is supported but weak; enabling encryption is the recommended\nposture (inferred — Microsoft \"highly recommends\" it and gates history/DSRM on it).\n\nLAPS can also manage the **DSRM account** on domain controllers (AD-only, encryption\nrequired), which ties it to [[ad-forest-recovery]] — DSRM credentials are needed for\nauthoritative restores. It is disabled in safe mode/DSRM boots, rotates the password\nafter it detects an interactive sign-in (bounds clear-text exposure), and protects\nthe managed account from tampering (rejected changes raise\n`STATUS_POLICY_CONTROLLED_ACCOUNT` / event 10031).\n\n## Contradictions / caveats\n\n- Encryption and encrypted password **history** require the **Windows Server 2016\n  Domain Functional Level** or later; below that, decrypt is unsupported.\n- **OS image rollback** (e.g. VM snapshot revert) creates a \"torn state\" where the\n  stored password no longer matches the device. Rollback detection\n  (`msLAPS-CurrentPasswordVersion`) fixes this on Win 11 24H2 / Server 2025 only, and\n  only after `Update-LapsADSchema` extends the schema; otherwise recovery needs a\n  manual rotation or the machine-account reset.\n\n## See also\n- [[laps-password-encryption]]\n- [[securing-active-directory]]\n- [[active-directory-overview]]\n- [[active-directory-implementation-review]]\n", "body_total_chars": 3112, "session_tokens_served": 10744}

## TOOL wikikb_read_page({"slug": "laps-password-encryption"})
### OUTPUT
{"slug": "laps-password-encryption", "path": "entities/laps-password-encryption.md", "frontmatter": {"title": "Windows LAPS — AD password encryption & access model", "type": "entity", "domain": "active-directory", "slug": "laps-password-encryption", "summary": "The AD-side LAPS retrieval security model — ACLs on the computer OU plus optional CNG-DPAPI/AES-256 encryption to a single security principal, the 2016-DFL requirement, encrypted history, and the layered read/decrypt permission tiers.", "sources": "", "provenance_extracted": "7", "provenance_inferred": "1", "provenance_ambiguous": "0", "tags": "[security, directory-services]", "status": "draft", "updated": "2026-06-18"}, "body": "# Windows LAPS — AD password encryption & access model\n\n**When LAPS backs passwords to Active Directory, it secures them with ACLs on the\ncomputer object and, recommended, CNG-DPAPI/AES-256 encryption decryptable by exactly\none security principal.**\n\n## Body\n\nPasswords are stored on the **computer object**. Two (optionally three) layers guard\nthem:\n\n1. **ACLs** inherited from the computer's OU. Grant read with\n   `Set-LapsADReadPasswordPermission`; grant read/set of the expiration time with\n   `Set-LapsADResetPasswordPermission`.\n2. **Encryption** (recommended). The password is encrypted **on the managed device\n   before it reaches AD**, using CNG DPAPI with **AES-256**, against a **single**\n   security principal set via `ADPasswordEncryptionPrincipal` (defaults to the\n   domain's Domain Admins). LAPS deliberately supports only one principal (multi-\n   principal CNG DPAPI bloats the buffer) — to grant several readers, encrypt to a\n   **wrapper group**. The authorized principal **cannot be changed after** a password\n   is encrypted.\n3. **Encrypted password history** — only available when encryption is on; the device\n   needs SELF read permission (`Set-LapsADComputerSelfPermission`).\n\nThink of access as concentric tiers: read/set *expiry* (sensitive but\nnondestructive — at worst forces extra rotations) → read the *password* (reserve for\nDomain Admins) → *decrypt* (reserve for Domain Admins). Tighten tiers for sensitive\nmachines (e.g. executive laptops) versus front-line devices.\n\n## Contradictions / caveats\n\n- **Requires the Windows Server 2016 Domain Functional Level or later.** Below that,\n  Microsoft does not support retrieving decrypted passwords, and behavior is\n  undefined if pre-2016 DCs were ever promoted into the domain.\n- DSRM-account backup on DCs **requires** encryption (clear-text DSRM backup is not\n  offered) — this is the LAPS dependency that [[ad-forest-recovery]] relies on.\n- Microsoft recommends **never** granting a managed device permission to decrypt any\n  device's password, including its own (inferred constraint stated as a hard\n  recommendation in the source).\n\n## See also\n- [[windows-laps]]\n- [[fine-grained-password-policies]]\n", "body_total_chars": 2186, "session_tokens_served": 11483}

## ASSISTANT-REASONING
These wiki pages mention the schema but don't name the specific attributes. The question explicitly asks "which schema attributes are involved". The wiki pages mention `msLAPS-CurrentPasswordVersion` but not the main attributes. I should grep the raw reference tier and the references/ for LAPS schema attributes. Let me look in the raw tier for LAPS.

Let me search the vault for the LAPS schema attributes. The known attributes are: msLAPS-Password, msLAPS-PasswordExpirationTime, msLAPS-EncryptedPassword, msLAPS-EncryptedPasswordHistory, msLAPS-EncryptedDSRMPassword, msLAPS-EncryptedDSRMPasswordHistory, msLAPS-CurrentPasswordVersion, etc.

But I must only cite what's in the corpus. Let me grep the vault. Let me check reference/active-directory/ and references/ for LAPS content. Let me grep for the attributes

## ASSISTANT
The wiki pages describe the model but don't list the exact schema attribute names. Per the protocol, I'll grep the in-vault raw/reference tiers for LAPS schema attributes.

## TOOL grep({"pattern": "msLAPS|ms-Mcs|LAPS-Password|PasswordExpirationTime|DSRMPassword|CurrentPasswordVersion", "path": "/Users/guylavian/Downloads/skills/llm-wiki", "include": "*.md"})
### OUTPUT
Found 2 matches
/Users/guylavian/Downloads/skills/llm-wiki/topics/windows-laps.md:
  Line 69:   (`msLAPS-CurrentPasswordVersion`) fixes this on Win 11 24H2 / Server 2025 only, and


/Users/guylavian/Downloads/skills/llm-wiki/_sources/active-directory/windows-laps.md:
  Line 76:   `msLAPS-CurrentPasswordVersion`; on mismatch (e.g. VM snapshot revert) rotates


## TOOL grep({"pattern": "Reset-LapsPassword|Update-LapsADSchema|Set-LapsADReadPasswordPermission|ADPasswordEncryptionPrincipal|Invoke-LapsPolicyProcessing", "path": "/Users/guylavian/Downloads/skills/llm-wiki", "include": "*.md"})
### OUTPUT
Found 9 matches
/Users/guylavian/Downloads/skills/llm-wiki/topics/windows-laps.md:
  Line 48: `Reset-LapsPassword` or the CSP, and force a cycle with `Invoke-LapsPolicyProcessing`.

  Line 70:   only after `Update-LapsADSchema` extends the schema; otherwise recovery needs a


/Users/guylavian/Downloads/skills/llm-wiki/_sources/active-directory/windows-laps.md:
  Line 47: - Manual rotation: `Reset-LapsPassword` (local), the CSP ResetPassword action, or

  Line 48:   editing the expiration time in AD. Force a cycle with `Invoke-LapsPolicyProcessing`.

  Line 52: 1. **ACLs** on the computer object's OU — `Set-LapsADReadPasswordPermission` (read)

  Line 57:    (`ADPasswordEncryptionPrincipal`; defaults to Domain Admins). For multiple

  Line 77:   immediately. Requires running the latest `Update-LapsADSchema`. AD-only.


/Users/guylavian/Downloads/skills/llm-wiki/entities/laps-password-encryption.md:
  Line 30:    `Set-LapsADReadPasswordPermission`; grant read/set of the expiration time with

  Line 34:    security principal set via `ADPasswordEncryptionPrincipal` (defaults to the


## ASSISTANT-REASONING
Let me read the raw _sources/active-directory/windows-laps.md to get the full schema attributes and monitoring events. This is the notes-first source. Let me read it.

## ASSISTANT
Let me read the raw notes source for the full detail on schema attributes and monitoring.

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/_sources/active-directory/windows-laps.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/_sources/active-directory/windows-laps.md</path>
<type>file</type>
<content>
1: # Raw note — Windows LAPS (Local Administrator Password Solution)
2: 
3: - Source: Microsoft Learn, "What is Windows LAPS?", "Key concepts in Windows LAPS",
4:   "Windows LAPS passwords and passphrases", "Get started…", "Migrate to Windows
5:   LAPS from legacy LAPS", "Use Windows LAPS event logs"
6:   (web:https://learn.microsoft.com/windows-server/identity/laps/, distilled from the
7:   *windows-server identity* PDF export, fetched 2026-06-18).
8: - Status: notes-first ground truth (paraphrased — no verbatim) for the
9:   `active-directory` domain.
10: 
11: ## What it is
12: 
13: Windows LAPS is a built-in Windows feature that **automatically rotates and backs
14: up the password of a local administrator account** on devices joined to Windows
15: Server Active Directory or Microsoft Entra ID. It can also back up the **DSRM
16: (Directory Services Restore Mode) account password** on domain controllers.
17: 
18: - Native to Windows since the April 11 2023 update (Win 10/11, Server 2019/2022)
19:   and built into Server 2025. **Distinct from** the deprecated legacy MSI "Microsoft
20:   LAPS" product (legacy is deprecated as of Win 11 23H2; install blocked on newer OS).
21: - Free; backing up to AD needs no extra license, backing up to Entra ID needs Entra
22:   ID Free or higher.
23: 
24: ## Why (benefits)
25: 
26: - Defeats **pass-the-hash / lateral-traversal** by ensuring every machine's local
27:   admin password is unique and rotated.
28: - Recover otherwise-inaccessible devices; safer help-desk hand-off.
29: - Fine-grained access model (ACLs + optional encryption in AD; RBAC in Entra ID).
30: 
31: ## Backup targets & join-state rules
32: 
33: - Entra-joined only → can back up **only to Entra ID**.
34: - AD-joined only → can back up **only to AD**.
35: - Hybrid-joined → either AD **or** Entra ID (not both at once).
36: - Workplace-joined clients are **not** supported.
37: 
38: ## Key concepts / architecture
39: 
40: - Components on the managed device: `laps.dll` (core), `lapscsp.dll` (CSP),
41:   `lapspsh.dll` (PowerShell). Policy via **Intune CSP** (preferred for Entra) or
42:   **Group Policy** (preferred for AD).
43: - A **background task wakes once per hour** (hard-coded, not Task Scheduler, not the
44:   GP refresh cycle — unlike legacy LAPS which was a GPO client-side extension). It
45:   generates a new policy-compliant random password on expiry, stores it + an
46:   expiration time in the directory, and rotates automatically.
47: - Manual rotation: `Reset-LapsPassword` (local), the CSP ResetPassword action, or
48:   editing the expiration time in AD. Force a cycle with `Invoke-LapsPolicyProcessing`.
49: 
50: ## AD password security (two/three layers)
51: 
52: 1. **ACLs** on the computer object's OU — `Set-LapsADReadPasswordPermission` (read)
53:    and `Set-LapsADResetPasswordPermission` (read/set expiry).
54: 2. **Encryption** (recommended) — needs the **Windows Server 2016 Domain Functional
55:    Level** or later; uses CNG DPAPI / AES-256; encrypts the password on the device
56:    *before* it reaches AD, decryptable by **one** security principal
57:    (`ADPasswordEncryptionPrincipal`; defaults to Domain Admins). For multiple
58:    readers, wrap them in a group.
59: 3. **Encrypted password history** — only when encryption is on; device needs SELF
60:    read permission (`Set-LapsADComputerSelfPermission`).
61: 
62: Suggested permission tiers: read/set *expiry* (sensitive but nondestructive) →
63: read *password* (reserve for Domain Admins) → *decrypt* (reserve for Domain Admins).
64: 
65: ## Other behaviors
66: 
67: - **DSRM** backup: AD-only, encryption required. Recoverable as long as ≥1 DC in the
68:   domain is reachable; otherwise restore DSRM passwords from backups.
69: - **Password reset after authentication** — rotates the password once it detects the
70:   account was used to sign in (bounds clear-text exposure); configurable grace
71:   period. Not supported for DSRM.
72: - **Tampering protection** — rejects unexpected password changes with
73:   `STATUS_POLICY_CONTROLLED_ACCOUNT` (0xC000A08B), logged as event 10031.
74: - **Disabled in safe mode / DSRM / abnormal boot.**
75: - **OS image rollback detection** (Win 11 24H2 / Server 2025) — stores a GUID in
76:   `msLAPS-CurrentPasswordVersion`; on mismatch (e.g. VM snapshot revert) rotates
77:   immediately. Requires running the latest `Update-LapsADSchema`. AD-only.
78: - Management/monitoring: ADUC properties dialog, a dedicated **event log channel**,
79:   and the LAPS PowerShell module.
80: 
81: ## Symptoms (feed the review MOC)
82: 
83: - Event **10031** in the LAPS channel → blocked tamper attempt on the managed account.
84: - IT admin can't sign in with the stored LAPS password after a VM snapshot
85:   revert → "torn state"; fixed by rollback detection (24H2+) or manual rotation.
86: - Decrypt fails / "DFL too low" → encryption needs the 2016 DFL or later.

(End of file - total 86 lines)
</content>

## ASSISTANT-REASONING
The raw source doesn't list the full schema attribute names (msLAPS-Password, msLAPS-PasswordExpirationTime, etc.). It only mentions msLAPS-CurrentPasswordVersion. The corpus is the ground truth. Let me grep more broadly for the actual attributes. Let me check the reference tier and references/ for LAPS. Let me search the full vault including references/.

Actually the corpus in this vault (notes-first for AD) only contains the above. The raw source confirms msLAPS-CurrentPasswordVersion is the only attribute named. There's also mention of "password + expiration time in the directory". 

Let me check if there's a references/ entry for LAPS that might name the attributes. Let me search references/ and reference/ for "LAPS" and "msLAPS".

## ASSISTANT
Let me check whether the curated `references/` or `reference/` tiers name the specific LAPS schema attributes (e.g., `msLAPS-Password`, `msLAPS-PasswordExpirationTime`).

## TOOL grep({"pattern": "msLAPS|LAPS-Password|PasswordExpirationTime|DSRMPassword", "path": "/Users/guylavian/Downloads/skills/llm-wiki/references"})
### OUTPUT
No files found

## TOOL grep({"pattern": "msLAPS|LAPS-Password|PasswordExpirationTime|DSRMPassword", "path": "/Users/guylavian/Downloads/skills/llm-wiki/reference"})
### OUTPUT
No files found

## TOOL grep({"pattern": "LAPS", "path": "/Users/guylavian/Downloads/skills/llm-wiki/references"})
### OUTPUT
No files found

## ASSISTANT-REASONING
So the corpus only names one schema attribute: `msLAPS-CurrentPasswordVersion`. The other attributes (msLAPS-Password, msLAPS-PasswordExpirationTime, msLAPS-EncryptedPassword, etc.) are NOT in the corpus. 

Per the HARD RULE, I must not invent or transfer. The question asks "which schema attributes are involved". The corpus mentions only `msLAPS-CurrentPasswordVersion` verbatim, and also says LAPS stores the password + expiration time in the directory on the computer object. The attributes as named strings are not fully in the corpus. 

But wait — I should be careful. The corpus references Microsoft Learn "What is Windows LAPS". The schema attributes are part of the domain. But I must only cite what's in the corpus. The corpus doesn't name most of them. I should report what the corpus actually says: that LAPS stores the password and expiration time on the computer object after `Update-LapsADSchema` extends the schema, and names `msLAPS-CurrentPasswordVersion` as a specific attribute. I should not fabricate the full list of msLAPS-* attributes that aren't in the corpus.

Actually, let me reconsider. The protocol says to answer from the corpus. If the corpus doesn't contain the full attribute names, I should report what is there and note that the corpus only explicitly names `msLAPS-CurrentPasswordVersion`. But I should be honest about coverage gaps.

Now for the monitoring part — the question "what should we monitor to verify rotation is actually happening". The corpus mentions:
- LAPS has a dedicated event log channel
- Event 10031 → blocked tamper attempt
- The background task runs once per hour and rotates on expiry

For verifying rotation, the corpus tells us: the password is stored with an expiration time in the directory; rotation happens on expiry; manual rotation via Reset-LapsPassword. To monitor rotation, the corpus points to the dedicated event log channel. But it doesn't name specific "rotation success" event IDs in the corpus. The raw source mentions event 10031 (tamper). Hmm.

Let me check if there are more LAPS event IDs in the corpus. The raw source only names event 10031. So I should report that the LAPS dedicated event log channel is the monitoring surface, and the most concrete event the corpus names is 10031 (tamper blocked). For verifying rotation, the corpus says to watch the dedicated event log channel and check the stored expiration time on the computer object.

Let me also check what's in the windows-server-identity-coverage-gaps page — maybe it lists known coverage gaps including LAPS attributes. Let me read it quickly. Actually, that's about coverage gaps. It might be relevant to note that the corpus has gaps. But the question wants a real answer.

Let me also double check the references group in CLAUDE.md to comply with the output. The user explicitly wants the two-group References section and to file as questions/<slug>.md.

Let me check CLAUDE.md for the exact References format and the question page frontmatter.

Actually, I have enough. Let me also verify the monitoring angle more. Let me read windows-server-identity-coverage-gaps to see if LAPS event monitoring is mentioned, and also check if there's any mention of specific LAPS events like 10024, 10029 (rotation events). Let me grep for "1002" "1003" "event" in the laps source. Already grep showed only 10031.

So the corpus's monitoring guidance for LAPS:
- Dedicated event log channel (Microsoft-Windows-LAPS/Operational) — the corpus says "a dedicated event log channel" without naming it exactly. I'll describe it as the dedicated LAPS event log channel.
- Event 10031 for tamper.
- The once-per-hour background task.
- Verify by checking the stored expiration time on the computer object and that it advances.

Now I need the exact References format from CLAUDE.md. The ask output already gives me a "References (canonical)" with two groups: RH ground-truth and Wiki. But the user wants me to end with the two-group References section (RH ground-truth +

## ASSISTANT
The corpus names only one LAPS schema attribute verbatim (`msLAPS-CurrentPasswordVersion`); the rest of the `msLAPS-*` set isn't enumerated here. Let me confirm the exact `questions/` page format and banner rules from `CLAUDE.md` before writing the file.

## TOOL grep({"pattern": "questions/|Operation: QUERY|References|RH ground-truth|web:|banner|status: draft", "path": "/Users/guylavian/Downloads/skills/llm-wiki/CLAUDE.md"})
### OUTPUT
Found 100 matches (more matches available)
/Users/guylavian/Downloads/skills/llm-wiki/_sources/keycloak/owasp-cheatsheets.md:
  Line 132: - **Upstream tier.** All of the above is `web:` (upstream/community best practice), not Red Hat ground truth — for what RHBK supports/enforces, defer to `kb:`/`guide:`/`ref:` sources.


/Users/guylavian/Downloads/skills/llm-wiki/questions/kc-cache-embedded-mcast-port-behavior.md:
  Line 16: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/saml-sp-integration-rhbk-migration.md:
  Line 19: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/SKILL.md:
  Line 130: `entities/`, and answered `questions/` pages that *compile* the raw sources into


/Users/guylavian/Downloads/skills/llm-wiki/topics/rhsso-to-rhbk-migration.md:
  Line 30: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/migrate-rhsso-76-java-client-adapters.md:
  Line 17: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/kcd-rbcd-mutual-exclusivity.md:
  Line 17: status: draft

  Line 89: ## References


/Users/guylavian/Downloads/skills/llm-wiki/questions/sysvol-folder-function.md:
  Line 6: status: draft

  Line 15:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview

  Line 81: ## References


/Users/guylavian/Downloads/skills/llm-wiki/questions/access-token-cryptographic-verification.md:
  Line 7: status: draft

  Line 15:   - web:https://www.rfc-editor.org/rfc/rfc9068 (RFC 9068 JWT Profile for OAuth2 Access Tokens)

  Line 16:   - web:https://www.rfc-editor.org/rfc/rfc6749 (RFC 6749 OAuth2 core)

  Line 17:   - web:https://www.rfc-editor.org/rfc/rfc6750 (RFC 6750 Bearer Token Usage)

  Line 18:   - web:https://www.rfc-editor.org/rfc/rfc7662 (RFC 7662 Token Introspection)

  Line 19:   - web:https://www.rfc-editor.org/rfc/rfc7515 (RFC 7515 JWS)

  Line 20:   - web:https://www.rfc-editor.org/rfc/rfc7009 (RFC 7009 Token Revocation)

  Line 71: ## References

  Line 73: ### RH ground-truth (wiki sources)


/Users/guylavian/Downloads/skills/llm-wiki/topics/ad-certificate-services.md:
  Line 10:   - web:https://learn.microsoft.com/windows-server/identity/ad-cs/ (Microsoft Learn — AD CS, fetched 2026-06-18)

  Line 15: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/feature-flags-enable-disable.md:
  Line 16: status: draft

  Line 57: ## References

  Line 59: **RH ground-truth:**


/Users/guylavian/Downloads/skills/llm-wiki/questions/types-of-service-accounts.md:
  Line 17: status: draft

  Line 35: ## References

  Line 37: ### RH ground-truth (`kb:`)


/Users/guylavian/Downloads/skills/llm-wiki/topics/observability-stack.md:
  Line 22: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/vlan-trunking-ios-xe.md:
  Line 10:   - web:https://datatracker.ietf.org/doc/rfc9700/ (RFC 9700, fetched 2026-06-16)

  Line 15: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/rhbk-upgrade-cadence.md:
  Line 20: status: draft

  Line 52: ### RH ground-truth

  Line 66: - `web:https://access.redhat.com/support/policy/updates/jboss_notes` (נקודת כניסה למדיניות מחזור החיים של Red Hat Runtimes, לא מאוחזת בוויקי)


/Users/guylavian/Downloads/skills/llm-wiki/topics/virtualized-domain-controllers.md:
  Line 8:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/Introduction-to-Active-Directory-Domain-Services-AD-DS-Virtualization-Level-100 (Microsoft Learn — Safely virtualizing Active Directory Domain Services (AD DS), fetched 2026-06-18)

  Line 9:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Deployment-and-Configuration (Microsoft Learn — Virtualized Domain Controller Deployment and Configuration, fetched 2026-06-18)

  Line 10:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Virtualized-Domain-Controller-Architecture (Microsoft Learn — Virtualized Domain Controller Architecture, fetched 2026-06-18)

  Line 11:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v (Microsoft Learn — Virtualizing domain controllers with Hyper-V, fetched 2026-06-18)

  Line 12:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/Support-for-using-Hyper-V-Replica-for-virtualized-domain-controllers (Microsoft Learn — Support for using Hyper-V Replica for virtualized domain controllers, fetched 2026-06-18)

  Line 27: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/mtls-certificate-binding-oauth2-tokens.md:
  Line 9:   - web:https://www.rfc-editor.org/rfc/rfc8705 (RFC 8705, fetched 2026-06-17)

  Line 10:   - web:https://openid.net/specs/fapi-security-profile-2_0-final.html (FAPI 2.0 Security Profile, fetched 2026-06-17)

  Line 36: ## References

  Line 38: *RH ground-truth:*

  Line 50: - `web:https://www.rfc-editor.org/rfc/rfc8705` (RFC 8705, fetched 2026-06-17)

  Line 51: - `web:https://openid.net/specs/fapi-security-profile-2_0-final.html` (FAPI 2.0 Security Profile, fetched 2026-06-17)


/Users/guylavian/Downloads/skills/llm-wiki/questions/parallel-user-import-silent-failure.md:
  Line 23: status: draft

  Line 135: ## References

  Line 137: ### RH ground-truth (`kb:` / `guide:` / `ref:`)


/Users/guylavian/Downloads/skills/llm-wiki/topics/fine-grained-authorization.md:
  Line 20: status: draft


/Users/guylavian/Downloads/skills/llm-wiki/questions/policy-based-routing.md:
  Line 15: status: draft

  Line 50: ## References

  Line 52: **RH ground-truth (kb):**


/Users/guylavian/Downloads/skills/llm-wiki/questions/spi-customization-rhbk.md:
  Line 17: status: draft

  Line 85: ## References

  Line 87: **RH ground-truth:**


/Users/guylavian/Downloads/skills/llm-wiki/topics/identity-brokering.md:
  Line 16: status: draft


/Users/guylavian/Downloads/skills/llm-

## ASSISTANT-REASONING
I have enough context. Let me look at an existing AD question page to match the frontmatter format. Let me read one, e.g., questions/sysvol-folder-function.md (AD domain) to see the exact frontmatter and banner format

## ASSISTANT
Let me look at an existing AD question page to match its frontmatter/banner format exactly.

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/questions/sysvol-folder-function.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/questions/sysvol-folder-function.md</path>
<type>file</type>
<content>
1: ---
2: title: What is the function of the SYSVOL folder?
3: type: question
4: domain: active-directory
5: slug: sysvol-folder-function
6: status: draft
7: summary: SYSVOL is the shared system volume on every domain controller that hosts the Group Policy template files, logon/logoff/startup/shutdown scripts, and other domain-wide file-based policy content, replicated between DCs via FRS or DFSR.
8: sources:
9:   - kb:ad-ds-group-policy-overview
10:   - kb:ad-ds-virtualized-domain-controller-architecture
11:   - kb:ad-ds-virtualized-domain-controller-troubleshooting
12:   - kb:ad-ds-ad-forest-recovery-authoritative-recovery-sysvol
13:   - kb:ad-ds-install-active-directory-domain-services-level-100
14:   - kb:ad-ds-install-a-new-windows-server-2012-active-directory-forest-level-200
15:   - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview
16: provenance:
17:   extracted: 10
18:   inferred: 1
19:   ambiguous: 0
20: question_tier: conceptual
21: updated: 2026-07-09
22: ---
23: 
24: # What is the function of the SYSVOL folder?
25: 
26: **SYSVOL (System Volume) is a mandatory shared folder on every Active Directory domain controller (DC) that stores the file-based components of Group Policy Objects and domain-wide scripts, and is replicated among all DCs within a domain.**
27: 
28: ## Core functions
29: 
30: ### 1. Group Policy Template (GPT) storage
31: 
32: Every Group Policy Object (GPO) consists of two halves:
33: 
34: - **Group Policy container** — stored in the domain partition of Active Directory, replicated by AD replication.
35: - **Group Policy template** — the actual policy files (registry settings in `Registry.pol`, security settings, administrative templates, scripts, and other policy data) stored on-disk under `\\<domain>\SYSVOL\<domain>\Policies\{GPO-GUID}\`.
36: 
37: Because the template lives in SYSVOL, a GPO can exist in AD but fail to apply if SYSVOL replication is unhealthy and the template files are not present on a given DC (inferred).
38: 
39: ### 2. Logon / logoff / startup / shutdown scripts
40: 
41: Group Policy logon and logoff scripts (for users) and startup/shutdown scripts (for computers) are placed in the SYSVOL share, typically under:
42: `\\<domain>\SYSVOL\<domain>\scripts\`
43: or within individual GPO policy paths. Client machines access these over the network via the `NETLOGON` share (which maps to `SYSVOL\<domain>\scripts`).
44: 
45: ### 3. DFSR / FRS replication target
46: 
47: SYSVOL is a directory that must be identical across all DCs in a domain. It is kept in sync via:
48: 
49: - **FRS (File Replication Service)** — the legacy replication engine, still supported through Windows Server 2016 (the last release to support FRS).
50: - **DFSR (Distributed File System Replication)** — the modern, more efficient engine replacing FRS. Newer Windows Server versions and higher functional levels require DFSR for SYSVOL.
51: 
52: The replication service on each DC ensures that GPO templates and scripts created or updated on one DC propagate to all other DCs.
53: 
54: ### 4. Netlogon share
55: 
56: The `NETLOGON` share, used during domain logon for processing logon scripts and policies, is a published share pointing into the SYSVOL directory tree. The Netlogon service only shares SYSVOL as `NETLOGON` after SYSVOL initialization is complete.
57: 
58: ### 5. Domain controller advertisement prerequisite
59: 
60: A DC does not advertise itself as available (via LDAP ping, DNS SRV, etc.) until SYSVOL has finished its initial synchronization. Event ID 13516 (FRS) or 4604 (DFSR) confirms that SYSVOL initialization is complete and the Netlogon service has been notified to share SYSVOL. This is a gating condition for DC readiness.
61: 
62: ### 6. Forest recovery role
63: 
64: During AD forest recovery, SYSVOL requires distinct handling:
65: 
66: - **Authoritative restore** — The first DC restored in the domain must perform an authoritative sync of SYSVOL, typically using `wbadmin -authsysvol` or editing the `msDFSR-Options` attribute, so that this DC's SYSVOL is treated as the primary copy and propagated to all other recovered DCs.
67: - **Non-authoritative restore** — Subsequent DCs are restored non-authoritatively; their SYSVOL is overwritten from the authoritative source.
68: 
69: ### 7. Safe virtualization trigger
70: 
71: When a virtualized DC running Windows Server 2012+ is restored from a hypervisor snapshot, VM-GenerationID detection triggers a non-authoritative SYSVOL synchronization (FRS uses D2 BURFLAGS; DFSR deletes its database files) to ensure SYSVOL converges with the rest of the domain.
72: 
73: ## Physical location
74: 
75: Default path: `%SystemRoot%\SYSVOL` (e.g., `C:\Windows\SYSVOL`). The path is configurable during DC promotion via `-SYSVOLPath` (PowerShell) or the AD DS Installation Wizard Paths page. The SYSVOL path is subject to the Win32 `MAX_PATH` limit (260 characters). Microsoft recommends storing NTDS.DIT, logs, and SYSVOL on a dedicated virtual SCSI disk separate from the OS disk for durability and performance.
76: 
77: ## ReFS restriction
78: 
79: The AD DS database (NTDS.DIT), transaction logs, and SYSVOL must **not** be placed on a volume formatted with ReFS (Resilient File System). Only NTFS-formatted volumes are supported for these components.
80: 
81: ## References
82: 
83: ### Microsoft Learn (ground truth)
84: 
85: - [Group Policy overview for Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
86: - [Virtualized Domain Controller Architecture](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture)
87: - [AD Forest Recovery — authoritative sync of DFSR-replicated SYSVOL](https://learn.microsoft.com/en-us/windows-se

## ASSISTANT-REASONING
Now I understand the format. The References section uses "Microsoft Learn (ground truth)" and "Wiki / vault". But CLAUDE.md and the user ask for "two-group References section (RH ground-truth + Wiki/`web:`)". The user explicitly said: "end the answer with the two-group References section (RH ground-truth + Wiki/`web:`) mandated by 'Operation: QUERY' in `CLAUDE.md`".

So my final answer should end with:
## References
### RH ground-truth
### Wiki / `web:`

For LAPS, the ground-truth is the Microsoft Learn "windows-server identity" LAPS docs. The wiki pages are windows-laps and laps-password-encryption.

Now I need to write the comprehensive answer and file it as questions/<slug>.md.

Let me think about what slug to use: "windows-laps-ad-storage-rotation-monitoring" or similar. The question is about LAPS AD storage, schema attributes, rotation monitoring. Let me use slug: `windows-laps-ad-storage-rotation-monitor`.

Now, the banner rules. The ask result had an out-of-coverage banner: "out-of-coverage: support-kb not in ['conceptual'] (H1)" and the gateway returned no answer. So I should include a banner noting this is a synthesized answer from corpus pages (since the gateway didn't answer). Actually the user wants me to deepen it. Let me add a banner line noting provenance.

Given the question asks about specifics the corpus only partially covers (schema attribute names), I should be honest. Let me write the answer grounded strictly in the corpus, noting the gap.

Let me now compose the answer content:

1. Where LAPS stores the managed local admin password in AD:
- On the **computer object** (the device's computer account) in Active Directory. It stores the password plus an expiration time. (from windows-laps.md: "stores it with an expiration time in the directory" and laps-password-encryption.md: "Passwords are stored on the computer object.")
- Backed up to AD only when the device is **AD-joined** (or hybrid joined choosing AD) — join-state decides the target, never both at once.
- The once-per-hour hard-coded background task stores the new password on expiry.

2. Schema attributes involved:
- The corpus explicitly names only **`msLAPS-CurrentPasswordVersion`** — a GUID stored to detect OS image rollback (e.g., VM snapshot revert); on mismatch the device rotates immediately. Present only after running the latest `Update-LapsADSchema` to extend the schema.
- The corpus states that `Update-LapsADSchema` extends the AD schema to add the LAPS attribute set on the computer object, and that encryption/history require the 2016 DFL. But it does NOT enumerate the individual `msLAPS-*` attribute names (e.g., the clear-text vs encrypted password / expiration-time attributes). I'll flag this as a corpus coverage gap.
- I must NOT invent the attribute names. I'll state what's grounded.

Actually, let me reconsider whether to claim more. The HARD RULE says never transfer/invent. The corpus doesn't name msLAPS-Password etc. So I report the gap honestly. That's the disciplined answer.

3. What to monitor to verify rotation is happening:
- **Dedicated LAPS event log channel** — the corpus says LAPS has "a dedicated event log channel" used for management/monitoring. Monitor it for rotation and error activity.
- **Event 10031** — logged when an unexpected password change is rejected (`STATUS_POLICY_CONTROLLED_ACCOUNT`), indicating LAPS tampering protection is active. (This is more a tamper signal than a rotation-success signal, but it confirms LAPS is functioning.)
- **Check the stored expiration time on the computer object** advances/refreshes after each rotation cycle — the password is stored with an expiration time; verifying that the expiration time keeps moving forward is the direct proof rotation is occurring.
- **`Reset-LapsPassword` / `Invoke-LapsPolicyProcessing`** can be used to force rotation and then confirm the new expiry.
- **`msLAPS-CurrentPasswordVersion` rollback detection** — on 24H2+/Server 2025, a mismatch triggers an immediat

## ASSISTANT
I have what I need from the corpus. Note: the question doesn't name a single specific token (it's a multi-part conceptual query), so the token GATE is skipped per the contract. Now I'll write the synthesized answer to `questions/windows-laps-ad-storage-rotation-monitor.md`.

## TOOL write({"content": "---\ntitle: Where does Windows LAPS store the managed local-admin password in AD, which schema attributes are involved, and what should we monitor to verify rotation?\ntype: question\ndomain: active-directory\nslug: windows-laps-ad-storage-rotation-monitor\nstatus: draft\nsummary: Windo)
### OUTPUT
Wrote file successfully.

## ASSISTANT-REASONING
Now let me present the final answer to the user, ending with the two-group References section. The user asked me to "end the answer with the two-group References section (RH ground-truth + Wiki/`web:`)". I've filed the question page. Now give the final synthesized answer in chat.

Let me present a concise but complete answer, then the References

## ASSISTANT
## Answer

**Where the password lives in AD**
For AD-joined (or hybrid-joined devices that pick AD as the target) machines, Windows LAPS backs the managed local-admin password up **onto the device's own computer object** in Active Directory, storing the password **together with an expiration time**. The backup target is fixed by *join state* — AD-joined → AD only; Entra-joined → Entra ID only; hybrid → either AD *or* Entra ID but **never both at once**. Retrieval in AD is guarded by OU-inherited **ACLs** (`Set-LapsADReadPasswordPermission` / `Set-LapsADResetPasswordPermission`) plus **optional CNG-DPAPI/AES-256 encryption** done on the device before the value leaves it. LAPS can also back up the **DSRM** account on DCs (AD-only, encryption required).

**Schema attributes**
`Update-LapsADSchema` extends the AD schema to add the LAPS attribute set on the computer object. The corpus names **only one** LAPS attribute verbatim — **`msLAPS-CurrentPasswordVersion`**, a GUID used for OS-image-rollback detection (on Win 11 24H2 / Server 2025 a mismatch after e.g. a VM snapshot revert forces an immediate rotation; present only after the latest `Update-LapsADSchema`). 

> Coverage caveat: the vault describes LAPS storing "the password + an expiration time" and extending the schema, but it does **not** enumerate the individual `msLAPS-*` attribute display names (clear-text/encrypted password, expiration-time, history, DSRM). Those strings are not in the corpus, so I've omitted them rather than invent them. Encrypted password + history additionally require the **Windows Server 2016 DFL**.

**What to monitor to verify rotation**
A hard-coded **once-per-hour background task** generates a new password on expiry and rewrites it with a fresh expiration time. To confirm rotation is actually happening:
1. **The dedicated LAPS event-log channel** — primary monitoring surface for backup/rotation and errors.
2. **Confirm the stored expiration time on the computer object keeps advancing** — the direct proof rotation occurred (read via the LAPS PowerShell module / ADUC).
3. **Event 10031** — logged when an unexpected change is rejected (`STATUS_POLICY_CONTROLLED_ACCOUNT`), confirming LAPS tamper-protection is live.
4. **Rollback-triggered rotations** via `msLAPS-CurrentPasswordVersion` mismatch (24H2+/Server 2025) — validates the rollback-detection path.
5. **Decrypt/retrieval health** — ensure the authorized principal (default Domain Admins) can read *and* decrypt; a "DFL too low" decrypt failure means the 2016 DFL isn't met.
6. **Drill:** force a rotation with `Reset-LapsPassword` / CSP `ResetPassword`, or `Invoke-LapsPolicyProcessing`, then confirm the expiry refreshed.

## References

### RH ground-truth (`web:`)
- `web:https://learn.microsoft.com/windows-server/identity/laps/` — Microsoft Learn, *Windows LAPS* (What is Windows LAPS?, Key concepts, passwords and passphrases, Get started, Migrate from legacy LAPS, Use Windows LAPS event logs). Distilled into `_sources/active-directory/windows-laps.md` (PDF export of *windows-server identity*, fetched 2026-06-18).

### Wiki / vault (`wiki:`)
- [[windows-laps]] — `topics/windows-laps.md` (join-state rules, hourly task, DSRM, rollback detection, `msLAPS-CurrentPasswordVersion`).
- [[laps-password-encryption]] — `entities/laps-password-encryption.md` (AD ACL + CNG-DPAPI/AES-256 encryption model, 2016 DFL requirement, permission tiers).

---
*Answer filed as `questions/windows-laps-ad-storage-rotation-monitor.md` (status: draft). Banner: the `wikikb ask` gateway returned no model answer (out-of-coverage for the `support-kb` tier), so this is a corpus-synthesized answer built only from the LAPS wiki pages and the notes-first source — it intentionally omits any LAPS attribute/event name not present in the vault.*