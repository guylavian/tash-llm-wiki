---
title: "Tutorial: Setting up an identity provider"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-idp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-idp
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Setting up an identity provider

[id="cloud-experts-getting-started-idp"]
= Tutorial: Setting up an identity provider

[role="_abstract"]
To log in to your cluster, set up an identity provider (IDP). This tutorial uses GitHub as an example IDP. See the full list of IDPs supported by ROSA.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-idp.adoc

[id="cloud-experts-getting-started-idp-creating_{context}"]
= Creating an identiy provider using GitHub

[role="_abstract"]
You need to configure an identity provider to access your cluster.

.Procedure
. View all IDP options, run the following command:
+
[source,terminal]
----
rosa create idp --help
----
+
This tutorial uses GitHub to create your IDP.

. Log in to your GitHub account.
. Create a new GitHub organization where you are an administrator.
+
[TIP]
====
If you are already an administrator in an existing organization and you want to use that organization, skip to step 9.
====
+
Click the *+* icon, then click *New Organization*.
+
image::cloud-experts-getting-started-idp-new-org.png[]

. Choose the most applicable plan for your situation or click *Join for free*.
. Enter an organization account name, an email, and whether it is a personal or business account. Then, click *Next*.
+
image::cloud-experts-getting-started-idp-team.png[]

. *Optional:* Add the GitHub IDs of other users to grant additional access to your ROSA cluster. You can also add them later.
. Click *Complete Setup*.
. *Optional:* Enter the requested information on the following page.
. Click *Submit*.
. Go back to the terminal and enter the following command to set up the GitHub IDP:
+
[source,terminal]
----
rosa create idp --cluster=<cluster name> --interactive
----

. Enter the following values:
+
[source,terminal]
----
Type of identity provider: github
Identity Provider Name: <IDP-name>
Restrict to members of: organizations
GitHub organizations: <organization-account-name>
----

. The CLI will provide you with a link. Copy and paste the link into a browser and press *Enter*. This will fill the required information to register this application for OAuth. You do not need to modify any of the information.
+
image::cloud-experts-getting-started-idp-link.png[]

. Click *Register application*.
+
image::cloud-experts-getting-started-idp-register.png[]

. The next page displays a *Client ID*.  Copy the ID and paste it in the terminal where it asks for *Client ID*.
+
[NOTE]
====
Do not close the tab.
====

. The CLI will ask for a *Client Secret*. Go back in your browser and click *Generate a new client secret*.
+
image::cloud-experts-getting-started-idp-secret.png[]

. A secret is generated for you. Copy your secret because it will never be visible again.

. Paste your secret into the terminal and press *Enter*.
. Leave *GitHub Enterprise Hostname* blank.
. Select *claim*.
. Wait approximately 1 minute for the IDP to be created and the configuration to land on your cluster.
+
image::cloud-experts-getting-started-idp-inputs.png[]

. Copy the returned link and paste it into your browser. The new IDP should be available under your chosen name. Click your IDP and use your GitHub credentials to access the cluster.
+
image::cloud-experts-getting-started-idp-login.png[]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-idp.adoc

[id="cloud-experts-getting-started-idp-granting-other-users_{context}"]
= Granting other users access to the cluster

[role="_abstract"]
To grant access to other cluster user you will need to add their GitHub user ID to the GitHub organization used for this cluster.

.Procedure
. In GitHub, go to the *Your organizations* page.
. Click your *profile icon*, then *Your organizations*. Then click *<your-organization-name>*.  In our example, it is `my-rosa-cluster`.
+
image::cloud-experts-getting-started-idp-org.png[]

. Click *Invite someone*.
+
image::cloud-experts-getting-started-idp-invite.png[]

. Enter the GitHub ID of the new user, select the correct user, and click *Invite*.
. Once the new user accepts the invitation, they will be able to log in to the ROSA cluster using the {hybrid-console-second} link and their GitHub credentials.
