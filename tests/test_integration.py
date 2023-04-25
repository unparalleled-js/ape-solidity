import pytest
from ape._cli import cli
from click.testing import CliRunner


@pytest.fixture
def ape_cli():
    return cli


@pytest.fixture
def runner():
    return CliRunner()


def test_compile_using_cli(ape_cli, runner):
    import ape

    pdir  = ape.config.DATA_FOLDER / 'packages'
    debug_str = f"\nData folder: {ape.config.DATA_FOLDER}\n"
    debug_str += f"Packages folder exists: {pdir.is_dir()}\n"
    debug_str += f"Packages contents: {' '.join([x for x in pdir.itedir()])}"

    #debug_str += f"OZ exists: {(ape.config.DATA_FOLDER / 'packages' / 'OpenZeppelin').is_dir()}\n"
    # debug_str += f"{' '.join([x for x in (ape.config.DATA_FOLDER / 'packages' / 'OpenZeppelin').iterdir()])}\n"

    # debug_str += f"Project folder: {ape.config.PROJECT_FOLDER}\n"
    # debug_str += f"Contracts folder: {ape.config.contracts_folder}\n"
    # debug_str += f"Cache exists: {(ape.project.contracts_folder / '.cache').is_dir()}\n"
    # debug_str += f"OZ exists: {(ape.project.contracts_folder / '.cache' / 'OpenZeppelin').is_dir()}\n"
    # debug_str += f"OZ version exists: {(ape.project.contracts_folder / '.cache' / 'OpenZeppelin' / 'v4.7.1').is_dir()}\n"
    # debug_str += f"erc20 exists: {(ape.project.contracts_folder / '.cache' / 'OpenZeppelin' / 'v4.7.1' / 'token' / 'ERC20' / 'ERC20.sol').is_dir()}"

    raise ValueError(debug_str)

    result = runner.invoke(ape_cli, ["compile"], catch_exceptions=False)
    assert result.exit_code == 0
    assert "CompilesOnce" in result.output
    result = runner.invoke(ape_cli, ["compile"], catch_exceptions=False)

    # Already compiled so does not compile again.
    assert "CompilesOnce" not in result.output


@pytest.mark.parametrize(
    "contract_path",
    (
        "CompilesOnce",
        "CompilesOnce.sol",
        "contracts/CompilesOnce",
        "contracts/CompilesOnce.sol",
    ),
)
def test_compile_specified_contracts(ape_cli, runner, contract_path):
    result = runner.invoke(ape_cli, ["compile", contract_path, "--force"], catch_exceptions=False)
    assert result.exit_code == 0, result.output
    assert "Compiling 'CompilesOnce.sol'" in result.output, f"Failed to compile {contract_path}."


def test_force_recompile(ape_cli, runner):
    result = runner.invoke(ape_cli, ["compile", "--force"], catch_exceptions=False)
    assert result.exit_code == 0
