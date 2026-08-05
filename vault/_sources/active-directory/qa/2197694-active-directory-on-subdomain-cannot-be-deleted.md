---
title: "Active directory on subdomain cannot be deleted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197694/active-directory-on-subdomain-cannot-be-deleted
question_id: 2197694
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory on subdomain cannot be deleted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197694/active-directory-on-subdomain-cannot-be-deleted (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am unsure where to start, as a professional installed and set up our server. He has the physical machine as the main domain and a virtual machine as the subdomain, both with an active directory. The active directories are supposed to replicate each other, meaning a user on the physical machine will automatically be a user of the virtual machine and more data consistency in general. 

It all worked for a month or so. Then, an event occurred (no one knows what), and the virtual and physical machines stopped communicating and replicating. This caused speed and other issues, mainly though new devices could not be added to the domain. And somehow, the virtual machine acts as if it was the main domain.

After many failed attempts to remedy the situation, the expert tried deleting the active directory, which also failed. Demoting the virtual machine to a subdomain failed. Basically, any attempt to fix the situation failed.

One of the error codes he came across was fatal win32 error 8440.  

My questions:  

-  is it necessary for a single application to set up a virtual machine with replicating active directories? (The explanation was that in case of a hardware failure, it would be quicker to set up a replacement server)  

-  Should I find another professional?  

-  Could a hardware or software problem cause these issues?  

I need this to be fixed. What is my best course of action?  

PS: I tried to describe the situation as best as I could. I am not an expert.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-12*

Hello linmen,  

Thank you for posting in Microsoft Community forum.  

Here are the answers for your references.  

-  is it necessary for a single application to set up a virtual machine with replicating active directories? (The explanation was that in case of a hardware failure, it would be quicker to set up a replacement server)  

A1: I understand you are asking if you need more than one Domain Controller in one domain, am I right? If so, yes, we suggest you had better set up two DCs in one domain. If there is hardware issue that cannot be fixed on the first DC, we can use the other one.  

-  Should I find another professional?  

A2: If you want to troubleshoot or fix this problem, we can try our best to help you.  

-  Could a hardware or software problem cause these issues?  

A3: Yes, it may be.  

For the AD replication status, you can check it by running commands below on PDC.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv

Here is a similar thread for your reference.

Replication Error : SyncAll exited with fatal Win32 error. | Microsoft Learn  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
