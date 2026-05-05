---
name: form-validate
description: 1C form - validate Form.xml, BaseForm, callType, extension IDs.
---

# $form-validate — валидация управляемой формы 1С

Проверяет Form.xml на структурные ошибки: уникальность ID, наличие companion-элементов, корректность ссылок DataPath и команд.

## Параметры

| Параметр  | Обяз. | Умолч. | Описание                                |
|-----------|:-----:|---------|-----------------------------------------|
| FormPath  | да    | —       | Путь к файлу Form.xml                   |
| Detailed  | нет   | —       | Подробный вывод (все проверки, включая успешные) |
| MaxErrors | нет   | 30      | Остановиться после N ошибок              |

## Команда

```bash
python .agents/skills/form-validate/scripts/form-validate.py -FormPath "Catalogs/Номенклатура/Forms/ФормаЭлемента"
python .agents/skills/form-validate/scripts/form-validate.py -FormPath "src/МояОбработка/Forms/Форма/Ext/Form.xml"
```

