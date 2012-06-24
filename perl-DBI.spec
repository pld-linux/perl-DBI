#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBI
%define	pnam	DBI
Summary:	DBI - database independent interface for Perl
Summary(pl):	DBI - niezale�ny interfejs baz danych dla perla
Name:		perl-DBI
Version:	1.35
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		perl-DBI-changes.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl-PlRPC
BuildRequires:	perl-Storable
BuildRequires:	perl-Net-Daemon
%endif
Obsoletes:	perl-DBI-FAQ
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::<foo>)' 'perl(DBI::Format)' 'perl(DBI::PurePerl)'
%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide
a consistent database interface, independent of the actual database
being used.

%description -l pl
DBI jest modu�em dost�pu do baz danych dla Perla.  Definiuje grup� metod,
zmiennych i konwencji, zapewniaj�cych sp�jny interfejs do baz danych,
niezale�ny od typu aktualnie u�ywanej bazy.

%package ProfileDumper-Apache
Summary:	DBI::ProfileDumper::Apache - capture DBI profiling data from Apache/mod_perl
Summary(pl):	DBI::ProfileDumper::Apache - przechwytywanie danych parametryzuj�cych DBI z Apache/mod_perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description ProfileDumper-Apache
This module interfaces DBI::ProfileDumper to Apache/mod_perl. Using
this module you can collect profiling data from mod_perl applications.
It works by creating a DBI::ProfileDumper data file for each Apache
process. These files are created in your Apache log directory. You can
then use dbiprof to analyze the profile files.

%description ProfileDumper-Apache -l pl
Modu� ten sprz�ga DBI::ProfileDumper z Apache/mod_perl. Korzystaj�c z
niego mo�na pobra� dane o parametryzacji z aplikacji mod_perl. Dzia�a
on w oparciu o tworzenie przez DBI::ProfileDumper pliku danych dla
ka�dego procesu Apache'a. Pliki te tworzone s� w katalogu log�w
Apache'a. Mo�na je analizowa� za pomoc� dbiprof.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/DBIx,%{perl_vendorarch}/auto/DBD}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/DBIx
%{perl_vendorarch}/DBI.pm
%dir %{perl_vendorarch}/DBI
%{perl_vendorarch}/DBI/Const
%{perl_vendorarch}/DBI/[DFPS]*.pm
%{perl_vendorarch}/DBI/DBD
%{perl_vendorarch}/DBD
%dir %{perl_vendorarch}/auto/DBD
%dir %{perl_vendorarch}/auto/DBI
%{perl_vendorarch}/auto/DBI/*.h
%{perl_vendorarch}/auto/DBI/Driver.xst
%{perl_vendorarch}/auto/DBI/DBI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBI/DBI.so
%{_mandir}/man1/*
%{_mandir}/man3/DBD*
%{_mandir}/man3/DBI.*
%{_mandir}/man3/DBI::Profile.*
%{_mandir}/man3/DBI::ProfileData.*
%{_mandir}/man3/DBI::ProfileDumper.*
%{_mandir}/man3/DBI::ProxyServer.*
%{_mandir}/man3/DBI::PurePerl.*
%{_mandir}/man3/DBI::[!PW]*

%files ProfileDumper-Apache
%defattr(644,root,root,755)
%{perl_vendorarch}/DBI/ProfileDumper
%{_mandir}/man3/DBI::ProfileDumper::*
