---
name: web-stop
description: 1C web - stop Apache HTTP Server and publications.
---

# /skill:web-stop — Остановка Apache

Останавливает Apache HTTP Server. Публикации сохраняются — при следующем `/skill:web-publish` сервер запустится снова.

## Usage

```
/web-stop
```

## Параметры подключения

Прочитай `.v8-project.json` из корня проекта. Если задан `webPath` — используй как `-ApachePath`.
По умолчанию `tools/apache24` от корня проекта.

## Команда

```powershell
python .agents/skills/epf-init/scripts/init.py <параметры>
```

### Параметры скрипта

| Параметр | Обязательный | Описание |
|----------|:------------:|----------|
| `-ApachePath <путь>` | нет | Корень Apache (по умолчанию `tools/apache24`) |

## После выполнения

Предложи пользователю:
- **Перезапуск** — `/skill:web-publish <база>` (повторный вызов поднимет Apache с существующими публикациями)
- **Удаление публикаций** — `/skill:web-unpublish <имя>` или `/skill:web-unpublish --all`

## Примеры

```powershell
# Остановить Apache
python .agents/skills/epf-init/scripts/init.py

# С указанием пути
python .agents/skills/epf-init/scripts/init.py -ApachePath "C:\tools\apache24"
```
