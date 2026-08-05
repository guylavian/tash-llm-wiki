---
title: "AD server with all FSMO roles installed got crashed and no longer accessible"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1044976/ad-server-with-all-fsmo-roles-installed-got-crashe
question_id: 1044976
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
---
# AD server with all FSMO roles installed got crashed and no longer accessible

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1044976/ad-server-with-all-fsmo-roles-installed-got-crashe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have one AD/DNS server with all FSMO roles installed. Now that server is not switching on. I am not able to access additional domain controller as it says "Naming information cannot be located because: specified domain either doesnot exist or could not be contacted".    

Can any one help me to troublehoot this, as the primary DC will no longer available.    

Thanks    

Suravind

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-13*

Hello there,    

You can seize the FSMO role, but never & ever connect the DC with whom you have seized the FSMO role, even though its works fine post-seizing the FSMO role. The right method is once the role has been seized from the DC perform the metadata cleanup of the failed DC & allowed it to replicate the changes & freshly install the OS on crashed DC not mandatory but a good way to go.    

The error "The Specified Domain Either Does Not Exist or Could Not Be Contacted" commonly occurs due to invalid DNS settings on the workstation's side because Active directory requires you to use domain DNS to work properly.    

To resolve the "Specified Domain Does Not Exist or Could Not Be Contacted" error, you have to set the Preferred DNS IP to point to Primary Domain Controller's IP address, on each client workstation that you want to join in the domain.     

The below thread discusses the same issue and you can try out some troubleshooting steps from this and see if that helps you to sort the Issue.    

https://social.technet.microsoft.com/Forums/en-US/091a1ea6-88c3-4a43-96eb-3969cd90c20a/the-specified-domain-either-does-not-exist-or-could-not-be-contacted?forum=winserver8gen    

https://social.technet.microsoft.com/Forums/windowsserver/en-US/4fcce8da-5b34-416d-8aed-4fe0074e2058/what-if-a-dc-fails-that-had-all-fsmo-roles?forum=winserverDS    

--------------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
