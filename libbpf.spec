%define major 1
%define libname %mklibname bpf
%define devname %mklibname bpf -d
%define sdevname %mklibname bpf -d -s

Name: libbpf
Version: 1.1.0
Release: 1
Source0: https://github.com/libbpf/libbpf/archive/refs/tags/v%{version}.tar.gz
Summary: Library for working with BPF object files
URL: https://github.com/libbpf/libbpf
License: GPL
Group: System/Libraries
BuildRequires: pkgconf
BuildRequires: make
BuildRequires: pkgconfig(libelf)

%description
libbpf is a C-based library containing a BPF loader that takes compiled BPF
object files and prepares and loads them into the Linux kernel. libbpf takes
the heavy lifting of loading, verifying, and attaching BPF programs to various
kernel hooks, allowing BPF application developers to focus only on BPF program
correctness and performance.

The following are the high-level features supported by libbpf:

* Provides high-level and low-level APIs for user space programs to interact
  with BPF programs. The low-level APIs wrap all the bpf system call
  functionality, which is useful when users need more fine-grained control
  over the interactions between user space and BPF programs.

* Provides overall support for the BPF object skeleton generated by bpftool.
  The skeleton file simplifies the process for the user space programs to
  access global variables and work with BPF programs.

* Provides BPF-side APIS, including BPF helper definitions, BPF maps
  support, and tracing helpers, allowing developers to simplify BPF code writing.

* Supports BPF CO-RE mechanism, enabling BPF developers to write portable BPF
  programs that can be compiled once and run across different kernel versions.

%package -n %{libname}
Summary: Library for working with BPF object files
Group: System/Libraries

%description -n %{libname}
libbpf is a C-based library containing a BPF loader that takes compiled BPF
object files and prepares and loads them into the Linux kernel. libbpf takes
the heavy lifting of loading, verifying, and attaching BPF programs to various
kernel hooks, allowing BPF application developers to focus only on BPF program
correctness and performance.

The following are the high-level features supported by libbpf:

* Provides high-level and low-level APIs for user space programs to interact
  with BPF programs. The low-level APIs wrap all the bpf system call
  functionality, which is useful when users need more fine-grained control
  over the interactions between user space and BPF programs.

* Provides overall support for the BPF object skeleton generated by bpftool.
  The skeleton file simplifies the process for the user space programs to
  access global variables and work with BPF programs.

* Provides BPF-side APIS, including BPF helper definitions, BPF maps
  support, and tracing helpers, allowing developers to simplify BPF code writing.

* Supports BPF CO-RE mechanism, enabling BPF developers to write portable BPF
  programs that can be compiled once and run across different kernel versions.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{sdevname}
Summary: Static library files for %{name}
Group: Development/C/Static
Requires: %{devname} = %{EVRD}

%description -n %{sdevname}
Static libraries for %{name}.

%prep
%autosetup -p1

%build
%make_build -C src CFLAGS="%{optflags} -fno-strict-aliasing -Werror -Wall" CC="%{__cc}"

%install
%make_install -C src CFLAGS="%{optflags}" CC="%{__cc}"

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n %{sdevname}
%{_libdir}/*.a
