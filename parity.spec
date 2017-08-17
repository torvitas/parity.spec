Name:		parity
Version:	1.6.10
Release:	1%{?dist}
Summary:	Fast, light, robust Ethereum implementation

License:	GPL-3.0
URL:		https://parity.io/parity.html
Source0:	https://github.com/paritytech/parity/archive/v1.6.10.tar.gz

# systemd-devel for libudev.h
BuildRequires:	rust cargo git gcc-c++ openssl-devel systemd-devel

%description
Fast, light, and robust Ethereum implementation

%prep
%setup -q -n parity-%{version}

%build
export CARGO_HOME=`pwd`/.cargo/
cargo build --release

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 target/release/parity %{buildroot}%{_bindir}

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/parity

%changelog
* Wed Jun 26 2017 Timothée Floure <fnux@fnux.ch> - 1.6.10-1
- Initial build

