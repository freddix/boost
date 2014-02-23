# TODO: enable openmpi support

%define		fver	%(echo %{version} | tr . _)

Summary:	The Boost C++ Libraries
Name:		boost
Version:	1.55.0
Release:	1
License:	Boost Software License and others
Group:		Libraries
Source0:	http://downloads.sourceforge.net/boost/%{name}_%{fver}.tar.bz2
# Source0-md5:	d6eef4b4cacb2183f2bf265a5a03a354
Patch0:		%{name}-link.patch
URL:		http://www.boost.org/
BuildRequires:	bzip2-devel
BuildRequires:	icu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautochrpath  .*%{_includedir}/.*

%description
The Boost web site provides free peer-reviewed portable C++ source
libraries. The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been proposed for inclusion in the C++ Standards Committee's
upcoming C++ Standard Library Technical Report.

%package devel
Summary:	Boost C++ development headers
Group:		Development/Libraries
Requires:	%{name}-chrono-devel = %{version}-%{release}
Requires:	%{name}-date_time-devel = %{version}-%{release}
Requires:	%{name}-filesystem-devel = %{version}-%{release}
Requires:	%{name}-graph-devel = %{version}-%{release}
Requires:	%{name}-iostreams-devel = %{version}-%{release}
Requires:	%{name}-locale-devel = %{version}-%{release}
Requires:	%{name}-prg_exec_monitor-devel = %{version}-%{release}
Requires:	%{name}-program_options-devel = %{version}-%{release}
Requires:	%{name}-python-devel = %{version}-%{release}
Requires:	%{name}-random-devel = %{version}-%{release}
Requires:	%{name}-regex-devel = %{version}-%{release}
Requires:	%{name}-serialization-devel = %{version}-%{release}
Requires:	%{name}-signals-devel = %{version}-%{release}
Requires:	%{name}-system-devel = %{version}-%{release}
Requires:	%{name}-thread-devel = %{version}-%{release}
Requires:	%{name}-timer-devel = %{version}-%{release}
Requires:	%{name}-unit_test_framework-devel = %{version}-%{release}
Requires:	%{name}-wave-devel = %{version}-%{release}
Requires:	%{name}-wserialization-devel = %{version}-%{release}

%description devel
Header files for the Boost C++ libraries.

%package doc
Summary:	Boost C++ Library documentation
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description doc
Documentation for the Boost C++ Library.

###
%package atomic
Summary:	Boost C++ atmoic library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description atomic
Boost C++ atomic library.

%package atomic-devel
Summary:	Boost C++ atomic headers
Group:		Development/Libraries
Requires:	%{name}-atomic = %{version}-%{release}

%description atomic-devel
Boost C++ atomic headers.

###
%package chrono
Summary:	Boost C++ chrono library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description chrono
Boost C++ chrono library.

%package chrono-devel
Summary:	Boost C++ chrono headers
Group:		Development/Libraries
Requires:	%{name}-chrono = %{version}-%{release}

%description chrono-devel
Boost C++ chrono headers.

###
%package context
Summary:	Boost C++ context library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description context
Boost C++ context library.

%package context-devel
Summary:	Boost C++ context headers
Group:		Development/Libraries
Requires:	%{name}-context = %{version}-%{release}

%description context-devel
Boost C++ context headers.

###
%package coroutine
Summary:	Boost C++ coroutine library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description coroutine
Boost C++ coroutine library.

%package coroutine-devel
Summary:	Boost C++ coroutine headers
Group:		Development/Libraries
Requires:	%{name}-coroutine = %{version}-%{release}

%description coroutine-devel
Boost C++ coroutine headers.

###
%package date_time
Summary:	Boost C++ date_time library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description date_time
Boost C++ date_time library.

%package date_time-devel
Summary:	Boost C++ date_time headers
Group:		Development/Libraries
Requires:	%{name}-date_time = %{version}-%{release}

%description date_time-devel
Boost C++ date_time headers.

###
%package filesystem
Summary:	Boost C++ date_time library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description filesystem
Boost C++ filesystem library.

%package filesystem-devel
Summary:	Boost C++ filesystem headers
Group:		Development/Libraries
Requires:	%{name}-filesystem = %{version}-%{release}

%description filesystem-devel
Boost C++ filesystem headers.

###
%package graph
Summary:	Boost C++ graph library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description graph
Boost C++ graph library.

%package graph-devel
Summary:	Boost C++ graph headers
Group:		Development/Libraries
Requires:	%{name}-graph = %{version}-%{release}

%description graph-devel
Boost C++ graph headers.

###
%package iostreams
Summary:	Boost C++ iostreams library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description iostreams
Boost C++ iostreams library.

%package iostreams-devel
Summary:	Boost C++ iostreams headers
Group:		Development/Libraries
Requires:	%{name}-iostreams = %{version}-%{release}

%description iostreams-devel
Boost C++ iostreams headers.

###
%package locale
Summary:	Boost C++ locale library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description locale
Boost C++ locale library.

%package locale-devel
Summary:	Boost C++ locale headers
Group:		Development/Libraries
Requires:	%{name}-locale = %{version}-%{release}

%description locale-devel
Boost C++ locale headers.

###
%package log
Summary:	Boost C++ log library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description log
Boost C++ log library.

%package log-devel
Summary:	Boost C++ log headers
Group:		Development/Libraries
Requires:	%{name}-log = %{version}-%{release}

%description log-devel
Boost C++ log headers.

###
%package log_setup
Summary:	Boost C++ log_setup library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description log_setup
Boost C++ log_setup library.

%package log_setup-devel
Summary:	Boost C++ log_setup headers
Group:		Development/Libraries
Requires:	%{name}-log_setup = %{version}-%{release}

%description log_setup-devel
Boost C++ log_setup headers.

###
%package math
Summary:	Boost C++ iostreams libraries
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description math
Boost C++ math libraries.

%package math-devel
Summary:	Boost C++ iostreams headers
Group:		Development/Libraries
Requires:	%{name}-math = %{version}-%{release}

%description math-devel
Boost C++ math headers.

###
%package prg_exec_monitor
Summary:	Boost C++ prg_exec_monitor library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description prg_exec_monitor
Boost C++ prg_exec_monitor library.

%package prg_exec_monitor-devel
Summary:	Boost C++ prg_exec_monitor headers
Group:		Development/Libraries
Requires:	%{name}-prg_exec_monitor = %{version}-%{release}

%description prg_exec_monitor-devel
Boost C++ prg_exec_monitor headers.

###
%package program_options
Summary:	Boost C++ program_options library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description program_options
Boost C++ program_options library.

%package program_options-devel
Summary:	Boost C++ program_options headers
Group:		Development/Libraries
Requires:	%{name}-program_options = %{version}-%{release}

%description program_options-devel
Boost C++ program_options headers.

###
%package python
Summary:	Boost C++ python library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Boost C++ python library.

%package python-devel
Summary:	Boost C++ python headers
Group:		Development/Libraries
Requires:	%{name}-python = %{version}-%{release}

%description python-devel
Boost C++ python headers.

###
%package random
Summary:	Boost C++ random library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description random
Boost C++ random library.

%package random-devel
Summary:	Boost C++ random headers
Group:		Development/Libraries
Requires:	%{name}-random = %{version}-%{release}

%description random-devel
Boost C++ random headers.

###
%package regex
Summary:	Boost C++ regex library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description regex
Boost C++ regex library.

%package regex-devel
Summary:	Boost C++ regex headers
Group:		Development/Libraries
Requires:	%{name}-regex = %{version}-%{release}

%description regex-devel
Boost C++ regex headers.

###
%package serialization
Summary:	Boost C++ serialization library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description serialization
Boost C++ serialization library.

%package serialization-devel
Summary:	Boost C++ serialization headers
Group:		Development/Libraries
Requires:	%{name}-serialization = %{version}-%{release}

%description serialization-devel
Boost C++ serialization headers.

###
%package signals
Summary:	Boost C++ signals library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description signals
Boost C++ signals library.

%package signals-devel
Summary:	Boost C++ signals headers
Group:		Development/Libraries
Requires:	%{name}-signals = %{version}-%{release}

%description signals-devel
Boost C++ signals headers.

###
%package system
Summary:	Boost C++ signals library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description system
Boost C++ system library.

%package system-devel
Summary:	Boost C++ system headers
Group:		Development/Libraries
Requires:	%{name}-system = %{version}-%{release}

%description system-devel
Boost C++ system headers.

###
%package timer
Summary:	Boost C++ timer library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description timer
Boost C++ timer library.

%package timer-devel
Summary:	Boost C++ timer headers
Group:		Development/Libraries
Requires:	%{name}-timer = %{version}-%{release}

%description timer-devel
Boost C++ timer headers.

###
%package thread
Summary:	Boost C++ thread library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description thread
Boost C++ thread library.

%package thread-devel
Summary:	Boost C++ thread headers
Group:		Development/Libraries
Requires:	%{name}-thread = %{version}-%{release}

%description thread-devel
Boost C++ thread headers.

###
%package unit_test_framework
Summary:	Boost C++ unit_test_framework library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description unit_test_framework
Boost C++ unit_test_framework library.

%package unit_test_framework-devel
Summary:	Boost C++ unit_test_framework headers
Group:		Development/Libraries
Requires:	%{name}-unit_test_framework = %{version}-%{release}

%description unit_test_framework-devel
Boost C++ unit_test_framework headers.

###
%package wave
Summary:	Boost C++ wave library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description wave
Boost C++ wave library.

%package wave-devel
Summary:	Boost C++ wave headers
Group:		Development/Libraries
Requires:	%{name}-wave = %{version}-%{release}

%description wave-devel
Boost C++ wave headers.

###
%package wserialization
Summary:	Boost C++ wserialization library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description wserialization
Boost C++ wserialization library.

%package wserialization-devel
Summary:	Boost C++ wserialization headers
Group:		Development/Libraries
Requires:	%{name}-wserialization = %{version}-%{release}

%description wserialization-devel
Boost C++ wserialization headers.

%prep
%setup -qn %{name}_%{fver}
%patch0 -p1

%{__sed} -i "s/<optimization>speed : -O3/<optimization>speed : ${CXXFLAGS:-%rpmcxxflags} -fPIC/" tools/build/v2/tools/gcc.jam
%{__sed} -i 's/<debug-symbols>on : -g/<debug-symbols>on :/' tools/build/v2/tools/gcc.jam
%{__sed} -i 's:find-static:find-shared:' libs/graph/build/Jamfile.v2

echo "using mpi ;" >> tools/build/v2/user-config.jam

cat << EOF > tools/build/v2/user-config.jam
using gcc : %(%{__cxx} -dumpversion) : %{__cxx} ;
EOF

%build
./bootstrap.sh \
	--with-icu		\
	--with-toolset=gcc

mkdir -p dist/bin
install tools/build/v2/engine/bin.linux*/b2 dist/bin

./dist/bin/b2 \
	--layout=system		\
	--prefix=./dist		\
	--toolset=gcc		\
	-d2			\
	-q %{?_smp_mflags}	\
	cflags="%{rpmcflags}"	\
	linkflags="%{rpmldflags}"   \
	debug-symbols=on	\
	inlining=on		\
	link=shared		\
	pch=off			\
	python=2.7		\
	runtime-link=shared	\
	threading=multi		\
	variant=release		\
	install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -a dist/lib/* $RPM_BUILD_ROOT%{_libdir}
cp -rf dist/include/* $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	atomic -p /usr/sbin/ldconfig
%postun	atomic -p /usr/sbin/ldconfig

%post	context -p /usr/sbin/ldconfig
%postun	context -p /usr/sbin/ldconfig

%post	coroutine -p /usr/sbin/ldconfig
%postun	coroutine -p /usr/sbin/ldconfig

%post	date_time -p /usr/sbin/ldconfig
%postun	date_time -p /usr/sbin/ldconfig

%post	filesystem -p /usr/sbin/ldconfig
%postun	filesystem -p /usr/sbin/ldconfig

%post	graph -p /usr/sbin/ldconfig
%postun	graph -p /usr/sbin/ldconfig

%post	locale -p /usr/sbin/ldconfig
%postun	locale -p /usr/sbin/ldconfig

%post	log -p /usr/sbin/ldconfig
%postun	log -p /usr/sbin/ldconfig

%post	log_setup -p /usr/sbin/ldconfig
%postun	log_setup -p /usr/sbin/ldconfig

%post	iostreams -p /usr/sbin/ldconfig
%postun	iostreams -p /usr/sbin/ldconfig

%post	math -p /usr/sbin/ldconfig
%postun	math -p /usr/sbin/ldconfig

%post	prg_exec_monitor -p /usr/sbin/ldconfig
%postun	prg_exec_monitor -p /usr/sbin/ldconfig

%post	program_options -p /usr/sbin/ldconfig
%postun	program_options -p /usr/sbin/ldconfig

%post	python -p /usr/sbin/ldconfig
%postun	python -p /usr/sbin/ldconfig

%post	regex -p /usr/sbin/ldconfig
%postun	regex -p /usr/sbin/ldconfig

%post	serialization -p /usr/sbin/ldconfig
%postun	serialization -p /usr/sbin/ldconfig

%post	signals -p /usr/sbin/ldconfig
%postun	signals -p /usr/sbin/ldconfig

%post	system -p /usr/sbin/ldconfig
%postun	system -p /usr/sbin/ldconfig

%post	thread -p /usr/sbin/ldconfig
%postun	thread -p /usr/sbin/ldconfig

%post	timer -p /usr/sbin/ldconfig
%postun	timer -p /usr/sbin/ldconfig

%post	unit_test_framework -p /usr/sbin/ldconfig
%postun	unit_test_framework -p /usr/sbin/ldconfig

%post	wave -p /usr/sbin/ldconfig
%postun	wave -p /usr/sbin/ldconfig

%post	wserialization -p /usr/sbin/ldconfig
%postun	wserialization -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE_1_0.txt

%files devel
%defattr(644,root,root,755)
%{_includedir}/boost

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}

###
%files atomic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_atomic.so.*

%files atomic-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_atomic.so

###
%files chrono
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_chrono.so.*

%files chrono-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_chrono.so

###
%files context
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_context.so.*

%files context-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_context.so

###
%files coroutine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_coroutine.so.*

%files coroutine-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_coroutine.so

###
%files date_time
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time.so.*

%files date_time-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time.so

###
%files filesystem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem.so.*

%files filesystem-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem.so

###
%files graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph.so.*

%files graph-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph.so

###
%files iostreams
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams.so.*

###
%files iostreams-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams.so

###
%files locale
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_locale.so.*

###
%files locale-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_locale.so

###
%files log
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_log.so.*

%files log-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_log.so

###
%files log_setup
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_log_setup.so.*

%files log_setup-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_log_setup.so

###
%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_math_*.so.*

###
%files math-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_math_*.so

###
%files prg_exec_monitor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so.*

%files prg_exec_monitor-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so

###
%files program_options
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options.so.*

%files program_options-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options.so

###
%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python.so.*

%files python-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python.so

###
%files random
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_random.so.*

%files random-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_random.so

###
%files regex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex.so.*

%files regex-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex.so

###
%files signals
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals.so.*

%files signals-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals.so

###
%files system
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_system.so.*

%files system-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_system.so

###
%files timer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_timer.so.*

%files timer-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_timer.so

###
%files thread
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread.so.*

%files thread-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread.so

###
%files unit_test_framework
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so.*

%files unit_test_framework-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so

###
%files wave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave.so.*

###
%files wave-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave.so

###
%files serialization
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_serialization.so.*

###
%files serialization-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_serialization.so

###
%files wserialization
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wserialization.so.*

###
%files wserialization-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wserialization.so

