## Context

目前專案僅存在於本地 Windows 環境，需要遷移至 GitHub 以進行版本控制與公開展示。

## Goals / Non-Goals

**Goals:**
- 建立專業的遠端 GitHub 倉庫。
- 確保上傳的檔案皆為原始碼與必要資源，排除大型媒體與暫存檔。
- 提供清晰的 README 文件。

**Non-Goals:**
- 設定 GitHub Actions CI/CD（暫不實施）。
- 自動發布 Release 版本的二進位檔案。

## Decisions

### 1. 檔案排除策略 (.gitignore)
- **決策**: 建立自定義的 `.gitignore`。
- **理由**: 專案中包含 `.gemini`, `.claude` 等工具產生的暫存檔，以及 `Video/` (MP4) 與 `data/` (PNG/CSV) 等大型檔案，不宜直接推送至 GitHub 以維持倉庫輕量化。
- **替代方案**: 使用 `git lfs`（但這會增加維護複雜度，目前建議直接排除）。

### 2. 使用 GitHub CLI (`gh`)
- **決策**: 優先使用 `gh repo create` 自動化流程。
- **理由**: 比起手動在網頁建立後再關聯，`gh` 指令能更快速、準確地完成認證、命名與推送。

### 3. 文案語氣 (README)
- **決策**: 採用「專業正式 (Professional)」語氣。
- **理由**: 符合使用者對專案形象的要求，提升專業感。

## Risks / Trade-offs

- **[Risk] 誤傳敏感資訊**  **Mitigation**: 在執行 `git add .` 前，必須先完成並檢查 `.gitignore`。
- **[Risk] 檔案過大導致推送失敗**  **Mitigation**: 明確將 `Video/` 和 `data/` 排除。
