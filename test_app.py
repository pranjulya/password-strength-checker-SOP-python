from app import app, check_password_strength


def test_very_strong_password_has_no_suggestions():
    strength, suggestions = check_password_strength("Abcdef1!")
    assert strength == "Very Strong"
    assert suggestions == []


def test_symbols_outside_old_list_count_as_special():
    for pw in ("Abcdef1-", "Abcdef1_", "Abcdef1?", "Abcdef1."):
        strength, _ = check_password_strength(pw)
        assert strength == "Very Strong", pw


def test_space_is_not_a_special_character():
    strength, suggestions = check_password_strength("Abcdef1 ")
    assert strength == "Strong"
    assert any("special character" in s for s in suggestions)


def test_short_lowercase_password_is_very_weak():
    strength, suggestions = check_password_strength("abc")
    assert strength == "Very Weak"
    assert len(suggestions) == 4


def test_index_post_renders_rating():
    client = app.test_client()
    resp = client.post("/", data={"password": "Abcdef1!"})
    assert resp.status_code == 200
    assert b"Very Strong" in resp.data
