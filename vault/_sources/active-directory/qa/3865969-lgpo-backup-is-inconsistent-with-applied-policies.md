---
title: "LGPO backup is inconsistent with applied policies"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3865969/lgpo-backup-is-inconsistent-with-applied-policies
question_id: 3865969
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# LGPO backup is inconsistent with applied policies

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3865969/lgpo-backup-is-inconsistent-with-applied-policies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello microsoft community, I have a question regarding the LGPO tool.

I am trying to create a set of policies to apply across many machines automatically, so to get started I've been playing around manually. I've downloaded the LGPO tool and made some manual configurations to my local policies in the graphical Local Group Policy Editor - specifically setting the password history and minimum and maximum password ages at Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy. Then, I tried to extract those policies after applying them with the following commands:

```
.\LGPO.exe /b C:\CIS /n "Backup"
mv '.\{874F6B0E-845E-4301-A911-81E71B3135C0}\' .\LGPO_clean
.\LGPO.exe /parse /m .\LGPO_clean\DomainSysvol\GPO\Machine\registry.pol > clean.machine.machine_flag.registry.txt
.\LGPO.exe /parse /u .\LGPO_clean\DomainSysvol\GPO\Machine\registry.pol > clean.machine.user_flag.registry.txt
.\LGPO.exe /parse /m .\LGPO_clean\DomainSysvol\GPO\User\registry.pol > clean.user.machine_flag.registry.txt
.\LGPO.exe /parse /u .\LGPO_clean\DomainSysvol\GPO\User\registry.pol > clean.user.user_flag.registry.txt
```

My expectation was that I would get text files with the respective policies applied to either the user or the machine as a whole. However. my files are empty of any policies, despite them being configured in the GUI. 

```
; ----------------------------------------------------------------------

; PARSING Computer POLICY

; Source file:  .\LGPO_clean\DomainSysvol\GPO\User\registry.pol

; PARSING COMPLETED.

; ----------------------------------------------------------------------
```

But this is not the whole story.

Before I did this, I had simply tried to configure the policies through the command line, taking a text-formatted output as a template and adding (or more precisely, guessing) the paths to these policies (below is the amalgamation of my three attempts):

```
; ----------------------------------------------------------------------

; PARSING Computer POLICY

; Source file:  .\LGPO_clean\DomainSysvol\GPO\Machine\registry.pol

Computer

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy

Enforce Password History

DWORD:24

Computer

Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy

Maximum Password Age

DWORD:365

Computer

Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy

Enforce Password History

DWORD:24

Computer

Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy

Maximum Password Age

DWORD:365

Computer

Configuration\Policies\WindowsSettings\SecuritySettings\AccountPolicies\PasswordPolicy

EnforcePasswordHistory

DWORD:24

Computer

Configuration\Policies\WindowsSettings\SecuritySettings\AccountPolicies\PasswordPolicy

MaximumPasswordAge

DWORD:365

; PARSING COMPLETED.

; ----------------------------------------------------------------------
```

When I did the commands at the top to create a "Backup", all these showed up with the correct numbers, exactly how I had tried to configure them. However, they were not visible in the GUI, not even after a restart.

So, TL;DR: For some reason there seems to be an inconsistency between the policies in the GUI editor and the LGPO programme. What have I missed to have caused this? As a final note: this is on a VM, so a full system reset is no problem if that is required.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-07-01*

Hi Harry, thank you very much for your reply. It makes sense that it doesn't show up if I was using the wrong tool! If I may ask a follow-up, are there any other policies that require a different tool than LGPO.exe and secedit? As mentioned, I want to automate it as much as possible, so any other command-line tools that I may have missed would be welcome :)
