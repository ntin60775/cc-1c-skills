#!/usr/bin/env python3
# db-run v1.0 — Launch 1C:Enterprise
# Source: https://github.com/Nikolay-Shirokov/cc-1c-skills

import argparse
import glob
import os
import platform
import subprocess
import sys


def resolve_v8path(v8path):
    """Resolve path to 1cv8 executable."""
    if v8path:
        if os.path.isdir(v8path):
            v8path = os.path.join(v8path, "1cv8.exe" if platform.system() == "Windows" else "1cv8")
        if not os.path.isfile(v8path):
            print(f"Error: 1cv8 not found at {v8path}", file=sys.stderr)
            sys.exit(1)
        return v8path

    # Auto-detect
    if platform.system() == "Windows":
        candidates = glob.glob(r"C:\Program Files\1cv8\*\bin\1cv8.exe")
    else:
        candidates = []
        for pattern in ["/opt/1cv8/*/bin/1cv8", "/opt/1cv8/x86_64/*/bin/1cv8"]:
            candidates.extend(glob.glob(pattern))
        if not candidates:
            for path_dir in os.environ.get("PATH", "").split(os.pathsep):
                candidate = os.path.join(path_dir, "1cv8")
                if os.path.isfile(candidate):
                    candidates.append(candidate)

    if candidates:
        candidates.sort()
        return candidates[-1]

    print("Error: 1cv8 not found. Specify -V8Path", file=sys.stderr)
    sys.exit(1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Launch 1C:Enterprise",
        allow_abbrev=False,
    )
    parser.add_argument("-V8Path", default="")
    parser.add_argument("-InfoBasePath", default="")
    parser.add_argument("-InfoBaseServer", default="")
    parser.add_argument("-InfoBaseRef", default="")
    parser.add_argument("-UserName", default="")
    parser.add_argument("-Password", default="")
    parser.add_argument("-Execute", default="")
    parser.add_argument("-CParam", default="")
    parser.add_argument("-URL", default="")
    args = parser.parse_args()

    v8path = resolve_v8path(args.V8Path)

    # --- Validate connection ---
    if not args.InfoBasePath and (not args.InfoBaseServer or not args.InfoBaseRef):
        print("Error: specify -InfoBasePath or -InfoBaseServer + -InfoBaseRef", file=sys.stderr)
        sys.exit(1)

    # --- Build arguments ---
    arguments = ["ENTERPRISE"]

    if args.InfoBaseServer and args.InfoBaseRef:
        arguments.extend(["/S", f"{args.InfoBaseServer}/{args.InfoBaseRef}"])
    else:
        arguments.extend(["/F", args.InfoBasePath])

    if args.UserName:
        arguments.append(f"/N{args.UserName}")
    if args.Password:
        arguments.append(f"/P{args.Password}")

    # --- Optional params ---
    execute = args.Execute
    if execute:
        ext = os.path.splitext(execute)[1].lower()
        if ext == ".erf":
            print("[WARN] /Execute does not support ERF files (external reports).")
            print(f"       Open the report via File -> Open: {execute}")
            print("       Launching database without /Execute.")
            execute = ""

    if execute:
        arguments.extend(["/Execute", execute])
    if args.CParam:
        arguments.extend(["/C", args.CParam])
    if args.URL:
        arguments.extend(["/URL", args.URL])

    arguments.append("/DisableStartupDialogs")

    # --- Execute (background, no wait) ---
    print(f"Running: 1cv8 {' '.join(arguments)}")
    subprocess.Popen([v8path] + arguments)
    print("1C:Enterprise launched")


if __name__ == "__main__":
    main()
