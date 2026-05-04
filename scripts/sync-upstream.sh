#!/bin/bash
# Синхронизация форка с upstream-репозиторием.
#
# Workflow:
#   1. main   — чистая копия upstream (не редактировать вручную)
#   2. custom — твои модификации (работай здесь)
#
# Использование:
#   ./scripts/sync-upstream.sh        # merge-стратегия (по умолчанию)
#   ./scripts/sync-upstream.sh rebase # rebase-стратегия

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

STRATEGY="${1:-merge}"
UPSTREAM_BRANCH="main"
LOCAL_MAIN="main"
LOCAL_CUSTOM="custom"

# Проверка наличия upstream remote
if ! git remote | grep -q "^upstream$"; then
    echo "❌ Remote 'upstream' не найден. Добавь его:"
    echo "   git remote add upstream https://github.com/Nikolay-Shirokov/cc-1c-skills.git"
    exit 1
fi

# Сохранение текущей ветки
CURRENT_BRANCH="$(git branch --show-current)"

cleanup() {
    if [[ "$CURRENT_BRANCH" != "$(git branch --show-current)" ]]; then
        echo "↩️  Возвращаюсь на ветку '$CURRENT_BRANCH'..."
        git checkout "$CURRENT_BRANCH" 2>/dev/null || true
    fi
}
trap cleanup EXIT

echo "🔄 Fetch upstream..."
git fetch upstream

echo "🔄 Синхронизация $LOCAL_MAIN с upstream/$UPSTREAM_BRANCH..."
git checkout "$LOCAL_MAIN"
git reset --hard "upstream/$UPSTREAM_BRANCH"

echo "🚀 Push $LOCAL_MAIN в origin..."
git push origin "$LOCAL_MAIN" --force-with-lease

echo "🔀 Переключение на $LOCAL_CUSTOM и применение $STRATEGY..."
git checkout "$LOCAL_CUSTOM"

if [[ "$STRATEGY" == "rebase" ]]; then
    git rebase "$LOCAL_MAIN"
else
    git merge "$LOCAL_MAIN" --no-edit
fi

echo "✅ Готово. Ветка '$LOCAL_CUSTOM' синхронизирована с upstream."
