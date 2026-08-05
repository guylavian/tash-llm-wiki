---
title: "Need help for Windows Domain Controller certificate enrollment - RPC server is unavailable. 0x800706ba"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196877/need-help-for-windows-domain-controller-certificat
question_id: 2196877
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Need help for Windows Domain Controller certificate enrollment - RPC server is unavailable. 0x800706ba

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196877/need-help-for-windows-domain-controller-certificat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So, I've been troubleshooting this for the past week. I have an offline root CA and a sub CA setup. I setup a cert template for autoenrollment 'ABC Domain Controller Authentication'. Autoenrollment is not working and it's failing even if I try to manually request a new cert from the DC.

Certificate enrollment for Local system failed in authentication to all urls for enrollment server associated with policy id: {9A03AADF-BD83-4A2D-AEE7-751976512571} (The RPC server is unavailable. 0x800706ba (WIN32: 1722 RPC_S_SERVER_UNAVAILABLE)). Failed to enroll for template: ABCDomainControllerAuthentication.

I've read so many articles and tried so many things with no luck and coming here for some help.

I tried everything here with no luck.

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/error-0x800706ba-certificate-enrollment

I made changes to the 'Certificate Service DCOM Access' group on the CA - no luck.

I even disabled the fw on both the CA and the DC, no luck. On the CA server there are 4 fw entries all enabled - TCP 135, TCP 445, TCP RPC Endpoint Manager, TCP RPC Dynamic Ports.

Any help would be so appreciated!

Certificate enrollment for Local system failed in authentication to all urls for enrollment server associated with policy id: {9A03AADF-BD83-4A2D-AEE7-751976512571} (The RPC server is unavailable. 0x800706ba (WIN32: 1722 RPC_S_SERVER_UNAVAILABLE)). Failed to enroll for template: ABCDomainControllerAuthentication.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-23*

Hello Brian Strain (IT),  

Thank you for posting in Microsoft Community forum.

Is your sub CA server also a Domain Controller?

1.Check the “Authenticated Users” group is in the “Certificate Service DCOM Access” group in Active Directory Users and Computers, it is correct. 

2.Check the Built-in\Users group includes the following member groups: Authenticated Users, Domain Users and INTERACTIVE, it is correct. 

3.Check the DCOM Access Limit of “My Computer” of the DC and CA server.   

  

4.Check whether we have edited the local group policy before on the CA and DC server:  

4-1Start > Run > gpedit.msc > OK

4-2Expand: Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options

4-3Check the Security Setting of "DCOM: Machine Access Restrictions in Security Descriptor Definition Language (SDDL) syntax" and "DCOM: Machine Launch Restrictions in Security Descriptor Definition Language (SDDL) syntax".  

4-4The default Security Settings is Not Defined. If the Security Settings of both is Not Defined, we do not need to do anything.  

4-5If we have edited any one of them, and the Edit Limits button is greyed out.

5.Check the port 135,88 and 389.

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
