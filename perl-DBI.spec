%include	/usr/lib/rpm/macros.perl
Summary:	DBI perl module
Summary(pl):	Modu� perla DBI
Name:		perl-DBI
Version:	1.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/DBI-%{version}.tar.gz
Patch:		perl-DBI-fmt.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-PlRPC
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	perl-DBI-FAQ
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBI - Database independent interface for Perl

%description -l pl
DBI - niezale�ny interfejs bazy danych dla perla

%prep
%setup -q -n DBI-%{version}
%patch -p0

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/DBI/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBI
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ToDo}.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitearch}/Bundle/DBI.pm
%{perl_sitearch}/DBD/*.pm
%{perl_sitearch}/DBI.pm
%{perl_sitearch}/DBI/*.pm
%{perl_sitearch}/Win32/DBIODBC.pm

%{perl_sitearch}/auto/DBI/DBIXS.h
%{perl_sitearch}/auto/DBI/Driver.xst
%{perl_sitearch}/auto/DBI/dbd_xsh.h
%{perl_sitearch}/auto/DBI/dbi_sql.h
%{perl_sitearch}/auto/DBI/.packlist
%{perl_sitearch}/auto/DBI/DBI.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBI/DBI.so

%{_mandir}/man[13]/*
