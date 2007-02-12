Summary:	ne, the nice editor
Summary(pl.UTF-8):   ne - niezły edytor
Name:		ne
Version:	1.41
Release:	1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://ne.dsi.unimi.it/%{name}-%{version}.tar.gz
# Source0-md5:	023e68d23a6216e89737ff2b6996aa77
URL:		http://ne.dsi.unimi.it/
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

%description -l pl.UTF-8
ne jest wolnym (na licencji GPL) edytorem tekstu bazującym na
standardzie POSIX który można uruchomić na prawie każdej maszynie
UN*Xowej. ne jest łatwy do użycia dla początkujących, ale potężny i
łatwo konfigurowalny dla czarodziejów, oraz oszczędny w użyciu
zasobów. Jeżeli masz zasoby aby użyć emacsa lub potrzebę korzystania z
vi, wtedy ne prawdopodobnie nie jest dla ciebie. Mimo to, będąc
szybkim, małym, potężnym i łatwym w użyciu jest idealny dla poczty,
edycji poprzez linie telefoniczne (lub wolny GSM/GPRS) itp. Co więcej,
wewnętrzna reprezentacja tekstu jest bardzo skondensowana - możesz
łatwo odczytywać i modyfikować nawet bardzo duże pliki.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="-D_POSIX_C_SOURCE=199506L -DNODEBUG %{rpmcflags} -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

install ./src/ne $RPM_BUILD_ROOT%{_bindir}/ne
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
