---
name: web-info
description: 1C web - check Apache, publications, web client, publication errors.
---

# $web-info — Статус Apache и публикаций 1С

Показывает состояние Apache HTTP Server, список опубликованных баз и последние ошибки.

## Usage

```
/web-info
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

## Формат вывода

```
=== Apache Web Server ===
Status: Запущен (PID: 12345)
Path:   C:\...\tools\apache24
Port:   8081
Module: C:/Program Files/1cv8/8.3.24.1691/bin/wsap24.dll

=== Опубликованные базы ===
  mydb   http://localhost:8081/mydb   File="C:\Bases\MyDB";

=== Последние ошибки ===
(пусто)
```

## Примеры

```bash
# Статус по умолчанию
python .agents/skills/epf-init/scripts/init.py

# Указать путь к Apache
python .agents/skills/epf-init/scripts/init.py -ApachePath "C:\tools\apache24"
```
