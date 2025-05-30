# Create the virtual environment.
make venv
.venv/bin/pre-commit run --all-files

# Get the data and symlink to it.
sudo chown -R vscode:vscode /workspaces
cd /workspaces
git clone --depth=1 https://github.com/joejcollins/atlanta-shore.git
ln -s  ../atlanta-shore/data /workspaces/admiral-denver/data
