---
title: "Deploying AV via GPO, having problems!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196866/deploying-av-via-gpo-having-problems
question_id: 2196866
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy"]
---
# Deploying AV via GPO, having problems!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196866/deploying-av-via-gpo-having-problems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am in the process of trying to deploy our endpoint security to about 50 PCs.  I created a test OU and placed my PC in it. Created a GPO to install the MSI that is shared on our server.  What I figured out is that it won't install automatically on my standard user account.  If I open a cmd and run gpudate /force it will come up with a message saying to hit yes/no to restart and then it will install.  If I set my account as a local admin it is automatic and I don't need to run gpudate /force and then enter yes.  Is this normal? Is there anyway that I can deploy automatically when standard users without manually running the gpudate /force command?  Thanks for any help!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-20*

Hello Dan Meyer2,  

Thank you for posting in Microsoft Community forum.  

For deploying software installation via gpo, you need to restart the client machine (instead of running gpupdate /force command) one or two time to make the software to install.  

Then software will install automatically when standard users sign in.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
