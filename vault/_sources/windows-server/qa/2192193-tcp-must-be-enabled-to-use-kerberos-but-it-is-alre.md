---
title: "TCP must be enabled to use Kerberos, but it is already enabled in Configuration Manager"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192193/tcp-must-be-enabled-to-use-kerberos-but-it-is-alre
question_id: 2192193
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-network-connectivity-file-sharing"]
---
# TCP must be enabled to use Kerberos, but it is already enabled in Configuration Manager

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192193/tcp-must-be-enabled-to-use-kerberos-but-it-is-alre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I currently have a SQL server with two instance using one Service account. In Kerberos Configuration Manager under SPN I show both are on SQL Service 2016 Standard, Instance name , Cluster is no, TCP Enabled is no and the Service account. I am trying to set up two separate accounts for each instance of SQL . Once I change the Service account out for them. I am getting the error TCP Must Be Enabled to User Kerberos. In configuration Manager it show TCP is already Enabled. Also when opening SQL Instance in SSMS I get error when trying to log into the Instance with the New service account. I am at a loss as to what to do to fix this issue. It is an issue with SPN ? or SQL?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-25*

Hi Michael, 

Thank you for providing the details of the issue you are encountering with Kerberos authentication and SQL Server. Based on the information provided, it appears that the problem may be related to SPN configuration or SQL Server settings. Please follow the steps below to resolve the issue: 

Steps to Resolve the TCP Must Be Enabled to Use Kerberos Issue 

-  Verify TCP/IP is Enabled for SQL Server Instances: 

-  Open *SQL Server Configuration Manager*. 

-  Expand *SQL Server Network Configuration*. 

-  Select *Protocols for <YourInstanceName>*. 

-  Ensure that *TCP/IP* is enabled for both SQL Server instances. 

-  Restart the SQL Server services if you made any changes. 

-  Verify SPN Registration: 

-  SPNs must be correctly registered in Active Directory for Kerberos authentication to work. Here’s how you can manually register SPNs: 

-  Open a Command Prompt as Administrator. 

-  Use the following commands to set SPNs for each instance (replace placeholders with actual values):        cmd        setspn -S MSSQLSvc/<FQDN>:<Port> <ServiceAccount>        setspn -S MSSQLSvc/<FQDN> <ServiceAccount>        For example, if your instance is running on the default port (1433) and the service account is `sqlsvc1`:        cmd        setspn -S MSSQLSvc/sqlserver.domain.com:1433 sqlsvc1        setspn -S MSSQLSvc/sqlserver.domain.com sqlsvc1 

-  Repeat the steps for the second instance using its specific service account and port. 

-  Verify Kerberos Configuration in SQL Server: 

-  Open *Kerberos Configuration Manager*for SQL Server. 

-  Check if there are any SPN errors or warnings and resolve them based on the tool’s suggestions. 

-  Ensure that the correct service accounts are listed for each SQL Server instance. 

-  Set the Service Account for SQL Server: 

-  Open *SQL Server Configuration Manager*. 

-  Under *SQL Server Services*, right-click your SQL Server instance and select *Properties*. 

-  Go to the *Log On* tab and ensure that the correct service account is set. 

-  Restart the SQL Server service after changing the service account. 

-  Check DNS Resolution: 

-  Ensure that the Fully Qualified Domain Name (FQDN) of the SQL Server resolves correctly to the server’s IP address. 

-  Use the `ping` command or other network diagnostic tools to verify DNS resolution. 

-  Troubleshoot Authentication Issues: 

-  If you receive errors when trying to log in with the new service accounts, check the SQL Server error logs and Windows Event Logs for more details. 

-  Ensure that the new service accounts have the necessary permissions to log in to SQL Server and access the database instances. 

Current Status and Further Steps 

Despite following these steps, it appears that the Configuration Manager still shows TCP as not enabled, and there are issues with logging into the SQL instances using the new service accounts. Given this, we need to: 

-  Double-Check SPN Configuration: 

-  Ensure there are no duplicate SPNs that could be causing conflicts. 

-  Use the `setspn -L &lt;ServiceAccount&gt;` command to list the SPNs for each service account and verify correctness. 

-  Review SQL Server and Kerberos Logs: 

-  Look into SQL Server logs and Kerberos event logs for any additional errors or warnings that could provide more insights. 

-  Validate Service Account Permissions: 

-  Confirm that the new service accounts have the necessary SQL Server permissions and are correctly configured for delegation in Active Directory. 

-  Verify TCP Settings: 

-  Double-check that TCP is indeed enabled in the SQL Server Configuration Manager for both instances and that there are no network policies blocking TCP connections. 

Please try these steps and let me know the results. If the issue persists, we can explore further troubleshooting options. 

Thank you for your patience and cooperation. 

Best regards, 

Rosy   

Windows Networking Team

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-17*

I had to remove spn and re added. The new service account now has the service Principal name and can delegate . However configuration Manager is still showing TCP is not enabled. I followed all the trouble shooting steps and while it is somewhat working it is not working 100 percent.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Dear Michael, 

Thank you for providing the details of the issue you are encountering with Kerberos authentication and SQL Server. Based on the information provided, it appears that the problem may be related to SPN configuration or SQL Server settings. Please follow the steps below to resolve the issue: 

Steps to Resolve the TCP Must Be Enabled to Use Kerberos Issue 

1. Verify TCP/IP is Enabled for SQL Server Instances: 

-  Open *SQL Server Configuration Manager*. 

-  Expand **SQL Server Network Configuration**. 

-  Select **Protocols for <YourInstanceName>**. 

-  Ensure that **TCP/IP** is enabled for both SQL Server instances. 

-  Restart the SQL Server services if you made any changes. 

2. Verify SPN Registration: 

-  SPNs must be correctly registered in Active Directory for Kerberos authentication to work. Here’s how you can manually register SPNs: 

-  Open a Command Prompt as Administrator. 

-  Use the following commands to set SPNs for each instance (replace placeholders with actual values): 

```
setspn -S MSSQLSvc/:  

setspn -S MSSQLSvc/ 
```

            For example, if your instance is running on the default port (1433) and the service account is `sqlsvc1`: 

```
setspn -S MSSQLSvc/sqlserver.domain.com:1433 sqlsvc1 

  setspn -S MSSQLSvc/sqlserver.domain.com sqlsvc1
```

-  Repeat the steps for the second instance using its specific service account and port. 

3. Verify Kerberos Configuration in SQL Server: 

-  Open **Kerberos Configuration Manager** for SQL Server. 

-  Check if there are any SPN errors or warnings and resolve them based on the tool’s suggestions. 

-  Ensure that the correct service accounts are listed for each SQL Server instance. 

4. Set the Service Account for SQL Server: 

-  Open **SQL Server Configuration Manager**. 

-  Under **SQL Server Services**, right-click your SQL Server instance and select **Properties**. 

-  Go to the **Log On** tab and ensure that the correct service account is set. 

-  Restart the SQL Server service after changing the service account. 

5. Check DNS Resolution: 

-  Ensure that the Fully Qualified Domain Name (FQDN) of the SQL Server resolves correctly to the server’s IP address. 

-  Use the `ping` command or other network diagnostic tools to verify DNS resolution. 

 

6. Troubleshoot Authentication Issues: 

-  If you receive errors when trying to log in with the new service accounts, check the SQL Server error logs and Windows Event Logs for more details. 

-  Ensure that the new service accounts have the necessary permissions to log in to SQL Server and access the database instances. 

Please try these steps and let me know the results. If the issue persists, we can explore further troubleshooting options. 

Thank you for your patience and cooperation. 

Best regards, 

Rosy
