---
name: cfe-validate
description: 1C CFE extension - validate XML sources after create/edit.
---

# /skill:cfe-validate — валидация расширения конфигурации (CFE)

Проверяет структурную корректность расширения: XML-формат, свойства, состав, заимствованные объекты. Аналог `/skill:cf-validate`, но для расширений.

## Параметры

| Параметр      | Обяз. | Умолч. | Описание                                        |
|---------------|:-----:|---------|-------------------------------------------------|
| ExtensionPath | да    | —       | Путь к каталогу или Configuration.xml расширения |
| Detailed      | нет   | —       | Подробный вывод (все проверки, включая успешные)  |
| MaxErrors     | нет   | 30      | Остановиться после N ошибок                      |
| OutFile       | нет   | —       | Записать результат в файл                        |

## Команда

```powershell
python .agents/skills/epf-init/scripts/init.py -ExtensionPath "src"
python .agents/skills/epf-init/scripts/init.py -ExtensionPath "src/Configuration.xml"
```
