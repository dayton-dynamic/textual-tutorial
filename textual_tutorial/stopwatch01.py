from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
    ("x", "toggle_super_dark", "Super dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_super_dark(self) -> None:
        self.dark = True 


def main():
    app = StopwatchApp()
    app.run()
