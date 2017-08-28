Name:   parity
Version:  1.7.0
Release:  1%{?dist}
Summary:  Ethereum browser

License:  GPLv3
URL:    https://parity.io/parity.html
Source0:  https://github.com/paritytech/parity/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# systemd-devel for libudev.h
BuildRequires:  rust cargo git gcc-c++ openssl-devel systemd-devel

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
* Thu Aug 17 2017 Timothée Floure <fnux@fnux.ch> - 1.7.0-1
- Update to 1.7.0
* Mon Jun 26 2017 Timothée Floure <fnux@fnux.ch> - 1.6.10-1
- Initial build
