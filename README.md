# Development

Your new jumpstart project includes basic organization with an organized `assets` folder and a `components` folder.
If you chose to develop with the router feature, you will also have a `views` folder.

```
project/
├─ assets/ # Any assets that are used by the app should be placed here
├─ src/
│  ├─ main.rs # The entrypoint for the app. It also defines the routes for the app.
│  ├─ components/
│  │  ├─ mod.rs # Defines the components module
│  │  ├─ hero.rs # The Hero component for use in the home page
│  │  ├─ echo.rs # The echo component uses server functions to communicate with the server
│  ├─ views/ # The views each route will render in the app.
│  │  ├─ mod.rs # Defines the module for the views route and re-exports the components for each route
│  │  ├─ blog.rs # The component that will render at the /blog/:id route
│  │  ├─ home.rs # The component that will render at the / route
├─ Cargo.toml # The Cargo.toml file defines the dependencies and feature flags for your project
```

### Automatic Tailwind (Dioxus 0.7+)

As of Dioxus 0.7, there no longer is a need to manually install tailwind. Simply `dx serve` and you're good to go!

Automatic tailwind is supported by checking for a file called `tailwind.css` in your app's manifest directory (next to Cargo.toml). To customize the file, use the dioxus.toml:

```toml
[application]
tailwind_input = "my.css"
tailwind_output = "assets/out.css"
```

### Tailwind Manual Install

To use tailwind plugins or manually customize tailwind, you can can install the Tailwind CLI and use it directly.

1. Install npm: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
2. Install the Tailwind CSS CLI: https://tailwindcss.com/docs/installation/tailwind-cli
3. Run the following command in the root of the project to start the Tailwind CSS compiler:

```bash
npx @tailwindcss/cli -i ./input.css -o ./assets/tailwind.css --watch
```

### Serving Your App

Run the following command in the root of your project to start developing with the default platform:

```bash
dx serve --platform mobile
```

To run for a different platform, use the `--platform platform` flag. E.g.
```bash
dx serve --platform desktop
```

### Code Formatting and Linting

This project uses automated formatting and linting tools to ensure code quality and consistency.

#### Setup

The project uses pre-commit hooks to automatically format and lint code before commits. After cloning the repository, install the hooks:

```bash
uv sync --extra dev
uv run pre-commit install
```

#### Tools Used

- **Python**: [ruff](https://docs.astral.sh/ruff/) for formatting, linting, and import sorting
- **Rust**: [rustfmt](https://github.com/rust-lang/rustfmt) for code formatting

#### Pre-commit Hooks

Pre-commit hooks automatically run when you commit changes:
- Python files are formatted and linted with ruff
- Rust files are formatted with rustfmt
- Common file checks (trailing whitespace, end-of-file, etc.)

#### Manual Checks

To manually run all formatting and linting checks:

```bash
# Run all pre-commit hooks on all files
uv run pre-commit run --all-files

# Or run individual tools:
# Python formatting
uv run ruff format .

# Python linting
uv run ruff check .

# Rust formatting
cargo fmt --all
```

#### CI Validation

The GitHub Actions CI workflow validates formatting and linting on pull requests. The pipeline will fail if:
- Python code is not properly formatted or has linting errors
- Rust code is not properly formatted

**Note**: CI checks do not automatically fix issues - you must fix them locally and push the changes.

### Running E2E Tests

This project uses Python and Playwright for end-to-end integration tests. All test code is located in the `tests/` directory.

#### Prerequisites

1. Install `uv` (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install Python dependencies and Playwright browsers:
   ```bash
   uv sync --extra dev
   uv run playwright install
   ```

#### Running Tests

1. Start the Dioxus server in one terminal:
   ```bash
   dx serve --platform web
   ```

2. In another terminal, run the test suite:
   ```bash
   uv run pytest tests/
   ```

3. To run a specific test file:
   ```bash
   uv run pytest tests/test_dioxus_app.py
   ```

4. To run a specific test:
   ```bash
   uv run pytest tests/test_dioxus_app.py::test_home_page_loads_and_displays_content
   ```

5. To run tests with verbose output:
   ```bash
   uv run pytest tests/ -v
   ```

#### Test Structure

- `tests/__init__.py` - Makes tests a Python package
- `tests/conftest.py` - Shared fixtures (browser setup, base URL configuration)
- `tests/test_dioxus_app.py` - Validation tests that verify the Dioxus app is working
- `tests/test_example.py` - Example tests demonstrating Playwright usage

The tests validate that:
- Home page loads and displays content
- Navigation between routes works
- App is fully hydrated and interactive
- Routing system works end-to-end

### Continuous Integration

This project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that automatically:
- Validates code formatting and linting (Python with ruff, Rust with rustfmt)
- Builds the Dioxus application
- Runs all e2e integration tests
- Validates that the app works correctly

The CI runs on:
- Pull requests to `main` or `master` branches
- Pushes to `main` or `master` branches

The workflow ensures that all changes are validated before merging. The CI will fail if formatting or linting issues are found, but it will not automatically fix them - you must fix issues locally and push the changes.
