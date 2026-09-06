"""Install a complete skill snapshot, preserving an existing installation as a backup."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile


def install(source, destination):
    source = source.resolve()
    destination = destination.expanduser().absolute()
    if destination.is_symlink():
        raise ValueError('Destination is a symlink; choose its intended directory explicitly')
    if destination.exists() and not destination.is_dir():
        raise ValueError('Destination must be a directory')
    if source == destination.resolve() or source in destination.resolve().parents or destination.resolve() in source.parents:
        raise ValueError('Source and destination must not overlap')
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source is missing SKILL.md')
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.design-install-', dir=destination.parent))
    backup = None
    try:
        shutil.copytree(source, staging / 'design')
        if destination.exists():
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            backup_dir = destination.parent / '.design-backups'
            backup_dir.mkdir(exist_ok=True)
            backup = backup_dir / stamp
            destination.rename(backup)
        try:
            (staging / 'design').rename(destination)
        except BaseException:
            if backup is not None:
                backup.rename(destination)
            raise
    finally:
        shutil.rmtree(staging)
    print(f'Installed: {destination}')
    if backup:
        print(f'Previous installation preserved: {backup}')
    return backup


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, default=Path.home() / '.agents/skills/design')
    args = parser.parse_args()
    install(Path(__file__).resolve().parents[1] / 'skills/design', args.destination)
