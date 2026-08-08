---
title: "Setting up an identity provider"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-idp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-idp
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Setting up an identity provider

[id="learning-getting-started-idp"]
= Setting up an identity provider

[role="_abstract"]
To allow users to log in to your newly created cluster, configure an identity provider (IDP). You can choose from multiple supported IDP options, such as GitHub, to manage authentication and access.

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-idp.adoc
[id="learning-getting-started-idp-cli-overview_{context}"]
= Viewing IDP options

[role="_abstract"]
To determine which authentication methods are available for your cluster's users, view your identity provider (IDP) options. You can quickly list these supported configurations by using the {rosa-cli}.

.Procedure
* Before creating your IDP, you can view all IDP options by running the following command:
+
[source,terminal]
----
$ rosa create idp --help
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-idp.adoc
[id="learning-getting-started-idp-github-org_{context}"]
= Creating a GitHub organization

[role="_abstract"]
To use GitHub as your identity provider (IDP), configure an organization within your GitHub account, and set yourself as an administrator.

[TIP]
====
If you are already an administrator in an existing organization and you want to use that organization, skip to the next section "Setting up an IDP with GitHub".
====

.Procedure
. Log in to your GitHub account.
. Click the *+* icon, then click *New Organization*.
+
image::cloud-experts-getting-started-idp-new-org.png[]

. Choose the most applicable plan for your situation or click *Join for free*.

. Enter an organization account name, an email, and whether it is a personal or business account. Then, click *Next*.
+
image::cloud-experts-getting-started-idp-team.png[]

. *Optional:* Add the GitHub IDs of other users to grant additional access to your OpenShift Container Platform cluster. You can also add them later.
. Click *Complete Setup*.
. *Optional:* Enter the requested information on the following page.
. Click *Submit*.
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-idp.adoc
[id="learning-getting-started-idp-creating_{context}"]
= Setting up an IDP with GitHub

[role="_abstract"]
To streamline the login process and allow users to authenticate with their existing credentials, configure GitHub as an identity provider (IDP). This integration simplifies access management across your organization by centralizing user authentication.

.Procedure
. Log in to your GitHub account.
+
[TIP]
====
If you are not an administrator in an existing organization, see the previous section "Creating a GitHub organization".
====
+
. In the terminal, enter the following command to set up the GitHub IDP:
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
// * rosa_learning/creating_cluster_workshop/learning-getting-started-idp.adoc
[id="learning-getting-started-idp-granting-access_{context}"]
= Granting other users access to the cluster

[role="_abstract"]
To grant access to other cluster users, you will need to add their GitHub user ID to the GitHub organization used for this cluster.

.Procedure
. In GitHub, go to the *Your organizations* page.

. Click your *profile icon*, then *Your organizations*. Then click *<your-organization-name>*.  In our example, it is `my-rosa-cluster`.
+
image::cloud-experts-getting-started-idp-org.png[]

. Click *Invite someone*.
+
image::cloud-experts-getting-started-idp-invite.png[]

. Enter the GitHub ID of the new user, select the correct user, and click *Invite*.
. Once the new user accepts the invitation, they will be able to log in to the OpenShift Container Platform cluster using the {hybrid-console-second} link and their GitHub credentials.

[role="_additional-resources"]
== Additional resources

* IDPs supported by OpenShift Container Platform
