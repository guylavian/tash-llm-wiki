---
title: "ADFS error - Need help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1077963/adfs-error-need-help
question_id: 1077963
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS error - Need help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1077963/adfs-error-need-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I get below error when I test login to application. Can someone give some visibility please.

SAML Login response received  

SAML failed to login  

Status code is urn:oasis:names:tc:SAML:2.0:status:Requester. When it is supposed to be urn:oasis:names:tc:SAML:2.0:status:Success  

Ensure that the 'AuthContextClass' related properties are set correctly.

SSO Test Connection Summary:

11/06/22 22:50:51 (939) sysparm_form_fields: sysparm_ck=2df87d09970f1110c4a735dfe153af7ff985ef16d4f700114aa9eb5196d165b187148ee1&sys_base_uri=https%3A%2F%2Fdev130499.service-now.com%2F&sys_target=saml2_update1_properties&sys_uniqueName=sys_id&sys_uniqueValue=dc33b505970f1110c4a735dfe153af57&sys_displayValue=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&sys_titleValue=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&onLoad_sys_updated_on=2022-11-07+06%3A44%3A00&sys_row=0&sys_modCount=7&sys_action=none&sysparm_collection=&sysparm_collectionID=&sysparm_collection_key=&sysparm_collection_related_field=&sysparm_collection_relationship=&sysparm_redirect_url=&sysparm_goto_url=&isFormPage=true&sysparm_referring_url=&sysparm_view=&sysparm_changeset=&sysparm_template_editable=&sysparm_record_row=2&sysparm_record_list=ORDERBYname&sysparm_record_rows=3&sysparm_record_target=sso_properties&sysparm_modify_check=true&sysparm_action_template=&sysparm_link_collection=&sysparm_pop_onLoad=&sysparm_nameofstack=&sysparm_transaction_scope=&sysparm_transaction_update_set=&sysparm_record_scope=&sysparm_ck=2df87d09970f1110c4a735dfe153af7ff985ef16d4f700114aa9eb5196d165b187148ee1&sys_original.saml2_update1_properties.name=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&saml2_update1_properties.name=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&sys_original.saml2_update1_properties.default=false&saml2_update1_properties.default=false&sys_original.saml2_update1_properties.active=false&saml2_update1_properties.active=false&sys_original.saml2_update1_properties.is_primary=false&saml2_update1_properties.is_primary=false&sys_original.saml2_update1_properties.idp=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&saml2_update1_properties.idp=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&sys_original.saml2_update1_properties.idp_authnrequest_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&saml2_update1_properties.idp_authnrequest_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&sys_original.saml2_update1_properties.idp_logout_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&saml2_update1_properties.idp_logout_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&sys_original.saml2_update1_properties.service_url=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.do&saml2_update1_properties.service_url=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.do&sys_original.saml2_update1_properties.issuer=https%3A%2F%2Fdev130499.service-now.com&saml2_update1_properties.issuer=https%3A%2F%2Fdev130499.service-now.com&sys_original.saml2_update1_properties.audience=https%3A%2F%2Fdev130499.service-now.com&saml2_update1_properties.audience=https%3A%2F%2Fdev130499.service-now.com&sys_original.saml2_update1_properties.nameid_policy=urn%3Aoasis%3Anames%3Atc%3ASAML%3A1.1%3Anameid-format%3AemailAddress&saml2_update1_properties.nameid_policy=urn%3Aoasis%3Anames%3Atc%3ASAML%3A1.1%3Anameid-format%3AemailAddress&sys_original.saml2_update1_properties.external_logout_redirect=external_logout_complete.do&saml2_update1_properties.external_logout_redirect=external_logout_complete.do&sys_original.saml2_update1_properties.failed_requirement_redirect=&saml2_update1_properties.failed_requirement_redirect=&sys_original.saml2_update1_properties.signing_key_alias=saml2sp&saml2_update1_properties.signing_key_alias=saml2sp&sys_original.saml2_update1_properties.signing_key_password=********&saml2_update1_properties.signing_key_password=********&ni.nolog.saml2_update1_properties.signing_key_password=true&sys_original.saml2_update1_properties.encrypt_assertion=false&saml2_update1_properties.encrypt_assertion=false&sys_original.saml2_update1_properties.sign_algorithmuri=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&saml2_update1_properties.sign_algorithmuri=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&sys_original.saml2_update1_properties.require_signed_authnrequest=false&saml2_update1_properties.require_signed_authnrequest=false&sys_original.saml2_update1_properties.require_signed_logoutrequest=true&ni.saml2_update1_properties.require_signed_logoutrequest=true&saml2_update1_properties.require_signed_logoutrequest=true&sys_original.saml2_update1_properties.auto_provision=false&saml2_update1_properties.auto_provision=false&sys_original.saml2_update1_properties.auto_update_user=true&ni.saml2_update1_properties.auto_update_user=true&saml2_update1_properties.auto_update_user=true&sys_original.saml2_update1_properties.user_field=email&saml2_update1_properties.user_field=email&sys_original.saml2_update1_properties.nameid_attribute=&saml2_update1_properties.nameid_attribute=&sys_original.saml2_update1_properties.createrequestedauthncontext=false&saml2_update1_properties.createrequestedauthncontext=false&sys_original.saml2_update1_properties.authncontextcassref_method=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Aac%3Aclasses%3APasswordProtectedTransport&saml2_update1_properties.authncontextcassref_method=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Aac%3Aclasses%3APasswordProtectedTransport&sys_original.saml2_update1_properties.force_authn=false&saml2_update1_properties.force_authn=false&sys_original.saml2_update1_properties.is_passive=false&saml2_update1_properties.is_passive=false&sys_original.saml2_update1_properties.sign_logout_response=false&saml2_update1_properties.sign_logout_response=false&sys_original.saml2_update1_properties.sso_script=48d518ff73022300ec77bd49faf6a7f6&saml2_update1_properties.sso_script=48d518ff73022300ec77bd49faf6a7f6&sys_display.original.saml2_update1_properties.sso_script=MultiSSOv2_SAML2_custom&sys_display.saml2_update1_properties.sso_script=MultiSSOv2_SAML2_custom&lookup.saml2_update1_properties.sso_script=&viewr.saml2_update1_properties.sso_script=&sys_original.saml2_update1_properties.clock_skew=180&saml2_update1_properties.clock_skew=180&sys_original.saml2_update1_properties.idp_authnrequest_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&saml2_update1_properties.idp_authnrequest_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&sys_original.saml2_update1_properties.idp_logout_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST&saml2_update1_properties.idp_logout_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST&sys_original.saml2_update1_properties.idp_logout_response_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&saml2_update1_properties.idp_logout_response_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&sys_original.saml2_update1_properties.idp_metadata_url=&saml2_update1_properties.idp_metadata_url=&not_important=sysverb_update&sysparm_encoded_record=&sysverb_update_and_stay=&sysverb_insert=&sysverb_insert_and_stay=&show_history=&personalizer_saml2_update1_properties=true&sysparm_changes_tested=true&saml2_update1_properties.active=false&ni.saml2_update1_properties.active=true  

11/06/22 22:50:51 (943) masked field changed: signing_key_password  

11/06/22 22:50:51 (947) SSOID received dc33b505970f1110c4a735dfe153af57  

11/06/22 22:50:51 (947) Applying form changes for dc33b505970f1110c4a735dfe153af57  

11/06/22 22:50:51 (948) masked field changed: signing_key_password  

11/06/22 22:50:51 (948) Testing SSO: dc33b505970f1110c4a735dfe153af57  

11/06/22 22:50:51 (949) Performing test connection login for dc33b505970f1110c4a735dfe153af57  

11/06/22 22:50:51 (951) sso_id:dc33b505970f1110c4a735dfe153af57  

11/06/22 22:50:51 (951) User attempting to login using SSO http://adfs01.rcw.com/adfs/services/trust  

11/06/22 22:50:51 (953) ScriptName : MultiSSOv2_SAML2_custom  

11/06/22 22:50:51 (954) SAML Request xml: <saml2p:AuthnRequest xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol" AssertionConsumerServiceURL="https://dev130499.service-now.com/navpage.do" Destination="https://adfs01.rcw.com/adfs/ls/" ForceAuthn="true" ID="SNC8fa3e13b282557b038524021e03b895e" IsPassive="false" IssueInstant="2022-11-07T06:50:51.954Z" ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" ProviderName="https://dev130499.service-now.com/navpage.do" Version="2.0"><saml2:Issuer xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">https://dev130499.service-now.com</saml2:Issuer><saml2p:NameIDPolicy AllowCreate="true" Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"/></saml2p:AuthnRequest>  

11/06/22 22:50:51 (956) Redirecting to: https://adfs01.rcw.com/adfs/ls/?SAMLRequest=lVLRTsIwFP2Vpe%2Fb2o4JNIxkQowkiIugD76V7aJNunb2dkP%2FXhgY9UGNj7339JzTczpBWWveiLz1z%2BYOXlpAH7zW2qA4bTLSOiOsRIXCyBpQ%2BFKs85ul4BEVjbPellaTIEcE55U1M2uwrcGtwXWqhPu7ZUaevW9QxHEFHUvoYDyO8LQNjd1Hpa1jI7tGPkFUWRLMDx6UkUeyz6uy2iFlkStP%2BOMx1hiT4Mq6Enr7GfGuBRIs5hlZr2ajnUyAJVs%2B4mk63NJklPIB5Qxosh2N0yMQC4moOsjITmrsJ9jCwqCXxmeEU85DxkI63NALkVKRsmicDh5JUJzffalMpczT7yFtTyAU15tNERa3601P0KkK3OqA%2Fm8%2BD%2BCwz%2BZATqaTvifRO3dfq%2FvdlPzoi0z%2FVJ%2FEXzXOio04el%2FMC6tV%2BRbkWtv9zIH08NHDoZla%2Bp9tsIj1E1WFux4qoJZK51XlAJHE07Pu9985fQc%3D&RelayState=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.doSNCRSEPsysparm_saml_tc%3Dtrue%26glide_sso_id%3Ddc33b505970f1110c4a735dfe153af57%26exit_name%3DMultiSSOv2  

11/06/22 22:50:51 (956) request type : request  

11/06/22 22:50:51 (957) We will be redirecting user to the URL: /saml_test_conn_completed.do?sysparm_nostack=true&sysparm_test_sso_id=dc33b505970f1110c4a735dfe153af57  

11/06/22 22:50:51 (957) userToLogin: https://adfs01.rcw.com/adfs/ls/?SAMLRequest=lVLRTsIwFP2Vpe%2Fb2o4JNIxkQowkiIugD76V7aJNunb2dkP%2FXhgY9UGNj7339JzTczpBWWveiLz1z%2BYOXlpAH7zW2qA4bTLSOiOsRIXCyBpQ%2BFKs85ul4BEVjbPellaTIEcE55U1M2uwrcGtwXWqhPu7ZUaevW9QxHEFHUvoYDyO8LQNjd1Hpa1jI7tGPkFUWRLMDx6UkUeyz6uy2iFlkStP%2BOMx1hiT4Mq6Enr7GfGuBRIs5hlZr2ajnUyAJVs%2B4mk63NJklPIB5Qxosh2N0yMQC4moOsjITmrsJ9jCwqCXxmeEU85DxkI63NALkVKRsmicDh5JUJzffalMpczT7yFtTyAU15tNERa3601P0KkK3OqA%2Fm8%2BD%2BCwz%2BZATqaTvifRO3dfq%2FvdlPzoi0z%2FVJ%2FEXzXOio04el%2FMC6tV%2BRbkWtv9zIH08NHDoZla%2Bp9tsIj1E1WFux4qoJZK51XlAJHE07Pu9985fQc%3D&RelayState=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.doSNCRSEPsysparm_saml_tc%3Dtrue%26glide_sso_id%3Ddc33b505970f1110c4a735dfe153af57%26exit_name%3DMultiSSOv2  

11/06/22 22:50:51 (958) Read from column : popup_dlg_width, value: 900  

11/06/22 22:50:51 (958) Read from column : popup_dlg_height, value: 800  

11/06/22 22:51:03 (460) sso_id:dc33b505970f1110c4a735dfe153af57  

11/06/22 22:51:03 (461) User attempting to login using SSO http://adfs01.rcw.com/adfs/services/trust  

11/06/22 22:51:03 (462) ScriptName : MultiSSOv2_SAML2_custom  

11/06/22 22:51:03 (463) SAML Request xml:<samlp:Response ID="_ca831c6f-72cb-49a3-bca7-807c59a27f00" Version="2.0" IssueInstant="2022-11-07T06:51:02.523Z" Destination="https://dev130499.service-now.com/navpage.do" Consent="urn:oasis:names:tc:SAML:2.0:consent:unspecified" InResponseTo="SNC8fa3e13b282557b038524021e03b895e" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"><Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">http://adfs01.rcw.com/adfs/services/trust</Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /><ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" /><ds:Reference URI="#_ca831c6f-72cb-49a3-bca7-807c59a27f00"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" /><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" /><ds:DigestValue>PfmGno7WrCkusFXBj6V5Qcf12cmY2CGD27zNrbOgACU=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>eHoyxsX2b1WA4mP9EzH12oM4TAxFLgPB3CwCJco2QygfjBO5T46blLhWnyEZQjy5FFHkJzKO8fOQejpeG4gvisTnkXMqXW6gXGzY56TanFu3sujHVhEtEnXW0UojROlL5n/YGYB9U9hm/cUPROhr39ku+1fCqjE768l6XIafpWGKwW0uB7oTFwN9r2QgZHD8UxluI2IIU0CBGq7vkOWORcGDU+LybzppAp8IZfXH00TCJz1BEsajNn3gW8vcrHRPagAq0bf6WpfXY/s22BsAUpwTEFYaP+ukPGtn+RakoN0vfqB4nxF+aHf4Ui5PpOsoJEpGgDYK5Rl6RPDrJ/OZhA==</ds:SignatureValue><KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIC2DCCAcCgAwIBAgIQI60wgkbaF7RKWn4JaaxBXTANBgkqhkiG9w0BAQsFADAoMSYwJAYDVQQDEx1BREZTIFNpZ25pbmcgLSBhZGZzMDEucmN3LmNvbTAeFw0yMjExMDUwNzI5MzFaFw0yMzExMDUwNzI5MzFaMCgxJjAkBgNVBAMTHUFERlMgU2lnbmluZyAtIGFkZnMwMS5yY3cuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPl6/dfdFqD7ZxWipF0rm+RfjlF7O1vW2M0kxoNQiPqq2K4UbTfe5fWDyfGeN3hvdjbtKFnWUdXOnpq9/3RHR3EL0SSRuhY1gtC+wOvadzHVXmbCB36zzkuDKA+DZytHgufGSvFvvURm9lYOF+p2L5wokgLpHbAjwy9N24a73dmJIlezoUIi4BF9i1hpjRuzg8bZigRKQqOz1zj8BsrxtQwj2H7ADbAIZKO/aQqqJqA4jx2j+LuWN5qXNKe5I5exM76hcOMLsxBmWxljwAzQ210bLXAp1y9iTu2Wla3yjd7HXmryLMh4QUaQAWnTEkCp5ZyeBixqxEfhX1xBmT1S5wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAAdBblBZF+cr5t4b+zzVOM2qrxCkeOO7SZNdrNZXPE3F4rq1ZSgvjJre27fjNYlrfxz+t5vHFQPoIEkhb4uhSpq+V+6R/C00VlLe52Hwhjrve3ThWdfsfREcyxyD3Vy45Z3Tiw5/WO5r4J6LICOUWVrFrG0g+B5oKI4JIR5ls8k+wgI0DLlnAHD9epvNBGDu/UGU2U7jNIc0kfg444Jy9i8PeUQSGU7SmpsgulK1789xURJUfqXTWLhEe96W6JXQahQ96SvqXsLCf3B7+LzXNDJlKyB7XXj8wS6xv7anhlnn2AlSnrWxu63SI3Hrb4AMHGLe3DFU1jxGBzhaQM1kYw</ds:X509Certificate></ds:X509Data></KeyInfo></ds:Signature><samlp:Status><samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Requester"><samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:InvalidNameIDPolicy" /></samlp:StatusCode></samlp:Status></samlp:Response>  

11/06/22 22:51:03 (463) SAML Request object created.  

11/06/22 22:51:03 (464) Issue Instant: 2022-11-07T06:51:02.523Z  

11/06/22 22:51:03 (464) Issuer found in the response : http://adfs01.rcw.com/adfs/services/trust  

11/06/22 22:51:03 (465) IdP found based on SAML response: dc33b505970f1110c4a735dfe153af57  

11/06/22 22:51:03 (465) Session inResponseTo: SNC8fa3e13b282557b038524021e03b895e  

11/06/22 22:51:03 (466) Status code: urn:oasis:names:tc:SAML:2.0:status:Requester  

11/06/22 22:51:03 (466) Status message: null  

11/06/22 22:51:03 (466) SAML2Error: SAML failed to login, Status code is urn:oasis:names:tc:SAML:2.0:status:Requester. When it is supposed to be urn:oasis:names:tc:SAML:2.0:status:Success  

11/06/22 22:51:03 (466) Could not validate SAMLResponse  

11/06/22 22:51:03 (467) request type : request  

11/06/22 22:51:03 (467) We will be redirecting user to the URL: /saml_test_conn_completed.do?sysparm_nostack=true&sysparm_test_sso_id=dc33b505970f1110c4a735dfe153af57  

11/06/22 22:51:03 (467) userToLogin: failed_authentication  

11/06/22 22:51:03 (752) User session is using SSO : null  

11/06/22 22:51:03 (753) Testing SSO: dc33b505970f1110c4a735dfe153af57  

11/06/22 22:51:03 (753) StatusCode: urn:oasis:names:tc:SAML:2.0:status:Requester  

11/06/22 22:51:03 (756) **** NEED LOGOUT SET TO TRUE ****

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-08*

Hi Piaudonn,    

Thanks a lot for your response. I tried and it seems to be better now. But I got below error.    

User: ******@rcw.com not found    

Ensure that the user you are trying the test connection with is present in the system.    

Ensure that 'User Field' property value corresponds to the value set in the IDP returned through 'Subject NameID' in the response.    

11/08/22 07:00:49 (471) sysparm_form_fields: sysparm_ck=7a21b46597031110c4a735dfe153af011b76da204740c3729d7fe7c769a0ef3b1010b68b&sys_base_uri=https%3A%2F%2Fdev130499.service-now.com%2F&sys_target=saml2_update1_properties&sys_uniqueName=sys_id&sys_uniqueValue=dc33b505970f1110c4a735dfe153af57&sys_displayValue=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&sys_titleValue=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&onLoad_sys_updated_on=2022-11-07+07%3A40%3A31&sys_row=0&sys_modCount=9&sys_action=none&sysparm_collection=&sysparm_collectionID=&sysparm_collection_key=&sysparm_collection_related_field=&sysparm_collection_relationship=&sysparm_redirect_url=&sysparm_goto_url=&isFormPage=true&sysparm_referring_url=&sysparm_view=&sysparm_changeset=&sysparm_template_editable=&sysparm_record_row=2&sysparm_record_list=ORDERBYname&sysparm_record_rows=3&sysparm_record_target=sso_properties&sysparm_modify_check=true&sysparm_action_template=&sysparm_link_collection=&sysparm_pop_onLoad=&sysparm_nameofstack=&sysparm_transaction_scope=&sysparm_transaction_update_set=&sysparm_record_scope=&sysparm_ck=7a21b46597031110c4a735dfe153af011b76da204740c3729d7fe7c769a0ef3b1010b68b&sys_original.saml2_update1_properties.name=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&saml2_update1_properties.name=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&sys_original.saml2_update1_properties.default=false&saml2_update1_properties.default=false&sys_original.saml2_update1_properties.active=false&saml2_update1_properties.active=false&sys_original.saml2_update1_properties.is_primary=false&saml2_update1_properties.is_primary=false&sys_original.saml2_update1_properties.idp=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&saml2_update1_properties.idp=http%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fservices%2Ftrust&sys_original.saml2_update1_properties.idp_authnrequest_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&saml2_update1_properties.idp_authnrequest_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&sys_original.saml2_update1_properties.idp_logout_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&saml2_update1_properties.idp_logout_url=https%3A%2F%2Fadfs01.rcw.com%2Fadfs%2Fls%2F&sys_original.saml2_update1_properties.service_url=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.do&saml2_update1_properties.service_url=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.do&sys_original.saml2_update1_properties.issuer=https%3A%2F%2Fdev130499.service-now.com&saml2_update1_properties.issuer=https%3A%2F%2Fdev130499.service-now.com&sys_original.saml2_update1_properties.audience=https%3A%2F%2Fdev130499.service-now.com&saml2_update1_properties.audience=https%3A%2F%2Fdev130499.service-now.com&sys_original.saml2_update1_properties.nameid_policy=urn%3Aoasis%3Anames%3Atc%3ASAML%3A1.1%3Anameid-format%3AemailAddress&saml2_update1_properties.nameid_policy=urn%3Aoasis%3Anames%3Atc%3ASAML%3A1.1%3Anameid-format%3AemailAddress&sys_original.saml2_update1_properties.external_logout_redirect=external_logout_complete.do&saml2_update1_properties.external_logout_redirect=external_logout_complete.do&sys_original.saml2_update1_properties.failed_requirement_redirect=&saml2_update1_properties.failed_requirement_redirect=&sys_original.saml2_update1_properties.signing_key_alias=saml2sp&saml2_update1_properties.signing_key_alias=saml2sp&sys_original.saml2_update1_properties.signing_key_password=&saml2_update1_properties.signing_key_password=&ni.nolog.saml2_update1_properties.signing_key_password=true&sys_original.saml2_update1_properties.encrypt_assertion=false&saml2_update1_properties.encrypt_assertion=false&sys_original.saml2_update1_properties.sign_algorithmuri=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&saml2_update1_properties.sign_algorithmuri=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&sys_original.saml2_update1_properties.require_signed_authnrequest=false&saml2_update1_properties.require_signed_authnrequest=false&sys_original.saml2_update1_properties.require_signed_logoutrequest=true&ni.saml2_update1_properties.require_signed_logoutrequest=true&saml2_update1_properties.require_signed_logoutrequest=true&sys_original.saml2_update1_properties.auto_provision=false&saml2_update1_properties.auto_provision=false&sys_original.saml2_update1_properties.auto_update_user=true&ni.saml2_update1_properties.auto_update_user=true&saml2_update1_properties.auto_update_user=true&sys_original.saml2_update1_properties.user_field=email&saml2_update1_properties.user_field=email&sys_original.saml2_update1_properties.nameid_attribute=&saml2_update1_properties.nameid_attribute=&sys_original.saml2_update1_properties.createrequestedauthncontext=true&ni.saml2_update1_properties.createrequestedauthncontext=true&saml2_update1_properties.createrequestedauthncontext=true&sys_original.saml2_update1_properties.authncontextcassref_method=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Aac%3Aclasses%3APasswordProtectedTransport&saml2_update1_properties.authncontextcassref_method=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Aac%3Aclasses%3APasswordProtectedTransport&sys_original.saml2_update1_properties.force_authn=false&saml2_update1_properties.force_authn=false&sys_original.saml2_update1_properties.is_passive=false&saml2_update1_properties.is_passive=false&sys_original.saml2_update1_properties.sign_logout_response=false&saml2_update1_properties.sign_logout_response=false&sys_original.saml2_update1_properties.sso_script=48d518ff73022300ec77bd49faf6a7f6&saml2_update1_properties.sso_script=48d518ff73022300ec77bd49faf6a7f6&sys_display.original.saml2_update1_properties.sso_script=MultiSSOv2_SAML2_custom&sys_display.saml2_update1_properties.sso_script=MultiSSOv2_SAML2_custom&lookup.saml2_update1_properties.sso_script=&viewr.saml2_update1_properties.sso_script=&sys_original.saml2_update1_properties.clock_skew=180&saml2_update1_properties.clock_skew=180&sys_original.saml2_update1_properties.idp_authnrequest_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&saml2_update1_properties.idp_authnrequest_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&sys_original.saml2_update1_properties.idp_logout_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST&saml2_update1_properties.idp_logout_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST&sys_original.saml2_update1_properties.idp_logout_response_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&saml2_update1_properties.idp_logout_response_binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-Redirect&sys_original.saml2_update1_properties.idp_metadata_url=&saml2_update1_properties.idp_metadata_url=&not_important=sysverb_update&sysparm_encoded_record=&sysverb_update_and_stay=&sysverb_insert=&sysverb_insert_and_stay=&show_history=&personalizer_saml2_update1_properties=true&sysparm_changes_tested=true&saml2_update1_properties.active=false&ni.saml2_update1_properties.active=true    

11/08/22 07:00:49 (474) masked field changed: signing_key_password    

11/08/22 07:00:49 (477) SSOID received dc33b505970f1110c4a735dfe153af57    

11/08/22 07:00:49 (477) Applying form changes for dc33b505970f1110c4a735dfe153af57    

11/08/22 07:00:49 (478) masked field changed: signing_key_password    

11/08/22 07:00:49 (478) Testing SSO: dc33b505970f1110c4a735dfe153af57    

11/08/22 07:00:49 (478) Performing test connection login for dc33b505970f1110c4a735dfe153af57    

11/08/22 07:00:49 (480) sso_id:dc33b505970f1110c4a735dfe153af57    

11/08/22 07:00:49 (481) User attempting to login using SSO http://adfs01.rcw.com/adfs/services/trust    

11/08/22 07:00:49 (482) ScriptName : MultiSSOv2_SAML2_custom    

11/08/22 07:00:49 (484) SAML Request xml: <saml2p:AuthnRequest xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol" AssertionConsumerServiceURL="https://dev130499.service-now.com/navpage.do" Destination="https://adfs01.rcw.com/adfs/ls/" ForceAuthn="true" ID="SNCa08e9d6bd57f3eb7597f2b88d6b66a93" IsPassive="false" IssueInstant="2022-11-08T15:00:49.483Z" ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" ProviderName="https://dev130499.service-now.com/navpage.do" Version="2.0"><saml2:Issuer xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">https://dev130499.service-now.com</saml2:Issuer><saml2p:NameIDPolicy AllowCreate="true" Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"/><saml2p:RequestedAuthnContext Comparison="exact"><saml2:AuthnContextClassRef xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml2:AuthnContextClassRef></saml2p:RequestedAuthnContext></saml2p:AuthnRequest>    

11/08/22 07:00:49 (485) Redirecting to: https://adfs01.rcw.com/adfs/ls/?SAMLRequest=nVNNb9swDP0rhu7%2BzJctxAE8B8MCdF2QeDvspkh0K8CWPFF2sn8%2F20naHNoU3VHkI%2Fn4HrVEVldRQ7PWPqsd%2FGkBrXOqK4X0nElJaxTVDCVSxWpAajndZ98faOQFtDHaaq4r4mSIYKzUKtcK2xrMHkwnOfzcPaTk2doGqe8L6MJJME0SD89ZV%2Bmjx3XtK9Y17Ak8oYmz7jlIxYZmr6VMlBiEnuFn%2FPD0K%2FSJ81UbDiP9lFjTAnE265TsH3MWxJCI%2BUHMFuUEDotZsiijQxz3ofmcJZMeiFuGKDtISckqHEoRW9gotEzZlERBFLlh6AZxEc5oENBp4k3jyW%2FibC97f5FKSPV0X6TDGYT0W1Fs3e2PfTE26KQA89ijP6vPLzA4atM3J6vl6BMdmZtb6%2B6TYle%2FyOrD6Uv%2FdsZlYkMH7pv1VleS%2F3WyqtLH3ACzcPWhd6Zm9n0aoReOESnccoRSqJmsMiEMIBL%2FZdDlLkGMNvcHZuFknVzXDTMSByXgxLh90eIWllf9pjso%2F0uZuzBO%2BdC7Dw9XdNRGDFcBvOdZGKaw0cZelXuL0eqSfGe%2F1%2FTt31z9Aw%3D%3D&RelayState=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.doSNCRSEPsysparm_saml_tc%3Dtrue%26glide_sso_id%3Ddc33b505970f1110c4a735dfe153af57%26exit_name%3DMultiSSOv2    

11/08/22 07:00:49 (486) request type : request    

11/08/22 07:00:49 (486) We will be redirecting user to the URL: /saml_test_conn_completed.do?sysparm_nostack=true&sysparm_test_sso_id=dc33b505970f1110c4a735dfe153af57    

11/08/22 07:00:49 (486) userToLogin: https://adfs01.rcw.com/adfs/ls/?SAMLRequest=nVNNb9swDP0rhu7%2BzJctxAE8B8MCdF2QeDvspkh0K8CWPFF2sn8%2F20naHNoU3VHkI%2Fn4HrVEVldRQ7PWPqsd%2FGkBrXOqK4X0nElJaxTVDCVSxWpAajndZ98faOQFtDHaaq4r4mSIYKzUKtcK2xrMHkwnOfzcPaTk2doGqe8L6MJJME0SD89ZV%2Bmjx3XtK9Y17Ak8oYmz7jlIxYZmr6VMlBiEnuFn%2FPD0K%2FSJ81UbDiP9lFjTAnE265TsH3MWxJCI%2BUHMFuUEDotZsiijQxz3ofmcJZMeiFuGKDtISckqHEoRW9gotEzZlERBFLlh6AZxEc5oENBp4k3jyW%2FibC97f5FKSPV0X6TDGYT0W1Fs3e2PfTE26KQA89ijP6vPLzA4atM3J6vl6BMdmZtb6%2B6TYle%2FyOrD6Uv%2FdsZlYkMH7pv1VleS%2F3WyqtLH3ACzcPWhd6Zm9n0aoReOESnccoRSqJmsMiEMIBL%2FZdDlLkGMNvcHZuFknVzXDTMSByXgxLh90eIWllf9pjso%2F0uZuzBO%2BdC7Dw9XdNRGDFcBvOdZGKaw0cZelXuL0eqSfGe%2F1%2FTt31z9Aw%3D%3D&RelayState=https%3A%2F%2Fdev130499.service-now.com%2Fnavpage.doSNCRSEPsysparm_saml_tc%3Dtrue%26glide_sso_id%3Ddc33b505970f1110c4a735dfe153af57%26exit_name%3DMultiSSOv2    

11/08/22 07:00:49 (487) Read from column : popup_dlg_width, value: 900    

11/08/22 07:00:49 (488) Read from column : popup_dlg_height, value: 800    

11/08/22 07:01:02 (821) sso_id:dc33b505970f1110c4a735dfe153af57    

11/08/22 07:01:02 (822) User attempting to login using SSO http://adfs01.rcw.com/adfs/services/trust    

11/08/22 07:01:02 (822) ScriptName : MultiSSOv2_SAML2_custom    

11/08/22 07:01:02 (823) SAML Request xml:<samlp:Response ID="_b54b68ff-f0f7-4d55-868e-aa0a324d4947" Version="2.0" IssueInstant="2022-11-08T15:01:01.481Z" Destination="https://dev130499.service-now.com/navpage.do" Consent="urn:oasis:names:tc:SAML:2.0:consent:unspecified" InResponseTo="SNCa08e9d6bd57f3eb7597f2b88d6b66a93" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"><Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion">http://adfs01.rcw.com/adfs/services/trust</Issuer>samlp:Status<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success" /></samlp:Status><Assertion ID="_6be43188-e46e-44f1-8950-2f0862565e8b" IssueInstant="2022-11-08T15:01:01.481Z" Version="2.0" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"><Issuer>http://adfs01.rcw.com/adfs/services/trust</Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /><ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" /><ds:Reference URI="#_6be43188-e46e-44f1-8950-2f0862565e8b"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" /><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" /><ds:DigestValue>GILA/a9k9DqLA691Col6bBR9aDalsaTU0NeM0md+fS4=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>RzSPA3sp41K93Yb570QD94/eBjAgdggQ33pdjGAv7RfjhAXMiCjwp+DowSBaEjyMkYDNye57SdftuSR9S58+GX9ciQAFZnknQA0+cNgxtlSasyIerX0aYN++Ro+bdOofUvOeBkvNa5PXRpW3G0kVK+CbE/cvmlE9OT2iBAAum2mFAf4V+RZyFAD/XvWVo09Y8YYfdYZpa47EhlsuOCqO3t71zUlefzmRSZdSCTb5spvY1neO5GMC/TtB41Hjez/m5LvrjSjroDLw64G7XU48QH6P4nLAKm4ALlfufogfS9F2GaGBsPo54haQEKACFqmruh3k9kgmVQpIw0suVJLXoA==</ds:SignatureValue><KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIC2DCCAcCgAwIBAgIQI60wgkbaF7RKWn4JaaxBXTANBgkqhkiG9w0BAQsFADAoMSYwJAYDVQQDEx1BREZTIFNpZ25pbmcgLSBhZGZzMDEucmN3LmNvbTAeFw0yMjExMDUwNzI5MzFaFw0yMzExMDUwNzI5MzFaMCgxJjAkBgNVBAMTHUFERlMgU2lnbmluZyAtIGFkZnMwMS5yY3cuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPl6/dfdFqD7ZxWipF0rm+RfjlF7O1vW2M0kxoNQiPqq2K4UbTfe5fWDyfGeN3hvdjbtKFnWUdXOnpq9/3RHR3EL0SSRuhY1gtC+wOvadzHVXmbCB36zzkuDKA+DZytHgufGSvFvvURm9lYOF+p2L5wokgLpHbAjwy9N24a73dmJIlezoUIi4BF9i1hpjRuzg8bZigRKQqOz1zj8BsrxtQwj2H7ADbAIZKO/aQqqJqA4jx2j+LuWN5qXNKe5I5exM76hcOMLsxBmWxljwAzQ210bLXAp1y9iTu2Wla3yjd7HXmryLMh4QUaQAWnTEkCp5ZyeBixqxEfhX1xBmT1S5wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAAdBblBZF+cr5t4b+zzVOM2qrxCkeOO7SZNdrNZXPE3F4rq1ZSgvjJre27fjNYlrfxz+t5vHFQPoIEkhb4uhSpq+V+6R/C00VlLe52Hwhjrve3ThWdfsfREcyxyD3Vy45Z3Tiw5/WO5r4J6LICOUWVrFrG0g+B5oKI4JIR5ls8k+wgI0DLlnAHD9epvNBGDu/UGU2U7jNIc0kfg444Jy9i8PeUQSGU7SmpsgulK1789xURJUfqXTWLhEe96W6JXQahQ96SvqXsLCf3B7+LzXNDJlKyB7XXj8wS6xv7anhlnn2AlSnrWxu63SI3Hrb4AMHGLe3DFU1jxGBzhaQM1kYw</ds:X509Certificate></ds:X509Data></KeyInfo></ds:Signature><Subject><NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">@rcw.com</NameID><SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><SubjectConfirmationData InResponseTo="SNCa08e9d6bd57f3eb7597f2b88d6b66a93" NotOnOrAfter="2022-11-08T15:06:01.481Z" Recipient="https://dev130499.service-now.com/navpage.do" /></SubjectConfirmation></Subject><Conditions NotBefore="2022-11-08T15:01:01.481Z" NotOnOrAfter="2022-11-08T16:01:01.481Z"><AudienceRestriction><Audience>https://dev130499.service-now.com</Audience></AudienceRestriction></Conditions><AuthnStatement AuthnInstant="2022-11-08T15:01:01.448Z" SessionIndex="_6be43188-e46e-44f1-8950-2f0862565e8b"><AuthnContext><AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</AuthnContextClassRef></AuthnContext></AuthnStatement></Assertion></samlp:Response>    

11/08/22 07:01:02 (824) SAML Request object created.    

11/08/22 07:01:02 (825) Issue Instant: 2022-11-08T15:01:01.481Z    

11/08/22 07:01:02 (826) Issuer found in the response : http://adfs01.rcw.com/adfs/services/trust    

11/08/22 07:01:02 (827) IdP found based on SAML response: dc33b505970f1110c4a735dfe153af57    

11/08/22 07:01:02 (827) Session inResponseTo: SNCa08e9d6bd57f3eb7597f2b88d6b66a93    

11/08/22 07:01:02 (827) Status code: urn:oasis:names:tc:SAML:2.0:status:Success    

11/08/22 07:01:02 (828) Status message: null    

11/08/22 07:01:02 (828) Signature Reference ID: _b54b68ff-f0f7-4d55-868e-aa0a324d4947    

11/08/22 07:01:02 (829) Subject NameID:@rcw.com    

11/08/22 07:01:02 (829) SessionIndex: _6be43188-e46e-44f1-8950-2f0862565e8b    

11/08/22 07:01:02 (829) Signature not in response, attempting to get signature from assertion    

11/08/22 07:01:02 (831) Validating SAML response against the certificate : http://adfs01.rcw.com/adfs/services/trust_1    

11/08/22 07:01:02 (832) certificate Issuer DN: CN=ADFS Encryption - adfs01.rcw.com    

11/08/22 07:01:02 (832) certificate valid date from: Sat Nov 05 00:29:31 PDT 2022    

11/08/22 07:01:02 (833) certificate valid date to: Sun Nov 05 00:29:31 PDT 2023    

11/08/22 07:01:02 (833) Current timestamp: Tue Nov 08 07:01:02 PST 2022    

11/08/22 07:01:02 (834) Public key created    

11/08/22 07:01:02 (834) Got signature    

11/08/22 07:01:02 (835) <?xml version="1.0" encoding="UTF-8"?><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/><ds:Reference URI="#_6be43188-e46e-44f1-8950-2f0862565e8b"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/><ds:DigestValue>GILA/a9k9DqLA691Col6bBR9aDalsaTU0NeM0md+fS4=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>RzSPA3sp41K93Yb570QD94/eBjAgdggQ33pdjGAv7RfjhAXMiCjwp+DowSBaEjyMkYDNye57SdftuSR9S58+GX9ciQAFZnknQA0+cNgxtlSasyIerX0aYN++Ro+bdOofUvOeBkvNa5PXRpW3G0kVK+CbE/cvmlE9OT2iBAAum2mFAf4V+RZyFAD/XvWVo09Y8YYfdYZpa47EhlsuOCqO3t71zUlefzmRSZdSCTb5spvY1neO5GMC/TtB41Hjez/m5LvrjSjroDLw64G7XU48QH6P4nLAKm4ALlfufogfS9F2GaGBsPo54haQEKACFqmruh3k9kgmVQpIw0suVJLXoA==</ds:SignatureValue><KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIC2DCCAcCgAwIBAgIQI60wgkbaF7RKWn4JaaxBXTANBgkqhkiG9w0BAQsFADAoMSYwJAYDVQQDEx1BREZTIFNpZ25pbmcgLSBhZGZzMDEucmN3LmNvbTAeFw0yMjExMDUwNzI5MzFaFw0yMzExMDUwNzI5MzFaMCgxJjAkBgNVBAMTHUFERlMgU2lnbmluZyAtIGFkZnMwMS5yY3cuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPl6/dfdFqD7ZxWipF0rm+RfjlF7O1vW2M0kxoNQiPqq2K4UbTfe5fWDyfGeN3hvdjbtKFnWUdXOnpq9/3RHR3EL0SSRuhY1gtC+wOvadzHVXmbCB36zzkuDKA+DZytHgufGSvFvvURm9lYOF+p2L5wokgLpHbAjwy9N24a73dmJIlezoUIi4BF9i1hpjRuzg8bZigRKQqOz1zj8BsrxtQwj2H7ADbAIZKO/aQqqJqA4jx2j+LuWN5qXNKe5I5exM76hcOMLsxBmWxljwAzQ210bLXAp1y9iTu2Wla3yjd7HXmryLMh4QUaQAWnTEkCp5ZyeBixqxEfhX1xBmT1S5wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAAdBblBZF+cr5t4b+zzVOM2qrxCkeOO7SZNdrNZXPE3F4rq1ZSgvjJre27fjNYlrfxz+t5vHFQPoIEkhb4uhSpq+V+6R/C00VlLe52Hwhjrve3ThWdfsfREcyxyD3Vy45Z3Tiw5/WO5r4J6LICOUWVrFrG0g+B5oKI4JIR5ls8k+wgI0DLlnAHD9epvNBGDu/UGU2U7jNIc0kfg444Jy9i8PeUQSGU7SmpsgulK1789xURJUfqXTWLhEe96W6JXQahQ96SvqXsLCf3B7+LzXNDJlKyB7XXj8wS6xv7anhlnn2AlSnrWxu63SI3Hrb4AMHGLe3DFU1jxGBzhaQM1kYw</ds:X509Certificate></ds:X509Data></KeyInfo></ds:Signature>    

11/08/22 07:01:02 (836) Failed to validate signature profile.    

11/08/22 07:01:02 (836) SAML2ValidationError: Signature cryptographic validation not successful    

11/08/22 07:01:02 (836) Validating SAML response against the certificate : http://adfs01.rcw.com/adfs/services/trust_2    

11/08/22 07:01:02 (837) certificate Issuer DN: CN=ADFS Signing - adfs01.rcw.com    

11/08/22 07:01:02 (837) certificate valid date from: Sat Nov 05 00:29:31 PDT 2022    

11/08/22 07:01:02 (837) certificate valid date to: Sun Nov 05 00:29:31 PDT 2023    

11/08/22 07:01:02 (837) Current timestamp: Tue Nov 08 07:01:02 PST 2022    

11/08/22 07:01:02 (838) Public key created    

11/08/22 07:01:02 (838) Got signature    

11/08/22 07:01:02 (838) <?xml version="1.0" encoding="UTF-8"?><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/><ds:Reference URI="#_6be43188-e46e-44f1-8950-2f0862565e8b"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/><ds:DigestValue>GILA/a9k9DqLA691Col6bBR9aDalsaTU0NeM0md+fS4=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>RzSPA3sp41K93Yb570QD94/eBjAgdggQ33pdjGAv7RfjhAXMiCjwp+DowSBaEjyMkYDNye57SdftuSR9S58+GX9ciQAFZnknQA0+cNgxtlSasyIerX0aYN++Ro+bdOofUvOeBkvNa5PXRpW3G0kVK+CbE/cvmlE9OT2iBAAum2mFAf4V+RZyFAD/XvWVo09Y8YYfdYZpa47EhlsuOCqO3t71zUlefzmRSZdSCTb5spvY1neO5GMC/TtB41Hjez/m5LvrjSjroDLw64G7XU48QH6P4nLAKm4ALlfufogfS9F2GaGBsPo54haQEKACFqmruh3k9kgmVQpIw0suVJLXoA==</ds:SignatureValue><KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIC2DCCAcCgAwIBAgIQI60wgkbaF7RKWn4JaaxBXTANBgkqhkiG9w0BAQsFADAoMSYwJAYDVQQDEx1BREZTIFNpZ25pbmcgLSBhZGZzMDEucmN3LmNvbTAeFw0yMjExMDUwNzI5MzFaFw0yMzExMDUwNzI5MzFaMCgxJjAkBgNVBAMTHUFERlMgU2lnbmluZyAtIGFkZnMwMS5yY3cuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApPl6/dfdFqD7ZxWipF0rm+RfjlF7O1vW2M0kxoNQiPqq2K4UbTfe5fWDyfGeN3hvdjbtKFnWUdXOnpq9/3RHR3EL0SSRuhY1gtC+wOvadzHVXmbCB36zzkuDKA+DZytHgufGSvFvvURm9lYOF+p2L5wokgLpHbAjwy9N24a73dmJIlezoUIi4BF9i1hpjRuzg8bZigRKQqOz1zj8BsrxtQwj2H7ADbAIZKO/aQqqJqA4jx2j+LuWN5qXNKe5I5exM76hcOMLsxBmWxljwAzQ210bLXAp1y9iTu2Wla3yjd7HXmryLMh4QUaQAWnTEkCp5ZyeBixqxEfhX1xBmT1S5wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAAdBblBZF+cr5t4b+zzVOM2qrxCkeOO7SZNdrNZXPE3F4rq1ZSgvjJre27fjNYlrfxz+t5vHFQPoIEkhb4uhSpq+V+6R/C00VlLe52Hwhjrve3ThWdfsfREcyxyD3Vy45Z3Tiw5/WO5r4J6LICOUWVrFrG0g+B5oKI4JIR5ls8k+wgI0DLlnAHD9epvNBGDu/UGU2U7jNIc0kfg444Jy9i8PeUQSGU7SmpsgulK1789xURJUfqXTWLhEe96W6JXQahQ96SvqXsLCf3B7+LzXNDJlKyB7XXj8wS6xv7anhlnn2AlSnrWxu63SI3Hrb4AMHGLe3DFU1jxGBzhaQM1kYw</ds:X509Certificate></ds:X509Data></KeyInfo></ds:Signature>    

11/08/22 07:01:02 (839) Signature validated.    

11/08/22 07:01:02 (840) Step 1/5: Signature validation is successful    

11/08/22 07:01:02 (840) Certificate validated.    

11/08/22 07:01:02 (840) Step 2/5: Certificate validation is successful    

11/08/22 07:01:02 (841) audience, value: https://dev130499.service-now.com    

11/08/22 07:01:02 (841) Found matching audience.    

11/08/22 07:01:02 (841) Conditions validated.    

11/08/22 07:01:02 (841) Step 3/5: AudienceRestriction/Condition validation is successful    

11/08/22 07:01:02 (842) Response issuer validation is skipped.    

11/08/22 07:01:02 (842) Issuer found in the assertion : http://adfs01.rcw.com/adfs/services/trust    

11/08/22 07:01:02 (842) Issuer validated.    

11/08/22 07:01:02 (842) Step 4/5: Certificate Issuer validation is successful    

11/08/22 07:01:02 (846) SubjectConfirmations validated.    

11/08/22 07:01:02 (847) Step 5/5: Subject Confirmation validation is successful    

11/08/22 07:01:02 (847) Authn response object validated.    

11/08/22 07:01:02 (847) Subject NameID:@rcw.com    

11/08/22 07:01:02 (847) Subject NameID:@rcw.com    

11/08/22 07:01:02 (848) SAML2 NameID: ******@rcw.com    

11/08/22 07:01:02 (848) SessionIndex: _6be43188-e46e-44f1-8950-2f0862565e8b    

11/08/22 07:01:02 (848) SAML2 SessionIndex: _6be43188-e46e-44f1-8950-2f0862565e8b    

11/08/22 07:01:02 (850) User: @rcw.com not found    

11/08/22 07:01:02 (851) request type : request    

11/08/22 07:01:02 (852) We will be redirecting user to the URL: /saml_test_conn_completed.do?sysparm_nostack=true&sysparm_test_sso_id=dc33b505970f1110c4a735dfe153af57    

11/08/22 07:01:02 (852) userToLogin: failed_authentication    

11/08/22 07:01:03 (153) User session is using SSO : null    

11/08/22 07:01:03 (154) Testing SSO: dc33b505970f1110c4a735dfe153af57    

11/08/22 07:01:03 (154) StatusCode: urn:oasis:names:tc:SAML:2.0:status:Success    

11/08/22 07:01:03 (157) **** NEED LOGOUT SET TO TRUE ****    

11/08/22 07:01:03 (539) Performing test connection logout for dc33b505970f1110c4a735dfe153af57    

11/08/22 07:01:03 (542) Logging out external auth : saml2_update1_properties    

11/08/22 07:01:03 (542) Logging out external auth : saml2_update1_properties    

11/08/22 07:01:04 (065) Credential: org.opensaml.security.x509.BasicX509Credential@457db7    

11/08/22 07:01:04 (076) SAML Request xml: <saml2p:LogoutRequest xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol" Destination="https://adfs01.rcw.com/adfs/ls/" ID="SNC3d520f9fdbcdbc83ea5dbd75c425c5e1" IssueInstant="2022-11-08T15:01:03.543Z" Version="2.0"><saml2:Issuer xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">https://dev130499.service-now.com</saml2:Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">    

<ds:SignedInfo>    

<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>    

<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>    

<ds:Reference URI="#SNC3d520f9fdbcdbc83ea5dbd75c425c5e1">    

<ds:Transforms>    

<ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>    

<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>    

</ds:Transforms>    

<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>    

<ds:DigestValue>Svi2xMjFwDlH6GSFoNwZ+eKVowb15ULQ+F4uz9ILsAU=</ds:DigestValue>    

</ds:Reference>    

</ds:SignedInfo>    

<ds:SignatureValue>    

rfZ38NSPmniz+ArJh6yU8lioh4OcrQ7fhVmKqzBIufUzS3Q7y7UgoiojJikoJEyZ+OKQ3FcNHcdY    

Z9lZG2m2WzZ0BRATaMsdhGD6kUDrdqNXQwi8eHf1OAmqyaPAFGRsfHB38twuCzcYAtItPTmT8kj5    

6DS2nDx0RezCriGwwTcK7ujHpLV7Y+kmrdTdg16vNHOJDr0llau8D+vaRCOHGnQjtw+tvMmXhiiv    

QGimYrfZRcDOWePBK/+UXhWPwYxmHnNgZEZACn2S1bBhAjOx/IDy5sEAhcjSfl6jFa40Z6BqL4gI    

JtEdnsIssJPtF1UrDfZnPZe8lilkvM5YU9oXnA==    

</ds:SignatureValue>    

<ds:KeyInfo><ds:X509Data><ds:X509Certificate>MIIDoTCCAomgAwIBAgIERs1yFjANBgkqhkiG9w0BAQsFADCBgDELMAkGA1UEBhMCVVMxCzAJBgNV    

BAgTAkNBMRQwEgYDVQQHEwtTYW50YSBDbGFyYTETMBEGA1UEChMKU2VydmljZU5vdzEdMBsGA1UE    

CxMUUGxhdGZvcm0gRGV2ZWxvcG1lbnQxGjAYBgNVBAMTEVBsYXRmb3JtIFNlY3VyaXR5MB4XDTE2    

MDMwOTIyNTYyMVoXDTI2MDMwNzIyNTYyMVowgYAxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEU    

MBIGA1UEBxMLU2FudGEgQ2xhcmExEzARBgNVBAoTClNlcnZpY2VOb3cxHTAbBgNVBAsTFFBsYXRm    

b3JtIERldmVsb3BtZW50MRowGAYDVQQDExFQbGF0Zm9ybSBTZWN1cml0eTCCASIwDQYJKoZIhvcN    

AQEBBQADggEPADCCAQoCggEBAMdREVxdscrxy9ap/UnDsdihJjoKxY6qpxvLUHUGKjTsSNNu/6Fd    

hh4y5hkYLklY0vEdXStqwvqJjqiCn1LPPo/WjWBAv1kVZXiA0pbaxRaX0wtQ2zo4ddIpCc6/UFOZ    

QxPTk+974KPKiA9wDa9/mSqfLfzPmDrSPGLvbiQACTHozLTXxMv+z7pJg77muWIHet5pdrUThF9w    

8iANYTRie+dl+LxEyF5U5tdQXlFgRo5qBQQvSDVL+FbjiX+XllNLwP2RX7IwZChxi6B8dgkAuXTX    

dII309L9NXy3E8pefhAJgSe5FnkGaQk/HlqOBtgKdp9/Rf5Uy6fz0ZJmEqKzM+8CAwEAAaMhMB8w    

HQYDVR0OBBYEFNF7CaQY7kZQM5ulSV8bOAl2mgdNMA0GCSqGSIb3DQEBCwUAA4IBAQC+f3HXbp/2    

IaF/bmUICCkVragGpX4IslJPxjdShUA7qwIZ8YNZZHT9R8bRrcOIRy83fKiXDmlWYSgiuA3cckH4    

WSvwCHOCSi0H72/L9QRjqcrlzpzoCFP1v57tzGOPyAsRr/kU7v01g6bCKlnXPhXpX6EA5m0h37vQ    

rV++9aXSiThRbatOkRVow4NohbkVZA8zhn6kxSI3nwM1xRO30dtb8iQGo/2/J9d2pzLKnvC3pFVF    

W7GRabHJ8Zv5k/9f45/9F8l/9+v8g+OaqEdQuAdymHbeFQ732vd/4MuJWHylQGcyQz7ytJUqr7j4    

epX6Li/sQdXGaLxLM+rEKFMY7uB/</ds:X509Certificate></ds:X509Data></ds:KeyInfo></ds:Signature><saml2:NameID xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion" Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">@rcw.com</saml2:NameID>saml2p:SessionIndex_6be43188-e46e-44f1-8950-2f0862565e8b</saml2p:SessionIndex></saml2p:LogoutRequest>    

11/08/22 07:01:04 (077) html post: <html lang="en"><body onload="document.forms[0].submit()"><form method="POST" action="https://adfs01.rcw.com/adfs/ls/"><input type="HIDDEN" name="SAMLRequest" value="PHNhbWwycDpMb2dvdXRSZXF1ZXN0IHhtbG5zOnNhbWwycD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOnByb3RvY29sIiBEZXN0aW5hdGlvbj0iaHR0cHM6Ly9hZGZzMDEucmN3LmNvbS9hZGZzL2xzLyIgSUQ9IlNOQzNkNTIwZjlmZGJjZGJjODNlYTVkYmQ3NWM0MjVjNWUxIiBJc3N1ZUluc3RhbnQ9IjIwMjItMTEtMDhUMTU6MDE6MDMuNTQzWiIgVmVyc2lvbj0iMi4wIj48c2FtbDI6SXNzdWVyIHhtbG5zOnNhbWwyPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIj5odHRwczovL2RldjEzMDQ5OS5zZXJ2aWNlLW5vdy5jb208L3NhbWwyOklzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG5zOmRzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjIj4KPGRzOlNpZ25lZEluZm8+CjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIi8+CjxkczpTaWduYXR1cmVNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNyc2Etc2hhMjU2Ii8+CjxkczpSZWZlcmVuY2UgVVJJPSIjU05DM2Q1MjBmOWZkYmNkYmM4M2VhNWRiZDc1YzQyNWM1ZTEiPgo8ZHM6VHJhbnNmb3Jtcz4KPGRzOlRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNlbnZlbG9wZWQtc2lnbmF0dXJlIi8+CjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiLz4KPC9kczpUcmFuc2Zvcm1zPgo8ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2Ii8+CjxkczpEaWdlc3RWYWx1ZT5TdmkyeE1qRndEbEg2R1NGb053WitlS1Zvd2IxNVVMUStGNHV6OUlMc0FVPTwvZHM6RGlnZXN0VmFsdWU+CjwvZHM6UmVmZXJlbmNlPgo8L2RzOlNpZ25lZEluZm8+CjxkczpTaWduYXR1cmVWYWx1ZT4KcmZaMzhOU1Btbml6K0FySmg2eVU4bGlvaDRPY3JRN2ZoVm1LcXpCSXVmVXpTM1E3eTdVZ29pb2pKaWtvSkV5WitPS1EzRmNOSGNkWSYjMTM7Clo5bFpHMm0yV3paMEJSQVRhTXNkaEdENmtVRHJkcU5YUXdpOGVIZjFPQW1xeWFQQUZHUnNmSEIzOHR3dUN6Y1lBdEl0UFRtVDhrajUmIzEzOwo2RFMybkR4MFJlekNyaUd3d1RjSzd1akhwTFY3WStrbXJkVGRnMTZ2TkhPSkRyMGxsYXU4RCt2YVJDT0hHblFqdHcrdHZNbVhoaWl2JiMxMzsKUUdpbVlyZlpSY0RPV2VQQksvK1VYaFdQd1l4bUhuTmdaRVpBQ24yUzFiQmhBak94L0lEeTVzRUFoY2pTZmw2akZhNDBaNkJxTDRnSSYjMTM7Ckp0RWRuc0lzc0pQdEYxVXJEZlpuUFplOGxpbGt2TTVZVTlvWG5BPT0KPC9kczpTaWduYXR1cmVWYWx1ZT4KPGRzOktleUluZm8+PGRzOlg1MDlEYXRhPjxkczpYNTA5Q2VydGlmaWNhdGU+TUlJRG9UQ0NBb21nQXdJQkFnSUVSczF5RmpBTkJna3Foa2lHOXcwQkFRc0ZBRENCZ0RFTE1Ba0dBMVVFQmhNQ1ZWTXhDekFKQmdOVgpCQWdUQWtOQk1SUXdFZ1lEVlFRSEV3dFRZVzUwWVNCRGJHRnlZVEVUTUJFR0ExVUVDaE1LVTJWeWRtbGpaVTV2ZHpFZE1Cc0dBMVVFCkN4TVVVR3hoZEdadmNtMGdSR1YyWld4dmNHMWxiblF4R2pBWUJnTlZCQU1URVZCc1lYUm1iM0p0SUZObFkzVnlhWFI1TUI0WERURTIKTURNd09USXlOVFl5TVZvWERUSTJNRE13TnpJeU5UWXlNVm93Z1lBeEN6QUpCZ05WQkFZVEFsVlRNUXN3Q1FZRFZRUUlFd0pEUVRFVQpNQklHQTFVRUJ4TUxVMkZ1ZEdFZ1EyeGhjbUV4RXpBUkJnTlZCQW9UQ2xObGNuWnBZMlZPYjNjeEhUQWJCZ05WQkFzVEZGQnNZWFJtCmIzSnRJRVJsZG1Wc2IzQnRaVzUwTVJvd0dBWURWUVFERXhGUWJHRjBabTl5YlNCVFpXTjFjbWwwZVRDQ0FTSXdEUVlKS29aSWh2Y04KQVFFQkJRQURnZ0VQQURDQ0FRb0NnZ0VCQU1kUkVWeGRzY3J4eTlhcC9VbkRzZGloSmpvS3hZNnFweHZMVUhVR0tqVHNTTk51LzZGZApoaDR5NWhrWUxrbFkwdkVkWFN0cXd2cUpqcWlDbjFMUFBvL1dqV0JBdjFrVlpYaUEwcGJheFJhWDB3dFEyem80ZGRJcENjNi9VRk9aClF4UFRrKzk3NEtQS2lBOXdEYTkvbVNxZkxmelBtRHJTUEdMdmJpUUFDVEhvekxUWHhNdit6N3BKZzc3bXVXSUhldDVwZHJVVGhGOXcKOGlBTllUUmllK2RsK0x4RXlGNVU1dGRRWGxGZ1JvNXFCUVF2U0RWTCtGYmppWCtYbGxOTHdQMlJYN0l3WkNoeGk2QjhkZ2tBdVhUWApkSUkzMDlMOU5YeTNFOHBlZmhBSmdTZTVGbmtHYVFrL0hscU9CdGdLZHA5L1JmNVV5NmZ6MFpKbUVxS3pNKzhDQXdFQUFhTWhNQjh3CkhRWURWUjBPQkJZRUZORjdDYVFZN2taUU01dWxTVjhiT0FsMm1nZE5NQTBHQ1NxR1NJYjNEUUVCQ3dVQUE0SUJBUUMrZjNIWGJwLzIKSWFGL2JtVUlDQ2tWcmFnR3BYNElzbEpQeGpkU2hVQTdxd0laOFlOWlpIVDlSOGJScmNPSVJ5ODNmS2lYRG1sV1lTZ2l1QTNjY2tINApXU3Z3Q0hPQ1NpMEg3Mi9MOVFSanFjcmx6cHpvQ0ZQMXY1N3R6R09QeUFzUnIva1U3djAxZzZiQ0tsblhQaFhwWDZFQTVtMGgzN3ZRCnJWKys5YVhTaVRoUmJhdE9rUlZvdzROb2hia1ZaQTh6aG42a3hTSTNud00xeFJPMzBkdGI4aVFHby8yL0o5ZDJwekxLbnZDM3BGVkYKVzdHUmFiSEo4WnY1ay85ZjQ1LzlGOGwvOSt2OGcrT2FxRWRRdUFkeW1IYmVGUTczMnZkLzRNdUpXSHlsUUdjeVF6N3l0SlVxcjdqNAplcFg2TGkvc1FkWEdhTHhMTStyRUtGTVk3dUIvPC9kczpYNTA5Q2VydGlmaWNhdGU+PC9kczpYNTA5RGF0YT48L2RzOktleUluZm8+PC9kczpTaWduYXR1cmU+PHNhbWwyOk5hbWVJRCB4bWxuczpzYW1sMj0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiIgRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoxLjE6bmFtZWlkLWZvcm1hdDplbWFpbEFkZHJlc3MiPnN2Yy1hZGZzQHJjdy5jb208L3NhbWwyOk5hbWVJRD48c2FtbDJwOlNlc3Npb25JbmRleD5fNmJlNDMxODgtZTQ2ZS00NGYxLTg5NTAtMmYwODYyNTY1ZThiPC9zYW1sMnA6U2Vzc2lvbkluZGV4Pjwvc2FtbDJwOkxvZ291dFJlcXVlc3Q+" /><input type="HIDDEN" name="RelayState" value="https://dev130499.service-now.com/navpage.doSNCRSEPsysparm_saml_tc=true&glide_sso_id=dc33b505970f1110c4a735dfe153af57&exit_name=MultiSSOv2" /></form></body></html>    

11/08/22 07:01:04 (078) Generated Request : <html lang="en"><body onload="document.forms[0].submit()"><form method="POST" action="https://adfs01.rcw.com/adfs/ls/"><input type="HIDDEN" name="SAMLRequest" value="PHNhbWwycDpMb2dvdXRSZXF1ZXN0IHhtbG5zOnNhbWwycD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOnByb3RvY29sIiBEZXN0aW5hdGlvbj0iaHR0cHM6Ly9hZGZzMDEucmN3LmNvbS9hZGZzL2xzLyIgSUQ9IlNOQzNkNTIwZjlmZGJjZGJjODNlYTVkYmQ3NWM0MjVjNWUxIiBJc3N1ZUluc3RhbnQ9IjIwMjItMTEtMDhUMTU6MDE6MDMuNTQzWiIgVmVyc2lvbj0iMi4wIj48c2FtbDI6SXNzdWVyIHhtbG5zOnNhbWwyPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIj5odHRwczovL2RldjEzMDQ5OS5zZXJ2aWNlLW5vdy5jb208L3NhbWwyOklzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG5zOmRzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjIj4KPGRzOlNpZ25lZEluZm8+CjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmc

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-11-07*

The error message is in the trace:    

```
samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:InvalidNameIDPolicy"
```

You are requesting a NameID `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` but you do not issue it.     

You probably haven't configured a NameID in the list of claims you are issuing.     

Edit your relaying party and add the following Transform rule:
