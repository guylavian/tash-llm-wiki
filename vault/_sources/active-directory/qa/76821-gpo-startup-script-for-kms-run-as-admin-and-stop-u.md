---
title: "GPO StartUp Script for KMS Run as Admin and Stop User Prompts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/76821/gpo-startup-script-for-kms-run-as-admin-and-stop-u
question_id: 76821
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO StartUp Script for KMS Run as Admin and Stop User Prompts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/76821/gpo-startup-script-for-kms-run-as-admin-and-stop-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have 2 Data Centers which are connected to the same AD's Structure through a VPN tunnel. We have two KMS Servers due to using a VDI solution, if they is a fail-over we need to be able to License the newly created machines. KMS DNS setup only works when using a single KMS Server. The work around is to manually set a the KMS Server and the Windows 10 GVLK with a Batch File.     

I have done this as a start up script through GPO. The GPO is working and applying however the script does not seem to be running. I am 100% sure the GPO is working and starting the script because the logs are returning a error code 0. I think the issue is a combination of admin permissions and user prompts when the script is run.     

I could use some help with making sure the script is running as an admin and is not have permission errors.     

I also need help modifying the script so it runs either with out User Notification Prompts or just ignores them completely.     

The script is     

@Echo   OFF    

slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX    

slmgr /skms "KMS Server FQDN":1688    

slmgr /ato    

After the slmgr /ipk and Slmgr /skms commands there is a popup letting you know that the command run and requires you to hit enter to continue.     

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-03*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-31*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-26*

Hi,  

Thank you for posting in our forum.  

According to my judgment, this problem may be a scripting problem.  

I recommend you to post to the script forum, they can give you more professional help  

Hope this information can help you  

Best wishes  

Vicky
