#
# Conditional build:
# _with_tests - perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBI
%define	pnam	DBI
Summary:	DBI - Database independent interface for Perl
Summary(pl):	DBI - niezale¿ny interfejs baz danych dla perla
Name:		perl-DBI
Version:	1.30
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl-PlRPC
BuildRequires:	perl-Storable
BuildRequires:	perl-Net-Daemon
%endif
Obsoletes:	perl-DBI-FAQ
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::<foo>)' 'perl(DBI::Format)' 'perl(DBI::PurePerl)'

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide
a consistent database interface, independent of the actual database
being used.

%description -l pl
DBI jest modu³em dostêpu do baz danych dla Perla.  Definiuje grupê metod,
zmiennych i konwencji, zapewniaj±cych spójny interfejs do baz danych,
niezale¿ny od typu aktualnie u¿ywanej bazy.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_sitelib}/DBIx,%{perl_sitearch}/auto/DBD}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%attr(755,root,root) %{_bindir}/*
%dir %{perl_sitelib}/DBIx
%{perl_sitearch}/DBI.pm
%{perl_sitearch}/DBI
%{perl_sitearch}/DBD
%dir %{perl_sitearch}/auto/DBD
%dir %{perl_sitearch}/auto/DBI
%{perl_sitearch}/auto/DBI/*.h
%{perl_sitearch}/auto/DBI/Driver.xst
%{perl_sitearch}/auto/DBI/DBI.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBI/DBI.so
%{_mandir}/man1/*
%{_mandir}/man3/D*
