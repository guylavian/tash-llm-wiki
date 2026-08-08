---
title: "I am having issues with DSC Domain Controller promotion"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193113/i-am-having-issues-with-dsc-domain-controller-prom
question_id: 2193113
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# I am having issues with DSC Domain Controller promotion

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193113/i-am-having-issues-with-dsc-domain-controller-prom (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I would like to ask about DSC Domain controller promotion with command ADDomainController.

When I try to promote server manually with the same account, it is working fine.

When promoting via DSC, I am receiving errors on the VM and the process is stuck and cannot be finished.

The error logs are:

DNS installation - ok  

Group policy installation - ok  

Configuring the local computer to host Active Directory Domain Services Active Directory Domain Services successfully deleted the \Registry\Machine\System\CurrentControlSet\Services\NTDS registry key (DeleteRoot=0  

The attempted domain controller operation has completed  

An unknown error occurred while installing Active Directory Domain Services  

Active Directory Domain Services was not installed The Directory Service Event logs: The Active Directory Domain Services Installation Wizard (Dcpromo) was unable to establish connection with the following domain controller.  

Additional Data Error value: 1749 The security context is invalid.  

Internal event: The local directory service received an exception from a remote procedure call (RPC) connection.  

Extended error information is not available.  

Additional Data Error value: The security context is invalid. (1749) Attempting to set the desired authentication protocol for a connection to the following DSA failed. Additional Data: Error: 1749 The security context is invalid.

Could somebody please advise what could be the issue ?

Thanks

Jan

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-18*

Hi JanJanza,

Thank you for posting in the Microsoft Community Forum.

The error message indicates a problem establishing a connection with the domain controller and suggests that there may be an issue with the security context or authentication protocol during the promotion process.

Here are some troubleshooting steps you can try to resolve this issue:

-  Check Network Connectivity: Ensure that the server being promoted to a domain controller has proper network connectivity to the domain controllers in the domain. Verify that there are no network issues or firewall restrictions blocking communication.

-  Verify Credentials: Double-check the credentials being used for the DSC configuration. Ensure that the account has sufficient permissions to perform the domain controller promotion operation.

-  Review DSC Configuration: Check the DSC configuration script to ensure that all parameters and settings are correctly specified. Pay special attention to any parameters related to domain controller promotion and authentication.

-  Test DSC Configuration: Try running the DSC configuration script on a test environment or another server to see if the issue persists. This can help isolate whether the problem is specific to the server being promoted or if it's a broader issue with the DSC configuration.

-  Review Event Logs: Examine the event logs on both the server being promoted and the domain controllers for any relevant error messages or warnings. Look for any clues that might indicate the cause of the connection or authentication failure.

-  Check DNS Configuration: Ensure that the DNS settings on the server being promoted are correctly configured to point to the domain controllers in the domain. DNS resolution issues can sometimes cause problems during domain controller promotion.

-  Verify Time Synchronization: Check that the system time on the server being promoted is synchronized with the domain controllers. Time discrepancies can cause authentication issues in Active Directory environments.

By following these steps, you should be able to identify and resolve the issues preventing successful domain controller promotion using DSC.

Best regards

Neuvi Jiang
