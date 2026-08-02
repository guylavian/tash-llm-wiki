---
title: "SYSVOL file got Encrypted via Ransomeware attack"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199252/sysvol-file-got-encrypted-via-ransomeware-attack
question_id: 199252
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOL file got Encrypted via Ransomeware attack

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199252/sysvol-file-got-encrypted-via-ransomeware-attack (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts ,  

We have faced ransomware attack recently , it encrypted files of Domain Controller 2012 SysVol Windows Server 2012 Standard working as Primary Domain Controller while two more additional domain controllers are there with GC enabled, what's the easiest way to recover the SysVol folders only ?  

We have taken System State Backup of DC that's older after that many Policies have been made, 600+ users were created, if we go with recovery option, we have to create them all a very hectic job.  

Please suggest and share the easiest way to recover only the SysVol from the backup, if there is any option available to reconstruct sysvol from the scratch, please suggest.  

I always taken benefits from this community and expecting again from you.  

Regards,  

Kamal

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

Dear  DSPatrick I must try and get back to you. I really appreciate your help in this regard.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-15*

Should work and sounds like there's nothing lost in trying. I'd probably copy to one domain controller then you could do a non-authoritative restore to others.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

Thank you SDPatrick, bit explanation is needed, I have studied the link which you have refereed,   

How to temporarily stabilize the domain SYSVOL tree ? this option is mentioned, If I restore system estate backup on any other location and copy the entire contents of SYSVOL as per mentioned detail, can i be able to restore all files ?  

1.Stop FRS on all domain controllers in the domain and set the service to Disabled.  

Manually copy the full set of policies to the following folder on each domain controller:  

\SYSVOL\SYSVOL\dns domain name\policies  

2.Typically, the following two policies are required for authentication:  

```
Default Domain Controllers Policy{6AC1786C-016F-11D2-945F-00C04fB984F9}
Default Domain Policy {31B2F340-016D-11D2-945F-00C04FB984F9}
```

Note You may have to copy additional policies depending on Group Policy requirements for the environment.  

3.Manually copy all necessary scripts to the following folder:

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-15*

How many domain controllers? and how recent is the backup? The simpler solution may be to turn existing off, restore the recent backup of PDCe and rebuild the other domain controllers.  

--please don't forget to Accept as answer if the reply is helpful--
