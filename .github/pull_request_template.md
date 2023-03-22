Recommended steps to avoid delays in CI and code review:

- [ ] Use `nbqa black nbs` to use `black` to format the notebook code.
- [ ] Use `nbqa flake8 nbs` to run linting checks on the notebooks.

Required steps:

- [ ] Increment version number in `settings.ini` if changing the library.
- [ ] Use `nbdev_preview` to preview the documentation site if changing the notebooks.
- [ ] Use `nbdev_prepare` to export, test, and clean notebooks.