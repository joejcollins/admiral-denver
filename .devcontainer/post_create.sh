# Create the virtual environment.
make venv
.venv/bin/pre-commit run --all-files

# Get the data and symlink to it.
cd ..
git clone https://github.com/joejcollins/atlanta-shore.git
ln -s  ../atlanta-shore/data ./admiral-denver/data
