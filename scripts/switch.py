#!/usr/bin/env python3
# switch.py v2.0 — Установка навыков 1С для AI-платформ
# Source: https://github.com/Nikolay-Shirokov/cc-1c-skills
"""
Копирует (или создаёт ссылки на) навыки из .agents/skills/ на другие AI-платформы
(Cursor, Codex, Copilot, Kiro, Gemini CLI, OpenCode, Windsurf, Kilo Code, Cline,
Roo Code, Augment и др.) с перезаписью путей.

Использование:
  python scripts/switch.py                                       # интерактивный режим
  python scripts/switch.py cursor                                # скопировать на Cursor
  python scripts/switch.py kimi --project-dir /my/proj           # установить в проект
  python scripts/switch.py claude-code --project-dir /my/proj --link  # ссылки вместо копий
  python scripts/switch.py --undo cursor                         # удалить копию
"""
import argparse
import os
import shutil
import sys

# ---------------------------------------------------------------------------
# Platform registry
# ---------------------------------------------------------------------------
PLATFORMS = {
    'agents':      '.agents/skills',
    'augment':     '.augment/skills',
    'cline':       '.cline/skills',
    'claude-code': '.claude/skills',
    'codex':       '.codex/skills',
    'cursor':      '.cursor/skills',
    'copilot':     '.github/skills',
    'gemini':      '.gemini/skills',
    'kilo':        '.kilocode/skills',
    'kiro':        '.kiro/skills',
    'kimi':        '.agents/skills',
    'opencode':    '.opencode/skills',
    'roo':         '.roo/skills',
    'windsurf':    '.windsurf/skills',
}

SOURCE_PREFIX = '.agents/skills'

# Рекомендуемые записи для .gitignore целевого проекта
GITIGNORE_RECOMMENDATIONS = [
    '.v8-project.json',
    'build/',
    'base/',
    '*.epf',
    '*.erf',
    '*.log',
]


# ---------------------------------------------------------------------------
# Junction / symlink helpers
# ---------------------------------------------------------------------------
def is_junction(path):
    """Check if path is a junction or symlink."""
    if os.path.islink(path):
        return True
    if hasattr(os, 'isjunction'):
        return os.path.isjunction(path)
    return False


def remove_junction(path):
    """Remove junction/symlink without following it."""
    if sys.platform == 'win32':
        os.rmdir(path)
    else:
        os.unlink(path)


def create_junction(src, dst):
    """Create directory junction (Windows) or symlink (Unix)."""
    if sys.platform == 'win32':
        import _winapi
        _winapi.CreateJunction(src, dst)
    else:
        os.symlink(src, dst, target_is_directory=True)


def safe_rmtree(path):
    """Remove directory tree, handling junctions/symlinks safely.

    Unlike shutil.rmtree, this does not follow junctions/symlinks —
    it removes the link itself without touching the target.
    """
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if is_junction(entry_path):
            remove_junction(entry_path)
        elif os.path.isdir(entry_path):
            shutil.rmtree(entry_path)
        else:
            os.unlink(entry_path)
    os.rmdir(path)


def repo_root():
    """Return the repository root (parent of scripts/)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def source_skills_dir():
    return os.path.join(repo_root(), '.agents', 'skills')


def scan_skills(skills_dir):
    """Return sorted list of skill directory names that contain SKILL.md."""
    result = []
    for entry in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, entry)
        if os.path.isdir(skill_path) and os.path.isfile(os.path.join(skill_path, 'SKILL.md')):
            result.append(entry)
    return result


def collect_md_files(skill_dir):
    """Return list of .md files in a skill directory."""
    import glob
    return sorted(glob.glob(os.path.join(skill_dir, '*.md')))


def is_different_dir(dir1, dir2):
    """Check if two directories are different (resolved)."""
    return os.path.normcase(os.path.realpath(dir1)) != \
           os.path.normcase(os.path.realpath(dir2))


# ---------------------------------------------------------------------------
# Transformations
# ---------------------------------------------------------------------------
def rewrite_paths(content, source_prefix, target_prefix):
    """Replace .agents/skills/ path prefix with target platform prefix."""
    return content.replace(source_prefix + '/', target_prefix + '/')


def print_gitignore_recommendations(project_dir):
    """Print .gitignore recommendations for the target project."""
    gitignore_path = os.path.join(project_dir, '.gitignore')
    existing = set()
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                existing.add(line.strip())

    missing = [r for r in GITIGNORE_RECOMMENDATIONS if r not in existing]
    if missing:
        print(f"\nРекомендуется добавить в .gitignore проекта:")
        for r in missing:
            print(f"  {r}")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
def cmd_install(platform, project_dir):
    """Copy skills to target platform directory with path rewriting."""
    src_dir = source_skills_dir()
    target_prefix = PLATFORMS[platform]
    target_dir = os.path.join(project_dir, target_prefix.replace('/', os.sep))

    skills = scan_skills(src_dir)
    if not skills:
        print(f"Ошибка: навыки не найдены в {src_dir}", file=sys.stderr)
        return 1

    if os.path.isdir(target_dir):
        existing = scan_skills(target_dir)
        if existing:
            print(f"В {target_prefix}/ уже есть {len(existing)} навыков. Обновляю...")
            safe_rmtree(target_dir)

    os.makedirs(target_dir, exist_ok=True)

    # Copy root-level files from source skills dir (.gitignore, etc.)
    for name in os.listdir(src_dir):
        src_path = os.path.join(src_dir, name)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, os.path.join(target_dir, name))

    installed = 0

    print(f"\nКопирование {len(skills)} навыков в {target_prefix}/ ...")

    for skill_name in skills:
        src_skill = os.path.join(src_dir, skill_name)
        dst_skill = os.path.join(target_dir, skill_name)

        # Copy entire skill directory
        shutil.copytree(src_skill, dst_skill)

        # Rewrite paths in all .md files
        for md_path in collect_md_files(dst_skill):
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = rewrite_paths(content, SOURCE_PREFIX, target_prefix)

            if new_content != content:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

        print(f"  [OK] {skill_name}")
        installed += 1

    print(f"\nГотово! {installed} навыков установлено в {target_prefix}/")

    print_gitignore_recommendations(project_dir)

    if platform != 'claude-code':
        print(f"\nДля удаления: python scripts/switch.py --undo {platform}")
    return 0


def cmd_link(platform, project_dir):
    """Create junctions/symlinks to skills instead of copying."""
    if platform != 'claude-code':
        print(f"Ошибка: ссылки поддерживаются только для claude-code "
              f"(выбрано: {platform}).", file=sys.stderr)
        print("Для других платформ требуется перезапись путей в SKILL.md — "
              "используйте копирование.", file=sys.stderr)
        return 1

    src_dir = source_skills_dir()
    target_prefix = PLATFORMS[platform]
    target_dir = os.path.join(project_dir, target_prefix.replace('/', os.sep))

    if not is_different_dir(target_dir, src_dir):
        print("Ошибка: нельзя создать ссылки на самого себя.", file=sys.stderr)
        return 1

    skills = scan_skills(src_dir)
    if not skills:
        print(f"Ошибка: навыки не найдены в {src_dir}", file=sys.stderr)
        return 1

    if os.path.isdir(target_dir):
        existing = scan_skills(target_dir)
        if existing:
            print(f"В {target_prefix}/ уже есть {len(existing)} навыков. "
                  f"Обновляю...")
            safe_rmtree(target_dir)

    os.makedirs(target_dir, exist_ok=True)

    # Copy root-level files (.gitignore etc.)
    for name in os.listdir(src_dir):
        src_path = os.path.join(src_dir, name)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, os.path.join(target_dir, name))

    linked = 0
    link_type = "junction" if sys.platform == 'win32' else "symlink"
    print(f"\nСоздание {link_type}-ссылок на {len(skills)} навыков "
          f"в {target_prefix}/ ...")

    for skill_name in skills:
        src_skill = os.path.join(src_dir, skill_name)
        dst_skill = os.path.join(target_dir, skill_name)
        create_junction(src_skill, dst_skill)
        print(f"  [OK] {skill_name}")
        linked += 1

    print(f"\nГотово! {linked} навыков подключено через {link_type} "
          f"в {target_prefix}/")
    print("Обновления в источнике автоматически подхватятся.")
    print("⚠ Режим --link экспериментальный. При ошибках запуска "
          "скриптов переключитесь на копирование (без --link).")
    print_gitignore_recommendations(project_dir)
    print(f"\nДля удаления: python scripts/switch.py --undo claude-code"
          f" --project-dir \"{project_dir}\"")
    return 0


def cmd_undo(platform, project_dir):
    """Remove installed skills for a platform."""
    target_prefix = PLATFORMS[platform]
    target_dir = os.path.join(project_dir, target_prefix.replace('/', os.sep))

    if not os.path.isdir(target_dir):
        print(f"Директория {target_prefix}/ не найдена — нечего удалять.")
        return 0

    skills = scan_skills(target_dir)
    safe_rmtree(target_dir)

    # Clean up empty parent directories
    parent = os.path.dirname(target_dir)
    if os.path.isdir(parent) and not os.listdir(parent):
        os.rmdir(parent)

    print(f"Удалено: {target_prefix}/ ({len(skills)} навыков)")
    return 0


# ---------------------------------------------------------------------------
# Interactive mode
# ---------------------------------------------------------------------------
def ask_choice(prompt, options, default=1):
    """Ask user to choose from numbered options. Returns 1-based index."""
    print(f"\n{prompt}")
    for i, (label, hint) in enumerate(options, 1):
        marker = "*" if i == default else " "
        print(f"  {marker}{i:>2}. {label:<16} ({hint})")
    while True:
        try:
            raw = input(f"\nВыбор [{default}]: ").strip()
            if not raw:
                return default
            val = int(raw)
            if 1 <= val <= len(options):
                return val
            print(f"  Введите число от 1 до {len(options)}")
        except ValueError:
            print(f"  Введите число от 1 до {len(options)}")
        except (EOFError, KeyboardInterrupt):
            print("\nОтмена.")
            sys.exit(0)


def ask_path(prompt, default=''):
    """Ask user for a directory path."""
    hint = f" [{default}]" if default else ""
    try:
        raw = input(f"\n{prompt}{hint}: ").strip()
        return raw if raw else default
    except (EOFError, KeyboardInterrupt):
        print("\nОтмена.")
        sys.exit(0)


def interactive_mode():
    """Run interactive setup wizard."""
    print("Навыки 1С — настройка платформы")
    print("=" * 31)

    platform_options = [
        ("Claude Code",    ".agents/skills/"),
        ("Augment",        ".augment/skills/"),
        ("Cline",          ".cline/skills/"),
        ("Cursor",         ".cursor/skills/"),
        ("GitHub Copilot", ".github/skills/"),
        ("Kilo Code",      ".kilocode/skills/"),
        ("Kiro",           ".kiro/skills/"),
        ("Kimi CLI",       ".kimi/skills/"),
        ("OpenAI Codex",   ".codex/skills/"),
        ("Gemini CLI",     ".gemini/skills/"),
        ("OpenCode",       ".opencode/skills/"),
        ("Roo Code",       ".roo/skills/"),
        ("Windsurf",       ".windsurf/skills/"),
        ("Agent Skills",   ".agents/skills/"),
    ]
    platform_keys = [
        'claude-code', 'augment', 'cline', 'cursor', 'copilot', 'kilo',
        'kiro', 'kimi', 'codex', 'gemini', 'opencode', 'roo', 'windsurf', 'agents',
    ]

    choice = ask_choice("Для какой платформы настроить навыки?", platform_options)
    platform = platform_keys[choice - 1]

    project_dir = os.getcwd()

    # For claude-code in repo root, only runtime switch was offered.
    # Now we always proceed to install if a different project is needed.
    if platform == 'claude-code' and not is_different_dir(project_dir, repo_root()):
        # Already in repo root — ask if user wants to install to a different project
        mode_options = [
            ("Установить в проект", "скопировать навыки в другой проект"),
            ("Отмена",              "ничего не делать"),
        ]
        mode = ask_choice("Что сделать?", mode_options)
        if mode == 2:
            print("Отмена.")
            return 0

    default_dir = project_dir
    project_dir = ask_path("Путь к целевому проекту", default_dir)
    if not project_dir or not os.path.isdir(project_dir):
        print(f"Ошибка: директория '{project_dir}' не найдена.",
              file=sys.stderr)
        return 1

    # Check if already installed — offer update or remove
    target_prefix = PLATFORMS[platform]
    target_dir = os.path.join(project_dir, target_prefix.replace('/', os.sep))

    if os.path.isdir(target_dir):
        existing = scan_skills(target_dir)
        if existing:
            action_options = [
                ("Обновить", f"перезаписать {len(existing)} навыков"),
                ("Удалить",  f"удалить {target_prefix}/"),
                ("Отмена",   "ничего не делать"),
            ]
            action = ask_choice(
                f"В {target_prefix}/ уже есть {len(existing)} навыков.",
                action_options
            )
            if action == 2:
                return cmd_undo(platform, project_dir)
            if action == 3:
                print("Отмена.")
                return 0

    # Ask install method for claude-code to different project
    if platform == 'claude-code' and is_different_dir(project_dir, repo_root()):
        method_options = [
            ("Ссылки (junction)", "обновления подхватываются автоматически"),
            ("Копирование",       "независимая копия навыков"),
        ]
        method = ask_choice("Способ установки:", method_options)
        if method == 1:
            return cmd_link('claude-code', project_dir)

    return cmd_install(platform, project_dir)


# ---------------------------------------------------------------------------
# CLI argument parsing
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) == 1:
        return interactive_mode()

    parser = argparse.ArgumentParser(
        description='Установка навыков 1С для AI-платформ',
        epilog='Примеры:\n'
               '  python scripts/switch.py cursor\n'
               '  python scripts/switch.py kimi --project-dir /my/proj\n'
               '  python scripts/switch.py claude-code --project-dir /my/proj --link\n'
               '  python scripts/switch.py --undo cursor\n',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('platform', nargs='?', choices=list(PLATFORMS.keys()),
                        help='целевая платформа')
    parser.add_argument('--undo', action='store_true',
                        help='удалить навыки для указанной платформы')
    parser.add_argument('--project-dir', default=os.getcwd(),
                        help='путь к целевому проекту (по умолчанию: текущий каталог)')
    parser.add_argument('--link', action='store_true',
                        help='[экспериментально] создать ссылки (junction/symlink) '
                             'вместо копирования (только для claude-code)')

    args = parser.parse_args()

    # --link: create junctions/symlinks
    if args.link:
        if not args.platform:
            parser.error("--link требует указания платформы")
        return cmd_link(args.platform, args.project_dir)

    # --undo requires platform
    if args.undo:
        if not args.platform:
            parser.error("--undo требует указания платформы")
        if args.platform == 'claude-code' \
                and not is_different_dir(args.project_dir, repo_root()):
            parser.error(
                "--undo не применим к claude-code в исходном репозитории")
        return cmd_undo(args.platform, args.project_dir)

    # platform specified
    if args.platform:
        return cmd_install(args.platform, args.project_dir)

    # No args at all — shouldn't reach here due to len(sys.argv)==1 check
    return interactive_mode()


if __name__ == '__main__':
    sys.exit(main() or 0)
