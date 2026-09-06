from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from scripts.install import install
from scripts.validate import validate

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'skills', self.root / 'skills')
        self.source = self.root / 'skills/design'

    def test_valid(self):
        validate(self.root)

    def test_unterminated_frontmatter(self):
        entry = self.source / 'SKILL.md'
        entry.write_text('---\nname: design\ndescription: sample\n')
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_invalid_metadata_type(self):
        (self.source / 'agents/openai.yaml').write_text('interface: []\n')
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_missing_reference_and_anchor(self):
        entry = self.source / 'SKILL.md'
        original = entry.read_text()
        for target in ('references/missing.md', 'references/modes.md#nonexistent', '../../README.md'):
            with self.subTest(target=target):
                entry.write_text(original + f'\n[bad]({target})\n')
                with self.assertRaises(ValueError):
                    validate(self.root)

    def test_upgrade_preserves_backup_and_removes_stale_files(self):
        target = self.root / 'installed/design'
        install(self.source, target)
        (target / 'obsolete.md').write_text('user content')
        backup = install(self.source, target)
        self.assertFalse((target / 'obsolete.md').exists())
        self.assertEqual((backup / 'obsolete.md').read_text(), 'user content')

    def test_symlink_refused(self):
        target = self.root / 'link'
        target.symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(ValueError):
            install(self.source, target)

    def test_failed_replacement_restores_original(self):
        target = self.root / 'installed/design'
        install(self.source, target)
        (target / 'personal.md').write_text('keep me')
        rename = Path.rename

        def fail_staging(path, destination):
            if path.parent.name.startswith('.design-install-'):
                raise OSError('simulated replacement failure')
            return rename(path, destination)

        with patch.object(Path, 'rename', fail_staging):
            with self.assertRaises(OSError):
                install(self.source, target)
        self.assertEqual((target / 'personal.md').read_text(), 'keep me')
