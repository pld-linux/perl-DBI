%include	/usr/lib/rpm/macros.perl
%define		pdir	DBI
%define		pnam	DBI
Summary:	DBI Perl module
Summary(cs):	Modul DBI pro Perl
Summary(da):	Perlmodul DBI
Summary(de):	DBI Perl Modul
Summary(es):	Módulo de Perl DBI
Summary(fr):	Module Perl DBI
Summary(it):	Modulo di Perl DBI
Summary(ja):	DBI Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	DBI ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul DBI
Summary(pl):	Modu³ Perla DBI
Summary(pt):	Módulo de Perl DBI
Summary(pt_BR):	Módulo Perl DBI
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl DBI
Summary(sv):	DBI Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl DBI
Summary(zh_CN):	DBI Perl Ä£¿é
Name:		perl-DBI
Version:	1.21
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fmt.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-PlRPC
Obsoletes:	perl-DBI-FAQ
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBI - Database independent interface for Perl

%description -l pl
DBI - niezale¿ny interfejs bazy danych dla perla

%prep
%setup -q -n %{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
%dir %{perl_sitearch}/DBD
%{perl_sitearch}/Bundle
%{perl_sitearch}/DBD/*.pm
%dir %{perl_sitearch}/DBI
%{perl_sitearch}/DBI.pm
%{perl_sitearch}/DBI/*.pm
%dir %{perl_sitearch}/Win32
%{perl_sitearch}/Win32/DBIODBC.pm
%dir %{perl_sitearch}/auto/DBD
%dir %{perl_sitearch}/auto/DBI
%{perl_sitearch}/auto/DBI/DBIXS.h
%{perl_sitearch}/auto/DBI/Driver.xst
%{perl_sitearch}/auto/DBI/dbd_xsh.h
%{perl_sitearch}/auto/DBI/dbi_sql.h
%{perl_sitearch}/auto/DBI/DBI.bs
%{perl_sitearch}/auto/DBI/dbipport.h
%attr(755,root,root) %{perl_sitearch}/auto/DBI/DBI.so
%{_mandir}/man1/*
%{_mandir}/man3/*
