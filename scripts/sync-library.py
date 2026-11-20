#!/usr/bin/env python3
import argparse, shutil
from common import ROOT, today

def main():
    ap=argparse.ArgumentParser(description='Import a user-supplied Steam export; never logs in or mutates Steam.')
    ap.add_argument('--source', help='Path to a local markdown/text export')
    ap.add_argument('--dry-run', action='store_true')
    args=ap.parse_args()
    if not args.source: print('No source supplied. Safe exit: use --source PATH or --dry-run.'); return
    src=ROOT/args.source if not __import__('pathlib').Path(args.source).is_absolute() else __import__('pathlib').Path(args.source)
    if not src.exists(): raise SystemExit(f'Missing source: {src}')
    dest=ROOT/'data/library/snapshots'/f'{today()}.md'
    if args.dry_run: print(f'Would copy {src} -> {dest}')
    else: shutil.copyfile(src,dest); print(f'Wrote {dest}')
if __name__ == '__main__': main()
