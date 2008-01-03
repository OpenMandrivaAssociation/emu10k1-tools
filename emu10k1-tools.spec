%define	version	0.9.4
%define	name	emu10k1-tools
%define	release	%mkrel 6

Summary:	The emu-tools work with the emu10k1 driver include in the kernel
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Hardware
Source0:	http://prdownloads.sourceforge.net/emu10k1/emu-tools-%{version}.tar.bz2
Url:		http://sourceforge.net/projects/emu10k1
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kernel-source-latest
Patch0:		emu-tools-0.9.4-mdkconf.patch.bz2
Patch1:		%{name}-0.9.4-gcc3.3-fix.patch.bz2
Patch2:		emu10k1-tools-0.9.4-gcc4.0-fix.patch.bz2

Conflicts:      as10k1

%description
The emu-tools work with the emu10k1 driver include in the kernel.

%prep
%setup -q -n emu-tools-%{version}
%patch0 -p1 -b .mdkconf
%patch1 -p1 -b .gcc3.3
%patch2 -p1 -b .gcc4.0

%build
make CFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall	man_prefix=$RPM_BUILD_ROOT/%{_mandir} \
		data_dir=$RPM_BUILD_ROOT/%{_datadir}/emu10k1 \
		script_dir=$RPM_BUILD_ROOT/%{_initrddir}

mv $RPM_BUILD_ROOT%{_initrddir}/emu10k1.conf $RPM_BUILD_ROOT%{_sysconfdir}
mv $RPM_BUILD_ROOT%{_initrddir}/emu-script $RPM_BUILD_ROOT%{_bindir}/emu10k1-ctl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root, root)
%doc docs
%{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/emu10k1.conf
%dir %{_datadir}/emu10k1/
%attr(644,root,root) %{_datadir}/emu10k1/*

