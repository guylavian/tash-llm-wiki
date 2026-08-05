---
title: "Welcome — pages 201-240"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0201-0240
family: sccm
documentKind: "doc"
abstract: "the package. SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) RCV: INSERT on PkgNotification for PkgNotify_Add [P010000F ][145011] SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) SND: Dropped E:\\ConfigMgr\\inboxes\\distmgr.box\\P010000F.PKN [145011] Step 4: DistMgr wakes up to pro"
---

# Welcome — pages 201-240

<!-- p.201 -->

the package.

  SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) RCV: INSERT on PkgNotification
  for PkgNotify_Add [P010000F ][145011]
  SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\P010000F.PKN [145011]

Step 4: DistMgr wakes up to process the package
DistMgr wakes up after detecting the PKN file and processes the package.

  1. Main DistMgr thread starts a Package Processing Thread.

     Main DistMgr thread adds the package to the package processing queue, and creates a
     package processing thread.

       SMS_DISTRIBUTION_MANAGER 5292 (0x14ac) Adding package 'P010000F' to
       package processing queue.
       SMS_DISTRIBUTION_MANAGER 5292 (0x14ac) ~Currently using 0 out of 3 allowed
       package processing threads.
       SMS_DISTRIBUTION_MANAGER 5292 (0x14ac) ~Started package processing thread
       for package 'P010000F', thread ID = 0x2C44 (11332)

  2. Package processing thread creates DP thread(s) to process package actions and waits for
     them to exit.

     Package processing thread (TID 11332) processes the package actions
     (add/update/remove) for the DP(s). In this case, the package was added to a DP and the
     package processing thread creates a DP thread to add the package to the DP. After
     creating DP thread(s), the package processing thread waits for all the DP threads to exit
     before moving further.

       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~Processing package P010000F
       (SourceVersion:3;StoredVersion:3)
       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) No action specified for the package
       P010000F, however there may be package server changes for this package.
       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) Start adding package P010000F to
       server ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\...

<!-- p.202 -->

    SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~Created DP processing thread
    22444 for addition or update of package P010000F on server
    ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~Waiting for all DP threads to
    complete for package P010000F processing thread.

3. DP thread creates a PkgXferMgr job to transfer content to the DPs and exits.

  DP thread (TID 22444) starts working on adding the package to the DP. DP threads do
  not copy the package contents to the DP directly, and instead create a job for Package
  Transfer Manager (PkgXferMgr) instructing it to copy the package contents to the DP.
  Following log entries show the DP thread creating a PkgXferMgr job. After the job is
  created, DP thread's work is done and the DP thread exits.

    SMS_DISTRIBUTION_MANAGER 22444 (0x57ac) DP Thread: Attempting to add or
    update package P010000F on DP ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 22444 (0x57ac) Package Server
    ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\ is a PullDP.
    SMS_DISTRIBUTION_MANAGER 22444 (0x57ac) ~Created package transfer job to
    send package P010000F to distribution point
    ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\.
    SMS_DISTRIBUTION_MANAGER 22444 (0x57ac) STATMSG: ID=2357 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=P01SITE.CONTOSO.COM SITE=P01 PID=36968 TID=22444 GMTDATE=Mon Jan
    07 20:05:18.665 2019 ISTR0="P010000F" ISTR1="
    ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
    ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="P010000F"
    AID1=404 AVAL1="["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\"

  When the DP thread creates a PkgXferMgr job, it does so by inserting a row in
  DistributionJobs table.

<!-- p.203 -->

       SQL

       insert into DistributionJobs
       (DPID,PkgID,PackageVersion,State,CreationTime,Action)
       values(8,N'P010000F',3,0,N'2019/01/07 20:05:18',1)

     After creating the job, the DP thread also resets the Action for the DP in PkgServers_L
     table.

   4. Package processing thread exits after all DP threads exit.

     After all the DP threads exit, package processing thread exits as well.

       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~DP thread for package P010000F
       with thread handle 0000000000003E2C and thread ID 22444 ended.
       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~All DP threads have completed for
       package P010000F processing thread.
       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~StoredPkgVersion (3) of package
       P010000F. StoredPkgVersion in database is 3.
       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~SourceVersion (3) of package
       P010000F. SourceVersion in database is 3.
       SMS_DISTRIBUTION_MANAGER 11332 (0x2c44) ~Exiting package processing thread
       for package P010000F.

Step 5: SMSDBMON notifies PkgXferMgr to process the job
After the PkgxferMgr job is created, SMSDBMON this time detects a change in
DistributionJobs table and drops a PKN file in PkgTransferMgr.box to instruct PkgXferMgr to

process the job.

  SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) RCV: UPDATE on
  DistributionJobs for DistributionJob_Creation [P010000F ][145013]
  SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) SND: Dropped
  E:\ConfigMgr\inboxes\PkgTransferMgr.box\P010000F.PKN [145013]

Step 6: PkgXferMgr wakes up to process the job
   1. Main PkgXferMgr thread creates a pull DP sending thread to send the package to the
     specified DP.

<!-- p.204 -->

    SMS_PACKAGE_TRANSFER_MANAGER 32936 (0x80a8) Found send request with ID:
    190, Package: P010000F, Version:3, Priority: 2, Destination: P01PDP1.CONTOSO.COM,
    DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 32936 (0x80a8) ~Created sending thread
    (Thread ID = 0x2B4C)

2. Pull DP sending thread sends a notification to the pull DP

  Unlike a regular sending thread, pull DP sending thread (TID 11084) instructs the pull DP
  to start downloading the content by sending a notification. This is done in 4 phases.

  Phase 1: Pull DP sending thread checks to see if the content being distributed to the pull
  DP is available on a source DP(s). If the content is not available on the source DP, the pull
  DP sending thread ends with the below message in the log and raises Status Message ID
  8212 which means 'This pull distribution point has no sources from which it can download
  content. We will try again later.' Retries are attempted later based on Retry settings
  configured in Software Distribution Component Configuration > Pull Distribution Point
  tab.

    ~Unable to find any source locations for one or more contents under package
    P0100009, for pull DP P01PDP1.CONTOSO.COM. Notification not sent.
    ~ PullDP notification failed. Failure count = 1/30, Restart time = 1/10/2019 2:00:42
    AM Eastern Standard Time
    STATMSG: ID=8212 SEV=I LEV=M SOURCE='SMS Server'
    COMP='SMS_PACKAGE_TRANSFER_MANAGER' SYS=P01SITE.CONTOSO.COM
    SITE=P01 PID=2336...

  Here's the query that is executed to check if content is available on a source DP:

    SQL

    SELECT p.SourceDPServerName FROM PullDPMap p INNER JOIN ContentDPMap c ON
    p.SourceDPServerName = c.ServerName WHERE c.AccessType = 1 AND
    p.PullDPServerName = 'P01PDP1.CONTOSO.COM' AND c.ContentID = 'P0100009' AND
    c.Version = 4

  Phase 2: Pull DP sending thread checks to see if the pull DP has capacity for more jobs. By
  default, pull DPs can handle 50 jobs simultaneously. This is controlled by the PullDP
  Number Of Active Jobs SCF property for SMS_DISTRIBUTION_MANAGER and it's not
  recommended to increase the capacity because it can introduce scalability issues. If the

<!-- p.205 -->

pull DP is already working at max capacity (i.e., it has 50 running jobs), the pull DP
sending thread ends with the below message in the log and retries later based on Retry
settings configured in Software Distribution Component Configuration > Pull
Distribution Point tab.

  PullDP <DPNALPATH> has reached maximum capacity 50
  PullDP has no capacity. Restart time = <timestamp>
  STATMSG: ID=8211 SEV=E LEV=M SOURCE="SMS Server"
  COMP="SMS_PACKAGE_TRANSFER_MANAGER" SYS=P01SITE.CONTOSO.COM
  SITE=P01 PID=17252 TID=4712…

Here's the query that is used to determine if pull DP is at capacity:

 SQL

 SELECT COUNT(*) FROM DistributionJobs job
 JOIN DistributionPoints dp ON dp.DPID=job.DPID AND
 dp.NALPath='["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
 ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\'
 WHERE job.State in (2, 3, 4) AND (job.Action<>5) AND (ISNULL(job.SendAction,
 '') <> '')

Phase 3: Pull DP sending thread sends a package info bundle file which contains a
metadata of the files that need to be downloaded. This file is a <PackageID>.TZ file which
generated from the package INI file from the site servers content library and is copied to
the SMS_DP$ directory on the pull DP.

  SMS_PACKAGE_TRANSFER_MANAGER 11084 (0x2b4c) Pull DP Sending thread starting
  for Job: 190, package: P010000F, Version: 3, Priority: 2, server:
  P01PDP1.CONTOSO.COM, DPPriority: 200
  SMS_PACKAGE_TRANSFER_MANAGER 11084 (0x2b4c) Sending package info bundle
  P010000F to PullDP. ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\

Phase 4: Pull DP sending thread creates an instance of SMS_PullDPNotification class on
the pull DP within root\SCCMDP namespace, which contains the package ID, package
version and an XML notification. After creating the instance of SMS_PullDPNotification
class, it executes the NotifyPullDP method in the SMS_DistributionPoint class in the
root\SCCMDP namespace which instructs the DP WMI Provider to notify the pull DP

component to start downloading the content.

<!-- p.206 -->

    SMS_PACKAGE_TRANSFER_MANAGER 11084 (0x2b4c) ~Successfully performed WMI
    actions on pull DP P01PDP1.CONTOSO.COM.
    SMS_PACKAGE_TRANSFER_MANAGER 11084 (0x2b4c) ~ PullDP notification sent.
    Attempted count = 1/30, Restart time = 1/7/2019 4:06:04 PM Eastern Standard Time
    SMS_PACKAGE_TRANSFER_MANAGER 11084 (0x2b4c) Pull DP Sending thread
    complete~

  Notification XML is generated by calling fnGetPullDPXMLNotification . Here's how a
  sample query that generates the notification XML query looks like which shows that the
  Action is add since the content was not redistributed:

    SQL

    SELECT [dbo].[fnGetPullDPXMLNotification]('P010000F', 3,
    'P01PDP1.CONTOSO.COM', 2, 'add', 1, 'O:SYG:BAD:P(A;;FA;;;BA)(A;OICIIO;GA;;;BA)
    (A;;0x1200a9;;;BU)(A;OICIIO;GXGR;;;BU)(A;;FA;;;BA)(A;OICIIO;GA;;;BA)', 0,
    32780, '3ED23B9869F7E10E19439F11341405FF76E22022E56468DCF211475899BD2914', '')
    AS Notification

  The XML notification contains the content metadata along with the source DP location.
  Here's how a sample XML notification looks like:

    XML

    <PullDPNotification>
       <PullDPPackageNotification PackageID='P010000F' Version='3' Action='redist'
    AllowFallback='true' Priority='2' PackageType='content' PackageTypeID='8'
    PackageFlags='16777216' PackageSize='5532' SDDL='O:SYG:BAD:P(A;;FA;;;BA)
    (A;OICIIO;GA;;;BA)(A;;0x1200a9;;;BU)(A;OICIIO;GXGR;;;BU)(A;;FA;;;BA)
    (A;OICIIO;GA;;;BA)' HashAlgorithm='32780'
    Hash='3ED23B9869F7E10E19439F11341405FF76E22022E56468DCF211475899BD2914'
    ExpandShare='0' ShareName='' ShareType='1'>
         <PullDPPackageContent ContentID='Content_3c9813ba-d7ab-4963-929c-
    36f90f479613.1' RelatedContentID='Content_162d6f21-176e-4e4b-a620-
    6e94a4b9f73e.1'>
            <DPLocation
    DPUrl='http://P01MP.CONTOSO.COM/SMS_DP_SMSPKG$/Content_3c9813ba-d7ab-4963-
    929c-36f90f479613.1' Rank='1' Type='Windows NT Server' Protocol='https' />
         </PullDPPackageContent>
       </PullDPPackageNotification>
    </PullDPNotification>

3. Pull DP sending thread updates the job so status polling can start.

<!-- p.207 -->

  Unlike a sending thread for a standard DP which deletes the job after successful
  completion, pull DP sending thread updates the job in DistributionJobs table and sets
  the SendAction to PullQueryResultAction after successfully sending the notification to
  the pull DP.

    SQL

    update DistributionJobs set DPID=8,SendAction = N'PullQueryResultAction',
    LastUpdateTime = N'2019/01/07 21:07:14' where JobID = 194

  State messages are used as the primary mechanism for distribution status reporting from
  the pull DP and the distribution job remains in the database until we are notified of
  success/failure status of the job. PkgXferMgr starts polling at scheduled intervals
  (configurable in the Software Distribution Component Properties > Pull Distribution
  Point tab) to check whether the content has been downloaded on the pull DP. Although
  the pull DP sends a state message containing the distribution status, PkgXferMgr also
  performs polling as a backup mechanism to get the distribution status in case pull DP
  cannot send a state message to the management point for some reason.

4. (On polling interval): Pull DP sending thread is created to poll the distribution status from
  the pull DP.

  A new pull DP sending thread starts after Delay before polling (minutes) value specified
  in the Software Distribution Component Properties to check the distribution status. In
  the below example, it queries the pull DP and finds that the content has been installed
  successfully and sends a status message to Distribution Manager.

    SMS_PACKAGE_TRANSFER_MANAGER 18724 (0x4924) Pull DP Sending thread starting
    for Job: 194, package: P010000F, Version: 3, Priority: 2, server:
    P01PDP1.CONTOSO.COM, DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 18724 (0x4924) ~Finished sending SWD
    package P010000F version 3 to distribution point P01PDP1.CONTOSO.COM
    SMS_PACKAGE_TRANSFER_MANAGER 18724 (0x4924) Sent status to the distribution
    manager for pkg P010000F, version 3, status 3 and distribution point
    ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\~
    SMS_PACKAGE_TRANSFER_MANAGER 18724 (0x4924) STATMSG: ID=8210 SEV=I
    LEV=M SOURCE="SMS Server" COMP="SMS_PACKAGE_TRANSFER_MANAGER"
    SYS=P01SITE.CONTOSO.COM SITE=P01 PID=36968 TID=18724 GMTDATE=Mon Jan

<!-- p.208 -->

       07 22:22:16.059 2019 ISTR0="P010000F" ISTR1="3"
       ISTR2="P01PDP1.CONTOSO.COM" ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7=""
       ISTR8="" ISTR9="" NUMATTRS=3 AID0=400 AVAL0="P010000F" AID1=410
       AVAL1="3" AID2=404 AVAL2="["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\"
       SMS_PACKAGE_TRANSFER_MANAGER 18724 (0x4924) Pull DP Sending thread
       complete~

     Note that the job is deleted from the database when after receiving a success status
     message from the pull DP, which causes the polling to stop.

Step 7: SMS DP Provider notifies pull DP component
(CcmExec) to process the job
On execution of the NotifyPullDP method, DP WMI Provider notifies CcmExec which hosts the
pull DP component. SMSDPProv.log shows:

  4688 (0x1250) Successfully notified PullDP

Step 8: Pull DP loads the job(s) from WMI
On receiving a notification, pull DP component loads the job(s) from WMI as well as validates
the <PackageID>.TZ file that was copied by PkgxferMgr.

  PullDP 4404 (0x1134) CPullDPService::LoadJobsFromXML for P010000F.3
  PullDP 4404 (0x1134) - P010000F.3 - XML has 1 content jobs.
  PullDP 4404 (0x1134) CPullDPPkgContJob::LoadContentJobFromXML(): Set JobState =
  NotStarted
  PullDP 4404 (0x1134) - P010000F.3 - Loaded content job {C10457F9-DE3A-4B45-878C-
  345919AFF97E} for content Content_3c9813ba-d7ab-4963-929c-36f90f479613.1 from
  XML...
  PullDP 4404 (0x1134) CPullDPPkgJob::LoadJobFromXML() successfully loaded job for
  package P010000F.3, there are 1 content jobs. ...
  PullDP 4404 (0x1134) Successfully verified content info Hash E:\SMS_DP$\P010000F.tz
  :3ED23B9869F7E10E19439F11341405FF76E22022E56468DCF211475899BD2914
  PullDP 4404 (0x1134) CPullDPService::ExecuteJobs(). 1 jobs to do

<!-- p.209 -->

Step 9: Pull DP creates content job(s) to download the content
associated with the package
  PullDP 4404 (0x1134) P010000F.3 Starting Download there are 1 content jobs.
  PullDP 3812 (0xee4) Content job {C10457F9-DE3A-4B45-878C-345919AFF97E} running.
  PullDP 3812 (0xee4) ContentExecuteJob {C10457F9-DE3A-4B45-878C-345919AFF97E}
  (state: 1-NotStarted) for package P010000F.3 content Content_3c9813ba-d7ab-4963-929c-
  36f90f479613.1.

In the example above, the job {C10457F9-DE3A-4B45-878C-345919AFF97E} is associated with
content Content_3c9813ba-d7ab-4963-929c-36f90f479613.1. For a package with multiple
content items, you would see the number of jobs (with a unique ID) associated with the
package.

  PullDP 1320 (0x528) P010000A.2 Starting Download there are 2 content jobs.
  PullDP 5012 (0x1394) ContentExecuteJob {55692006-DFE8-4357-86D9-9839C8BF79CF}
  (state: 1-NotStarted) for package P010000A.2 content 2484568c-7aba-44ae-8557-
  05b61d62e70d.
  PullDP 4112 (0x1010) ContentExecuteJob {7175CD81-CF67-48C9-AA22-010BF60B640E}
  (state: 1-NotStarted) for package P010000A.2 content c085b4ba-8e8f-42bf-8e2d-
  bc1067697722.

Step 10: (If applicable) Pull DP downloads content signature
(If applicable) Content job creates a Data Transfer Service (DTS) job to download the package
signature. The signature file is a TAR file which is downloaded from the SMSSIG$ virtual
directory from the source distribution point and contains the RDC signatures for each file in the
content. The RDC signatures are used to determine if the file content have changed and
whether to download delta content or full content. This step is only applicable for content that
has changed, so you may not always see this step, and would see step 11 instead.

  PullDP 3812 (0xee4) Created SignatureDownload DTS job {3C962758-7ABE-40F2-A585-
  E5B59E378BEA} for package P010000F.3, content id Content_3c9813ba-d7ab-4963-929c-
  36f90f479613.1. JobState = NotStarted
  PullDP 3812 (0xee4) CPullDPPkgContJob::NotifyDeltaDownload. JobState = [Downloading
  Signature] Content_3c9813ba-d7ab-4963-929c-36f90f479613.1 for package P010000F.3
  content job id {C10457F9-DE3A-4B45-878C-345919AFF97E}
  PullDP 752 (0x2f0) ContentExecuteJob {C10457F9-DE3A-4B45-878C-345919AFF97E} (state:

<!-- p.210 -->

  4-Downloading Signature) for package P010000F.3 content Content_3c9813ba-d7ab-4963-
  929c-36f90f479613.1.

DataTransferService.log shows the progress of the DTS job, which creates a BITS job to
download the signature file and notifies upon completion:

  DataTransferService 3812 (0xee4) DTSJob {3C962758-7ABE-40F2-A585-E5B59E378BEA}
  created to download from '< https://P01MP.CONTOSO.COM:443/SMS_DP_SMSSIG$ >' to
  'E:\SMS_DP$\P010000F\Content_3c9813ba-d7ab-4963-929c-36f90f479613.1'.
  DataTransferService 3856 (0xf10) Starting BITS download for DTS job '{3C962758-7ABE-
  40F2-A585-E5B59E378BEA}'.
  DataTransferService 3856 (0xf10) Starting BITS job '{43647077-986C-4727-A954-
  B327ECA50302}' for DTS job '{3C962758-7ABE-40F2-A585-E5B59E378BEA}' under user 'S-
  1-5-18'.
  DataTransferService 3856 (0xf10) Adding to BITS job: Content_3c9813ba-d7ab-4963-929c-
  36f90f479613.1.tar
  DataTransferService 2528 (0x9e0) DTSJob {3C962758-7ABE-40F2-A585-E5B59E378BEA}
  successfully completed download.
  DataTransferService 3856 (0xf10) Execute called for DTS job '{3C962758-7ABE-40F2-A585-
  E5B59E378BEA}'. Current state: 'RetrievedData'.
  DataTransferService 3856 (0xf10) DTSJob {3C962758-7ABE-40F2-A585-E5B59E378BEA} in
  state 'NotifiedComplete'.
  DataTransferService 3856 (0xf10) DTS job {3C962758-7ABE-40F2-A585-E5B59E378BEA} has
  completed:

Pull DP receives the completion notification, and processes the signatures to determine if full
or delta download is required.

  PullDP 4300 (0x10cc) DTS message for content job {C10457F9-DE3A-4B45-878C-
  345919AFF97E} received, searching 1 active jobs for any containing this content job. DTS
  Job is {3C962758-7ABE-40F2-A585-E5B59E378BEA}
  PullDP 4300 (0x10cc) DTS succeeded message received for P010000F.3, content job
  {C10457F9-DE3A-4B45-878C-345919AFF97E}, status is 0x0 :
  PullDP 3856 (0xf10) ContentExecuteJob {C10457F9-DE3A-4B45-878C-345919AFF97E}
  (state: 5-Signature Downloaded) for package P010000F.3 content Content_3c9813ba-d7ab-
  4963-929c-36f90f479613.1.

<!-- p.211 -->

Step 11: Pull DP creates a DataTransferService (DTS) job for
content download
Pull DP creates a download job for the content. In this example, the content did not exist on
the pull DP so a full download DTS job is created for the package. The DTS job can be used to
track the download process in the DataTransferService.log in the next step:

  PullDP 4300 (0x10cc) DTS message for content job {C10457F9-DE3A-4B45-878C-
  345919AFF97E} received, searching 1 active jobs for any containing this content job. DTS
  Job is {3C962758-7ABE-40F2-A585-E5B59E378BEA}
  PullDP 4300 (0x10cc) DTS succeeded message received for P010000F.3, content job
  {C10457F9-DE3A-4B45-878C-345919AFF97E}, status is 0x0 :
  PullDP 3856 (0xf10) ContentExecuteJob {C10457F9-DE3A-4B45-878C-345919AFF97E}
  (state: 5-Signature Downloaded) for package P010000F.3 content Content_3c9813ba-d7ab-
  4963-929c-36f90f479613.1. ...
  PullDP 3856 (0xf10) File To Download: ConfigMgrTools.msi
  PullDP 3856 (0xf10) Content_3c9813ba-d7ab-4963-929c-36f90f479613.1: 0 files already
  exists, 1 files to download
  PullDP 3856 (0xf10) Created FullDownload(Manifest) DTS job {78635652-3D12-4A26-A51B-
  D553934ECB54} for package P010000F.3, content id Content_3c9813ba-d7ab-4963-929c-
  36f90f479613.1, content job id {C10457F9-DE3A-4B45-878C-345919AFF97E}.

Step 12: DTS creates a BITS job which downloads the content
and sends a completion notification
DataTransferService.log shows the progress of the job. With verbose logging enabled for the
pull DP, PullDP.log would show more information about the download progress as well.

  DataTransferService 3856 (0xf10) DTSJob {78635652-3D12-4A26-A51B-D553934ECB54}
  created to download from
  '< https://P01MP.CONTOSO.COM:443/SMS_DP_SMSPKG$/Content_3c9813ba-d7ab-4963-929c-
  36f90f479613.1 >' to 'E:\SMS_DP$\P010000F\Content_3c9813ba-d7ab-4963-929c-

  36f90f479613.1\3'.
  DataTransferService 3812 (0xee4) Starting BITS job '{04498466-5A8E-4A22-97F2-
  A66306143A20}' for DTS job '{78635652-3D12-4A26-A51B-D553934ECB54}' under user 'S-
  1-5-18'.
  DataTransferService 3812 (0xee4) DTSJob {78635652-3D12-4A26-A51B-D553934ECB54} in
  state 'DownloadingData'.

<!-- p.212 -->

  DataTransferService 752 (0x2f0) DTS job {78635652-3D12-4A26-A51B-D553934ECB54} has
  completed:

Step 13: Pull DP moves the content to Downloaded state
After the DTS job finishes, pull DP is notified and moves the content to Downloaded state:

  PullDP 3812 (0xee4) DTS message for content job {C10457F9-DE3A-4B45-878C-
  345919AFF97E} received, searching 1 active jobs for any containing this content job. DTS
  Job is {78635652-3D12-4A26-A51B-D553934ECB54}
  PullDP 3812 (0xee4) DTS succeeded message received for P010000F.3, content job
  {C10457F9-DE3A-4B45-878C-345919AFF97E}, status is 0x0 :
  PullDP 3856 (0xf10) ContentExecuteJob {C10457F9-DE3A-4B45-878C-345919AFF97E}
  (state: 9-Downloaded) for package P010000F.3 content Content_3c9813ba-d7ab-4963-
  929c-36f90f479613.1.

Step 14: Content is moved to the content library and state
moves to Succeeded
After the content is successfully Downloaded, pull DP then moves the content to the content
library (which is also known as Single Instance Storage). After the content is moved to the
content library, the content moves to SIApplied state followed by the Succeeded state.

  PullDP 3856 (0xf10) CPullDPPkgContJob::ApplySingleInstancing(): JobState = Downloaded
  PullDP 3856 (0xf10) CPullDPPkgContJob::NotifySIApplied(). JobState = SIApplied
  PullDP 3812 (0xee4) Content job {C10457F9-DE3A-4B45-878C-345919AFF97E} running.
  PullDP 3812 (0xee4) ContentExecuteJob {C10457F9-DE3A-4B45-878C-345919AFF97E}
  (state: 13-SIApplied) for package P010000F.3 content Content_3c9813ba-d7ab-4963-929c-
  36f90f479613.1.
  ...
  PullDP 3812 (0xee4) CPullDPPkgContJob::NotifySucceeded(). Content job {C10457F9-DE3A-
  4B45-878C-345919AFF97E} for package P010000F.3 and content Content_3c9813ba-d7ab-
  4963-929c-36f90f479613.1 has completed successfully. JobState = Succeeded
  PullDP 3812 (0xee4) Notification that content job {C10457F9-DE3A-4B45-878C-
  345919AFF97E} for package P010000F.3 has completed.

<!-- p.213 -->

After each content item is added to the content library, SMSDPProv.log is also notified and
reports the following:

  4688 (0x1250) Content 'Content_3c9813ba-d7ab-4963-929c-36f90f479613.1' for package
  'P010000F' has been added to content library successfully

Note that there may be multiple content items associated with a single package (for example,
an application with more than a Deployment Type or a Software Update Package). For each
content associated with the package, a DTS job is created for content download and the
content is moved to the content library (Succeeded state) upon successful completion. Because
of this, you may see multiple content items for a package move to Succeeded state in the
PullDP.log but the overall package status may still remain in In Progress state if other content
items that are part of the package are still be downloading.

Step 15: After all content is downloaded, package moves to
'Succeeded' state
After all the content jobs for the package have completed successfully and applied to the
content library, pull DP moves the package to Succeeded state.

  PullDP 3812 (0xee4) All 1 content jobs for P010000F.3 have completed, notify of success for
  this pull dp job.
  PullDP 3812 (0xee4) P010000F.3 has completed successfully, will clear stored content job
  state.

Step 16: Pull DP sends a state message to the management
point (MP)
After completion of the download, a state message is sent to the management point with State
ID 1 indicating Success.

  PullDP 3812 (0xee4) Report state message 0x00000001 (1) to MP for package 'P010000F.3'
  PullDP 3812 (0xee4) Request was successful.
  PullDP 3812 (0xee4) CPullDPResponse::ReportPackageState return value 0x00000000.

With verbose and debug logging enabled, you can see the entire message body:

<!-- p.214 -->

  PullDP 3812 (0xee4) Sending Report
  PullDP 3812 (0xee4) <Report><ReportHeader><Identification><Machine>
  <ClientInstalled>0</ClientInstalled><ClientType>1</ClientType>
  <Unknown>0</Unknown><ClientID IDType="0" IDFlag="1">00001111-aaaa-2222-bbbb-
  3333cccc4444</ClientID><ClientVersion>5.00.0000.0000</ClientVersion>
  <NetBIOSName>P01PDP1.CONTOSO.COM</NetBIOSName>
  <CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
  </Machine></Identification><ReportDetails>
  <ReportContent>StateMessage</ReportContent><ReportType>Full</ReportType>
  <Date>20190107200618.000000+000</Date><Version>1.0</Version>
  <Format>1.1</Format></ReportDetails></ReportHeader>
  <ReportBody><StateMessage MessageTime="20190107200618.000000+000"
  SerialNumber="3"><Topic ID="P010000F" Type="902" IDType="0"/><State ID="1"
  Criticality="0"/><UserParameters Flags="0" Count="4"><Param>P010000F</Param>
  <Param>["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\</Param><Param>{11112222-bbbb-3333-
  cccc-4444dddd5555}</Param><Param></Param></UserParameters></StateMessage>
  </ReportBody>

During content download, there are intermediate state messages sent to the MP which include
the download percentage. To see all available State IDs, see Advanced troubleshooting tips for
Content Distribution.

Step 17: Pull DP clears the content job state in WMI
After sending the Success state message, pull DP clears the job states for the package.

  PullDP 3812 (0xee4) Clearing content job states for all 1 content jobs in package
  P010000F.3.
  PullDP 3812 (0xee4) CPullDPService::ClearCompletedJobs(), removing 1 completed jobs.
  PullDP 3812 (0xee4) Removing job for package P010000F.3 from job array and WMI.
  PullDP 3812 (0xee4) Clearing content job states for all 1 content jobs in package
  P010000F.3.

Step 18: MP_Relay endpoint on the MP receives the state
message and moves it to site server

<!-- p.215 -->

MP_Relay endpoint on the management point processes the state message and routes the

state message SMX file to the auth\statesys.box\incoming directory on the site server. If the
MP is co-located on the site server (example below), it's directly sent to the
inboxes\auth\statesys.box\incoming directory. If the MP is remote, it moves it to

\mp\outboxes\StateMsg.box directory on the MP, and MP file dispatch manager (MPFDM)

moves the file to the inboxes\auth\statesys.box\incoming directory on the site server.

  MP_RelayEndpoint 25912 (0x6538) Mp Message Handler: start message processing for
  Relay. -----------------------
  MP_RelayEndpoint 25912 (0x6538) Mp Message Handler: FileType=SMX
  MP_RelayEndpoint 25912 (0x6538) Message Body :
  <Report><ReportHeader><Identification><Machine>
  <ClientInstalled>0</ClientInstalled><ClientType>1</ClientType>
  <Unknown>0</Unknown><ClientID IDType="0" IDFlag="1">00001111-aaaa-2222-bbbb-
  3333cccc4444</ClientID><ClientVersion>5.00.0000.0000</ClientVersion>
  <NetBIOSName>P01PDP1.CONTOSO.COM</NetBIOSName>
  <CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
  </Machine></Identification><ReportDetails>
  <ReportContent>StateMessage</ReportContent><ReportType>Full</ReportType>
  <Date>20190107200618.000000+000</Date><Version>1.0</Version>
  <Format>1.1</Format></ReportDetails></ReportHeader>
  <ReportBody><StateMessage MessageTime="20190107200618.000000+000"
  SerialNumber="3"><Topic ID="P010000F" Type="902" IDType="0"/><State ID="1"
  Criticality="0"/><UserParameters Flags="0" Count="4"><Param>P010000F</Param>
  <Param>["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\</Param><Param>{11112222-bbbb-3333-
  cccc-4444dddd5555}</Param><Param></Param></UserParameters></StateMessage>
  </ReportBody>
  </Report>
  MP_RelayEndpoint 25912 (0x6538) Inv-Relay Task: Processing message body
  MP_RelayEndpoint 25912 (0x6538) Relay: Outbox dir:
  E:\ConfigMgr\inboxes\auth\statesys.box\incoming

Note that verbose and debug logging should be enabled on the MP to see above log entries
on the MP. Without verbose and debug logs, MP_Relay.log will just log "".

<!-- p.216 -->

Step 19: State System component on site server processes the
state message into the database
After the state message SMX file arrives in the StateSys.box\incoming directory, State System
component on the site server processes the message. All state messages are processed by
calling spProcessReport stored procedure. For pull DP state messages, spProcessReport calls
spProcessPullDPMessage which updates the PullDPResponse table with the state message

details.

  SMS_STATE_SYSTEM 23544 (0x5bf8) CMessageProcessor - Processing file:
  N_6RB4OA3A.SMX
  SMS_STATE_SYSTEM 23544 (0x5bf8) CMessageProcessor - the cmdline to DB exec
  dbo.spProcessStateReport N'?<Report><ReportHeader><Identification><Machine>
  <ClientInstalled>0</ClientInstalled><ClientType>1</ClientType>
  <Unknown>0</Unknown><ClientID IDType="0" IDFlag="1">00001111-aaaa-2222-bbbb-
  3333cccc4444</ClientID><ClientVersion>5.00.0000.0000</ClientVersion>
  <NetBIOSName>P01PDP1.CONTOSO.COM</NetBIOSName>
  <CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
  </Machine></Identification><ReportDetails>
  <ReportContent>StateMessage</ReportContent><ReportType>Full</ReportType>
  <Date>20190107200618.000000+000</Date><Version>1.0</Version>
  <Format>1.1</Format></ReportDetails></ReportHeader>~~ <ReportBody>
  <StateMessage MessageTime="20190107200618.000000+000" SerialNumber="3"><Topic
  ID="P010000F" Type="902" IDType="0"/><State ID="1" Criticality="0"/><UserParameters
  Flags="0" Count="4"><Param>P010000F</Param><Param>
  ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\</Param><Param>{11112222-bbbb-3333-
  cccc-4444dddd5555}</Param><Param></Param></UserParameters></StateMessage>
  </ReportBody>~~</Report>~~'

Note that StateSys.log does not log the message body unless verbose logging for StateSys.log
is enabled. To enable verbose logging for StateSys.log, see Enable verbose logging.

Here's the excerpt from spProcessReport stored procedure which processes the pull DP state
messages:

  SQL

<!-- p.217 -->

 else if @TopicType=902 -- Pull Distribution Point
         exec @Ret=spProcessPullDPMessage @SenderID=@SenderID,
 @MessageTime=@tmMessageTime, @PkgID=@TopicID, @PkgVersion=@MessageSerialNumber,
 @StateID=@StateID, @P1=@P1, @P2=@P2, @P3=@P3, @P4=@P4, @P5=@P5, @Error=@Error
 OUTPUT

Step 20: SMSDBMON notifies DistMgr to update the status
After PullDPResponse table is updated, SMSDBMON detects a change in the table and drops a
.PUL file for DistMgr to process, where the name of the file identifies the row that was
inserted/modified.

  SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) RCV: INSERT on
  PullDPResponse for PullDPResponse_UpdIns [72057594037928008 ][145014]
  SMS_DATABASE_NOTIFICATION_MONITOR 29748 (0x7434) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\incoming\72057594037928008.PUL [145014]

Step 21: DistMgr updates the distribution status
DistMgr processes the .PUL file, and retrieves the row from PullDPResponse table based on the
file name and updates the package status. After the response is processed, DistMgr deletes the
processed row from the PullDPResponse table.

  SMS_DISTRIBUTION_MANAGER 32876 (0x806c) SQL>>>select s.ID, s.PkgServer, s.SiteCode,
  p.StoredPkgVersion, s.Status, r.PkgVersion, r.ActionState, r.ActionData, p.PkgFlags,
  p.ShareType, CONVERT(VARCHAR(64), r.MessageTime, 127) AS MessageTime from
  PullDPResponse r join PkgStatus s on r.PkgStatusID = s.PKID AND r.PkgStatusID =
  72057594037928008 join SMSPackages p on s.ID = p.PkgID
  SMS_DISTRIBUTION_MANAGER 32876 (0x806c) ~Processing PullDP response P01 -
  ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\
  SMS_DISTRIBUTION_MANAGER 32876 (0x806c) Package P010000F, Version 3(3),
  ActionState 1, PkgStatus 0, ActionData =
  SMS_DISTRIBUTION_MANAGER 32876 (0x806c) ~Successfully updated the package server
  status for ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\ for package P010000F, Status 3
  SMS_DISTRIBUTION_MANAGER 32876 (0x806c) SQL>>>DELETE FROM PullDPResponse
  WHERE PkgStatusID = 72057594037928008 AND MessageTime = '2019-01-07T20:06:18'

<!-- p.218 -->

  SMS_DISTRIBUTION_MANAGER 32876 (0x806c) ~Successfully processed PullDP response
  file E:\ConfigMgr\inboxes\distmgr.box\INCOMING\72057594037928008.PUL

Step 22: Database replication replicates the status change to
other sites
After the package status is updated in the database, it is replicated to other sites via database
replication.

Update a package
When you update a package, the package content is resent to all of the distribution points that
the package was distributed to. This is done by incrementing Package Source version, and only
the content changes are sent to the DPs instead of sending all of the content again.

The following steps outline the flow of events that occur when a package is updated. In this
example, we will look at the package update operation for a package that was created at a
primary site and focus on process changes specific to the package update operation.

Step 1: The admin console executes the RefreshPkgSource
method against the SMS_Package WMI class in the SMS
Provider namespace
After the administrator updates the package from the console, the admin console calls the
RefreshPkgSource method of the SMS_Package class to update the package. SMSProv.log shows

the following:

  SMS Provider 4716 (0x126c) Context: SMSAppName=Configuration Manager Administrator
  console~
  SMS Provider 4716 (0x126c) ExecMethodAsync : SMS_Package.PackageID="
  <PackageID>"::RefreshPkgSource ~
  SMS Provider 4716 (0x126c) CExtProviderClassObject::DoExecuteMethod
  RefreshPkgSource~
  SMS Provider 4716 (0x126c) Auditing: User CONTOSO\Admin called an audited method of
  an instance of class SMS_Package.~

When this method is called, SMS Provider updates SMSPackages to set Action to 1(UPDATE) and
inserts a row in PkgNotification table.

<!-- p.219 -->

 SQL

 update SMSPackages set Source = N'\\PS1SITE\SOURCE\Packages\200MB_1',
 StoredPkgVersion = 1, UpdateMask = 32, UpdateMaskEx = 8388608, Action = 1 where
 PkgID = N'PackageID'
 insert PkgNotification (PkgID, Priority, Type, TimeKey) values (N'PackageID', 2, 1,
 GetDate())

Step 2: SMSDBMON notifies DistMgr to process the package
SMSDBMON detects a change in the PkgNotification table which causes it to drop a
<PackageID>.PKN file in DistMgr.box to instruct DistMgr to process the package:

  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) RCV: INSERT on PkgNotification
  for PkgNotify_Add [<PackageID>][1036610]
  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) SND: Dropped
  E:\ConfigMgr\inboxes\distmgr.box\<PackageID>.PKN [1036610]

Step 3: DistMgr wakes up to process the package after
receiving the PKN file
  1. The main DistMgr thread starts a package processing thread.

     The main DistMgr thread adds the package to the package processing queue and creates
     a package processing thread.

       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) Found package properties updated
       notification for package '<PackageID>'
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) Adding package '<PackageID>' to
       package processing queue.
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Currently using 0 out of 3 allowed
       package processing threads.
       SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Started package processing thread
       for package '<PackageID>', thread ID = 0x1690 (5776)

  2. The package processing thread creates a package snapshot, writes content to the content
     library and increments the package version.

     The package processing thread (thread ID 5776 in this case) starts processing the package
     and creates a package snapshot. After creating the package snapshot, this thread also

<!-- p.220 -->

writes the package content to the content library on the site server:

  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Processing package <PackageID>
  (SourceVersion:1;StoredVersion:1)
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Start updating the package
  <PackageID>...
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Taking package snapshot for package
  <PackageID> from source \\PS1SITE\SOURCE\Packages\200MB_1
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) The size of package <PackageID>,
  version 2 is 204800 KBytes
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Writing package definition for
  <PackageID>
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Successfully created RDC signatures
  for package <PackageID> version 2
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Creating hash for algorithm 32780
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) The hash for algorithm 32780 is
  <HashString>
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) The RDC signature hash for algorithm
  32780 is
  79A56464F7BAC44B3D183D5EFC1160E51F95A34FECA492AAD73BC73C8B6DBA38
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) STATMSG: ID=2376 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
  SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5776 GMTDATE=Tue May 17
  18:31:23.782 2016 ISTR0="PS100039" ISTR1="" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
  ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400 AVAL0="PS100039"
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~The source for package PS100039
  has changed or the package source needs to be refreshed
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Adding these contents to the
  package PS100039 version 2.
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~The Package Action is 1, the Update
  Mask is 32 and UpdateMaskEx is 0.
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Use drive E for storing the
  compressed package.
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Successfully created/updated the
  package PS100039.
  SMS_DISTRIBUTION_MANAGER 5776 (0x1690) STATMSG: ID=2311 SEV=I LEV=M
  SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"

<!-- p.221 -->

    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5776 GMTDATE=Tue May 17
    18:31:23.982 2016 ISTR0="PS100039" ISTR1="" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
    ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400 AVAL0="PS100039"

3. Package processing thread processes starts DP threads to process package actions then
  waits for them to exit.

  The package processing thread processes the package actions to update the package,
  which involves updating the package on all the DPs where this package is distributed.
  Since there are package actions to process, the package processing thread creates DP
  threads to perform these actions and waits for the DP threads to exit before moving on.

    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Start updating package PS100039 on
    server ["Display=\\PS1SITE.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1SITE.CONTOSO.COM\...
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Created DP processing thread 920
    for addition or update of package PS100039 on server
    ["Display=\\PS1SITE.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1SITE.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Start updating package PS100039 on
    server ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\...
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Created DP processing thread 2060
    for addition or update of package PS100039 on server
    ["Display=\\PS1SYS.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1SYS.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Start updating package PS100039 on
    server ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\...
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Created DP processing thread 6076
    for addition or update of package PS100039 on server
    ["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Start updating package PS100039 on
    server ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\...
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Created DP processing thread 5948
    for addition or update of package PS100039 on server

<!-- p.222 -->

    ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Waiting for all DP threads to
    complete for package PS100039 processing thread.

4. DP threads start and create PkgXferMgr jobs to transfer content to the DPs, then exit.

  DP threads start working on creating a PkgXferMgr job to update the package on the
  DPs. At this point there are four DP threads for four different DPs:

    SMS_DISTRIBUTION_MANAGER 5948 (0x173c) DP Thread: Attempting to add or
    update package PS100039 on DP ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\
    SMS_DISTRIBUTION_MANAGER 5948 (0x173c) ~Created package transfer job to send
    package PS100039 to distribution point
    ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\.
    SMS_DISTRIBUTION_MANAGER 5948 (0x173c) Performing cleanup prior to returning.
    SMS_DISTRIBUTION_MANAGER 5948 (0x173c) Cancelling network connection to
    \\PS1DP2.CONTOSO.COM\ADMIN$.

  When the DP thread creates a PkgXferMgr job, it does so by inserting a row in
  DistributionJobs table.

    SQL

    insert into DistributionJobs
    (DPID,PkgID,PackageVersion,State,CreationTime,Action)
    values(35,N'PS100039',2,0,N'2016/05/17 14:31:35',1)

5. (if applicable) Package processing thread creates a mini-job to send the compressed copy
  of the package to other sites.

  After all the DP threads finish working, the package processing thread creates a mini-job
  to send the compressed copy of the package to other sites, if applicable. This mini-job is
  processed by Scheduler to create a send request for Sender to transfer the compressed
  copy of the package to the destination site:

    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~All DP threads have completed for
    package PS100039 processing thread.

<!-- p.223 -->

    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Package PS100039 does not have a
    preferred sender.
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) STATMSG: ID=2333 SEV=I LEV=M
    SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
    SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5776 GMTDATE=Tue May 17
    18:31:44.977 2016 ISTR0="PS100039" ISTR1="PS2" ISTR2="" ISTR3="" ISTR4=""
    ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
    AVAL0="PS100039" ...
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Needs to send the compressed
    package for package PS100039 to site PS2
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Sending a copy of package
    PS100039 to site PS2
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Use drive E for storing the
    compressed package.
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Setting CMiniJob transfer root to
    E:\SMSPKG\PS100039.DLT.1.2
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Created minijob to send compressed
    copy of package PS100039 to site PS2. Transfer root = E:\SMSPKG\PS100039.DLT.1.2.
    ...
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Needs to send the compressed
    package for package PS100039 to site SS1
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Sending a copy of package
    PS100039 to site SS1
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Use drive E for storing the
    compressed package.
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Setting CMiniJob transfer root to
    E:\SMSPKG\PS100039.DLT.1.2
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Created minijob to send compressed
    copy of package PS100039 to site SS1. Transfer root = E:\SMSPKG\PS100039.DLT.1.2.

6. Package processing thread exits after processing the package:

    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) Package PS100039 is new or has
    changed, replicating to all applicable sites.
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690)
    ~CDistributionSrcSQL::UpdateAvailableVersion PackageID=PS100039, Version=2,
    Status=2301
    SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~StoredPkgVersion (2) of package

<!-- p.224 -->

        PS100039. StoredPkgVersion in database is 2.
        SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~SourceVersion (2) of package
        PS100039. SourceVersion in database is 2.
        SMS_DISTRIBUTION_MANAGER 5776 (0x1690) STATMSG: ID=2301 SEV=I LEV=M
        SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
        SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5776 GMTDATE=Tue May 17
        18:31:45.415 2016 ISTR0="Dummy2" ISTR1="PS100039" ISTR2="" ISTR3="" ISTR4=""
        ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=1 AID0=400
        AVAL0="PS100039"
        SMS_DISTRIBUTION_MANAGER 5776 (0x1690) ~Exiting package processing thread
        for package PS100039.

Step 4: SMSDBMON notifies PkgXferMgr to process the job
SMSDBMON detects a change in the DistributionJobs table and drops a PKN file in
PkgTransferMgr.box to instruct PkgXferMgr to process the job:

  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) RCV: UPDATE on DistributionJobs
  for DistributionJob_Creation [PS100039 ][1036623]
  SMS_DATABASE_NOTIFICATION_MONITOR 1792 (0x700) SND: Dropped
  E:\ConfigMgr\inboxes\PkgTransferMgr.box\PS100039.PKN [1036623]

Step 5: PkgXferMgr wakes up to process the job
For standard DPs, a sending thread copies the content to the DP, and the remaining process is
identical to the process described in step 6 of Distribute a package to standard DP.

For pull DPs, a pull DP sending thread sends the notification to the pull DP to perform content
download. Pull DP then downloads the content from the source DP, and the remaining process
is identical to the process described in step 6 of Distribute a package to pull DP.

Step 6: The package status changes are replicated to other
sites via DRS
After the package status is updated in the database, it is replicated to other sites via database
replication.

Redistribute a package

<!-- p.225 -->

When you redistribute a package to a DP, all of the package content files are re-copied to the
DP even if the content already exists in the content library on the DP.

The following steps outline the flow of events that occur when a package is redistributed to a
DP. In this example, the primary site server already has a compressed copy of the package. This
process is identical to the process outlined in Distribute a package to standard DP or Distribute
a package to pull DP, so here we only look at detailed log snippets for relevant changes.

Step 1: Administrator redistributes the package to the DP

Step 2: If Administrator redistributed the package from a
different primary site or the central administration site, DRS
replicates changes to the site in question

Step 3: SMSDBMON notifies DistMgr to process the package

Step 4: DistMgr wakes up to process the package
   1. The main DistMgr thread starts a package processing thread.

   2. The package processing thread creates DP threads to process package actions and waits
     for them to exit.

   3. The DP threads create a PkgXferMgr job to add the package to the DPs and then exits.

     The DP thread starts working on adding the package to the DP. DP threads do not copy
     the package content to the DP directly, but instead creates a job for Package Transfer
     Manager (PkgXferMgr) instructing it to copy the package content to the DP. The
     following log entries show the DP thread creating a PkgXferMgr job. After the job is
     created, the DP thread's work is done and the DP thread exits.

       SMS_DISTRIBUTION_MANAGER 3792 (0xed0) DP Thread: Attempting to add or
       update package <PackageID> on DP
       ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\
       SMS_DISTRIBUTION_MANAGER 3792 (0xed0) ~Created package transfer job to send
       package <PackageID> to distribution point
       ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
       ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\.
       SMS_DISTRIBUTION_MANAGER 3792 (0xed0) STATMSG: ID=2357 SEV=I LEV=M

<!-- p.226 -->

     SOURCE="SMS Server" COMP="SMS_DISTRIBUTION_MANAGER"
     SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=3792 GMTDATE=Mon May 16
     19:26:58.642 2016 ISTR0="<PackageID>" ISTR1="
     ["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
     ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\" ISTR2="" ISTR3="" ISTR4="" ISTR5=""
     ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2 AID0=400 AVAL0="
     <PackageID>" AID1=404 AVAL1="["Display=\\PS1DP2.CONTOSO.COM\"]MSWNET:
     ["SMS_SITE=PS1"]\\PS1DP2.CONTOSO.COM\"

   When the DP thread creates a PkgXferMgr job, it does so by inserting a row in the
   DistributionJobs table. For redistributing a package, Action is set to 2.

     SQL

     insert into DistributionJobs
     (DPID,PkgID,PackageVersion,State,CreationTime,Action)
     values(32,N'CS100026',1,0,N'2016/05/16 16:03:49',2)

 4. The package processing thread exits after all DP threads exit.

Step 5: SMSDBMON notifies PkgXferMgr to process the job

Step 6: PkgXferMgr wakes up to process the job
 1. The main PkgXferMgr thread creates a sending thread.

 2. The sending thread or pull DP sending thread processes the job.

   Standard DP:

   Sending thread starts copying the package contents to the DP. This process involves
   copying all the files in the package to the DP in the SMS_DP$ directory. Since the package
   was redistributed, PkgXferMgr shows that Redistribute is set to 1, which means that all
   the files will get re-copied to the DP even if they already exist in the content library on the
   DP.

     SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Sending thread starting for Job:
     583, package: <PackageID>, Version: 1, Priority: 2, server: PS1DP1.CONTOSO.COM,
     DPPriority: 200
     SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Sent status to the distribution
     manager for pkg <PackageID>, version 1, status 0 and distribution point

<!-- p.227 -->

["Display=\\PS1DP1.CONTOSO.COM\"]MSWNET:
["SMS_SITE=PS1"]\\PS1DP1.CONTOSO.COM\~
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Performing preactions package
<PackageID>, Distribution point PS1DP1.CONTOSO.COM
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Sending legacy content
<PackageID>.1 for package <PackageID>
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Redistribute=1, Related=
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Sending file
'\\PS1DP1.CONTOSO.COM\SMS_DP$\73E055438D4731F41DB6C3BCB90919F6000022
6B330C73942454A174D7E26533-<PackageID>.1.temp'
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) ~Sending Started
[E:\SCCMContentLib\FileLib\73E0\73E055438D4731F41DB6C3BCB90919F60000226B3
30C73942454A174D7E26533]
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) ~Attempt to write 983040 bytes
to
\\PS1DP1.CONTOSO.COM\SMS_DP$\73E055438D4731F41DB6C3BCB90919F6000022
6B330C73942454A174D7E26533-<PackageID>.1.temp at position 208732160
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) ~Wrote 983040 bytes to
\\PS1DP1.CONTOSO.COM\SMS_DP$\73E055438D4731F41DB6C3BCB90919F6000022
6B330C73942454A174D7E26533-<PackageID>.1.temp at position 208732160 in 344
ticks
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) ~Sending completed
[E:\SCCMContentLib\FileLib\73E0\73E055438D4731F41DB6C3BCB90919F60000226B3
30C73942454A174D7E26533]
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) Completed post-actions for
remote DP PS1DP1.CONTOSO.COM
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) ~Sending completed
successfully
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) ~Finished sending SWD
package <PackageID> version 1 to distribution point PS1DP1.CONTOSO.COM
SMS_PACKAGE_TRANSFER_MANAGER 5272 (0x1498) STATMSG: ID=8200 SEV=I
LEV=M SOURCE="SMS Server" COMP="SMS_PACKAGE_TRANSFER_MANAGER"
SYS=PS1SITE.CONTOSO.COM SITE=PS1 PID=5428 TID=5272 GMTDATE=Mon May 16
20:06:36.827 2016 ISTR0="<PackageID>" ISTR1="1" ISTR2="PS1DP1.CONTOSO.COM"
ISTR3="" ISTR4="" ISTR5="" ISTR6="" ISTR7="" ISTR8="" ISTR9="" NUMATTRS=2
AID0=400 AVAL0="<PackageID>" AID1=410 AVAL1="1"

<!-- p.228 -->

     Pull DP:

     Pull DP sending thread sends a notification to the pull DP to start downloading the
     content. Since the package was redistributed, the generated notification XML shows that
     Action is set to redist, which means that all the files will get re-downloaded by the pull
     DP even if they already exist in the content library on the pull DP.

     Here's how a sample query that generates the notification XML query looks like showing
     that the Action is redist since the content was redistributed:

       SQL

       SELECT [dbo].[fnGetPullDPXMLNotification]('P010000F', 3,
       'P01PDP1.CONTOSO.COM', 2, 'redist', 1, 'O:SYG:BAD:P(A;;FA;;;BA)
       (A;OICIIO;GA;;;BA)(A;;0x1200a9;;;BU)(A;OICIIO;GXGR;;;BU)(A;;FA;;;BA)
       (A;OICIIO;GA;;;BA)', 0, 32780,
       '3ED23B9869F7E10E19439F11341405FF76E22022E56468DCF211475899BD2914', '') AS
       Notification

     On receiving a notification for a redistribute action, PullDP.log will show that all content
     will get redownloaded even if some/all of the content may exist in the content library.

       PullDP 3676 (0xe5c) Content_3c9813ba-d7ab-4963-929c-36f90f479613.1:
       redistribute/redownload all files

     After this is done, the remaining process is similar to the process described in step 6 of
     Distribute a package to pull DP.

  3. The sending thread sends a status message to DistMgr.

Step 7: SMS DP Provider adds the content to the content
library

Step 8: DistMgr processes the status messages sent by
PkgXferMgr

Step 9: Package status changes are replicated to other sites
via DRS

Last updated on 03/30/2026

<!-- p.229 -->

Troubleshoot content distribution
This article discusses how to troubleshoot common content distribution issues.

Original product version: Configuration Manager current branch, Microsoft System Center
2012 Configuration Manager, Microsoft System Center 2012 R2 Configuration Manager

Sample problem
For this example, let's say that you distributed a package to a distribution point but the
package is in either a Failed or In Progress state for the DP.

   1. First, review DistMgr.log on the site (primary/secondary) where the DP resides.
      a. Look for ~Processing package entries in the log and identify the package processing
        thread for the package ID in question. Filter DistMgr.log for the thread ID you
        identified. Review step 4 in Distribute a package to standard DP to see log excerpts.
      b. Review the filtered log and check if a DP thread was created for the DP in question.
        Filter DistMgr.log for the thread ID to make this easier.
      c. Review the filtered log and check whether a PkgXferMgr job was created.

   2. Review PkgXferMgr.log on the site (primary/secondary) where the DP resides.
      a. Look for Found send request with ID entries in the log and identify the sending thread
        for the affected DP/package combination. Filter PkgXferMgr.log for the thread ID
        identified. Review step 6 in Distribute a package to standard DP to see log excerpts.
      b. Review the filtered log to see if the content was successfully transferred to the DP or if
        there was an error.

   3. For Standard DPs, PkgXferMgr copies the content file(s) to the DP, it instructs the DP WMI
     Provider to add the file to the content library by calling WMI methods. Review
     SMSDPProv.log on the DP to ensure that content was added to the content library.
     Review step 7 in Distribute a package to standard DP to see log excerpts.

     For pull DPs, PkgXferMgr notifies pull DP to initiate the content download. Review steps
     8-16 in Distribute a package to pull DP to understand the flow and review PullDP.log and
     DataTransferService.log to ensure content was downloaded successfully.

   4. For standard DPs, PkgXferMgr sends a status message to DistMgr. Review DistMgr.log to
     verify if the status message was processed successfully. Review step 8 in Distribute a

<!-- p.230 -->

   package to standard DP to see log excerpts.

   For pull DPs, pull DP sends a state message to indicate success. Review steps 16-22 in
   Distribute a package to pull DP to understand the flow and review the relevant logs to
   ensure state message is processed successfully.

 5. If multiple sites are involved, ensure that database replication is working and the
   database links between relevant sites are active.

Common DistMgr issues
   DistMgr.log shows the following entry for the package ID in question:

     Output

     SMS_DISTRIBUTION_MANAGER 2732 (0xaac) ~The contents for the package \
     <PackageID> hasn't arrived from site CS1 yet, will retry later.

   This usually happens temporarily while the content is in transit from one site to another.
   Review the Sender/Despooler logs to ensure that there are no issues with site
   communications. If you see errors during site to site communication (Scheduler ->
   Sender -> Despooler), focus on resolving those errors before troubleshooting the above
   message in DistMgr.log. Review Distribute a package to DP across sites to understand the
   log flow.

   If there are no errors, it may be necessary to force the parent site to resend the package
   to the affected site. See Resend compressed copy of a package to a site for more
   information.

   DistMgr.log may show that it's busy processing other packages and is using all the
   available threads for package processing.

     Output

     SMS_DISTRIBUTION_MANAGER 4824 (0x12d8) ~Currently using 3 out of 3 allowed
     package processing threads.

   If you see this, review the current package processing threads in DistMgr.log to see if
   they are stuck. You can also review the Package Processing Queue and Packages Being
   Processed registry values under the following registry key to see how many packages are
   currently in the Processing Queue:

<!-- p.231 -->

  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Components\SMS_DISTRIBUTION_MANAGER

  If the Packages Being Processed values do not change and are stuck over a long period
  of time, it is possible that DistMgr is hung/stuck. If this happens, capture a process dump
  of SMSExec.exe for review.

  If there are many packages in the queue but the queue is moving, it may be necessary to
  review and change the thread configuration.

  DistMgr.log does not process the incoming PKN files, and as a result packages are not
  being processed. This is resulting in a backlog of PKN files in the DistMgr inbox.

  PKN files are processed by the main DistMgr thread so in these cases it's helpful to
  identify the main DistMgr thread ID by looking for the SMS_EXECUTIVE started
  SMS_DISTRIBUTION_MANAGER log entry, then filter the DistMgr.log for the thread ID
  identified.

  In most cases, this issue occurs when the main DistMgr thread is making a WMI call to a
  remote DP but WMI on the DP is not responding, causing DistMgr to wait for it
  indefinitely. Filtering the DistMgr.log for the main DistMgr thread can provide clues
  about the DP it's trying to communicate with. Once identified, check if the DP is
  responding and WMI is functional on the DP. If necessary, reboot the DP to see if that
  helps.

  If the filtered DistMgr.log doesn't provide any clues, capture a process dump of
  SMSExec.exe while in problem state for review.

Common PkgXferMgr issues
  PkgXferMgr.log shows an error while adding files to the content library on the DP:

    Output

    SMS_PACKAGE_TRANSFER_MANAGER 5744 (0x1670) ~Sending completed
    [D:\SCCMContentLib\FileLib\B53B\B53B6F96ECC3FB2AF59D02C84A2D31434904BACF2F9C90
    D80107B6602860BCFD]
    SMS_PACKAGE_TRANSFER_MANAGER 5744 (0x1670) ~ExecStaticMethod failed (80041001)
    SMS_DistributionPoint, AddFile
    SMS_PACKAGE_TRANSFER_MANAGER 5744 (0x1670) CSendFileAction::AddFile failed;
    0x80041001
    SMS_PACKAGE_TRANSFER_MANAGER 5744 (0x1670) ~Deleting remote file
    \\DPNAME.CONTOSO.COM\SMS_DP$\Content_b034813c-bc60-4a16-b471-7a0dc3d9662b.1-
    B53B6F96ECC3FB2AF59D02C84A2D31434904BACF2F9C90D80107B6602860BCFD

<!-- p.232 -->

 SMS_PACKAGE_TRANSFER_MANAGER 5744 (0x1670) ~ Sending failed. Failure count =
 1, Restart time = 12/4/2014 6:14:27 AM Eastern Standard Time

After PkgXferMgr copies the content file to the DP, it executes WMI methods to instruct
the remote DP to add the file to the content library. If the remote DP fails to add the file
to the content library, you will see a generic WMI error (0x80041001 = WBEM_E_FAILED)
in PkgXferMgr.log.

When this happens, it is necessary to review SMSDPProv.log on the DP to identify the
reason that the DP failed to add the file to the content library. If you see File/Path not
found errors in SMSDPProv.log, you would need to capture a Process Monitor trace to
determine the reason for failure.

PkgXferMgr.log shows that only one connection is allowed to the DP:

 Output

 SMS_PACKAGE_TRANSFER_MANAGER 21216 (0x52e0) ~Address to DPNAME.CONTOSO.COM is
 currently under bandwidth control, therefore only one connection is allowed,
 returning send request to the pool.

or

 Output

 SMS_PACKAGE_TRANSFER_MANAGER 21216 (0x52e0) ~Address to DPNAME.CONTOSO.COM is
 currently in pulse mode, therefore only one connection is allowed.

If PkgXferMgr.log shows that 'only one connection is allowed' to the DP, it means that the
DP is configured for bandwidth throttling. If this is the case, PkgXferMgr can only use one
thread for the DP, and as a result only send one package to the DP at a time. See
Bandwidth control and threads for more information.

PkgXferMgr.log shows the address is closed:

 Output

 SMS_PACKAGE_TRANSFER_MANAGER 7156 (0x1BF4) Address is closed for priority 2
 jobs, stop
 sending[E:\SCCMContentLib\FileLib\2F08\2F0819F959E788CF843F42E9CA7B44E258B8B4B
 A37BB63902DB39ACF747BE7DA]
 SMS_PACKAGE_TRANSFER_MANAGER 7156 (0x1BF4) Deleting remote file
 \\DPNAME.CONTOSO.COM\SMS_DP$\<PackageID>.6-
 2F0819F959E788CF843F42E9CA7B44E258B8B4BA37BB63902DB39ACF747BE7DA
 SMS_PACKAGE_TRANSFER_MANAGER 7156 (0x1BF4) CSendFileAction::SendFiles failed;

<!-- p.233 -->

    0x80004005
    SMS_PACKAGE_TRANSFER_MANAGER 7156 (0x1BF4) Sending failed. Failure count = 1,
    Restart time = 3/15/2016 8:30:08 AM Mountain Daylight Time

  If you see this in the log, it means that the DP is under bandwidth control and the address
  to the DP closed while content transfer was in progress. In the example above, the DP
  schedule was configured for Allow high priority only during 8:00AM to 10:00AM. As a
  result, PkgXferMgr stopped sending content at 8:00AM and marked the package/DP in a
  failed state.

  PkgXferMgr.log shows multiple threads starting at the same time for the same job:

    Output

    SMS_PACKAGE_TRANSFER_MANAGER 8360 (0x20a8) Sending thread starting for Job:
    12771, package: <PackageID>, Version: 8, Priority: 2, server:
    DPNAME.CONTOSO.COM, DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 10752 (0x2a00) Sending thread starting for Job:
    12771, package: <PackageID>, Version: 8, Priority: 2, server:
    DPNAME.CONTOSO.COM, DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 12208 (0x2fb0) Sending thread starting for Job:
    12771, package: <PackageID>, Version: 8, Priority: 2, server:
    DPNAME.CONTOSO.COM, DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 4244 (0x1094) Sending thread starting for Job:
    12771, package: <PackageID>, Version: 8, Priority: 2, server:
    DPNAME.CONTOSO.COM, DPPriority: 200
    SMS_PACKAGE_TRANSFER_MANAGER 8348 (0x209c) Sending thread starting for Job:
    12771, package: <PackageID>, Version: 8, Priority: 2, server:
    DPNAME.CONTOSO.COM, DPPriority: 200

  Typically, PkgXferMgr uses one thread for a job, but if it uses multiple threads for the
  same job, the content transfer may start failing because of error 0x80070020
  (ERROR_SHARING_VIOLATION). This happens if the site server and the site database
  servers are in different time zones. The solution here is to ensure that the site server and
  site database servers have the same time zone set.

Common pull DP issues
  PkgXferMgr.log shows that the Pull DP is at capacity and no more jobs are sent to the
  pull DP:

    Output

    SMS_PACKAGE_TRANSFER_MANAGER 4712 (0x1268) PullDP
    ["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
    ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\ has reached maximum capacity 50

<!-- p.234 -->

  SMS_PACKAGE_TRANSFER_MANAGER 4712 (0x1268) ~ PullDP has no capacity. Restart
  time = 1/10/2019 1:16:33 PM Eastern Standard Time

PkgXferMgr runs the following query to check how many jobs are currently in an
unfinished state on the pull DP. If the query returns more than 50 jobs, it will not send any
more jobs to the pull DP.

  SQL

  SELECT COUNT(*) FROM DistributionJobs job
  JOIN DistributionPoints dp ON dp.DPID=job.DPID AND
  dp.NALPath='["Display=\\P01PDP1.CONTOSO.COM\"]MSWNET:
  ["SMS_SITE=P01"]\\P01PDP1.CONTOSO.COM\'
  WHERE job.State in (2, 3, 4) AND (job.Action<>5) AND (ISNULL(job.SendAction,
  '') <> '')

These jobs are removed from the DistributionJobs table when pull DP sends a Success
state message or when the status polling stops (based on configured values). To see the
jobs on the pull DP, you can use wbemtest or WMI Explorer        to review the instance
count for SMS_PullDPNotification class. You can also review the instances of
ROOT\SCCMDP:SMS_PullDPState WMI class on the pull DP to identify packages that are in a

Failed state and review PullDP.log as well as DataTransferService.log to investigate the
failures.

SignatureDownload job on pull DP fails with HTTP 404 error.

  Created SignatureDownload DTS job {JOBID} for package C010000D.28, content id
  ContentID. JobState = NotStarted
  DTS error message received for C010000D.28, content job {JOBID}, 0x80070002 : BITS
  error: 'HTTP status 404: The requested URL does not exist on the server.

This is a known issue because the signature files are not present on a Source DP that is
colocated on a site server. This issue only occurs when the distribution action is not redist.

To work around this issue, use one of the following methods:
   Redistribute the package (redistributing the package does not require downloading
   signatures since full content is downloaded).
   Configure the pull DP to use a source DP that is not colocated on the site server.

DataTransferService.log shows 0x800706D9 when trying to download content from the
source DP:

<!-- p.235 -->

 Output

 DataTransferService 4864 (0x1300) CDTSJob::HandleErrors: DTS Job '{5285F8B3-
 C426-4882-85F2-AD5331DD4179}' BITS Job '{D53BA625-24AA-41FA-A357-
 6EB1B7D7E701}' under user 'S-1-5-18' OldErrorCount 29 NewErrorCount 30
 ErrorCode

0x800706D9 means that there are no more endpoints available from the endpoint
mapper. This issue may occur due to RPC port allocation failures caused by firewall. It can
also occur when Windows Firewall service is disabled.

Check to see if there is a firewall between the site server and the affected server and find
out if RPC ports are open. You can also capture a Network Trace       (from the pull DP as
well as the source DP server) while reproducing the error for review.

Pull DP shows that it has a large number of jobs but the jobs are not getting processed.

In some instances (normally after installation of a new pull DP when all content is sent to
the pull DP), too many job failures on the pull DP can end up stalled processing of the
jobs. Although most of these issues are fixed in the recent releases of the product
(Configuration Manager version 1810), some environmental factors can result in pull DP
not processing jobs. When this happens, you would likely see thousands of DTS jobs in
ROOT\ccm\DataTransferService:CCM_DTS_JobEx WMI class and ~50 (or more) BITS jobs in

Failed state. In this scenario, it can be beneficial to remove all the job-specific items from
WMI on the pull DP and distribute the content again to the pull DP in a controlled
manner and investigate failures.

To remove all the job-specific items from WMI on the Pull DP, you can use the below
PowerShell script (review the script comments for help):

Reset-PullDPState.ps1

 PowerShell

 <#

 .SYNOPSIS
 Resets the state of the Pull DP and deletes data from various WMI classes
 related to Pull DP. You need to run this script as Administrator.

 .DESCRIPTION
 This script deletes the data from following WMI classes:
 - CCM_DTS_JobEx
 - CCM_DTS_JobItemEx
 - SMS_PullDPState

<!-- p.236 -->

- SMS_PullDPContentState
- SMS_PullDPNotification (optional)

The script also checks and reports the count of BITS Jobs.

.PARAMETER ComputerName
(Optional) Name of the Pull DP. You can leave this blank for local machine.

.PARAMETER DeletePullDPNotifications
(Optional) Use this switch if you want to delete the job notifications from
SMS_PullDPNotification class.

.PARAMETER KeepBITSJobs
(Optional) Use this switch if you don't want the script to delete ALL BITS
Jobs. If this switch is not used, ALL BITS jobs are deleted (even the ones
that are not created by ConfigMgr)

.PARAMETER NotifyPullDP
(Optional) Use this switch if you want the script to execute NotifyPullDP
method against SMS_DistributionPoint class. This is only useful when there
aren't a lot of notifications in WMI and -DeletePullDPNotifications switch was
not used.

.PARAMETER WhatIf
(Optional) Use this switch to see how many instances will be deleted.

.EXAMPLE
Reset-PullDPState -WhatIf
This command checks how many Pull PD jobs will get deleted when running the
script

.EXAMPLE
Reset-PullDPState
This command resets the Pull DP related WMI classes except the Pull DP job
Notification XML's

.EXAMPLE
Reset-PullDPState -DeletePullDPNotifications
This command resets the Pull DP related WMI classes along with the Pull DP job
Notification XML's. If you do this, you would need to distribute/redistribute
these packages to the Pull DP again.

.NOTES
07/28/2016 - Version 1.0 - Initial Version of the script
01/09/2019 - Version 2.0 - Added batch size for instance removal to prevent
WMI Quota issues. Also added removal of BITS jobs (can be disabled by using -
KeepBITSJobs switch) and restart of CcmExec service.

#>

[CmdletBinding()]
Param(
  [Parameter(Mandatory=$false)]
   [string]$ComputerName = $env:COMPUTERNAME,

<!-- p.237 -->

    [Parameter(Mandatory=$false)]
    [switch]$DeletePullDPNotifications,

    [Parameter(Mandatory=$false)]
    [switch]$KeepBITSJobs,

    [Parameter(Mandatory=$false)]
    [switch]$NotifyPullDP,

    [Parameter(Mandatory=$false)]
    [switch]$WhatIf
)

$LogFile = Join-Path (Split-Path $SCRIPT:MyInvocation.MyCommand.Path -Parent)
"Reset-PullDPState.log"
$ErrorActionPreference = "SilentlyContinue"

Function Write-Log {
    Param(
      [string] $text,
      [switch] $NoWriteHost,
      [switch] $IsErrorMessage,
      [switch] $IsWarning,
      [switch] $WhatIfMode
    )

     $timestamp = Get-Date -Format "MM-dd-yyyy HH:mm:ss"
     "$timestamp $text" | Out-File -FilePath $LogFile -Append

     if ($WhatIfMode) {
         Write-Host $text -ForegroundColor Yellow
         return
     }

     if (-not $NoWriteHost) {
         if ($IsErrorMessage) {
             Write-Host $text -ForegroundColor Red
         }
         elseif ($IsWarning) {
             Write-Host $text -ForegroundColor Yellow
         }
         else {
             Write-Host $text -ForegroundColor Cyan
         }
     }
}

Function Delete-WmiInstances {
    Param(
        [string] $Namespace,
        [string] $ClassName,
        [string] $Filter = $null,
        [string] $Property1,
        [string] $Property2 = "",
        [string] $Property3 = "",

<!-- p.238 -->

        [int] $BatchSize = 10000
    )

    $success = 0
    $totalfailed = 0
    $counter = 0
    $total = 0

    Write-Host ""
    Write-Log "$ClassName - Connecting to WMI Class on $ComputerName"

    do {

        if ($Filter -eq $null) {
            $Instances = Get-WmiObject -ComputerName $ComputerName -Namespace
$Namespace -Class $ClassName -ErrorVariable WmiError -ErrorAction
SilentlyContinue | Select -First $BatchSize
        }
        else {
            $Instances = Get-WmiObject -ComputerName $ComputerName -Namespace
$Namespace -Class $ClassName -Filter $Filter -ErrorVariable WmiError -
ErrorAction SilentlyContinue | Select -First $BatchSize
        }

        if ($WmiError.Count -ne 0) {
            Write-Log "    Failed to connect. Error:
$($WmiError[0].Exception.Message)" -IsErrorMessage
            $WmiError.Clear()
            return
        }

        $currentfailed = 0
        $current = ($Instances | Measure-Object).Count
        if ($current -gt 0) {$script:serviceRestartRequired = $true}
        if ($WhatIf) { break }

        if ($current -ne $null -and $current -gt 0) {
            Write-Log "    Found $total total instances (Batch size
$BatchSize)"

              foreach($instance in $Instances) {

                 $instanceText = "$Property1 $($instance.$Property1)"

                 if ($Property2 -ne "") {
                     $instanceText += ", $Property2 $($instance.$Property2)"
                 }

                 if ($Property3 -ne "") {
                     $instanceText += ", $Property3 $($instance.$Property3)"
                 }

                 Write-Log "     Deleting instance for $instanceText" -
NoWriteHost
                 $counter += 1

<!-- p.239 -->

                $percentComplete = "{0:N2}" -f (($counter/$total) * 100)
                Write-Progress -Activity "Deleting instances from $ClassName"
-Status "Deleting instance #$counter/$total - $instanceText" -PercentComplete
$percentComplete -CurrentOperation "$($percentComplete)% complete"

                Remove-WmiObject -InputObject $instance -ErrorVariable
DeleteError -ErrorAction SilentlyContinue
                if ($DeleteError.Count -ne 0) {
                    Write-Log "    Failed to delete instance. Error:
$($DeleteError[0].Exception.Message)" -NoWriteHost -IsErrorMessage
                    $DeleteError.Clear()
                    $currentfailed += 1
                }
                else {
                    $success += 1
                }
            }

            $totalfailed += $currentfailed

            if ($currentfailed -eq $current) {
                # Every instance in current batch failed. Break to avoid
infinite while loop
                break
            }
        }

    } while (($Instances | Measure-Object).Count -ne 0)

    if ($WhatIf) {
        if ($total -eq $BatchSize) {
            Write-Log "    (What-If Mode) Found more than $BatchSize instances
which will be deleted" -WhatIfMode
        }
        else {
            Write-Log "    (What-If Mode) $total instances will be deleted" -
WhatIfMode
        }
    }
    else {
        if ($total -gt 0) {
            # $totalfailed is likely not the accurate count here as it could
include duplicate failures due to batching
            Write-Log "    Deleted $success instances. Failed to delete
$totalfailed instances."
        }
        else {
            Write-Log "    Found 0 instances."
        }
    }
}

Function Check-BITSJobs {

<!-- p.240 -->

    $DisplayName = "BITS Jobs"

    Write-Host ""
    Write-Log "$DisplayName - Gettting jobs on $ComputerName"
    Import-Module BitsTransfer
    $Instances = Get-BitsTransfer -AllUsers -Verbose -ErrorVariable BitsError
-ErrorAction SilentlyContinue | Where-Object {$_.DisplayName -eq 'CCMDTS Job'}

    if ($BitsError.Count -ne 0) {
        Write-Log "    $DisplayName - Failed to get jobs. Error:
$($BitsError[0].Exception.Message)" -IsErrorMessage
        $BitsError.Clear()
    }
    else {
        $total = ($Instances | Measure-Object).Count
        Write-Log "    $DisplayName - Found $total jobs"

        if ($KeepBITSJobs) {
            Write-Log "     BITS Jobs will not be removed because KeepBITSJobs
is true." -WhatIfMode
        }
        else {
            if ($WhatIf) {
                Write-Log "     (What-If Mode) ALL BITS jobs will be removed
since KeepBITSJobs is NOT specified." -WhatIfMode
            }
            else {
                if ($total -gt 0) {
                    Write-Log "     Removing ALL jobs since KeepBITSJobs is NOT
specified."
                    Remove-BITSJobs
                }
                else {
                    Write-Log "     There are no jobs to delete."
                }
            }
        }
    }
}

Function Remove-BITSJobs {

    try {
        Stop-Service BITS
        Rename-Item "$($env:ALLUSERSPROFILE)\Microsoft\Network\Downloader" -
NewName "Downloader.OLD.$([Guid]::NewGuid().Guid.Substring(0,8))"
        Start-Service BITS
        $script:serviceRestartRequired = $true
        Write-Log "    Removed ALL BITS Jobs successfully."
    } catch {
        Write-Log "    Failed to delete the BITS jobs."
        Write-Log "    If necessary, run 'bitsadmin /reset /allusers' command
under SYSTEM account (using psexec.exe) to delete the BITS Jobs."
        Write-Log "    Additionally, you can delete these jobs by stopping
BITS service, renaming %allusersprofile%\Microsoft\Network\Downloader folder,
