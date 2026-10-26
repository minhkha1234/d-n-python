"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect a successful offline response fixture."""
    result = parse_json_response(200, fixture)
    assert result["lesson"] == 13
    print(result)

    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
