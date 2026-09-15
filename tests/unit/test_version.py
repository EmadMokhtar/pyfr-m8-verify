import pyfr_m8_verify


def test_package_exposes_a_version() -> None:
    assert isinstance(pyfr_m8_verify.__version__, str)
    assert pyfr_m8_verify.__version__ != ""
