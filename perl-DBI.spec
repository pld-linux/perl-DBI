#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBI
%define	pnam	DBI
Summary:	DBI - Database independent interface for Perl
Summary(pl):	DBI - niezale¿ny interfejs baz danych dla perla
Name:		perl-DBI
Version:	1.32
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
DBI jest modu³em dostêpu do baz danych dla Perla.  Definiuje grupê metod,
zmiennych i konwencji, zapewniaj±cych spójny interfejs do baz danych,
niezale¿ny od typu aktualnie u¿ywanej bazy.

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
%{perl_vendorarch}/DBD
%dir %{perl_vendorarch}/auto/DBD
%dir %{perl_vendorarch}/auto/DBI
%{perl_vendorarch}/auto/DBI/*.h
%{perl_vendorarch}/auto/DBI/Driver.xst
%{perl_vendorarch}/auto/DBI/DBI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBI/DBI.so
%{_mandir}/man1/*
%{_mandir}/man3/D*
