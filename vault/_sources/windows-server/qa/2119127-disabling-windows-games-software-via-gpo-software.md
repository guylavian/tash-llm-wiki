---
title: "Disabling Windows Games/Software via GPO Software Restrictions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2119127/disabling-windows-games-software-via-gpo-software
question_id: 2119127
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Disabling Windows Games/Software via GPO Software Restrictions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2119127/disabling-windows-games-software-via-gpo-software (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Disabling Windows Games/Software via GPO Software Restrictions

I tried Computer Configuration > Policies > Windows Settings > Security Settings > Application Control Policies > AppLocker. this but no luck 

please any other way to block solitaire game in windows 10 and windows 11 using group policy .please help me in this us

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-14*

Hello,

Let's explore another method using Group Policy to achieve this.

Using Software Restriction Policies

You can use Software Restriction Policies (SRP) to block specific applications like Solitaire. Here's how you can do it:

1.Open Group Policy Management Console (GPMC):

Press Win + R, type gpmc.msc, and press Enter.

2.Create a New Group Policy Object (GPO):

Right-click on your domain or organizational unit (OU) where you want to apply the policy, and select Create a GPO in this domain, and Link it here....

Name your new GPO, for example, "Block Solitaire".

3.Edit the GPO:

Right-click on the newly created GPO and select Edit.

4.Navigate to Software Restriction Policies:

Go to Computer Configuration > Policies > Windows Settings > Security Settings > Software Restriction Policies.

If no policies are defined, right-click on Software Restriction Policies and select New Software Restriction Policies.

5.Create a New Hash Rule:

Right-click on Additional Rules and select New Hash Rule.

Browse to the location of the Solitaire executable file (usually C:\Program Files\Microsoft Games\Solitaire\Solitaire.exe or C:\Program Files\WindowsApps\Microsoft.MicrosoftSolitaireCollection_*\Solitaire.exe).

Select the file and click Open.

Set the Security Level to Disallowed and click OK.

6.Apply the GPO:

Close the Group Policy Management Editor.

Ensure the GPO is linked to the correct OU or domain.

Using Path Rules

Alternatively, you can use Path Rules to block the application:

1.Follow steps 1-4 above to create and edit a GPO.

2.Create a New Path Rule:

Right-click on Additional Rules and select New Path Rule.

Enter the path to the Solitaire executable file (e.g., C:\Program Files\Microsoft Games\Solitaire\Solitaire.exe or C:\Program Files\WindowsApps\Microsoft.MicrosoftSolitaireCollection_*\Solitaire.exe).

Set the Security Level to Disallowed and click OK.
