# TODO
# - perl(RPC::PlClient) as optional?  If yes, separate /proxy/i to subpackage.
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBI
%define		pnam	DBI
Summary:	DBI - database independent interface for Perl
Summary(cs):	API pro pøístup k databázím pro Perl
Summary(da):	En database-API for Perl
Summary(de):	Ein API Datenbankzugriff für Perl
Summary(es):	Acceso de base de datos API para Perl
Summary(fr):	Une IPA pour l'accès aux bases de données pour Perl
Summary(it):	API di accesso a database per Perl
Summary(ja):	Perl ÍÑ¥Ç¡¼¥¿¥Ù¡¼¥¹¥¢¥¯¥»¥¹ API
Summary(ko):	ÆÞ¿¡ »ç¿ëµÇ´Â µ¥ÀÌÅ¸º£ÀÌ½º ¾×¼¼½º API
Summary(nb):	Et database-API for Perl
Summary(pl):	DBI - niezale¿ny interfejs baz danych dla Perla
Summary(pt):	Uma API de acesso a bases de dados para o Perl
Summary(pt_BR):	Uma API de acesso a bases de dados para o Perl
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÄÌÑ ÄÏÓÔÕÐÁ Ë ÂÁÚÁÍ ÄÁÎÎÙÈ ÄÌÑ Perl
Summary(sv):	Ett databasåtkomst-API för Perl
Summary(zh_CN):	Perl µÄÊý¾Ý¿â·ÃÎÊ API¡£
Name:		perl-DBI
Version:	1.53
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	e76dfeeb37eb7346342a49142d36171d
Patch0:		%{name}-changes.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Net-Daemon
BuildRequires:	perl-PlRPC
%endif
Obsoletes:	perl-DBI-FAQ
Conflicts:	perl-DBD-CSV < 1:0.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DBD::<foo>)' 'perl(DBI::Format)' 'perl(DBI::PurePerl)' 'perl(DBI)' 'perl(DBI::.*)'
%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.

%description -l cs
DBI je Application Programming Interface (API) pro pøístup k databázím
pro programovací jazyk Perl. Specifikace DBI API definuje sadu funkcí,
promìnných a konvencí, které poskytují konzistentní databázové
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
(Application Programming Interface) ¤Ç¤¹¡£DBI API ¤Î»ÅÍÍ¤Ï¡¢¼ÂºÝ¤Ë»ÈÍÑ
¤µ¤ì¤ë¥Ç¡¼¥¿¥Ù¡¼¥¹¤È¤ÏÊÌ¤Î°ì´ÓÀ­¤Î¤¢¤ë¥Ç¡¼¥¿¥Ù¡¼¥¹¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òµ¬
Äê¤¹¤ë´Ø¿ô¡¢ ÊÑ¿ô¡¢Ë¡Â§¤Î¥»¥Ã¥È¤òÄêµÁ¤·¤Þ¤¹¡£

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
DBI ÜÔÏ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÄÏÓÔÕÐÁ Ë ÂÁÚÁÍ ÄÁÎÎÙÈ ÄÌÑ ÑÚÙËÁ Perl. DBI API
ÏÐÒÅÄÅÌÑÅÔ ÎÁÂÏÒ ÆÕÎËÃÉÊ, ÐÅÒÅÍÅÎÎÙÈ É ËÏÎ×ÅÒÓÉÊ; ÏÂÅÓÐÅÞÉ×ÁÅÔ
ÎÅÚÁ×ÉÓÉÍÙÊ ÉÎÔÅÒÆÅÊÓ ÂÁÚÙ ÄÁÎÎÙÈ.

%description -l sv
DBI är ett databasåtkomstprogrammeringsgränssnitt (API) för
programmeringsspråket Perl. DBI API-specifikationen definerar ett
antal funktioner, variabler och konventioner som erbjuder ett
konsistent databasgränssnitt oberoende av den faktiska databas som
används.

%description -l zh_CN
DBI ÊÇÓÃÓÚ Perl ±à³ÌÓïÑÔµÄÊý¾Ý¿â·ÃÎÊ³ÌÐò±àÐ´½çÃæ (API)¡£ DBI API
Ã÷Ï¸±í¶¨ÒåÁËÒ»×éº¯Êý¡¢±äÁ¿ºÍ¶¨¹æ£¬ËüÃÇÌá¹©ÁËÒ»¸ö¶ÀÁ¢ÓÚÊµ¼Ê±»Ê¹ÓÃµÄÊý¾Ý
¿âÖ®ÍâµÄÁ¬¹áµÄÊý¾Ý¿â ½çÃæ¡£

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
%patch0 -p1
mv Roadmap.pod lib/DBI
mv Changes lib/DBI/Changes.pod
echo 'man DBI::Changes' > Changes

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/DBIx,%{perl_vendorarch}/{DBIx,auto/{DBD,DBIx}}}

# no reason to include Bundle::* in rpms
rm -rf $RPM_BUILD_ROOT{%{perl_vendorarch}/Bundle,%{_mandir}/man3/Bundle::*}
rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/DBI/.packlist

# not our os
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/{DBI/W32ODBC,Win32/DBIODBC}.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/{DBI::W32,Win32::DBI}ODBC.3pm
# different format in %doc
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/{TASKS,DBI/{Changes,Roadmap}}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/DBIx
%{perl_vendorarch}/DBI.pm
%dir %{perl_vendorarch}/DBI
%dir %{perl_vendorarch}/DBIx
%{perl_vendorarch}/DBI/Const
%{perl_vendorarch}/DBI/DBD
%{perl_vendorarch}/DBI/SQL
%{perl_vendorarch}/DBI/[DFPS]*.pm
%{perl_vendorarch}/DBD
%dir %{perl_vendorarch}/auto/DBD
%dir %{perl_vendorarch}/auto/DBI
%dir %{perl_vendorarch}/auto/DBIx
%{perl_vendorarch}/auto/DBI/*.h
%{perl_vendorarch}/auto/DBI/Driver.xst
%{perl_vendorarch}/auto/DBI/DBI.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBI/DBI.so
%{_mandir}/man1/*
%{_mandir}/man3/DBD*
%{_mandir}/man3/DBI.3*
%{_mandir}/man3/DBI::Profile.3*
%{_mandir}/man3/DBI::ProfileData.3*
%{_mandir}/man3/DBI::ProfileDumper.3*
%{_mandir}/man3/DBI::ProfileSubs.3pm*
%{_mandir}/man3/DBI::ProxyServer.3*
%{_mandir}/man3/DBI::PurePerl.3*
%{_mandir}/man3/DBI::[!PW]*
%{_mandir}/man3/TASKS.3pm*

%files ProfileDumper-Apache
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/DBI/ProfileDumper
%{perl_vendorarch}/DBI/ProfileDumper/Apache.pm
%{_mandir}/man3/DBI::ProfileDumper::Apache.3*
