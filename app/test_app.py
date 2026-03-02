from unittest.mock import patch
import app

def test_create_user():
    with patch("app.input", side_effect=["flash", "1234"]), patch("app.db.create_user") as mock_create, patch("app.print") as mock_print:

        app.create_user()

        mock_create.assert_called_once_with("flash", "1234")
        mock_print.assert_called_once_with("User created!")


def test_view_user_found():
    with patch("app.input", return_value="flash"), patch("app.db.get_user", return_value=("flash", "1234")), patch("app.print") as mock_print:

        app.view_user()

        mock_print.assert_called_once_with(("flash", "1234"))

def test_view_user_not_found():
    with patch("app.input", return_value="luna"), patch("app.db.get_user", return_value=None), patch("app.print") as mock_print:

        app.view_user()

        mock_print.assert_called_once_with("User not found")