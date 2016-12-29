Name     : jdk-trilead-ssh2
Version  : 217.8
Release  : 1
URL      : https://github.com/jenkinsci/trilead-ssh2/archive/trilead-ssh2-build217-jenkins-8.tar.gz
Source0  : https://github.com/jenkinsci/trilead-ssh2/archive/trilead-ssh2-build217-jenkins-8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-junit4
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-surefire
BuildRequires : jdk-hamcrest
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-log4j
BuildRequires : jdk-xbean
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-plexus-io
BuildRequires : jdk-commons-compress
BuildRequires : jdk-snappy-java
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-xmlunit
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-velocity
BuildRequires : jdk-commons-collections
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-plexus-compiler
BuildRequires : apache-maven2

%description
Trilead SSH-2 for Java - build 212
==================================
http://www.trilead.com

%prep
%setup -q -n trilead-ssh2-trilead-ssh2-build217-jenkins-8

python3 /usr/share/java-utils/mvn_file.py  : trilead-ssh2/trilead-ssh2 trilead-ssh2
python3 /usr/share/java-utils/mvn_alias.py : "org.tmatesoft.svnkit:trilead-ssh2" "com.trilead:trilead-ssh2"

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n trilead-ssh2 -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/trilead-ssh2.jar
/usr/share/java/trilead-ssh2/trilead-ssh2.jar
/usr/share/maven-metadata/trilead-ssh2.xml
/usr/share/maven-poms/trilead-ssh2.pom
/usr/share/maven-poms/trilead-ssh2/trilead-ssh2.pom
