# This install all Atom packages found in the atom-package.list onto local Atom

echo 'Installing atom packages from ~/.atom/package.list'
apm install --packages-file ~/.atom/package.list
