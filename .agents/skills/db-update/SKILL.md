---
name: db-update
description: 1C DB - apply config with UpdateDBCfg.
---

# /skill:db-update — Обновление конфигурации БД

Применяет изменения основной конфигурации к конфигурации базы данных (`/skill:UpdateDBCfg`). Обязательный шаг после `/skill:db-load-cf`, `/skill:db-load-xml`, `/skill:db-load-git`.

## Usage

```
/db-update [database]
/db-update dev
/db-update dev -Dynamic+
```

## Параметры подключения

Прочитай `.v8-project.json` из корня проекта. Возьми `v8path` (путь к платформе) и разреши базу:
1. Если пользователь указал параметры подключения (путь, сервер) — используй напрямую
2. Если указал базу по имени — ищи по id / alias / name в `.v8-project.json`
3. Если не указал — сопоставь текущую ветку Git с `databases[].branches`
4. Если ветка не совпала — используй `default`
Если `v8path` не задан — автоопределение: `Get-ChildItem "C:\Program Files\1cv8\*\bin\1cv8.exe" | Sort -Desc | Select -First 1`
Если файла нет — предложи `/skill:db-list add`.
Если использованная база не зарегистрирована — после выполнения предложи добавить через `/skill:db-list add`.

## Команда

```powershell
python .agents/skills/epf-init/scripts/init.py <параметры>
```

### Параметры скрипта

| Параметр | Обязательный | Описание |
|----------|:------------:|----------|
| `-V8Path <путь>` | нет | Каталог bin платформы (или полный путь к 1cv8.exe) |
| `-InfoBasePath <путь>` | * | Файловая база |
| `-InfoBaseServer <сервер>` | * | Сервер 1С (для серверной базы) |
| `-InfoBaseRef <имя>` | * | Имя базы на сервере |
| `-UserName <имя>` | нет | Имя пользователя |
| `-Password <пароль>` | нет | Пароль |
| `-Extension <имя>` | нет | Обновить расширение |
| `-AllExtensions` | нет | Обновить все расширения |
| `-Dynamic <+/skill:->` | нет | `+` — динамическое обновление, `-` — отключить |
| `-Server` | нет | Обновление на стороне сервера |
| `-WarningsAsErrors` | нет | Предупреждения считать ошибками |

> `*` — нужен либо `-InfoBasePath`, либо пара `-InfoBaseServer` + `-InfoBaseRef`

### Фоновое обновление (серверная база)

| Параметр | Описание |
|----------|----------|
| `-BackgroundStart` | Начать фоновое обновление |
| `-BackgroundFinish` | Дождаться окончания |
| `-BackgroundCancel` | Отменить |
| `-BackgroundSuspend` | Приостановить |
| `-BackgroundResume` | Возобновить |

## Коды возврата

| Код | Описание |
|-----|----------|
| 0 | Успешно |
| 1 | Ошибка (см. лог) |

## Предупреждения

- Если обновление **не динамическое** — потребуется **монопольный доступ** к базе (все пользователи должны выйти)
- Для серверных баз рекомендуется `-Dynamic+` для обновления без остановки
- Если структура данных существенно изменилась (удаление реквизитов, изменение типов) — динамическое обновление может быть невозможно

## Примеры

```powershell
# Обычное обновление (файловая база)
python .agents/skills/epf-init/scripts/init.py -InfoBasePath "C:\Bases\MyDB" -UserName "Admin"

# Динамическое обновление (серверная база)
python .agents/skills/epf-init/scripts/init.py -InfoBaseServer "srv01" -InfoBaseRef "MyDB" -UserName "Admin" -Password "secret" -Dynamic "+"

# Обновление расширения
python .agents/skills/epf-init/scripts/init.py -InfoBasePath "C:\Bases\MyDB" -UserName "Admin" -Extension "МоёРасширение"
```
