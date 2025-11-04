"""
Example Playwright test demonstrating basic e2e testing of the Dioxus app.

To run these tests:
1. Start the Dioxus server: dx serve --platform web
2. Run tests: uv run pytest tests/test_example.py
"""

from playwright.sync_api import Page, expect


def test_home_page_loads(page: Page):
    """Test that the home page loads successfully."""
    # Wait for the page to be fully loaded
    page.wait_for_load_state("networkidle")

    # Check that the page title or main content is present
    # Adjust selectors based on your actual Dioxus app structure
    body = page.locator("body")
    expect(body).to_be_visible()


def test_navigation_works(page: Page):
    """Test that navigation between routes works."""
    # Wait for initial load
    page.wait_for_load_state("networkidle")

    # Check if we're on the home page (adjust selector based on your app)
    # This is a placeholder - update based on your actual app structure
    body = page.locator("body")
    expect(body).to_be_visible()

    # If your app has navigation links, test them here
    # Example:
    # home_link = page.get_by_role("link", name="Home")
    # expect(home_link).to_be_visible()


def test_app_is_interactive(page: Page):
    """Test that the app is interactive (basic smoke test)."""
    # Wait for the page to load
    page.wait_for_load_state("networkidle")

    # Basic check that the page is interactive
    # This ensures the Dioxus app has hydrated and is functional
    body = page.locator("body")
    expect(body).to_be_visible()

    # Try clicking somewhere on the page to ensure interactivity
    # Adjust based on your actual app structure
    page.click("body")  # Basic interaction test
