---
title: "Active Directory network problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197678/active-directory-network-problem
question_id: 2197678
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active Directory network problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197678/active-directory-network-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

A few nights ago, the power went out and after the UPS was fully uncharged, the servers were turned off. Starting tomorrow, strange problems were observed on the network.  

-1. After turning on the clients, they did not show the domain name (fsm.local) under the NIC in network adapter section, and only displayed the word “network”.  

2. Replicate between two Active Directories gave an error in DCDIAG.  

3. Users who were connecting to a program from outside via “Citrix Store Front”, no longer could connect, Citrix Receiver says “Access Denied”.  

4. we have problem with GPUPDATE, [lack of network connectivity].  

By searching the Internet, I first tried to solve the problem of the domain name not being displayed in clients’ NIC. Then I realized that Replicate did not exist and I tried to solve the problem with commands to fix DFSR, but it did not work.  

I have included the dcdig information below.  

Thank you for your guidance so that I can solve this problem.

Directory Server Diagnosis  

Performing initial setup:  

   Trying to find home server...  

   Home Server = SRV-AD  

   * Identified AD Forest.  

   Done gathering initial info.  

Doing initial required tests  

   Testing server: Default-First-Site-Name\SRV-AD  

```
Starting test: Connectivity  

     ......................... SRV-AD passed test Connectivity
```

Doing primary tests  

   Testing server: Default-First-Site-Name\SRV-AD  

```
Starting test: Advertising  

     ......................... SRV-AD passed test Advertising  

  Starting test: FrsEvent  

     ......................... SRV-AD passed test FrsEvent  

  Starting test: DFSREvent  

     There are warning or error events within the last 24 hours after the  

     SYSVOL has been shared.  Failing SYSVOL replication problems may cause  

     Group Policy problems.  

     ......................... SRV-AD failed test DFSREvent  

  Starting test: SysVolCheck  

     ......................... SRV-AD passed test SysVolCheck  

  Starting test: KccEvent  

     A warning event occurred.  EventID: 0x80000BEB  

        Time Generated: 01/07/2025   11:37:36  

        Event String:  

        The directory has been configured to not enforce per-attribute authorization during LDAP add operations. Warning events will be logged, but no requests will be blocked.    

     A warning event occurred.  EventID: 0x80000BEE  

        Time Generated: 01/07/2025   11:37:36  

        Event String:  

        The directory has been configured to allow implicit owner privileges when initially setting or modifying the nTSecurityDescriptor attribute during LDAP add and modify operations. Warning events will be logged, but no requests will be blocked.    

     A warning event occurred.  EventID: 0x8000087A  

        Time Generated: 01/07/2025   11:37:37  

        Event String: A Generation ID change has been detected.    

     A warning event occurred.  EventID: 0x80000B46  

        Time Generated: 01/07/2025   11:37:47  

        Event String:  

        The security of this directory server can be significantly enhanced by configuring the server to reject SASL (Negotiate, Kerberos, NTLM, or Digest) LDAP binds that do not request signing (integrity verification) and LDAP simple binds that are performed on a clear text (non-SSL/TLS-encrypted) connection.  Even if no clients are using such binds, configuring the server to reject them will improve the security of this server.    

     A warning event occurred.  EventID: 0x80000BE1  

        Time Generated: 01/07/2025   11:37:47  

        Event String:  

        The security of this directory server can be significantly enhanced by configuring the server to enforce  validation of Channel Binding Tokens received in LDAP bind requests sent over LDAPS connections. Even if  no clients are issuing LDAP bind requests over LDAPS, configuring the server to validate Channel Binding  Tokens will improve the security of this server.    

     A warning event occurred.  EventID: 0x8000082C  

        Time Generated: 01/07/2025   11:38:18  

        Event String:    

     A warning event occurred.  EventID: 0x8000082C  

        Time Generated: 01/07/2025   11:38:48  

        Event String:    

     A warning event occurred.  EventID: 0x8000082C  

        Time Generated: 01/07/2025   11:39:18  

        Event String:    

     A warning event occurred.  EventID: 0x8000082C  

        Time Generated: 01/07/2025   11:39:48  

        Event String:    

     A warning event occurred.  EventID: 0x8000051C  

        Time Generated: 01/07/2025   11:42:48  

        Event String:  

        The Knowledge Consistency Checker (KCC) has detected that successive attempts to replicate with the following directory service has consistently failed.    

     ......................... SRV-AD passed test KccEvent  

  Starting test: KnowsOfRoleHolders  

     ......................... SRV-AD passed test KnowsOfRoleHolders  

  Starting test: MachineAccount  

     ......................... SRV-AD passed test MachineAccount  

  Starting test: NCSecDesc  

     ......................... SRV-AD passed test NCSecDesc  

  Starting test: NetLogons  

     ......................... SRV-AD passed test NetLogons  

  Starting test: ObjectsReplicated  

     ......................... SRV-AD passed test ObjectsReplicated  

  Starting test: Replications  

     [Replications Check,SRV-AD] A recent replication attempt failed:  

        From SRV-AD-REP to SRV-AD  

        Naming Context: DC=ForestDnsZones,DC=fsm,DC=local  

        The replication generated an error (1908):  

        Could not find the domain controller for this domain.  

        The failure occurred at 2025-01-07 11:38:25.  

        The last success occurred at 2025-01-07 08:24:03.  

        2 failures have occurred since the last success.  

        Kerberos Error.  

        A KDC was not found to authenticate the call.  

        Check that sufficient domain controllers are available.  

     [Replications Check,SRV-AD] A recent replication attempt failed:  

        From SRV-AD-REP to SRV-AD  

        Naming Context: CN=Schema,CN=Configuration,DC=fsm,DC=local  

        The replication generated an error (1908):  

        Could not find the domain controller for this domain.  

        The failure occurred at 2025-01-07 11:38:24.  

        The last success occurred at 2025-01-07 09:24:23.  

        1 failures have occurred since the last success.  

        Kerberos Error.  

        A KDC was not found to authenticate the call.  

        Check that sufficient domain controllers are available.  

     [Replications Check,SRV-AD] A recent replication attempt failed:  

        From SRV-AD-REP to SRV-AD  

        Naming Context: CN=Configuration,DC=fsm,DC=local  

        The replication generated an error (1908):  

        Could not find the domain controller for this domain.  

        The failure occurred at 2025-01-07 11:38:24.  

        The last success occurred at 2025-01-07 09:24:23.  

        1 failures have occurred since the last success.  

        Kerberos Error.  

        A KDC was not found to authenticate the call.  

        Check that sufficient domain controllers are available.  

     ......................... SRV-AD failed test Replications  

  Starting test: RidManager  

     ......................... SRV-AD passed test RidManager  

  Starting test: Services  

     ......................... SRV-AD passed test Services  

  Starting test: SystemLog  

     An error event occurred.  EventID: 0x80001778  

        Time Generated: 01/07/2025   11:37:43  

        Event String:  

        The previous system shutdown at 9:30:53 AM on 1/7/2025 was unexpected.  

     A warning event occurred.  EventID: 0x000727AA  

        Time Generated: 01/07/2025   11:38:26  

        Event String:  

        The WinRM service failed to create the following SPNs: WSMAN/SRV-AD.fsm.local; WSMAN/SRV-AD.    

     An error event occurred.  EventID: 0x00000029  

        Time Generated: 01/07/2025   11:36:52  

        Event String:  

        The system has rebooted without cleanly shutting down first. This error could be caused if the system stopped responding, crashed, or lost power unexpectedly.  

     An error event occurred.  EventID: 0x40000004  

        Time Generated: 01/07/2025   11:38:32  

        Event String:  

        The Kerberos client received a KRB\_AP\_ERR\_MODIFIED error from the server srv-ad-rep$. The target name used was DNS/srv-ad-rep.fsm.local. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (FSM.LOCAL) is different from the client domain (FSM.LOCAL), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.  

     A warning event occurred.  EventID: 0x00001796  

        Time Generated: 01/07/2025   11:38:33  

        Event String:  

        Microsoft Windows Server has detected that NTLM authentication is presently being used between clients and this server. This event occurs once per boot of the server on the first time a client uses NTLM with this server.   

     An error event occurred.  EventID: 0x0000410B  

        Time Generated: 01/07/2025   11:38:18  

        Event String:  

        The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is    

     A warning event occurred.  EventID: 0x0000A00A  

        Time Generated: 01/07/2025   11:38:23  

        Event String:  

        The Security System has detected a downgrade attempt when contacting the 3-part SPN    

     A warning event occurred.  EventID: 0x0000A00A  

        Time Generated: 01/07/2025   11:38:23  

        Event String:  

        The Security System has detected a downgrade attempt when contacting the 3-part SPN    

     A warning event occurred.  EventID: 0x0000A00A  

        Time Generated: 01/07/2025   11:38:23  

        Event String:  

        The Security System has detected a downgrade attempt when contacting the 3-part SPN    

     A warning event occurred.  EventID: 0x0000A00A  

        Time Generated: 01/07/2025   11:38:23  

        Event String:  

        The Security System has detected a downgrade attempt when contacting the 3-part SPN    

     A warning event occurred.  EventID: 0x0000A00A  

        Time Generated: 01/07/2025   11:38:24  

        Event String:  

        The Security System has detected a downgrade attempt when contacting the 3-part SPN    

     An error event occurred.  EventID: 0xC0001B61  

        Time Generated: 01/07/2025   11:38:48  

        Event String:  

        A timeout was reached (30000 milliseconds) while waiting for the ADWS service to connect.  

     An error event occurred.  EventID: 0xC0001B58  

        Time Generated: 01/07/2025   11:38:48  

        Event String:  

        The ADWS service failed to start due to the following error:    

     An error event occurred.  EventID: 0x40000004  

        Time Generated: 01/07/2025   11:38:59  

        Event String:  

        The Kerberos client received a KRB\_AP\_ERR\_MODIFIED error from the server srv-ad-rep$. The target name used was E3514235-4B06-11D1-AB04-00C04FC2DCD2/d599bead-73a2-46ed-8e76-49be77ca8f60/fsm.local@fsm.local. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (FSM.LOCAL) is different from the client domain (FSM.LOCAL), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.  

     An error event occurred.  EventID: 0x40000004  

        Time Generated: 01/07/2025   11:39:44  

        Event String:  

        The Kerberos client received a KRB\_AP\_ERR\_MODIFIED error from the server srv-ad-rep$. The target name used was FSM\SRV-AD-REP$. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (FSM.LOCAL) is different from the client domain (FSM.LOCAL), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server.  

     An error event occurred.  EventID: 0xC0001B70  

        Time Generated: 01/07/2025   11:42:44  

        EvtFormatMessage failed (second call), error 15033 The locale specific resource for the desired message is not present.. 

        (Event String (event log = System) could not be retrieved, error  

        0x3ab9)  

     An error event occurred.  EventID: 0xC0001B77  

        Time Generated: 01/07/2025   11:42:44  

        Event String:  

        The Windows Search service terminated unexpectedly.  It has done this 1 time(s).  The following corrective action will be taken in 30000 milliseconds: Restart the service.  

     A warning event occurred.  EventID: 0x80000434  

        Time Generated: 01/07/2025   11:42:44  

        Event String:  

        The reason supplied by user FSM\Administrator for the last unexpected shutdown of this computer is: Other (Unplanned)   

     ......................... SRV-AD failed test SystemLog  

  Starting test: VerifyReferences  

     ......................... SRV-AD passed test VerifyReferences
```

   Running partition tests on : ForestDnsZones  

```
Starting test: CheckSDRefDom  

     ......................... ForestDnsZones passed test CheckSDRefDom  

  Starting test: CrossRefValidation  

     ......................... ForestDnsZones passed test  

     CrossRefValidation
```

   Running partition tests on : DomainDnsZones  

```
Starting test: CheckSDRefDom  

     ......................... DomainDnsZones passed test CheckSDRefDom  

  Starting test: CrossRefValidation  

     ......................... DomainDnsZones passed test  

     CrossRefValidation
```

   Running partition tests on : Schema  

```
Starting test: CheckSDRefDom  

     ......................... Schema passed test CheckSDRefDom  

  Starting test: CrossRefValidation  

     ......................... Schema passed test CrossRefValidation
```

   Running partition tests on : Configuration  

```
Starting test: CheckSDRefDom  

     ......................... Configuration passed test CheckSDRefDom  

  Starting test: CrossRefValidation  

     ......................... Configuration passed test CrossRefValidation
```

   Running partition tests on : fsm  

```
Starting test: CheckSDRefDom  

     ......................... fsm passed test CheckSDRefDom  

  Starting test: CrossRefValidation  

     ......................... fsm passed test CrossRefValidation
```

   Running enterprise tests on : fsm.local  

```
Starting test: LocatorCheck  

     ......................... fsm.local passed test LocatorCheck  

  Starting test: Intersite  

     ......................... fsm.local passed test Intersite
```

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-07*

Hello Omid Pand,

Thank you for posting in Microsoft Community forum.

It seems there are multiple problems from the description.

Do you have two Domain Controllers in this domain? If so, please check AD replication status between two Domain Controllers first. Please run commands below on PDC.

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt  

repadmin /showrepl * /csv >c:\repsum.csv

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
