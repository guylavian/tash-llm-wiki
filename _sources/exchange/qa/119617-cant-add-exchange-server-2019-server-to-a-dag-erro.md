---
title: "Can't add Exchange Server 2019 server to a DAG Error:CreateCluster() failed with 0x42a"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/119617/cant-add-exchange-server-2019-server-to-a-dag-erro
question_id: 119617
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Can't add Exchange Server 2019 server to a DAG Error:CreateCluster() failed with 0x42a

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/119617/cant-add-exchange-server-2019-server-to-a-dag-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Environment: Exchange Server 2019 Exchange 2013 exists Forest functional level – 2016 Exchange Server OS – Server 2019 Exchange servers are VMs (vSphere 6.7) Hey team, got an odd error here when my customer runs “Add-DatabaseAvailabilityGroupServer” for the first server being added to a 2019 DAG: [2020-10-06T21:22:34] The operation wasn't successful because an error was encountered. You may find more details in log file "C:\ExchangeSetupLogs\DagTasks\dagtask_2020-10-06_21-19-28.923_add-databaseavailabiltygroupserver.log" on "XXXX-EX19A1-X". (the log is attached) [2020-10-06T21:22:34] WriteError! Exception = Microsoft.Exchange.Cluster.Replay.DagTaskOperationFailedException: A server-side database availability group administrative operation failed. Error The operation failed. CreateCluster errors may result from incorrectly configured static addresses. Error: An error occurred while attempting a cluster operation. Error: Cluster API failed: "CreateCluster() failed with 0x42a. Error: The service has returned a service-specific error code". ---> [30752-error-dag.txt][1] When I look up further in the log that the error mentions, I see the error code mentioned: [2020-10-06T21:22:34] ClusterSetupProgressCallback( eSetupPhase = ClusterSetupPhaseFormingCluster, ePhaseType = ClusterSetupPhaseEnd, ePhaseSeverity = ClusterSetupPhaseFatal, dwPercentComplete = 56, szObjectName = xxxx-daga-x, dwStatus = 0x42a ) We tried adding a different server first, but same error occurs. I’ve seen a couple of links mentioning permissions/configurations on the CNO and duplicate MACs, but all those things are set correctly as well. We’ve also tried removing and re-creating the DAG (with the same name and with a different name) without an IP without success. At first, we were getting an error about Failover Clustering not being installed. We checked that and it said a restart was pending, so we restarted and now we get this error above. Also in the log, it mentions the DAG CNO doesn’t exist, but it does. Screenshots show the command we ran and where it sticks, then the second shows the error message that comes up afterward. Anyone got any ideas? ![30773-screenshot.png][2]![30783-failedscreenshot.png][3] [1]: /api/attachments/30752-error-dag.txt?platform=QnA [2]: /api/attachments/30773-screenshot.png?platform=QnA [3]: /api/attachments/30783-failedscreenshot.png?platform=QnA

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-10-19*

For the TL:DR folks, the answer ended up being that there was a "Deny access to this computer from the network" setting configured to not allow "Local Accounts" (read as: CLIUSR). And that makes sense because that user is heavily involved in managing and establishing the cluster.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-08*

anonymous user     

Hi,    

if there is no cluster, would the service start?    

I tested it in my lab(Exchange 2019 CU2):    

If the server hasn't been add to the DAG (a cluster)yet,the cluster service is disabled and can't be started(the button is grayed out)    

Are you able to click start? And after that does the Event Viewer generate the 1090,7024,7031 errors?    

Now we also can't add any servers to the 2013 DAGs in the lab.    

Did you receive the same error as Exchange 2019?    

Please check if there are some network problems between the new servers and the numbers of the DAG.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
