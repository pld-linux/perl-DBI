%include	/usr/lib/rpm/macros.perl
Summary:	DBI perl module
Summary(pl):	Modu³ perla DBI
Name:		perl-DBI
Version:	1.21
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/DBI-%{version}.tar.gz
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
%setup -q -n DBI-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{perl_sitearch}/DBD
%{perl_sitearch}/Bundle/*.pm
%{perl_sitearch}/DBD/*.pm
%dir %{perl_sitearch}/DBI
%{perl_sitearch}/DBI.pm
%{perl_sitearch}/DBI/*.pm
%dir %{perl_sitearch}/Win32
%{perl_sitearch}/Win32/DBIODBC.pm
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
