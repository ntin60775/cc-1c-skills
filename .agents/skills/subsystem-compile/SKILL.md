---
name: subsystem-compile
description: 1C subsystem - create XML section sources from JSON.
---

# $subsystem-compile — генерация подсистемы из JSON

Принимает JSON-определение подсистемы → генерирует XML + файловую структуру + регистрирует в родителе (Configuration.xml или родительская подсистема).

## Параметры и команда

| Параметр | Описание |
|----------|----------|
| `DefinitionFile` | Путь к JSON-файлу определения |
| `Value` | Инлайн JSON-строка (альтернатива DefinitionFile) |
| `OutputDir` | Корень выгрузки (где `Subsystems/`, `Configuration.xml`) |
| `Parent` | Путь к XML родительской подсистемы (для вложенных) |
| `NoValidate` | Пропустить авто-валидацию |

```bash
python '.agents/skills/subsystem-compile/scripts/subsystem-compile.py' -Value '<json>' -OutputDir '<ConfigDir>'
```

## JSON-определение

```json
{
  "name": "МояПодсистема",
  "synonym": "Моя подсистема",
  "comment": "",
  "includeInCommandInterface": true,
  "useOneCommand": false,
  "explanation": "Описание раздела",
  "picture": "CommonPicture.МояКартинка",
  "content": ["Catalog.Товары", "Document.Заказ"]
}
```

Минимально: только `name`. Остальное — дефолты.

## Примеры

```bash
# Минимальная подсистема
... -Value '{"name":"Тест"}' -OutputDir config/

# С составом и картинкой
... -Value '{"name":"Продажи","content":["Catalog.Товары","Report.Продажи"],"picture":"CommonPicture.Продажи"}' -OutputDir config/

# Вложенная подсистема
... -Value '{"name":"Дочерняя"}' -OutputDir config/ -Parent config/Subsystems/Продажи.xml
```

