import pytest
import gowt.__main__


def test_main_error(capsys) -> None:
    print(type(capsys))
    # TODO: main() -> run(), _main() -> main()
    with pytest.raises(SystemExit) as exit_info:
        gowt.__main__.main()
        out, err = capsys.readouterr()
        assert out == ""
        errmsg: str = f"""
        {gowt.__name__}: error: Gentoo master repo not found (didn't check if needed)
        please sync it or provide it's location with --gentoo flag
        """.strip()
        assert err == errmsg
        assert exit_info.value.code == 2


#
# def test_main_error():
#     pass
#
#
# def test__main():
#     pass
#
#
# def test__get_repo():
#     pass
