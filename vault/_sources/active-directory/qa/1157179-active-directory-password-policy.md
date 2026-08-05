---
title: "Active Directory Password Policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1157179/active-directory-password-policy
question_id: 1157179
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Active Directory Password Policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1157179/active-directory-password-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hallo    

Beim Benutzer steht drinn, net user username /domain, dass das Passwort abläuft, das ist doof weil cih das eigentlich in der GPO auf 0 gesetzt habe.    

Das scheint aber nicht zu finktionieren.    

Bei den Administratoren ist über eine eigene GPO 365 Tage gesetzt, das scheint aber auch  nicht zu funktionieren.    

Was mache ich falsch?    

GPO --> Default Domain Policy --> Computerkonfiguration --> Windows-Einstellungen --> Sicherheitseinstellungen --> Kontorichtlinien --> Kennwortrichtlinien --> Maximales Kennwortalter auf 0    

GPO --> ou firma -- > user --> administrators --> password policys for administrators Maximales kennwortalter auf 365 gesetzt.    

Mit net account /maxpwage:0 bzw. 365 kann ich das zwar ändern aber nur global und das möchte ich nicht.    

LG gdc

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-01-09*

Hi,    

Here , it's a english forum , that's why I will answer to your question in english.    

If you want apply the password policy on domain users through GPO ,you have to use only the default domain policy object linked on domain level.    

If you are using a GPO linked on Organization Unit level, the password policy will be applied on local users in member machine.    

Since Windows 2008 , you can create and deploy many password policy in same domain using FGPP (Fine Grained Password Policy), I recommend you to use this feature for your case:    

fine-grained-password-policy-best-practices    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-09*

Hello    

Thank you.    

Instead of using gpo i should use fgpp?    

If i already configured 0 in gpo is that something i have to look at or can i just let this stay how it is?    

Unter "net user adminaccountusername /domain" in cmd i see still not that he has to change the password but unter testing the policy affects with powershell Get-ADUserResultantPasswordPolicy adminaccountsuser he show's the account is affected to the policy.    

greetings    

gdc
