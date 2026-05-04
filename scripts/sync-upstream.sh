#!/bin/bash
# Синхронизация форка с upstream-репозиторием.
# 
# Workflow (main = рабочая ветка с доработками):
#   main — содержит все наши изменения + upstream через merge
#   upstream/main — отслеживаем, подтягиваем обновления через merge
#
# Использование:
#   ./scripts/sync-upstream.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

UPSTREAM_BRANCH="main"
LOCAL_MAIN="main"

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

echo "🔄 Merge upstream/$UPSTREAM_BRANCH в $LOCAL_MAIN..."
git checkout "$LOCAL_MAIN"
git merge "upstream/$UPSTREAM_BRANCH" --no-edit

echo "🚀 Push $LOCAL_MAIN в origin..."
git push origin "$LOCAL_MAIN"

echo "✅ Готово. $LOCAL_MAIN синхронизирован с upstream и запушен в origin."
