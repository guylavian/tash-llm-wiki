---
title: "Removing Active Directory Locked all accounts on the Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191854/removing-active-directory-locked-all-accounts-on-t
question_id: 1191854
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Removing Active Directory Locked all accounts on the Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191854/removing-active-directory-locked-all-accounts-on-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello I was wondering if I could get help. 

I install Active Directory on my server but realise I didn't want to use it anymore and decided to remove it. 

I was able to login as domain\user priory to removing Active Directory. 

After removing Active Directory (following the steps) I can no longer log into my server I tried using domain\user (which should work) and just the username (which should work but am getting the following

I can logging into the system via the Ionos KVM console which doesn't show me much,  trying to use the same user i get the message above. 

I have check for the other users I created priory to Adding AD  but there doesn't seem to be any other users but the folder users does still contain the user info's and my apps, systems are all still running

Am not a server guru so any help would really really be appreciated. 

Thanks in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-22*

Hello there,

Disabled computer accounts in AD will not prevent local logons if the machine is not connected to the domain.

Also if the computer is deleted from AD it will not prevent local logons, even with "some" domain user accounts as they use cached credentials, because the computer may not "know" about the deleting from the domain.

When a computer object is deleted from AD, and AD doesn't have the computer's object or password it its database. So what happens to the computer? The trust relationship between the computer an AD is broken because it cannot authenticate to the domain because the AD doesn't have its password anymore. computer's local secret cannot be used to authenticate the computer object then.

Similar discussion here

https://social.technet.microsoft.com/Forums/Lync/en-US/a7b9bc35-3737-4468-899e-55e181bf04fc/what-actually-happen-when-i-delete-computer-account-from-active-directory?forum=winserverDS#:~:text=When%20a%20computer%20object%20is,t%20have%20its%20password%20anymore.

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
