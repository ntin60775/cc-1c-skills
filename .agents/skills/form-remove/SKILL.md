---
name: form-remove
description: 1C form - remove a form from a config object.
---

# /skill:form-remove — Удаление формы

Удаляет форму и убирает её регистрацию из корневого XML объекта.

## Usage

```
/form-remove <ObjectName> <FormName>
```

| Параметр   | Обязательный | По умолчанию | Описание                            |
|------------|:------------:|--------------|-------------------------------------|
| ObjectName | да           | —            | Имя объекта                         |
| FormName   | да           | —            | Имя формы для удаления              |
| SrcDir     | нет          | `src`        | Каталог исходников                  |

## Команда

```powershell
python .agents/skills/epf-init/scripts/init.py -ObjectName "<ObjectName>" -FormName "<FormName>" [-SrcDir "<SrcDir>"]
```

## Что удаляется

```
<SrcDir>/<ObjectName>/Forms/<FormName>.xml     # Метаданные формы
<SrcDir>/<ObjectName>/Forms/<FormName>/         # Каталог формы (рекурсивно)
```

## Что модифицируется

- `<SrcDir>/<ObjectName>.xml` — убирается `<Form>` из `ChildObjects`
- Если удаляемая форма была DefaultForm — очищается значение DefaultForm
