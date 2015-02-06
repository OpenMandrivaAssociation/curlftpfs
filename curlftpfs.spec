%define name curlftpfs
%define version 0.9.2
%define release 5

Name:		%name
Version:	%version
Release:	%release
Url:		http://curlftpfs.sourceforge.net/
Summary:	Filesystem for accessing FTP hosts based on FUSE and libcurl
License:	GPL+
Group:		Networking/Other
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	curl-devel, fuse-devel, glib2-devel
Requires:	fuse
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
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-4mdv2011.0
+ Revision: 617482
- the mass rebuild of 2010.0 packages

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.2-3mdv2010.0
+ Revision: 455796
- rebuild for new curl SSL backend

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.9.2-2mdv2010.0
+ Revision: 437167
- rebuild

* Wed Mar 18 2009 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2009.1
+ Revision: 357158
- New version 0.9.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-3mdv2008.1
+ Revision: 170791
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Nicolas Vigier <nvigier@mandriva.com>
    - update license tag

* Sat Jul 07 2007 Nicolas Vigier <nvigier@mandriva.com> 0.9.1-2mdv2008.0
+ Revision: 49359
- add require on fuse (fix bug #31788)

* Wed May 23 2007 Nicolas Vigier <nvigier@mandriva.com> 0.9.1-1mdv2008.0
+ Revision: 30027
- Import curlftpfs

