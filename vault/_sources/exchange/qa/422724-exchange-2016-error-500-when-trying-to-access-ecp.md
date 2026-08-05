---
title: "Exchange 2016 - Error 500 when trying to access ECP as Domain Admin"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/422724/exchange-2016-error-500-when-trying-to-access-ecp
question_id: 422724
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 - Error 500 when trying to access ECP as Domain Admin

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/422724/exchange-2016-error-500-when-trying-to-access-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

We are currently migrating from a single Exchange 2010 to a 2 016 DAG composed of 2 server.    

All was working fine, we were about to migrate users in bulk, then ECP on one of our 2016 server stop working.    

Outlook connection,OWA, Autodiscover and active sync are ok. It's only ECP access.    

At the beginning it was an Access Denied, even with user member of rightfull Groups    

We did the following :    

-Check that computer Object have no ms-Exch-EPI-Token-Serialization right    

https://learn.microsoft.com/fr-fr/exchange/troubleshoot/client-connectivity/error-occur-ems-eac-owa    

-Change certificate for Back End WebSite in IIS with a valide One    

https://letsexchange.blogspot.com/2017/05/an-error-occurred-while-using-ssl.html?m=0    

-Verify authentication method for owa and ECP and switch from true to false to true + iis reset    

-Recycle Apppool    

-Test with internal/external URL, localhost, IP    

-Delete/recreate VirtualDirectory for front and back end    

-Delete ExchCanarydata0 in ADSI Edit    

https://ril3y.wordpress.com/2014/03/25/exchange-2013-owa-and-ecp-logins-fail-with-500-error/    

-Verified if there was a double entry in RemoteDomains.xaml     

https://moh10ly.wordpress.com/2015/08/03/exchange-2013-ecp-admin-panel-page-fails-with-500-unexpected-error-after-running-hybrid-configuration-wizard-with-office-365/    

-----    

None f this worked...    

We are thinking of restoring from the last backup when all was ok 2 days ago or doing a fresh install. But I'd like to know what's happenning...    

In the Event log we have now the following event:    

Niveau	Date et heure	Source	ID de l’événement	Catégorie de la tâche    

Erreur	04.06.2021 15:37:59	MSExchange Control Panel	4	General	"Current user: 'domain/OU/user'    

Request for URL 'https://Exch2016:444/ecp/default.aspx?exchclientver=15(https://Exch2016.domain/ecp/?exchclientver=15)' failed with the following error:    

System.Web.HttpUnhandledException (0x80004005): Une exception de type 'System.Web.HttpUnhandledException' a été levée. ---> Microsoft.Exchange.Management.ControlPanel.CannotAccessOptionsWithBEParamOrCookieException: Un problème est survenu lors de l'ouverture des options dans Outlook Web App. Cliquez sur Se déconnecter ci-dessous, puis reconnectez-vous aux options dans Outlook Web App. Si cela ne fonctionne pas, déconnectez-vous, supprimez des cookies du navigateur et reconnectez-vous.    

   à Microsoft.Exchange.Management.ControlPanel.HttpContextExtensions.ThrowIfViewOptionsWithBEParam(HttpContext context, FeatureSet featureSet)    

   à Microsoft.Exchange.Management.ControlPanel._Default.InitFeatureSetAndStartPage()    

   à Microsoft.Exchange.Management.ControlPanel._Default.OnLoad(EventArgs e)    

   à System.Web.UI.Control.LoadRecursive()    

   à System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

   à System.Web.UI.Page.HandleError(Exception e)    

   à System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

   à System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

   à System.Web.UI.Page.ProcessRequest()    

   à System.Web.UI.Page.ProcessRequest(HttpContext context)    

   à System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()    

   à System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)    

   à System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)    

   à System.Web.UI.Page.HandleError(Exception e)    

   à System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

   à System.Web.UI.Page.ProcessRequest(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

   à System.Web.UI.Page.ProcessRequest()    

   à System.Web.UI.Page.ProcessRequest(HttpContext context)    

   à System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()    

   à System.Web.HttpApplication.ExecuteStepImpl(IExecutionStep step)    

   à System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)    

Microsoft.Exchange.Management.ControlPanel.CannotAccessOptionsWithBEParamOrCookieException: Un problème est survenu lors de l'ouverture des options dans Outlook Web App. Cliquez sur Se déconnecter ci-dessous, puis reconnectez-vous aux options dans Outlook Web App. Si cela ne fonctionne pas, déconnectez-vous, supprimez des cookies du navigateur et reconnectez-vous.    

   à Microsoft.Exchange.Management.ControlPanel.HttpContextExtensions.ThrowIfViewOptionsWithBEParam(HttpContext context, FeatureSet featureSet)    

   à Microsoft.Exchange.Management.ControlPanel._Default.InitFeatureSetAndStartPage()    

   à Microsoft.Exchange.Management.ControlPanel._Default.OnLoad(EventArgs e)    

   à System.Web.UI.Control.LoadRecursive()    

   à System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

   à Microsoft.Exchange.Management.ControlPanel.HttpContextExtensions.ThrowIfViewOptionsWithBEParam(HttpContext context, FeatureSet featureSet)    

   à Microsoft.Exchange.Management.ControlPanel._Default.InitFeatureSetAndStartPage()    

   à Microsoft.Exchange.Management.ControlPanel._Default.OnLoad(EventArgs e)    

   à System.Web.UI.Control.LoadRecursive()    

   à System.Web.UI.Page.ProcessRequestMain(Boolean includeStagesBeforeAsyncPoint, Boolean includeStagesAfterAsyncPoint)    

Flight info: Features:[[Global.DistributedKeyManagement, False],[Global.FrontdoorDefaultURL, False],[Global.GlobalCriminalCompliance, False],[Global.MultiTenancy, False],[Global.PopulateGroupMasterSid, False],[Global.WindowsLiveID, False],[Eac.AllowMailboxArchiveOnlyMigration, True],[Eac.AllowRemoteOnboardingMovesOnly, False],[Eac.AllowSender, False],[Eac.AntiSpamBulkThresholdUI, False],[Eac.AntispamTenantAllowBlockLists, False],[Eac.AtpPolicyForO365, False],[Eac.BulkPermissionAddRemove, True],[Eac.CaseHoldQuery, False],[Eac.CaseHoldSearch, False],[Eac.CmdletLogging, True],[Eac.ComplianceAllPublicFolderSearch, False],[Eac.ComplianceAllPublicFolderSearchForHold, False],[Eac.ComplianceCase, False],[Eac.ComplianceCaseClosing, False],[Eac.ComplianceCaseSources, False],[Eac.ComplianceExportIndividualMessageFormat, False],[Eac.ComplianceExportZipFormat, False],[Eac.ComplianceMnc, False],[Eac.ComplianceNewValidator, False],[Eac.ComplianceSearchRefiners, False],[Eac.ComplianceSearchStatistics, False],[Eac.ConditionCards, False],[Eac.ConditionCardsForCaseHoldQuery, False],[Eac.ConvertMailboxUI, False],[Eac.CrossPremiseMigration, False],[Eac.CustomizableMaxMsgSizeUI, True],[Eac.CutomizableSenderAuthenticationInNewDistributionGroup, False],[Eac.DefensibilityReport, False],[Eac.DeleteMessage, False],[Eac.DeleteQuarantineMessage, False],[Eac.DevicePolicyMgmtUI, False],[Eac.DiscontinueSafetenantConnectorUI, False],[Eac.DiscoveryDocIdHint, False],[Eac.DiscoveryMultiHoldSearch, False],[Eac.DiscoveryMultiQuerySearch, False],[Eac.DiscoveryMultiQueryV2Export, False],[Eac.DiscoveryPFSearch, True],[Eac.DiscoverySearchStats, False],[Eac.DiscoveryV1Export, True],[Eac.DistributionToUnifiedGroupMigrationEac, False],[Eac.DKIMSigningConfigUI, False],[Eac.DLPBlockForUnifiedCompliance, False],[Eac.DlpFingerprint, False],[Eac.DlpPolicyDetailsAndError, False],[Eac.DLPUnifiedCompliancePreview, False],[Eac.DLPWarnForUnifiedComplianceAvailability, False],[Eac.EACClientAccessRulesEnabled, False],[Eac.EacConciergeControl, False],[Eac.EacFeedbackControl, False],[Eac.EacPswsProxy, False],[Eac.EDiscoveryEacDecommisionExemption, True],[Eac.EdiscoveryExportPaging, False],[Eac.EdiscoveryExportV2AnalyzeWithZoom, False],[Eac.EdiscoveryExportV2ClientExportToolLiteEngine, False],[Eac.EdiscoveryExportV2General, False],[Eac.EdiscoveryHold, False],[Eac.EdiscoveryPreviewSearchUI, True],[Eac.EdiscoverySearchUI, False],[Eac.EDiscoverySPOMultiGEOEnabled, False],[Eac.EnableForInternalSendersInUI, False],[Eac.ExportDedupe, False],[Eac.ExportReportOnly, False],[Eac.FileFilter, False],[Eac.GeminiShell, False],[Eac.GrantSendOnBehalfToForSharedMailbox, False],[Eac.GroupsBulkUpgradeWizard, False],[Eac.GroupsInOutlookPromotionBanner, False],[Eac.HoldForModernGroups, False],[Eac.InactiveMailboxForCaseHold, False],[Eac.InactiveMailboxPickerEmailAddress, True],[Eac.InactiveMailboxSearch, False],[Eac.IsDedicatedTenant, False],[Eac.ManageMailboxAuditing, False],[Eac.ModernGroupCreateOnBehalfOf, False],[Eac.ModernGroupDelegatedUserSupport, False],[Eac.ModernGroupDomainSelectionSupport, False],[Eac.ModernGroupEnableDeliveryManagement, False],[Eac.ModernGroupManagement, False],[Eac.ModernGroupMoreEditOptions, False],[Eac.ModernGroupNonMailboxUserSupport, False],[Eac.ModernGroups, False],[Eac.ModernGroupsAllowAddingGuestInO365GroupMembership, False],[Eac.ModernGroupsAllowCreationByNonAADAdmin, False],[Eac.ModernGroupsPromotion, False],[Eac.ModernGroupsPromotionV2, False],[Eac.ModernGroupsSendOnBehalfOf, False],[Eac.ModernGroupsSkipVerifyOwnerLimit, True],[Eac.NewAuditingOptInUIOptIn, True],[Eac.NewAuditingReportUIOptIn, True],[Eac.NonExchangeWorkloadsUI, False],[Eac.Office365DIcon, False],[Eac.OrgIdADSeverSettings, False],[Eac.PreviewQuarantineMessage, False],[Eac.PreviewQuarantineMessageAdvanced, False],[Eac.PreviewSnapshotSearchUI, False],[Eac.PromoteProtectionCenter, False],[Eac.ProtectionCenterForceRedirect, False],[Eac.ProtectionCenterOptIn, False],[Eac.ProtectionCenterOptOut, False],[Eac.PublicFolderHoldManagement, False],[Eac.QuarantineMalware, False],[Eac.RemoteDomain, False],[Eac.RestoreUnifiedGroup, False],[Eac.RetentionPoliciesEacDecommisionExemption, True],[Eac.RetentionTagsEacDecommisionExemption, True],[Eac.RmsDecode, False],[Eac.SafeAttachments, False],[Eac.SafeAttachmentsDynamicDelivery, True],[Eac.SafelinkConvergedView, True],[Eac.SafeLinks, False],[Eac.SafeLinksBlockListFlexibleUrlPattern, False],[Eac.SafeLinksDoNotRewriteUrlByFlexibleUrlPattern, False],[Eac.SafeLinksScanUrls, True],[Eac.SelectivelyExportItemsById, False],[Eac.SetAtpPolicyForO365CmdletWACOption, False],[Eac.ShowExternalStorageWarningInGCC, False],[Eac.SingleFolderExport, False],[Eac.SPOPickerSearchAllTenantContent, False],[Eac.SupervisoryReview, False],[Eac.SupportAdfsIdentityInEcpProxy, False],[Eac.TestTransferToE164Extension, False],[Eac.ToggleABQWarning, False],[Eac.UCCAlertsReportingUI, False],[Eac.UCCAuditReports, False],[Eac.UCCIngestionUI, False],[Eac.UCCPermissions, False],[Eac.UCCTestProbeUI, False],[Eac.UnifiedAuditPolicy, False],[Eac.UnifiedAuditReportUI, False],[Eac.UnifiedComplianceCenter, False],[Eac.UnifiedDlpGA, False],[Eac.UnifiedPolicy, True],[Eac.UnifiedRetention, False],[Eac.UnlistedServices, True],[Eac.UseDoNotRewriteUrlsParamInSafeLinksPolicyCmdletAndUI, False],[Eac.WorkloadUIInUrlTraceTab, False],],  Flights:[],  Constraints:[[LOC, FR-CH],[MACHINE, EXCH2016],[MODE, ENTERPRISE],[PROCESS, MSEXCHANGEECPAPPPOOL],[USER.USER^A, TRUE],[USER.USER^ADOMAIN, TRUE],[USERTYPE, BUSINESS],], IsGlobalSnapshot: False"    

Any help would be appreciated ;)    

THanks a lot in advance,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-09*

Hi All,    

I tried replacing RemoteDomains.xaml with the file from the valid server and same issue.    

I have a 500 error when trying to access ecp.    

@Anonymous   : What do you mean exactly with same permissions ? In fact if it was an AD permissions issue I would not be able to access ecp on the valid Exchange no ?    

I just re-checked  VD URLs, all are ok and identical.    

Certificate on default Web Site and Backend are the same (a wildcard one), and same configuration on valid exchange...    

We are running out of ideas....    

THanks for the help

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Hi,  

Thanks for the answer Lou.  

Nop it's not the only user, we have same issue with all admins account. A standard user can access its own ecp mailbox. That's the weird thing.  

Yes we tried resetting both owa and ECP virtual directories. I will try replacing the RemoteDomains.xaml on the faulty servers with the healthy one but I didn't see any "visual mistake" in it.  

We also tried to repace the IIS config with a backup/restore from the healthy one, but we quickly rollback on a snapshot after many errors.  

We tried on localhost/ecp, and same issue. We are testing from different computers, different browsers,different users and on privacy signet, so I think we can exclude any form of cookie or cache :D.  

I give a try on replacing the xaml file and keep you inform.  

Regards,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-07*

Hi @colin szajkowski   ,    

Good day!    

Is this the only user and only EAC with this error? Well I mean if the other server EAC has the same error and if you tried logging in with other accounts?    

I'm a little confused with the error message:     

Microsoft.Exchange.Management.ControlPanel.CannotAccessOptionsWithBEParamOrCookieException: There was a problem opening options in Outlook Web App. Click Sign Out below, then sign back in to options in Outlook Web App. If that doesn't work, log out, delete browser cookies and log back in.    

I would think the error is between OWA and ECP, some data exchanging or sharing error. Please try logging out and deleting the cookies and re-login.    

Have you reset both OWA and ECP virtual directory? And for the RemoteDomains.xaml, I think you could replace it with a health server's.    

And also try using the Https://localhost/ecp to login and see if that helps.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
