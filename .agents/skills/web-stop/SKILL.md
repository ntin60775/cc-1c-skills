---
name: web-stop
description: 1C web - stop Apache HTTP Server and publications.
---

# $web-stop — Остановка Apache

Останавливает Apache HTTP Server. Публикации сохраняются — при следующем `$web-publish` сервер запустится снова.

## Usage

```
/web-stop
```

## Параметры подключения

Прочитай `.v8-project.json` из корня проекта. Если задан `webPath` — используй как `-ApachePath`.
По умолчанию `tools/apache24` от корня проекта.

## Команда

```bash
python .agents/skills/epf-init/scripts/init.py <параметры>
```

### Параметры скрипта

| Параметр | Обязательный | Описание |
|----------|:------------:|----------|
| `-ApachePath <путь>` | нет | Корень Apache (по умолчанию `tools/apache24`) |

## После выполнения

Предложи пользователю:
- **Перезапуск** — `$web-publish <база>` (повторный вызов поднимет Apache с существующими публикациями)
- **Удаление публикаций** — `$web-unpublish <имя>` или `$web-unpublish --all`

## Примеры

```bash
# Остановить Apache
python .agents/skills/epf-init/scripts/init.py

# С указанием пути
python .agents/skills/epf-init/scripts/init.py -ApachePath "C:\tools\apache24"
```
