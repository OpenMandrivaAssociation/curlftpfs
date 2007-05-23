%define name curlftpfs
%define version 0.9.1
%define release %mkrel 1

Name:		%name
Version:	%version
Release:	%release
Url:		http://curlftpfs.sourceforge.net/
Summary:	CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and libcurl
License:	GPL
Group:		Networking/Other
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	curl-devel, fuse-devel, glib2-devel
Source:		%{name}-%{version}.tar.gz
%description
CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and libcurl.

CurlFtpFS diferentiates itself from other FTP filesystems because it features:

    * SSLv3 and TLSv1 support
    * connecting through tunneling HTTP proxies
    * automatically reconnection if the server times out
    * transform absolute symlinks to point back into the ftp file system

%prep
%setup -q

%build
%configure
make

%install
%makeinstall

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
