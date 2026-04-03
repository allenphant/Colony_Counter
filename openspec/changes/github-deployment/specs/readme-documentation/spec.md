## ADDED Requirements

### Requirement: Professional README Generation
系統必須以專業且正式 (Professional) 的語氣產生專案的 `README.md` 檔案。

#### Scenario: README Content Creation
- **WHEN** 提供專案概略、安裝步驟與使用方法時
- **THEN** 會產生一個結構完整且語句專業的 `README.md` 檔案

### Requirement: Repository Description
系統必須為 GitHub 倉庫設定簡短且專業的描述。

#### Scenario: Setting Description
- **WHEN** 執行 `gh repo create --description` 或相關指令時
- **THEN** GitHub 倉庫的「關於」區域會顯示專業的專案簡介
