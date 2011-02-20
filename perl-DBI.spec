#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBI
%define		pnam	DBI
Summary:	DBI - database independent interface for Perl
Summary(cs.UTF-8):	API pro přístup k databázím pro Perl
Summary(da.UTF-8):	En database-API for Perl
Summary(de.UTF-8):	Ein API Datenbankzugriff für Perl
Summary(es.UTF-8):	Acceso de base de datos API para Perl
Summary(fr.UTF-8):	Une IPA pour l'accès aux bases de données pour Perl
Summary(it.UTF-8):	API di accesso a database per Perl
Summary(ja.UTF-8):	Perl 用データベースアクセス API
Summary(ko.UTF-8):	펄에 사용되는 데이타베이스 액세스 API
Summary(nb.UTF-8):	Et database-API for Perl
Summary(pl.UTF-8):	DBI - niezależny interfejs baz danych dla Perla
Summary(pt.UTF-8):	Uma API de acesso a bases de dados para o Perl
Summary(pt_BR.UTF-8):	Uma API de acesso a bases de dados para o Perl
Summary(ru.UTF-8):	Библиотека для доступа к базам данных для Perl
Summary(sv.UTF-8):	Ett databasåtkomst-API för Perl
Summary(zh_CN.UTF-8):	Perl 的数据库访问 API。
Name:		perl-DBI
Version:	1.616
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBI/TIMB/%{pnam}-%{version}.tar.gz
# Source0-md5:	799313e54a693beb635b47918458f7c4
URL:		http://search.cpan.org/dist/DBI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-Daemon
BuildRequires:	perl-PlRPC
%endif
Obsoletes:	perl-DBI-FAQ
Conflicts:	perl-DBD-CSV < 1:0.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::<foo>)' 'perl(DBI)' 'perl(DBI::.*)' 'perl(DBD::File::.*)'
%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.

%description -l cs.UTF-8
DBI je Application Programming Interface (API) pro přístup k databázím
pro programovací jazyk Perl. Specifikace DBI API definuje sadu funkcí,
proměnných a konvencí, které poskytují konzistentní databázové
rozhraní nezávislé na právě použité databázi.

%description -l da.UTF-8
DBI er en databaseadgangsprogrammeringsgrænseflade (API) for
programmeringssproget Perl. DBI API-specifikationen definerer et antal
funktioner, variable og konventioner som tilbyder et konsistent
databasegrænseflade uafhængigt af den faktiske database som bruges.

%description -l de.UTF-8
DBI ist ein Datenbankzugriff Application Programming Interface (API)
für die Programmiersprache Perl. Die DBI API Spezifikation definiert
ein Set von Funktionen, Variablen und Konventionen die ein von der
aktuell benutzten Datenbank unabhängiges, konsistentes
Datenbankinterface bereitstellen.

%description -l es.UTF-8
DBI es una interfaz de programación de aplicación del acceso de base
dedatos (API) para el lenguaje de programación de Perl. La
especificación de DBI API define un conjunto de funciones, de
variables y de las convenciones que proporcionan a un interfaz de base
de datos constante independiente de la base de datos real que es
utilizada.

%description -l fr.UTF-8
DBI est une interface de programme d'applications d'accès aux bases de
données (IPA) pour le langage de programmation Perl. La spécification
de l'IPA DBI définit des fonctions, des variables et des conventions
qui fournissent une interface de base de donnée indépendante de la
base de données utilisée.

%description -l it.UTF-8
DBI è un'API (Application Programming Interface) di accesso a database
per il linguaggio di programmazione Perl. La specifica API di DBI
definisce una serie di funzioni, variabili e convenzioni che
forniscono un'interfaccia database conforme e indipendente dal
database in uso.

%description -l ja.UTF-8
DBI は Perl プログラミング言語用のデータベースアクセス API
(Application Programming Interface) です。DBI API の仕様は、実際に使用
されるデータベースとは別の一貫性のあるデータベースインターフェイスを規
定する関数、 変数、法則のセットを定義します。

%description -l pl.UTF-8
DBI jest modułem dostępu do baz danych dla Perla. Definiuje grupę
metod, zmiennych i konwencji, zapewniających spójny interfejs do baz
danych, niezależny od typu aktualnie używanej bazy.

%description -l pt.UTF-8
O DBI é uma API (Application Programming Interface) de acesso a bases
de dados para a linguagem Perl. A especificação da API do DBI define
um conjunto de funções, variáveis e convenções que oferecem uma
interface de bases de dados consistente e independente da base de
dados que é usada para o efeito.

%description -l pt_BR.UTF-8
O DBI é uma API (Application Programming Interface) de acesso a bases
de dados para a linguagem Perl. A especificação da API do DBI define
um conjunto de funções, variáveis e convenções que oferecem uma
interface de bases de dados consistente e independente da base de
dados que é usada para o efeito.

%description -l ru.UTF-8
DBI это библиотека для доступа к базам данных для языка Perl. DBI API
определяет набор функций, переменных и конверсий; обеспечивает
независимый интерфейс базы данных.

%description -l sv.UTF-8
DBI är ett databasåtkomstprogrammeringsgränssnitt (API) för
programmeringsspråket Perl. DBI API-specifikationen definerar ett
antal funktioner, variabler och konventioner som erbjuder ett
konsistent databasgränssnitt oberoende av den faktiska databas som
används.

%description -l zh_CN.UTF-8
DBI 是用于 Perl 编程语言的数据库访问程序编写界面 (API)。 DBI API
明细表定义了一组函数、变量和定规，它们提供了一个独立于实际被使用的数据
库之外的连贯的数据库 界面。

%package -n perl-DBD-Proxy
Summary:	DBD::Proxy - A proxy driver for the DBI
Summary(pl.UTF-8):	DBD::Proxy - sterownik proxy dla DBI
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-DBD-Proxy
DBD::Proxy is a Perl module for connecting to a database via a remote
DBI driver.

This is of course not needed for DBI drivers which already support
connecting to a remote database, but there are engines which don't
offer network connectivity.

%description -n perl-DBD-Proxy -l pl.UTF-8
DBD::Proxy to moduł Perla służący do łączenia się z bazą danych
poprzez zdalny sterownik DBI.

Nie jest to oczywiście potrzebne dla sterowników DBI które same
obsługują łączenie się ze zdalną bazą danych, ale oprócz nich są
silniki, które nie oferują łączności sieciowej.

%package ProfileDumper-Apache
Summary:	DBI::ProfileDumper::Apache - capture DBI profiling data from Apache/mod_perl
Summary(pl.UTF-8):	DBI::ProfileDumper::Apache - przechwytywanie danych parametryzujących DBI z Apache/mod_perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description ProfileDumper-Apache
This module interfaces DBI::ProfileDumper to Apache/mod_perl. Using
this module you can collect profiling data from mod_perl applications.
It works by creating a DBI::ProfileDumper data file for each Apache
process. These files are created in your Apache log directory. You can
then use dbiprof to analyze the profile files.

%description ProfileDumper-Apache -l pl.UTF-8
Moduł ten sprzęga DBI::ProfileDumper z Apache/mod_perl. Korzystając z
niego można pobrać dane o parametryzacji z aplikacji mod_perl. Działa
on w oparciu o tworzenie przez DBI::ProfileDumper pliku danych dla
każdego procesu Apache'a. Pliki te tworzone są w katalogu logów
Apache'a. Można je analizować za pomocą dbiprof.

%prep
%setup -q -n %{pnam}-%{version}
mv Changes lib/DBI/Changes.pod
echo 'man DBI::Changes' > Changes

mv t/80proxy.t{,-needs-syslog}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/DBIx,%{perl_vendorarch}/{DBIx,auto/{DBD,DBIx}}}

# no reason to include Bundle::* in rpms
%{__rm} -r $RPM_BUILD_ROOT{%{perl_vendorarch}/Bundle,%{_mandir}/man3/Bundle::*}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/DBI/.packlist

# not our os
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/{DBI/W32ODBC,Win32/DBIODBC}.pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/{DBI::W32,Win32::DBI}ODBC.3pm
# already in doc
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/DBI/Changes.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/dbilogstrip
%attr(755,root,root) %{_bindir}/dbiprof
%attr(755,root,root) %{_bindir}/dbiproxy
%dir %{perl_vendorlib}/DBIx
%{perl_vendorarch}/*.pl
%{perl_vendorarch}/DBI.pm
%dir %{perl_vendorarch}/DBI
%dir %{perl_vendorarch}/DBIx
%{perl_vendorarch}/DBI/Const
%{perl_vendorarch}/DBI/DBD
%{perl_vendorarch}/DBI/Gofer
%{perl_vendorarch}/DBI/SQL
%{perl_vendorarch}/DBI/Util
%{perl_vendorarch}/DBI/*.pm
%{perl_vendorarch}/DBD
%dir %{perl_vendorarch}/auto/DBD
%dir %{perl_vendorarch}/auto/DBI
%dir %{perl_vendorarch}/auto/DBIx
%{perl_vendorarch}/auto/DBI/*.h
%{perl_vendorarch}/auto/DBI/Driver.xst
%{perl_vendorarch}/auto/DBI/DBI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBI/DBI.so
%{_mandir}/man1/dbilogstrip.1p*
%{_mandir}/man1/dbiprof.1p*
%{_mandir}/man1/dbiproxy.1p*
%{_mandir}/man3/DBD::*.3pm*
%{_mandir}/man3/DBI*.3pm*

# in subpackages
%exclude %{_mandir}/man3/DBD::Proxy.3pm*
%exclude %{_mandir}/man3/DBI::ProfileDumper::Apache.3pm*
%exclude %{_mandir}/man3/DBI::ProxyServer.3pm*
%exclude %{perl_vendorarch}/DBD/Proxy.pm
%exclude %{perl_vendorarch}/DBI/ProfileDumper/Apache.pm
%exclude %{perl_vendorarch}/DBI/ProxyServer.pm

%files -n perl-DBD-Proxy
%defattr(644,root,root,755)
%{perl_vendorarch}/DBD/Proxy.pm
%{perl_vendorarch}/DBI/ProxyServer.pm
%{_mandir}/man3/DBD::Proxy.3pm*
%{_mandir}/man3/DBI::ProxyServer.3pm*

%files ProfileDumper-Apache
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/DBI/ProfileDumper
%{perl_vendorarch}/DBI/ProfileDumper/Apache.pm
%{_mandir}/man3/DBI::ProfileDumper::Apache.3pm*
