Summary:	ne, the nice editor
Summary(pl):	ne - ciekawy edytor tekstu
Name:		ne
Version:	1.35
Release:	2
License:	GPL
Group:		Applications/Editors
Source0:	http://ne.dsi.unimi.it/%{name}-%{version}.tar.gz
# Source0-md5:	dfdec289ec522f3987596d2a43a02149
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ne is a free (GPL'd) text editor based on the POSIX standard that runs
(we hope) on almost any UN*X machine. ne is easy to use for the
beginner, but powerful and fully configurable for the wizard, and most
sparing in its resource usage. If you have the resources and the
patience to use emacs or the right mental twist to use vi then
probably ne is not for you. However, being fast, small, powerful and
simple to use, ne is ideal for email, editing through phone line (or
slow GSM/GPRS) connections and so on. Moreover, the internal text
representation is very compact--you can easily load and modify very
large files.

%description -l pl
ne jest wolnym (na licencji GPL) edytorem tekstu bazuj±cym na
standardzie POSIX który mo¿na uruchomiæ na prawie ka¿dej maszynie
UN*Xowej. ne jest ³atwy do u¿ycia dla pocz±tkuj±cych, ale potê¿ny i
³atwo konfigurowalny dla czarodziejów, oraz oszczêdny w u¿yciu
zasobów. Je¿eli masz zasoby aby u¿yæ emacsa lub potrzebê korzystania z
vi, wtedy ne prawdopodobnie nie jest dla ciebie. Mimo to, bêd±c
szybkim, ma³ym, potê¿nym i ³atwym w u¿yciu jest idealny dla poczty,
edycji poprzez linie telefoniczne (lub wolny GSM/GPRS) itp. Co wiêcej,
wewnêtrzna reprezentacja tekstu jest bardzo skondensowana - mo¿esz
³atwo odczytywaæ i modyfikowaæ nawet bardzo du¿e pliki.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="-D_POSIX_C_SOURCE=199506L -DNODEBUG %{rpmcflags} -I%{_includedir}/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

install -m 755 ./src/ne $RPM_BUILD_ROOT%{_bindir}/ne
install doc/ne.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/ne.info* $RPM_BUILD_ROOT%{_infodir}
rm -f doc/ne.1 doc/ne.info*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES terms
%attr(755,root,root) %{_bindir}/ne
%{_mandir}/man?/ne.1*
%{_infodir}/ne.info*
