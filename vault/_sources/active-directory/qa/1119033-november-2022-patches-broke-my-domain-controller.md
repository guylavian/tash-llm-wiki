---
title: "November 2022 Patches Broke my Domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1119033/november-2022-patches-broke-my-domain-controller
question_id: 1119033
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# November 2022 Patches Broke my Domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1119033/november-2022-patches-broke-my-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 1 DC out of the 7 total that somehow got the November 22 Patch that causes issues with Kerberos etc. I thought that uninstalling that patch on that DC would do the trick but low and behold the issue remained even after uninstall of that update. I did find the Nov 17th update that was supposed to fix it which I did install but again, still broken. I do not want to patch the other DC's at this time as I would rather keep them at bay until MS fixes all this in a DEC rollup or Security patch.     

How can I fix my 1 DC? Seems crazy that something like the patches can bust the domain , I can't imagine if I had installed this on all the DC's, we'd be down with all sorts of issues.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2022-12-07*

Hi,    

Install the following update on all domain controllers to fix the kerberos issue:       

november-17-2022-kb5021655    

november-17-2022-kb5021654    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-12-07*

Something here could help.    

https://dirteam.com/sander/2022/11/11/knowledgebase-you-experience-errors-with-event-id-14-and-source-kerberos-key-distribution-center-on-domain-controllers/    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-07*

Replication is broken along with my other DC's not being able to see it when doing NSlookup. Nor can my 1 DC that has the Nov 17th patch KB5021654 see the other DC's. Keep in mind , initially it had the Nov 8th patch installed. When I found things were broken, I uninstalled it and things were still not working. Then I installed the Nov 17th patch KB5021654.       

Errors in System log point to the patch being the issue based off the errors I am seeing. When checking dcdiag from an unaffected DC it shows the remote system is not available and "the target principal name is incorrect" repadmin /showrepl.    

This all started the day this patch was installed.     

Also when doing NSLookup on DC with patch it shows "unknown" as it's name and then the IP address.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-06*

Patches Broke my Domain controller    

What is broken? What operating systems are used?
