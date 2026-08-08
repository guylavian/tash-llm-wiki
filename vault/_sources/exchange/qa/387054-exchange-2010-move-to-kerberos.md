---
title: "Exchange 2010 move to Kerberos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387054/exchange-2010-move-to-kerberos
question_id: 387054
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2010 move to Kerberos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387054/exchange-2010-move-to-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are moving an Exchange 2010 cluster to Kerberos in prep for migration to Exchange online and have run into a problem regarding the script "ConvertOABDir.ps1". According to a few different sites I need to do the following:  

-  Create an ASA computer account.  

-  Run the script: .\RollAlternateserviceAccountPassword.ps1 -ToArrayMembers {CAS array name} -GenerateNewPasswordFor "{Domain}{ASA}" –Verbose  

(This script appears to be located in the SP3 scripts directory)  

-  Convert OAB virtual directory to web application with the script ConvertOABDir.ps1, just download and run.  

The problem is I can't find that script. All the links that have been provided to Microsoft don't have this file. Searching Microsoft can't find this file. The closest I can get is post here which appears to have pasted the contents but I can't validate whether or not this is the actual script, unchanged for Exchange 2010 SP3.  

https://social.technet.microsoft.com/Forums/lync/en-US/ab5409ff-f20c-4d66-a261-c3c73f01a919/cant-enable-kerberos-in-outlook-and-exchange-2013-bug-in-convertoabvdirps1?forum=exchangesvrclients  

Can anyone help? Or is there a different way to achieve this same goal?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-10*

Hmm, not sure what you are referring to, but there is no relationship between kerberos and migrating to Exchange Online. :)   

Moving to Kerberos auth only makes sense if you want to reduce the load mail clients have on Domain controllers, otherwise there is no reason to introduce this change now and it doesn't buy you anything if you are moving to Exchange Online.   

Another thing to remember is that kerberos auth only works for domain-joined clients, so enabling this wont make a difference for non-domain joined clients and won't have any benefit for this  that you mentioned above "One of the strongly recommended things to do is to NOT allow NTLM traffic outside of your organization"

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-10*

This is Exchange 2010. THAT script is not on either server. However I've modified my search and found the file "convertoabvdir.ps1". Is that the same thing?  

Edit: this is in the SP3 install directories. I assume it's the same but would like to know for sure.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-10*

Hi,    

It's still in %Exchangeinstallpath\scripts folder in Exchange2016:    

    

In case your folder not complete, I post it here in txt:    

95045-1.txt    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
