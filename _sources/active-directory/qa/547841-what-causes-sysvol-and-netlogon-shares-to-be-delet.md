---
title: "What Causes SYSVOL and NETLOGON Shares to be Deleted?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/547841/what-causes-sysvol-and-netlogon-shares-to-be-delet
question_id: 547841
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# What Causes SYSVOL and NETLOGON Shares to be Deleted?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/547841/what-causes-sysvol-and-netlogon-shares-to-be-delet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a perplexing problem on a test network I have.  It was the victim of a ransomware attack recently but, being a test network, all of the encryption didn't really cause a problem.  However, none of the DC's work now.  If I try to open any of the AD** utilities, they tell me that the domain doesn't exist.  After some initial troubleshooting, I discovered that the SYSVOL and NETLOGON shares had been deleted.  The strange part is that I copied the vhdx file for a DC on another network and spun it up as the only running DC on the network.  Its shares ended up deleted as well.  Even after manually recreating the shares and rebooting, the shares were gone again.  

So, what would cause these shares to be deleted?  Since this is the only DC on the network now, it can't be a replication or GPO issue.  DNS appears to be solid so it can't be the problem, either.  Scratching my head...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-13*

Hello MsTech,     

This sounds like a common issue after you restore a DC, and it forces authoritative synchronization.    

Please check this document that explains the checklist and troubleshooting: https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/missing-sysvol-and-netlogon-shares    

Initially I would try the next:    

-  Open the registry and navigate to "HKLM\System\CurrentControlSet\Services\NtFrs\Parameters"    

-  Change value for "Enable Journal Wrap Automatic Restore" from 0 to 1. If the DWORD Value does not exist, create a new one, including spaces but without the quotes.    

-  Stop the NTFRS Service (from an elevated command prompt and type "net stop ntfrs")    

-  Start the NTFRS Service (net start ntfrs)    

-  Check for File Replication Services events in Event Viewer:    

• 13553 – The DC is performing the recovery process.    

• 13554 – The DC is ready to pull the replica from another DC.     

• 13516 - If you receive this Event ID everything went fine, then you can continue:    

-  From the elevated command prompt type: "net share" and look for SYSVOL and NETLOGON. The issue will be resolved when the new SYSVOL replica from a peer Domain Controller. This may take some minutes.    

-  Revert the value for "Enable Journal Wrap Automatic Restore" from 1 to 0.            

Hope this helps in your case,    

Best regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-10*

But, there is only one DC so how could replication be a/the problem?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-10*

May be hopeless because of the malware but if DFSR is used    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

or for FRS    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/missing-sysvol-and-netlogon-shares    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
