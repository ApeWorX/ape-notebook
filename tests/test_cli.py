"""Test the CLI script."""
import unittest
from unittest.mock import MagicMock, patch

import click.testing

from ape_notebook._cli import cli


class TestCLIScript(unittest.TestCase):
    """Test the CLI script."""

    @patch("ape_notebook._cli.launch_new_instance")
    def test_cli(self, mock_launch_new_instance: MagicMock):
        """Run the main function."""

        # Set the mock to return None
        mock_launch_new_instance.return_value = None

        click.echo("Running CLI")
        runner = click.testing.CliRunner()
        result = runner.invoke(cli)

        # Print the result attributes
        click.echo(f"Exit code: {result.exit_code}")
        click.echo(f"Output: {result.output.strip()}")

        # Assert that the function was called once
        mock_launch_new_instance.assert_called_once()

        # Assert that the result has no output and exit code is 0 (indicating success)
        self.assertEqual(result.output, "")
        self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
