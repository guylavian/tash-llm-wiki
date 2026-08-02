---
title: "Active Directory and ARM64 Laptops"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3897097/active-directory-and-arm64-laptops
question_id: 3897097
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-home-windows-11-platform-security-privacy", "windows-server"]
answer_author_roles: ["Volunteer Moderator"]
---
# Active Directory and ARM64 Laptops

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3897097/active-directory-and-arm64-laptops (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Our environment is slowly switching to ARM64 Architecture, and as an IT team here, we cannot utilize Active Directory since it's not compatible with ARM as far as we are aware.  We have to create a VDI instance and use AD there, and it's counterproductive to what we need, but the battery life and other functions are what we are looking for in a laptop that's not named Apple.

My question is, when will Microsoft allow AD to work on ARM64 Architecture and if there are alternatives to AD that we can utilize on ARM64.

Thanks,

Giuseppe DeFabrizio

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2025-02-24*

Giuseppe,

The correct way to say this is that these Microsoft Community forums are here to support primarily consumer and tiny business users using Microsoft accounts, not anything related to larger businesses using either Active Directory, servers, or other mass management tools that those businesses typically require.

That's what the Microsoft Learn document structure and the associated Q&A Forums are for, so few here will even understand what you're asking, let alone be able to provide a useful answer.

However, since my own background included medium sized business administration using Active Directory, servers, and similar concepts, I at least can look for the types of information you might want to view to understand your situation and provide a path to the correct forums where these can be discussed.  Here's what I found in a quick search which I'm sure you can use to find more useful information relating to your specific needs.

Here's a Q&A Forums thread discussing RSAT and ARM, that gave me some idea of the likely problems you're experiencing.

Are there plans to make RSAT available for the ARM Processors? - Microsoft Q&A

Here's the link provided within one of the posts in that thread to the Microsoft Learn deployment and management page that explains the support provided for these devices.  Use the index provided on the left-hand side of that page to select the other article related to Arm devices.

Deploy, manage, and service Arm processor-based Surface devices - Surface | Microsoft Learn

From what I read in that thread; it appears that Microsoft is assuming those using Arm devices will also be using these more modern cloud-based support tools and not the older Active Directory ones more typically associated with standalone server use in isolated business operations.  That's also what the document linked seems to imply, so that's likely why you're struggling to make these two dissimilar environments work with each other, since the entire management structure appears to have changed.

Since I have no direct experience, as I left my administrative position over a decade ago, that's the reason you should discuss these issues with others in the Q&A Forums that were recommended, since Microsoft Learn is the documentation structure that has been provided for IT professionals going on a decade now as well, with these Community Forums for consumers as I mentioned earlier.

Rob

< EDIT > Since it's now becoming public at the top of threads in at least the Q&A Forums, I'll note that the Microsoft Community and Q&A forums are in the process of being merged to reduce the confusion this situation has caused for many in both communities, so relatively soon, you'd be asking this question in the same place and not be needing to be redirected.  Though this situation has existed for nearly a decade since the older TechNet and MSDN Developer documentation and forum structures evolved to become Microsoft Learn, Microsoft finally decided that trying to maintain two separate structures for IT professionals and consumers was simply confusing, and thus the final evolution to combine these is in the process of occurring as we speak.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-24*

Hello, this is not Windows Server related.  We are using Lenovo SnapDragon laptops for regular business use and our IT team here can't access Active Directory and RSAT Tools so we can do our everyday work.  Seems like there are limitations between the ARM64-based systems and Microsoft.  The only way we can work around this is to utilize a Virtual Instance or Remote into a server to use RSAT Tools.  Do we know when Microsoft will have their tools work with ARM64?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-14*

Hi Giuseppe, 

Welcome to Microsoft Community.
I wish I could handle your problem; however, it is more suitable for publishing on Microsoft Learn (English only), more users post these issues there, you can click on "Ask a question", there are experts who can provide more professional solutions in that place.Here is a link [Windows Server - Microsoft Q&A] to the forum where you can raise specific scenarios and share your idea to help solve the problem.I sincerely hope that your question will be dealt with appropriately after contact the correct department. Thank you for your understanding!
Your Sincerely
Hahn. W - MSFT | Microsoft Community Support Specialist
