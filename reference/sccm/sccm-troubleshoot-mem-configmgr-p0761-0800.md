---
title: "Welcome — pages 761-800"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0761-0800
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0761-0800
family: sccm
documentKind: "doc"
abstract: "PolicyID {2ba787b6-4ee9-4b33-b0ff-8663d181c84d} PolicyVersion 1.00 PolicyHash SHA256:0C6D50CBFB36750CCA381B61E014A6C55D821001487C824F9112DAA1C64BAD32 SMS_OBJECT_REPLICATION_MANAGER Notifying policy provider about changes in policy content/targeting SMS_OBJECT_REPLICATION_MANAGER"
---

# Welcome — pages 761-800

<!-- p.761 -->

 PolicyID {2ba787b6-4ee9-4b33-b0ff-8663d181c84d} PolicyVersion 1.00 PolicyHash
 SHA256:0C6D50CBFB36750CCA381B61E014A6C55D821001487C824F9112DAA1C64BAD32
 SMS_OBJECT_REPLICATION_MANAGER
 Notifying policy provider about changes in policy content/targeting
 SMS_OBJECT_REPLICATION_MANAGER
 Successfully created policy for CI Assignment {2ba787b6-4ee9-4b33-b0ff-
 8663d181c84d}    SMS_OBJECT_REPLICATION_MANAGER
 Notifying policy provider about changes in policy content/targeting
 SMS_OBJECT_REPLICATION_MANAGER
 Successfully updated Policy Targeting for CI Assignment {2ba787b6-4ee9-4b33-b0ff-
 8663d181c84d}   SMS_OBJECT_REPLICATION_MANAGER
 Found file trigger for E:\ConfigMgr\inboxes\objmgr.box\16777228.CIV
 SMS_OBJECT_REPLICATION_MANAGER
 Assigned CIs: [ 16777275 ]   SMS_OBJECT_REPLICATION_MANAGER
 Begin processing Assigned CI: [16777275]    SMS_OBJECT_REPLICATION_MANAGER
 Creating VersionInfo policy for CI 16777275    SMS_OBJECT_REPLICATION_MANAGER
 Creating VersionInfo policy ScopeId_FC8FCC38-4BB1-4245-92F5-
 9CE841775019/AuthList_4d3480d5-de12-4864-b872-187479e2b381/VI
 SMS_OBJECT_REPLICATION_MANAGER
 16777275 Referenced CIs: [ 1395 1396 1397 1398 1399 1400 1401 3013 3014 3015 3016
 3017 3018 3019 3020 3021 3959 3960 3961 4112 4113 4114 4115 4116 4117 4118 4502
 4503 4504 4505 4506 4507 4508 4509 4510 4511 4512 4513 4514 ]
 SMS_OBJECT_REPLICATION_MANAGER
 VersionInfo policy for CI 16777275 is Machine type    SMS_OBJECT_REPLICATION_MANAGER
 PolicyID ScopeId_FC8FCC38-4BB1-4245-92F5-9CE841775019/AuthList_4d3480d5-de12-4864-
 b872-187479e2b381/VI PolicyVersion 1.00 PolicyHash
 SHA256:01BECBBF2B3EE56BD5B0742A04404C1C895A4C87B6915D55078AB157FEBA1E0F
 SMS_OBJECT_REPLICATION_MANAGER
 Notifying policy provider about changes in policy content/targeting
 SMS_OBJECT_REPLICATION_MANAGER
 Updated dependent policy references to CIA {2ba787b6-4ee9-4b33-b0ff-8663d181c84d}
 SMS_OBJECT_REPLICATION_MANAGER
 STATMSG: ID=5800 SEV=I LEV=M SOURCE="SMS Server"
 COMP="SMS_OBJECT_REPLICATION_MANAGER" SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=6176
 TID=6868 GMTDATE=Thu Feb 06 20:09:17.989 2014 ISTR0="ADR_Test" ISTR1="" ISTR2=""
 ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=414
 AVAL0="{2ba787b6-4ee9-4b33- b0ff-8663d181c84d}"    SMS_OBJECT_REPLICATION_MANAGER
 Successfully updated CRCs for CI Assignment {2ba787b6-4ee9-4b33-b0ff-8663d181c84d}
 SMS_OBJECT_REPLICATION_MANAGER
 Successfully processed Update Group Assignment {2ba787b6-4ee9-4b33-b0ff-
 8663d181c84d}    SMS_OBJECT_REPLICATION_MANAGER
 Set last row version for CI Assignment to 0x0000000000487EB6
 SMS_OBJECT_REPLICATION_MANAGER
 +++Completed processing changed CIA objects     SMS_OBJECT_REPLICATION_MANAGER

The following example shows the Policy creation process:

In SMSDBMON.log:

 Output

 RCV: INSERT on CrpChange_Notify for CrpChange_Notify_ins [15 ][66199]
 SMS_DATABASE_NOTIFICATION_MONITOR

<!-- p.762 -->

 RCV: INSERT on RBAC_ChangeNotification for Rbac_Sync_ChangeNotification [399 ]
 [66200]   SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\15.CRP [66199]
  SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\hman.box\399.RBC [66200]
 SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on PolicyAssignmentChg_Notify for PolicyAssignmentChg_Notify_iu
 [16787957 ][66201]    SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\16787957.PAC
 [66201]    SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: INSERT on PolicyAssignmentChg_Notify for PolicyAssignmentChg_Notify_iu
 [16787957 ][66202]    SMS_DATABASE_NOTIFICATION_MONITOR
 RCV: UPDATE on PolicyAssignmentChg_Notify for PolicyAssignmentChg_Notify_iu
 [16787957 ][66203]    SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\16787957.PAC
 [66202]    SMS_DATABASE_NOTIFICATION_MONITOR
 SND: Dropped E:\ConfigMgr\inboxes\policypv.box\policytargeteval\16787957.PAC
 [66203]    SMS_DATABASE_NOTIFICATION_MONITOR

In PolicyPv.log:

 Output

 File notification triggered.   SMS_POLICY_PROVIDER

 --Process Collection Changes    SMS_POLICY_PROVIDER
 Building Collection Change List from Collection Change Notification
 files    SMS_POLICY_PROVIDER

 --Process Collection Member Changes    SMS_POLICY_PROVIDER
 Building Collection Change List from Collection Member Notification
 files    SMS_POLICY_PROVIDER

 --Handle PolicyAssignment Resigning    SMS_POLICY_PROVIDER
 Found the certificate that matches the SHA1 hash.    SMS_POLICY_PROVIDER
 Completed batch with beginning PADBID = 16787957 ending PADBID =
 16787958.    SMS_POLICY_PROVIDER

 --Process Policy Changes    SMS_POLICY_PROVIDER
 Found some Policy changes, returning New
 LastRowversion=0x0000000000487EB7     SMS_POLICY_PROVIDER
 Processing Updated Policies     SMS_POLICY_PROVIDER
 Building Collection Change List from New and Targeting Changed
 Policies    SMS_POLICY_PROVIDER

 --Update Policy Targeting Map    SMS_POLICY_PROVIDER
 **** Evaluating Collection 15 for targeting changes ****      SMS_POLICY_PROVIDER

 --Process Policy Targeting Map    SMS_POLICY_PROVIDER
 **** Process notification table to update resultant targeting table
 ****    SMS_POLICY_PROVIDER

 --Process Targeting and Collection Membership changes      SMS_POLICY_PROVIDER

<!-- p.763 -->

 Updating Policy Map       SMS_POLICY_PROVIDER

 --UpdateMDMUserTargetingForUser    SMS_POLICY_PROVIDER
 Start Update MDM User Targeting For User SMS_POLICY_PROVIDER

 --UpdatePolicyMapForPA     SMS_POLICY_PROVIDER
 Found 16787957.PAC     SMS_POLICY_PROVIDER
 Adding to delete list:
 E:\ConfigMgr\inboxes\policypv.box\policytargeteval\16787957.PAC            SMS_POLICY_PROVI
 DER
 Updating ResPolicyMap     SMS_POLICY_PROVIDER

RuleEngine.log shows completion of rule processing:

 Output

 CRuleHandler: Rule 1 Successfully Applied!        SMS_RULE_ENGINE
 Updated Success Information for Rule: 1          SMS_RULE_ENGINE

Deployment evaluation and update installation on
clients
After the deployment and the deployment policy have been created on the server, clients
receive the policy on the next policy evaluation cycle. Before you review the deployment
evaluation process, it's important to find the Deployment Unique ID of the deployment. To find
the Deployment Unique ID, add the Deployment Unique ID column in the console. For the
deployment in the following example, the Deployment Unique ID is {B040D195-8FA8-48D3-
953F-17E878DAB23D}.

   1. Policy Agent receives the policy on manual policy retrieval or on schedule. When policy is
     received, the following are logged in PolicyAgent.log:

       Output

       Initializing download of policy 'CCM_Policy_Policy5.PolicyID="{B040D195-8FA8-
       48D3-953F-17E878DAB23D}",PolicySource="SMS:PR1",PolicyVersion="1.00"' from
       'http://PR1SITE.CONTOSO.COM/SMS_MP/.sms_pol?{B040D195-8FA8-48D3-953F-
       17E878DAB23D}.SHA256:0EE489DB3036BE80BB43676340249A254278BEBDDD80B6004C11FF10F
       12BC9D6' PolicyAgent_ReplyAssignments
       Download of policy CCM_Policy_Policy5.PolicyID="{B040D195-8FA8-48D3-953F-
       17E878DAB23D}",PolicySource="SMS:PR1",PolicyVersion="1.00" completed (DTS Job
       ID: {D53DAB18-ED97-4373-A3BE-3FBA5DB3C6C6}) PolicyAgent_PolicyDownload

     The following are logged in PolicyEvaluator.log:

<!-- p.764 -->

    Output

    Initializing download of policy 'CCM_Policy_Policy5.PolicyID="{B040D195-8FA8-
    48D3-953F-17E878DAB23D}",PolicySource="SMS:PR1",PolicyVersion="1.00"' from
    'http://PR1SITE.CONTOSO.COM/SMS_MP/.sms_pol?{B040D195-8FA8-48D3-953F-
    17E878DAB23D}.SHA256:0EE489DB3036BE80BB43676340249A254278BEBDDD80B6004C11FF10F
    12BC9D6' PolicyAgent_ReplyAssignments
    Download of policy CCM_Policy_Policy5.PolicyID="{B040D195-8FA8-48D3-953F-
    17E878DAB23D}",PolicySource="SMS:PR1",PolicyVersion="1.00" completed (DTS Job
    ID: {D53DAB18-ED97-4373-A3BE-3FBA5DB3C6C6}) PolicyAgent_PolicyDownload

  After the policy is evaluated, the scheduler for the deadline is evaluated. This operation is
  done by the Scheduler component. In this example, deadline randomization is disabled in
  Computer Agent client settings. So the deployment evaluation is started on deadline and
  without randomization. Here's what we see in the Scheduler.log file:

    Output

    Initialized trigger ("3E692B0000080000") for schedule 'Machine/DEADLINE:
    {B040D195-8FA8-48D3-953F-17E878DAB23D}':
    Conditions=1 with deadline 4320 minutes
    Allow randomization override=1
    HasMissedOccurrence=FALSE
    ScheduleLoadedTime="02/09/2014 19:05:947"
    LastFireTime="00/00/00 00:00:00"
    CurrentTime="02/09/2014 19:05:947"    Scheduler
    Processing trigger '3E692B0000080000' for scheduler 'Machine/DEADLINE:
    {B040D195-8FA8-48D3-953F-17E878DAB23D}'. MaxRandomDelay = 120, MissedOccur =
    0, RandomizeEvenIfMissed = 1, PreventRandomizationInducedMisses = 0
    Scheduler
    Randomization is disabled in client settings and this schedule is set to honor
    client setting.   Scheduler
    SMSTrigger '3E692B0000080000' for scheduler 'Machine/DEADLINE:{B040D195-8FA8-
    48D3-953F-17E878DAB23D}' will fire at 02/09/2014 07:15:00 PM without
    randomization.   Scheduler

2. At the scheduled deadline, Scheduler notifies the Updates Deployment Agent to start the
  deployment evaluation process, as shown in Scheduler.log:

    Output

    Sending message for schedule 'Machine/DEADLINE:{B040D195-8FA8-48D3-953F-
    17E878DAB23D}' (Target: 'direct:UpdatesDeploymentAgent', Name: '')
    Scheduler
    SMSTrigger '3E692B0000080000' (Schedule ID: 'Machine/DEADLINE:{B040D195-8FA8-
    48D3-953F-17E878DAB23D}', Message Name: '', Target:
    'direct:UpdatesDeploymentAgent') will never fire again.     Scheduler

  In UpdatesDeployment.log:

<!-- p.765 -->

    Output

    Message received: '<?xml version='1.0' ?>
    <CIAssignmentMessage MessageType='EnforcementDeadline'>
    <AssignmentID>{B040D195-8FA8-48D3-953F-17E878DAB23D}</AssignmentID>
    </CIAssignmentMessage>'    UpdatesDeploymentAgent

  Updates Deployment Agent starts the deployment evaluation process by requesting a
  software update scan. The scan ensures that the deployed updates are still applicable. In
  UpdatesDeployment.log:

    Output

    Assignment {B040D195-8FA8-48D3-953F-17E878DAB23D} has total CI = 3
    UpdatesDeploymentAgent
    Deadline received for assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D})
    UpdatesDeploymentAgent
    Detection job ({99ADA372-0738-44E4-9C4D-EBA30F23E9FD}) started for assignment
    ({B040D195-8FA8-48D3-953F-17E878DAB23D})   UpdatesDeploymentAgent

  In UpdatesHandler.log:

    Output

    Successfully initiated scan for job ({99ADA372-0738-44E4-9C4D-EBA30F23E9FD}).
    UpdatesHandler
    Scan completion received for job ({99ADA372-0738-44E4-9C4D-EBA30F23E9FD}).
    UpdatesHandler
    Initial scan completed for the job ({99ADA372-0738-44E4-9C4D-EBA30F23E9FD}).
    UpdatesHandler
    Evaluating status of the updates for the job ({99ADA372-0738-44E4-9C4D-
    EBA30F23E9FD}).   UpdatesHandler
    CompleteJob - Job ({99ADA372-0738-44E4-9C4D-EBA30F23E9FD}) removed from job
    manager list.    UpdatesHandler

3. At this point, the scan request is handled by Scan Agent component. Scan Agent calls
  WUAHandler to perform a scan and then hands the results back to Updates Handler and
  Updates Deployment Agent. For more information about the scan process, see Software
  update scan on clients.

  After the scan is completed, Updates Deployment Agent is notified. Here's what we see in
  UpdatesDeployment.log:

    Output

    DetectJob completion received for assignment ({B040D195-8FA8-48D3-953F-
    17E878DAB23D}) UpdatesDeploymentAgent

<!-- p.766 -->

   Making updates available for assignment ({B040D195-8FA8-48D3-953F-
   17E878DAB23D}) UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_e06056e3-0199-4c68-8ac3-
   bdddff356a0a) Name (Security Update for Windows Server 2008 R2 x64 Edition
   (KB2698365)) ArticleID (2698365) added to the targeted list of deployment
   ({B040D195-8FA8-48D3-953F-17E878DAB23D}) UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_ada7cf51-66b0-4a00-b37b-
   68d569d6ff8b) Name (Security Update for Windows Server 2008 R2 x64 Edition
   (KB2712808)) ArticleID (2712808) added to the targeted list of deployment
   ({B040D195-8FA8-48D3-953F-17E878DAB23D}) UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_3cbcf577-5139-49b8-afe8-
   620af5c52f95) Name (Security Update for Windows Server 2008 R2 x64 Edition
   (KB2705219)) ArticleID (2705219) added to the targeted list of deployment
   ({B040D195-8FA8-48D3-953F-17E878DAB23D}) UpdatesDeploymentAgent

4. Updates Deployment Agent raises state messages for the deployment to update the
  current Evaluation and Compliance state. Here's what we see in UpdatesDeployment.log:

   Output

   Raised assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D}) state message
   successfully. TopicType = Evaluate, StateId = 2, StateName =
   ASSIGNMENT_EVALUATE_SUCCESS     UpdatesDeploymentAgent
   Raised assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D}) state message
   successfully. TopicType = Compliance, Signature = 5e176837, IsCompliant =
   False    UpdatesDeploymentAgent

  Updates Deployment Agent now starts a job to download the software update files from
  the distribution point. Here's what we see in UpdatesDeployment.log:

   Output

   DownloadCIContents Job ({C531FD04-FADA-4F75-A399-EEA2D3EDB56C}) started for
   assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D})   UpdatesDeploymentAgent
   Progress received for assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D})
   UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_e06056e3-0199-4c68-8ac3-
   bdddff356a0a) Progress: Status = ciStateDownloading, PercentComplete = 0,
   Result = 0x0   UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_ada7cf51-66b0-4a00-b37b-
   68d569d6ff8b) Progress: Status = ciStateDownloading, PercentComplete = 0,
   Result = 0x0   UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_3cbcf577-5139-49b8-afe8-
   620af5c52f95) Progress: Status = ciStateDownloading, PercentComplete = 0,
   Result = 0x0   UpdatesDeploymentAgent

  We can also see in UpdatesHandler.log:

   Output

<!-- p.767 -->

    Initiating download for the job ({C531FD04-FADA-4F75-A399-EEA2D3EDB56C}).
    UpdatesHandler
    Update Id = 3cbcf577-5139-49b8-afe8-620af5c52f95, State = StateDownloading,
    Result = 0x0 UpdatesHandler
    Update Id = ada7cf51-66b0-4a00-b37b-68d569d6ff8b, State = StateDownloading,
    Result = 0x0 UpdatesHandler
    Update Id = e06056e3-0199-4c68-8ac3-bdddff356a0a, State = StateDownloading,
    Result = 0x0 UpdatesHandler
    Timeout Options: Priority = 2, DPLocality = 1048578, Location = 604800,
    Download = 864000, PerDPInactivity = 0, TotalInactivityTimeout = 0,
    bUseBranchCache = True, bPersistOnWriteFilterDevices = True,
    bOverrideServiceWindow = False UpdatesHandler

5. Updates Handler starts the download request from Content Access service for the three
  actionable updates that are listed above. The download job is started for the child update
  in the bundle and the Content ID is logged.

  In UpdatesHandler.log

    Output

    Bundle update (3cbcf577-5139-49b8-afe8-620af5c52f95) is requesting download
    from child updates for action (INSTALL) UpdatesHandler
    Content Text = <Content ContentId="fbb5724a-aa0f-47f9-908a-47068fd8ad6f"
    Version="1"><FileContent Name="windows6.1-kb2705219-v2-x64.cab"
    Hash="AA11BB22CC33DD44EE55FF66AA77BB88CC99DD00" HashAlgorithm="SHA1"
    Size="199093"/></Content>
    Bundle update (ada7cf51-66b0-4a00-b37b-68d569d6ff8b) is requesting download
    from child updates for action (INSTALL) UpdatesHandler
    Content Text = <Content ContentId="3e9b1132-9ccd-439d-b32a-5cefd19735d1"
    Version="1"><FileContent Name="windows6.1-kb2712808-x64.cab"
    Hash="BB22CC33DD44EE55FF66AA77BB88CC99DD00EE11" HashAlgorithm="SHA1"
    Size="805071"/></Content>
    Bundle update (e06056e3-0199-4c68-8ac3-bdddff356a0a) is requesting download
    from child updates for action (INSTALL) UpdatesHandler
    Content Text = <Content ContentId="d2a9ee23-9cab-4843-b040-e2da1cc167e9"
    Version="1"><FileContent Name="windows6.1-kb2698365-x64.cab"
    Hash="CC33DD44EE55FF66AA77BB88CC99DD00EE11FF22" HashAlgorithm="SHA1"
    Size="2496330"/></Content>

  Content Access service starts a download job for each update and creates a Content
  Transfer Manager (CTM) job. A CTM job is created for each update separately, and
  CAS.log entries resemble the following for each update:

    Output

    Requesting content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1, size(KB) 0, under
    context System with priority Medium ContentAccess
    Created and initialized a DownloadContentRequest ContentAccess

<!-- p.768 -->

    Target location for content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1 is
    C:\Windows\ccmcache\1 ContentAccess
    CDownloadManager::RequestDownload fbb5724a-aa0f-47f9-908a-
    47068fd8ad6f.1.System ContentAccess
    Submitted CTM job {E0452CF4-5B04-4A1A-B8EB-10B11B063249} to download Content
    fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1 under context System ContentAccess
    Successfully created download request {856FA4CA-D02A-4E2C-841E-841ED3C7EC01}
    for content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1 ContentAccess
    Created and submitted a new Content Request for fbb5724a-aa0f-47f9-908a-
    47068fd8ad6f.1.System ContentAccess

6. Content Transfer Manager starts working on the download job. It first requests the
  location for the content that must be downloaded. This location request is handled by
  Location Services. Location Services sends the location request to the management point,
  obtains the location response, and then hands it back to the Content Transfer Manager.
  Here's what we see in ContentTransferManager.log:

    Output

    Starting CTM job {E0452CF4-5B04-4A1A-B8EB-10B11B063249}.
    ContentTransferManager
    CTM job {E0452CF4-5B04-4A1A-B8EB-10B11B063249} entered phase
    CCM_DOWNLOADSTATUS_DOWNLOADING_DATA ContentTransferManager
    Queued location request '{C56C01F2-2388-4710-BF3B-A526DB40E35F}' for CTM job
    '{E0452CF4-5B04-4A1A-B8EB-10B11B063249}'. ContentTransferManager
    CCTMJob::EvaluateState(JobID={E0452CF4-5B04-4A1A-B8EB-10B11B063249},
    State=RequestedLocations) ContentTransferManager

  We can also see in LocationServices.log:

    Output

    Created filter for LS request {C56C01F2-2388-4710-BF3B-A526DB40E35F}.
    LocationServices
    ContentLocationReply : <ContentLocationReply SchemaVersion="1.00"><ContentInfo
    PackageFlags="0"><ContentHashValues/></ContentInfo><Sites><Site><MPSite
    SiteCode="PR1" MasterSiteCode="PR1" SiteLocality="LOCAL" IISPreferedPort="80"
    IISSSLPreferedPort="443"/><LocationRecords><LocationRecord><URL Name="
    <http://PR1SITE.CONTOSO.COM/SMS_DP_SMSPKG$/fbb5724a-aa0f-47f9-908a-
    47068fd8ad6f>" Signature="<http://PR1SITE.CONTOSO.COM/SMS_DP_SMSSIG$/fbb5724a-
    aa0f-47f9-908a-47068fd8ad6f.1.tar>"/><ADSite Name="Default-First-Site-Name"/>
    <IPSubnets><IPSubnet Address="192.168.10.0"/><IPSubnet Address=""/>
    </IPSubnets><Metric Value=""/><Version>7958</Version><Capabilities
    SchemaVersion="1.0"><Property Name="SSLState" Value="0"/></Capabilities>
    <ServerRemoteName>PR1SITE.CONTOSO.COM</ServerRemoteName>
    <DPType>SERVER</DPType><Windows Trust="1"/><Locality>LOCAL</Locality>
    </LocationRecord></LocationRecords></Site></Sites><RelatedContentIDs/>
    </ContentLocationReply>   LocationServices
    Distribution Point='<http://PR1SITE.CONTOSO.COM/SMS_DP_SMSPKG$/fbb5724a-aa0f-
    47f9-908a-47068fd8ad6f>', Locality='LOCAL', DPType='SERVER', Version='7958',

<!-- p.769 -->

 Capabilities='<Capabilities SchemaVersion="1.0"><Property Name="SSLState"
 Value="0"/></Capabilities>',
 Signature='<http://PR1SITE.CONTOSO.COM/SMS_DP_SMSSIG$/fbb5724a-aa0f-47f9-908a-
 47068fd8ad6f.1.tar>', ForestTrust='TRUE',   LocationServices
 Calling back with locations for location request {C56C01F2-2388-4710-BF3B-
 A526DB40E35F}   LocationServices

Content Transfer Manager receives the distribution point location for the requested
content and starts a Data Transfer Service job to start the download of the update. Here's
what we see in ContentTransferManager.log:

 Output

 CCTMJob::UpdateLocations({E0452CF4-5B04-4A1A-B8EB-10B11B063249})
 ContentTransferManager
 CTM_NotifyLocationUpdate   ContentTransferManager
 Persisted location '<http://PR1SITE.CONTOSO.COM/SMS_DP_SMSPKG$/fbb5724a-aa0f-
 47f9-908a-47068fd8ad6f>', Order 0, for CTM job {E0452CF4-5B04-4A1A-B8EB-
 10B11B063249}   ContentTransferManager
 Persisted locations for CTM job {E0452CF4-5B04-4A1A-B8EB-10B11B063249}:
 (LOCAL) '<http://PR1SITE.CONTOSO.COM/SMS_DP_SMSPKG$/fbb5724a-aa0f-47f9-908a-
 47068fd8ad6f>'   ContentTransferManager
 CTM job {E0452CF4-5B04-4A1A-B8EB-10B11B063249} (corresponding DTS job
 {594E9A72-43D1-48D1-A639-D18DF7D286A2}) started download from
 'http://PR1SITE.CONTOSO.COM/SMS_DP_SMSPKG$/fbb5724a-aa0f-47f9-908a-
 47068fd8ad6f' for full content download.    ContentTransferManager
 CCTMJob::EvaluateState(JobID={E0452CF4-5B04-4A1A-B8EB-10B11B063249},
 State=DownloadingData)    ContentTransferManager
 CTM job {E0452CF4-5B04-4A1A-B8EB-10B11B063249} entered phase
 CCM_DOWNLOADSTATUS_DOWNLOADING_DATA     ContentTransferManager

In CAS.log:

 Output

 Location update from CTM for content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1
 and request {856FA4CA-D02A-4E2C-841E-841ED3C7EC01} ContentAccess
 Download location found 0 -
 <http://PR1SITE.CONTOSO.COM/SMS_DP_SMSPKG$/fbb5724a-aa0f-47f9-908a-
 47068fd8ad6f> ContentAccess
 Download request only, ignoring location update ContentAccess
 Download started for content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1
 ContentAccess

At this point, Data Transfer Service creates a BITS job to download the file and then
monitors the download progress as noted in DataTransferService.log:

 Output

<!-- p.770 -->

DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} created to download from
'http://PR1SITE.CONTOSO.COM:80/SMS_DP_SMSPKG$/fbb5724a-aa0f-47f9-908a-
47068fd8ad6f' to 'C:\Windows\ccmcache\1'.    DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} in state 'DownloadingManifest'.
DataTransferService
CDTSJob::ProcessManifestCallback - processing manifest for job '{594E9A72-
43D1-48D1-A639-D18DF7D286A2}'. DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} in state 'RetrievedManifest'.
DataTransferService
Execute called for DTS job '{594E9A72-43D1-48D1-A639-D18DF7D286A2}'. Current
state: 'RetrievedManifest'.    DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} in state 'PendingDownload'.
DataTransferService
Starting BITS download for DTS job '{594E9A72-43D1-48D1-A639-D18DF7D286A2}'.
DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} set BITS job to use default
credentials.   DataTransferService
Starting BITS job '{38E74FCB-4397-4CA9-94AE-BDD49F550EC9}' for DTS job
'{594E9A72-43D1-48D1-A639-D18DF7D286A2}' under user 'S-1-5-18'.
DataTransferService
DTS::SetCustomHeadersOnBITSJob - setting custom headers on DTS job '{594E9A72-
43D1-48D1-A639-D18DF7D286A2}':
<none>   DataTransferService
DTS::AddTransportSecurityOptionsToBITSJob - Removing security info from DTS
job '{594E9A72-43D1-48D1-A639-D18DF7D286A2}'.    DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} in state 'DownloadingData'.
DataTransferService
Job: {594E9A72-43D1-48D1-A639-D18DF7D286A2}, Total Files: 1, Transferred
Files: 0, Total Bytes: 199093, Transferred Bytes: 5760    DataTransferService
Job: {594E9A72-43D1-48D1-A639-D18DF7D286A2}, Total Files: 1, Transferred
Files: 0, Total Bytes: 199093, Transferred Bytes: 199093    DataTransferService
CDTSJob::JobTransferred : DTS Job ID='{594E9A72-43D1-48D1-A639-D18DF7D286A2}'
BITS Job ID='{38E74FCB-4397-4CA9-94AE-BDD49F550EC9}'    DataTransferService
Job: {594E9A72-43D1-48D1-A639-D18DF7D286A2}, Total Files: 1, Transferred
Files: 1, Total Bytes: 199093, Transferred Bytes: 199093    DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} in state 'RetrievedData'.
DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} successfully completed download.
DataTransferService
BITS job '{38E74FCB-4397-4CA9-94AE-BDD49F550EC9}' is not found. The BITS job
may have completed already.    DataTransferService
CBITSDownloadMonitor(DTSJobID={594E9A72-43D1-48D1-A639-D18DF7D286A2},
BITSJobID={38E74FCB-4397-4CA9-94AE-BDD49F550EC9}) ignoring cancelled object.
DataTransferService
DTSJob {594E9A72-43D1-48D1-A639-D18DF7D286A2} in state 'NotifiedComplete'.
DataTransferService
DTS job {594E9A72-43D1-48D1-A639-D18DF7D286A2} has completed:
Status : SUCCESS,
Start time : 02/09/2014 19:15:05,
Completion time : 02/09/2014 19:15:12,
Elapsed time : 7 seconds    DataTransferService

<!-- p.771 -->

7. After the download is complete, CTM and Content Access service are notified, and they
  mark the download jobs as completed. Content Access service performs a hash
  verification of the downloaded content to verify the integrity of the downloaded file. This
  process occurs for each file, although the following example involves a single update
  being downloaded. Here's what we see in ContentTransferManager.log:

    Output

    CCTMJob::EvaluateState(JobID={E0452CF4-5B04-4A1A-B8EB-10B11B063249},
    State=Success)   ContentTransferManager
    CCTMJob::EvaluateState(JobID={E0452CF4-5B04-4A1A-B8EB-10B11B063249},
    State=Complete)   ContentTransferManager

  In CAS.log:

    Output

    Download completed for content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1 under
    context System   ContentAccess
    The hash we are verifying is SDMPackage:<Content ContentId="fbb5724a-aa0f-
    47f9-908a-47068fd8ad6f" Version="1"><FileContent Name="windows6.1-kb2705219-
    v2-x64.cab" Hash="AA11BB22CC33DD44EE55FF66AA77BB88CC99DD00"
    HashAlgorithm="SHA1" Size="199093"/></Content> ContentAccess
    CContentAccessService::NotifyDownloadComplete Start Content Hashing
    ContentAccess
    Hashing file c:\windows\ccmcache\1\windows6.1-kb2705219-v2-x64.cab
    ContentAccess
    Hash matches ContentAccess 2/9/2014 7:15:12 PM 3532 (0x0DCC)
    Hash verification succeeded for content fbb5724a-aa0f-47f9-908a-47068fd8ad6f.1
    downloaded under context System ContentAccess

  Then Updates Deployment Agent raises a state message to update the current
  enforcement state and then starts the installation of the update. We see the following
  message in UpdatesDeployment.log:

    Output

    Raised assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D}) state message
    successfully. TopicType = Enforce, StateId = 8, StateName =
    ASSIGNMENT_ENFORCE_ADVANCE_DOWNLOAD_SUCCESS   UpdatesDeploymentAgent
    Starting install for assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D})
    UpdatesDeploymentAgent
    ApplyCIs - JobId = {CEE4AA3A-DE7B-4D9F-8949-E421BBBF2993}
    UpdatesDeploymentAgent
    Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_3cbcf577-5139-49b8-afe8-
    620af5c52f95) Progress: Status = ciStateWaitInstall, PercentComplete = 0,
    DownloadSize = 0, Result = 0x0   UpdatesDeploymentAgent
    Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_ada7cf51-66b0-4a00-b37b-

<!-- p.772 -->

   68d569d6ff8b) Progress: Status = ciStateWaitInstall, PercentComplete = 0,
   DownloadSize = 0, Result = 0x0   UpdatesDeploymentAgent
   Update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_e06056e3-0199-4c68-8ac3-
   bdddff356a0a) Progress: Status = ciStateWaitInstall, PercentComplete = 0,
   DownloadSize = 0, Result = 0x0   UpdatesDeploymentAgent

  We also see this entry in UpdatesHandler.log:

   Output

   Job {CEE4AA3A-DE7B-4D9F-8949-E421BBBF2993} is starting execution
   UpdatesHandler
   CDeploymentJob::InstallUpdatesInBatch - Batch or non-batch install is not in
   progress for the job ({CEE4AA3A-DE7B-4D9F-8949-E421BBBF2993}). So allowing
   install..   UpdatesHandler
   Update (3cbcf577-5139-49b8-afe8-620af5c52f95) added to the installation batch
   UpdatesHandler
   Update (ada7cf51-66b0-4a00-b37b-68d569d6ff8b) added to the installation batch
   UpdatesHandler
   Update (e06056e3-0199-4c68-8ac3-bdddff356a0a) added to the installation batch
   UpdatesHandler
   Got execute info for (3) updates   UpdatesHandler
   Updates installation started as batch   UpdatesHandler

8. Windows Update Agent Handler then copies the downloaded binaries to the Windows
  Update Agent cache (C:\Windows\SoftwareDistribution\Download) directory and instructs
  Windows Update Agent to start the installation process. Here's what we see in
  WUAHandler.log:

   Output

   Adding file to list for CopyToCache(): C:\Windows\ccmcache\1\windows6.1-
   kb2705219-v2-x64.cab    WUAHandler
   CopyToCache() for update (fbb5724a-aa0f-47f9-908a-47068fd8ad6f) completed
   successfully   WUAHandler
   Adding file to list for CopyToCache(): C:\Windows\ccmcache\2\windows6.1-
   kb2712808-x64.cab    WUAHandler
   CopyToCache() for update (3e9b1132-9ccd-439d-b32a-5cefd19735d1) completed
   successfully   WUAHandler
   Adding file to list for CopyToCache(): C:\Windows\ccmcache\3\windows6.1-
   kb2698365-x64.cab    WUAHandler
   CopyToCache() for update (d2a9ee23-9cab-4843-b040-e2da1cc167e9) completed
   successfully   WUAHandler
   Update(s) downloaded to WUA file cache, starting installation.   WUAHandler
   Async installation of updates started.   WUAHandler
   Update 1 (3cbcf577-5139-49b8-afe8-620af5c52f95) finished installing
   (0x00000000), Reboot Required? Yes   WUAHandler
   Update 2 (ada7cf51-66b0-4a00-b37b-68d569d6ff8b) finished installing
   (0x00000000), Reboot Required? Yes   WUAHandler
   Update 3 (e06056e3-0199-4c68-8ac3-bdddff356a0a) finished installing

<!-- p.773 -->

     (0x00000000), Reboot Required? Yes    WUAHandler
     Async install completed.   WUAHandler
     Installation of updates completed.    WUAHandler

   We also see the following entries in WindowsUpdate.log:

     Output

     2014-02-09 19:15:26:130 800 ed0 Agent ** START ** Agent: Installing updates
     [CallerId = CcmExec]
     2014-02-09 19:15:26:130 800 ed0 Agent * Updates to install = 3
     2014-02-09 19:15:26:254 1048 84c Handler Starting install of CBS update
     FBB5724A-AA0F-47F9-908A-47068FD8AD6F
     2014-02-09 19:15:29:218 1048 84c Handler Completed install of CBS update with
     type=3, requiresReboot=1, installerError=0, hr=0x0
     2014-02-09 19:15:29:265 1048 84c Handler Starting install of CBS update
     3E9B1132-9CCD-439D-B32A-5CEFD19735D1
     2014-02-09 19:15:30:435 1048 84c Handler Completed install of CBS update with
     type=3, requiresReboot=1, installerError=0, hr=0x0
     2014-02-09 19:15:30:451 1048 84c Handler Starting install of CBS update
     D2A9EE23-9CAB-4843-B040-E2DA1CC167E9
     2014-02-09 19:15:39:296 1048 84c Handler Completed install of CBS update with
     type=3, requiresReboot=1, installerError=0, hr=0x0
     2014-02-09 19:15:39:327 788 9f8 COMAPI - Reboot required = Yes
     2014-02-09 19:15:39:327 788 9f8 COMAPI -- END -- COMAPI: Install [ClientId =
     CcmExec]

 9. After the updates are installed, Updates Deployment Agent checks whether any updates
   require a reboot. Then, it notifies the user if client settings are configured to allow such
   notifications. Here's what we see in UpdatesDeployment.log:

     Output

     No installations in pipeline, notify reboot. NotifyUI = True
     UpdatesDeploymentAgent
     Notify reboot with deadline = Sunday, Feb 09, 2014. - 19:15:39, Ignore reboot
     Window = False, NotifyUI = True UpdatesDeploymentAgent
     Raised assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D}) state message
     successfully. TopicType = Enforce, StateId = 5, StateName =
     ASSIGNMENT_ENFORCE_PENDING_REBOOT   UpdatesDeploymentAgent

10. After the computer restarts, a post-reboot detection scan is started for the deployment.
   The scan verifies that updates are installed and raises state messages for the update and
   deployment to indicate that updates are installed and that enforcement was successful.
   Here's what we see in UpdatesDeployment.log:

     Output

<!-- p.774 -->

        CTargetedUpdatesManager::DetectRebootPendingUpdates - Total Pending reboot
        updates = 3   UpdatesDeploymentAgent
        Initiated detect for pending reboot updates after system restart - JobId =
        {53F4851F-7E63-4C7E-952D-78345039FFFC}   UpdatesDeploymentAgent
        CUpdatesJob({53F4851F-7E63-4C7E-952D-78345039FFFC}): Job completion received.
        UpdatesDeploymentAgent
        CUpdatesJob({53F4851F-7E63-4C7E-952D-78345039FFFC}): Detect after reboot job
        completed with result = 0x0   UpdatesDeploymentAgent
        Raised update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_e06056e3-0199-
        4c68-8ac3-bdddff356a0a) enforcement state message successfully. StateId = 10,
        StateName = CI_ENFORCEMENT_SUCCESSFULL   UpdatesDeploymentAgent
        Raised update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_ada7cf51-66b0-
        4a00-b37b-68d569d6ff8b) enforcement state message successfully. StateId = 10,
        StateName = CI_ENFORCEMENT_SUCCESSFULL   UpdatesDeploymentAgent
        Raised update (Site_D3A5F7EA-25D4-4C6B-B47C-C74997522A76/SUM_3cbcf577-5139-
        49b8-afe8-620af5c52f95) enforcement state message successfully. StateId = 10,
        StateName = CI_ENFORCEMENT_SUCCESSFULL   UpdatesDeploymentAgent
        Raised assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D}) state message
        successfully. TopicType = Compliance, Signature = 5e176837, IsCompliant = True
        UpdatesDeploymentAgent
        Raised assignment ({B040D195-8FA8-48D3-953F-17E878DAB23D}) state message
        successfully. TopicType = Enforce, StateId = 4, StateName =
        ASSIGNMENT_ENFORCE_SUCCESS   UpdatesDeploymentAgent

      At this point, the software updates deployment has been downloaded and successfully
      installed on the client, and the process is complete.

State message reporting
Throughout the deployment phase, multiple state messages are raised to indicate the current
state of the updates and the deployment itself. After these state messages are raised, they're
processed in the way that's described in State messaging data flow.

 Last updated on 03/30/2026

<!-- p.775 -->

Enable verbose logging and configure SQL
Server Profiler for troubleshooting
Applies to: Configuration Manager

In Configuration Manager, client and site server components record process information in
individual log files. You can use the information in these log files to help you troubleshoot
issues that might occur.

Enable verbose and debug logging on the client and
management point
     Verbose logging can be enabled by creating the following registry value as REG_DWORD
     with value 0x0:

     HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\@GLOBAL\LogLevel

     Debug logging can be enabled by creating the following registry value as REG_SZ with a
     value of True:

     HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\DebugLogging\Enabled

     The CCM log size can be increased to 5 MB by setting the following registry value as
     REG_DWORD with a value of 5242880 (decimal):

     HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\@GLOBAL\LogMaxSize

     You can edit the REG_DWORD value for the following registry value to increase the
     number of history log files to be retained:

     HKEY_LOCAL_MACHINE\Software\Microsoft\CCM\Logging\@GLOBAL\LogMaxHistory

  ７ Note

  Restart the SMS Agent Host service to enable the changes. On the management point,
  you may have to restart IIS-related services for verbose logging to take effect for some
  logs.

<!-- p.776 -->

Enable verbose logging for the state system
component on the site server
To enable verbose logging for State System (StateSys), set the REG_DWORD value for the
following registry value to 1:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Components\SMS_STATE_SYSTEM\Verbose logging

  ７ Note

  This registry key change doesn't require a restart of the SMS_Executive service or the
  SMS_STATE_SYSTEM thread.

Enable verbose logging for WSUS Synchronization
Manager (WSYNCMGR)
To enable verbose logging for WsyncMgr.log, create or modify the following registry value on
the site server and set the REG_DWORD value to 0:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SMS_WSUS_SYNC_MANAGER\LogLevel

Enable SQL tracing for Configuration Manager logs
To enable SQL tracing, set the REG_DWORD value for the following registry value to 1:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SqlEnabled

  ７ Note

  This registry change doesn't require a restart of the SMS_Executive service. This registry
  value adds SQL trace logging for all site server logs. This should only be done temporarily
  while troubleshooting, and should be disabled after getting the relevant logs.

Enable verbose logging for Windows Update Agent
To enable verbose logging, create the following registry subkey with two values:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Trace

<!-- p.777 -->

                                                                                 ﾉ    Expand table

 Value name                      Value type                         Value data

 Flags                           REG_DWORD                          00000007

 Level                           REG_DWORD                          00000004

This subkey turns on an extended tracing to the %systemroot%\Windowsupdate.log file, it also
turns on an extended tracing to any attached debuggers.

  ７ Note

  Extended verbose logging can be enabled by setting the value of Flags to 17 instead of 7.
  However, it will significantly increase the size of WindowsUpdate.log.

Configure SQL Server Profiler to troubleshoot WSUS
location request issues
In some circumstances, you may need to use SQL Server Profiler to find the call to the
MP_GetWSUSServerLocation stored procedure and see what parameters are passed.

To do this, configure the SQL Server Profiler as shown in the following screenshot:

<!-- p.778 -->

Configure SQL Server Profiler to view state message
processing
To do this, configure the SQL Server Profiler as shown in the following screenshot:

<!-- p.779 -->

Last updated on 03/30/2026

<!-- p.780 -->

Troubleshoot software update
management in Configuration
Manager
This article helps you troubleshoot the software update management process in Configuration
Manager. It includes client software update scanning, synchronization issues, and detection
problems with specific updates.

Original product version: Configuration Manager (current branch), System Center 2012 R2
Configuration Manager, System Center 2012 Configuration Manager
Original KB number: 4505440

Scope your issue
This guide assumes that a software update point has already been installed and configured. For
more information about configuring software updates in Configuration Manager, see Prepare
for software updates management.

Before you start troubleshooting, it's important to emphasize that, the better you understand
the problem you're experiencing, the quicker and easier it will be for you to fix it. Whether
you're tasked with fixing a problem that you are experiencing, or a problem reported to you by
someone in your organization, take a moment and answer the following questions:

   1. What specifically isn't working and/or what is your goal?
   2. What is the frequency or pattern for the issue? Is the problem still happening?
   3. How did you become aware that the problem exists?
   4. Has it ever worked? If so, when did it stop? Was anything changed in the environment
     right before it stopped working?
   5. What percentage of clients are affected?
   6. What has been done already (if anything) to try to fix it?
   7. Know the exact version of the client and the version of the server. Are these systems up to
     date?
   8. What do affected clients have in common? For example, same subnet, AD site, domain,
     physical location, site, site system.

Knowing and understanding the answers to these questions will put you on the best path for a
quick and easy resolution to whatever problem you're experiencing.

If you know the specific area within the software update management process that you'd like
to troubleshoot, select it below. Start with client software update scanning if unsure and we'll
walk through the entire process from beginning to end.

     Client software update scanning
     WSUS to Microsoft Update synchronization
     Installation, supersedence, or detection issues with specific updates

Client software update scanning
The client scan process is outlined in the following steps. Confirm each step to properly
establish where the issue is.

Step 1: The client sends a WSUS location request to
the management point

<!-- p.781 -->

The first thing the client does is set the WSUS server that will be its update source for software
update scans. That process is detailed below.

   1. When the Configuration Manager client needs to process a software update scan, Scan
     Agent creates a scan request based on the available policy as noted in ScanAgent.log:

       Output

       CScanAgent::ScanByUpdates- Policy available for UpdateSourceID={SourceID}
       ContentVersion=38
       CScanAgent::ScanByUpdates- Added Policy to final ScanRequest List
       UpdateSourceID={SourceID}, Policy-ContentVersion=38, Required-
       ContentVersion=38

   2. Scan Agent now sends a WSUS location request to Location Services as noted in
     ScanAgent.log:

       Output

       Inside CScanAgent::ProcessScanRequest()
       CScanJobManager::Scan- entered
       ScanJob({JobID}): CScanJob::Initialize- entered
       ScanJob({JobID}): CScanJob::Scan- entered
       ScanJob({JobID}): CScanJob::RequestLocations- entered
       - - - - - -Requesting WSUS Server Locations from LS for {WSUSLocationID}
       version 38
       - - - - - -Location Request ID = {LocationRequestID}
       CScanAgentCache::PersistInstanceInCache- Persisted Instance
       CCM_ScanJobInstance
       ScanJob({JobID}): - - - - - -Locations requested for ScanJobID={JobID}
       (LocationRequestID={LocationRequestID}), will process the scan request once
       locations are available.

         Tip

        Each scan job is stored in WMI in the CCM_ScanJobInstance class:

        Namespace: root\CCM\ScanAgent Class: CCM_ScanJobInstance

   3. Location Services creates a location request and sends it to the management point. The
     package ID for a WSUS location request is the update source unique ID. In
     LocationServices.log:

       Output

       CCCMWSUSLocation::GetLocationsAsyncEx
       Attempting to persist WSUS location request for ContentID='{ContentID}' and
       ContentVersion='38'
       Persisted WSUS location request LocationServices
       Attempting to send WSUS Location Request for ContentID='{ContentID}'
       WSUSLocationRequest : <WSUSLocationRequest SchemaVersion="1.00"><Content ID="
       {ContentID}" Version="38"/><AssignedSite SiteCode="PS1"/><ClientLocationInfo
       OnInternet="0"><ADSite Name="CM12-R2PS1"/><Forest Name="CONTOSO.COM"/><Domain
       Name="CONTOSO.COM"/><IPAddresses><IPAddress SubnetAddress="192.168.2.0"
       Address="192.168.2.62"/></IPAddresses></ClientLocationInfo>
       </WSUSLocationRequest>
       Created and Sent Location Request '{LocationRequestID}' for package
       {ContentID}

   4. CCM Messaging sends the location request message to the management point. In
     CcmMessaging.log:

       Output

       Sending async message '{Message}' to outgoing queue 'mp:
       [http]mp_locationmanager'
       Sending outgoing message '{Message}'. Flags 0x200, sender account empty

<!-- p.782 -->

5. The management point parses this request and calls the MP_GetWSUSServerLocations
  stored procedure to get the WSUS locations from the database. In MP_Location.log:

    Output

    MP LM: Message Body : \<WSUSLocationRequest SchemaVersion="1.00"><Content ID="
    {ContentID}" Version="38"/><AssignedSite SiteCode="PS1"/><ClientLocationInfo
    OnInternet="0"><ADSite Name="CM12-R2PS1"/><Forest Name="CONTOSO.COM"/><Domain
    Name="CONTOSO.COM"/><IPAddresses><IPAddress SubnetAddress="192.168.2.0"
    Address="192.168.2.62"/></IPAddresses></ClientLocationInfo>
    </WSUSLocationRequest> MP_LocationManager
    MP LM: calling MP_GetWSUSServerLocations

  In SQL Server Profiler:

    Output

    exec MP_GetMPSitesFromAssignedSite N'PS1'
    exec MP_GetSiteInfoUnified N'<ClientLocationInfo OnInternet="0"><ADSite
    Name="CM12-R2-PS1"/><Forest Name="CONTOSO.COM"/><Domain Name="CONTOSO.COM"/>
    <IPAddresses><IPAddress SubnetAddress="192.168.2.0" Address="192.168.2.62"/>
    </IPAddresses></ClientLocationInfo>'
    exec MP_GetWSUSServerLocations
    N'{WSUSServerLocationsID}',N'38',N'PS1',N'PS1',N'0',N'CONTOSO.COM'

6. After getting the results from the stored procedure, the management point sends a
  response to the client. In MP_Location.log:

    Output

    MP LM: Reply message body: <WSUSLocationReply SchemaVersion="1.00"><Sites>
    <Site><MPSite SiteCode="PS1"/><LocationRecords><LocationRecord
    WSUSURL="http://PS1SITE.CONTOSO.COM:8530" ServerName="PS1SITE.CONTOSO.COM"
    Version="38"/><LocationRecord WSUSURL="https://PS1SYS.CONTOSO.COM:8531"
    ServerName="PS1SYS.CONTOSO.COM" Version="38"/></LocationRecords></Site>
    </Sites></WSUSLocationReply>

7. CCM Messaging receives the response and sends it back to Location Services. In
  CcmMessaging.log:

    Output

    Message '{Message1}' got reply '{Message2}' to local endpoint queue
    'LS_ReplyLocations'
    OutgoingMessage(Queue='mp_[http]mp_locationmanager', ID={*Message1*}):
    Delivered successfully to host 'PS1SYS.CONTOSO.COM'.
    Message '{Message2}' delivered to endpoint 'LS_ReplyLocations'

8. Location Services parses the response and sends the location back to Scan Agent. In
  LocationServices.log:

    Output

    Processing Location reply message LocationServices
    WSUSLocationReply : <WSUSLocationReply SchemaVersion="1.00"><Sites><Site>
    <MPSite SiteCode="PS1"/><LocationRecords><LocationRecord
    WSUSURL="http://PS1SITE.CONTOSO.COM:8530" ServerName="PS1SITE.CONTOSO.COM"
    Version="38"/><LocationRecord WSUSURL="https://PS1SYS.CONTOSO.COM:8531"
    ServerName="PS1SYS.CONTOSO.COM" Version="38"/></LocationRecords></Site>
    </Sites></WSUSLocationReply>
    Calling back with the following WSUS locations
    WSUS Path='http://PS1SITE.CONTOSO.COM:8530', Server='PS1SITE.CONTOSO.COM',
    Version='38'
    WSUS Path='https://PS1SYS.CONTOSO.COM:8531', Server='PS1SYS.CONTOSO.COM',
    Version='38'
    Calling back with locations for WSUS request {WSUSLocationID}

9. Scan Agent now has the policy and the update source location with the appropriate
  content version. In ScanAgent.log:

    Output

<!-- p.783 -->

      *****WSUSLocationUpdate received for location request guid={LocationGUID}
      ScanJob({JobID}): CScanJob::OnLocationUpdate- Received
      Location=<http://PS1SITE.CONTOSO.COM:8530>, Version=38
      ScanJob({JobID}): CScanJob::Execute- Adding UpdateSource={SourceID},
      ContentType=2, ContentLocation=<http://PS1SITE.CONTOSO.COM:8530>,
      ContentVersion=38

 10. Scan Agent notifies WUAHandler to add the update source. WUAHandler adds the
    update source to the registry. It initiates a Group Policy refresh if the client is in domain to
    see whether Group Policy overrides the update server that's added. The following entries
    are logged in WUAHandler.log showing a new Update Source being added:

      Output

      Its a WSUS Update Source type ({WSUSUpdateSource}), adding it
      Its a completely new WSUS Update Source
      Enabling WUA Managed server policy to use server:
      <http://PS1SITE.CONTOSO.COM:8530>
      Policy refresh forced
      Waiting for 2 mins for Group Policy to notify of WUA policy change
      Waiting for 30 secs for policy to take effect on WU Agent.
      Added Update Source ({UpdateSource}) of content type: 2

    During this time, the Windows Update Agent sees a WSUS configuration change. In
    WindowsUpdate.log:

      Output

      * WSUS server: <http://PS1SITE.CONTOSO.COM:8530> (Changed)
      * WSUS status server: <http://PS1SITE.CONTOSO.COM:8530> (Changed)
      Sus server changed through policy.

    The following registry keys are checked and set:

                                                                                   ﾉ     Expand table

     Registry subkey                                                                         Value name       Type        Data

      HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\WindowsUpdate        WUServer        REG_SZ      The full W
                                                                                                                          the port.
                                                                                                                          < http://

      HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\WindowsUpdate       WUStatusServer   REG_SZ      The full W
                                                                                                                          the port.
                                                                                                                          < http://

      HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\WindowsUpdate\AU     UseWUServer     REG_DWORD   0x1

    For an existing client, we could expect to see the following message in WUAHandler.log
    to denote when content version has incremented:

      Output

      Its a WSUS Update Source type ({WSUSUpdateSource}), adding it.
      WSUS update source already exists, it has increased version to 38.

 11. After the update source is successfully added, Scan Agent raises a state message and
    starts the scan. In ScanAgent.log:

      Output

      ScanJob({JobID}): Raised UpdateSource ({UpdateSource}) state message
      successfully. StateId = 2
      ScanJob({JobID}): CScanJob::Execute - successfully requested Scan, ScanType=1

Troubleshoot issues in step 1

                                                                                   ﾉ     Expand table

<!-- p.784 -->

 Issues                                    What to check

 ScanAgent.log shows no policy             Check the Enable software updates on clients setting.
 available for an update source and no
 WUAHandler.log exists or no current
 activity within WUAHandler.log

 Scan Agent or Location Services doesn't         Is a software update point (SUP) role installed for the
 receive the WSUS server location                site?

                                                 If not, install and configure a software update point and
                                                 monitor SUPSetup.log for progress. For more
                                                 information, see Install and configure a software update
                                                 point.
                                                 If a SUP role is installed, is it configured and
                                                 synchronizing?

                                                 Check WCM.log, WSUSCtrl.log, and WSyncMgr.log for
                                                 errors.
                                                     select * from WSUSServerLocations
                                                     select * from Update_SyncStatus

 Client receives the WSUS location but     Did Group Policy refresh respond within the 2-minute timeout
 fails to configure the WSUS registry      per WUAHandler.log? If so, does WUAHandler denote Group
 keys                                      policy settings were overwritten by a higher authority
                                           (Domain Controller)?

                                           For more information, see Group Policy overrides the correct
                                           WSUS configuration information.

For more information about software update scan failures troubleshooting, see Troubleshoot
software update scan failures.

Step 2: Scan Agent requests the scan and
WUAHandler starts the scan
After the client has identified and set the WSUS server that will be its update source for
software update scans, Scan Agent requests the scan from WUAHandler that uses the Windows
Update Agent API to request a software update scan from the Windows Update Agent. A scan
may result from:

        A scheduled or manual software update scan
        A scheduled or manual software updated deployment re-evaluation
        A deployment that becomes active

The scan triggers an evaluation. In ScanAgent.log:

 Output

 ScanJob({JobID}): CScanJob::Execute - successfully requested Scan, ScanType=1

Scan results will include superseded updates only when they're superseded by service packs
and definition updates. In WUAHandler.log:

 Output

 Search Criteria is (DeploymentAction=* AND Type='Software') OR (DeploymentAction=*
 AND Type='Driver')
 Running single-call scan of updates.
 Async searching of updates using WUAgent started.

   Tip

  Review WUAHandler.log after a software update scan to see if any new entries occur. If no
  new entries occur, it indicates that no SUP is returned by the management point.

<!-- p.785 -->

Troubleshoot issues in step 2
Many issues with software update scan can be caused by one of the following reasons:

     Missing or corrupted files or registry keys.
     Component registration issues.

To fix such issues, see Scan failures due to missing or corrupted components.

There's a known issue that a 32-bit Windows 7 ConfigMgr 2012 R2 client requesting an update
scan fails to return scan results to Configuration Manager. It causes the client to report
incorrect compliance status and the updates fail to install when Configuration Manager
requests the update cycle. However, if you use the Windows Update control panel applet, the
updates usually install fine. When you're experiencing this problem, you receive a message
similar to the following one in WindowsUpdate.log:

 Output

 WARNING: ISusInternal::GetUpdateMetadata2 failed, hr=8007000E

It's a memory allocation issue, 64-bit Windows 7 computers won't see this error since their
address space is effectively unlimited. However, they'll exhibit high memory and high CPU
usage, possibly affecting performance. X86 clients will also exhibit high memory usage (usually
around 1.2 GB to 1.4 GB).

To fix this issue, apply Windows Update Client for Windows 7: June 2015 .

When troubleshooting scan failures, check the WUAHandler.log and WindowsUpdate.log files.
WUAHandler simply reports what Windows Update Agent reported. So, the error in
WUAHandler would be the same error that was reported by the Windows Update Agent itself.
More information about the error can be found in WindowsUpdate.log. To understand how to
read WindowsUpdate.log, see Windows Update log files.

Your best source of information will come from the logs and the error codes they contain. For
more information about the error codes, see Windows Update common errors and mitigation.

Step 3: Windows Update Agent (WUA) starts the
scan against the WSUS computer
Windows Update Agent starts a scan after receiving a request from the Configuration Manager
client (CcmExec). If these registry values are correctly set to a WSUS computer that's a valid
SUP for the site through a local policy, you should see a COM API search request from the
Configuration Manager client (ClientId = CcmExec). In WindowsUpdate.log:

 Output

 COMAPI -- START -- COMAPI: Search [ClientId = CcmExec]
 COMAPI <<-- SUBMITTED -- COMAPI: Search [ClientId = CcmExec] PT + ServiceId =
 {ServiceID}, Server URL =
 <http://PS1.CONTOSO.COM:8530/ClientWebService/client.asmx>
 Agent ** START ** Agent: Finding updates [CallerId = CcmExec]
 Agent * Include potentially superseded updates
 Agent * Online = Yes; Ignore download priority = Yes
 Agent * Criteria = "(DeploymentAction=* AND Type='Software') OR (DeploymentAction=*
 AND Type='Driver')"
 Agent * ServiceID = {ServiceID} Managed
 Agent * Search Scope = {Machine}

 PT + ServiceId = {ServiceID}, Server URL =
 <http://PS1.CONTOSO.COM:8530/ClientWebService/client.asmx>
 Agent * Added update {4AE85C00-0EAA-4BE0-B81B-DBD7053D5FAE}.104 to search result
 Agent * Added update {57260DFE-227C-45E3-9FFC-2FC77A67F95A}.104 to search result
 Agent * Found 163 updates and 70 categories in search; evaluated appl. rules of 622
 out of 1150 deployed entities
 Agent ** END ** Agent: Finding updates [CallerId = CcmExec]
 COMAPI >>-- RESUMED -- COMAPI: Search [ClientId = CcmExec]

<!-- p.786 -->

 COMAPI - Updates found = 163
 COMAPI -- END -- COMAPI: Search [ClientId = CcmExec]

Troubleshoot issues in step 3
During a scan, the Windows Update Agent needs to communicate with the ClientWebService
and SimpleAuthWebService virtual directories on the WSUS computer to perform a scan. If the
client can't communicate with the WSUS computer, the scan will fail. This issue can happen for
many reasons, including:

     Proxy related issues

     To fix these issues, see Scan failures due to proxy-related issues.

     For more information about proxy servers, see the following articles:
        How the Windows Update client determines which proxy server to use to connect to
        the Windows Update website
        DNS and DHCP Support for Web Proxy and Firewall Client Autodiscovery

     HTTP timeout errors

     To troubleshoot HTTP timeout errors, first review the Internet Information Services (IIS)
     logs on the WSUS computer to confirm that the errors are actually being returned from
     WSUS. If the WSUS computer isn't returning the error, the issue is likely with an
     intermediate firewall or proxy.

     If the WSUS computer is returning the error, verify connectivity with the WSUS computer.
     Here are the steps:

        1. To confirm that the client is connecting to the correct WSUS server, find the URL of
          the WSUS computer used by the Windows Update Agent client. This URL can be
          found by checking the
           HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate registry

          subkey or by viewing the WindowsUpdate.log file.

          Common reasons that the WSUS assignment may be incorrect include:
             Group Policy conflicts
             The addition of a SUP to a secondary site after initial client installation

             ７ Note

             Active Directory Group Policy may override the local WSUS policy.

          The software updates feature automatically configures a local Group Policy setting
          for the Configuration Manager client so that it's configured with the software
          update point source location and port number. Both the server name and port
          number are required for the client to find the software update point.

          If an Active Directory Group Policy setting is applied to computers for software
          update point client installation, it overrides the local Group Policy setting. If the
          value of the setting defined in the Active Directory Group Policy is different from the
          one set by Configuration Manager, the scan will fail on the client because it can't
          locate the correct WSUS computer. In this situation, WUAHandler.log will show the
          following message:

             Group policy settings were overwritten by a higher authority (Domain
             Controller) to: Server < http://server > and Policy ENABLED

          The software update point for client installation and software updates must be the
          same server. And it must be specified in the Active Directory Group Policy setting

<!-- p.787 -->

  with the correct name format and port information. For example, it would be
  < http://server1.contoso.com:80 > if the software update point was using the
  default website.

2. If the server URL is correct, access the server using a URL similar to the following
  one to verify connectivity between the client and the WSUS computer:

  < http://SUPSERVER.CONTOSO.COM:8530/Selfupdate/wuident.cab >

  To check whether the client can access the ClientWebService virtual directory, try
  accessing a URL similar to this one:

  < http://SUPSERVER.CONTOSO.COM:8530/ClientWebService/wusserverversion.xml >

  To check whether the client can access the SimpleAuthWebService , try accessing a
  URL similar to this one:

  < http://SUPSERVER.CONTOSO.COM:8530/SimpleAuthWebService/SimpleAuth.asmx >

  If any of these URLs fail, some of the possible reasons include:

     Name resolution issues on the client. Verify that you can resolve the FQDN of the
     WSUS computer.

     Proxy configuration issues.

     Other network-related connectivity issues.

     Port configuration problems, so it's a good idea to verify that the port settings
     are correct. WSUS can be configured to use any of the following ports: 80, 443 or
     8530, 8531.

     For clients to communicate with the WSUS computer, the appropriate ports must
     be allowed on the firewall on the WSUS computer. Port settings are configured
     when the software update point site system role is created. These port settings
     must be the same as the port settings used by the WSUS website. Otherwise,
     WSUS Synchronization Manager will fail to connect to WSUS running on the
     software update point to request synchronization. The following procedures
     provide information about how to verify the port settings used by WSUS and the
     software update point.

      a. Determine the WSUS port settings used in IIS 7.0 and later versions.

     b. Determine the WSUS port settings in IIS 6.0.

      c. Configure ports for the software update point.

     d. Verify port connectivity

        To check port connectivity from the client, run the following command:

          Console

          telnet SUPSERVER.CONTOSO.COM <portnumber>

        For example, run the following command if the port is 8530:

          Console

          telnet SUPSERVER.CONTOSO.COM 8530

        If the port isn't accessible, telnet will return an error that resembles the
        following one:

          Could not open connection to the host, on port <PortNumber>

<!-- p.788 -->

                This error suggests that the firewall rules aren't configured to allow
                communication for the WSUS computer. This error can also suggest that an
                intermediate network device is blocking that port. To verify, try the same test
                from a client on the same local subnet. If it works, the computers are
                configured correctly. However, a router or firewall between segments is
                blocking the port and causing the failure.

             IIS availability problems.
              a. On the WSUS computer, open Internet Information Services (IIS) Manager.
              b. Expand Sites, right-click the website for the WSUS computer, and then click
                Edit Bindings.
              c. In the Site Bindings dialog box, the HTTP and HTTPS port values are displayed
                in the Port column.
              d. On the WSUS server, open Internet Information Services (IIS) Manager.
              e. Expand Web Sites, right-click the website for the WSUS computer, then click
                Properties.
              f. Click the Web Site tab. The HTTP port setting is displayed in TCP port and the
                HTTPS port setting is displayed in SSL port.
              g. In the Configuration Manager console, go to Administration > Site
                Configuration > Servers and Site System Roles, then click the
                <SiteSystemName> right-hand pane.
              h. In the bottom pane, right-click Software Update Point and then click
                Properties.
              i. Go to the General tab, specify or verify the WSUS configuration port numbers.

     Authentication errors

     It's typically indicated when the scan fails with authentication errors 0x80244017 (HTTP
     Status 401) or 0x80244018 (HTTP Status 403).

     First, confirm the correct WinHTTP proxy settings using the following commands:
        On Windows Vista or later versions: netsh winhttp show proxy
        On Windows XP: proxycfg.exe

     If the proxy settings are correct, verify connectivity with the WSUS computer by
     completing the steps in HTTP timeout errors. Also review the IIS logs on the WSUS
     computer to confirm that the HTTP errors are being returned from WSUS. If the WSUS
     computer isn't returning the error, the issue is likely with an intermediate firewall or proxy.

     Certificate problems

     Certificate problems are indicated by error code 0x80072F0C that means "A certificate is
     required to complete client authentication". To fix this issue, see Scan fails with error
     0x80072f0c.

Step 4: WUAHandler receives results from Windows
Update Agent and marks the scan as complete
The following are logged in WUAHandler.log:

 Output

 Async searching completed.
 Finished searching for everything in single call.

Troubleshoot issues in step 4
Problems here should be addressed the same way as scan failures in step 3.

<!-- p.789 -->

As mentioned earlier in this guide, when troubleshooting scan failures, check the
WUAHandler.log and WindowsUpdate.log files. WUAHandler simply reports what Windows
Update Agent reported. So the error in WUAHandler would be the same error that was
reported by the Windows Update Agent itself. More information about the error could be
found in WindowsUpdate.log. To understand how to read WindowsUpdate.log, see Windows
Update log files.

There are many reasons why a software update scan might fail. It could be caused by one of
the issues mentioned earlier, or a communication or firewall issue between the client and the
software update point computer. Your best source of information will come from the logs and
the error codes they contain. For more information about the error codes, see Windows
Update common errors and mitigation.

Step 5: WUAHandler parses the scan results
WUAHandler then parses the results, which include the applicability state for each update. As
part of this process, superseded updates are pruned out. The applicability state is checked for
all updates that align to the criteria submitted by CCMExec to the Windows Update Agent. The
important thing to understand here is that you should see applicability results for updates
whether those updates are in a deployment or not.

The following entries are logged in WUAHandler.log:

 Output

 > Pruning: update id (70f4f236-0248-4e84-b472-292913576fa1) is superseded by
 (726b7201-862a-4fde-9b12-f36b38323a6f).
 > ...
 > Update (Installed): Security Update for Windows 7 for x64-based Systems
 (KB2584146) (4ae85c00-0eaa-4be0-b81b-dbd7053d5fae, 104)
 > Update (Missing): Security Update for Windows 7 for x64-based Systems (KB2862152)
 (505fda07-b4f3-45fb-83d9-8642554e2773, 200)
 > ...
 > Successfully completed scan.

Troubleshoot issues in step 5
Problems can be addressed the same way as scan failures in step 3.

As mentioned earlier in this guide, when troubleshooting scan failures, check the
WUAHandler.log and WindowsUpdate.log files. WUAHandler simply reports what Windows
Update Agent reported. So the error in WUAHandler would be the same error that was
reported by the Windows Update Agent itself. More information about the error could be
found in WindowsUpdate.log. To understand how to read WindowsUpdate.log, see Windows
Update log files.

Generally speaking, there are many reasons why a software update scan might fail. It could be
caused by one of the issues mentioned earlier, or by a communication or firewall issue
between the client and the software update point computer. Your best source of information
will come from the logs and the error codes they contain. As a reference, see Windows Update
common errors and mitigation.

Step 6: Update store records the status and raises a
state message for each update in WMI
Once the scan results are available, these results are stored in the updates store. Update store
records the current state of each update and creates a state message for each update. These
state messages are forwarded to the site server in bulk at the end of the status message
reporting cycle (which is minutes, by default). We only send a state message under the
following circumstances:

<!-- p.790 -->

     A previous state message has never been sent for an update (log entry: hasn't been
     reported before, creating new instance).
     The applicability state for an update has changed since the last state message was
     submitted.

UpdatesStore.log showing state for missing update (KB2862152) being recorded and a state
message being raised:

 Output

 Processing update status from update (505fda07-b4f3-45fb-83d9-8642554e2773) with
 ProductID = 0fa1201d-4330-4fa8-8ae9b877473b6441
 Update status from update (505fda07-b4f3-45fb-83d9-8642554e2773) hasn't been
 reported before, creating new instance.
 Successfully raised state message for update (505fda07-b4f3-45fb-83d9-8642554e2773)
 with state (Missing).
 Successfully added WMI instance of update status (505fda07-b4f3-45fb-83d9-
 8642554e2773).

StateMessage.log showing state messaged being recorded with State ID 2 (missing):

 Output

 Adding message with TopicType 500 and TopicId 505fda07-b4f3-45fb-83d9-8642554e2773
 to WMI
 State message(State ID : 2) with TopicType 500 and TopicId 505fda07-b4f3-45fb-83d9-
 8642554e2773 has been recorded for SYSTEM

   Tip

  For each update, an instance of the CCM_UpdateStatus class is created or updated, and it
  stores the current status of the update. The CCM_UpdateStatus class is located in the
  ROOT\CCM\SoftwareUpdates\UpdatesStore namespace.

Troubleshoot issues in step 6
Problems here should be addressed the same way as scan failures in step 3.

As mentioned earlier in this guide, when troubleshooting scan failures, check the
WUAHandler.log and WindowsUpdate.log files. WUAHandler simply reports what Windows
Update Agent reported. So the error in WUAHandler would be the same error that was
reported by the Windows Update Agent itself. More information about the error could be
found in WindowsUpdate.log. To understand how to read WindowsUpdate.log, see Windows
Update log files.

Generally speaking, there are many reasons why a software update scan might fail. It could be
caused by one of the issues mentioned earlier, or by a communication or firewall issue
between the client and the software update point computer. Your best source of information
will come from the logs and the error codes they contain. As a reference, see Windows Update
common errors and mitigation.

Step 7: State messages are sent to the management
point
When WUAHandler successfully receives the results from the Windows Update Agent, it marks
the scan as complete and logs the following message in WUAHandler.log:

 Output

 Async searching completed. WUAHandler
 Finished searching for everything in single call

Troubleshoot issues in step 7

<!-- p.791 -->

Problems here should be addressed the same way as scan failures in step 3, although failures
at this stage will likely be surfaced in the WindowsUpdate.log file specifically. To understand
how to read WindowsUpdate.log, see Windows Update log files.

Generally speaking, there are many reasons why a software update scan might fail. It could be
caused by one of the issues mentioned earlier, or by a communication or firewall issue
between the client and the software update point computer. Your best source of information
will come from the logs and the error codes they contain. As a reference, see Windows Update
common errors and mitigation.

WSUS to Microsoft Update synchronization
WSUS synchronizing with Microsoft Update is outlined in the following steps. Confirm each
step to properly establish where the issue is.

Step 1: Synchronization starts through a scheduled
or manual request
When a synchronization is triggered, we expect to see the following messages within the WSUS
server's SoftwareDistribution.log:

For manual sync:

 Output

 Changew3wp.6AdminDataAccess.StartSubscriptionManuallySynchronization manually
 started
 Info WsusService.27EventLogEventReporter.ReportEvent
 EventId=382,Type=Information,Category=Synchronization,Message=A manual
 synchronization was started.

For scheduled synch:

 Output

 InfoWsusService.10EventLogEventReporter.ReportEvent
 EventId=381,Type=Information,Category=Synchronization,Message=A scheduled
 synchronization was started.

Troubleshoot a manual sync in step 1
   1. Confirm that the WSUS service is running. If a manual synchronization has started but
     stays at 0%, it's because that the WSUS service (Update Services on WSUS 3.x;
     WSUSService on Windows Server 2012 and later versions) is in a stopped state.

   2. Reset the WSUS console MMC cache by following these steps:
      a. Close the WSUS console.
      b. Stop the WSUS service (Update Services on WSUS 3.x; WSUS Service on Windows
        Server 2012 and later versions).
      c. Browse to %appdata%\Microsoft\mmc .
      d. Rename wsus to wsus_bak.
      e. Start the WSUS service.
      f. Open the WSUS console and try another manual synchronization.

Troubleshoot a scheduled sync in step 1
   1. Try a manual synchronization from the WSUS console.
   2. If a manual synchronization works fine, check the scheduled synchronization settings.

Step 2: WSUS spawns a connection to Microsoft
Update (MU)

<!-- p.792 -->

After a synchronization starts, the WSUS server attempts to make an HTTP connection through
WinHTTP. Consider the following factors when troubleshooting the connection:

WSUS <=winhttp=> Network entities <=> Internet

     Does a network entity (proxy, firewall, security filter, and so on) exist between the WSUS
     host machine and the Internet?
     If a proxy exists and the WSUS server is required to use the proxy, is the proxy configured
     within the proper WSUS settings?

Troubleshoot a manual sync in step 2
   1. Confirm that the WSUS service is running. If a manual synchronization has started but it
     stays at 0%, it's because the WSUS service (Update Services on WSUS 3.x; WSUS Service
     on Windows Server 2012 and later versions) is in a stopped state.

   2. Reset the WSUS console MMC cache by completing the following steps:
      a. Close the WSUS console.
      b. Stop the WSUS service (Update Services on WSUS 3.x; WSUS Service on Windows
         Server 2012 and later versions).
      c. Browse to %appdata%\Microsoft\mmc .
      d. Rename wsus to wsus_bak.
      e. Start the WSUS service.
      f. Open the WSUS console and try another manual synchronization.

Troubleshoot a scheduled sync in step 2
   1. Try a manual synchronization from the WSUS console.
   2. If a manual synchronization works fine, check the scheduled synchronization settings.

Step 3: The WSUS computer receives product and
classification information from Microsoft Update and
any subscribed metadata
After WSUS receives product and classification information and any subscribed metadata from
Microsoft Update, the WSUS synchronization is complete.

Installation, supersedence, or detection issues
with specific updates
Deployment issues that occur with specific updates can be broken into the areas below. When
you begin troubleshooting, consider the following components associated with these areas.

                                                                                ﾉ    Expand table

 Areas         Installation                              Supersedence    Detection

 Components          WUA                                 Update               WUA
                     Update Installer (Component-Based   metadata             Update metadata
                     Servicing (CBS), MSI)                                    Update Installer
                     CCMExec                                                  (CBS, MSI)

Installation issues
What is the installer (CBS, MSI, other)?

CBS

<!-- p.793 -->

For updates that apply to Windows Vista and later versions, CBS is used to handle the
installation.

   1. Gather the CBS log ( %Windir%\Logs\Cbs\Cbs.log ) and perform an initial review to gain
      insight into the cause of the failure. Troubleshooting installation-based issues through
      CBS logs is beyond the scope of this guide. For more information, see Fix Windows
      corruption errors by using the DISM or System Update Readiness tool          .
   2. Does the update install successfully as a logged on user? If so, does it fail only when it's
      installed under the System context? In this case, focus on troubleshooting the manual
      installation failure under the System context.

MSI (Windows Installer)
For non-Windows software updates, MSI is used to handle the installation.

   1. Gather and review the default MSI logs for the update. Check the associated KB article for
      the update for any known issues or FAQ.

   2. Enable Windows Installer logging       and reproduce the failure.

      When reviewing the resulting logs, check for return value 3 within the log and the lines
      preceding that entry for insight into the failure.

   3. Check whether the same update fails to install manually under the local system context.
      To do so, use the same installation switches that failed during the software update
      deployment.

      If it fails, test the installation as the logged on user with the same installation switches.
      Check if it's an issue with installing under local system. If it works, you can then focus the
      issue on how to properly install the update using the local system context. It may require
      checking for administrative deployment guidance within the KB for the update or online.

Supersedence issues
Attempt to isolate the issue that relates to supersedence by using the following questions:

   1. For questions about how to control when Configuration Manager expires an update, see
      Supersedence rules.
   2. If an update has been expired by Configuration Manager, Microsoft recommends that the
      latest superseding update be deployed. If you still need to deploy the expired updates,
      they can be deployed outside a software update deployment through software
      distribution or application management.
   3. For questions related specifically to the supersedence logic of an update, first review the
      KB article for the update for further information. You can also review supersedence within
      the Microsoft Update Catalog, WSUS console, or the Configuration Manager console.

Detection issues
Determine compliance state per update on a client
   1. Review the update KB article for known issues with the update.
   2. Run the Software Updates Scan Cycle action on the Configuration Manager client.
   3. Review UpdatesStore.log and WindowsUpdate.log.

Troubleshoot update applicability
   1. Check if any prerequisites are missing using the KB article for the update. For example,
      does the update require the application or OS being patched to a specific service pack
      level?

<!-- p.794 -->

   2. Confirm that the Unique Update ID of the update in question matches what is deployed.
      For example, is the update in question a 32-bit update but is targeted to a 64-bit host?

More information
For more information about how to configure software updates in Configuration Manager, see
the following articles:

      Plan for software updates in Configuration Manager
      How to Configure a Software Update Point to Use Network Load Balancing (NLB) Cluster
      How to Enable CRL Checking for Software Updates

You can also post a question in our Configuration Manager support forum for security,
updates, and compliance here       .

Visit our blog     for all the latest news, information, and tech tips on Configuration Manager.

 Last updated on 03/30/2026

<!-- p.795 -->

Troubleshoot software update
synchronization in Configuration Manager
This article helps you diagnose and resolve some common issues with software update
synchronization in Configuration Manager.

We'll begin by asking if the prerequisites for software update synchronization are met. If you
met the prerequisites but still face the issue, we'll take you through a series of steps to resolve
your issue.

Original product version: Configuration Manager (current branch), Microsoft System Center
2012 R2 Configuration Manager, Microsoft System Center 2012 Configuration Manager
Original KB number: 4505439

Verify the Prerequisites
The first step in troubleshooting synchronization issues is to verify that the following
prerequisites are met:

     Verify that Prerequisites for software updates in Configuration Manager are met.

     When you install the software update point on a remote site system server, the WSUS
     Administration console must be installed on the site server.

     Verify that WSUS running on a software update point isn't configured to be a replica.

     To verify it, open the WSUS console on the software update point. Select Options in the
     console tree pane, and then select Update Source and Proxy Server in the display pane.

     Verify that the Update Services service is running on the WSUS server.

     Verify that the Default website or WSUS Administration website is running on the WSUS
     server.

Check the Update Source settings in WSUS
Check the Update Source settings in the WSUS console on the software update point site
system server. These settings are set automatically by WSUS Configuration Manager (WCM). If
these settings don't match, review WCM.log.

<!-- p.796 -->

To check the update source settings in WSUS, open the WSUS console on the software update
point site system server. Select Options in the console tree pane, and then select Update
Source and Proxy Server in the display pane.

Verify that the following settings are configured correctly:

     Synchronize from Microsoft Update

     Generally, this setting should be selected when you're in the WSUS console on the
     software update point for the top-level site. Starting with Configuration Manager 2012
     SP1, you can specify an existing WSUS server as the upstream synchronization source
     location for the top-level site. If you've specified an existing WSUS server as the upstream
     source location, then this setting shouldn't be selected.

     Synchronize from another Windows Server Update Services server

     Generally, this setting should be selected when you're in the WSUS console for:
        Software update points for top-level site if an upstream source location is specified
        instead of Microsoft Update.
        Software update points for a primary site.
        Other software update points installed in the primary site.
        Internet-based software update points.
        Software update points for a secondary site.

     Server name: It should be the fully qualified domain name (FQDN) of the upstream
     update source.
        For the first software update point in the primary site, it should be the software update
        point for the parent site.
        For other software update points in the site, it should be the first software update
        point on the same site.
        For an Internet-based software update point, it should be the first software update
        point on the same site.

     Port number: It should be the port number for the upstream WSUS server. To determine
     the port number on the upstream WSUS server, see Determine the port settings used by
     WSUS and the software update point.

     Use SSL when synchronizing update information: When the software update point is in
     HTTPS mode, this setting must be selected. When using Secure Sockets Layer (SSL) for

<!-- p.797 -->

     software updates, several requirements apply. For more information, see Check SSL
     configuration.

     This server is a replica of the upstream server: Never select this setting on the software
     update point for the top-level site or the first software update point for the primary site.
     This setting should be selected on:
           Internet-based software update points
           Other software update points for the primary site.
           Software update points for a secondary site

Synchronization fails because of authentication and
proxy issues
WSUS Configuration Manager configures the WSUS server once every hour. It does so to
ensure that the settings configured in WSUS match the setting specified in the Configuration
Manager console.

If WCM fails to configure the WSUS server properly, synchronization attempts can fail with an
error similar to the following screenshot:

You'll also find the following error in the WsyncMgr.log file on the site server (located in
\Logs ):

  Sync failed: WSUS server not configured. Please refer to WCM.log for configuration error
  details. Source: CWSyncMgr::DoSync

<!-- p.798 -->

  Sync failed. Will retry in 60 minutes

Synchronization may fail because of authentication or proxy issues. When this issue occurs,
you'll see an error similar to the following error in the WCM.log file:

  System.Net.WebException: The request failed with HTTP status 502

The error may not always be HTTP status 502, and may in fact be one of the following errors:

     HTTP Status 401 Unauthorized
     HTTP Status 403 Forbidden
     HTTP Status 407 Proxy Authentication Required
     HTTP Status 502 Proxy Error
     No connection could be made because the target machine actively refused it
     Authentication failed because the remote party has closed the transport stream

To troubleshoot authentication or proxy issues, follow these steps:

   1. Verify that the Update Services service is running on the WSUS server.
   2. Verify that the Default website or WSUS Administration website is running on the WSUS
     server.
   3. Verify that the fully qualified domain name (FQDN) for the software update point site
     system server is correct and accessible from the site server.
   4. If the software update point is remote from the site server, verify that you can connect to
     the WSUS server from the site server. For more information, see Check connectivity from
     the site server to the WSUS server.
   5. Check the port settings configured for the software update point. Verify that they're the
     same as the port settings configured for the website used by WSUS running on the
     software update point. For more information, see Determine the port settings used by
     WSUS and the software update point.
   6. Verify that the proxy and account settings are correctly configured for the software
     update point. For more information, see Configure proxy setting for the software update
     point.
   7. Verify that the software update point connection account is configured (if necessary). And
     verify that it has permissions to connect to the WSUS server. For more information, see
     Configure the WSUS Server Connection Account for the software update point.
   8. Verify that the permissions on the ApiRemoting30 virtual directory are set correctly in IIS.
     When WSUS Synchronization Manager starts synchronization, the computer and

<!-- p.799 -->

     Administrator accounts must have access to the ApiRemoting30 virtual directory under the
     WSUS website in IIS. To check permissions on the ApiRemoting30 virtual directory:
      a. On the WSUS server, open IIS Manager.
      b. Expand Sites, expand the website for the WSUS server, right-click the ApiRemoting30
        virtual directory, and then select Edit Permissions.
   9. If the software update point is configured for SSL (HTTPS), verify that WSUS is correctly
     configured for SSL. For more information, see Check SSL configuration.
 10. Review WSUSCtrl.log for errors. For more information, see WSUS Control Manager
     reports an error.

Synchronization fails because of web service issues
Synchronization may be failing because of issues with the web service. When this issue occurs,
you'll see an error similar to the following errors in the WCM.log file:

  System.Net.WebException: The request failed with HTTP status 500

  System.Net.WebException: The request failed with HTTP status 503

To troubleshoot web service issues, follow these steps:

   1. Verify that the Update Services service is running on the WSUS server.
   2. Verify that the Default website or WSUS Administration website is running on the WSUS
     server.
   3. Check the port settings configured for the software update point. Verify that they're the
     same as the port settings configured for the website used by WSUS running on the
     software update point. For more information, see Determine the port settings used by
     WSUS and the software update point.
   4. Review WSUSCtrl.log for errors. For more information, see WSUS Control Manager
     reports an error.

Synchronization fails because of SSL issues
If you're using SSL, verify the following settings:

     Verify that the certificate configured for the WSUS website is configured with the correct
     FQDN. If the certificate doesn't have the correct FQDN, see Add a subject alternative
     name to a secure LDAP certificate.
     Verify that the certificate hasn't expired.

<!-- p.800 -->

     Verify that WSUS is correctly configured for SSL. For more information, see Check SSL
     configuration.

Synchronization fails because of issues with the EULA
Synchronization issues can often be traced back to issues relating to the End User Licensing
Agreement (EULA). To verify whether it's your issue, follow these steps:

   1. Review the SoftwareDistribution.log file on the WSUS server to find out why the EULAs
     aren't getting downloaded. Look for .txt in the log to find relevant entries.

   2. Verify that the firewall is configured to allow communication with Microsoft Update. For
     more information, see Connection from the WSUS server to the Internet.

   3. Verify the proxy server settings.

   4. Run the following command from a Command Prompt to have WSUS download the
     missing content again, including EULAs:

      %ProgramFiles%\Update Services\Tools\wsusutil.exe reset

Synchronization fails because of errors
communicating with Microsoft Update
When this issue occurs, you usually receive the following errors:

  A connection attempt failed because the connected party did not properly respond after a
  period of time, or established connection failed because connected host has failed to
  respond.

  0x80072EFE - The connection with the server was terminated abnormally

To troubleshoot this issue, follow these steps:

   1. Verify that the WSUS server can connect to the Internet.
   2. Verify that the firewall is configured to allow communication with Microsoft Update. For
     more information, see Connection from the WSUS server to the Internet.
   3. Verify the proxy server settings.

WSUS Control Manager reports an error
