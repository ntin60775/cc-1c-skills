# SDD: Адаптация cc-1c-skills под Kimi Code CLI

## 1. Проблема

Навыки cc-1c-skills созданы для Claude Code (`.claude/skills/`). Kimi Code CLI:
- Использует путь `.kimi/skills/` (или fallback на `.claude/skills/`)
- Не поддерживает короткие слеш-команды (`/epf-init`) — только `/skill:epf-init`
- Работает на Linux, где PowerShell недоступен
- Игнорирует `allowed-tools` и `argument-hint` в frontmatter

## 2. Целевая архитектура

```
.kimi/skills/           ← навыки для Kimi CLI (копия/адаптация .claude/skills/)
├── epf-init/
│   ├── SKILL.md        ← адаптированный frontmatter + пути
│   └── scripts/
│       └── epf-init.py  ← только Python (без .ps1)
...
```

## 3. Ключевые решения

### 3.1 Рантайм
- **Только Python** — удалить все `.ps1` файлы
- `switch.py` для `kimi` платформы: `--runtime python` принудительно

### 3.2 Frontmatter
- Убрать `argument-hint` и `allowed-tools` (Kimi игнорирует, занимают контекст)
- Оставить `name`, `description`

### 3.3 Слеш-команды
- В SKILL.md заменить примеры: `/epf-init` → `/skill:epf-init`
- В заголовках оставить как есть (для читаемости), добавить примечание

### 3.4 Пути в SKILL.md
- Заменить абсолютные `.claude/skills/` на относительные `./`
- Или параметризовать через switch.py при копировании

### 3.5 AskUserQuestion
- Удалить из `allowed-tools` во всех SKILL.md
- Заменить на прямое описание запроса пользователю в тексте

## 4. Инварианты

- Все `.ps1` файлы должны быть удалены из `.claude/skills/`
- Каждый SKILL.md должен содержать только `name` и `description` в frontmatter
- Ни один SKILL.md не должен содержать `AskUserQuestion` в `allowed-tools`
- `switch.py` должен поддерживать `kimi` платформу
- Все Python-скрипты должны компилироваться без ошибок

## 5. Затронутые файлы

### 5.1 Глобальные
- `scripts/switch.py`
- `README.md`
- `.gitignore`

### 5.2 Все навыки (66 штук)
- `.claude/skills/*/SKILL.md`
- `.claude/skills/*/scripts/*.ps1` → удалить

### 5.3 Особое внимание (10 навыков с AskUserQuestion)
- `meta-remove/SKILL.md`
- `db-update/SKILL.md`
- `db-dump-xml/SKILL.md`
- `db-run/SKILL.md`
- `db-dump-cf/SKILL.md`
- `db-load-xml/SKILL.md`
- `db-load-cf/SKILL.md`
- `web-publish/SKILL.md`
- `db-create/SKILL.md`
- `db-load-git/SKILL.md`

## 6. Риски и смягчение

| Риск | Вероятность | Влияние | Смягчение |
|------|-------------|---------|-----------|
| Удаление .ps1 ломает Claude Code пользователей | Низкая | Среднее | Это наш форк, ориентирован на Kimi |
| Некоторые навыки требуют Windows/1С | Высокая | Низкое | Python-скрипты оставляем, документируем ограничение |
| Конфликты при будущем merge upstream | Средняя | Среднее | Использовать rerere, тщательно разрешать |

## 7. Acceptance Criteria

- [ ] `python scripts/switch.py kimi --runtime python --project-dir .` создаёт `.kimi/skills/`
- [ ] `find .claude/skills -name "*.ps1" | wc -l` → 0
- [ ] Все SKILL.md имеют frontmatter только с `name` и `description`
- [ ] Ни один SKILL.md не содержит `AskUserQuestion`
- [ ] README.md содержит инструкции для Kimi CLI
- [ ] `.gitignore` содержит `.kimi/skills/`
