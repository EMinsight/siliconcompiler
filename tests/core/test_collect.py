import siliconcompiler
import os
from siliconcompiler.targets import asic_demo


def test_collect_file_update():
    # Checks if collected files are properly updated after editing

    # Create instance of Chip class
    with open('fake.v', 'w') as f:
        f.write('fake')
    chip = siliconcompiler.Chip('fake')
    chip.input('fake.v')
    chip._collect()
    filename = chip._get_imported_filename('fake.v')

    with open(os.path.join(chip._getcollectdir(), filename), 'r') as f:
        assert f.readline() == 'fake'

    # Edit file
    with open('fake.v', 'w') as f:
        f.write('newfake')

    # Rerun remote run
    chip._collect()
    with open(os.path.join(chip._getcollectdir(), filename), 'r') as f:
        assert f.readline() == 'newfake'


def test_collect_file_asic_demo():
    chip = siliconcompiler.Chip('demo')
    chip.load_target(asic_demo)
    chip._collect()

    for f in chip.find_files('input', 'rtl', 'verilog', step='import', index=0):
        assert f.startswith(chip._getcollectdir())


def test_collect_file_copyall():
    chip = siliconcompiler.Chip('demo')
    chip.load_target(asic_demo)
    chip.set('option', 'copyall', True)
    chip._collect()

    # check that all file are copied (input, library, and pdk)
    assert len(os.listdir(chip._getcollectdir())) == 23


def test_collect_file_copyall_with_false():
    chip = siliconcompiler.Chip('demo')
    chip.load_target(asic_demo)
    chip.set('input', 'rtl', 'verilog', False, field='copy')
    chip.set('option', 'copyall', True)
    chip._collect()

    # check that all file are copied (input, library, and pdk)
    assert len(os.listdir(chip._getcollectdir())) == 23


def test_collect_file_with_false():
    chip = siliconcompiler.Chip('demo')
    chip.load_target(asic_demo)
    chip.set('input', 'rtl', 'verilog', False, field='copy')
    chip._collect()

    # No files should have been collected
    assert len(os.listdir(chip._getcollectdir())) == 0
