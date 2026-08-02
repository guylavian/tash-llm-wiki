---
title: "Exchange 2019 minimum memory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192589/exchange-2019-minimum-memory
question_id: 192589
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2019 minimum memory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192589/exchange-2019-minimum-memory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We're in the process of installing a couple of Exchange 2019 (physical) servers in a small test environment.  

I understand the Microsoft recommended minimums for memory - I'm not asking about that, thanks.  

It seems to run OK in 8GB, the only issue is that some of the Exchange services don't start after booting the system. They apparently time out but they can be started again manually and everything seems to be fine at that point.  

Just curious what experience others have had with Exchange 2019 running on a machine with 8 or 16 GB of memory?  

Again, not interested in hearing about Microsofts recommendations for this, just asking what specific experience others have had running Exchange 2019 in a test environment with a minimum amount of memory.  

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-12-28*

I was following Paul Cunningham's latest course on Exchange at Pluralsight. He stated that 8 GiB was enough for a trial with Exchange Server 2019. So I created several VMs in Azure using B2 machines with 8 GiB. It worked. Respons times with 16 GiB, which I tried with one machine was better, but not worth the cost.  

Actually, I think 16 GiB could be fine for production, not close to the recommended 128.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-10*

Thanks for your response YukiSun!  

I suspect my Exchange 2019 services are timing out right after the system is booted because the hardware is a low end dual-core and the CPU is maxed out for a few minutes at boot time.  (This is a fresh installation on Windows 2019 Server Core). Your machine is much faster than mine.  I had the same issue when Exchange 2016 was new - I tried running it in the same 4gb that Exchange 2010 ran successfully in and ended up increasing memory to 8gb which Exchange 2016 was happy with.  

I've been supporting Exchange since 4.0 and I'm familiar with all of the supported pre-requisites.  However Microsoft is making it more difficult all the time for people to build simple test environments to help support on-premises Microsoft products.  128gb is not a practical requirement for a test box that may only support one test user and have a short life - its too expensive, especially if you are an independent consultant who has to pay for it.   

I will add some more memory - I was just trying to get a feel for the minimum practical requirement for a test box that was not supporting any production mailboxes.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-10*

Hi @SamT  ,    

I happened to have an freshly created Exchange 2019 lab environment with 8GB memeory, and so far haven't experienced the issue described in your post.     

    

Upon the boot of the sysmtem(Windows Server 2019), the Exchange related services can run properly. From the screenshot below, we can see that only the Microsoft exchange service broker is stopped, which is an expected behavior, see Lynn's explanation in this thread.     

    

With the above being said, considering that as you may have known, the official recommended minimum memory for Exchange 2019 mailbox server is 128 GB, and the memory consumption may depend on the load, personally I'd like to suggest try increasing the memory when encountering performance issues. Actually I am wondering that perhaps I haven't seen issues in my 8GB lab because it's a totally new environment with only 2 test mailboxes.     

Here's a blog about the memory needs in Exchange 2019 for your reference:    

Why Exchange 2019 Demands 128 GB Minimum Server Memory    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Hope the information above could be helpful.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
