#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBI
%define	pnam	DBI
Summary:	DBI - database independent interface for Perl
Summary(cs):	API pro pøístup k databázím pro Perl
Summary(da):	En database-API for Perl
Summary(de):	Ein API Datenbankzugriff für Perl
Summary(es):	Acceso de base de datos API para Perl
Summary(fr):	Une IPA pour l'accès aux bases de données pour Perl
Summary(it):	API di accesso a database per Perl
Summary(ja):	Perl ÍÑ¥Ç¡¼¥¿¥Ù¡¼¥¹¥¢¥¯¥»¥¹ API
Summary(ko):	ÆŞ¿¡ »ç¿ëµÇ´Â µ¥ÀÌÅ¸º£ÀÌ½º ¾×¼¼½º API
Summary(nb):	Et database-API for Perl
Summary(pl):	DBI - niezale¿ny interfejs baz danych dla perla
Summary(pt):	Uma API de acesso a bases de dados para o Perl
Summary(pt_BR):	Uma API de acesso a bases de dados para o Perl
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÄÌÑ ÄÏÓÔÕĞÁ Ë ÂÁÚÁÍ ÄÁÎÎÙÈ ÄÌÑ Perl
Summary(sv):	Ett databasåtkomst-API för Perl
Summary(zh_CN):	Perl µÄÊı¾İ¿â·ÃÎÊ API¡£
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
DBI je Application Programming Interface (API) pro pøístup k databázím
pro programovací jazyk Perl. Specifikace DBI API definuje sadu funkcí,
promìnnıch a konvencí, které poskytují konzistentní databázové
rozhraní nezávislé na právì pou¾ité databázi.

%description -l da
DBI er en databaseadgangsprogrammeringsgrænseflade (API) for
programmeringssproget Perl. DBI API-specifikationen definerer et antal
funktioner, variable og konventioner som tilbyder et konsistent
databasegrænseflade uafhængigt af den faktiske database som bruges.

%description -l de
DBI ist ein Datenbankzugriff Application Programming Interface (API)
für die Programmiersprache Perl. Die DBI API Spezifikation definiert
ein Set von Funktionen, Variablen und Konventionen die ein von der
aktuell benutzten Datenbank unabhängiges, konsistentes
Datenbankinterface bereitstellen.

%description -l es
DBI es una interfaz de programación de aplicación del acceso de base
dedatos (API) para el lenguaje de programación de Perl. La
especificación de DBI API define un conjunto de funciones, de
variables y de las convenciones que proporcionan a un interfaz de base
de datos constante independiente de la base de datos real que es
utilizada.

%description -l fr
DBI est une interface de programme d'applications d'accès aux bases de
données (IPA) pour le langage de programmation Perl. La spécification
de l'IPA DBI définit des fonctions, des variables et des conventions
qui fournissent une interface de base de donnée indépendante de la
base de données utilisée.

%description -l it
DBI è un'API (Application Programming Interface) di accesso a database
per il linguaggio di programmazione Perl. La specifica API di DBI
definisce una serie di funzioni, variabili e convenzioni che
forniscono un'interfaccia database conforme e indipendente dal
database in uso.

%description -l ja
DBI ¤Ï Perl ¥×¥í¥°¥é¥ß¥ó¥°¸À¸ìÍÑ¤Î¥Ç¡¼¥¿¥Ù¡¼¥¹¥¢¥¯¥»¥¹ API
(Application Programming Interface) ¤Ç¤¹¡£DBI API ¤Î»ÅÍÍ¤Ï¡¢¼Âºİ¤Ë»ÈÍÑ
¤µ¤ì¤ë¥Ç¡¼¥¿¥Ù¡¼¥¹¤È¤ÏÊÌ¤Î°ì´ÓÀ­¤Î¤¢¤ë¥Ç¡¼¥¿¥Ù¡¼¥¹¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òµ¬
Äê¤¹¤ë´Ø¿ô¡¢ ÊÑ¿ô¡¢Ë¡Â§¤Î¥»¥Ã¥È¤òÄêµÁ¤·¤Ş¤¹¡£

%description -l pl
DBI jest modu³em dostêpu do baz danych dla Perla. Definiuje grupê
metod, zmiennych i konwencji, zapewniaj±cych spójny interfejs do baz
danych, niezale¿ny od typu aktualnie u¿ywanej bazy.

%description -l pt
O DBI é uma API (Application Programming Interface) de acesso a bases
de dados para a linguagem Perl. A especificação da API do DBI define
um conjunto de funções, variáveis e convenções que oferecem uma
interface de bases de dados consistente e independente da base de
dados que é usada para o efeito.

%description -l pt_BR
O DBI é uma API (Application Programming Interface) de acesso a bases
de dados para a linguagem Perl. A especificação da API do DBI define
um conjunto de funções, variáveis e convenções que oferecem uma
interface de bases de dados consistente e independente da base de
dados que é usada para o efeito.

%description -l ru
DBI ÜÔÏ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÄÏÓÔÕĞÁ Ë ÂÁÚÁÍ ÄÁÎÎÙÈ ÄÌÑ ÑÚÙËÁ Perl. DBI API
ÏĞÒÅÄÅÌÑÅÔ ÎÁÂÏÒ ÆÕÎËÃÉÊ, ĞÅÒÅÍÅÎÎÙÈ É ËÏÎ×ÅÒÓÉÊ; ÏÂÅÓĞÅŞÉ×ÁÅÔ
ÎÅÚÁ×ÉÓÉÍÙÊ ÉÎÔÅÒÆÅÊÓ ÂÁÚÙ ÄÁÎÎÙÈ.

%description -l sv
DBI är ett databasåtkomstprogrammeringsgränssnitt (API) för
programmeringsspråket Perl. DBI API-specifikationen definerar ett
antal funktioner, variabler och konventioner som erbjuder ett
konsistent databasgränssnitt oberoende av den faktiska databas som
används.

%description -l zh_CN
DBI ÊÇÓÃÓÚ Perl ±à³ÌÓïÑÔµÄÊı¾İ¿â·ÃÎÊ³ÌĞò±àĞ´½çÃæ (API)¡£ DBI API
Ã÷Ï¸±í¶¨ÒåÁËÒ»×éº¯Êı¡¢±äÁ¿ºÍ¶¨¹æ£¬ËüÃÇÌá¹©ÁËÒ»¸ö¶ÀÁ¢ÓÚÊµ¼Ê±»Ê¹ÓÃµÄÊı¾İ
¿âÖ®ÍâµÄÁ¬¹áµÄÊı¾İ¿â ½çÃæ¡£

%package ProfileDumper-Apache
Summary:	DBI::ProfileDumper::Apache - capture DBI profiling data from Apache/mod_perl
Summary(pl):	DBI::ProfileDumper::Apache - przechwytywanie danych parametryzuj±cych DBI z Apache/mod_perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description ProfileDumper-Apache
This module interfaces DBI::ProfileDumper to Apache/mod_perl. Using
this module you can collect profiling data from mod_perl applications.
It works by creating a DBI::ProfileDumper data file for each Apache
process. These files are created in your Apache log directory. You can
then use dbiprof to analyze the profile files.

%description ProfileDumper-Apache -l pl
Modu³ ten sprzêga DBI::ProfileDumper z Apache/mod_perl. Korzystaj±c z
niego mo¿na pobraæ dane o parametryzacji z aplikacji mod_perl. Dzia³a
on w oparciu o tworzenie przez DBI::ProfileDumper pliku danych dla
ka¿dego procesu Apache'a. Pliki te tworzone s± w katalogu logów
Apache'a. Mo¿na je analizowaæ za pomoc± dbiprof.

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
