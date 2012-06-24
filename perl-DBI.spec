#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBI
%define	pnam	DBI
Summary:	DBI - database independent interface for Perl
Summary(cs):	API pro p��stup k datab�z�m pro Perl
Summary(da):	En database-API for Perl
Summary(de):	Ein API Datenbankzugriff f�r Perl
Summary(es):	Acceso de base de datos API para Perl
Summary(fr):	Une IPA pour l'acc�s aux bases de donn�es pour Perl
Summary(it):	API di accesso a database per Perl
Summary(ja):	Perl �ѥǡ����١����������� API
Summary(ko):	�޿� ���Ǵ� ����Ÿ���̽� �׼��� API
Summary(nb):	Et database-API for Perl
Summary(pl):	DBI - niezale�ny interfejs baz danych dla perla
Summary(pt):	Uma API de acesso a bases de dados para o Perl
Summary(pt_BR):	Uma API de acesso a bases de dados para o Perl
Summary(ru):	���������� ��� ������� � ����� ������ ��� Perl
Summary(sv):	Ett databas�tkomst-API f�r Perl
Summary(zh_CN):	Perl �����ݿ���� API��
Name:		perl-DBI
Version:	1.42
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	ca8c8a1a4797d98121b41c1d0a5b3b7c
Patch0:		perl-DBI-changes.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-PlRPC
BuildRequires:	perl-Net-Daemon
%endif
Conflicts:	perl-DBD-CSV < 1:0.21
Obsoletes:	perl-DBI-FAQ
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::<foo>)' 'perl(DBI::Format)' 'perl(DBI::PurePerl)'
%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.

%description -l cs
DBI je Application Programming Interface (API) pro p��stup k datab�z�m
pro programovac� jazyk Perl. Specifikace DBI API definuje sadu funkc�,
prom�nn�ch a konvenc�, kter� poskytuj� konzistentn� datab�zov�
rozhran� nez�visl� na pr�v� pou�it� datab�zi.

%description -l da
DBI er en databaseadgangsprogrammeringsgr�nseflade (API) for
programmeringssproget Perl. DBI API-specifikationen definerer et antal
funktioner, variable og konventioner som tilbyder et konsistent
databasegr�nseflade uafh�ngigt af den faktiske database som bruges.

%description -l de
DBI ist ein Datenbankzugriff Application Programming Interface (API)
f�r die Programmiersprache Perl. Die DBI API Spezifikation definiert
ein Set von Funktionen, Variablen und Konventionen die ein von der
aktuell benutzten Datenbank unabh�ngiges, konsistentes
Datenbankinterface bereitstellen.

%description -l es
DBI es una interfaz de programaci�n de aplicaci�n del acceso de base
dedatos (API) para el lenguaje de programaci�n de Perl. La
especificaci�n de DBI API define un conjunto de funciones, de
variables y de las convenciones que proporcionan a un interfaz de base
de datos constante independiente de la base de datos real que es
utilizada.

%description -l fr
DBI est une interface de programme d'applications d'acc�s aux bases de
donn�es (IPA) pour le langage de programmation Perl. La sp�cification
de l'IPA DBI d�finit des fonctions, des variables et des conventions
qui fournissent une interface de base de donn�e ind�pendante de la
base de donn�es utilis�e.

%description -l it
DBI � un'API (Application Programming Interface) di accesso a database
per il linguaggio di programmazione Perl. La specifica API di DBI
definisce una serie di funzioni, variabili e convenzioni che
forniscono un'interfaccia database conforme e indipendente dal
database in uso.

%description -l ja
DBI �� Perl �ץ���ߥ󥰸����ѤΥǡ����١����������� API
(Application Programming Interface) �Ǥ���DBI API �λ��ͤϡ��ºݤ˻���
�����ǡ����١����Ȥ��̤ΰ�����Τ���ǡ����١������󥿡��ե�������
�ꤹ��ؿ��� �ѿ���ˡ§�Υ��åȤ�������ޤ���

%description -l pl
DBI jest modu�em dost�pu do baz danych dla Perla. Definiuje grup�
metod, zmiennych i konwencji, zapewniaj�cych sp�jny interfejs do baz
danych, niezale�ny od typu aktualnie u�ywanej bazy.

%description -l pt
O DBI � uma API (Application Programming Interface) de acesso a bases
de dados para a linguagem Perl. A especifica��o da API do DBI define
um conjunto de fun��es, vari�veis e conven��es que oferecem uma
interface de bases de dados consistente e independente da base de
dados que � usada para o efeito.

%description -l pt_BR
O DBI � uma API (Application Programming Interface) de acesso a bases
de dados para a linguagem Perl. A especifica��o da API do DBI define
um conjunto de fun��es, vari�veis e conven��es que oferecem uma
interface de bases de dados consistente e independente da base de
dados que � usada para o efeito.

%description -l ru
DBI ��� ���������� ��� ������� � ����� ������ ��� ����� Perl. DBI API
���������� ����� �������, ���������� � ���������; ������������
����������� ��������� ���� ������.

%description -l sv
DBI �r ett databas�tkomstprogrammeringsgr�nssnitt (API) f�r
programmeringsspr�ket Perl. DBI API-specifikationen definerar ett
antal funktioner, variabler och konventioner som erbjuder ett
konsistent databasgr�nssnitt oberoende av den faktiska databas som
anv�nds.

%description -l zh_CN
DBI ������ Perl ������Ե����ݿ���ʳ����д���� (API)�� DBI API
��ϸ������һ�麯���������Ͷ��棬�����ṩ��һ��������ʵ�ʱ�ʹ�õ�����
��֮�����������ݿ� ���档

%package ProfileDumper-Apache
Summary:	DBI::ProfileDumper::Apache - capture DBI profiling data from Apache/mod_perl
Summary(pl):	DBI::ProfileDumper::Apache - przechwytywanie danych parametryzuj�cych DBI z Apache/mod_perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

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
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/DBIx,%{perl_vendorarch}/auto/DBD}

# no reason to include Bundle::* in rpms
rm -rf $RPM_BUILD_ROOT{%{perl_vendorarch}/Bundle,%{_mandir}/man3/Bundle::*}

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
%{perl_vendorarch}/DBI/DBD
%{perl_vendorarch}/DBI/SQL
%{perl_vendorarch}/DBI/[DFPS]*.pm
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
