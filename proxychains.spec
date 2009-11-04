Summary:	ProxyChains
Name:		proxychains
Version:	3.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/proxychains/%{name}-%{version}.tar.gz
# Source0-md5:	4629c156001ab70aa7e98960eb513148
URL:		http://proxychains.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProxyChains is a program allows you to use SSH, TELNET, VNC, FTP and
any other Internet application from behind HTTP(HTTPS) and SOCKS(4/5)
proxy servers. This "proxifier" provides proxy server support to any
app.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no -devel
rm -f $RPM_BUILD_ROOT%{_libdir}/libproxychains.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libproxychains.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libproxychains.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/proxychains
%attr(755,root,root) %{_bindir}/proxyresolv
%attr(755,root,root) %{_libdir}/libproxychains.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libproxychains.so.3
