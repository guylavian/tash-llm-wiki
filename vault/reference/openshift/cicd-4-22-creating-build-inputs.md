---
title: "Creating build inputs"
type: reference
domain: openshift
slug: cicd-4-22-creating-build-inputs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/creating-build-inputs
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Creating build inputs

[id="creating-build-inputs"]
= Creating build inputs

Use the following sections for an overview of build inputs, instructions on how
to use inputs to provide source content for builds to operate on, and how to use
build environments and create secrets.

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-define-build-inputs_{context}"]
= Build inputs

[role="_abstract"]
Use different build inputs in OpenShift Container Platform to provide source content for your builds. Understanding the order of precedence helps ensure your builds use the correct sources.

The following build inputs are available and listed in order of precedence:

* Inline Dockerfile definitions
* Content extracted from existing images
* Git repositories
* Binary (Local) inputs
* Input secrets
* External artifacts

[IMPORTANT]
====
The docker build strategy is not supported in OpenShift Container Platform. Therefore, inline Dockerfile definitions are not accepted.
====

You can combine multiple inputs in a single build.
However, as the inline Dockerfile takes precedence, it can overwrite any other file named Dockerfile provided by another input.
Binary (local) input and Git repositories are mutually exclusive inputs.

You can use input secrets when you do not want certain resources or credentials used during a build to be available in the final application image produced by the build, or want to consume a value that is defined in a secret resource. External artifacts can be used to pull in additional files that are not available as one of the other build input types.

When you run a build:

. A working directory is constructed and all input content is placed in the working directory. For example, the input Git repository is cloned into the working directory, and files specified from input images are copied into the working directory using the target path.

. The build process changes directories into the `contextDir`, if one is defined.

. The inline Dockerfile, if any, is written to the current directory.

. The content from the current directory is provided to the build process
for reference by the
Dockerfile, custom builder logic, or
`assemble` script. This means any input content that resides outside the `contextDir` is ignored by the build.

The following example of a source definition includes multiple input types and an explanation of how they are combined. For more details on how each input type is defined, see the specific sections for each input type.

[source,yaml]
----
source:
  git:
    uri: https://github.com/openshift/ruby-hello-world.git
    ref: "master"
  images:
  - from:
      kind: ImageStreamTag
      name: myinputimage:latest
      namespace: mynamespace
    paths:
    - destinationDir: app/dir/injected/dir
      sourcePath: /usr/lib/somefile.jar
  contextDir: "app/dir"
  dockerfile: "FROM centos:7\nRUN yum install -y httpd"
----
where:

`uri`:: Specifies the repository to be cloned into the working directory for the build.
`destinationDir`:: Specifies the repository to be cloned into the working directory for the build.
`contextDir`:: Specifies the working directory for the build becomes `<original_workingdir>/app/dir`.
`dockerFile`:: A Dockerfile with this content is created in `<original_workingdir>/app/dir`, overwriting any existing file with that name.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-dockerfile-source_{context}"]
= Dockerfile source

When you supply a `dockerfile` value, the content of this field is written to disk as a file named `dockerfile`. This is done after other input sources are processed, so if the input source repository contains a Dockerfile in the root directory, it is overwritten with this content.

The source definition is part of the `spec` section in the `BuildConfig`:

[source,yaml]
----
source:
  dockerfile: "FROM centos:7\nRUN yum install -y httpd" <1>
----
<1> The `dockerfile` field contains an inline Dockerfile that is built.

[role="_additional-resources"]
.Additional resources

* The typical use for this field is to provide a Dockerfile to a docker strategy build.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-image-source_{context}"]
= Image source

You can add additional files to the build process with images. Input images are referenced in the same way the `From` and `To` image targets are defined. This means both container images and image stream tags can be referenced. In conjunction with the image, you must provide one or more path pairs to indicate the path of the files or directories to copy the image and the destination to place them in the build context.

The source path can be any absolute path within the image specified. The destination must be a relative directory path. At build time, the image is loaded and the indicated files and directories are copied into the context directory of the build process. This is the same directory into which the source repository content is cloned. If the source path ends in `/.` then the content of the directory is copied, but the directory itself is not created at the destination.

Image inputs are specified in the `source` definition of the `BuildConfig`:

[source,yaml]
----
source:
  git:
    uri: https://github.com/openshift/ruby-hello-world.git
    ref: "master"
  images: <1>
  - from: <2>
      kind: ImageStreamTag
      name: myinputimage:latest
      namespace: mynamespace
    paths: <3>
    - destinationDir: injected/dir <4>
      sourcePath: /usr/lib/somefile.jar <5>
  - from:
      kind: ImageStreamTag
      name: myotherinputimage:latest
      namespace: myothernamespace
    pullSecret: mysecret <6>
    paths:
    - destinationDir: injected/dir
      sourcePath: /usr/lib/somefile.jar
----
<1> An array of one or more input images and files.
<2> A reference to the image containing the files to be copied.
<3> An array of source/destination paths.
<4> The directory relative to the build root where the build process can access the file.
<5> The location of the file to be copied out of the referenced image.
<6> An optional secret provided if credentials are needed to access the input image.
+

.Images that require pull secrets

When using an input image that requires a pull secret, you can link the pull secret to the service account used by the build. By default, builds use the `builder` service account. The pull secret is automatically added to the build if the secret contains a credential that matches the repository hosting the input image. To link a pull secret to the service account used by the build, run:

[source,terminal]
----
$ oc secrets link builder dockerhub
----

[NOTE]
====
This feature is not supported for builds using the custom strategy.
====

.Images on mirrored registries that require pull secrets

When using an input image from a mirrored registry, if you get a `build error: failed to pull image` message, you can resolve the error by using either of the following methods:

* Create an input secret that contains the authentication credentials for the builder image's repository and all known mirrors. In this case, create a pull secret for credentials to the image registry and its mirrors.
* Use the input secret as the pull secret on the `BuildConfig` object.

[role="_additional-resources"]
.Additional resources

* Configuring project-scoped image pull secrets for mirrored registries

// Module included in the following assemblies:
//* builds/creating-build-inputs.adoc

[id="builds-source-code_{context}"]
= Git source

When specified, source code is fetched from the supplied location.

If you supply an inline Dockerfile, it overwrites the Dockerfile in the `contextDir` of the Git repository.

The source definition is part of the `spec` section in the `BuildConfig`:

[source,yaml]
----
source:
  git: <1>
    uri: "https://github.com/openshift/ruby-hello-world"
    ref: "master"
  contextDir: "app/dir" <2>
  dockerfile: "FROM openshift/ruby-22-centos7\nUSER example" <3>
----
<1> The `git` field contains the Uniform Resource Identifier (URI) to the remote Git repository of the source code. You must specify the value of the `ref` field to check out a specific Git reference. A valid `ref` can be a SHA1 tag or a branch name. The default value of the `ref` field is `master`.
<2> The `contextDir` field allows you to override the default location inside the source code repository where the build looks for the application source code. If your application exists inside a sub-directory, you can override the default location (the root folder) using this field.
<3> If the optional `dockerfile` field is provided, it should be a string containing a Dockerfile that overwrites any Dockerfile that may exist in the source repository.

If the `ref` field denotes a pull request, the system uses a `git fetch` operation and then checkout `FETCH_HEAD`.

When no `ref` value is provided, OpenShift Container Platform performs a shallow clone (`--depth=1`). In this case, only the files associated with the most recent commit on the default branch (typically `master`) are downloaded. This results in repositories downloading faster, but without the full commit history. To perform a full `git clone` of the default branch of a specified repository, set `ref` to the name of the default branch (for example `main`).

[WARNING]
====
Git clone operations that go through a proxy that is performing man in the middle (MITM) TLS hijacking or reencrypting of the proxied connection do not work.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-using-proxy-git-cloning_{context}"]
= Using a proxy

If your Git repository can only be accessed using a proxy, you can define the proxy to use in the `source` section of the build configuration. You can configure both an HTTP and HTTPS proxy to use. Both fields are optional. Domains for which no proxying should be performed can also be specified in the `NoProxy` field.

[NOTE]
====
Your source URI must use the HTTP or HTTPS protocol for this to work.
====

[source,yaml]
----
source:
  git:
    uri: "https://github.com/openshift/ruby-hello-world"
    ref: "master"
    httpProxy: http://proxy.example.com
    httpsProxy: https://proxy.example.com
    noProxy: somedomain.com, otherdomain.com
----

[NOTE]
====
For Pipeline strategy builds, given the current restrictions with the Git plugin for Jenkins, any Git operations through the Git plugin do not leverage the HTTP or HTTPS proxy defined in the `BuildConfig`. The Git plugin only uses the proxy configured in the Jenkins UI at the Plugin Manager panel. This proxy is then used for all git interactions within Jenkins, across all jobs.
====

[role="_additional-resources"]
.Additional resources

* You can find instructions on how to configure proxies through the Jenkins UI at JenkinsBehindProxy.

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-adding-source-clone-secrets_{context}"]
= Source clone secrets

Builder pods require access to any Git repositories defined as source for a build. Source clone secrets are used to provide the builder pod with access it would not normally have access to, such as private repositories or repositories with self-signed or untrusted SSL certificates.

The following source clone secret configurations are supported:

* A `.gitconfig` file
* Basic authentication
* SSH key authentication
* Trusted certificate authorities

[NOTE]
====
You can also use combinations of these configurations to meet your specific needs.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-automatically-add-source-clone-secrets_{context}"]
= Automatically adding a source clone secret to a build configuration

When a `BuildConfig` is created, OpenShift Container Platform can automatically populate its source clone secret reference. This behavior allows the resulting builds to automatically use the credentials stored in the referenced secret to authenticate to a remote Git repository, without requiring further configuration.

To use this functionality, a secret containing the Git repository credentials must exist in the namespace in which the `BuildConfig` is later created. This secrets must include one or more annotations prefixed with `build.openshift.io/source-secret-match-uri-`. The value of each of these annotations is a Uniform Resource Identifier (URI) pattern, which is defined as follows. When a `BuildConfig` is created without a source clone secret reference and its Git source URI matches a URI pattern in a secret annotation, OpenShift Container Platform automatically inserts a reference to that secret in the `BuildConfig`.

.Prerequisites

A URI pattern must consist of:

* A valid scheme: `*://`, `git://`, `http://`, `https://` or `ssh://`
* A host: \*` or a valid hostname or IP address optionally preceded by `*.`
* A path: `/\*` or `/` followed by any characters optionally including `*` characters

In all of the above, a `*` character is interpreted as a wildcard.

[IMPORTANT]
====
URI patterns must match Git source URIs which are conformant to RFC3986. Do not include a username (or password) component in a URI pattern.

For example, if you use `ssh://git@bitbucket.atlassian.com:7999/ATLASSIAN jira.git` for a git repository URL, the source secret must be specified as `pass:c[ssh://bitbucket.atlassian.com:7999/*]` (and not `pass:c[ssh://git@bitbucket.atlassian.com:7999/*]`).

[source,terminal]
----
$ oc annotate secret mysecret \
    'build.openshift.io/source-secret-match-uri-1=ssh://bitbucket.atlassian.com:7999/*'
----

====

.Procedure

If multiple secrets match the Git URI of a particular `BuildConfig`, OpenShift Container Platform selects the secret with the longest match. This allows for basic overriding, as in the following example.

The following fragment shows two partial source clone secrets, the first matching any server in the domain `mycorp.com` accessed by HTTPS, and the second overriding access to servers `mydev1.mycorp.com` and `mydev2.mycorp.com`:

[source,yaml]
----
kind: Secret
apiVersion: v1
metadata:
  name: matches-all-corporate-servers-https-only
  annotations:
    build.openshift.io/source-secret-match-uri-1: https://*.mycorp.com/*
data:
  ...
---
kind: Secret
apiVersion: v1
metadata:
  name: override-for-my-dev-servers-https-only
  annotations:
    build.openshift.io/source-secret-match-uri-1: https://mydev1.mycorp.com/*
    build.openshift.io/source-secret-match-uri-2: https://mydev2.mycorp.com/*
data:
  ...
----

* Add a `build.openshift.io/source-secret-match-uri-` annotation to a pre-existing secret using:
+
[source,terminal]
----
$ oc annotate secret mysecret \
    'build.openshift.io/source-secret-match-uri-1=https://*.mycorp.com/*'
----

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-manually-add-source-clone-secrets_{context}"]
= Manually adding a source clone secret

Source clone secrets can be added manually to a build configuration by adding a `sourceSecret` field to the `source` section inside the `BuildConfig` and setting it to the name of the secret that you created. In this example, it is the `basicsecret`.

[source,yaml]
----
apiVersion: "build.openshift.io/v1"
kind: "BuildConfig"
metadata:
  name: "sample-build"
spec:
  output:
    to:
      kind: "ImageStreamTag"
      name: "sample-image:latest"
  source:
    git:
      uri: "https://github.com/user/app.git"
    sourceSecret:
      name: "basicsecret"
  strategy:
    sourceStrategy:
      from:
        kind: "ImageStreamTag"
        name: "python-33-centos7:latest"
----

.Procedure

You can also use the `oc set build-secret` command to set the source clone secret on an existing build configuration.

* To set the source clone secret on an existing build configuration, enter the following command:
+
[source,terminal]
----
$ oc set build-secret --source bc/sample-build basicsecret
----

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-gitconfig-file_{context}"]
= Creating a secret from a .gitconfig file

If the cloning of your application is dependent on a `.gitconfig` file, then you can create a secret that contains it. Add it to the builder service account and then your `BuildConfig`.

.Procedure

* To create a secret from a `.gitconfig` file:

[source,terminal]
----
$ oc create secret generic <secret_name> --from-file=<path/to/.gitconfig>
----

[NOTE]
====
SSL verification can be turned off if `sslVerify=false` is set for the `http`
section in your `.gitconfig` file:

[source,text]
----
[http]
        sslVerify=false
----
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-gitconfig-file-secured-git_{context}"]
= Creating a secret from a .gitconfig file for secured Git

If your Git server is secured with two-way SSL and user name with password, you must add the certificate files to your source build and add references to the certificate files in the `.gitconfig` file.

.Prerequisites

* You must have Git credentials.

.Procedure

Add the certificate files to your source build and add references to the certificate files in the `.gitconfig` file.

. Add the `client.crt`, `cacert.crt`, and `client.key` files to the `/var/run/secrets/openshift.io/source/` folder in the application source code.

. In the `.gitconfig` file for the server, add the `[http]` section shown in the following example:
+
[source,terminal]
----
# cat .gitconfig
----
+
.Example output
[source,terminal]
----
[user]
        name = <name>
        email = <email>
[http]
        sslVerify = false
        sslCert = /var/run/secrets/openshift.io/source/client.crt
        sslKey = /var/run/secrets/openshift.io/source/client.key
        sslCaInfo = /var/run/secrets/openshift.io/source/cacert.crt
----

. Create the secret:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
--from-literal=username=<user_name> \// <1>
--from-literal=password=<password> \// <2>
--from-file=.gitconfig=.gitconfig \
--from-file=client.crt=/var/run/secrets/openshift.io/source/client.crt \
--from-file=cacert.crt=/var/run/secrets/openshift.io/source/cacert.crt \
--from-file=client.key=/var/run/secrets/openshift.io/source/client.key
----
<1> The user's Git user name.
<2> The password for this user.

[IMPORTANT]
====
To avoid having to enter your password again, be sure to specify the source-to-image (S2I) image in your builds. However, if you cannot clone the repository, you must still specify your user name and password to promote the build.
====

[role="_additional-resources"]
.Additional resources

* `/var/run/secrets/openshift.io/source/` folder in the application source code.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-secret-basic-auth_{context}"]
= Creating a secret from source code basic authentication

Basic authentication requires either a combination of `--username` and `--password`, or a token to authenticate against the software configuration management (SCM) server.

.Prerequisites

* User name and password to access the private repository.

.Procedure

. Create the secret first before using the `--username` and `--password` to access the private repository:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --type=kubernetes.io/basic-auth
----
+
. Create a basic authentication secret with a token:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=password=<token> \
    --type=kubernetes.io/basic-auth
----

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-secret-ssh-key-auth_{context}"]
= Creating a secret from source code SSH key authentication

SSH key based authentication requires a private SSH key.

The repository keys are usually located in the `$HOME/.ssh/` directory, and are named `id_dsa.pub`, `id_ecdsa.pub`, `id_ed25519.pub`, or `id_rsa.pub` by default.

.Procedure

. Generate SSH key credentials:
+
[source,terminal]
----
$ ssh-keygen -t ed25519 -C "your_email@example.com"
----
+
[NOTE]
====
Creating a passphrase for the SSH key  prevents OpenShift Container Platform from building. When prompted for a passphrase, leave it blank.
====
+
Two files are created: the public key and a corresponding private key (one of `id_dsa`, `id_ecdsa`, `id_ed25519`, or `id_rsa`). With both of these in place, consult your source control management (SCM) system's manual on how to upload
the public key. The private key is used to access your private repository.
+
. Before using the SSH key to access the private repository, create the secret:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-file=ssh-privatekey=<path/to/ssh/private/key> \
    --from-file=<path/to/known_hosts> \// <1>
    --type=kubernetes.io/ssh-auth
----
<1> Optional: Adding this field enables strict server host key check.
+
[WARNING]
====
Skipping the `known_hosts` file while creating the secret makes the build vulnerable to a potential man-in-the-middle (MITM) attack.
====
+
[NOTE]
====
Ensure that the `known_hosts` file includes an entry for the host of your source code.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-secret-trusted-ca_{context}"]
= Creating a secret from source code trusted certificate authorities

The set of Transport Layer Security (TLS) certificate authorities (CA) that are trusted during a Git clone operation are built into the OpenShift Container Platform infrastructure images. If your Git server uses a self-signed certificate or one signed by an authority not trusted by the image, you can create a secret that contains the certificate or disable TLS verification.

If you create a secret for the CA certificate, OpenShift Container Platform uses it to access your Git server during the Git clone operation. Using this method is significantly more secure than disabling Git SSL verification, which accepts any TLS certificate that is presented.

.Procedure

Create a secret with a CA certificate file.

. If your CA uses Intermediate Certificate Authorities, combine the certificates for all CAs in a `ca.crt` file. Enter the following command:
+
[source,terminal]
----
$ cat intermediateCA.crt intermediateCA.crt rootCA.crt > ca.crt
----

. Create the secret by entering the following command:
+
[source,terminal]
----
$ oc create secret generic mycert --from-file=ca.crt=</path/to/file> <1>
----
<1> You must use the key name `ca.crt`.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-secret-combinations_{context}"]
= Source secret combinations

You can combine the different methods for creating source clone secrets for your specific needs.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-secret-combinations-ssh-gitconfig_{context}"]
= Creating a SSH-based authentication secret with a `.gitconfig` file

You can combine the different methods for creating source clone secrets for your specific needs, such as a SSH-based authentication secret with a `.gitconfig` file.

.Prerequisites

* SSH authentication
* A `.gitconfig` file

.Procedure

* To create a SSH-based authentication secret with a `.gitconfig` file, enter the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-file=ssh-privatekey=<path/to/ssh/private/key> \
    --from-file=<path/to/.gitconfig> \
    --type=kubernetes.io/ssh-auth
----

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-secret-combinations-gitconfig-ca_{context}"]
= Creating a secret that combines a .gitconfig file and CA certificate

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a `.gitconfig` file and certificate authority (CA) certificate.

.Prerequisites

* A `.gitconfig` file
* CA certificate

.Procedure

* To create a secret that combines a `.gitconfig` file and CA certificate, enter the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-file=ca.crt=<path/to/certificate> \
    --from-file=<path/to/.gitconfig>
----

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-source-secret-combinations-basic-auth-ca_{context}"]
= Creating a basic authentication secret with a CA certificate

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a basic authentication and certificate authority (CA) certificate.

.Prerequisites

* Basic authentication credentials
* CA certificate

.Procedure

* To create a basic authentication secret with a CA certificate, enter the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --from-file=ca-cert=</path/to/file> \
    --type=kubernetes.io/basic-auth
----

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-source-secret-combinations-basic-auth-gitconfig_{context}"]
= Creating a basic authentication secret with a Git configuration file

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a basic authentication and a `.gitconfig` file.

.Prerequisites

* Basic authentication credentials
* A `.gitconfig` file

.Procedure

* To create a basic authentication secret with a `.gitconfig` file, enter the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --from-file=</path/to/.gitconfig> \
    --type=kubernetes.io/basic-auth
----

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-source-secret-combinations-basic-auth-gitconfig-ca_{context}"]
= Creating a basic authentication secret with a .gitconfig file and CA certificate

You can combine the different methods for creating source clone secrets for your specific needs, such as a secret that combines a basic authentication, `.gitconfig` file, and certificate authority (CA) certificate.

.Prerequisites

* Basic authentication credentials
* A `.gitconfig` file
* CA certificate

.Procedure

* To create a basic authentication secret with a `.gitconfig` file and CA certificate, enter the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
    --from-literal=username=<user_name> \
    --from-literal=password=<password> \
    --from-file=</path/to/.gitconfig> \
    --from-file=ca-cert=</path/to/file> \
    --type=kubernetes.io/basic-auth
----

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-binary-source_{context}"]
= Binary (local) source

Streaming content from a local file system to the builder is called a `Binary` type build. The corresponding value of `BuildConfig.spec.source.type` is `Binary` for these builds.

This source type is unique in that it is leveraged solely based on your use of the `oc start-build`.

[NOTE]
====
Binary type builds require content to be streamed from the local file system, so automatically triggering a binary type build, like an image change trigger, is not possible. This is because the binary files cannot be provided. Similarly, you cannot launch binary type builds from the web console.
====

To utilize binary builds, invoke `oc start-build` with one of these options:

* `--from-file`: The contents of the file you specify are sent as a binary stream to the builder. You can also specify a URL to a file. Then, the builder stores the data in a file with the same name at the top of the build context.

* `--from-dir` and `--from-repo`: The contents are archived and sent as a binary stream to the builder. Then, the builder extracts the contents of the archive within the build context directory. With `--from-dir`, you can also specify a URL to an archive, which is extracted.

* `--from-archive`: The archive you specify is sent to the builder, where it is extracted within the build context directory. This option behaves the same as `--from-dir`; an archive is created on your host first, whenever the argument to these options is a directory.

In each of the previously listed cases:

* If your `BuildConfig` already has a `Binary` source type defined, it is effectively ignored and replaced by what the client sends.

* If your `BuildConfig` has a `Git` source type defined, it is dynamically disabled, since `Binary` and `Git` are mutually exclusive, and the data in the binary stream provided to the builder takes precedence.

Instead of a file name, you can pass a URL with HTTP or HTTPS schema to `--from-file` and `--from-archive`. When using `--from-file` with a URL, the name of the file in the builder image is determined by the `Content-Disposition` header sent by the web server, or the last component of the URL path if the header is not present. No form of authentication is supported and it is not possible to use custom TLS certificate or disable certificate validation.

When using `oc new-build --binary=true`, the command ensures that the restrictions associated with binary builds are enforced. The resulting `BuildConfig` has a source type of `Binary`, meaning that the only valid way to run a build for this `BuildConfig` is to use `oc start-build` with one of the `--from` options to provide the requisite binary data.

The Dockerfile and `contextDir` source options have special meaning with binary builds.

Dockerfile can be used with any binary build source. If Dockerfile is used and the binary stream is an archive, its contents serve as a replacement Dockerfile to any Dockerfile in the archive. If Dockerfile is used with the `--from-file` argument, and the file argument is named Dockerfile, the value from Dockerfile replaces the value from the binary stream.

In the case of the binary stream encapsulating extracted archive content, the value of the `contextDir` field is interpreted as a subdirectory within the archive, and, if valid, the builder changes into that subdirectory before executing the build.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-input-secrets-configmaps_{context}"]
= Input secrets and config maps

[IMPORTANT]
====
To prevent the contents of input secrets and config maps from appearing in build output container images, use build volumes in your Docker build and source-to-image build strategies.
====

In some scenarios, build operations require credentials or other configuration data to access dependent resources, but it is undesirable for that information to be placed in source control. You can define input secrets and input config maps for this purpose.

For example, when building a Java application with Maven, you can set up a private mirror of Maven Central or JCenter that is accessed by private keys. To download libraries from that private mirror, you have to supply the
following:

. A `settings.xml` file configured with the mirror's URL and connection settings.
. A private key referenced in the settings file, such as `~/.ssh/id_rsa`.

For security reasons, you do not want to expose your credentials in the application image.

This example describes a Java application, but you can use the same approach for adding SSL certificates into the `/etc/ssl/certs` directory, API keys or tokens, license files, and more.

// Module included in the following assemblies:
// * builds/creating-build-inputs.adoc

[id="builds-secrets-overview_{context}"]
= What is a secret?

The `Secret` object type provides a mechanism to hold sensitive information such as passwords, OpenShift Container Platform client configuration files, `dockercfg` files, private source repository credentials, and so on. Secrets decouple sensitive content from the pods. You can mount secrets into containers using a volume plugin or the system can use secrets to perform actions on behalf of a pod.

.YAML Secret Object Definition

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
  namespace: my-namespace
type: Opaque <1>
data: <2>
  username: <username> <3>
  password: <password>
stringData: <4>
  hostname: myapp.mydomain.com <5>
----
<1> Indicates the structure of the secret's key names and values.
<2> The allowable format for the keys in the `data` field must meet the guidelines in the `DNS_SUBDOMAIN` value in the Kubernetes identifiers glossary.
<3> The value associated with keys in the `data` map must be base64 encoded.
<4> Entries in the `stringData` map are converted to base64 and the entry are then moved to the `data` map automatically. This field is write-only. The value is only be returned by the `data` field.
<5> The value associated with keys in the `stringData` map is made up of plain text strings.

[id="builds-secrets-overview-properties_{context}"]
== Properties of secrets

Key properties include:

* Secret data can be referenced independently from its definition.
* Secret data volumes are backed by temporary file-storage facilities (tmpfs) and never come to rest on a node.
* Secret data can be shared within a namespace.

[id="builds-secrets-overview-types_{context}"]
== Types of Secrets

The value in the `type` field indicates the structure of the secret's key names and values. The type can be used to enforce the presence of user names and keys in the secret object. If you do not want validation, use the `opaque` type, which is the default.

Specify one of the following types to trigger minimal server-side validation to ensure the presence of specific key names in the secret data:

* `kubernetes.io/service-account-token`. Uses a service account token.
* `kubernetes.io/dockercfg`. Uses the `.dockercfg` file for required Docker credentials.
* `kubernetes.io/dockerconfigjson`. Uses the `.docker/config.json` file for required Docker credentials.
* `kubernetes.io/basic-auth`. Use with basic authentication.
* `kubernetes.io/ssh-auth`. Use with SSH key authentication.
* `kubernetes.io/tls`. Use with TLS certificate authorities.

Specify `type= Opaque` if you do not want validation, which means the secret does not claim to conform to any convention for key names or values. An `opaque` secret, allows for unstructured `key:value` pairs that can contain arbitrary values.

[NOTE]
====
You can specify other arbitrary types, such as `example.com/my-secret-type`. These types are not enforced server-side, but indicate that the creator of the
secret intended to conform to the key/value requirements of that type.
====

[id="builds-secrets-overview-updates_{context}"]
== Updates to secrets

When you modify the value of a secret, the value used by an already running pod does not dynamically change. To change a secret, you must delete the original pod and create a new pod, in some cases with an identical `PodSpec`.

Updating a secret follows the same workflow as deploying a new container image. You can use the `kubectl rolling-update` command.

The `resourceVersion` value in a secret is not specified when it is referenced. Therefore, if a secret is updated at the same time as pods are starting, the version of the secret that is used for the pod is not defined.

[NOTE]
====
Currently, it is not possible to check the resource version of a secret object that was used when a pod was created. It is planned that pods report this information, so that a controller could restart ones using an old `resourceVersion`. In the interim, do not update the data of existing secrets, but create new ones with distinct names.
====

// Module included in the following assemblies:
// * builds/creating-build-inputs.adoc

[id="builds-creating-secrets_{context}"]
= Creating secrets

You must create a secret before creating the pods that depend on that secret.

When creating secrets:

* Create a secret object with secret data.
* Update the pod service account to allow the reference to the secret.
* Create a pod, which consumes the secret as an environment variable or as a file using a `secret` volume.

.Procedure

* To create a secret object from a JSON or YAML file, enter the following command:
+
[source,terminal]
----
$ oc create -f <filename>
----
+
For example, you can create a secret from your local `.docker/config.json` file:
+
[source,terminal]
----
$ oc create secret generic dockerhub \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
----
+
This command generates a JSON specification of the secret named `dockerhub` and creates the object.
+
.YAML Opaque Secret Object Definition
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque <1>
data:
  username: <username>
  password: <password>
----
+
<1> Specifies an _opaque_ secret.
+
.Docker Configuration JSON File Secret Object Definition
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: aregistrykey
  namespace: myapps
type: kubernetes.io/dockerconfigjson <1>
data:
  .dockerconfigjson:bm5ubm5ubm5ubm5ubm5ubm5ubm5ubmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cgYXV0aCBrZXlzCg== <2>
----
+
<1> Specifies that the secret is using a docker configuration JSON file.
<2> The output of a base64-encoded docker configuration JSON file.

// Module included in the following assemblies:
// * builds/creating-build-inputs.adoc

[id="builds-using-secrets_{context}"]
= Using secrets

After creating secrets, you can create a pod to reference your secret, get logs, and delete the pod.

.Procedure

. Create the pod to reference your secret by entering the following command:
+
[source,terminal]
----
$ oc create -f <your_yaml_file>.yaml
----

. Get the logs by entering the following command:
+
[source,terminal]
----
$ oc logs secret-example-pod
----

. Delete the pod by entering the following command:
+
[source,terminal]
----
$ oc delete pod secret-example-pod
----

[role="_additional-resources"]
.Additional resources

* Example YAML files with secret data:
+
.YAML file of a secret that will create four files
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
data:
  username: <username> # <1>
  password: <password> # <2>
stringData:
  hostname: myapp.mydomain.com # <3>
  secret.properties: |- # <4>
    property1=valueA
    property2=valueB
----
<1> File contains decoded values.
<2> File contains decoded values.
<3> File contains the provided string.
<4> File contains the provided data.
+
.YAML file of a pod populating files in a volume with secret data
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: secret-example-pod
spec:
  containers:
    - name: secret-test-container
      image: busybox
      command: [ "/bin/sh", "-c", "cat /etc/secret-volume/*" ]
      volumeMounts:
          # name must match the volume name below
          - name: secret-volume
            mountPath: /etc/secret-volume
            readOnly: true
  volumes:
    - name: secret-volume
      secret:
        secretName: test-secret
  restartPolicy: Never
----
+
.YAML file of a pod populating environment variables with secret data
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: secret-example-pod
spec:
  containers:
    - name: secret-test-container
      image: busybox
      command: [ "/bin/sh", "-c", "export" ]
      env:
        - name: TEST_SECRET_USERNAME_ENV_VAR
          valueFrom:
            secretKeyRef:
              name: test-secret
              key: username
  restartPolicy: Never
----
+
.YAML file of a `BuildConfig` object that populates environment variables with secret data
[source,yaml]
----
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: secret-example-bc
spec:
  strategy:
    sourceStrategy:
      env:
      - name: TEST_SECRET_USERNAME_ENV_VAR
        valueFrom:
          secretKeyRef:
            name: test-secret
            key: username
----

[id="builds-adding-input-secrets-configmaps_{context}"]
= Adding input secrets and config maps

To provide credentials and other configuration data to a build without placing them in source control, you can define input secrets and input config maps.

In some scenarios, build operations require credentials or other configuration data to access dependent resources. To make that information available without placing it in source control, you can define input secrets and input config maps.

.Procedure

To add an input secret, config maps, or both to an existing `BuildConfig` object:

. If the `ConfigMap` object does not exist, create it by entering the following command:
+
[source,terminal]
----
$ oc create configmap settings-mvn \
    --from-file=settings.xml=<path/to/settings.xml>
----
+
This creates a new config map named `settings-mvn`, which contains the plain text content of the `settings.xml` file.
+
[TIP]
====
You can alternatively apply the following YAML to create the config map:
[source,yaml]
----
apiVersion: core/v1
kind: ConfigMap
metadata:
  name: settings-mvn
data:
  settings.xml: |
    <settings>
    … # Insert maven settings here
    </settings>
----
====

. If the `Secret` object does not exist, create it by entering the following command:
+
[source,terminal]
----
$ oc create secret generic secret-mvn \
    --from-file=ssh-privatekey=<path/to/.ssh/id_rsa> \
    --type=kubernetes.io/ssh-auth
----
+
This creates a new secret named `secret-mvn`, which contains the base64 encoded content of the `id_rsa` private key.
+
[TIP]
====
You can alternatively apply the following YAML to create the input secret:
[source,yaml]
----
apiVersion: core/v1
kind: Secret
metadata:
  name: secret-mvn
type: kubernetes.io/ssh-auth
data:
  ssh-privatekey: |
    # Insert ssh private key, base64 encoded
----
====

. Add the config map and secret to the `source` section in the existing
`BuildConfig` object:
+
[source,yaml]
----
source:
  git:
    uri: https://github.com/wildfly/quickstart.git
  contextDir: helloworld
  configMaps:
    - configMap:
        name: settings-mvn
  secrets:
    - secret:
        name: secret-mvn
----

. To include the secret and config map in a new `BuildConfig` object, enter the following command:
+
[source,terminal]
----
$ oc new-build \
    openshift/wildfly-101-centos7~https://github.com/wildfly/quickstart.git \
    --context-dir helloworld --build-secret “secret-mvn” \
    --build-config-map "settings-mvn"
----
+
During the build, the build process copies the `settings.xml` and `id_rsa` files into the directory where the source code is located. In OpenShift Container Platform S2I builder images, this is the image working directory, which is set using the `WORKDIR` instruction in the `Dockerfile`. If you want to specify another directory, add a `destinationDir` to the definition:
+
[source,yaml]
----
source:
  git:
    uri: https://github.com/wildfly/quickstart.git
  contextDir: helloworld
  configMaps:
    - configMap:
        name: settings-mvn
      destinationDir: ".m2"
  secrets:
    - secret:
        name: secret-mvn
      destinationDir: ".ssh"
----
+
You can also specify the destination directory when creating a new `BuildConfig` object by entering the following command:
+
[source,terminal]
----
$ oc new-build \
    openshift/wildfly-101-centos7~https://github.com/wildfly/quickstart.git \
    --context-dir helloworld --build-secret “secret-mvn:.ssh” \
    --build-config-map "settings-mvn:.m2"
----
+
In both cases, the `settings.xml` file is added to the `./.m2` directory of the build environment, and the `id_rsa` key is added to the `./.ssh` directory.

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-to-image_{context}"]
= Source-to-image strategy

When using a `Source` strategy, all defined input secrets are copied to their respective `destinationDir`. If you left `destinationDir` empty, then the secrets are placed in the working directory of the builder image.

The same rule is used when a `destinationDir` is a relative path. The secrets are placed in the paths that are relative to the working directory of the image. The final directory in the `destinationDir` path is created if it does not exist in the builder image. All preceding directories in the `destinationDir` must exist, or an error will occur.

[NOTE]
====
Input secrets are added as world-writable, have `0666` permissions, and are truncated to size zero after executing the `assemble` script. This means that the secret files exist in the resulting image, but they are empty for security reasons.

Input config maps are not truncated after the `assemble` script completes.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-docker-strategy_{context}"]
= Docker strategy

When using a docker strategy, you can add all defined input secrets into your container image using the `ADD` and `COPY` instructions in your Dockerfile.

If you do not specify the `destinationDir` for a secret, then the files are copied into the same directory in which the Dockerfile is located. If you specify a relative path as `destinationDir`, then the secrets are copied into that directory, relative to your Dockerfile location. This makes the secret files available to the Docker build operation as part of the context directory used during the build.

.Example of a Dockerfile referencing secret and config map data
----
FROM centos/ruby-22-centos7

USER root
COPY ./secret-dir /secrets
COPY ./config /

# Create a shell script that will output secrets and ConfigMaps when the image is run
RUN echo '#!/bin/sh' > /input_report.sh
RUN echo '(test -f /secrets/secret1 && echo -n "secret1=" && cat /secrets/secret1)' >> /input_report.sh
RUN echo '(test -f /config && echo -n "relative-configMap=" && cat /config)' >> /input_report.sh
RUN chmod 755 /input_report.sh

CMD ["/bin/sh", "-c", "/input_report.sh"]
----

[IMPORTANT]
====
Users normally remove their input secrets from the final application image so that the secrets are not present in the container running from that image. However, the secrets still exist in the image itself in the layer where they were added. This removal is part of the Dockerfile itself.

To prevent the contents of input secrets and config maps from appearing in the build output container images and avoid this removal process altogether, use build volumes in your Docker build strategy instead.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-custom-strategy_{context}"]
= Custom strategy

When using a Custom strategy, all the defined input secrets and config maps are available in the builder container in the `/var/run/secrets/openshift.io/build` directory. The custom build image must use these secrets and config maps appropriately. With the Custom strategy, you can define secrets as described in Custom strategy options.

There is no technical difference between existing strategy secrets and the input secrets. However, your builder image can distinguish between them and use them differently, based on your build use case.

The input secrets are always mounted into the `/var/run/secrets/openshift.io/build` directory, or your builder can parse the `$BUILD` environment variable, which includes the full build object.

[IMPORTANT]
====
If a pull secret for the registry exists in both the namespace and the node, builds default to using the pull secret in the namespace.
====

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-using-external-artifacts_{context}"]
= External artifacts

It is not recommended to store binary files in a source repository. Therefore, you must define a build which pulls additional files, such as Java `.jar` dependencies, during the build process. How this is done depends on the build strategy you are using.

For a Source build strategy, you must put appropriate shell commands into the `assemble` script:

.`.s2i/bin/assemble` File
[source,terminal]
----
#!/bin/sh
APP_VERSION=1.0
wget http://repository.example.com/app/app-$APP_VERSION.jar -O app.jar
----

.`.s2i/bin/run` File
[source,terminal]
----
#!/bin/sh
exec java -jar app.jar
----

For a Docker build strategy, you must modify the Dockerfile and invoke
shell commands with the `RUN` instruction:

.Excerpt of Dockerfile
[source,terminal]
----
FROM jboss/base-jdk:8

ENV APP_VERSION 1.0
RUN wget http://repository.example.com/app/app-$APP_VERSION.jar -O app.jar

EXPOSE 8080
CMD [ "java", "-jar", "app.jar" ]
----

In practice, you may want to use an environment variable for the file location so that the specific file to be downloaded can be customized using an environment variable defined on the `BuildConfig`, rather than updating the
Dockerfile or
`assemble` script.

You can choose between different methods of defining environment variables:

* Using the `.s2i/environment` file (only for a `Source` build strategy)
* Setting the variables in the `BuildConfig` object
* Providing the variables explicitly using the `oc start-build --env` command (only for builds that are triggered manually)

//[role="_additional-resources"]
//.Additional resources
//* For more information on how to control which *_assemble_* and *_run_* script is
//used by a Source build, see Overriding builder image scripts.

// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-docker-credentials-private-registries_{context}"]
= Using docker credentials for private registries

You can supply builds with a .`docker/config.json` file with valid credentials for private container registries. This allows you to push the output image into a private container image registry or pull a builder image from the private container image registry that requires authentication.

You can supply credentials for multiple repositories within the same registry, each with credentials specific to that registry path.

[NOTE]
====
For the OpenShift Container Platform container image registry, this is not required because secrets are generated automatically for you by OpenShift Container Platform.
====

The `.docker/config.json` file is found in your home directory by default and
has the following format:

[source,yaml]
----
auths:
  index.docker.io/v1/: <1>
    auth: "YWRfbGzhcGU6R2labnRib21ifTE=" <2>
    email: "user@example.com" <3>
  docker.io/my-namespace/my-user/my-image: <4>
    auth: "GzhYWRGU6R2fbclabnRgbkSp=""
    email: "user@example.com"
  docker.io/my-namespace: <5>
    auth: "GzhYWRGU6R2deesfrRgbkSp=""
    email: "user@example.com"
----
<1> URL of the registry.
<2> Encrypted password.
<3> Email address for the login.
<4> URL and credentials for a specific image in a namespace.
<5> URL and credentials for a registry namespace.

You can define multiple container image registries or define multiple repositories in the same registry. Alternatively, you can also add authentication entries to this file by running the `docker login` command. The file will be created if it does not exist.

Kubernetes provides `Secret` objects, which can be used to store configuration and passwords.

.Prerequisites

* You must have a `.docker/config.json` file.

.Procedure

. Create the secret from your local `.docker/config.json` file by entering the following command:
+
[source,terminal]
----
$ oc create secret generic dockerhub \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
----
+
This generates a JSON specification of the secret named `dockerhub` and creates the object.
+
. Add a `pushSecret` field into the `output` section of the `BuildConfig` and set it to the name of the `secret` that you created, which in the previous example is `dockerhub`:
+
[source,yaml]
----
spec:
  output:
    to:
      kind: "DockerImage"
      name: "private.registry.com/org/private-image:latest"
    pushSecret:
      name: "dockerhub"
----
+
You can use the `oc set build-secret` command to set the push secret on the build configuration:
+
[source,terminal]
----
$ oc set build-secret --push bc/sample-build dockerhub
----
+
You can also link the push secret to the service account used by the build instead of specifying the `pushSecret` field. By default, builds use the `builder` service account. The push secret is automatically added to the build if the secret contains a credential that matches the repository hosting the build's output image.
+
[source,terminal]
----
$ oc secrets link builder dockerhub
----
+
. Pull the builder container image from a private container image registry by specifying the `pullSecret` field, which is part of the build strategy definition:
+
[source,yaml]
----
strategy:
  sourceStrategy:
    from:
      kind: "DockerImage"
      name: "docker.io/user/private_repository"
    pullSecret:
      name: "dockerhub"
----
+
You can use the `oc set build-secret` command to set the pull secret on the build configuration:
+
[source,terminal]
----
$ oc set build-secret --pull bc/sample-build dockerhub
----
+
[NOTE]
====
This example uses `pullSecret` in a Source build, but it is also applicable in Docker and Custom builds.
====
+
You can also link the pull secret to the service account used by the build instead of specifying the `pullSecret` field. By default, builds use the `builder` service account. The pull secret is automatically added to the build if the secret contains a credential that matches the repository hosting the build's input image. To link the pull secret to the service account used by the build instead of specifying the `pullSecret` field, enter the following command:
+
[source,terminal]
----
$ oc secrets link builder dockerhub
----
+
[NOTE]
====
You must specify a `from` image in the `BuildConfig` spec to take advantage of this feature. Docker strategy builds generated by `oc new-build` or `oc new-app` may not do this in some situations.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-build-environment_{context}"]
= Build environments

As with pod environment variables, build environment variables can be defined in terms of references to other resources or variables using the Downward API. There are some exceptions, which are noted.

You can also manage environment variables defined in the `BuildConfig` with the `oc set env` command.

[NOTE]
====
Referencing container resources using `valueFrom` in build environment variables is not supported as the references are resolved before the container is created.
====

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-using-build-fields-as-environment-variables_{context}"]
= Using build fields as environment variables

You can inject information about the build object by setting the `fieldPath` environment variable source to the `JsonPath` of the field from which you are interested in obtaining the value.

[NOTE]
====
Jenkins Pipeline strategy does not support `valueFrom` syntax for environment variables.
====

.Procedure

* Set the `fieldPath` environment variable source to the `JsonPath` of the field from which you are interested in obtaining the value:
+
[source,yaml]
----
env:
  - name: FIELDREF_ENV
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
----

// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-using-secrets-as-environment-variables_{context}"]
= Using secrets as environment variables

You can make key values from secrets available as environment variables using the `valueFrom` syntax.

[IMPORTANT]
====
This method shows the secrets as plain text in the output of the build pod console. To avoid this, use input secrets and config maps instead.
====

.Procedure

* To use a secret as an environment variable, set the `valueFrom` syntax:
+
[source,yaml]
----
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: secret-example-bc
spec:
  strategy:
    sourceStrategy:
      env:
      - name: MYVAL
        valueFrom:
          secretKeyRef:
            key: myval
            name: mysecret
----

[role="_additional-resources"]
.Additional resources

* Input secrets and config maps

// Module included in the following assemblies:
// * builds/creating-build-inputs.adoc

[id="builds-service-serving-certificate-secrets_{context}"]
= Service serving certificate secrets

Service serving certificate secrets are intended to support complex middleware applications that need out-of-the-box certificates. It has the same settings as the server certificates generated by the administrator tooling for nodes and masters.

.Procedure

To secure communication to your service, have the cluster generate a signed serving certificate/key pair into a secret in your namespace.

* Set the `service.beta.openshift.io/serving-cert-secret-name` annotation on your service with the value set to the name you want to use for your secret.
+
Then, your `PodSpec` can mount that secret. When it is available, your pod runs. The certificate is good for the internal service DNS name, `<service.name>.<service.namespace>.svc`.
+
The certificate and key are in PEM format, stored in `tls.crt` and `tls.key` respectively. The certificate/key pair is automatically replaced when it gets close to expiration. View the expiration date in the `service.beta.openshift.io/expiry` annotation on the secret, which is in RFC3339 format.

[NOTE]
====
In most cases, the service DNS name `<service.name>.<service.namespace>.svc` is not externally routable. The primary use of `<service.name>.<service.namespace>.svc` is for intracluster or intraservice communication, and with re-encrypt routes.
====

Other pods can trust cluster-created certificates, which are only signed for
internal DNS names, by using the certificate authority (CA) bundle in the `/var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt` file that is automatically mounted in their pod.

The signature algorithm for this feature is `x509.SHA256WithRSA`. To manually rotate, delete the generated secret. A new certificate is created.

// Module included in the following assemblies:
// * builds/creating-build-inputs.adoc

[id="builds-secrets-restrictions_{context}"]
= Secrets restrictions

To use a secret, a pod needs to reference the secret. A secret can be used with a pod in three ways:

* To populate environment variables for containers.
* As files in a volume mounted on one or more of its containers.
* By kubelet when pulling images for the pod.

Volume type secrets write data into the container as a file using the volume mechanism. `imagePullSecrets` use service accounts for the automatic injection of the secret into all pods in a namespaces.

When a template contains a secret definition, the only way for the template to use the provided secret is to ensure that the secret volume sources are validated and that the specified object reference actually points to an object of type `Secret`. Therefore, a secret needs to be created before any pods that depend on it. The most effective way to ensure this is to have it get injected automatically through the use of a service account.

Secret API objects reside in a namespace. They can only be referenced by pods in that same namespace.

Individual secrets are limited to 1MB in size. This is to discourage the creation of large secrets that would exhaust apiserver and kubelet memory. However, creation of a number of smaller secrets could also exhaust memory.
