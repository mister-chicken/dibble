"""
E2E validation tests for the Dioxus application.

These tests validate that the core Dioxus app functionality is working:
- Home page loads and displays content
- Navigation between routes works
- App is interactive and hydrated

To run these tests:
1. Start the Dioxus server: dx serve --platform web
2. Run tests: uv run pytest tests/test_dioxus_app.py
"""

from urllib.parse import urljoin

from playwright.sync_api import Page, expect


def build_url(base_url: str, path: str = "") -> str:
    """
    Normalize and join the base URL with a relative path.
    Ensures consistent trailing slashes and works when the base URL includes a subpath.
    """
    normalized_base = base_url.rstrip("/") + "/"
    normalized_path = path.lstrip("/")
    return urljoin(normalized_base, normalized_path)


def test_home_page_loads_and_displays_content(page: Page):
    """Test that the home page loads successfully and displays content."""
    # Wait for the page to be fully loaded and hydrated
    page.wait_for_load_state("networkidle")

    # Check that the body is visible (basic page load validation)
    body = page.locator("body")
    expect(body).to_be_visible()

    # Check that the navbar is present (layout component)
    navbar = page.locator("#navbar")
    expect(navbar).to_be_visible()


def test_navbar_navigation_works(page: Page, base_url: str):
    """Test that navigation links in the navbar work correctly."""
    # Wait for initial load
    page.wait_for_load_state("networkidle")

    # Check that Home link exists and is visible
    home_link = page.get_by_role("link", name="Home")
    expect(home_link).to_be_visible()

    # Check that Blog link exists and is visible
    blog_link = page.get_by_role("link", name="Blog")
    expect(blog_link).to_be_visible()

    # Click the Blog link and verify navigation
    blog_link.click()
    page.wait_for_load_state("networkidle")

    # Verify URL changed (should include /blog/)
    expect(page).to_have_url(build_url(base_url, "blog/1"))

    # Navigate back to home
    home_link = page.get_by_role("link", name="Home")
    home_link.click()
    page.wait_for_load_state("networkidle")

    # Verify we're back on home page
    expect(page).to_have_url(build_url(base_url))


def test_app_is_fully_hydrated(page: Page):
    """Test that the Dioxus app has fully hydrated and is interactive."""
    # Wait for the page to load
    page.wait_for_load_state("networkidle")

    # Basic check that the page is interactive
    body = page.locator("body")
    expect(body).to_be_visible()

    # Try interacting with the page to ensure Dioxus hydration worked
    # Click on the navbar to ensure events are working
    navbar = page.locator("#navbar")
    navbar.click()

    # Verify the navbar is still visible after interaction
    expect(navbar).to_be_visible()


def test_blog_route_works(page: Page, base_url: str):
    """Test that the blog route with dynamic parameter works."""
    # Navigate directly to blog route
    page.goto(build_url(base_url, "blog/1"))
    page.wait_for_load_state("networkidle")

    # Verify we're on the blog page
    expect(page).to_have_url(build_url(base_url, "blog/1"))

    # Verify navbar is still present (layout should work)
    navbar = page.locator("#navbar")
    expect(navbar).to_be_visible()


def test_routing_system_works(page: Page, base_url: str):
    """Test that the Dioxus routing system works end-to-end."""
    # Start on home
    page.goto(build_url(base_url))
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(build_url(base_url))

    # Navigate to blog via link
    blog_link = page.get_by_role("link", name="Blog")
    blog_link.click()
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(build_url(base_url, "blog/1"))

    # Navigate back to home via link
    home_link = page.get_by_role("link", name="Home")
    home_link.click()
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(build_url(base_url))
