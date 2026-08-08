---
title: "Problem after applying the Deny Log on locally GPO setting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/473663/problem-after-applying-the-deny-log-on-locally-gpo
question_id: 473663
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Problem after applying the Deny Log on locally GPO setting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/473663/problem-after-applying-the-deny-log-on-locally-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!    

While testing tiered AD infrastructer I was greatly suprised to see how one of the key gpo parameters is working.      

Suppose there's a domain controller - DC - which belongs to Tier0 OU (with no gpo  applied except the Default Domain Policy) and a number of servers in the SERVERS OU (Tier1) to which the gpo with the following setting is applied:    

    

The most important idea in the tiered AD model is preventing the cross-tier logons - in other words, you should not be able to log on to Tier1 servers under Tier0 accounts - in my case it means I shouldn't be able to use any domain/enterprise admin accounts (which are Tier0 accounts) for logging onto Tier1 servers (in the SERVERS OU), and the aforementioned Deny log on locally policy setting is the setting that is supposed to do exactly that.    

And it really does what I expect it to do - any domain/enterprise-wide administrative accounts can no longer log on to Tier1 servers - so far so good, but... either I'm missing something or enabling this option may lead to other - rather weird - consequences.    

Once again: here's the MS's explanation of the Deny log on locally parameter:    

    

As far as I understand this text it means that the ONLY goal of this parameter is to deny log on locally  TO THIS COMPUTER for the defined accounts.    

Why in this case I'm loosing the ability to connect to DC right after the policy gets applied?    

For example, when I try to access \dc as Domain\AdminT1 I see this:    

    

ANY domain user can access ANY domain computer by default so what is preventing Domain\AdminT1 from accessing \DC AFTER applying the policy ???    

There're other gpo settings being applied but they do not have any effect on the possibility to connect to \dc - as soon as I delete the domain admins/enterprise admins accounts from the policy \dc gets accessible again:    

    

    

???

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-22*

"Check if there are following settings configured on the DCs:" - no, they are not configured.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-19*

"Did you try logon the server with other users?" - no, I didn't, there's only one administrative account for the tier1.  

"can you check the settings on the 2 GPOs?" - sorry, I just don't understand what should I be looking for... I already know that it is the Deny Log on policy that prevents AdminT1 from making NETWORK connections to \DC (and yes, there're no any additional GPOs applied to DC except the defaults ones).

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-16*

Sorry for the delay...    

DC:    

    

Server:

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-14*

Hi FanFan-MSFT,  

"Based on my understanding, the domain controllers are in the default domain controller OU, and only the domain admins can logon locally.  

The member servers are in the server OU, the admins can't logon to (deny logon locally policy GPO was linked on the server OU), but other users can.  

*When logon to the servers with admin 1, DCs can't be accessed." - yes, you are right!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-14*

Hi,  

Based on my understanding, the domain controllers are in the default domain controller OU, and only the domain admins can logon locally.  

The member servers are in the server OU, the admins can't logon to (deny logon locally policy GPO was linked on the server OU), but other users can.  

When logon to the servers with admin 1, DCs can't be accessed.  

If i misunderstand you, feel free to let me know.  

I also did a test in my lab, define the policy: deny logon locally with the domain admins.  

But the DCs was not impacted from the policy on the servers.  

It is suggested confirming the group policy on the servers and DCs by the command:  

Gpresult /h report.html.  

Best Regards,
