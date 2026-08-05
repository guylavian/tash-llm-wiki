---
title: "Prerequisites for Microsoft Exchange Server 2019 installation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/228321/prerequisites-for-microsoft-exchange-server-2019-i
question_id: 228321
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Prerequisites for Microsoft Exchange Server 2019 installation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/228321/prerequisites-for-microsoft-exchange-server-2019-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Recently I read prerequisites and watched a video.  

As per prerequisites; 128 GB RAM for Mail box server for production environment and 64 GB RAM for edge Transport server room required. For Testing, 8GB RAM is required. And 30GB free space for mail server installation is required.  

In the video, there is Windows Server 2019 Domain Controller and there is a member server which is also Windows Server 2019. All applications (Dot Net framework 4.8, Visual C++ Redistribution Package for Visual Studio 2013, Unified Communication Managed API 4.0 and Exchange Server 2019) were installed in the member server. Moreover, Exchange Server 2019 has been installed using Windows PowerShell command.   

Please let me know;  

-  Is it mandatory to have a member server in the domain network for setup and installation Exchange Server 2019?  

-  Can I setup Exchange Server 2019 at Active Directory-Domain Controller system?  

-  In the video, first Windows Server system joined the AD-DC system, then required application installed. Before joining the AD-DC system, can I install Dot Net framework 4.8, Visual C++ Redistribution Package for Visual Studio 2013, Unified Communication Managed API 4.0 and Windows components in member server?  

-  Exchange Server 2019 has been installed using Windows PowerShell. Can I install it using setup.exe through GUI steps?  

-  If member server is mandatory for setup Exchange Server, hardware configuration of member server must be high (as mentioned above). Am I right?  

Please clarify and elaborate. I’ll be thankful for your help.  

With Regards  

NndnG

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

anonymous userDavid and @Anonymous   I am thankful to both of you for elaborating and sharing links.    

At the end of explanations, I understood as    

-  Exchange Server must be setup, installed and configured at member server.    

-  All prerequisite applications can be installed in member server before joining the AD-DC computer but before installing Exchange Server 2019, the member server must join the AD-DC computer.    

Am I right?     

Moreover, please let me know,    

-  Hardware specification of member server must be high because of various reasons but for training or lab purpose generally we do all setup at virtual machine. And because of some limitations, for a virtual machine, higher specification (specially high RAM) is difficult. Can I setup member server with 4GB or 6GB RAM for training or lab purpose?    

-  On which computer, do we have to install Capacity calculator?    

Pls advise and guide me. Thank you in advance.     

With Regards    

NndnG

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-13*

Hi @NndnG   ,    

For your questions, I agree with Andy.    

In addition, I would like to provide you some steps about installing Exchange server.     

For example, you have 2 x Windows server 2019 and one is the domain controller, the other one is the member server.    

-  On the DC server, open server manager -> add roles and features -> add Active Directory Domain Services.    

     

-  Then promote the AD server to a domain controller, after the installation, you will need to restart the server to finish the changes.    

     

-  On the Member server(which is going to install Exchange), specify the DNS address and join the domain.    

        

-  On the Member server, install .Net Framework 4.8, Visual C++ Redistributable Package for Visual Studio 2012, Visual C++ Redistributable Package for Visual Studio 2013 and run Install-WindowsFeature RSAT-ADDS in PowerShell for preparing AD and installing Mailbox server.     

Add the required Lync server or Skype for Business Server components: Install-WindowsFeature Server-Media-Foundation, and Install Unified Communications Managed API 4.0.    

-  After these, you can use the Setup Wizard or unattended mode to install Exchange server.    

This article describes the prerequisites of Exchange 2019 installation: Exchange Server 2019 prerequisites.    

As for the hardware requirements, it is better to deploy a high configuration, but it’s not required. Here is an article about the RAM: Why Exchange 2019 Demands 128 GB Minimum Server Memory.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Also you could use the Capacity Calculator(URL has been given by Andy) to determine the hardware configuration of the server.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
