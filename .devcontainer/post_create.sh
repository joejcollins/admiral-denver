# Install Rust using rustup so we can have tex-fmt.
# Once Debian trixie is available tex-fmt can be installed as a package.
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
. "$HOME/.cargo/env"
cargo install tex-fmt

# Create the virtual environment.
make venv
.venv/bin/pre-commit run --all-files

# Get the data and symlink to it.
cd ..
git clone https://github.com/joejcollins/atlanta-shore.git
ln -s  ../atlanta-shore/data ./admiral-denver/data
