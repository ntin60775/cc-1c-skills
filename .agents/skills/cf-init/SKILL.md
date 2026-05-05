---
name: cf-init
description: 1C config - create an empty XML scaffold.
---

# /skill:cf-init — Создание пустой конфигурации 1С

Создаёт scaffold исходников пустой конфигурации 1С: `Configuration.xml`, `Languages/Русский.xml`.

## Параметры и команда

| Параметр | Описание |
|----------|----------|
| `Name` | Имя конфигурации (обязат.) |
| `Synonym` | Синоним (= Name если не указан) |
| `OutputDir` | Каталог для создания (default: `src`) |
| `Version` | Версия конфигурации |
| `Vendor` | Поставщик |
| `CompatibilityMode` | Режим совместимости (default: `Version8_3_24`) |

```powershell
python .agents/skills/epf-init/scripts/init.py -Name "МояКонфигурация"
```

## Примеры

```powershell
# Базовая конфигурация
... -Name МояКонфигурация -Synonym "Моя конфигурация" -OutputDir test-tmp/cf

# С версией и поставщиком
... -Name TestCfg -Synonym "Тестовая" -Version "1.0.0.1" -Vendor "Фирма 1С" -OutputDir test-tmp/cf2

# Другой режим совместимости
... -Name TestCfg -CompatibilityMode Version8_3_27 -OutputDir test-tmp/cf3
```

## Верификация

```
/cf-init TestConfig -OutputDir test-tmp/cf
/skill:cf-info test-tmp/cf          — проверить созданное
/skill:cf-validate test-tmp/cf      — валидировать
```
